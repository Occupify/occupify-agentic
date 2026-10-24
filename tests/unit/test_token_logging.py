import asyncio

import pytest
from pydantic_ai import Agent
from pydantic_ai.messages import ModelResponse, TextPart
from pydantic_ai.models.function import FunctionModel
from pydantic_ai.usage import RequestUsage

from app.agents.deps import AgentDeps
from app.agents.runner import run_agent, stream_agent
from app.core.security import CurrentUser
from app.db.models import AgentRun


class MockUsageStreamModel(FunctionModel):
    @property
    def model_name(self) -> str:
        return "glm-4.7-flashx"

    def request_stream(self, *args, **kwargs):
        cm = super().request_stream(*args, **kwargs)

        async def _wrapped():
            async with cm as resp:
                resp._usage = RequestUsage(
                    input_tokens=286,
                    output_tokens=997,
                    cache_read_tokens=186,
                    output_reasoning_tokens=890,
                )
                yield resp

        from contextlib import asynccontextmanager

        return asynccontextmanager(_wrapped)()


@pytest.mark.asyncio
async def test_tokens_logged_non_stream(test_db):
    user = CurrentUser(user_id="user-tok-1", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-tok-1", db=test_db)

    async def fn(messages, info):
        return ModelResponse(
            parts=[TextPart("Hello with usage")],
            usage=RequestUsage(
                input_tokens=286,
                output_tokens=997,
                cache_read_tokens=186,
                output_reasoning_tokens=890,
            ),
        )

    agent = Agent(model=FunctionModel(function=fn), deps_type=AgentDeps)
    res = await run_agent(agent, "hi", deps, use_case="chat")

    run_record = await test_db.get(AgentRun, res.run_id)
    assert run_record is not None
    steps = run_record.steps
    step_dict = {s["event"]: s for s in steps}

    assert "llm.response" in step_dict
    resp_step = step_dict["llm.response"]
    assert resp_step["tokens_in"] == 286
    assert resp_step["tokens_out"] == 997
    assert resp_step["tokens_cached"] == 186
    assert resp_step["tokens_reasoning"] == 890
    assert resp_step["tokens_total"] == 1283
    assert resp_step["requests"] == 1
    assert resp_step["tokens_known"] is True

    assert "run.end" in step_dict
    end_step = step_dict["run.end"]
    assert end_step["tokens_in"] == 286
    assert end_step["tokens_out"] == 997
    assert end_step["tokens_cached"] == 186
    assert end_step["tokens_reasoning"] == 890
    assert end_step["tokens_total"] == 1283
    assert end_step["tokens_known"] is True


@pytest.mark.asyncio
async def test_tokens_logged_stream(test_db):
    user = CurrentUser(user_id="user-tok-2", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-tok-2", db=test_db)

    async def stream_fn(messages, info):
        yield "chunk1"
        yield "chunk2"

    agent = Agent(model=MockUsageStreamModel(stream_function=stream_fn), deps_type=AgentDeps)
    items = []
    async for item in stream_agent(agent, "stream test", deps, use_case="chat"):
        items.append(item)

    done_items = [i for i in items if hasattr(i, "output")]
    assert len(done_items) == 1
    done = done_items[0]

    run_record = await test_db.get(AgentRun, done.run_id)
    assert run_record is not None
    step_dict = {s["event"]: s for s in run_record.steps}

    assert "llm.response" in step_dict
    assert step_dict["llm.response"]["tokens_cached"] == 186
    assert step_dict["llm.response"]["tokens_reasoning"] == 890
    assert step_dict["llm.response"]["tokens_known"] is True


@pytest.mark.asyncio
async def test_tokens_logged_on_error(test_db):
    user = CurrentUser(user_id="user-tok-3", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-tok-3", db=test_db)

    async def fn_err(messages, info):
        raise RuntimeError("LLM exploded")

    agent = Agent(model=FunctionModel(function=fn_err), deps_type=AgentDeps)
    with pytest.raises(Exception):
        await run_agent(agent, "fail", deps, use_case="chat")

    # Run should record run.error with tokens_known false
    runs = (
        await test_db.execute(
            AgentRun.__table__.select().where(AgentRun.session_id == "sess-tok-3")
        )
    ).fetchall()
    assert len(runs) >= 1
    run_row = runs[0]
    steps = run_row.steps
    error_step = next(s for s in steps if s["event"] == "run.error")
    assert error_step["tokens_known"] is False
    assert error_step["tokens_total"] == 0
    assert error_step["tokens_cached"] == 0
    assert error_step["tokens_reasoning"] == 0


@pytest.mark.asyncio
async def test_tokens_logged_on_interrupt(test_db):
    user = CurrentUser(user_id="user-tok-4", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-tok-4", db=test_db)

    async def slow_stream(messages, info):
        yield "chunk1"
        await asyncio.sleep(10)
        yield "chunk2"

    agent = Agent(model=FunctionModel(stream_function=slow_stream), deps_type=AgentDeps)

    async def runner_task():
        async for _ in stream_agent(agent, "slow", deps, use_case="chat"):
            await asyncio.sleep(0.01)

    t = asyncio.create_task(runner_task())
    await asyncio.sleep(0.05)
    t.cancel()
    with pytest.raises(asyncio.CancelledError):
        await t

    runs = (
        await test_db.execute(
            AgentRun.__table__.select().where(AgentRun.session_id == "sess-tok-4")
        )
    ).fetchall()
    assert len(runs) >= 1
    run_row = runs[0]
    interrupted_step = next(s for s in run_row.steps if s["event"] == "run.interrupted")
    assert interrupted_step is not None
    assert "tokens_known" in interrupted_step


@pytest.mark.asyncio
async def test_tokens_in_run_steps(test_db):
    user = CurrentUser(user_id="user-tok-5", role="ROLE_USER")
    deps = AgentDeps(user=user, session_id="sess-tok-5", db=test_db)

    async def fn(messages, info):
        return ModelResponse(
            parts=[TextPart("Step test")],
            usage=RequestUsage(
                input_tokens=100,
                output_tokens=50,
                cache_read_tokens=10,
                output_reasoning_tokens=20,
            ),
        )

    agent = Agent(model=FunctionModel(function=fn), deps_type=AgentDeps)
    res = await run_agent(agent, "hi", deps, use_case="chat")

    run_record = await test_db.get(AgentRun, res.run_id)
    step_dict = {s["event"]: s for s in run_record.steps}
    assert step_dict["run.end"]["tokens_cached"] == 10
    assert step_dict["run.end"]["tokens_reasoning"] == 20
    assert step_dict["run.end"]["tokens_total"] == 150
