from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logging import log_step
from app.db.models import TaskCheckpoint, utc_now
from app.state.schemas import TaskCheckpointRead, TaskStateUpdate


class TaskProgressManager:
    def __init__(self, db: AsyncSession):
        self.db = db

    def _to_read_model(self, cp: TaskCheckpoint) -> TaskCheckpointRead:
        return TaskCheckpointRead(
            id=cp.id,
            session_id=cp.session_id,
            user_id=cp.user_id,
            task_type=cp.task_type,
            stage=cp.stage,
            goal=cp.goal,
            constraints=list(cp.constraints or []),
            completed_steps=list(cp.completed_steps or []),
            pending_steps=list(cp.pending_steps or []),
            blockers=list(cp.blockers or []),
            decisions=list(cp.decisions or []),
            next_action=cp.next_action,
            checkpoint_seq=cp.checkpoint_seq,
            created_at=cp.created_at,
        )

    async def get_latest_checkpoint(
        self, session_id: str, task_type: str = "career_consulting", emit_log: bool = False
    ) -> TaskCheckpointRead | None:
        """Retrieves the latest checkpoint for the session and task type, emitting resumption telemetry."""
        stmt = (
            select(TaskCheckpoint)
            .where(
                TaskCheckpoint.session_id == session_id,
                TaskCheckpoint.task_type == task_type,
            )
            .order_by(TaskCheckpoint.checkpoint_seq.desc())
            .limit(1)
        )
        res = await self.db.execute(stmt)
        cp = res.scalar_one_or_none()
        if not cp:
            return None

        read_model = self._to_read_model(cp)

        if emit_log:
            log_step(
                "state.resumed",
                session_id=session_id,
                task_type=task_type,
                checkpoint_seq=read_model.checkpoint_seq,
                stage=read_model.stage,
                next_action=read_model.next_action,
            )
        return read_model

    async def get_latest_user_checkpoint(
        self, user_id: str, task_type: str = "career_consulting"
    ) -> TaskCheckpointRead | None:
        """Retrieves the most recent checkpoint for the user across all sessions."""
        stmt = (
            select(TaskCheckpoint)
            .where(
                TaskCheckpoint.user_id == user_id,
                TaskCheckpoint.task_type == task_type,
            )
            .order_by(TaskCheckpoint.checkpoint_seq.desc(), TaskCheckpoint.created_at.desc())
            .limit(1)
        )
        res = await self.db.execute(stmt)
        cp = res.scalar_one_or_none()
        return self._to_read_model(cp) if cp else None

    async def get_checkpoint_history(self, session_id: str) -> list[TaskCheckpointRead]:
        """Retrieves all historical checkpoints for a session ordered by sequence."""
        stmt = (
            select(TaskCheckpoint)
            .where(TaskCheckpoint.session_id == session_id)
            .order_by(TaskCheckpoint.checkpoint_seq.asc())
        )
        res = await self.db.execute(stmt)
        rows = res.scalars().all()
        return [
            TaskCheckpointRead(
                id=r.id,
                session_id=r.session_id,
                user_id=r.user_id,
                task_type=r.task_type,
                stage=r.stage,
                goal=r.goal,
                constraints=list(r.constraints or []),
                completed_steps=list(r.completed_steps or []),
                pending_steps=list(r.pending_steps or []),
                blockers=list(r.blockers or []),
                decisions=list(r.decisions or []),
                next_action=r.next_action,
                checkpoint_seq=r.checkpoint_seq,
                created_at=r.created_at,
            )
            for r in rows
        ]

    async def update_and_checkpoint(
        self,
        session_id: str,
        user_id: str,
        task_type: str,
        update: TaskStateUpdate,
        initial_goal: str = "Career Consulting Session",
    ) -> TaskCheckpointRead:
        """
        Updates task state and persists a new atomic checkpoint.
        Emits 'state.transition' when moving to a new stage and 'state.checkpoint_saved'.
        """
        latest = await self.get_latest_checkpoint(session_id, task_type=task_type)

        seq = (latest.checkpoint_seq + 1) if latest else 1
        stage = update.stage or (latest.stage if latest else "DISCOVERY")
        goal = update.goal or (latest.goal if latest else initial_goal)

        # Merge constraints
        constraints = list(latest.constraints) if latest else []
        if update.constraints_add:
            for c in update.constraints_add:
                if c not in constraints:
                    constraints.append(c)

        # Merge completed steps
        completed = list(latest.completed_steps) if latest else []
        if update.completed_steps_add:
            for s in update.completed_steps_add:
                if s not in completed:
                    completed.append(s)

        # Pending steps
        if update.pending_steps is not None:
            pending = list(update.pending_steps)
        else:
            pending = list(latest.pending_steps) if latest else []
            # remove any step that was just completed
            if update.completed_steps_add:
                pending = [p for p in pending if p not in update.completed_steps_add]

        # Merge blockers
        blockers = list(latest.blockers) if latest else []
        if update.blockers_add:
            for b in update.blockers_add:
                if b not in blockers:
                    blockers.append(b)
        if update.blockers_resolve:
            blockers = [b for b in blockers if b not in update.blockers_resolve]

        # Merge decisions
        decisions = list(latest.decisions) if latest else []
        if update.decisions_add:
            decisions.extend(update.decisions_add)

        next_action = update.next_action or (latest.next_action if latest else None)

        # Check if stage transitioned
        if latest and latest.stage != stage:
            log_step(
                "state.transition",
                session_id=session_id,
                task_type=task_type,
                from_stage=latest.stage,
                to_stage=stage,
                checkpoint_seq=seq,
            )

        new_cp = TaskCheckpoint(
            session_id=session_id,
            user_id=user_id,
            task_type=task_type,
            stage=stage,
            goal=goal,
            constraints=constraints,
            completed_steps=completed,
            pending_steps=pending,
            blockers=blockers,
            decisions=decisions,
            next_action=next_action,
            checkpoint_seq=seq,
            created_at=utc_now(),
        )
        self.db.add(new_cp)
        await self.db.commit()
        await self.db.refresh(new_cp)

        log_step(
            "state.checkpoint_saved",
            session_id=session_id,
            task_type=task_type,
            stage=stage,
            checkpoint_seq=seq,
            completed_count=len(completed),
            pending_count=len(pending),
            blockers_count=len(blockers),
            decisions_count=len(decisions),
        )

        return TaskCheckpointRead(
            id=new_cp.id,
            session_id=new_cp.session_id,
            user_id=new_cp.user_id,
            task_type=new_cp.task_type,
            stage=new_cp.stage,
            goal=new_cp.goal,
            constraints=list(new_cp.constraints or []),
            completed_steps=list(new_cp.completed_steps or []),
            pending_steps=list(new_cp.pending_steps or []),
            blockers=list(new_cp.blockers or []),
            decisions=list(new_cp.decisions or []),
            next_action=new_cp.next_action,
            checkpoint_seq=new_cp.checkpoint_seq,
            created_at=new_cp.created_at,
        )
