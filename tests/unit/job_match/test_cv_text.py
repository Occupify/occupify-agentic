import hashlib

import pytest

from app.core.security import CurrentUser
from app.documents.cv_text import (
    CV_GATE_VERSION,
    CvText,
    _cache_key,
    cache_cv_text,
    gate_cv_text,
    get_cv_text,
)


def test_one_gate_applied_once(monkeypatch):
    call_count = 0

    import app.documents.cv_text as cv_text_mod

    orig_clean = cv_text_mod.clean

    def spy_clean(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        return orig_clean(*args, **kwargs)

    monkeypatch.setattr(cv_text_mod, "clean", spy_clean)

    raw_cv = """
    Nguyễn Văn Candidate
    Kỹ sư phần mềm

    Kinh nghiệm làm việc:
    - 3 năm lập trình Python, FastAPI và PostgreSQL.

    Kỹ năng:
    - Python, Docker, Kubernetes
    """
    user = CurrentUser(user_id="u123", email="candidate@example.com")
    res = gate_cv_text(raw_cv, user)

    assert isinstance(res, CvText)
    assert call_count == 1
    assert "Python" in res.text


def test_cache_key_includes_gate_version():
    dummy_sha = hashlib.sha256(b"dummy_pdf_bytes").hexdigest()
    expected_key = hashlib.sha256((dummy_sha + CV_GATE_VERSION).encode("utf-8")).hexdigest()

    actual_key = _cache_key(dummy_sha)
    assert actual_key == expected_key
    assert CV_GATE_VERSION in (dummy_sha + CV_GATE_VERSION)


def test_known_email_and_name_removed():
    raw_cv = """
    Trần Thị Developer
    Email: dev.tran@example.com
    Số điện thoại: 0912 345 678
    Địa chỉ: 45 Đường Thử Nghiệm, Hà Nội

    Kinh nghiệm:
    - Backend Developer tại Tech Corp từ 2021 đến 2024.
    - Lập trình Java Spring Boot, MySQL.

    Kỹ năng:
    - Java, Spring Boot, Microservices
    """
    user = CurrentUser(user_id="u456", email="dev.tran@example.com")
    cv_res = gate_cv_text(raw_cv, user)

    assert "dev.tran@example.com" not in cv_res.text
    assert "Trần Thị Developer" not in cv_res.text
    assert "0912 345 678" not in cv_res.text
    assert "Java" in cv_res.text


def test_title_line_not_redacted():
    raw_cv = """
    CURRICULUM VITAE
    Lê Văn Kỹ Sư
    Email: le.eng@example.com

    Kinh nghiệm:
    - Soạn thảo CURRICULUM VITAE mẫu và phát triển hệ thống với Go và Kafka.

    Kỹ năng:
    - Golang, Kafka, Redis
    """
    user = CurrentUser(user_id="u789", email="le.eng@example.com")
    cv_res = gate_cv_text(raw_cv, user)

    # CURRICULUM VITAE should not be extracted as the person's name, so body mention remains unredacted as [NAME]
    assert "CURRICULUM VITAE" in cv_res.text
    # And candidate's actual name was removed
    assert "Lê Văn Kỹ Sư" not in cv_res.text


@pytest.mark.asyncio
async def test_cache_and_get_cv_text(test_db):
    pdf_sha = hashlib.sha256(b"sample_cv_pdf").hexdigest()
    cv_obj = CvText(text="Cleaned CV content for cache testing", removed={"email": 1})

    await cache_cv_text(pdf_sha, cv_obj, session=test_db)
    retrieved = await get_cv_text(pdf_sha, session=test_db)

    assert retrieved is not None
    assert retrieved.text == cv_obj.text
    assert retrieved.removed.get("email") == 1
