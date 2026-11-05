import asyncio
from typing import Any

from pydantic_ai import RunContext

from app.agents.deps import AgentDeps
from app.memory.schemas import MemoryItemCreate
from app.memory.service import MemoryService
from app.state.schemas import TaskStateUpdate
from app.state.task_progress import TaskProgressManager


async def record_user_memory(
    ctx: RunContext[AgentDeps],
    category: str,
    key: str,
    value: Any,
    is_confirmed: bool = False,
    confidence: float = 1.0,
    source: str = "user_chat",
) -> str:
    """
    Record or update a persistent user memory fact (e.g. skills, experience, preferences, target roles).
    This memory persists across all sessions for this user.
    """
    if not ctx.deps.db or not ctx.deps.user:
        return "Error: Database session or user unavailable to record memory."

    service = MemoryService(ctx.deps.db)
    item = MemoryItemCreate(
        category=category,
        key=key,
        value=value,
        is_confirmed=is_confirmed,
        confidence=confidence,
        source=source,
    )
    res = await service.record_fact(ctx.deps.user.user_id, item)
    status = "confirmed" if res.is_confirmed else "inferred"
    return f"Recorded memory [{res.category}] {res.key}: {res.value} ({status})."


async def update_consulting_progress(
    ctx: RunContext[AgentDeps],
    stage: str | None = None,
    goal: str | None = None,
    completed_step: str | None = None,
    pending_steps: list[str] | None = None,
    blocker: str | None = None,
    resolve_blocker: str | None = None,
    decision: str | None = None,
    decision_rationale: str | None = None,
    next_action: str | None = None,
) -> str:
    """
    Update consulting task progress, stage transition, checklist, blockers, or decisions, creating a new checkpoint.
    Stages: DISCOVERY -> ASSESSMENT -> PATH_EXPLORATION -> ROADMAP_FORMULATION -> COMPLETED.
    """
    if not ctx.deps.db or not ctx.deps.session_id or not ctx.deps.user:
        return "Error: Active database session, session_id, or user unavailable."

    if stage and ctx.deps.on_progress:
        if asyncio.iscoroutinefunction(ctx.deps.on_progress):
            asyncio.create_task(ctx.deps.on_progress(stage))
        else:
            ctx.deps.on_progress(stage)

    manager = TaskProgressManager(ctx.deps.db)
    decisions_add = (
        [{"decision": decision, "rationale": decision_rationale or ""}] if decision else None
    )
    update = TaskStateUpdate(
        stage=stage,
        goal=goal,
        completed_steps_add=[completed_step] if completed_step else None,
        pending_steps=pending_steps,
        blockers_add=[blocker] if blocker else None,
        blockers_resolve=[resolve_blocker] if resolve_blocker else None,
        decisions_add=decisions_add,
        next_action=next_action,
    )

    cp = await manager.update_and_checkpoint(
        session_id=ctx.deps.session_id,
        user_id=ctx.deps.user.user_id,
        task_type="career_consulting",
        update=update,
    )
    return f"Checkpoint saved (seq={cp.checkpoint_seq}): stage={cp.stage}, next_action={cp.next_action}"
