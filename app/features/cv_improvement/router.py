from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.responses import success_response
from app.core.security import CurrentUser, get_current_user
from app.db.session import get_db_session
from app.features.cv_improvement.schemas import (
    BatchCvDecisionRequest,
    CreateCvSessionRequest,
    CvDecisionRequest,
)
from app.features.cv_improvement.workflow import CvImprovementWorkflow

router = APIRouter(prefix="/ai/cv-improvement", tags=["cv-improvement"])


def session_to_dict(session) -> dict:
    return {
        "id": session.id,
        "user_id": session.user_id,
        "chat_session_id": session.chat_session_id,
        "status": session.status,
        "step": session.step,
        "original_cv_text": session.original_cv_text,
        "target_jd_text": session.target_jd_text,
        "proposals": session.proposals,
        "user_decisions": session.user_decisions,
        "revised_resume_data": session.revised_resume_data,
        "pdf_url": session.pdf_url,
        "created_at": session.created_at.isoformat() if session.created_at else None,
        "updated_at": session.updated_at.isoformat() if session.updated_at else None,
    }


@router.post("/sessions")
async def create_session(
    body: CreateCvSessionRequest,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    workflow = CvImprovementWorkflow(db)
    session = await workflow.start_session(
        user_id=user.user_id,
        original_cv_text=body.original_cv_text,
        target_jd_text=body.target_jd_text,
        chat_session_id=body.chat_session_id,
    )
    return success_response(
        session_to_dict(session), message="Session created", status_code=201
    )


@router.get("/{session_id}")
async def get_session(
    session_id: str,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    workflow = CvImprovementWorkflow(db)
    session = await workflow.get_session(session_id, user_id=user.user_id)
    return success_response(session_to_dict(session))


@router.post("/{session_id}/decide")
async def decide_suggestion(
    session_id: str,
    body: CvDecisionRequest,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    workflow = CvImprovementWorkflow(db)
    session = await workflow.decide(
        session_id=session_id,
        suggestion_id=body.suggestion_id,
        decision=body.decision,
        user_text=body.user_text,
        user_id=user.user_id,
    )
    return success_response(session_to_dict(session), message="Decision recorded")


@router.post("/{session_id}/batch-decide")
async def batch_decide(
    session_id: str,
    body: BatchCvDecisionRequest,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    workflow = CvImprovementWorkflow(db)
    decisions = [d.model_dump() for d in body.decisions]
    session = await workflow.batch_decide(
        session_id=session_id,
        decisions=decisions,
        user_id=user.user_id,
    )
    return success_response(session_to_dict(session), message="Decisions recorded")


@router.post("/{session_id}/resume")
async def resume_workflow(
    session_id: str,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    workflow = CvImprovementWorkflow(db)
    session = await workflow.resume(session_id, user_id=user.user_id)
    return success_response(
        session_to_dict(session), message="Workflow resumed and revisions applied"
    )


@router.post("/{session_id}/recovery")
async def recover_workflow(
    session_id: str,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    workflow = CvImprovementWorkflow(db)
    session = await workflow.recovery(session_id, user_id=user.user_id)
    return success_response(
        session_to_dict(session), message="Workflow state rolled back"
    )

