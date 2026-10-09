import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone

from . import settings


def now():
    return datetime.now(timezone.utc).isoformat()


@contextmanager
def connect():
    settings.DATA.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(settings.DB, timeout=30)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA foreign_keys=ON')
    try:
        yield db
        db.commit()
    except BaseException:
        db.rollback()
        raise
    finally:
        db.close()


def init():
    with connect() as db:
        db.execute('PRAGMA journal_mode=WAL')
        db.executescript('''
        CREATE TABLE IF NOT EXISTS sources (
          id TEXT PRIMARY KEY, path TEXT NOT NULL, title TEXT NOT NULL,
          kind TEXT NOT NULL, module TEXT NOT NULL, content TEXT NOT NULL,
          digest TEXT NOT NULL, version TEXT NOT NULL, active INTEGER NOT NULL DEFAULT 1,
          created_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS sources_active ON sources(active, kind, module);
        CREATE TABLE IF NOT EXISTS chunks (
          id INTEGER PRIMARY KEY, source_id TEXT NOT NULL REFERENCES sources(id),
          symbol TEXT NOT NULL, start_line INTEGER NOT NULL, end_line INTEGER NOT NULL,
          content TEXT NOT NULL
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS search_index USING fts5(
          title, body, tokenize='unicode61'
        );
        CREATE TABLE IF NOT EXISTS conversations (
          id TEXT PRIMARY KEY, title TEXT NOT NULL, mode TEXT NOT NULL,
          created_at TEXT NOT NULL, updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS messages (
          id TEXT PRIMARY KEY, conversation_id TEXT NOT NULL REFERENCES conversations(id),
          role TEXT NOT NULL, content TEXT NOT NULL, sources TEXT NOT NULL DEFAULT '[]',
          created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS jobs (
          id TEXT PRIMARY KEY, conversation_id TEXT REFERENCES conversations(id),
          kind TEXT NOT NULL, status TEXT NOT NULL, stage TEXT NOT NULL,
          error TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        ''')
        db.execute("UPDATE jobs SET status='error', stage='服务重启，任务已中断', error='请重新发送问题', updated_at=? WHERE status IN ('queued','running')", (now(),))


def rows(sql, params=()):
    with connect() as db:
        return [dict(x) for x in db.execute(sql, params).fetchall()]


def one(sql, params=()):
    result = rows(sql, params)
    return result[0] if result else None


def update_job(job_id, status, stage, error=None):
    with connect() as db:
        db.execute('UPDATE jobs SET status=?, stage=?, error=?, updated_at=? WHERE id=?',
                   (status, stage, error, now(), job_id))


def meta(key, default=None):
    item = one('SELECT value FROM metadata WHERE key=?', (key,))
    return json.loads(item['value']) if item else default
