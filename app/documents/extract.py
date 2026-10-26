import hashlib
import json
import logging
import sys
import time
from io import BytesIO
from pathlib import Path
from typing import Any

import pypdfium2 as pdfium
from doctr.io import DocumentFile
from doctr.models import ocr_predictor
from fastapi import UploadFile

from app.core.config import get_settings
from app.core.errors import FileInvalidError
from app.core.logging import log_step
from app.documents.cv_parser import parse_cv

_ocr_model = None


def get_ocr_model():
    """Lazy loader for docTR OCR model to avoid slow startup."""
    global _ocr_model
    if _ocr_model is None:
        _ocr_model = ocr_predictor(det_arch="db_resnet50", reco_arch="crnn_vgg16_bn", pretrained=True)
    return _ocr_model


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

    try:
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


def extract_cv(
    file_input: bytes | str | Path, hide_personal_info: bool = True
) -> tuple[dict[str, Any], list[str], int]:
    """
    Extracts structured CV data using docTR OCR predictor and cv_parser.
    Returns (cv_dict, all_lines, page_count).
    """
    model = get_ocr_model()
    doc = DocumentFile.from_pdf(file_input)
    page_count = len(doc)
    result = model(doc)

    all_lines: list[str] = []
    for page in result.pages:
        for block in page.blocks:
            for line in block.lines:
                text = " ".join(word.value for word in line.words).strip()
                if text:
                    all_lines.append(text)

    cv_data = parse_cv(all_lines, hide_personal_info=hide_personal_info)
    return cv_data, all_lines, page_count


def _extract_pdfium_text(content: bytes) -> tuple[str, int]:
    """Fallback text extractor using pypdfium2."""
    doc = pdfium.PdfDocument(BytesIO(content))
    page_count = len(doc)
    pages_text: list[str] = []
    for page in doc:
        text_page = page.get_textpage()
        text = text_page.get_text_range()
        if text and text.strip():
            pages_text.append(text.strip())
    return "\n\n".join(pages_text), page_count


def extract_pdf_text(content: bytes) -> tuple[str, int, str]:
    """
    Extracts text from PDF according to configured PDF_EXTRACTOR.
    Returns (raw_text, page_count, extractor_used).
    """
    settings = get_settings()
    start_time = time.perf_counter()
    extractor_used = settings.PDF_EXTRACTOR.lower()
    sha_prefix = hashlib.sha256(content).hexdigest()[:8]

    if extractor_used == "doctr":
        try:
            _, lines, pages = extract_cv(content)
            text = "\n".join(lines)
        except Exception as e:
            log_step("doctr.fallback", level=logging.WARNING, reason=str(e), fallback="pdfium")
            extractor_used = "pdfium"
            text, pages = _extract_pdfium_text(content)
    else:
        extractor_used = "pdfium"
        text, pages = _extract_pdfium_text(content)

    duration_ms = int((time.perf_counter() - start_time) * 1000)
    log_step(
        "doc.extracted",
        pages=pages,
        extractor=extractor_used,
        ms=duration_ms,
        sha256_prefix=sha_prefix,
        bytes=len(content),
    )

    return text, pages, extractor_used


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = Path(sys.argv[1])
        cv, lines, pages = extract_cv(str(target) if target.exists() else target)
        print(f"Extracted {pages} page(s), {len(lines)} lines")
        out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else target.parent / f"{target.stem}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(cv, f, indent=2, ensure_ascii=False)
        print(f"Saved result to {out_path}")
        print(json.dumps(cv, indent=2, ensure_ascii=False))
    else:
        print("Usage: python -m app.documents.extract <path_to_pdf> [output_path.json]")
