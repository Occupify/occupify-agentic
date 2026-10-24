import asyncio
import json

import pytest
from httpx import ASGITransport, AsyncClient

from app.core.config import get_settings
from app.core.logging import log_step
from app.main import app


@pytest.mark.asyncio
async def test_logs_endpoint_recent_entries(client):
    log_step("test.dev.entry.1", sample_val=100)
    log_step("test.dev.entry.2", sample_val=200)

    res = await client.get("/ai/dev/logs?limit=5")
    assert res.status_code == 200
    body = res.json()
    assert "data" in body
    entries = body["data"]
    assert len(entries) >= 2
    # Check that entries are dicts
    assert any(e.get("event") == "test.dev.entry.1" for e in entries)


@pytest.mark.asyncio
async def test_logs_filter_by_session(client):
    log_step("sess.entry.a", session_id="sess-filter-target")
    log_step("sess.entry.b", session_id="sess-filter-other")

    res = await client.get("/ai/dev/logs?sessionId=sess-filter-target")
    assert res.status_code == 200
    entries = res.json()["data"]
    assert all(e.get("session_id") == "sess-filter-target" for e in entries if "session_id" in e)


@pytest.mark.asyncio
async def test_logs_stream_pushes_new_entry():
    received_bodies = []
    received_event = asyncio.Event()

    disconnect_event = asyncio.Event()

    async def receive():
        await disconnect_event.wait()
        return {"type": "http.disconnect"}

    async def send(message):
        if message["type"] == "http.response.body" and message.get("body"):
            body_text = message["body"].decode("utf-8")
            received_bodies.append(body_text)
            if "live.stream.event" in body_text:
                received_event.set()
                disconnect_event.set()

    scope = {
        "type": "http",
        "asgi": {"version": "3.0"},
        "http_version": "1.1",
        "method": "GET",
        "path": "/ai/dev/logs/stream",
        "raw_path": b"/ai/dev/logs/stream",
        "query_string": b"",
        "headers": [],
    }

    app_task = asyncio.create_task(app(scope, receive, send))

    async def log_producer():
        for _ in range(5):
            await asyncio.sleep(0.05)
            log_step("live.stream.event", live_field=42)
            if received_event.is_set():
                break

    producer_task = asyncio.create_task(log_producer())

    try:
        await asyncio.wait_for(received_event.wait(), timeout=3.0)
    finally:
        producer_task.cancel()
        app_task.cancel()
        try:
            await app_task
        except (asyncio.CancelledError, Exception):
            pass

    full_output = "".join(received_bodies)
    assert "event: log" in full_output
    assert "live.stream.event" in full_output


@pytest.mark.asyncio
async def test_dev_routes_absent_in_production(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    get_settings.cache_clear()

    # Recreate client under production settings
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as prod_client:
        res1 = await prod_client.get("/ai/dev/logs")
        assert res1.status_code == 404

        res2 = await prod_client.get("/ai/dev/logs/stream")
        assert res2.status_code == 404

        res3 = await prod_client.get("/ui")
        assert res3.status_code == 404

    monkeypatch.undo()
    get_settings.cache_clear()


@pytest.mark.asyncio
async def test_logs_never_contain_message_text(client):
    secret = "SECRET-SENTENCE-123"
    await client.post(
        "/ai/chat/messages",
        data={"message": f"Hello {secret}"},
    )

    res = await client.get("/ai/dev/logs?limit=50")
    assert res.status_code == 200
    for entry in res.json()["data"]:
        entry_str = json.dumps(entry)
        assert secret not in entry_str
