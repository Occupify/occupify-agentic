import inspect

import pytest
from app.agents.budget import HarnessStop, RunBudget, StopReason
from app.features.job_match.search_agent import (
    SearchAgentHarness,
    maybe_search_more,
    search_more,
)
from pydantic_ai.exceptions import UnexpectedModelBehavior

from app.features.job_match.ports import PipelineOptions, RunState


def test_search_more_schema_has_no_user_or_write_args():
    sig = inspect.signature(search_more)
    param_names = list(sig.parameters.keys())
    assert "user_id" not in param_names
    assert "user" not in param_names
    # Only read parameters like ctx, query, skills
    for p in sig.parameters.values():
        assert p.name in ("ctx", "query", "skills", "args")


@pytest.mark.asyncio
async def test_not_called_when_goal_met_or_exhausted():
    state = RunState(fitting_projects_count=10, exhausted=False)
    budget = RunBudget()
    called, stop_reason = await maybe_search_more(state, budget, PipelineOptions())
    assert called is False
    assert stop_reason is None

    # Exhausted True
    state_ex = RunState(fitting_projects_count=3, exhausted=True)
    called_ex, stop_reason_ex = await maybe_search_more(state_ex, budget, PipelineOptions())
    assert called_ex is False


def test_duplicate_then_loop():
    harness = SearchAgentHarness(goal=10)
    # First call with (query="react", skills=["React"])
    res1 = harness.check_call_and_record("react", ["React"])
    assert res1.status == "ok"

    # Repeat once -> duplicate reject
    res2 = harness.check_call_and_record("react", ["React"])
    assert res2.status == "duplicate"
    assert harness.reject_count == 1

    # Repeat second time -> raises HarnessStop(loop)
    with pytest.raises(HarnessStop) as exc_info:
        harness.check_call_and_record("react", ["React"])
    assert exc_info.value.reason == StopReason.LOOP


def test_stop_reasons():
    # Verify all stop reason enums exist per spec
    expected_reasons = {
        "goal_reached",
        "loop",
        "stall",
        "budget_requests",
        "budget_tool_calls",
        "budget_input_tokens",
        "model_done",
        "invalid_tool_use",
    }
    actual_reasons = {r.value for r in StopReason}
    assert expected_reasons.issubset(actual_reasons)


def test_tool_states():
    # States returned by search_more: ok, ok_empty, invalid_param, duplicate, error, budget_exhausted
    from app.features.job_match.search_agent import ToolState

    expected_states = {"ok", "ok_empty", "invalid_param", "duplicate", "error", "budget_exhausted"}
    actual_states = {s.value for s in ToolState}
    assert expected_states.issubset(actual_states)


def test_unexpected_model_behavior_is_invalid_tool_use():
    from app.features.job_match.search_agent import map_exception_to_stop_reason

    stop = map_exception_to_stop_reason(UnexpectedModelBehavior("Invalid tool arguments"))
    assert stop == StopReason.INVALID_TOOL_USE


@pytest.mark.asyncio
async def test_nested_skill_match_counts_toward_agent_budget():
    budget = RunBudget()
    initial_requests = budget.usage.requests
    harness = SearchAgentHarness(goal=10, budget=budget)
    # Simulate nested S5b execution
    harness.record_nested_skill_match_requests(count=3)
    assert budget.usage.requests == initial_requests + 3
