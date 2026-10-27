import logging
from typing import Any

from fastapi import APIRouter, Depends, File, Form, Query, UploadFile
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.errors import AppError
from app.core.responses import success_response
from app.core.security import CurrentUser, get_current_user
from app.db.models import JobMatchResult, JobMatchRun
from app.db.session import get_db_session
from app.features.job_match.schemas import (
    ExperienceLevelFilter,
    HoursPerDayFilter,
    MatchCriteria,
    SalaryTypeFilter,
)
from app.features.job_match.service import start_job_match

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/ai/job-matches", tags=["job-match"])


@router.post("", status_code=202)
async def create_job_match(
    file: UploadFile = File(...),
    salaryType: SalaryTypeFilter | None = Form(None),
    minBudget: float | None = Form(None),
    maxBudget: float | None = Form(None),
    experienceLevel: ExperienceLevelFilter | None = Form(None),
    hoursPerDay: HoursPerDayFilter | None = Form(None),
    limit: int = Form(10),
    lang: str = Form("vi"),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
) -> JSONResponse:
    """Uploads CV PDF, starts async CV-job match run, returns 202 Accepted with runId."""
    # 1. Validate file extension and MIME type
    filename = (file.filename or "").lower()
    content_type = (file.content_type or "").lower()
    if not filename.endswith(".pdf") and content_type != "application/pdf":
        raise AppError(
            status_code=400,
            message="Failed to upload file: file must be a valid PDF document.",
            error_code="FILE_INVALID",
        )

    # 2. Read content and validate PDF magic header and size
    pdf_bytes = await file.read()
    if not pdf_bytes.startswith(b"%PDF-"):
        raise AppError(
            status_code=400,
            message="Failed to upload file: file magic bytes indicate it is not a valid PDF.",
            error_code="FILE_INVALID",
        )

    settings = get_settings()
    if len(pdf_bytes) > settings.JOB_MATCH_MAX_FILE_BYTES:
        raise AppError(
            status_code=400,
            message=f"Failed to upload file: file size exceeds {settings.JOB_MATCH_MAX_FILE_BYTES} bytes.",
            error_code="FILE_TOO_LARGE",
        )

    # 3. Validate criteria
    try:
        criteria = MatchCriteria(
            salary_type=salaryType,
            min_budget=minBudget,
            max_budget=maxBudget,
            experience_level=experienceLevel,
            hours_per_day=hoursPerDay,
            limit=limit,
            lang=lang,
        )
    except AppError:
        raise
    except ValidationError as exc:
        raise AppError(
            status_code=422,
            message=f"Validation error: {exc}",
            error_code="VALIDATION_ERROR",
        ) from exc

    # 4. Enforce user busy lock and start background task
    run = await start_job_match(user=user, pdf_bytes=pdf_bytes, criteria=criteria, db=db)

    return JSONResponse(
        status_code=202,
        content={
            "statusCode": 202,
            "message": "Accepted",
            "data": {
                "runId": run.id,
                "status": "queued",
            },
        },
    )


@router.get("/{run_id}")
async def get_job_match_run(
    run_id: str,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
) -> dict[str, Any]:
    """Retrieves detailed status, diagnostics, and match results for a specific run."""
    run = await db.get(JobMatchRun, run_id)
    if not run or run.user_id != user.user_id:
        raise AppError(
            status_code=404,
            message="Failed to find job match run.",
            error_code="JOB_MATCH_NOT_FOUND",
        )

    stmt = (
        select(JobMatchResult)
        .where(JobMatchResult.run_id == run_id)
        .order_by(JobMatchResult.rank.asc())
    )
    result_rows = (await db.execute(stmt)).scalars().all()

    items = []
    for r in result_rows:
        proj_title = ""
        if r.jobs and isinstance(r.jobs, list) and len(r.jobs) > 0:
            first_job = r.jobs[0]
            if isinstance(first_job, dict):
                proj_title = first_job.get("projectTitle") or first_job.get("project_title") or ""

        items.append(
            {
                "rank": r.rank,
                "projectId": r.project_id,
                "projectTitle": proj_title or r.project_id,
                "matchScore": int(r.match_score),
                "verified": r.verified,
                "jobs": r.jobs or [],
            }
        )

    detail = {
        "runId": run.id,
        "status": run.status,
        "stage": run.stage,
        "outcome": run.outcome,
        "stopReason": run.stop_reason,
        "errorCode": run.error_code,
        "message": run.message,
        "warnings": run.warnings or [],
        "criteria": run.criteria,
        "topMissingSkills": run.top_missing_skills or [],
        "items": items,
    }

    return success_response(detail)


@router.get("")
async def list_job_matches(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
) -> dict[str, Any]:
    """Lists paged historical job match runs for the authenticated user without items."""
    count_stmt = select(func.count(JobMatchRun.id)).where(JobMatchRun.user_id == user.user_id)
    total = (await db.execute(count_stmt)).scalar() or 0

    stmt = (
        select(JobMatchRun)
        .where(JobMatchRun.user_id == user.user_id)
        .order_by(JobMatchRun.created_at.desc())
        .offset((page - 1) * limit)
        .limit(limit)
    )
    runs = (await db.execute(stmt)).scalars().all()

    items = [
        {
            "runId": r.id,
            "status": r.status,
            "stage": r.stage,
            "outcome": r.outcome,
            "stopReason": r.stop_reason,
            "errorCode": r.error_code,
            "message": r.message,
            "warnings": r.warnings or [],
            "criteria": r.criteria,
            "topMissingSkills": r.top_missing_skills or [],
            "createdAt": r.created_at.isoformat() if r.created_at else None,
            "finishedAt": r.finished_at.isoformat() if r.finished_at else None,
        }
        for r in runs
    ]

    total_pages = (total + limit - 1) // limit if limit > 0 else 1
    return {
        "statusCode": 200,
        "message": "OK",
        "data": {
            "data": items,
            "paging": {
                "page": page,
                "limit": limit,
                "total": total,
                "totalPages": total_pages,
            },
        },
    }
