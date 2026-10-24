import json
import logging
import sys
from contextvars import ContextVar
from datetime import UTC, datetime
from typing import Any

from app.core.config import get_settings

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
        for key in ["trace_id", "run_id", "use_case", "session_id", "user_id"]:
            if key in ctx:
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
