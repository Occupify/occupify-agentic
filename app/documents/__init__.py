from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.documents.cv_parser import parse_cv
    from app.documents.extract import (
        extract_cv,
        extract_pdf_text,
        validate_pdf_bytes,
        validate_upload_file,
    )

__all__ = [
    "extract_cv",
    "extract_pdf_text",
    "parse_cv",
    "validate_pdf_bytes",
    "validate_upload_file",
]


def __getattr__(name: str):
    if name == "parse_cv":
        from app.documents.cv_parser import parse_cv

        return parse_cv
    if name in {"extract_cv", "extract_pdf_text", "validate_pdf_bytes", "validate_upload_file"}:
        import app.documents.extract as _ext

        return getattr(_ext, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
