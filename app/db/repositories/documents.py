import uuid
from datetime import UTC, datetime, timedelta
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Document


class DocumentRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_sha256(self, sha256_hash: str) -> Document | None:
        now = datetime.now(UTC)
        stmt = (
            select(Document).where(Document.sha256 == sha256_hash).where(Document.expires_at > now)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def save_document(
        self,
        sha256_hash: str,
        extractor: str,
        page_count: int,
        cleaned_text: str,
        removed_counts: dict[str, Any],
        ttl_days: int = 30,
    ) -> Document:
        now = datetime.now(UTC)
        expires_at = now + timedelta(days=ttl_days)

        # Check if record exists (even if expired) to perform UPSERT and avoid UniqueConstraint violation
        stmt = select(Document).where(Document.sha256 == sha256_hash)
        res = await self.session.execute(stmt)
        existing = res.scalar_one_or_none()

        if existing:
            existing.extractor = extractor
            existing.page_count = page_count
            existing.cleaned_text = cleaned_text
            existing.removed_counts = removed_counts
            existing.expires_at = expires_at
            doc = existing
        else:
            doc = Document(
                id=str(uuid.uuid4()),
                sha256=sha256_hash,
                extractor=extractor,
                page_count=page_count,
                cleaned_text=cleaned_text,
                removed_counts=removed_counts,
                created_at=now,
                expires_at=expires_at,
            )
            self.session.add(doc)

        await self.session.commit()
        await self.session.refresh(doc)
        return doc
