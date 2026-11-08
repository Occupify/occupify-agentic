from decimal import Decimal
from unittest.mock import MagicMock, patch

import pytest
from httpx import ASGITransport, AsyncClient
from pydantic_ai.exceptions import ModelRetry

from app.agents.deps import AgentDeps
from app.core.security import CurrentUser
from app.db.models import ChatMessage, ChatSession
from app.documents.cv_text import CvText, cache_cv_text
from app.features.chat.agent import chat_agent
from app.features.chat.service import ChatService
from app.features.job_match.chat_tool import (
    _find_candidate_cv,
    match_jobs_for_cv,
    render_job_match_markdown,
)
from app.features.job_match.ports import RunOutcome, RunResult, RunStatus
from app.main import app


def test_tool_registered_on_chat_agent():
    tools = chat_agent._function_toolset.tools
    assert "match_jobs_for_cv" in tools


@pytest.mark.asyncio
async def test_current_turn_cv_used():
    user = CurrentUser(user_id="u1", role="ROLE_USER", email="u1@test.com")
    cv = CvText(
        text="Nguyen Van A\n## Experience\nSenior Python Backend Developer with 5 years experience in FastAPI and PostgreSQL.\n## Skills\nPython, FastAPI",
        removed={},
    )
    sha = "sha-turn-cv"
    await cache_cv_text(sha, cv)

    ctx = MagicMock()
    ctx.deps = AgentDeps(
        user=user,
        session_id="s1",
        turn_documents=[sha],
    )

    found_cv = await _find_candidate_cv(ctx)
    assert found_cv is not None
    assert "FastAPI" in found_cv.text


@pytest.mark.asyncio
async def test_previous_turn_cv_used_only_own_session(test_db):
    user1 = CurrentUser(user_id="user-1", role="ROLE_USER", email="u1@test.com")
    user2 = CurrentUser(user_id="user-2", role="ROLE_USER", email="u2@test.com")

    cv = CvText(
        text="Candidate John Doe\n## Experience\nFullstack Engineer React Node Python Docker.\n## Skills\nReact",
        removed={},
    )
    sha = "sha-prev-turn-cv"
    await cache_cv_text(sha, cv)

    # Create session for user1
    sess = ChatSession(id="sess-u1", user_id="user-1", title="Chat 1")
    test_db.add(sess)
    msg = ChatMessage(
        id="msg-1",
        session_id="sess-u1",
        user_id="user-1",
        seq=1,
        role="user",
        display_text="Here is my CV",
        attachments=[{"fileName": "cv.pdf", "sha256": sha}],
    )
    test_db.add(msg)
    await test_db.commit()

    # User 1 in sess-u1 (no turn documents in current turn)
    ctx1 = MagicMock()
    ctx1.deps = AgentDeps(
        user=user1,
        session_id="sess-u1",
        db=test_db,
        turn_documents=[],
    )
    found1 = await _find_candidate_cv(ctx1)
    assert found1 is not None
    assert "Candidate John Doe" in found1.text

    # User 2 in another session (or trying to access sess-u1)
    ctx2 = MagicMock()
    ctx2.deps = AgentDeps(
        user=user2,
        session_id="sess-u1",
        db=test_db,
        turn_documents=[],
    )
    found2 = await _find_candidate_cv(ctx2)
    assert found2 is None


@pytest.mark.asyncio
async def test_need_cv_when_none_or_expired():
    user = CurrentUser(user_id="u1", role="ROLE_USER")
    ctx = MagicMock()
    ctx.deps = AgentDeps(
        user=user,
        session_id="s1",
        turn_documents=[],
    )

    # Even if index is missing/unavailable, missing CV takes precedence
    with (
        patch("app.features.job_match.chat_tool.models_loaded", return_value=True),
        patch("app.features.job_match.chat_tool.index_state", return_value="missing"),
    ):
        res = await match_jobs_for_cv(ctx)

    assert res["outcome"] == "NEED_CV"
    assert res["itemCount"] == 0
    assert ctx.deps.job_match_block is not None
    assert "Vui lòng đính kèm CV" in ctx.deps.job_match_block


@pytest.mark.asyncio
async def test_invalid_criteria_model_retry():
    user = CurrentUser(user_id="u1", role="ROLE_USER")
    ctx = MagicMock()
    ctx.deps = AgentDeps(user=user)

    with pytest.raises(ModelRetry) as exc_info:
        await match_jobs_for_cv(
            ctx,
            min_budget=Decimal("20000000"),
            max_budget=Decimal("10000000"),
        )
    assert "min_budget cannot be greater than max_budget" in str(exc_info.value)


@pytest.mark.asyncio
async def test_second_call_same_turn_returns_first_result():
    user = CurrentUser(user_id="u1", role="ROLE_USER")
    memo = {
        "outcome": "OK",
        "itemCount": 1,
        "warnings": [],
        "topMissingSkills": [],
        "criteriaApplied": {},
        "items": [{"rank": 1, "projectId": "p-1"}],
    }
    ctx = MagicMock()
    ctx.deps = AgentDeps(user=user, job_match_memo=memo)

    res = await match_jobs_for_cv(ctx)
    assert res == memo


@pytest.mark.asyncio
async def test_timeout_returns_run_timeout():
    user = CurrentUser(user_id="u1", role="ROLE_USER")
    cv = CvText(
        text="CV Candidate\n## Experience\nPython Software Engineer at ABC Corp\n## Skills\nPython",
        removed={},
    )
    sha = "sha-timeout"
    await cache_cv_text(sha, cv)

    ctx = MagicMock()
    ctx.deps = AgentDeps(user=user, turn_documents=[sha])

    async def mock_slow_pipeline(*args, **kwargs):
        raise TimeoutError()

    with (
        patch("app.features.job_match.chat_tool.models_loaded", return_value=True),
        patch("app.features.job_match.chat_tool.index_state", return_value="ok"),
        patch("app.features.job_match.chat_tool.run_pipeline", side_effect=mock_slow_pipeline),
    ):
        res = await match_jobs_for_cv(ctx)

    assert res["outcome"] == "RUN_TIMEOUT"
    assert res["itemCount"] == 0
    assert "vượt quá thời gian" in ctx.deps.job_match_block


@pytest.mark.asyncio
async def test_stream_progress_then_block_then_done(test_db):
    service = ChatService(test_db)
    user = CurrentUser(user_id="u-stream", role="ROLE_USER", email="u-stream@test.com")

    from app.agents.runner import AgentStreamDelta, AgentStreamDone, AgentStreamMeta

    async def fake_stream_agent(agent, prompt, deps, use_case, history):
        yield AgentStreamMeta(run_id="run-123", model="test-model", trace_id="trace-123")
        if deps.on_progress:
            await deps.on_progress("RETRIEVAL")
        yield AgentStreamDelta(content="Here are the matches:")
        deps.job_match_block = "\n### 🎯 Matching Jobs\n1. Backend Engineer"
        deps.pipeline_tokens_in = 100
        deps.pipeline_tokens_out = 20
        yield AgentStreamDone(
            run_id="run-123",
            output="Here are the matches:",
            model="test-model",
            tokens_in=50,
            tokens_out=10,
            user_model_messages=[],
            assistant_model_messages=[],
            latency_ms=100,
        )

    with patch("app.features.chat.service.stream_agent", side_effect=fake_stream_agent):
        events = []
        async for chunk in service.stream_chat_turn(user=user, message="Find jobs"):
            events.append(chunk)

    joined = "".join(events)
    assert "event: meta" in joined
    assert 'event: progress\ndata: {"stage": "RETRIEVAL"}' in joined
    assert "Here are the matches:" in joined
    assert "Matching Jobs" in joined
    assert "1. Backend Engineer" in joined
    assert "event: done" in joined
    assert '"model": "test-model"' in joined
    assert '"tokensIn": 150' in joined
    assert '"tokensOut": 30' in joined


@pytest.mark.asyncio
async def test_block_rendered_by_code_and_replayed_on_idempotent_retry(test_db):
    service = ChatService(test_db)
    user = CurrentUser(user_id="u-idem", role="ROLE_USER", email="u-idem@test.com")

    from app.agents.runner import AgentRunOutput

    async def fake_run_agent(agent, prompt, deps, use_case, history):
        deps.job_match_block = "\n### 🎯 Match 1: Python Dev"
        return AgentRunOutput(
            run_id="run-idem",
            output="Found matches for you.",
            model="test-model",
            tokens_in=10,
            tokens_out=5,
            user_model_messages=[],
            assistant_model_messages=[],
            latency_ms=100,
        )

    with patch("app.features.chat.service.run_agent", side_effect=fake_run_agent):
        res1 = await service.send_message(
            user=user,
            message="Match jobs",
            session_id=None,
            client_message_id="client-msg-123",
        )
        assert res1.reply == "Found matches for you.\n### 🎯 Match 1: Python Dev"

        # Replay with same client_message_id
        res2 = await service.send_message(
            user=user,
            message="Match jobs",
            session_id=res1.sessionId,
            client_message_id="client-msg-123",
        )
        assert res2.reply == "Found matches for you.\n### 🎯 Match 1: Python Dev"
        assert res2.messageId == res1.messageId


@pytest.mark.asyncio
async def test_summary_has_no_titles_scores_cv_or_employer_text():
    user = CurrentUser(user_id="u1", role="ROLE_USER")
    cv = CvText(
        text="CV Candidate\n## Experience\nPython Software Engineer at Secret Employer\n## Skills\nPython",
        removed={},
    )
    sha = "sha-summary-leak"
    await cache_cv_text(sha, cv)

    ctx = MagicMock()
    ctx.deps = AgentDeps(user=user, turn_documents=[sha])

    mock_item = MagicMock()
    mock_item.rank = 1
    mock_item.score = 0.95
    mock_item.project_id = "proj-xyz"
    mock_item.job_title = "Secret Job Title"
    mock_item.project_title = "Secret Project Title"
    mock_item.salary = "50 triệu"
    mock_item.matched_skills = ["Python"]

    mock_result = MagicMock()
    mock_result.status = RunStatus.SUCCEEDED
    mock_result.outcome = RunOutcome.OK
    mock_result.tokens_in = 100
    mock_result.tokens_out = 50
    mock_result.cost_usd = 0.001
    mock_result.items = [mock_item]
    mock_result.missing_skills = ["Docker"]
    mock_result.warnings = []

    with (
        patch("app.features.job_match.chat_tool.models_loaded", return_value=True),
        patch("app.features.job_match.chat_tool.index_state", return_value="ok"),
        patch("app.features.job_match.chat_tool.run_pipeline", return_value=mock_result),
    ):
        summary = await match_jobs_for_cv(ctx)

    # Allowed keys only
    assert set(summary.keys()) == {
        "outcome",
        "itemCount",
        "warnings",
        "topMissingSkills",
        "criteriaApplied",
        "items",
    }
    assert summary["items"] == [{"rank": 1, "projectId": "proj-xyz"}]

    # Ensure no titles, scores, employer, or CV text leaked in summary
    summary_str = str(summary)
    assert "Secret Job Title" not in summary_str
    assert "Secret Project Title" not in summary_str
    assert "0.95" not in summary_str
    assert "Secret Employer" not in summary_str


@pytest.mark.asyncio
async def test_ready_200_when_index_missing():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        with (
            patch("app.api.health.index_state", return_value="missing"),
            patch("app.api.health.is_broker_connected", return_value=True),
        ):
            resp = await client.get("/ready")
            assert resp.status_code == 200
            data = resp.json()
            assert data["status"] == "UP"
            assert data["checks"]["index"] == "missing"


@pytest.mark.asyncio
async def test_source_mismatch_is_not_usable():
    user = CurrentUser(user_id="u1", role="ROLE_USER")
    cv = CvText(
        text="CV Candidate\n## Experience\nPython Software Engineer\n## Skills\nPython",
        removed={},
    )
    sha = "sha-mismatch"
    await cache_cv_text(sha, cv)

    ctx = MagicMock()
    ctx.deps = AgentDeps(user=user, turn_documents=[sha])

    with (
        patch("app.features.job_match.chat_tool.models_loaded", return_value=True),
        patch("app.features.job_match.chat_tool.index_state", return_value="mismatch"),
    ):
        res = await match_jobs_for_cv(ctx)

    assert res["outcome"] == "INDEX_UNAVAILABLE"
    assert res["itemCount"] == 0
    assert "chưa sẵn sàng" in ctx.deps.job_match_block


@pytest.mark.asyncio
async def test_pipeline_dict_items_rendered_correctly():
    user = CurrentUser(user_id="u1", role="ROLE_USER")
    cv = CvText(
        text="CV Candidate\n## Experience\nPython Engineer\n## Skills\nPython",
        removed={},
    )
    sha = "sha-dict-items"
    await cache_cv_text(sha, cv)

    ctx = MagicMock()
    ctx.deps = AgentDeps(user=user, turn_documents=[sha])

    mock_result = MagicMock()
    mock_result.status = RunStatus.SUCCEEDED
    mock_result.outcome = RunOutcome.OK
    mock_result.tokens_in = 100
    mock_result.tokens_out = 50
    mock_result.cost_usd = 0.001
    mock_result.items = [
        {
            "rank": 1,
            "projectId": "proj-123",
            "projectTitle": "Fintech Platform",
            "matchScore": 85,
            "verified": True,
            "jobs": [
                {
                    "jobId": "job-1",
                    "title": "Senior Python Dev",
                    "salaryType": "FIXED",
                    "budgetMin": 20000000,
                    "budgetMax": 30000000,
                    "matchScore": 85,
                    "matchedSkills": ["Python", "FastAPI"],
                    "summary": "Great fit for backend",
                }
            ],
        }
    ]
    mock_result.missing_skills = []
    mock_result.warnings = []

    with (
        patch("app.features.job_match.chat_tool.models_loaded", return_value=True),
        patch("app.features.job_match.chat_tool.index_state", return_value="ok"),
        patch("app.features.job_match.chat_tool.run_pipeline", return_value=mock_result),
    ):
        summary = await match_jobs_for_cv(ctx)

    assert summary["outcome"] == "OK"
    assert summary["itemCount"] == 1
    assert summary["items"] == [{"rank": 1, "projectId": "proj-123"}]
    assert ctx.deps.job_match_block is not None
    assert "Senior Python Dev" in ctx.deps.job_match_block
    assert "Fintech Platform" in ctx.deps.job_match_block
    assert "20,000,000 - 30,000,000 VND" in ctx.deps.job_match_block


@pytest.mark.asyncio
async def test_real_run_result_instance_with_top_missing_skills():
    user = CurrentUser(user_id="u1", role="ROLE_USER")
    cv = CvText(
        text="CV Candidate\n## Experience\nPython Engineer\n## Skills\nPython",
        removed={},
    )
    sha = "sha-real-run-result"
    await cache_cv_text(sha, cv)

    ctx = MagicMock()
    ctx.deps = AgentDeps(user=user, turn_documents=[sha])

    real_result = RunResult(
        status=RunStatus.SUCCEEDED,
        outcome=RunOutcome.OK,
        tokens_in=120,
        tokens_out=45,
        cost_usd=0.0005,
        items=[
            {
                "rank": 1,
                "projectId": "proj-real",
                "projectTitle": "Cloud Platform",
                "matchScore": 90,
                "verified": True,
                "jobs": [
                    {
                        "jobId": "job-real-1",
                        "title": "Lead DevOps",
                        "salaryType": "FIXED",
                        "budgetMin": 30000000,
                        "budgetMax": 40000000,
                        "matchScore": 90,
                        "matchedSkills": ["Python"],
                        "missingSkills": ["Docker", "Kubernetes"],
                    }
                ],
            }
        ],
        top_missing_skills=["Docker", "Kubernetes"],
        warnings=[],
    )

    with (
        patch("app.features.job_match.chat_tool.models_loaded", return_value=True),
        patch("app.features.job_match.chat_tool.index_state", return_value="ok"),
        patch("app.features.job_match.chat_tool.run_pipeline", return_value=real_result),
    ):
        summary = await match_jobs_for_cv(ctx)

    assert summary["outcome"] == "OK"
    assert summary["itemCount"] == 1
    assert summary["items"] == [{"rank": 1, "projectId": "proj-real"}]
    assert summary["topMissingSkills"] == ["Docker", "Kubernetes"]
    assert ctx.deps.pipeline_tokens_in == 120
    assert ctx.deps.pipeline_tokens_out == 45
    assert ctx.deps.job_match_block is not None
    assert "Lead DevOps" in ctx.deps.job_match_block


def test_outcome_renderings():
    vi_not_cv = render_job_match_markdown([], {}, [], "NOT_A_CV", lang="vi")
    assert "không phải là CV hợp lệ" in vi_not_cv

    en_not_cv = render_job_match_markdown([], {}, [], "NOT_A_CV", lang="en")
    assert "not appear to be a valid CV" in en_not_cv

    vi_insufficient = render_job_match_markdown([], {}, [], "INSUFFICIENT_PROFILE", lang="vi")
    assert "chưa có đủ thông tin kỹ năng" in vi_insufficient

    vi_internal = render_job_match_markdown([], {}, [], "INTERNAL_ERROR", lang="vi")
    assert "Đã xảy ra lỗi" in vi_internal
