import asyncio
import json
from typing import Any

from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import StreamingResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.errors import AppError
from app.core.logging import get_recent_logs, subscribe_logs, unsubscribe_logs
from app.core.responses import success_response
from app.db.models import ChatSession
from app.db.session import get_db_session
from app.documents.extract import extract_pdf_text, validate_upload_file
from app.memory.service import MemoryService
from app.privacy.gate import clean
from app.state.task_progress import TaskProgressManager

router = APIRouter(prefix="/ai/dev", tags=["dev"])


@router.post("/cv-preview")
async def cv_preview(file: UploadFile = File(...)):
    settings = get_settings()
    if settings.APP_ENV not in ("local", "test"):
        raise AppError(404, "Endpoint not found.", "NOT_FOUND")

    filename = file.filename or "cv.pdf"
    content, page_count = await validate_upload_file(file)
    raw_text, pages, extractor_used = await asyncio.to_thread(extract_pdf_text, content)
    cleaned_text, removed = clean(raw_text, source="cv_preview", is_file=True)

    return success_response(
        {
            "filename": filename,
            "pageCount": page_count,
            "extractor": extractor_used,
            "removedCounts": removed,
            "cleanedText": cleaned_text,
        }
    )


@router.get("/logs")
async def get_logs(
    limit: int = 200,
    sessionId: str | None = None,
):
    settings = get_settings()
    if settings.APP_ENV not in ("local", "test"):
        raise AppError(404, "Endpoint not found.", "NOT_FOUND")

    limit = max(1, min(1000, limit))
    entries = get_recent_logs(limit=limit, session_id=sessionId)
    return success_response(data=entries)


@router.get("/logs/stream")
async def stream_logs(sessionId: str | None = None):
    settings = get_settings()
    if settings.APP_ENV not in ("local", "test"):
        raise AppError(404, "Endpoint not found.", "NOT_FOUND")

    q, sub = subscribe_logs()

    async def event_generator():
        try:
            while True:
                try:
                    entry = await asyncio.wait_for(
                        q.get(), timeout=float(settings.CHAT_STREAM_HEARTBEAT_S)
                    )
                    if sessionId and entry.get("session_id") != sessionId:
                        continue
                    data_str = json.dumps(entry, ensure_ascii=False)
                    yield f"event: log\ndata: {data_str}\n\n"
                except TimeoutError:
                    yield ": ping\n\n"
        finally:
            unsubscribe_logs(sub)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@router.get("/state/{session_id}")
async def get_session_state(
    session_id: str,
    db: AsyncSession = Depends(get_db_session),
):
    settings = get_settings()
    if settings.APP_ENV not in ("local", "test"):
        raise AppError(404, "Endpoint not found.", "NOT_FOUND")

    stmt = select(ChatSession).where(ChatSession.id == session_id)
    res = await db.execute(stmt)
    chat_sess = res.scalar_one_or_none()

    state_mgr = TaskProgressManager(db)
    mem_svc = MemoryService(db)

    latest_cp = await state_mgr.get_latest_checkpoint(session_id)
    history_cps = await state_mgr.get_checkpoint_history(session_id)

    user_id = chat_sess.user_id if chat_sess else (latest_cp.user_id if latest_cp else None)
    active_memory_items: list[dict[str, Any]] = []
    if user_id:
        active_mem = await mem_svc.get_active_memory(user_id)
        active_memory_items = [m.model_dump(mode="json") for m in active_mem.items]

    return success_response(
        data={
            "session_id": session_id,
            "latest_checkpoint": latest_cp.model_dump(mode="json") if latest_cp else None,
            "checkpoints_history": [cp.model_dump(mode="json") for cp in history_cps],
            "active_user_memory": active_memory_items,
        }
    )
