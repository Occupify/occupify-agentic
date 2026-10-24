import pytest
from pydantic_ai import Agent
from pydantic_ai.exceptions import (
    ModelContextWindowExceededError,
    UnexpectedModelBehavior,
)
from pydantic_ai.models.function import FunctionModel
from pydantic_ai.models.test import TestModel

from app.agents.deps import AgentDeps
from app.agents.runner import (
    AgentStreamDelta,
    AgentStreamDone,
    AgentStreamMeta,
    run_agent,
    stream_agent,
)
from app.core.errors import AppError, ChatContextFullError
from app.core.security import CurrentUser
from app.db.models import AgentRun


@pytest.mark.asyncio
async def test_runner_with_test_model(test_db):
    test_agent = Agent(
        model="zai:glm-4.7",
        system_prompt="You are a helpful test assistant.",
        deps_type=AgentDeps,
    )

    user = CurrentUser(user_id="user-999", role="ROLE_USER", email="u@example.com")
    deps = AgentDeps(user=user, session_id="sess-123", db=test_db)

    with test_agent.override(model=TestModel(custom_output_text="Test response")):
        res = await run_agent(
            agent=test_agent,
            prompt="Hello agent",
            deps=deps,
            use_case="chat",
        )

        assert res.output == "Test response"
        assert res.model == "glm-4.7"
        assert res.run_id is not None

        run_record = await test_db.get(AgentRun, res.run_id)
        assert run_record is not None
        assert run_record.status == "succeeded"
        assert run_record.user_id == "user-999"
        assert len(run_record.steps) >= 3  # run.start, llm.request, llm.response, run.end


@pytest.mark.asyncio
async def test_stream_agent_records_run_and_steps(test_db):
    async def stream_fn(messages, info):
        yield "Hello "
        yield "stream!"

    test_agent = Agent(
        model=FunctionModel(stream_function=stream_fn),
        system_prompt="You are a helpful assistant.",
        deps_type=AgentDeps,
    )

    user = CurrentUser(user_id="user-stream-1", role="ROLE_USER", email="s@example.com")
    deps = AgentDeps(user=user, session_id="sess-stream-1", db=test_db)

    items = []
    async for item in stream_agent(
        agent=test_agent,
        prompt="Stream prompt",
        deps=deps,
        use_case="chat",
    ):
        items.append(item)

    assert any(isinstance(i, AgentStreamMeta) for i in items)
    assert any(isinstance(i, AgentStreamDelta) for i in items)
    done_items = [i for i in items if isinstance(i, AgentStreamDone)]
    assert len(done_items) == 1
    done = done_items[0]
    assert done.output == "Hello stream!"

    # Verify agent_runs record was written in DB for streamed turn (F-03)
    run_record = await test_db.get(AgentRun, done.run_id)
    assert run_record is not None
    assert run_record.status == "succeeded"
    assert run_record.user_id == "user-stream-1"
    event_names = [s["event"] for s in run_record.steps]
    assert "run.start" in event_names
    assert "llm.request" in event_names
    assert "llm.response" in event_names
    assert "run.end" in event_names


@pytest.mark.asyncio
async def test_context_window_exceeded_error_mapping(test_db):
    user = CurrentUser(user_id="user-ctx", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-ctx", db=test_db)

    # 1. Pydantic AI ModelContextWindowExceededError
    async def overflow_fn(messages, info):
        raise ModelContextWindowExceededError(model_name="glm-4.7", message="Context limit reached")

    overflow_agent = Agent(model=FunctionModel(function=overflow_fn), deps_type=AgentDeps)
    with pytest.raises(ChatContextFullError) as exc_info:
        await run_agent(overflow_agent, "test", deps, use_case="chat")
    assert exc_info.value.status_code == 422
    assert exc_info.value.error_code == "CHAT_CONTEXT_FULL"

    # 2. UnexpectedModelBehavior with finish reason length
    async def length_limit_fn(messages, info):
        raise UnexpectedModelBehavior(
            "Model token limit exceeded before response, finish reason length"
        )

    len_agent = Agent(model=FunctionModel(function=length_limit_fn), deps_type=AgentDeps)
    with pytest.raises(ChatContextFullError) as exc_info2:
        await run_agent(len_agent, "test", deps, use_case="chat")
    assert exc_info2.value.error_code == "CHAT_CONTEXT_FULL"


@pytest.mark.asyncio
async def test_history_parse_failure_raises(test_db):
    user = CurrentUser(user_id="user-hist", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-hist", db=test_db)

    test_agent = Agent(model=TestModel(), deps_type=AgentDeps)
    malformed_history = [{"invalid": "cannot_be_parsed_as_model_message"}]

    # Must raise AppError with HISTORY_PARSE_FAILED rather than quietly discarding history (F-15)
    with pytest.raises(AppError) as exc_info:
        await run_agent(test_agent, "hi", deps, use_case="chat", history=malformed_history)
    assert exc_info.value.error_code == "HISTORY_PARSE_FAILED"
