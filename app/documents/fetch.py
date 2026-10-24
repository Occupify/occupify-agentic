from io import BytesIO

import pypdfium2 as pdfium
from fastapi import UploadFile

from app.core.config import get_settings
from app.core.errors import FileInvalidError


def validate_pdf_bytes(content: bytes, filename: str = "document.pdf") -> int:
    """
    Validates PDF bytes:
    - Content not empty
    - Size <= PDF_MAX_BYTES
    - Starts with %PDF magic bytes
    - Decodable and not encrypted/password-protected
    - Page count <= PDF_MAX_PAGES
    Returns the page count if valid.
    """
    settings = get_settings()

    if not content:
        raise FileInvalidError(filename, "file is empty")

    if len(content) > settings.PDF_MAX_BYTES:
        raise FileInvalidError(
            filename,
            f"larger than {settings.PDF_MAX_BYTES // (1024 * 1024)} MB",
        )

    if not content.startswith(b"%PDF"):
        raise FileInvalidError(filename, "not a PDF (invalid file header)")

    try:
        doc = pdfium.PdfDocument(BytesIO(content))
    except Exception as e:
        raise FileInvalidError(filename, f"cannot parse PDF: {e!s}")

    # Check encryption
    try:
        # If encrypted, pypdfium2 raises an exception or doc is invalid without password
        page_count = len(doc)
    except Exception:
        raise FileInvalidError(filename, "password-protected or encrypted")

    if page_count > settings.PDF_MAX_PAGES:
        raise FileInvalidError(
            filename,
            f"more than {settings.PDF_MAX_PAGES} pages ({page_count} pages found)",
        )

    return page_count


async def validate_upload_file(file: UploadFile) -> tuple[bytes, int]:
    """Validates an uploaded FastAPI file and returns (content, page_count)."""
    filename = file.filename or "upload.pdf"
    content = await file.read()
    page_count = validate_pdf_bytes(content, filename)
    return content, page_count
