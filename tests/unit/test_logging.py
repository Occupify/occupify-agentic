import json
import logging

from app.core.logging import JSONFormatter, bind_context


def test_json_formatter():
    formatter = JSONFormatter()
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test.py",
        lineno=10,
        msg="test message",
        args=(),
        exc_info=None,
    )
    bind_context(trace_id="trace-123", run_id="run-456", use_case="chat")
    output = formatter.format(record)
    data = json.loads(output)

    assert data["trace_id"] == "trace-123"
    assert data["run_id"] == "run-456"
    assert data["use_case"] == "chat"
    assert data["level"] == "INFO"


def test_log_step_extra_fields():
    formatter = JSONFormatter()
    bind_context(trace_id="tr-1", user_id="u-1")
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test.py",
        lineno=20,
        msg="",
        args=(),
        exc_info=None,
    )
    record.event = "llm.response"
    record.extra_fields = {"tokens_in": 100, "tokens_out": 50, "ms": 250}
    output = formatter.format(record)
    data = json.loads(output)

    assert data["event"] == "llm.response"
    assert data["tokens_in"] == 100
    assert data["tokens_out"] == 50
    assert data["ms"] == 250
    assert data["trace_id"] == "tr-1"
    assert data["user_id"] == "u-1"
