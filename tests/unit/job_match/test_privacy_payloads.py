from pathlib import Path

import pytest
from app.agents.capture import capture_model_requests
from app.features.job_match.pipeline import run_pipeline

from app.features.job_match.ports import PipelineOptions, RunState
from tests.unit.job_match.fakes import FakeJobIndex


@pytest.mark.asyncio
async def test_no_pii_or_employer_in_any_model_request(mock_user):
    # Read CV-B (which has sentinels in header AND body)
    cv_b_pdf = Path("evals/uc4/personas/cv-b.pdf").read_bytes()

    sentinels = [
        "sentinel.candidate@example.com",
        "0912 000 111",
        "Nguyễn Văn Testcase",
        "12 Ngõ Thử Nghiệm",
    ]

    with capture_model_requests() as captured:
        state = RunState()
        # Run pipeline with fake models and mock index
        _ = await run_pipeline(
            state=state,
            pdf_bytes=cv_b_pdf,
            user=mock_user,
            store=FakeJobIndex(),
            options=PipelineOptions(),
        )

    # Check that none of the captured requests contain sentinels or employer
    for req in captured:
        req_str = str(req)
        for s in sentinels:
            assert s not in req_str, f"PII Sentinel '{s}' leaked into model request: {req_str}"
        assert "'employer'" not in req_str
        assert '"employer"' not in req_str


@pytest.mark.asyncio
async def test_gate_failure_fails_run_without_model_call(mock_user, monkeypatch):
    def failing_gate(*args, **kwargs):
        raise ValueError("Privacy gate clean failed")

    monkeypatch.setattr("app.features.job_match.pipeline.clean_cv", failing_gate)

    cv_bytes = Path("evals/uc4/personas/cv-a.pdf").read_bytes()

    with capture_model_requests() as captured:
        state = RunState()
        res = await run_pipeline(
            state=state,
            pdf_bytes=cv_bytes,
            user=mock_user,
            store=FakeJobIndex(),
            options=PipelineOptions(),
        )

    assert res.status == "failed"
    assert res.error_code == "PII_REMOVAL_FAILED"
    # No model requests must have been made
    assert len(captured) == 0


@pytest.mark.asyncio
async def test_project_text_sanitised_before_any_prompt(mock_user):
    # Project p15 has email/phone in description ("hr@vidu-cloud.example", "0901 234 567")
    cv_bytes = Path("evals/uc4/personas/cv-a.pdf").read_bytes()

    with capture_model_requests() as captured:
        state = RunState()
        await run_pipeline(
            state=state,
            pdf_bytes=cv_bytes,
            user=mock_user,
            store=FakeJobIndex(),
            options=PipelineOptions(),
        )

    for req in captured:
        req_str = str(req)
        assert "hr@vidu-cloud.example" not in req_str
        assert "0901 234 567" not in req_str
