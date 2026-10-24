import asyncio

from fastapi import APIRouter, File, UploadFile

from app.core.config import get_settings
from app.core.errors import AppError
from app.core.responses import success_response
from app.documents.extract import extract_pdf_text
from app.documents.fetch import validate_upload_file
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
