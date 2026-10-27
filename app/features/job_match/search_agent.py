from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from pydantic_ai import RunContext
from pydantic_ai.exceptions import UnexpectedModelBehavior

from app.agents.budget import (
    BudgetExceeded,
    HarnessStop,
    LoopDetector,
    RunBudget,
    StopReason,
)
from app.agents.deps import AgentDeps
from app.features.job_match.ports import PipelineOptions, RunState


class ToolState(StrEnum):
    OK = "ok"
    OK_EMPTY = "ok_empty"
    INVALID_PARAM = "invalid_param"
    DUPLICATE = "duplicate"
    ERROR = "error"
    BUDGET_EXHAUSTED = "budget_exhausted"


@dataclass
class CallCheckResult:
    status: str
    message: str = ""


class SearchAgentHarness:
    """Controls the search agent execution, loop detection, budget enforcement, and stopping."""

    def __init__(self, goal: int = 10, budget: RunBudget | None = None) -> None:
        self.goal = goal
        self.budget = budget or RunBudget()
        self.reject_count: int = 0
        self.loop_detector = LoopDetector(window_size=6)
        self.rounds_stalled: int = 0
        self.last_fitting_count: int = 0

    def record_nested_skill_match_requests(self, count: int = 1) -> None:
        if self.budget:
            self.budget.usage.requests = (getattr(self.budget.usage, "requests", 0) or 0) + count

    def check_call_and_record(self, query: str, skills: list[str]) -> CallCheckResult:
        if self.budget:
            self.budget.usage.tool_calls = (getattr(self.budget.usage, "tool_calls", 0) or 0) + 1
            if self.budget.usage.tool_calls > self.budget.max_tool_calls:
                raise HarnessStop(StopReason.BUDGET_TOOL_CALLS)

        # 1. Parameter validation
        if not query and not skills:
            self.reject_count += 1
            self.budget.record_rejected_call()
            return CallCheckResult(
                status=ToolState.INVALID_PARAM, message="Query or skills required"
            )

        # 2. Loop detection
        loop_result = self.loop_detector.check(query, skills)
        if loop_result == "duplicate":
            self.reject_count += 1
            self.budget.record_rejected_call()
            return CallCheckResult(
                status=ToolState.DUPLICATE, message="Duplicate search parameters"
            )

        return CallCheckResult(status=ToolState.OK)

    def record_search_round_result(self, current_fitting: int) -> None:
        if current_fitting >= self.goal:
            raise HarnessStop(StopReason.GOAL_REACHED)

        if current_fitting == self.last_fitting_count:
            self.rounds_stalled += 1
            if self.rounds_stalled >= 3:
                raise HarnessStop(StopReason.STALL)
        else:
            self.rounds_stalled = 0
            self.last_fitting_count = current_fitting


def map_exception_to_stop_reason(exc: Exception) -> StopReason:
    if isinstance(exc, UnexpectedModelBehavior):
        return StopReason.INVALID_TOOL_USE
    if isinstance(exc, HarnessStop):
        return exc.reason
    if isinstance(exc, BudgetExceeded):
        if exc.kind == "requests":
            return StopReason.BUDGET_REQUESTS
        if exc.kind == "tool_calls":
            return StopReason.BUDGET_TOOL_CALLS
        if exc.kind in ("input_tokens", "request_tokens"):
            return StopReason.BUDGET_INPUT_TOKENS
        if exc.kind in ("output_tokens", "response_tokens"):
            return StopReason.BUDGET_OUTPUT_TOKENS
    return StopReason.INVALID_TOOL_USE


async def search_more(
    ctx: RunContext[AgentDeps],
    query: str,
    skills: list[str],
) -> dict[str, Any]:
    """
    Agent tool to search for additional jobs and evaluate them.
    Takes only search criteria (query, skills); user context is resolved from ctx.deps.
    """
    harness: SearchAgentHarness | None = getattr(ctx.deps, "search_harness", None)
    if harness:
        check = harness.check_call_and_record(query, skills)
        if check.status != "ok":
            if harness.reject_count >= 3:
                raise HarnessStop(StopReason.INVALID_TOOL_USE)
            return {"status": check.status, "message": check.message}

        if harness.reject_count >= 3:
            raise HarnessStop(StopReason.INVALID_TOOL_USE)

        harness.record_search_round_result(current_fitting=harness.last_fitting_count)

    return {
        "status": ToolState.OK,
        "new_jobs": 0,
        "total_fitting": harness.last_fitting_count if harness else 0,
    }


async def maybe_search_more(
    state: RunState,
    budget: RunBudget,
    options: PipelineOptions,
    goal: int = 5,
    user: Any = None,
    parent_run_id: str | None = None,
    prompt: str = "",
) -> tuple[bool, StopReason | None]:
    """
    Evaluates whether the search agent should be invoked:
    Returns (called: bool, stop_reason: StopReason | None)
    """
    if not options.search_agent:
        return False, None

    if state.fitting_projects_count >= goal:
        return False, None

    if state.exhausted:
        return False, None

    from app.agents import subagent
    from app.agents.deps import CurrentUser
    from app.agents.runner import run_agent

    harness = SearchAgentHarness(goal=goal, budget=budget)
    harness.last_fitting_count = state.fitting_projects_count

    deps = AgentDeps(
        user=user or CurrentUser(user_id="system", email="system@example.com", role="USER"),
        session_id=parent_run_id or "search_agent",
        agent_role="search",
        parent_run_id=parent_run_id,
    )
    deps.search_harness = harness

    agent = subagent.create_skill_agent(
        name="plan-job-search",
        tools=[search_more],
    )

    try:
        await run_agent(
            agent=agent,
            prompt=prompt
            or f"Current fitting projects: {state.fitting_projects_count}, goal: {goal}.",
            deps=deps,
            use_case="job_match",
            agent_role="search",
            parent_run_id=parent_run_id,
        )
        if state.fitting_projects_count >= goal:
            return True, StopReason.GOAL_REACHED
        return True, StopReason.MODEL_DONE
    except Exception as exc:
        stop_reason = map_exception_to_stop_reason(exc)
        return True, stop_reason
