import pytest
from pydantic_ai import Agent, RunContext
from pydantic_ai.messages import ModelResponse, TextPart, ToolCallPart, ToolReturnPart
from pydantic_ai.models.function import AgentInfo, FunctionModel
from pydantic_ai.usage import RequestUsage

from app.agents.deps import AgentDeps
from app.agents.subagent import invoke_subagent
from app.core.logging import bind_context
from app.features.chat.agent import chat_agent
from tests.unit.helpers import FakeRpc


@pytest.mark.asyncio
async def test_invoke_subagent_propagates_run_context(mock_user, monkeypatch):
    bind_context(run_id="parent-run-999")
    rpc = FakeRpc({"ok": True, "data": {"content": [], "totalElements": 0}})
    parent_deps = AgentDeps(user=mock_user, session_id="sess-parent-1", rpc=rpc)

    subagent_deps_captured = None

    def fake_create_subagent(tools=None, system_prompt=""):
        async def subagent_fn(messages, info: AgentInfo):
            nonlocal subagent_deps_captured
            # The subagent has access to its own deps via info
            return ModelResponse(
                parts=[TextPart("Subagent completed task.")],
                usage=RequestUsage(input_tokens=150, output_tokens=50),
            )

        agent = Agent(
            model=FunctionModel(function=subagent_fn),
            system_prompt=system_prompt,
            deps_type=AgentDeps,
        )
        return agent

    monkeypatch.setattr("app.agents.subagent.create_subagent", fake_create_subagent)

    # Invoke tool via chat_agent
    def parent_model_fn(messages, info: AgentInfo):
        last_msg = messages[-1]
        for part in getattr(last_msg, "parts", []):
            if isinstance(part, ToolReturnPart):
                return ModelResponse(parts=[TextPart(f"Parent received: {part.content}")])
        return ModelResponse(
            parts=[ToolCallPart("invoke_subagent", {"task": "Find top 5 python projects"})]
        )

    with chat_agent.override(model=FunctionModel(parent_model_fn)):
        result = await chat_agent.run("Research projects", deps=parent_deps)

    assert result.output == "Parent received: Subagent completed task."


@pytest.mark.asyncio
async def test_subagent_logs_start_end_with_cost(mock_user, monkeypatch):
    bind_context(run_id="parent-run-456")
    rpc = FakeRpc({"ok": True, "data": {}})
    parent_deps = AgentDeps(user=mock_user, rpc=rpc)

    logged_steps = []

    def mock_log_step(event, **fields):
        logged_steps.append((event, fields))

    monkeypatch.setattr("app.agents.subagent.log_step", mock_log_step)

    def fake_create_subagent(tools=None, system_prompt=""):
        async def subagent_fn(messages, info: AgentInfo):
            return ModelResponse(
                parts=[TextPart("Done research")],
                usage=RequestUsage(input_tokens=1000, output_tokens=500),
            )

        return Agent(
            model=FunctionModel(function=subagent_fn),
            system_prompt=system_prompt,
            deps_type=AgentDeps,
        )

    monkeypatch.setattr("app.agents.subagent.create_subagent", fake_create_subagent)

    # Create dummy RunContext
    context = RunContext(
        deps=parent_deps,
        model=None,
        usage=RequestUsage(),
        prompt="run subagent",
    )

    out = await invoke_subagent(context, task="Analyze budget distribution")
    assert out == "Done research"

    events = [e[0] for e in logged_steps]
    assert "subagent.start" in events
    assert "subagent.end" in events

    start_fields = next(f for e, f in logged_steps if e == "subagent.start")
    assert start_fields["parent_run_id"] == "parent-run-456"
    assert "Analyze budget distribution" in start_fields["task_summary"]

    end_fields = next(f for e, f in logged_steps if e == "subagent.end")
    assert end_fields["ok"] is True
    assert end_fields["parent_run_id"] == "parent-run-456"
    assert end_fields["prompt_tokens"] == 1000
    assert end_fields["completion_tokens"] == 500
    assert end_fields["total_tokens"] == 1500
    assert end_fields["cost_usd"] > 0
    assert end_fields["cost_vnd"] > 0


@pytest.mark.asyncio
async def test_subagent_failure_logged_and_reraised(mock_user, monkeypatch):
    bind_context(run_id="parent-run-err")
    parent_deps = AgentDeps(user=mock_user)

    logged_steps = []

    def mock_log_step(event, **fields):
        logged_steps.append((event, fields))

    monkeypatch.setattr("app.agents.subagent.log_step", mock_log_step)

    def fake_create_subagent(tools=None, system_prompt=""):
        async def subagent_err_fn(messages, info: AgentInfo):
            raise RuntimeError("Subagent simulated LLM crash")

        return Agent(
            model=FunctionModel(function=subagent_err_fn),
            system_prompt=system_prompt,
            deps_type=AgentDeps,
        )

    monkeypatch.setattr("app.agents.subagent.create_subagent", fake_create_subagent)

    context = RunContext(
        deps=parent_deps,
        model=None,
        usage=RequestUsage(),
        prompt="run subagent",
    )

    with pytest.raises(RuntimeError, match="Subagent simulated LLM crash"):
        await invoke_subagent(context, task="Failing task")

    end_fields = next(f for e, f in logged_steps if e == "subagent.end")
    assert end_fields["ok"] is False
    assert end_fields["parent_run_id"] == "parent-run-err"
    assert "Subagent simulated LLM crash" in end_fields["error"]
