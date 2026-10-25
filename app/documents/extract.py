import hashlib
import logging
import os
import time
from io import BytesIO

import pypdfium2 as pdfium

from app.core.config import get_settings
from app.core.logging import log_step


class PdfiumExtractor:
    @staticmethod
    def extract(content: bytes) -> tuple[str, int]:
        """Extracts text from PDF using pypdfium2. Returns (text, page_count)."""
        doc = pdfium.PdfDocument(BytesIO(content))
        page_count = len(doc)
        pages_text: list[str] = []

        for i in range(page_count):
            page = doc[i]
            text_page = page.get_textpage()
            text = text_page.get_text_range()
            if text and text.strip():
                pages_text.append(text.strip())

        return "\n\n".join(pages_text), page_count


class DoclingExtractor:
    _converter = None

    @classmethod
    def get_converter(cls):
        if cls._converter is None:
            try:
                from docling.datamodel.base_models import InputFormat
                from docling.datamodel.pipeline_options import (
                    PdfPipelineOptions,
                    TesseractCliOcrOptions,
                )
                from docling.document_converter import DocumentConverter, PdfFormatOption

                settings = get_settings()
                artifacts_path = os.getenv("DOCLING_ARTIFACTS_PATH")
                pipeline_options = PdfPipelineOptions()
                if artifacts_path and os.path.exists(artifacts_path):
                    pipeline_options.artifacts_path = artifacts_path
                pipeline_options.do_ocr = True

                ocr_langs = [
                    lang.strip() for lang in settings.OCR_LANGS.split(",") if lang.strip()
                ] or ["vie", "eng"]
                pipeline_options.ocr_options = TesseractCliOcrOptions(lang=ocr_langs)

                cls._converter = DocumentConverter(
                    format_options={
                        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                    }
                )
            except Exception as e:
                log_step(
                    "docling.init_failed", level=logging.WARNING, error=str(e), fallback="pdfium"
                )
                cls._converter = False
        return cls._converter

    @classmethod
    def extract(cls, content: bytes) -> tuple[str, int]:
        converter = cls.get_converter()
        if not converter:
            log_step(
                "docling.fallback",
                level=logging.WARNING,
                reason="converter_not_available",
                fallback="pdfium",
            )
            return PdfiumExtractor.extract(content)

        from docling.datamodel.document import DocumentStream

        stream = DocumentStream(name="document.pdf", stream=BytesIO(content))
        conv_res = converter.convert(stream)
        text = conv_res.document.export_to_markdown()
        pages = len(conv_res.document.pages) if hasattr(conv_res.document, "pages") else 1
        return text, pages


def extract_pdf_text(content: bytes) -> tuple[str, int, str]:
    """
    Extracts text from PDF according to configured PDF_EXTRACTOR.
    Returns (raw_text, page_count, extractor_used).
    """
    settings = get_settings()
    start_time = time.perf_counter()
    extractor_used = settings.PDF_EXTRACTOR.lower()
    sha_prefix = hashlib.sha256(content).hexdigest()[:8]

    if extractor_used == "docling":
        try:
            text, pages = DoclingExtractor.extract(content)
        except Exception as e:
            log_step("docling.fallback", level=logging.WARNING, reason=str(e), fallback="pdfium")
            extractor_used = "pdfium"
            text, pages = PdfiumExtractor.extract(content)
    else:
        extractor_used = "pdfium"
        text, pages = PdfiumExtractor.extract(content)

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
