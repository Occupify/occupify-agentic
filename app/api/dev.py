import asyncio
import json

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse

from app.core.config import get_settings
from app.core.errors import AppError
from app.core.logging import get_recent_logs, subscribe_logs, unsubscribe_logs
from app.core.responses import success_response
from app.documents.extract import extract_pdf_text, validate_upload_file
from app.privacy.gate import clean

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
