from enum import StrEnum

from pydantic_ai.usage import RunUsage, UsageLimits

from app.core.config import get_settings


class StopReason(StrEnum):
    LOOP = "loop"
    STALL = "stall"
    GOAL_REACHED = "goal_reached"
    INVALID_TOOL_USE = "invalid_tool_use"
    BUDGET_REQUESTS = "budget_requests"
    BUDGET_TOOL_CALLS = "budget_tool_calls"
    BUDGET_INPUT_TOKENS = "budget_input_tokens"
    BUDGET_OUTPUT_TOKENS = "budget_output_tokens"
    MODEL_DONE = "model_done"


class HarnessStop(Exception):
    """Raised by tools or harness to stop agent execution early with a known reason."""

    def __init__(self, reason: StopReason | str) -> None:
        self.reason = StopReason(reason) if isinstance(reason, str) else reason
        super().__init__(f"Harness stopped: {self.reason}")


class BudgetExceeded(Exception):
    """Raised when an explicit budget limit (requests, tool calls, tokens) is exceeded."""

    def __init__(self, kind: str) -> None:
        self.kind = kind
        super().__init__(f"Budget exceeded for kind: {kind}")


class LoopDetector:
    """Detects repetitive tool invocations within the last N calls."""

    def __init__(self, window_size: int = 6) -> None:
        self.window_size = window_size
        self.history: list[tuple[str, tuple[str, ...]]] = []
        self.repeat_counts: dict[tuple[str, tuple[str, ...]], int] = {}

    def check(self, query: str, skills: list[str]) -> str | None:
        norm_query = query.strip().lower()
        norm_skills = tuple(sorted(s.strip().lower() for s in skills))
        key = (norm_query, norm_skills)

        # Check in history
        if key in self.history:
            self.repeat_counts[key] = self.repeat_counts.get(key, 0) + 1
            if self.repeat_counts[key] >= 2:
                raise HarnessStop(StopReason.LOOP)
            return "duplicate"

        self.history.append(key)
        if len(self.history) > self.window_size:
            oldest = self.history.pop(0)
            if oldest in self.repeat_counts and oldest not in self.history:
                del self.repeat_counts[oldest]
        return None


class StageUsageLimits(UsageLimits):
    @property
    def request_tokens_limit(self) -> int | None:
        return self.input_tokens_limit

    @property
    def response_tokens_limit(self) -> int | None:
        return self.output_tokens_limit


class RunBudget:
    """Tracks token, request, and tool call usage across an entire job match run."""

    def __init__(self) -> None:
        self.usage = RunUsage()
        self.rejected_calls: int = 0
        settings = get_settings()
        self.max_requests = getattr(settings, "JOB_MATCH_MAX_REQUESTS", 60)
        self.max_input_tokens = getattr(settings, "JOB_MATCH_MAX_INPUT_TOKENS", 2_000_000)
        self.max_output_tokens = getattr(settings, "JOB_MATCH_MAX_OUTPUT_TOKENS", 300_000)
        self.max_tool_calls = getattr(settings, "JOB_MATCH_MAX_TOOL_CALLS", 15)

    def record_rejected_call(self) -> None:
        self.rejected_calls += 1

    def limits_for(self, stage: str) -> UsageLimits:
        requests_now = getattr(self.usage, "requests", 0) or 0

        stage_caps = {
            "profile": 1,
            "search": 40,
            "skill_match": 10,
            "assessment": 20,
        }
        stage_max = stage_caps.get(stage, 5)
        req_limit = min(self.max_requests, requests_now + stage_max)

        tool_calls_limit = self.max_tool_calls if stage == "search" else None

        return StageUsageLimits(
            request_limit=req_limit,
            input_tokens_limit=self.max_input_tokens,
            output_tokens_limit=self.max_output_tokens,
            tool_calls_limit=tool_calls_limit,
            total_tokens_limit=None,
        )
