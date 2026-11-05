import pytest

from app.memory.schemas import MemoryItemCreate
from app.memory.service import MemoryService


@pytest.mark.asyncio
async def test_memory_service_record_and_get(test_db):
    service = MemoryService(test_db)
    user_id = "user-123"

    item = MemoryItemCreate(
        category="career",
        key="target_role",
        value="Senior DevOps Engineer",
        is_confirmed=True,
        confidence=1.0,
        source="user_chat",
    )
    saved = await service.record_fact(user_id, item)
    assert saved.key == "target_role"
    assert saved.value == "Senior DevOps Engineer"
    assert saved.is_confirmed is True

    summary = await service.get_active_memory(user_id)
    assert len(summary.items) == 1
    assert summary.items[0].value == "Senior DevOps Engineer"
    prompt_str = summary.format_for_prompt()
    assert "<ACTIVE_USER_MEMORY>" in prompt_str
    assert "target_role: Senior DevOps Engineer" in prompt_str
    assert "user-confirmed" in prompt_str


@pytest.mark.asyncio
async def test_memory_service_precedence_rule_7(test_db):
    """Rule 7: Inferred fact cannot overwrite a user-confirmed fact."""
    service = MemoryService(test_db)
    user_id = "user-456"

    # 1. User explicitly states their role
    await service.record_fact(
        user_id,
        MemoryItemCreate(
            category="career",
            key="target_role",
            value="Kubernetes Architect",
            is_confirmed=True,
            confidence=1.0,
        ),
    )

    # 2. Agent makes an inference about the same key
    rejected = await service.record_fact(
        user_id,
        MemoryItemCreate(
            category="career",
            key="target_role",
            value="Junior DevOps",
            is_confirmed=False,
            confidence=0.6,
            source="rag_reasoning",
        ),
    )
    # Value must remain the confirmed one!
    assert rejected.value == "Kubernetes Architect"
    assert rejected.is_confirmed is True

    summary = await service.get_active_memory(user_id)
    assert summary.items[0].value == "Kubernetes Architect"

    # 3. User explicitly updates to another confirmed role
    updated = await service.record_fact(
        user_id,
        MemoryItemCreate(
            category="career",
            key="target_role",
            value="Platform Engineering Lead",
            is_confirmed=True,
            confidence=1.0,
        ),
    )
    assert updated.value == "Platform Engineering Lead"


@pytest.mark.asyncio
async def test_memory_service_multi_tenant_isolation(test_db):
    """User A's memory must never leak to User B."""
    service = MemoryService(test_db)
    user_a = "user-alice"
    user_b = "user-bob"

    await service.record_fact(
        user_a,
        MemoryItemCreate(
            category="skills",
            key="known_skills",
            value=["Python", "FastAPI"],
            is_confirmed=True,
        ),
    )

    summary_b = await service.get_active_memory(user_b)
    assert len(summary_b.items) == 0


@pytest.mark.asyncio
async def test_memory_service_delete_fact(test_db):
    service = MemoryService(test_db)
    user_id = "user-del"

    await service.record_fact(
        user_id,
        MemoryItemCreate(
            category="preferences",
            key="salary",
            value="$150,000",
            is_confirmed=True,
        ),
    )

    deleted = await service.delete_fact(user_id, "preferences", "salary")
    assert deleted is True

    summary = await service.get_active_memory(user_id)
    assert len(summary.items) == 0


@pytest.mark.asyncio
async def test_memory_service_ttl_expiration(test_db):
    """Expired facts should not be returned in active memory."""
    service = MemoryService(test_db)
    user_id = "user-ttl"

    # Negative TTL = immediately expired in past
    await service.record_fact(
        user_id,
        MemoryItemCreate(
            category="temporary",
            key="temp_note",
            value="call tomorrow",
            ttl_seconds=-10,
        ),
    )

    summary = await service.get_active_memory(user_id)
    assert len(summary.items) == 0

    purged = await service.purge_expired(user_id)
    assert purged == 1
