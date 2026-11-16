from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.errors import AppError
from app.core.responses import success_response
from app.core.security import CurrentUser, get_current_user
from app.core.storage import LocalStorageClient, get_storage_client
from app.db.session import get_db_session
from app.features.cv_improvement.schemas import (
    BatchCvDecisionRequest,
    CreateCvSessionRequest,
    CvDecisionRequest,
    CvSessionResponse,
)
from app.features.cv_improvement.tools import execute_cv_finalization
from app.features.cv_improvement.workflow import CvImprovementWorkflow

router = APIRouter(prefix="/ai/cv-improvement", tags=["cv-improvement"])


def session_to_dict(session) -> dict:
    return CvSessionResponse.model_validate(session).model_dump(mode="json")


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
    return success_response(session_to_dict(session), message="Session created", status_code=201)


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
    return success_response(session_to_dict(session), message="Workflow state rolled back")


@router.post("/{session_id}/generate")
async def generate_cv_endpoint(
    session_id: str,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    ok, message, data = await execute_cv_finalization(
        db=db,
        session_id=session_id,
        user_id=user.user_id,
    )
    if not ok:
        raise AppError(
            status_code=400,
            message=message,
            error_code=data.get("error_code", "GENERATION_FAILED"),
        )
    workflow = CvImprovementWorkflow(db)
    session = await workflow.get_session(session_id, user_id=user.user_id)
    return success_response(session_to_dict(session), message=message)


@router.get("/download/{filename}")
async def download_cv_artifact(filename: str):
    storage = get_storage_client()
    if hasattr(storage, "get_file_path"):
        path = storage.get_file_path(filename)
    else:
        path = LocalStorageClient().get_file_path(filename)
    if not path or not path.is_file():
        raise AppError(
            status_code=404,
            message=f"File '{filename}' not found or has expired.",
            error_code="FILE_NOT_FOUND",
        )
    MEDIA_TYPES = {".pdf": "application/pdf", ".tex": "application/x-tex; charset=utf-8"}
    media_type = MEDIA_TYPES.get(path.suffix.lower(), "application/octet-stream")
    return FileResponse(path, media_type=media_type, filename=path.name)
