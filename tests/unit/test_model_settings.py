import pytest
from pydantic_ai import Agent
from pydantic_ai.messages import ModelResponse, TextPart
from pydantic_ai.models.function import FunctionModel

from app.agents.deps import AgentDeps
from app.agents.runner import run_agent, stream_agent
from app.core.config import Settings
from app.core.security import CurrentUser


def test_default_model_is_flashx():
    settings = Settings(_env_file=None)
    assert settings.GLM_MODEL == "glm-4.7-flashx"
    assert settings.GLM_MODEL != "glm-4.7-flash"


@pytest.mark.asyncio
async def test_thinking_disabled_on_every_run(test_db):
    user = CurrentUser(user_id="user-t1", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-t1", db=test_db)

    passed_thinking = None

    async def mock_fn(messages, info):
        nonlocal passed_thinking
        passed_thinking = info.model_request_parameters.thinking
        return ModelResponse(parts=[TextPart("reply")])

    agent = Agent(
        model=FunctionModel(function=mock_fn, profile={"supports_thinking": True}),
        deps_type=AgentDeps,
    )
    await run_agent(agent, "hello", deps, use_case="chat")

    assert passed_thinking is False


@pytest.mark.asyncio
async def test_stream_sends_multiple_deltas(test_db):
    import asyncio

    user = CurrentUser(user_id="user-t1-s", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-t1-s", db=test_db)

    async def stream_fn(messages, info):
        for i in range(5):
            yield f"chunk {i} "
            await asyncio.sleep(0.01)

    agent = Agent(model=FunctionModel(stream_function=stream_fn), deps_type=AgentDeps)

    deltas = []
    async for item in stream_agent(agent, "stream test", deps, use_case="chat"):
        if hasattr(item, "content"):
            deltas.append(item.content)

    assert len(deltas) > 1
