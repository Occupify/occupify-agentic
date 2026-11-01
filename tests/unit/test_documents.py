from io import BytesIO
from pathlib import Path

import pytest
from reportlab.pdfgen import canvas

from app.core.errors import FileInvalidError
from app.documents.extract import extract_cv, extract_pdf_text, validate_pdf_bytes


def generate_sample_pdf(pages: int = 1, text: str = "Hello World") -> bytes:
    buf = BytesIO()
    c = canvas.Canvas(buf)
    for i in range(pages):
        y = 750
        for line in text.split("\n"):
            c.drawString(100, y, line)
            y -= 20
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
    text, pages, extractor = extract_pdf_text(content)
    assert pages == 2
    assert "Senior Python Developer" in text
    assert extractor in ["doctr", "pdfium"]


@pytest.mark.doctr
def test_doctr_pdf_extraction(monkeypatch):
    import app.documents.extract as extract_mod

    monkeypatch.setattr(extract_mod.get_settings(), "PDF_EXTRACTOR", "doctr")
    content = generate_sample_pdf(
        pages=1, text="Nguyen Van A\n## Experience\nSenior Backend Engineer"
    )
    text, pages, extractor = extract_mod.extract_pdf_text(content)
    assert extractor == "doctr"
    assert "Senior Backend Engineer" in text


@pytest.mark.doctr
def test_user_cv_extraction():
    fixture_path = Path(__file__).parent.parent / "fixtures" / "VoMinhTien_UIT_CV.pdf"
    if not fixture_path.exists():
        pytest.skip("User CV fixture not found")

    cv_data, lines, page_count = extract_cv(str(fixture_path))
    assert page_count == 1
    assert len(lines) > 20

    # Removed fields
    for field in ["personal_info", "summary", "education", "languages", "references"]:
        assert field not in cv_data

    # Kept skills
    assert len(cv_data["skills"]) >= 20
    assert "skills_by_category" in cv_data

    # Kept experience highlights only
    assert len(cv_data["experience"]) >= 1
    for exp in cv_data["experience"]:
        assert "highlights" in exp
        assert "company" not in exp
        assert "role" not in exp
        assert "period" not in exp
        assert "link" not in exp
        assert len(exp["highlights"]) >= 1

    # Kept project highlights only
    assert len(cv_data["projects"]) >= 1
    for proj in cv_data["projects"]:
        assert "highlights" in proj
        assert "name" not in proj
        assert "role" not in proj
        assert "period" not in proj
        assert "link" not in proj
        assert len(proj["highlights"]) >= 1

    # Kept key technical highlights
    assert len(cv_data["key_technical_highlights"]) >= 1


@pytest.mark.asyncio
async def test_cv_preview_endpoint(client):
    content = generate_sample_pdf(
        pages=1, text="Nguyen Van A\n## Skills\na@test.com\nPython, Docker"
    )
    files = {"file": ("my_cv.pdf", content, "application/pdf")}
    res = await client.post("/ai/dev/cv-preview", files=files)
    assert res.status_code == 200
    data = res.json()["data"]
    assert data["filename"] == "my_cv.pdf"
    assert data["pageCount"] == 1
    assert "a@test.com" not in data["cleanedText"]
    assert "Python, Docker" in data["cleanedText"]
