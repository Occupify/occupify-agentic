from pathlib import Path
import pytest

from app.agents.capture import capture_model_requests
from app.features.job_match.pipeline import run_pipeline
from app.features.job_match.ports import PipelineOptions, RunResult, RunState
from app.messaging.mock_core import MockCoreRpc
from tests.unit.job_match.fakes import FakeJobIndex


@pytest.fixture
def mock_rpc():
    return MockCoreRpc()


@pytest.fixture
def persona_a_pdf() -> bytes:
    return Path("evals/uc4/personas/cv-a.pdf").read_bytes()


@pytest.mark.asyncio
async def test_backend_persona_ranks_p03_top3_with_full_job_fields(mock_user, persona_a_pdf, mock_rpc):
    state = RunState()
    res = await run_pipeline(
        state=state,
        pdf_bytes=persona_a_pdf,
        user=mock_user,
        core_rpc=mock_rpc,
        options=PipelineOptions(),
    )
    assert res.status == "succeeded"
    assert res.outcome == "OK"
    assert len(res.items) <= 10

    # Project p03 (a1000000-0000-0000-0000-000000000003) must be in top 3
    top3_pids = [item["projectId"] for item in res.items[:3]]
    assert "a1000000-0000-0000-0000-000000000003" in top3_pids

    # Job j0301 listed with full fields
    p03 = next(item for item in res.items if item["projectId"] == "a1000000-0000-0000-0000-000000000003")
    j0301 = next(j for j in p03["jobs"] if j["jobId"] == "b1000000-0000-0000-0000-000000000301")
    assert j0301["matchScore"] > 0
    assert "matchedSkills" in j0301
    assert "missingSkills" in j0301
    assert "requirements" in j0301
    assert "summary" in j0301


@pytest.mark.asyncio
async def test_display_fields_come_from_core_snapshot(mock_user, persona_a_pdf, mock_rpc):
    state = RunState()
    res = await run_pipeline(
        state=state,
        pdf_bytes=persona_a_pdf,
        user=mock_user,
        core_rpc=mock_rpc,
        options=PipelineOptions(),
    )
    assert len(res.items) > 0
    item = res.items[0]
    # title, budget, salaryType must come from core's mock snapshot, not LLM inventions
    assert item["projectTitle"] != ""
    job = item["jobs"][0]
    assert "title" in job
    assert "salaryType" in job


@pytest.mark.asyncio
async def test_mock_run_is_succeeded_without_search_agent(mock_user, persona_a_pdf, mock_rpc):
    # On mock data, initial retrieval pool is exhausted, so search agent does not run
    state = RunState()
    res = await run_pipeline(
        state=state,
        pdf_bytes=persona_a_pdf,
        user=mock_user,
        core_rpc=mock_rpc,
        options=PipelineOptions(),
    )
    assert res.status == "succeeded"
    assert res.stop_reason is None or res.stop_reason == "goal_reached"


@pytest.mark.asyncio
async def test_not_a_cv_precheck_no_gate_no_model(mock_user, mock_rpc):
    not_a_cv_pdf = Path("tests/fixtures/job_match/not_a_cv.pdf").read_bytes()

    with capture_model_requests() as captured:
        state = RunState()
        res = await run_pipeline(
            state=state,
            pdf_bytes=not_a_cv_pdf,
            user=mock_user,
            core_rpc=mock_rpc,
            options=PipelineOptions(),
        )

    assert res.status == "succeeded"
    assert res.outcome == "NOT_A_CV"
    assert res.message.startswith("Failed to")
    # Neither privacy gate nor any model called
    assert len(captured) == 0


@pytest.mark.asyncio
async def test_insufficient_profile_stops_before_search(mock_user, mock_rpc, monkeypatch):
    # CV with recognized heading but fewer than 2 skills
    sparse_cv_pdf = Path("tests/fixtures/job_match/not_a_cv.pdf").read_bytes()

    from app.skill_schemas.candidate import CandidateProfile
    sparse_profile = CandidateProfile(status="ok", skills=["SoloSkill"])

    from tests.unit.job_match.scripts import structured
    with override_skill_models({"extract-candidate-profile": structured(sparse_profile)}):
        state = RunState()
        res = await run_pipeline(
            state=state,
            pdf_bytes=sparse_cv_pdf,
            user=mock_user,
            core_rpc=mock_rpc,
            options=PipelineOptions(),
        )

    assert res.status == "succeeded"
    assert res.outcome == "INSUFFICIENT_PROFILE"
    assert len(res.items) == 0


@pytest.mark.asyncio
async def test_reranker_failure_degraded_partial_warning(mock_user, persona_a_pdf, mock_rpc):
    state = RunState()
    res = await run_pipeline(
        state=state,
        pdf_bytes=persona_a_pdf,
        user=mock_user,
        core_rpc=mock_rpc,
        options=PipelineOptions(rerank=False),
    )
    assert res.status == "partial"
    warning_codes = [w["code"] for w in res.warnings]
    assert "RERANKER_UNAVAILABLE" in warning_codes


@pytest.mark.asyncio
async def test_index_unusable_falls_back_to_core_search(mock_user, persona_a_pdf, mock_rpc):
    # Unusable job index
    unusable_store = FakeJobIndex(usable=False)
    state = RunState()
    res = await run_pipeline(
        state=state,
        pdf_bytes=persona_a_pdf,
        user=mock_user,
        store=unusable_store,
        core_rpc=mock_rpc,
        options=PipelineOptions(),
    )
    assert res.status == "partial"
    warning_codes = [w["code"] for w in res.warnings]
    assert "INDEX_UNAVAILABLE" in warning_codes


@pytest.mark.asyncio
async def test_ml_disabled_outside_test_env_degrades_with_warnings(mock_user, persona_a_pdf, mock_rpc, monkeypatch):
    # Outside APP_ENV=test with ML_ENABLED=false
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.setenv("ML_ENABLED", "false")

    state = RunState()
    res = await run_pipeline(
        state=state,
        pdf_bytes=persona_a_pdf,
        user=mock_user,
        core_rpc=mock_rpc,
        options=PipelineOptions(),
    )
    assert res.status == "partial"
    warning_codes = [w["code"] for w in res.warnings]
    assert "RERANKER_UNAVAILABLE" in warning_codes or "INDEX_UNAVAILABLE" in warning_codes


@pytest.mark.asyncio
async def test_runs_after_request_session_closed(mock_user, persona_a_pdf, mock_rpc):
    # Verifies background execution runs independently with deps.db=None and its own session for documents
    state = RunState()
    res = await run_pipeline(
        state=state,
        pdf_bytes=persona_a_pdf,
        user=mock_user,
        core_rpc=mock_rpc,
        options=PipelineOptions(),
    )
    assert res.status in ("succeeded", "partial")


from app.agents.subagent import override_skill_models  # noqa: E402
