from io import BytesIO

import pytest
from reportlab.pdfgen import canvas

from app.core.errors import FileInvalidError
from app.documents.extract import extract_pdf_text
from app.documents.fetch import validate_pdf_bytes


def generate_sample_pdf(pages: int = 1, text: str = "Hello World") -> bytes:
    buf = BytesIO()
    c = canvas.Canvas(buf)
    for i in range(pages):
        c.drawString(100, 750, f"{text} - Page {i + 1}")
        c.showPage()
    c.save()
    return buf.getvalue()


def test_pdf_validation_valid():
    content = generate_sample_pdf(pages=2, text="John Doe Software Engineer")
    page_count = validate_pdf_bytes(content, "test.pdf")
    assert page_count == 2


def test_pdf_validation_empty():
    with pytest.raises(FileInvalidError):
        validate_pdf_bytes(b"", "empty.pdf")


def test_pdf_validation_not_pdf():
    with pytest.raises(FileInvalidError):
        validate_pdf_bytes(b"This is just a plain text file", "not_pdf.txt")


def test_pdf_validation_too_many_pages():
    content = generate_sample_pdf(pages=25, text="Lots of pages")
    with pytest.raises(FileInvalidError) as exc_info:
        validate_pdf_bytes(content, "large.pdf")
    assert "more than 20 pages" in str(exc_info.value.message)


def test_pdf_extraction():
    content = generate_sample_pdf(pages=2, text="Senior Python Developer with PostgreSQL")
    text, pages, extractor, ocr_pages = extract_pdf_text(content, "cv.pdf")
    assert pages == 2
    assert "Senior Python Developer" in text
    assert extractor in ["docling", "pdfium"]


@pytest.mark.asyncio
async def test_cv_preview_endpoint(client):
    content = generate_sample_pdf(pages=1, text="Nguyen Van A - Email: a@test.com - Python, Docker")
    files = {"file": ("my_cv.pdf", content, "application/pdf")}
    res = await client.post("/ai/dev/cv-preview", files=files)
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["filename"] == "my_cv.pdf"
    assert data["pageCount"] == 1
    assert "a@test.com" not in data["cleanedText"]
    assert "Python, Docker" in data["cleanedText"]
