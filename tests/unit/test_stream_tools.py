import pytest
from pydantic_ai import Agent
from pydantic_ai.messages import ModelResponse, TextPart, ToolCallPart
from pydantic_ai.models.function import FunctionModel
from pydantic_ai.usage import RequestUsage

from app.agents.deps import AgentDeps
from app.agents.runner import (
    AgentStreamDelta,
    AgentStreamDone,
    AgentStreamMeta,
    stream_agent,
)
from app.core.security import CurrentUser


@pytest.mark.asyncio
async def test_text_then_tool_call_runs_tool_and_continues():
    tool_called = False
    call_count = 0

    def handler(msgs, info):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return ModelResponse(
                parts=[
                    TextPart("Preamble text before tool call... "),
                    ToolCallPart("sample_tool", {"arg": "hello"}),
                ],
                usage=RequestUsage(input_tokens=10, output_tokens=5),
            )
        return ModelResponse(
            parts=[TextPart("Final answer after tool execution.")],
            usage=RequestUsage(input_tokens=20, output_tokens=10),
        )

    agent = Agent(FunctionModel(handler))

    @agent.tool_plain
    def sample_tool(arg: str) -> str:
        nonlocal tool_called
        tool_called = True
        return f"result_for_{arg}"

    user = CurrentUser(user_id="user_test", email="test@example.com")
    deps = AgentDeps(user=user, session_id="sess_test", db=None)

    events = []
    deltas = []
    async for event in stream_agent(agent, "test prompt", deps, use_case="chat"):
        events.append(event)
        if isinstance(event, AgentStreamDelta):
            deltas.append(event.content)

    assert tool_called is True
    assert deltas == [
        "Preamble text before tool call... ",
        "Final answer after tool execution.",
    ]
    assert isinstance(events[0], AgentStreamMeta)
    assert isinstance(events[-1], AgentStreamDone)
    done_event = events[-1]
    assert (
        done_event.output == "Preamble text before tool call... Final answer after tool execution."
    )


@pytest.mark.asyncio
async def test_plain_text_reply_unchanged():
    def handler(msgs, info):
        return ModelResponse(
            parts=[TextPart("Simple plain text reply without any tool calls.")],
            usage=RequestUsage(input_tokens=15, output_tokens=8),
        )

    agent = Agent(FunctionModel(handler))
    user = CurrentUser(user_id="user_test", email="test@example.com")
    deps = AgentDeps(user=user, session_id="sess_test", db=None)

    deltas = []
    events = []
    async for event in stream_agent(agent, "hello", deps, use_case="chat"):
        events.append(event)
        if isinstance(event, AgentStreamDelta):
            deltas.append(event.content)

    assert deltas == ["Simple plain text reply without any tool calls."]
    assert isinstance(events[-1], AgentStreamDone)
    assert events[-1].output == "Simple plain text reply without any tool calls."


@pytest.mark.asyncio
async def test_usage_summed_across_responses():
    call_count = 0

    def handler(msgs, info):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return ModelResponse(
                parts=[
                    TextPart("Step 1... "),
                    ToolCallPart("helper_tool", {}),
                ],
                usage=RequestUsage(input_tokens=100, output_tokens=25),
            )
        return ModelResponse(
            parts=[TextPart("Step 2 completed.")],
            usage=RequestUsage(input_tokens=150, output_tokens=40),
        )

    agent = Agent(FunctionModel(handler))

    @agent.tool_plain
    def helper_tool() -> str:
        return "done"

    user = CurrentUser(user_id="user_test", email="test@example.com")
    deps = AgentDeps(user=user, session_id="sess_test", db=None)

    events = []
    async for event in stream_agent(agent, "run helper", deps, use_case="chat"):
        events.append(event)

    done_event = events[-1]
    assert isinstance(done_event, AgentStreamDone)
    assert done_event.tokens_in == 250
    assert done_event.tokens_out == 65
