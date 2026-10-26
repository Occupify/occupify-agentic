import json
import logging
from pathlib import Path
import pytest

from app.core.logging import JSONFormatter, bind_context
from app.features.job_match.pipeline import run_pipeline
from app.features.job_match.ports import PipelineOptions, RunState
from app.messaging.mock_core import MockCoreRpc


class LogCaptureHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.records: list[dict] = []
        self.formatter = JSONFormatter()

    def emit(self, record):
        try:
            formatted = self.formatter.format(record)
            self.records.append(json.loads(formatted))
        except Exception:
            pass


@pytest.fixture
def log_capture():
    handler = LogCaptureHandler()
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    yield handler
    root_logger.removeHandler(handler)


@pytest.mark.asyncio
async def test_agent_role_and_parent_run_id(mock_user, log_capture):
    pdf_bytes = Path("evals/uc4/personas/cv-a.pdf").read_bytes()
    state = RunState(run_id="run-test-logging-1")

    await run_pipeline(
        state=state,
        pdf_bytes=pdf_bytes,
        user=mock_user,
        core_rpc=MockCoreRpc(),
        options=PipelineOptions(),
    )

    llm_events = [r for r in log_capture.records if r.get("event") in ("llm.request", "llm.response")]
    for event in llm_events:
        assert event.get("parent_run_id") == "run-test-logging-1"
        assert event.get("agent_role") in {"profile", "skill_match", "search", "assessment"}


@pytest.mark.asyncio
async def test_stage_events_carry_run_id_after_agent_calls(mock_user, log_capture):
    pdf_bytes = Path("evals/uc4/personas/cv-a.pdf").read_bytes()
    state = RunState(run_id="run-test-logging-2")

    await run_pipeline(
        state=state,
        pdf_bytes=pdf_bytes,
        user=mock_user,
        core_rpc=MockCoreRpc(),
        options=PipelineOptions(),
    )

    stage_events = [r for r in log_capture.records if r.get("event") == "job_match.stage"]
    assert len(stage_events) >= 3
    for ev in stage_events:
        assert ev.get("run_id") == "run-test-logging-2"


@pytest.mark.asyncio
async def test_no_text_in_logs(mock_user, log_capture):
    pdf_bytes = Path("evals/uc4/personas/cv-b.pdf").read_bytes()
    state = RunState(run_id="run-test-logging-3")

    await run_pipeline(
        state=state,
        pdf_bytes=pdf_bytes,
        user=mock_user,
        core_rpc=MockCoreRpc(),
        options=PipelineOptions(),
    )

    # Grep all logged json values
    for record in log_capture.records:
        rec_str = json.dumps(record, ensure_ascii=False)
        assert "sentinel.candidate@example.com" not in rec_str
        assert "0912 000 111" not in rec_str
        assert "Nguyễn Văn Testcase" not in rec_str
        assert "12 Ngõ Thử Nghiệm" not in rec_str
        assert "Ví điện tử với hơn 2 triệu" not in rec_str


@pytest.mark.asyncio
async def test_no_model_output_in_error_logs(log_capture):
    from app.agents.runner import run_agent
    from app.core.errors import AppError

    # Force an error with redact_errors=True
    try:
        bind_context(redact_errors=True)
        raise AppError(500, "INTERNAL_ERROR", "Failed to execute", extra={"sensitive": "secret_text"})
    except Exception:
        logging.getLogger().error("Stage error occurred", exc_info=True)

    for record in log_capture.records:
        rec_str = json.dumps(record)
        assert "secret_text" not in rec_str


@pytest.mark.asyncio
async def test_run_emits_start_stage_end_with_totals(mock_user, log_capture):
    pdf_bytes = Path("evals/uc4/personas/cv-a.pdf").read_bytes()
    state = RunState(run_id="run-test-logging-4")

    await run_pipeline(
        state=state,
        pdf_bytes=pdf_bytes,
        user=mock_user,
        core_rpc=MockCoreRpc(),
        options=PipelineOptions(),
    )

    events = [r.get("event") for r in log_capture.records if r.get("event")]
    assert "job_match.start" in events
    assert "job_match.stage" in events
    assert "job_match.end" in events

    end_event = next(r for r in log_capture.records if r.get("event") == "job_match.end")
    assert "status" in end_event
    assert "tokens_in" in end_event
    assert "tokens_out" in end_event
    assert "cost_usd" in end_event
