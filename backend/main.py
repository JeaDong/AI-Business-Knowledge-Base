import asyncio
import json
import re
import uuid
from contextlib import asynccontextmanager
from urllib.parse import urlparse

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from starlette.middleware.trustedhost import TrustedHostMiddleware

from . import agent, bootstrap, indexer, settings, store

sync_lock = asyncio.Lock()


@asynccontextmanager
async def lifespan(app):
    store.init()
    yield
    pending = list(agent.tasks.values())
    for task in pending:
        task.cancel()
    if pending:
        await asyncio.gather(*pending, return_exceptions=True)


app = FastAPI(title='知间 · 研发知识库', lifespan=lifespan)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=['127.0.0.1', 'localhost', '[::1]', 'testserver'])


@app.middleware('http')
async def local_boundary(request: Request, call_next):
    # Browser requests from another site must not spend Codex quota or mutate local data.
    if request.method not in ('GET', 'HEAD', 'OPTIONS'):
        origin = request.headers.get('origin')
        if (origin and urlparse(origin).netloc != request.headers.get('host')) or request.headers.get('sec-fetch-site') == 'cross-site':
            return JSONResponse({'detail': '仅接受当前工作台发起的请求'}, status_code=403)
        if not request.headers.get('content-type', '').startswith('application/json'):
            return JSONResponse({'detail': '需要 application/json'}, status_code=415)
    response = await call_next(request)
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'no-referrer'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; object-src 'none'; frame-ancestors 'none'"
    if request.url.path in ('/docs', '/redoc'):
        response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https://fastapi.tiangolo.com; connect-src 'self'; worker-src blob:; frame-ancestors 'none'"
    return response


@app.get('/api/status')
async def status():
    counts = store.rows('SELECT kind, COUNT(*) AS count FROM sources WHERE active=1 GROUP BY kind')
    return {'name': 'coinex_backend', 'repo': str(settings.REPO), 'counts': {x['kind']: x['count'] for x in counts},
            'sync': store.meta('sync'), 'codex': await agent.auth_status(),
            'jobs': store.rows("SELECT * FROM jobs WHERE status IN ('queued','running') ORDER BY created_at")}


async def sync_job(jid):
    try:
        async with sync_lock:
            store.update_job(jid, 'running', '正在同步代码与文档')
            await asyncio.to_thread(bootstrap.generate)
            await asyncio.to_thread(indexer.sync)
            store.update_job(jid, 'done', '知识库已更新')
    except Exception as exc:
        store.update_job(jid, 'error', '同步失败', str(exc)[:400])
    finally:
        agent.tasks.pop(jid, None)


@app.post('/api/sync', status_code=202)
async def sync():
    current = store.one("SELECT id FROM jobs WHERE kind='sync' AND status IN ('queued','running')")
    if current:
        return current
    jid = uuid.uuid4().hex
    with store.connect() as db:
        db.execute('INSERT INTO jobs VALUES (?,?,?,?,?,?,?,?)', (jid, None, 'sync', 'queued', '等待同步', None, store.now(), store.now()))
    agent.tasks[jid] = asyncio.create_task(sync_job(jid))
    return {'id': jid}


@app.get('/api/sources')
def sources(q: str = '', kind: str = '', module: str = '', limit: int = 100, offset: int = 0):
    conditions, params = ['active=1'], []
    if q:
        conditions.append('(path LIKE ? OR title LIKE ?)')
        params += ['%'+q+'%']*2
    if kind:
        conditions.append('kind=?')
        params.append(kind)
    if module:
        conditions.append('module=?')
        params.append(module)
    where = ' AND '.join(conditions)
    items = store.rows('SELECT id,path,title,kind,module,version,created_at FROM sources WHERE '+where+' ORDER BY kind DESC,path LIMIT ? OFFSET ?', params+[max(1,min(limit,200)),max(0,offset)])
    total = store.one('SELECT COUNT(*) AS count FROM sources WHERE '+where, params)['count']
    return {'items': items, 'total': total}


@app.get('/api/sources/{sid}')
def source(sid: str):
    result = store.one('SELECT * FROM sources WHERE id=?', (sid,))
    if not result:
        raise HTTPException(404, '资料不存在')
    return result


@app.get('/api/search')
def search(q: str, kind: str | None = None, module: str | None = None):
    if len(q) > 2000:
        raise HTTPException(400, '搜索内容过长')
    return {'items': indexer.search(q, 20, kind or None, module or None)}


@app.get('/api/conversations')
def conversations():
    return store.rows('SELECT * FROM conversations ORDER BY updated_at DESC LIMIT 200')


class ConversationInput(BaseModel):
    mode: str = 'ask'


@app.post('/api/conversations', status_code=201)
def new_conversation(body: ConversationInput):
    if body.mode not in agent.MODES:
        raise HTTPException(400, '未知分析类型')
    cid = uuid.uuid4().hex
    with store.connect() as db:
        db.execute('INSERT INTO conversations VALUES (?,?,?,?,?)', (cid, '新对话', body.mode, store.now(), store.now()))
    return {'id': cid}


@app.get('/api/conversations/{cid}')
def conversation(cid: str):
    row = store.one('SELECT * FROM conversations WHERE id=?', (cid,))
    if not row:
        raise HTTPException(404, '对话不存在')
    messages = store.rows('SELECT * FROM messages WHERE conversation_id=? ORDER BY created_at', (cid,))
    for m in messages:
        m['sources'] = json.loads(m['sources'])
    return {**row, 'messages': messages, 'job': store.one('SELECT * FROM jobs WHERE conversation_id=? ORDER BY created_at DESC LIMIT 1', (cid,))}


class MessageInput(BaseModel):
    content: str = Field(min_length=1, max_length=12000)
    mode: str = 'ask'


@app.post('/api/conversations/{cid}/messages', status_code=202)
async def message(cid: str, body: MessageInput):
    if body.mode not in agent.MODES or not body.content.strip():
        raise HTTPException(400, '请输入问题并选择分析类型')
    if not store.one('SELECT id FROM conversations WHERE id=?', (cid,)):
        raise HTTPException(404, '对话不存在')
    if not store.meta('sync'):
        raise HTTPException(409, '请先同步知识库')
    jid = uuid.uuid4().hex
    with store.connect() as db:
        db.execute('BEGIN IMMEDIATE')
        if db.execute("SELECT 1 FROM jobs WHERE conversation_id=? AND status IN ('running','queued')", (cid,)).fetchone():
            raise HTTPException(409, '当前对话正在分析中')
        if db.execute("SELECT count(*) FROM jobs WHERE kind='analysis' AND status IN ('running','queued')").fetchone()[0] >= 5:
            raise HTTPException(429, '任务队列已满，请稍后再试')
        db.execute('INSERT INTO messages VALUES (?,?,?,?,?,?)', (uuid.uuid4().hex, cid, 'user', body.content.strip(), '[]', store.now()))
        db.execute("UPDATE conversations SET title=CASE WHEN title='新对话' THEN ? ELSE title END, mode=?,updated_at=? WHERE id=?", (body.content.strip()[:32], body.mode, store.now(), cid))
        db.execute('INSERT INTO jobs VALUES (?,?,?,?,?,?,?,?)', (jid, cid, 'analysis', 'queued', '等待 Codex 分析', None, store.now(), store.now()))
    agent.tasks[jid] = asyncio.create_task(agent.run(jid, cid, body.content.strip(), body.mode))
    return {'id': jid}


@app.get('/api/jobs/{jid}')
def job(jid: str):
    item = store.one('SELECT * FROM jobs WHERE id=?', (jid,))
    if not item:
        raise HTTPException(404, '任务不存在')
    return item


@app.get('/api/jobs/{jid}/events')
async def events(jid: str, request: Request):
    job(jid)
    async def stream():
        prev = ''
        while not await request.is_disconnected():
            current = job(jid)
            encoded = json.dumps(current, ensure_ascii=False)
            if encoded != prev:
                yield 'data: ' + encoded + '\n\n'
                prev = encoded
            else:
                yield ': heartbeat\n\n'
            if current['status'] not in ('running', 'queued'):
                break
            await asyncio.sleep(1)
    return StreamingResponse(stream(), media_type='text/event-stream', headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'})


@app.post('/api/jobs/{jid}/cancel')
async def cancel(jid: str):
    item = job(jid)
    if item['kind'] == 'sync':
        raise HTTPException(409, '同步正在提交快照，请等待完成')
    if task := agent.tasks.get(jid):
        task.cancel()
        await asyncio.gather(task, return_exceptions=True)
        store.update_job(jid, 'cancelled', '已停止分析')
    return job(jid)


class SaveInput(BaseModel):
    title: str = Field(min_length=1, max_length=100)


@app.post('/api/messages/{mid}/save')
async def save(mid: str, body: SaveInput):
    item = store.one("SELECT * FROM messages WHERE id=? AND role='assistant'", (mid,))
    if not item:
        raise HTTPException(404, '分析结果不存在')
    saved_id = 'analysis-' + mid
    path = settings.DOCS / (saved_id + '.md')
    title = body.title.replace('\n', ' ').replace('\r', ' ').strip()
    sources = json.loads(item['sources'])
    answer = item['content']
    for i, source in enumerate(sources, 1):
        answer = answer.replace(f'[S{i}]', f"[{source['path']}:{source['start_line']}](/api/sources/{source['source_id']})")
    text = f'# {title}\n\n> AI 分析草稿 · 尚未经过产品或研发确认\n> 保存时间：{store.now()}\n\n{answer}\n'
    async with sync_lock:
        settings.DOCS.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        await asyncio.to_thread(indexer.sync)
    row = store.one('SELECT id FROM sources WHERE path=? AND active=1', ('requirements/' + path.name,))
    return {'id': row['id']}


dist = settings.ROOT / 'frontend' / 'dist'
if dist.exists():
    app.mount('/assets', StaticFiles(directory=dist / 'assets'), name='assets')


@app.get('/favicon.svg')
def favicon():
    return FileResponse(settings.ROOT / 'frontend' / 'public' / 'favicon.svg')


@app.get('/')
def home():
    if not (dist / 'index.html').exists():
        raise HTTPException(503, '请先构建前端：cd frontend && npm install && npm run build')
    return FileResponse(dist / 'index.html')
