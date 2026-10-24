import asyncio

import pytest
from pydantic_ai import Agent
from pydantic_ai.models.function import FunctionModel
from sqlalchemy import select

from app.db.models import AgentRun, ChatMessage, ChatSession
from app.features.chat import service as chat_service_mod
from app.main import app


@pytest.mark.asyncio
async def test_disconnect_saves_interrupted_and_frees_session(test_db, monkeypatch):
    sess = ChatSession(
        user_id="test-user-uuid-123",
        title="Disconnect Session",
    )
    test_db.add(sess)
    await test_db.commit()
    sess_id = sess.id

    first_chunk_sent = asyncio.Event()

    async def stream_fn(messages, info):
        yield "Chunk 1 "
        first_chunk_sent.set()
        await asyncio.sleep(5)
        yield "Chunk 2"

    test_agent = Agent(model=FunctionModel(stream_function=stream_fn))
    monkeypatch.setattr(chat_service_mod, "chat_agent", test_agent)

    # Prepare multipart body
    boundary = "----WebKitFormBoundaryDisconnectTest"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="message"\r\n\r\n'
        f"Hello disconnect\r\n"
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="sessionId"\r\n\r\n'
        f"{sess_id}\r\n"
        f"--{boundary}--\r\n"
    ).encode()

    body_sent = False
    disconnected = False

    async def receive():
        nonlocal body_sent, disconnected
        if not body_sent:
            body_sent = True
            return {
                "type": "http.request",
                "body": body,
                "more_body": False,
            }
        await first_chunk_sent.wait()
        disconnected = True
        return {"type": "http.disconnect"}

    sent_messages = []

    async def send(message):
        sent_messages.append(message)

    scope = {
        "type": "http",
        "asgi": {"version": "3.0"},
        "http_version": "1.1",
        "method": "POST",
        "path": "/ai/chat/messages",
        "raw_path": b"/ai/chat/messages",
        "query_string": b"stream=true",
        "headers": [
            (b"content-type", f"multipart/form-data; boundary={boundary}".encode()),
            (b"x-user-id", b"test-user-uuid-123"),
            (b"x-user-role", b"ROLE_USER"),
        ],
    }

    app_task = asyncio.create_task(app(scope, receive, send))
    try:
        await app_task
    except (asyncio.CancelledError, Exception):
        pass

    # Wait up to 5s for cleanup to finish
    for _ in range(50):
        await asyncio.sleep(0.1)
        await test_db.rollback()
        s = await test_db.get(ChatSession, sess_id)
        if s and s.busy_since is None:
            break

    # 1. Assert session busy_since is NULL
    await test_db.rollback()
    refreshed_sess = await test_db.get(ChatSession, sess_id)
    assert refreshed_sess.busy_since is None

    # 2. Assert interrupted assistant row exists
    msgs = (
        (
            await test_db.execute(
                select(ChatMessage)
                .where(ChatMessage.session_id == sess_id)
                .order_by(ChatMessage.seq)
            )
        )
        .scalars()
        .all()
    )
    assert len(msgs) >= 2  # user + assistant
    asst_msg = msgs[-1]
    assert asst_msg.role == "assistant"
    assert asst_msg.status == "interrupted"
    assert "Chunk 1" in asst_msg.content

    # 3. Assert run is marked failed with error containing interrupted
    runs = (
        (
            await test_db.execute(
                select(AgentRun)
                .where(AgentRun.session_id == sess_id)
                .order_by(AgentRun.created_at.desc())
            )
        )
        .scalars()
        .all()
    )
    assert len(runs) >= 1
    assert runs[0].status == "failed"
    assert "interrupted" in (runs[0].error_message or "").lower()
