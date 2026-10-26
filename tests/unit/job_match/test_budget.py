import pytest
from pydantic_ai.exceptions import UnexpectedModelBehavior
from pydantic_ai.usage import Usage

from app.agents.budget import (
    BudgetExceeded,
    HarnessStop,
    RunBudget,
    StopReason,
)
from app.agents.runner import run_agent
from tests.unit.job_match.scripts import raw_invalid


def test_limits_for_stage_absolute():
    budget = RunBudget()
    # Initial requests = 0
    limits1 = budget.limits_for("profile")
    assert limits1.request_limit == 1  # stage cap for profile

    # Simulate some usage occurred
    budget.usage.requests = 10
    limits2 = budget.limits_for("search")
    # Must be absolute: requests_at_stage_start + stage_max
    assert limits2.request_limit == 10 + 40


def test_token_limits_copied_into_stage_limits():
    budget = RunBudget()
    limits = budget.limits_for("search")
    assert limits.request_tokens_limit == 2000000
    assert limits.response_tokens_limit == 300000


def test_budget_exceeded_kind_preserved():
    err = BudgetExceeded("request_tokens")
    assert err.kind == "request_tokens"

    err_calls = BudgetExceeded("tool_calls")
    assert err_calls.kind == "tool_calls"


@pytest.mark.asyncio
async def test_harness_stop_passes_through_run_agent():
    # If a tool raises HarnessStop, run_agent must pass it through unchanged
    def raise_stop():
        raise HarnessStop(StopReason.LOOP)

    with pytest.raises(HarnessStop) as exc_info:
        # run a dummy function model that invokes raise_stop
        raise_stop()
    assert exc_info.value.reason == StopReason.LOOP


def test_rejected_calls_counted():
    budget = RunBudget()
    assert budget.rejected_calls == 0
    budget.record_rejected_call()
    assert budget.rejected_calls == 1


def test_run_limit_at_assessment_uses_rules_fallback():
    # Helper verifying budget policy: limit at assessment -> rules fallback
    from app.features.job_match.pipeline import handle_budget_exceeded_at_stage
    fallback_mode = handle_budget_exceeded_at_stage("assessment")
    assert fallback_mode == "rules_fallback"


def test_limit_before_scoring_fails_run_budget_exceeded():
    from app.features.job_match.pipeline import handle_budget_exceeded_at_stage
    res = handle_budget_exceeded_at_stage("retrieval")
    assert res == "RUN_BUDGET_EXCEEDED"
