import pytest
from pydantic_ai.messages import ModelMessage, ModelResponse, TextPart
from pydantic_ai.models.function import AgentInfo, FunctionModel

from app.db.repositories.chat import ChatRepository
from app.features.chat.agent import chat_agent
from tests.unit.test_documents import generate_sample_pdf


@pytest.mark.asyncio
async def test_chat_new_session_and_history_replay(client):
    received_messages_turn_2: list[ModelMessage] = []

    async def mock_fn(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
        nonlocal received_messages_turn_2
        if len(messages) > 1:
            received_messages_turn_2 = list(messages)
            return ModelResponse(parts=[TextPart("Turn 2 answer: I remember your turn 1.")])
        return ModelResponse(parts=[TextPart("Turn 1 answer: Nice to meet you!")])

    with chat_agent.override(model=FunctionModel(mock_fn)):
        # Turn 1: no sessionId
        res1 = await client.post(
            "/ai/chat/messages",
            data={"message": "Hello, I am looking for a Python backend role."},
        )
        assert res1.status_code == 200
        data1 = res1.json()["data"]
        session_id = data1["sessionId"]
        assert data1["newSession"] is True
        assert data1["reply"] == "Turn 1 answer: Nice to meet you!"

        # Turn 2: with sessionId
        res2 = await client.post(
            "/ai/chat/messages",
            data={
                "sessionId": session_id,
                "message": "What skills do I need?",
            },
        )
        assert res2.status_code == 200
        data2 = res2.json()["data"]
        assert data2["sessionId"] == session_id
        assert data2["newSession"] is False
        assert "Turn 2 answer" in data2["reply"]

        # Assert turn 2 received turn 1 history!
        assert len(received_messages_turn_2) >= 2


@pytest.mark.asyncio
async def test_chat_unknown_session_404(client):
    res = await client.post(
        "/ai/chat/messages",
        data={
            "sessionId": "00000000-0000-0000-0000-000000000000",
            "message": "Continuing non-existent chat",
        },
    )
    assert res.status_code == 404
    data = res.json()
    assert data["errorCode"] == "CHAT_SESSION_NOT_FOUND"
    assert "Failed to find this chat session" in data["message"]


@pytest.mark.asyncio
async def test_chat_pii_cleaned_before_model(client):
    inspected_prompts = []

    async def mock_fn(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
        for m in messages:
            for part in getattr(m, "parts", []):
                if hasattr(part, "content"):
                    inspected_prompts.append(str(part.content))
        return ModelResponse(parts=[TextPart("Response with no PII.")])

    with chat_agent.override(model=FunctionModel(mock_fn)):
        res = await client.post(
            "/ai/chat/messages",
            data={
                "message": "Contact me at personal.secret@gmail.com or 0912345678.",
            },
        )
        assert res.status_code == 200
        assert len(inspected_prompts) > 0
        joined = " ".join(inspected_prompts)
        assert "personal.secret@gmail.com" not in joined
        assert "0912345678" not in joined
        assert "[EMAIL]" in joined
        assert "[PHONE]" in joined


@pytest.mark.asyncio
async def test_chat_idempotency_client_message_id(client):
    async def mock_fn(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
        return ModelResponse(parts=[TextPart("Idempotent response")])

    with chat_agent.override(model=FunctionModel(mock_fn)):
        cid = "11111111-2222-3333-4444-555555555555"
        # First turn
        res1 = await client.post(
            "/ai/chat/messages",
            data={"message": "First call", "clientMessageId": cid},
        )
        assert res1.status_code == 200
        sess_id = res1.json()["data"]["sessionId"]

        # Duplicate call with same clientMessageId & sessionId
        res2 = await client.post(
            "/ai/chat/messages",
            data={"sessionId": sess_id, "message": "Duplicate call", "clientMessageId": cid},
        )
        assert res2.status_code == 200
        assert res2.json()["data"]["reply"] == "Idempotent response"


@pytest.mark.asyncio
async def test_chat_session_busy_409(client, test_db):
    repo = ChatRepository(test_db)
    sess = await repo.create_session("test-user-uuid-123", "Busy Session")
    await repo.mark_busy(sess.id)

    res = await client.post(
        "/ai/chat/messages",
        data={"sessionId": sess.id, "message": "Another message while busy"},
    )
    assert res.status_code == 409
    data = res.json()
    assert data["errorCode"] == "CHAT_BUSY"
    assert "still being answered" in data["message"]


@pytest.mark.asyncio
async def test_chat_list_and_delete_session(client):
    async def mock_fn(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
        return ModelResponse(parts=[TextPart("OK")])

    with chat_agent.override(model=FunctionModel(mock_fn)):
        # Create session
        res = await client.post(
            "/ai/chat/messages",
            data={"message": "Session to be deleted"},
        )
        sess_id = res.json()["data"]["sessionId"]

        # List sessions
        list_res = await client.get("/ai/chat/sessions")
        assert list_res.status_code == 200
        sessions = list_res.json()["data"]
        assert any(s["id"] == sess_id for s in sessions)

        # Get messages
        msg_res = await client.get(f"/ai/chat/sessions/{sess_id}/messages")
        assert msg_res.status_code == 200
        assert len(msg_res.json()["data"]) >= 2  # user + assistant

        # Delete session
        del_res = await client.delete(f"/ai/chat/sessions/{sess_id}")
        assert del_res.status_code == 200

        # Subsequent get returns 404
        msg_res_404 = await client.get(f"/ai/chat/sessions/{sess_id}/messages")
        assert msg_res_404.status_code == 404


@pytest.mark.asyncio
async def test_chat_pdf_attachment(client):
    content = generate_sample_pdf(
        pages=1, text="Nguyen Van B - Email: b@test.com\n## Experience\nPython Senior"
    )

    async def mock_fn(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
        return ModelResponse(parts=[TextPart("Analyzed your CV.")])

    with chat_agent.override(model=FunctionModel(mock_fn)):
        files = {"files": ("sample_cv.pdf", content, "application/pdf")}
        res = await client.post(
            "/ai/chat/messages",
            data={"message": "Please review my attached CV."},
            files=files,
        )
        assert res.status_code == 200
        data = res.json()["data"]
        assert len(data["attachments"]) == 1
        assert data["attachments"][0]["fileName"] == "sample_cv.pdf"
        assert data["attachments"][0]["pages"] == 1


@pytest.mark.asyncio
async def test_chat_streaming(client):
    async def stream_fn(messages: list[ModelMessage], info: AgentInfo):
        yield "Streaming "
        yield "word by word."

    with chat_agent.override(model=FunctionModel(stream_function=stream_fn)):
        res = await client.post(
            "/ai/chat/messages?stream=true",
            data={"message": "Stream this reply"},
        )
        assert res.status_code == 200
        text = res.text
        assert "event: meta" in text
        assert "event: delta" in text
        assert "event: done" in text
        # Verify plan §6.9 SSE contract (F-25)
        assert '"sessionId":' in text
        assert '"newSession":' in text
        assert '"messageId":' in text
        assert '"attachments":' in text
        assert '"text":' in text
        assert '"model":' in text
        assert '"usage":' in text
        assert '"tokensIn":' in text


@pytest.mark.asyncio
async def test_chat_streaming_heartbeat_survives_model_pause(client, monkeypatch):
    import asyncio

    from app.core.config import get_settings

    # Set heartbeat to 0.1s so we can test ping without slowing tests down (F-21)
    monkeypatch.setattr(get_settings(), "CHAT_STREAM_HEARTBEAT_S", 0.1)

    async def stream_fn(messages: list[ModelMessage], info: AgentInfo):
        yield "First chunk. "
        await asyncio.sleep(0.25)  # Pause longer than 0.1s heartbeat!
        yield "Second chunk after quiet pause."

    with chat_agent.override(model=FunctionModel(stream_function=stream_fn)):
        res = await client.post(
            "/ai/chat/messages?stream=true",
            data={"message": "Model pauses for heartbeat"},
        )
        assert res.status_code == 200
        text = res.text
        assert ": ping" in text
        assert "First chunk." in text
        assert "Second chunk after quiet pause." in text
        assert "event: done" in text


@pytest.mark.asyncio
async def test_no_new_session_created_on_validation_failure(client, test_db):
    from sqlalchemy import func, select

    from app.db.models import ChatSession

    # Count sessions before
    count_before = (await test_db.execute(select(func.count(ChatSession.id)))).scalar() or 0

    # 1. Reject invalid file (>20 pages)
    large_pdf = generate_sample_pdf(pages=25, text="Too big")
    files = {"files": ("big.pdf", large_pdf, "application/pdf")}
    res = await client.post(
        "/ai/chat/messages",
        data={"message": "Analyze my giant PDF"},
        files=files,
    )
    assert res.status_code == 400
    assert res.json()["errorCode"] == "FILE_INVALID"

    # Count sessions after - must NOT have created an empty session! (F-24)
    count_after = (await test_db.execute(select(func.count(ChatSession.id)))).scalar() or 0
    assert count_after == count_before


@pytest.mark.asyncio
async def test_empty_message_raises_400(client):
    res = await client.post(
        "/ai/chat/messages",
        data={"message": "   "},
    )
    assert res.status_code == 400
    assert res.json()["errorCode"] == "MESSAGE_EMPTY"


@pytest.mark.asyncio
async def test_chat_context_full_error(client):
    async def mock_fn(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
        raise Exception("model_context_window_exceeded: maximum tokens reached")

    with chat_agent.override(model=FunctionModel(mock_fn)):
        res = await client.post(
            "/ai/chat/messages",
            data={"message": "Long conversation turn"},
        )
        assert res.status_code == 422
        data = res.json()
        assert data["errorCode"] == "CHAT_CONTEXT_FULL"
        assert "too long for the model" in data["message"]


@pytest.mark.asyncio
async def test_chat_attachment_filename_masked_in_prompt(client):
    received_prompts = []

    async def mock_fn(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
        for m in messages:
            for part in getattr(m, "parts", []):
                if hasattr(part, "content"):
                    received_prompts.append(str(part.content))
        return ModelResponse(parts=[TextPart("Reviewed your document.")])

    content = generate_sample_pdf(
        pages=1, text="Nguyen Van An\n## Experience\nSenior Software Engineer at Tech Corp"
    )
    with chat_agent.override(model=FunctionModel(mock_fn)):
        files = {"files": ("CV_Nguyen_Van_An_Confidential.pdf", content, "application/pdf")}
        res = await client.post(
            "/ai/chat/messages",
            data={"message": "Please review my attached CV."},
            files=files,
        )
        assert res.status_code == 200
        # Assert the real filename is in the API response
        assert (
            res.json()["data"]["attachments"][0]["fileName"] == "CV_Nguyen_Van_An_Confidential.pdf"
        )

        # Assert the real filename NEVER went to the model prompt (F-02)
        joined_prompt = " ".join(received_prompts)
        assert "CV_Nguyen_Van_An_Confidential.pdf" not in joined_prompt
        assert "Attachment 1" in joined_prompt


@pytest.mark.asyncio
async def test_chat_session_checked_before_file_read(client):
    content = generate_sample_pdf(pages=1, text="Confidential CV")
    files = {"files": ("my_cv.pdf", content, "application/pdf")}
    res = await client.post(
        "/ai/chat/messages",
        data={
            "sessionId": "00000000-0000-0000-0000-000000000000",
            "message": "Review this on non-existent session",
        },
        files=files,
    )
    assert res.status_code == 404
    assert res.json()["errorCode"] == "CHAT_SESSION_NOT_FOUND"


@pytest.mark.asyncio
async def test_document_upsert_on_conflict(test_db):
    from app.db.repositories.documents import DocumentRepository

    repo = DocumentRepository(test_db)
    sha = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

    doc1 = await repo.save_document(
        sha256_hash=sha,
        extractor="pdfium",
        page_count=1,
        cleaned_text="Version 1",
        removed_counts={},
        ttl_days=-1,  # Expired immediately
    )
    assert doc1.cleaned_text == "Version 1"

    # Save again with same sha256 - must UPSERT rather than fail with IntegrityError (F-07)
    doc2 = await repo.save_document(
        sha256_hash=sha,
        extractor="pdfium",
        page_count=1,
        cleaned_text="Version 2 Updated",
        removed_counts={"email": 1},
        ttl_days=30,
    )
    assert doc2.id == doc1.id
    assert doc2.cleaned_text == "Version 2 Updated"


@pytest.mark.asyncio
async def test_readiness_probe_broker_status(client):
    from app.messaging import broker as broker_mod

    # 1. When broker is not connected, /ready returns 503 (F-10)
    broker_mod._broker_connected = False
    res_down = await client.get("/ready")
    assert res_down.status_code == 503
    assert res_down.json()["checks"]["broker"] == "DOWN"
    assert res_down.json()["status"] == "DOWN"

    # 2. When broker is connected, /ready returns 200 UP
    broker_mod._broker_connected = True
    res_up = await client.get("/ready")
    assert res_up.status_code == 200
    assert res_up.json()["checks"]["broker"] == "UP"
    assert res_up.json()["status"] == "UP"
