"""Read source files as text only. Never import or execute the target application."""
import ast
import hashlib
import json
import re
import subprocess
from pathlib import Path

from . import settings, store

ALIASES = {
    '提现': 'withdraw withdrawal wallet', '充值': 'deposit wallet',
    '兑换': 'swap exchange', '闪兑': 'swap exchange', '询价': 'quote swap',
    '安全': 'security auth', '认证': 'auth kyc', '登录': 'login signin auth',
    '账户': 'account user', '用户': 'user account', '资产': 'asset balance',
    '订单': 'order orders', '交易': 'trade order exchange', '手续费': 'fee',
    '并发': 'lock concurrent', '锁': 'lock', '测试': 'test pytest',
    '风控': 'risk control', '杠杆': 'margin loan', '合约': 'perpetual',
    '通知': 'notice message push', '营销': 'activity mission',
    '理财': 'investment staking', '子账户': 'sub account', '密码': 'password',
    '分页': 'page limit paginate', '冻结': 'freeze frozen', '钱包': 'wallet',
    '接口': 'api resource', '报价': 'quote', '状态': 'status',
}
DOMAINS = [
    ('account', '账户与身份', ('user', 'account', 'auth', 'login', 'kyc')),
    ('security', '安全设置与风控', ('security', 'password', 'risk', 'anti_fraud', 'webauthn')),
    ('assets', '资产、充值与提现', ('asset', 'wallet', 'deposit', 'withdraw', 'balance')),
    ('exchange', '兑换与闪兑', ('swap', 'exchange')),
    ('trading', '现货与市场', ('spot', 'market', 'order', 'trade', 'kline', 'fee')),
    ('margin', '杠杆与借贷', ('margin', 'loan', 'credit', 'pledge')),
    ('perpetual', '合约业务', ('perpetual',)),
    ('p2p', '法币与 P2P', ('p2p', 'fiat', 'payment')),
    ('investment', '理财与策略', ('investment', 'staking', 'strategy', 'amm')),
    ('operation', '运营与消息', ('activity', 'mission', 'push', 'notice', 'message', 'operation', 'refer')),
]


def module_for(path):
    name = path.lower()
    inventory = re.search(r'inventory-([a-z]+)\.md', name)
    if inventory and inventory.group(1) in {d[0] for d in DOMAINS}:
        return inventory.group(1)
    name += ' ' + ' '.join(value for key, value in ALIASES.items() if key in name)
    # Prioritize distinctive business names over a parent directory such as assets.
    for key in ('exchange', 'perpetual', 'p2p', 'margin', 'investment', 'security'):
        domain = next(d for d in DOMAINS if d[0] == key)
        if any(word in name for word in domain[2]):
            return key
    for key, _, words in DOMAINS:
        if any(word in name for word in words):
            return key
    return 'platform'


def tokens(text):
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text).lower()
    out = re.findall(r'[a-z0-9]+', text)
    for run in re.findall(r'[\u4e00-\u9fff]+', text):
        out.append(run)
        out.extend(run[i:i+2] for i in range(len(run)-1))
    return list(dict.fromkeys(out))


def query_tokens(query):
    extra = ' '.join(value for key, value in ALIASES.items() if key in query)
    return tokens(query + ' ' + extra)[:60]


def safe_files():
    result = subprocess.run(['git', '-C', str(settings.REPO), 'ls-files', '-z'],
                            capture_output=True, check=True)
    for raw in result.stdout.decode().split('\0'):
        if not raw:
            continue
        rel = Path(raw)
        allowed = (raw.startswith(('app/', 'tests/', 'docs/architecture/', 'migrations/versions/'))
                   and rel.suffix in ('.py', '.md', '.mmd')) or raw == 'README.md'
        if not allowed or any(p in {'config', 'translations', '__pycache__'} for p in rel.parts):
            continue
        if any(word in rel.name.lower() for word in ('.env', 'credential', 'secret', 'private_key')):
            continue
        path = settings.REPO / rel
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(settings.REPO):
            continue
        if path.stat().st_size > 800_000:
            continue
        yield raw, path


def redact(text):
    text = re.sub(r'(?is)-----BEGIN [^-]*PRIVATE KEY-----.*?-----END [^-]*PRIVATE KEY-----', lambda m: '[REDACTED PRIVATE KEY]' + '\n' * m.group().count('\n'), text)
    text = re.sub(r'(?i)(\b(?:api_key|secret_key|access_token|password|client_secret)\s*=\s*)[\'\"][^\'\"\n]+[\'\"]', r'\1"[REDACTED]"', text)
    text = re.sub(r'\bsk-[A-Za-z0-9_-]{20,}\b', '[REDACTED]', text)
    return text


def source_chunks(path, content):
    lines = content.splitlines()
    if not lines:
        return []
    spans = []
    if path.endswith('.py'):
        try:
            tree = ast.parse(content)
            for node in tree.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    start = min([node.lineno] + [d.lineno for d in node.decorator_list])
                    spans.append((node.name, start, node.end_lineno))
                elif isinstance(node, ast.ClassDef):
                    methods = [n for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
                    if methods:
                        first = min([methods[0].lineno] + [d.lineno for d in methods[0].decorator_list])
                        spans.append((node.name, min([node.lineno] + [d.lineno for d in node.decorator_list]), max(first-1, node.lineno)))
                        for method in methods:
                            start = min([method.lineno] + [d.lineno for d in method.decorator_list])
                            spans.append((node.name + '.' + method.name, start, method.end_lineno))
                    else:
                        spans.append((node.name, node.lineno, node.end_lineno))
            if spans and spans[0][1] > 1:
                spans.insert(0, ('模块导入与常量', 1, spans[0][1]-1))
        except SyntaxError:
            pass
    if not spans:
        spans = [(Path(path).stem, 1, len(lines))]
    # Preserve uncovered top-level assignments as searchable context.
    covered = set()
    for _, start, end in spans:
        covered.update(range(start, end+1))
    gap = None
    for n in range(1, len(lines)+2):
        if n <= len(lines) and n not in covered:
            gap = gap or n
        elif gap:
            if any(line.strip() for line in lines[gap-1:n-1]):
                spans.append(('模块上下文', gap, n-1))
            gap = None
    result = []
    for symbol, start, end in spans:
        for a in range(start, end+1, 100):
            b = min(a+119, end)
            text = '\n'.join(lines[a-1:b])
            if text.strip():
                result.append((symbol, a, b, text))
            if b == end:
                break
    return result


def sync():
    if not (settings.REPO / '.git').exists():
        raise ValueError('代码目录不是 Git 仓库，请检查 KNOWLEDGE_REPO')
    head = subprocess.check_output(['git', '-C', str(settings.REPO), 'rev-parse', 'HEAD'], text=True).strip()
    files = []
    for path, actual in safe_files():
        files.append((path, redact(actual.read_text(errors='replace')), 'test' if path.startswith('tests/') else ('code' if path.endswith('.py') else 'reference')))
    for actual in sorted(settings.DOCS.glob('*.md')):
        if not actual.is_symlink():
            files.append(('requirements/' + actual.name, actual.read_text(), 'requirement'))
    with store.connect() as db:
        db.execute('UPDATE sources SET active=0')
        added = 0
        manifest = hashlib.sha256()
        for path, content, kind in files:
            digest = hashlib.sha256(content.encode()).hexdigest()
            manifest.update((path + digest).encode())
            version = '文档草稿 · ' + digest[:8] if kind == 'requirement' else head[:12] + ' · ' + digest[:8]
            sid = hashlib.sha256((path + digest + (head if kind != 'requirement' else '')).encode()).hexdigest()[:24]
            title = next((line.lstrip('# ').strip() for line in content.splitlines() if line.startswith('# ')), Path(path).name) if kind in ('requirement', 'reference') else Path(path).name
            module = module_for(path + ' ' + title)
            if db.execute('SELECT 1 FROM sources WHERE id=?', (sid,)).fetchone():
                db.execute('UPDATE sources SET active=1,module=? WHERE id=?', (module, sid))
                continue
            db.execute('INSERT INTO sources VALUES (?,?,?,?,?,?,?,?,?,?)', (sid, path, title, kind, module, content, digest, version, 1, store.now()))
            for symbol, start, end, text in source_chunks(path, content):
                cur = db.execute('INSERT INTO chunks(source_id,symbol,start_line,end_line,content) VALUES (?,?,?,?,?)', (sid, symbol, start, end, text))
                db.execute('INSERT INTO search_index(rowid,title,body) VALUES (?,?,?)', (cur.lastrowid, ' '.join(tokens(path+' '+title+' '+symbol)), ' '.join(tokens(text))))
            added += 1
        result = {'synced_at': store.now(), 'commit': head, 'snapshot': manifest.hexdigest()[:12], 'files': len(files), 'added': added, 'repo': str(settings.REPO), 'basis': '已跟踪文件的当前工作区快照；内容哈希区分未提交修改'}
        db.execute('INSERT OR REPLACE INTO metadata VALUES (?,?)', ('sync', json.dumps(result)))
    return result


def search(query, limit=12, kind=None, module=None):
    terms = query_tokens(query)
    if not terms:
        return []
    match = ' OR '.join('"'+t.replace('"','')+'"' for t in terms)
    where = ' AND s.kind=?' if kind else ''
    if module:
        where += ' AND s.module=?'
    params = [match] + ([kind] if kind else []) + ([module] if module else []) + [min(limit*6, 120)]
    sql = '''SELECT c.id AS chunk_id,c.symbol,c.start_line,c.end_line,c.content,
      s.id AS source_id,s.path,s.title,s.kind,s.module,s.version,
      bm25(search_index, 5.0, 1.0) AS score
      FROM search_index JOIN chunks c ON c.id=search_index.rowid
      JOIN sources s ON s.id=c.source_id
      WHERE search_index MATCH ? AND s.active=1''' + where + ' ORDER BY score LIMIT ?'
    found = store.rows(sql, params)
    # Keep up to three chunks per file, avoiding one large file crowding out others.
    selected, counts = [], {}
    for item in found:
        count = counts.get(item['source_id'], 0)
        if count >= 3:
            continue
        counts[item['source_id']] = count+1
        selected.append(item)
        if len(selected) == limit:
            break
    return selected
