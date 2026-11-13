import uuid
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import CvImprovementSession


class CvImprovementStep(StrEnum):
    INIT = "INIT"
    ANALYZING = "ANALYZING"
    WAITING_USER_REVIEW = "WAITING_USER_REVIEW"
    REVISING = "REVISING"
    APPLYING_CHANGES = "APPLYING_CHANGES"
    PDF_GENERATED = "PDF_GENERATED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class CvDecisionType(StrEnum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    EDITED = "EDITED"
    REQUEST_ALTERNATIVE = "REQUEST_ALTERNATIVE"


class CvImprovementRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_session(
        self,
        user_id: str,
        original_cv_text: str,
        target_jd_text: str,
        chat_session_id: str | None = None,
    ) -> CvImprovementSession:
        now = datetime.now(UTC)
        cv_session = CvImprovementSession(
            id=str(uuid.uuid4()),
            user_id=user_id,
            chat_session_id=chat_session_id,
            status=CvImprovementStep.INIT,
            original_cv_text=original_cv_text,
            target_jd_text=target_jd_text,
            proposals={},
            user_decisions={},
            revised_resume_data=None,
            pdf_url=None,
            created_at=now,
            updated_at=now,
        )
        self.session.add(cv_session)
        await self.session.commit()
        await self.session.refresh(cv_session)
        return cv_session

    async def get_session(
        self,
        session_id: str,
        user_id: str | None = None,
    ) -> CvImprovementSession | None:
        stmt = select(CvImprovementSession).where(CvImprovementSession.id == session_id)
        if user_id is not None:
            stmt = stmt.where(CvImprovementSession.user_id == user_id)
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def list_sessions(
        self,
        user_id: str,
        limit: int = 20,
        offset: int = 0,
    ) -> list[CvImprovementSession]:
        stmt = (
            select(CvImprovementSession)
            .where(CvImprovementSession.user_id == user_id)
            .order_by(desc(CvImprovementSession.updated_at))
            .offset(offset)
            .limit(limit)
        )
        res = await self.session.execute(stmt)
        return list(res.scalars().all())

    async def save_suggestions(
        self,
        session_id: str,
        proposals: dict[str, Any] | BaseModel,
        auto_transition: bool = True,
    ) -> CvImprovementSession | None:
        cv_session = await self.get_session(session_id)
        if not cv_session:
            return None

        proposal_dict = (
            proposals.model_dump() if isinstance(proposals, BaseModel) else dict(proposals)
        )
        cv_session.proposals = proposal_dict
        if auto_transition:
            cv_session.status = CvImprovementStep.WAITING_USER_REVIEW
        cv_session.updated_at = datetime.now(UTC)

        await self.session.commit()
        await self.session.refresh(cv_session)
        return cv_session

    async def update_suggestion_decision(
        self,
        session_id: str,
        suggestion_id: str,
        decision: str | CvDecisionType,
        user_text: str | None = None,
    ) -> CvImprovementSession | None:
        cv_session = await self.get_session(session_id)
        if not cv_session:
            return None

        current_decisions = dict(cv_session.user_decisions or {})
        decision_str = str(decision.value if isinstance(decision, CvDecisionType) else decision)

        current_decisions[suggestion_id] = {
            "decision": decision_str,
            "final_text": user_text,
            "updated_at": datetime.now(UTC).isoformat(),
        }

        cv_session.user_decisions = current_decisions
        cv_session.updated_at = datetime.now(UTC)

        await self.session.commit()
        await self.session.refresh(cv_session)
        return cv_session

    async def update_all_decisions(
        self,
        session_id: str,
        decisions: dict[str, dict[str, Any]],
    ) -> CvImprovementSession | None:
        cv_session = await self.get_session(session_id)
        if not cv_session:
            return None

        current = dict(cv_session.user_decisions or {})
        current.update(decisions)
        cv_session.user_decisions = current
        cv_session.updated_at = datetime.now(UTC)

        await self.session.commit()
        await self.session.refresh(cv_session)
        return cv_session

    async def transition_step(
        self,
        session_id: str,
        new_step: str | CvImprovementStep,
    ) -> CvImprovementSession | None:
        cv_session = await self.get_session(session_id)
        if not cv_session:
            return None

        step_str = str(new_step.value if isinstance(new_step, CvImprovementStep) else new_step)
        cv_session.status = step_str
        cv_session.updated_at = datetime.now(UTC)

        await self.session.commit()
        await self.session.refresh(cv_session)
        return cv_session

    async def save_revised_resume(
        self,
        session_id: str,
        resume_data: dict[str, Any] | BaseModel,
        pdf_url: str | None = None,
    ) -> CvImprovementSession | None:
        cv_session = await self.get_session(session_id)
        if not cv_session:
            return None

        resume_dict = (
            resume_data.model_dump() if isinstance(resume_data, BaseModel) else dict(resume_data)
        )
        cv_session.revised_resume_data = resume_dict
        if pdf_url is not None:
            cv_session.pdf_url = pdf_url
        cv_session.updated_at = datetime.now(UTC)

        await self.session.commit()
        await self.session.refresh(cv_session)
        return cv_session

    async def reset_decisions(
        self,
        session_id: str,
        reset_step_to: str | CvImprovementStep = CvImprovementStep.WAITING_USER_REVIEW,
    ) -> CvImprovementSession | None:
        """Rollback decisions and revised data to initial review state."""
        cv_session = await self.get_session(session_id)
        if not cv_session:
            return None

        cv_session.user_decisions = {}
        cv_session.revised_resume_data = None
        cv_session.pdf_url = None
        cv_session.status = str(
            reset_step_to.value if isinstance(reset_step_to, CvImprovementStep) else reset_step_to
        )
        cv_session.updated_at = datetime.now(UTC)

        await self.session.commit()
        await self.session.refresh(cv_session)
        return cv_session

    async def delete_session(
        self,
        session_id: str,
        user_id: str | None = None,
    ) -> bool:
        cv_session = await self.get_session(session_id, user_id=user_id)
        if not cv_session:
            return False

        await self.session.delete(cv_session)
        await self.session.commit()
        return True

