import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO = Path(os.environ.get('KNOWLEDGE_REPO', str(ROOT.parent / 'coinex_backend'))).resolve()
DATA = Path(os.environ.get('KNOWLEDGE_DATA', str(ROOT / 'data'))).resolve()
DOCS = ROOT / 'docs' / 'requirements'
DB = DATA / 'knowledge.sqlite3'
CODEX_BIN = os.environ.get('CODEX_BIN', 'codex')
MODEL = os.environ.get('CODEX_MODEL', '')
TIMEOUT = int(os.environ.get('CODEX_TIMEOUT', '240'))
PORT = int(os.environ.get('PORT', '8765'))
