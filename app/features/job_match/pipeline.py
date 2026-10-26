from typing import Any

from app.core.security import CurrentUser
from app.features.job_match.ports import PipelineOptions, PipelineResult, RunState


def handle_budget_exceeded_at_stage(stage: str) -> str:
    """Returns the budget exceeded fallback action based on current pipeline stage."""
    if stage in ("assessment", "skill_match", "s5b", "s9"):
        return "rules_fallback"
    if stage == "search":
        return "stop_budget"
    return "RUN_BUDGET_EXCEEDED"


async def run_pipeline(
    state: RunState,
    pdf_bytes: bytes,
    user: CurrentUser,
    store: Any,
    options: PipelineOptions | None = None,
) -> PipelineResult:
    """Full UC4 pipeline orchestrator (S0-S10). To be completed in T-15."""
    raise NotImplementedError("run_pipeline will be implemented in T-15")
