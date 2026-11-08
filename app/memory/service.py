from datetime import UTC, datetime, timedelta

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logging import log_step
from app.db.models import UserMemory, utc_now
from app.memory.schemas import MemoryItemCreate, MemoryItemRead, UserMemorySummary


class MemoryService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def record_fact(self, user_id: str, item: MemoryItemCreate) -> MemoryItemRead:
        """
        Records or updates a user memory fact.
        Adheres to Rule 7 Precedence:
        - An unconfirmed inference (is_confirmed=False) NEVER silently overwrites a user-confirmed fact (is_confirmed=True).
        - A user-confirmed fact strictly updates and promotes any existing fact.
        """
        now = utc_now()
        expires_at = now + timedelta(seconds=item.ttl_seconds) if item.ttl_seconds else None

        stmt = select(UserMemory).where(
            UserMemory.user_id == user_id,
            UserMemory.category == item.category,
            UserMemory.key == item.key,
        )
        res = await self.db.execute(stmt)
        existing = res.scalar_one_or_none()

        if existing:
            # Rule 7 Precedence: Unconfirmed inference cannot override confirmed fact
            if existing.is_confirmed and not item.is_confirmed:
                log_step(
                    "memory.precedence_rejected",
                    user_id=user_id,
                    category=item.category,
                    key=item.key,
                    reason="Inferred fact cannot overwrite user-confirmed fact",
                )
                return MemoryItemRead(
                    id=existing.id,
                    user_id=existing.user_id,
                    category=existing.category,
                    key=existing.key,
                    value=existing.value,
                    is_confirmed=existing.is_confirmed,
                    confidence=existing.confidence,
                    source=existing.source,
                    created_at=existing.created_at,
                    updated_at=existing.updated_at,
                    expires_at=existing.expires_at,
                )

            old_val = existing.value
            existing.value = item.value
            existing.is_confirmed = item.is_confirmed or existing.is_confirmed
            existing.confidence = item.confidence
            existing.source = item.source
            existing.updated_at = now
            if expires_at:
                existing.expires_at = expires_at

            await self.db.commit()
            await self.db.refresh(existing)

            log_step(
                "memory.updated",
                user_id=user_id,
                category=item.category,
                key=item.key,
                old_value=old_val,
                new_value=item.value,
                is_confirmed=existing.is_confirmed,
                confidence=item.confidence,
            )
            target = existing
        else:
            new_row = UserMemory(
                user_id=user_id,
                category=item.category,
                key=item.key,
                value=item.value,
                is_confirmed=item.is_confirmed,
                confidence=item.confidence,
                source=item.source,
                created_at=now,
                updated_at=now,
                expires_at=expires_at,
            )
            self.db.add(new_row)
            await self.db.commit()
            await self.db.refresh(new_row)

            log_step(
                "memory.recorded",
                user_id=user_id,
                category=item.category,
                key=item.key,
                value=item.value,
                is_confirmed=item.is_confirmed,
                confidence=item.confidence,
                source=item.source,
            )
            target = new_row

        return MemoryItemRead(
            id=target.id,
            user_id=target.user_id,
            category=target.category,
            key=target.key,
            value=target.value,
            is_confirmed=target.is_confirmed,
            confidence=target.confidence,
            source=target.source,
            created_at=target.created_at,
            updated_at=target.updated_at,
            expires_at=target.expires_at,
        )

    async def get_active_memory(
        self, user_id: str, category: str | None = None, emit_log: bool = False
    ) -> UserMemorySummary:
        """
        Retrieves active unexpired memory facts for the user.
        Strictly multi-tenant: only rows matching user_id are returned.
        """
        now = datetime.now(UTC)
        query = select(UserMemory).where(UserMemory.user_id == user_id)

        if category:
            query = query.where(UserMemory.category == category)

        # Exclude expired
        query = query.where(
            (UserMemory.expires_at.is_(None)) | (UserMemory.expires_at > now)
        ).order_by(UserMemory.category, UserMemory.key)

        res = await self.db.execute(query)
        rows = res.scalars().all()

        items = [
            MemoryItemRead(
                id=r.id,
                user_id=r.user_id,
                category=r.category,
                key=r.key,
                value=r.value,
                is_confirmed=r.is_confirmed,
                confidence=r.confidence,
                source=r.source,
                created_at=r.created_at,
                updated_at=r.updated_at,
                expires_at=r.expires_at,
            )
            for r in rows
        ]

        if items and emit_log:
            log_step(
                "memory.injected",
                user_id=user_id,
                fact_count=len(items),
                categories=list({it.category for it in items}),
            )

        return UserMemorySummary(items=items)

    async def delete_fact(self, user_id: str, category: str, key: str) -> bool:
        """Deletes a specific user fact (Data Minimization / GDPR)."""
        stmt = delete(UserMemory).where(
            UserMemory.user_id == user_id,
            UserMemory.category == category,
            UserMemory.key == key,
        )
        res = await self.db.execute(stmt)
        await self.db.commit()
        deleted = res.rowcount > 0
        if deleted:
            log_step("memory.deleted", user_id=user_id, category=category, key=key)
        return deleted

    async def purge_expired(self, user_id: str | None = None) -> int:
        """Purges expired rows past their retention TTL."""
        now = datetime.now(UTC)
        stmt = (
            delete(UserMemory)
            .where(UserMemory.expires_at.is_not(None))
            .where(UserMemory.expires_at <= now)
        )
        if user_id:
            stmt = stmt.where(UserMemory.user_id == user_id)
        res = await self.db.execute(stmt)
        await self.db.commit()
        purged = res.rowcount
        if purged > 0:
            log_step("memory.purged_expired", count=purged, user_id=user_id)
        return purged
