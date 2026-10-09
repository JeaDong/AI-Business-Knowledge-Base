#!/bin/sh
set -eu
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
fi
if ! .venv/bin/python -c 'import fastapi, uvicorn' >/dev/null 2>&1; then
  .venv/bin/pip install -r requirements.lock.txt
fi
if [ ! -d frontend/node_modules ]; then
  (cd frontend && npm ci)
fi
(cd frontend && npm run build)
if [ ! -f data/knowledge.sqlite3 ]; then
  .venv/bin/python -m backend.bootstrap
fi
exec .venv/bin/python run.py
