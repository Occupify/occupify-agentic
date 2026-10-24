import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import AgentRun


class RunRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_run(
        self,
        use_case: str,
        user_id: str,
        model: str,
        trace_id: str,
        session_id: str | None = None,
        run_id: str | None = None,
    ) -> AgentRun:
        run = AgentRun(
            id=run_id or str(uuid.uuid4()),
            use_case=use_case,
            user_id=user_id,
            session_id=session_id,
            model=model,
            trace_id=trace_id,
            status="running",
            steps=[],
        )
        self.session.add(run)
        await self.session.commit()
        await self.session.refresh(run)
        return run

    async def finish_success(
        self,
        run_id: str,
        tokens_in: int,
        tokens_out: int,
        latency_ms: int,
        steps: list[Any],
    ) -> None:
        run = await self.session.get(AgentRun, run_id)
        if run:
            run.status = "succeeded"
            run.tokens_in = tokens_in
            run.tokens_out = tokens_out
            run.latency_ms = latency_ms
            run.steps = steps
            run.finished_at = datetime.now(UTC)
            await self.session.commit()

    async def finish_failed(
        self,
        run_id: str,
        error_message: str,
        latency_ms: int,
        steps: list[Any],
    ) -> None:
        run = await self.session.get(AgentRun, run_id)
        if run:
            run.status = "failed"
            run.error = error_message
            run.latency_ms = latency_ms
            run.steps = steps
            run.finished_at = datetime.now(UTC)
            await self.session.commit()
