import pytest
from pydantic_ai import Agent
from pydantic_ai.exceptions import ModelHTTPError, UnexpectedModelBehavior
from pydantic_ai.models.function import FunctionModel

from app.agents.deps import AgentDeps
from app.agents.runner import run_agent, stream_agent
from app.core.errors import (
    AppError,
    ChatContextFullError,
    ContentFilteredError,
    LlmUnavailableError,
)
from app.core.security import CurrentUser


@pytest.mark.parametrize(
    "status_code,body,expected_exc,expected_code",
    [
        (429, {"code": "1302", "message": "Rate limit"}, LlmUnavailableError, "LLM_UNAVAILABLE"),
        (401, {"code": "1001", "message": "Unauthorized"}, LlmUnavailableError, "LLM_UNAVAILABLE"),
        (500, {"code": "500", "message": "Server error"}, LlmUnavailableError, "LLM_UNAVAILABLE"),
        (400, {"code": "1211", "message": "Unknown Model"}, LlmUnavailableError, "LLM_UNAVAILABLE"),
        (
            400,
            {"code": "1261", "message": "Prompt too long"},
            ChatContextFullError,
            "CHAT_CONTEXT_FULL",
        ),
        (
            400,
            {"code": "1301", "message": "Content sensitive"},
            ContentFilteredError,
            "CHAT_CONTENT_FILTERED",
        ),
    ],
)
@pytest.mark.asyncio
async def test_zai_http_errors_mapped(test_db, status_code, body, expected_exc, expected_code):
    user = CurrentUser(user_id="user-err-1", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-err-1", db=test_db)

    async def err_fn(messages, info):
        raise ModelHTTPError(status_code=status_code, model_name="glm-4.7-flashx", body=body)

    agent = Agent(model=FunctionModel(function=err_fn), deps_type=AgentDeps)

    with pytest.raises(expected_exc) as exc_info:
        await run_agent(agent, "hi", deps, use_case="chat")

    assert exc_info.value.error_code == expected_code
    assert exc_info.value.message.startswith("Failed to")


@pytest.mark.asyncio
async def test_length_before_output_is_context_full(test_db):
    user = CurrentUser(user_id="user-err-2", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-err-2", db=test_db)

    async def length_before_fn(messages, info):
        raise UnexpectedModelBehavior(
            "Model token limit 128000 exceeded before any response was generated"
        )

    agent = Agent(model=FunctionModel(function=length_before_fn), deps_type=AgentDeps)

    with pytest.raises(ChatContextFullError) as exc_info:
        await run_agent(agent, "hi", deps, use_case="chat")

    assert exc_info.value.error_code == "CHAT_CONTEXT_FULL"
    assert exc_info.value.message.startswith("Failed to")


@pytest.mark.asyncio
async def test_stream_errors_use_failed_to_message(test_db):
    user = CurrentUser(user_id="user-err-3", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-err-3", db=test_db)

    async def stream_err_fn(messages, info):
        raise ModelHTTPError(
            status_code=400,
            model_name="glm-4.7-flashx",
            body={"code": "1261", "message": "Context limit exceeded"},
        )
        yield "never"

    agent = Agent(model=FunctionModel(stream_function=stream_err_fn), deps_type=AgentDeps)

    with pytest.raises(AppError) as exc_info:
        async for _ in stream_agent(agent, "hi", deps, use_case="chat"):
            pass

    assert exc_info.value.message.startswith("Failed to")


@pytest.mark.asyncio
async def test_error_step_contains_detailed_fields(test_db):
    from sqlalchemy import select

    from app.db.models import AgentRun

    user = CurrentUser(user_id="user-err-detail", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-err-detail", db=test_db)

    async def err_fn(messages, info):
        raise ModelHTTPError(
            status_code=400,
            model_name="glm-4.5-flash",
            body={"code": "1302", "message": "Too many concurrent requests"},
        )

    agent = Agent(model=FunctionModel(function=err_fn), deps_type=AgentDeps)

    with pytest.raises(LlmUnavailableError):
        await run_agent(agent, "hi", deps, use_case="chat")

    # Verify run record in DB
    runs = (
        (await test_db.execute(select(AgentRun).where(AgentRun.user_id == "user-err-detail")))
        .scalars()
        .all()
    )
    assert len(runs) == 1
    run_record = runs[0]
    assert run_record.status == "failed"
    assert "ModelHTTPError" in run_record.error
    assert "1302" in run_record.error or "Too many concurrent requests" in run_record.error

    # Verify step log
    error_step = next(s for s in run_record.steps if s["event"] == "run.error")
    assert error_step["error_type"] == "ModelHTTPError"
    assert "error_message" in error_step
    assert "status_code" in error_step
    assert error_step["status_code"] == 400
