from datetime import UTC, datetime
from typing import Any

from pydantic_ai import Agent
from sqlalchemy.ext.asyncio import AsyncSession

from app.agents.deps import AgentDeps
from app.agents.subagent import create_skill_agent
from app.core.errors import AppError
from app.db.models import CvImprovementSession
from app.db.repositories.cv_improvement import (
    CvDecisionType,
    CvImprovementRepository,
    CvImprovementStep,
)


def format_decisions_for_prompt(proposals: dict[str, Any], user_decisions: dict[str, Any]) -> str:
    """Formats proposals and user review decisions for the apply-cv-revisions skill prompt."""
    suggestions = proposals.get("suggestions", [])
    if not suggestions:
        return "Không có đề xuất thay đổi nào."

    lines = []
    for s in suggestions:
        s_id = s.get("id")
        decision_info = user_decisions.get(s_id, {})
        decision_type = decision_info.get("decision", CvDecisionType.REJECTED)

        if decision_type == CvDecisionType.APPROVED:
            revised_text = s.get("suggested_revised_text", "")
            lines.append(f'- Gợi ý {s_id}: APPROVED\n  Nội dung mới: "{revised_text}"')
        elif decision_type == CvDecisionType.EDITED:
            final_text = decision_info.get("final_text") or s.get("suggested_revised_text", "")
            lines.append(
                f'- Gợi ý {s_id}: EDITED (Người dùng tự sửa)\n  Nội dung mới: "{final_text}"'
            )
        else:
            lines.append(f"- Gợi ý {s_id}: REJECTED (Giữ nguyên văn bản gốc)")

    return "\n".join(lines)


class CvImprovementWorkflow:
    def __init__(
        self,
        db: AsyncSession,
        suggest_agent: Agent | None = None,
        apply_agent: Agent | None = None,
    ):
        self.db = db
        self.repo = CvImprovementRepository(db)
        self._suggest_agent = suggest_agent
        self._apply_agent = apply_agent

    async def get_session(
        self, session_id: str, user_id: str | None = None
    ) -> CvImprovementSession:
        session = await self.repo.get_session(session_id)
        if not session:
            raise AppError(
                status_code=404,
                message=f"CV Improvement session '{session_id}' not found.",
                error_code="CV_SESSION_NOT_FOUND",
            )
        if user_id is not None and session.user_id != user_id:
            raise AppError(
                status_code=403,
                message="Access denied to this session.",
                error_code="FORBIDDEN",
            )
        return session

    async def start_session(
        self,
        user_id: str,
        original_cv_text: str,
        target_jd_text: str,
        chat_session_id: str | None = None,
    ) -> CvImprovementSession:
        return await self.repo.create_session(
            user_id=user_id,
            original_cv_text=original_cv_text,
            target_jd_text=target_jd_text,
            chat_session_id=chat_session_id,
        )

    async def analyze(
        self,
        session_id: str,
        user_id: str | None = None,
        deps: AgentDeps | None = None,
    ) -> CvImprovementSession:
        session = await self.get_session(session_id, user_id=user_id)

        # Transition status to ANALYZING
        await self.repo.transition_step(session.id, CvImprovementStep.ANALYZING)

        prompt = (
            f"# CV CỦA ỨNG VIÊN\n{session.original_cv_text}\n\n"
            f"---\n\n"
            f"# JOB DESCRIPTION (JD)\n{session.target_jd_text}"
        )

        agent = self._suggest_agent or create_skill_agent("suggest-cv-improvements")
        run_res = await agent.run(prompt, deps=deps)

        updated = await self.repo.save_suggestions(session.id, run_res.output, auto_transition=True)
        return updated or session

    async def decide(
        self,
        session_id: str,
        suggestion_id: str,
        decision: str | CvDecisionType,
        user_text: str | None = None,
        user_id: str | None = None,
    ) -> CvImprovementSession:
        return await self.batch_decide(
            session_id=session_id,
            decisions=[
                {
                    "suggestion_id": suggestion_id,
                    "decision": decision,
                    "user_text": user_text,
                }
            ],
            user_id=user_id,
        )

    async def batch_decide(
        self,
        session_id: str,
        decisions: list[dict[str, Any]],
        user_id: str | None = None,
    ) -> CvImprovementSession:
        session = await self.get_session(session_id, user_id=user_id)

        if session.status != CvImprovementStep.WAITING_USER_REVIEW:
            raise AppError(
                status_code=400,
                message=f"Cannot record decisions: session is currently in '{session.status}' state. Expected 'WAITING_USER_REVIEW'.",
                error_code="INVALID_SESSION_STATE",
            )

        valid_decisions = {d.value for d in CvDecisionType}
        now_iso = datetime.now(UTC).isoformat()
        decisions_map: dict[str, dict[str, Any]] = {}
        for d in decisions:
            s_id = d.get("suggestion_id")
            dec = d.get("decision")
            if s_id and dec:
                dec_val = dec.value if isinstance(dec, CvDecisionType) else str(dec)
                if dec_val not in valid_decisions:
                    raise AppError(
                        status_code=400,
                        message=f"Invalid decision '{dec_val}'. Must be one of: {sorted(valid_decisions)}.",
                        error_code="INVALID_DECISION",
                    )
                u_text = d.get("user_text")
                if dec_val == CvDecisionType.EDITED and not (u_text and u_text.strip()):
                    raise AppError(
                        status_code=400,
                        message="user_text is required when decision is EDITED.",
                        error_code="USER_TEXT_REQUIRED",
                    )
                decisions_map[s_id] = {
                    "decision": dec_val,
                    "final_text": u_text,
                    "updated_at": now_iso,
                }

        if decisions_map:
            updated = await self.repo.update_all_decisions(session.id, decisions_map)
            return updated or session
        return session

    async def resume(
        self,
        session_id: str,
        user_id: str | None = None,
        deps: AgentDeps | None = None,
    ) -> CvImprovementSession:
        session = await self.get_session(session_id, user_id=user_id)

        if session.status != CvImprovementStep.WAITING_USER_REVIEW:
            raise AppError(
                status_code=400,
                message=f"Cannot resume session from status '{session.status}'. Expected 'WAITING_USER_REVIEW'.",
                error_code="INVALID_SESSION_STATE",
            )

        # Transition to APPLYING_CHANGES
        await self.repo.transition_step(session.id, CvImprovementStep.APPLYING_CHANGES)

        decisions_prompt = format_decisions_for_prompt(
            session.proposals or {}, session.user_decisions or {}
        )
        prompt = (
            f"# CV GỐC\n{session.original_cv_text}\n\n"
            f"---\n\n"
            f"# QUYẾT ĐỊNH CỦA NGƯỜI DÙNG (USER DECISIONS)\n{decisions_prompt}"
        )

        agent = self._apply_agent or create_skill_agent("apply-cv-revisions")
        run_res = await agent.run(prompt, deps=deps)

        updated = await self.repo.save_revised_resume(session.id, run_res.output)
        return updated or session

    async def recovery(self, session_id: str, user_id: str | None = None) -> CvImprovementSession:
        """Rollbacks session state, resetting all user decisions and clearing revised data."""
        session = await self.get_session(session_id, user_id=user_id)

        # Reverts decisions, revised resume data and resets status back to WAITING_USER_REVIEW
        recovered = await self.repo.reset_decisions(
            session_id=session.id,
            reset_step_to=CvImprovementStep.WAITING_USER_REVIEW,
        )
        return recovered or session
