import asyncio
import json
import subprocess
import time

import pytest
from fastapi.testclient import TestClient

from backend import agent, indexer, settings, store
from backend.main import app


@pytest.fixture
def workspace(tmp_path, monkeypatch):
    repo = tmp_path / 'repo'
    repo.mkdir()
    docs = tmp_path / 'docs'
    docs.mkdir()
    for name, value in {'REPO': repo, 'DATA': tmp_path / 'data', 'DB': tmp_path / 'data' / 'test.sqlite3', 'DOCS': docs}.items():
        monkeypatch.setattr(settings, name, value)
    monkeypatch.setattr(agent, 'gate', asyncio.Semaphore(1))
    monkeypatch.setattr(agent, 'tasks', {})
    subprocess.run(['git', 'init', '-q', str(repo)], check=True)
    (repo / 'app' / 'business').mkdir(parents=True)
    (repo / 'app' / 'config').mkdir()
    (repo / 'tests').mkdir()
    (repo / 'app' / 'business' / 'swap.py').write_text('''"""兑换业务"""
API_KEY = "not-a-real-key-for-test"

def submit_swap(amount):
    """兑换订单，需要正数金额。"""
    if amount <= 0:
        raise ValueError("amount")
    return {"status": "PROCESSING"}
''')
    (repo / 'tests' / 'test_swap.py').write_text('def test_positive_amount():\n    """兑换数量校验"""\n    assert True\n')
    (repo / 'app' / 'config' / 'prod.py').write_text('SECRET = "must-not-be-indexed"')
    (repo / 'app' / 'business' / 'escape.py').symlink_to('/etc/hosts')
    (docs / 'exchange.md').write_text('# 兑换需求草稿\n\n兑换订单需校验正数金额。\n')
    subprocess.run(['git', '-C', str(repo), 'add', '.'], check=True)
    subprocess.run(['git', '-C', str(repo), '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'fixture'], check=True)
    store.init()
    indexer.sync()
    return repo


def test_only_allowlisted_files_and_redaction(workspace):
    paths = [r['path'] for r in store.rows('SELECT path FROM sources')]
    assert 'app/config/prod.py' not in paths
    assert 'app/business/escape.py' not in paths
    body = store.one("SELECT content FROM sources WHERE path='app/business/swap.py'")['content']
    assert 'not-a-real-key-for-test' not in body
    assert '[REDACTED]' in body


def test_snapshot_citations_survive_update_and_delete(workspace):
    old = indexer.search('submit_swap', 1)[0]
    initial_count = store.one('SELECT COUNT(*) AS n FROM chunks')['n']
    assert indexer.sync()['added'] == 0
    assert store.one('SELECT COUNT(*) AS n FROM chunks')['n'] == initial_count
    path = workspace / 'app/business/swap.py'
    path.write_text(path.read_text().replace('PROCESSING', 'FINISHED'))
    indexer.sync()
    new = next(r for r in indexer.search('submit_swap') if r['path'].endswith('business/swap.py'))
    assert new['source_id'] != old['source_id']
    previous = store.one('SELECT * FROM sources WHERE id=?', (old['source_id'],))
    assert previous['active'] == 0
    assert 'PROCESSING' in previous['content']
    path.unlink()
    indexer.sync()
    assert not any(r['path'].endswith('business/swap.py') for r in indexer.search('submit_swap'))
    assert store.one('SELECT id FROM sources WHERE id=?', (old['source_id'],))


def test_chinese_queries_and_exact_line_evidence(workspace):
    hits = indexer.search('兑换订单')
    assert hits
    assert any(h['kind'] == 'requirement' for h in hits)
    hit = next(h for h in hits if h['symbol'] == 'submit_swap')
    content = store.one('SELECT content FROM sources WHERE id=?', (hit['source_id'],))['content']
    assert hit['content'] == '\n'.join(content.splitlines()[hit['start_line']-1:hit['end_line']])
    assert indexer.search('" OR * ( DROP TABLE sources') == []


def wait_done(client, jid):
    for _ in range(100):
        current = client.get('/api/jobs/' + jid).json()
        if current['status'] not in ('queued', 'running'):
            return current
        time.sleep(.03)
    raise AssertionError('job did not complete')


def test_end_to_end_answer_history_and_save(workspace, monkeypatch):
    async def fake(prompt):
        assert '证据开始' in prompt and 'submit_swap' in prompt
        return '兑换订单需要正数金额。[S1]\n\n无效证据 [S999]'
    monkeypatch.setattr(agent, 'call_codex', fake)
    with TestClient(app) as client:
        cid = client.post('/api/conversations', json={'mode': 'code'}).json()['id']
        response = client.post(f'/api/conversations/{cid}/messages', json={'content': '兑换订单 submit_swap 的规则是什么？', 'mode': 'code'})
        assert response.status_code == 202
        jid = response.json()['id']
        assert wait_done(client, jid)['status'] == 'done'
        data = client.get('/api/conversations/'+cid).json()
        assert len(data['messages']) == 2
        answer = data['messages'][-1]
        assert '引用无效' in answer['content']
        assert answer['sources']
        saved = client.post('/api/messages/'+answer['id']+'/save', json={'title': '兑换规则'})
        assert saved.status_code == 200
        doc = client.get('/api/sources/'+saved.json()['id']).json()
        assert '尚未经过产品或研发确认' in doc['content']
        assert '/api/sources/' in doc['content']
        assert client.get('/api/conversations').json()[0]['id'] == cid
        with client.stream('GET', '/api/jobs/'+jid+'/events') as events:
            assert '"status": "done"' in ''.join(events.iter_text())


def test_duplicate_send_and_cancellation(workspace, monkeypatch):
    async def waiting(prompt):
        await asyncio.sleep(60)
    monkeypatch.setattr(agent, 'call_codex', waiting)
    with TestClient(app) as client:
        cid = client.post('/api/conversations', json={}).json()['id']
        first = client.post(f'/api/conversations/{cid}/messages', json={'content': '兑换'})
        assert first.status_code == 202
        assert client.post(f'/api/conversations/{cid}/messages', json={'content': '重复'}).status_code == 409
        jid = first.json()['id']
        cancelled = client.post('/api/jobs/'+jid+'/cancel', json={}).json()
        assert cancelled['status'] == 'cancelled'
        assert len(client.get('/api/conversations/'+cid).json()['messages']) == 1


def test_model_failure_is_not_a_fabricated_answer(workspace, monkeypatch):
    async def fails(prompt):
        raise RuntimeError('模型暂不可用')
    monkeypatch.setattr(agent, 'call_codex', fails)
    with TestClient(app) as client:
        cid = client.post('/api/conversations', json={}).json()['id']
        jid = client.post(f'/api/conversations/{cid}/messages', json={'content': '兑换'}).json()['id']
        assert wait_done(client, jid)['error'] == '模型暂不可用'
        assert len(client.get('/api/conversations/'+cid).json()['messages']) == 1


def test_local_origin_and_input_validation(workspace):
    with TestClient(app) as client:
        assert client.post('/api/conversations', json={}, headers={'Origin': 'https://evil.example'}).status_code == 403
        assert client.post('/api/conversations', content='{}', headers={'Content-Type': 'text/plain'}).status_code == 415
        assert client.post('/api/conversations', json={'mode': 'shell'}).status_code == 400
        cid = client.post('/api/conversations', json={}).json()['id']
        assert client.post(f'/api/conversations/{cid}/messages', json={'content': '  '}).status_code == 400
        assert client.get('/api/sources/does-not-exist').status_code == 404
        assert client.get('/api/status', headers={'Host': 'evil.example'}).status_code == 400


def test_restart_marks_incomplete_jobs(workspace):
    with store.connect() as db:
        db.execute('INSERT INTO jobs VALUES (?,?,?,?,?,?,?,?)', ('pending', None, 'sync', 'running', '同步中', None, store.now(), store.now()))
    store.init()
    assert store.one('SELECT status FROM jobs WHERE id=?', ('pending',))['status'] == 'error'


def test_sync_endpoint_and_pagination(workspace):
    with TestClient(app) as client:
        response = client.post('/api/sync', json={})
        assert response.status_code == 202
        assert wait_done(client, response.json()['id'])['status'] == 'done'
        first = client.get('/api/sources?limit=2').json()
        second = client.get('/api/sources?limit=2&offset=2').json()
        assert first['total'] > 4
        assert {s['id'] for s in first['items']}.isdisjoint(s['id'] for s in second['items'])
        docs = client.get('/api/sources?kind=requirement').json()
        assert all(s['kind'] == 'requirement' for s in docs['items'])
        assert any(s['path'].endswith('00-overview.md') for s in docs['items'])


def test_secret_redaction_preserves_source_line_numbers():
    source = 'before\n-----BEGIN PRIVATE KEY-----\nsecret\n-----END PRIVATE KEY-----\nafter'
    redacted = indexer.redact(source)
    assert 'secret' not in redacted
    assert source.count('\n') == redacted.count('\n')
    assert redacted.splitlines()[-1] == 'after'
