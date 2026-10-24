import asyncio

import pytest
from pydantic_ai import Agent
from pydantic_ai.models.function import FunctionModel

from app.db.models import ChatSession
from app.features.chat import service as chat_service_mod


@pytest.mark.asyncio
async def test_409_keeps_running_turn_locked(client, test_db, monkeypatch):
    # 1. Create a session
    sess = ChatSession(
        user_id="test-user-uuid-123",
        title="Lock Test",
    )
    test_db.add(sess)
    await test_db.commit()
    await test_db.refresh(sess)

    # Mock agent with a slow function
    turn_a_started = asyncio.Event()
    release_turn_a = asyncio.Event()

    from pydantic_ai.messages import ModelResponse, TextPart

    async def slow_fn(messages, info):
        turn_a_started.set()
        await release_turn_a.wait()
        return ModelResponse(parts=[TextPart("Done turn A")])

    test_agent = Agent(model=FunctionModel(function=slow_fn))
    monkeypatch.setattr(chat_service_mod, "chat_agent", test_agent)

    # Start turn A in background task
    async def run_turn_a():
        return await client.post(
            "/ai/chat/messages",
            data={"message": "Turn A", "sessionId": sess.id},
        )

    task_a = asyncio.create_task(run_turn_a())
    await turn_a_started.wait()

    # Now turn A is running and has the lock
    # Send message B -> must be refused with 409
    res_b = await client.post(
        "/ai/chat/messages",
        data={"message": "Turn B", "sessionId": sess.id},
    )
    assert res_b.status_code == 409
    body_b = res_b.json()
    code_b = body_b.get("errorCode") or (
        body_b.get("error", {}).get("errorCode") if isinstance(body_b.get("error"), dict) else None
    )
    assert code_b in ("CHAT_BUSY", "CHAT_SESSION_BUSY")

    # Send message C -> must also be refused with 409 (message B's refusal didn't release the lock)
    res_c = await client.post(
        "/ai/chat/messages",
        data={"message": "Turn C", "sessionId": sess.id},
    )
    assert res_c.status_code == 409
    body_c = res_c.json()
    code_c = body_c.get("errorCode") or (
        body_c.get("error", {}).get("errorCode") if isinstance(body_c.get("error"), dict) else None
    )
    assert code_c in ("CHAT_BUSY", "CHAT_SESSION_BUSY")

    # Release turn A
    release_turn_a.set()
    res_a = await task_a
    assert res_a.status_code == 200

    # After turn A finished, the lock is released and message D is accepted
    res_d = await client.post(
        "/ai/chat/messages",
        data={"message": "Turn D", "sessionId": sess.id},
    )
    assert res_d.status_code == 200


@pytest.mark.asyncio
async def test_404_other_user_keeps_lock(client, test_db):
    from datetime import UTC, datetime

    # Create session owned by other user and currently locked
    now = datetime.now(UTC)
    other_sess = ChatSession(
        user_id="other-user-999",
        title="Other Locked Session",
        busy_since=now,
    )
    test_db.add(other_sess)
    await test_db.commit()
    await test_db.refresh(other_sess)

    # Current user tries to access other user's session -> 404
    res = await client.post(
        "/ai/chat/messages",
        data={"message": "Steal", "sessionId": other_sess.id},
    )
    assert res.status_code == 404

    # The other user's busy_since must remain set
    await test_db.refresh(other_sess)
    assert other_sess.busy_since is not None
