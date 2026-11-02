import asyncio
import hashlib
import re
from typing import Any

from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.documents import DocumentRepository
from app.db.session import get_sessionmaker
from app.documents.extract import extract_pdf_text
from app.privacy.gate import clean

CV_GATE_VERSION = "v1"


class CvText(BaseModel):
    text: str
    removed: dict[str, int] = Field(default_factory=dict)


def gate_cv_text(raw_text: str, user: Any = None) -> CvText:
    """Applies the CV privacy gate once to raw extracted CV text."""
    if not raw_text or not raw_text.strip():
        return CvText(text="", removed={})

    known_email = ""
    if user and hasattr(user, "email") and user.email:
        known_email = str(user.email).strip()

    # Pre-pass: replace leading CV / Resume title line in top lines so drop_contact_header doesn't mistake it for candidate name
    lines = raw_text.splitlines()
    pre_lines = []
    for i, line in enumerate(lines):
        if i < 5 and re.match(
            r"^\s*(?:#{1,6}\s*)?(?:curriculum\s+vitae|resume|cv)\s*$", line, re.IGNORECASE
        ):
            pre_lines.append("")
        else:
            pre_lines.append(line)
    text_for_cleaning = "\n".join(pre_lines)

    # Extract name candidate from the first 15 lines, skipping section titles
    known_name = ""
    for line in text_for_cleaning.splitlines()[:15]:
        stripped = line.strip()
        cleaned_line = re.sub(r"^[\s#*_\->|:]+", "", stripped)
        cleaned_line = re.sub(r"[\s*_\->|:]+$", "", cleaned_line).strip()
        if not cleaned_line:
            continue
        if any(
            h in cleaned_line.lower()
            for h in [
                "thông tin",
                "liên hệ",
                "curriculum vitae",
                "resume",
                "cv",
                "kỹ năng",
                "kinh nghiệm",
                "contact",
            ]
        ):
            continue
        words = cleaned_line.split()
        if (
            2 <= len(words) <= 6
            and "@" not in cleaned_line
            and "http" not in cleaned_line.lower()
            and not re.search(r"\d{3,}", cleaned_line)
        ):
            known_name = cleaned_line
            break

    # Strip inline address mentions
    addr_pat = re.compile(
        r"(?:tại\s+)?(?:địa chỉ|address)\s*[:\s]\s*[^,\n|)]+?(?=(?:\s+hoặc|\s+or|\s+qua|\s+với|[,|\n)]|$))",
        re.IGNORECASE,
    )
    pre_cleaned, addr_count = addr_pat.subn("[ADDRESS]", text_for_cleaning)

    # Privacy clean: single pass with known_email and known_name
    cleaned, counts = clean(
        pre_cleaned,
        source="cv",
        is_file=True,
        known_email=known_email,
        known_name=known_name,
    )
    if addr_count:
        counts["address"] = counts.get("address", 0) + addr_count

    return CvText(text=cleaned, removed=counts)


_mem_cv_cache: dict[str, CvText] = {}


def _cache_key(sha256_hash: str) -> str:
    return hashlib.sha256((sha256_hash + CV_GATE_VERSION).encode("utf-8")).hexdigest()


async def cache_cv_text(sha256: str, cv_text: CvText, session: AsyncSession | None = None) -> None:
    key = _cache_key(sha256)
    _mem_cv_cache[key] = cv_text
    try:
        if session is not None:
            repo = DocumentRepository(session)
            await repo.save_document(
                sha256_hash=key,
                extractor="cv_gate",
                page_count=1,
                cleaned_text=cv_text.text,
                removed_counts=cv_text.removed,
                ttl_days=30,
            )
        else:
            sessionmaker = get_sessionmaker()
            async with sessionmaker() as sess:
                repo = DocumentRepository(sess)
                await repo.save_document(
                    sha256_hash=key,
                    extractor="cv_gate",
                    page_count=1,
                    cleaned_text=cv_text.text,
                    removed_counts=cv_text.removed,
                    ttl_days=30,
                )
    except Exception:
        pass


async def get_cv_text(sha256: str, session: AsyncSession | None = None) -> CvText | None:
    key = _cache_key(sha256)
    if key in _mem_cv_cache:
        return _mem_cv_cache[key]

    try:
        if session is not None:
            repo = DocumentRepository(session)
            doc = await repo.get_by_sha256(key)
        else:
            sessionmaker = get_sessionmaker()
            async with sessionmaker() as sess:
                repo = DocumentRepository(sess)
                doc = await repo.get_by_sha256(key)

        if doc is not None:
            res = CvText(text=doc.cleaned_text, removed=doc.removed_counts or {})
            _mem_cv_cache[key] = res
            return res
    except Exception:
        pass
    return None


async def prepare_cv_text(
    pdf_bytes: bytes, user: Any, session: AsyncSession | None = None
) -> CvText:
    pdf_sha256 = hashlib.sha256(pdf_bytes).hexdigest()
    cached = await get_cv_text(pdf_sha256, session=session)
    if cached is not None:
        return cached

    raw_text, _, _ = await asyncio.to_thread(extract_pdf_text, pdf_bytes)
    cv_text = gate_cv_text(raw_text, user)
    await cache_cv_text(pdf_sha256, cv_text, session=session)
    return cv_text
