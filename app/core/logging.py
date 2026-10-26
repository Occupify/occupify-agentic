import asyncio
import json
import logging
import sys
import threading
from collections import deque
from contextvars import ContextVar
from datetime import UTC, datetime
from typing import Any

from app.core.config import get_settings

_LOG_BUFFER_MAX = 1000
_log_buffer: deque[dict[str, Any]] = deque(maxlen=_LOG_BUFFER_MAX)
_subscribers: set["LogSubscriber"] = set()
_log_lock = threading.Lock()

_context: ContextVar[dict[str, Any]] = ContextVar("log_context", default={})


def bind_context(**fields: Any) -> None:
    current = dict(_context.get())
    for k, v in fields.items():
        if v is not None:
            current[k] = v
        elif k in current:
            del current[k]
    _context.set(current)


def get_current_context() -> dict[str, Any]:
    return dict(_context.get())


def _safe_put(queue: asyncio.Queue[dict[str, Any]], entry: dict[str, Any]) -> None:
    try:
        queue.put_nowait(entry)
    except asyncio.QueueFull:
        pass
    except Exception:
        pass


class LogSubscriber:
    def __init__(self, queue: asyncio.Queue[dict[str, Any]], loop: asyncio.AbstractEventLoop):
        self.queue = queue
        self.loop = loop

    def push(self, entry: dict[str, Any]) -> None:
        if self.loop.is_closed():
            return
        try:
            self.loop.call_soon_threadsafe(_safe_put, self.queue, entry)
        except Exception:
            pass


def get_recent_logs(limit: int = 200, session_id: str | None = None) -> list[dict[str, Any]]:
    with _log_lock:
        entries = list(_log_buffer)
    if session_id:
        entries = [e for e in entries if e.get("session_id") == session_id]
    return entries[-limit:]


def subscribe_logs() -> tuple[asyncio.Queue[dict[str, Any]], LogSubscriber]:
    loop = asyncio.get_running_loop()
    q: asyncio.Queue[dict[str, Any]] = asyncio.Queue(maxsize=1000)
    sub = LogSubscriber(q, loop)
    with _log_lock:
        _subscribers.add(sub)
    return q, sub


def unsubscribe_logs(sub: LogSubscriber) -> None:
    with _log_lock:
        _subscribers.discard(sub)


class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        ctx = _context.get()
        entry: dict[str, Any] = {
            "ts": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
            "level": record.levelname,
        }

        # Include event if present on record
        if hasattr(record, "event") and record.event:
            entry["event"] = record.event
        else:
            entry["event"] = "log.message"

        # Inject context fields: trace_id, run_id, use_case, user_id, session_id, etc.
        for key in [
            "trace_id",
            "run_id",
            "parent_run_id",
            "agent_role",
            "use_case",
            "session_id",
            "user_id",
        ]:
            if key in ctx and ctx[key] is not None:
                entry[key] = ctx[key]

        # Add extra fields passed in kwargs
        if hasattr(record, "extra_fields") and record.extra_fields:
            for k, v in record.extra_fields.items():
                if k not in entry:
                    entry[k] = v

        if record.getMessage() and entry["event"] == "log.message":
            entry["message"] = record.getMessage()

        if record.exc_info:
            entry["exception"] = self.formatException(record.exc_info)

        with _log_lock:
            _log_buffer.append(entry)
            for sub in list(_subscribers):
                sub.push(entry)

        return json.dumps(entry, ensure_ascii=False)


_configured = False


def setup_logging() -> None:
    global _configured
    if _configured:
        return
    settings = get_settings()
    level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JSONFormatter())

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.handlers = [handler]

    # Silence verbose 3rd party logs
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    _configured = True


def log_step(event: str, level: int = logging.INFO, **fields: Any) -> None:
    setup_logging()
    logger = logging.getLogger("app.step")
    extra = {"event": event, "extra_fields": fields}
    logger.log(level, "", extra=extra)
