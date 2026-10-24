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
    content = generate_sample_pdf(pages=1, text="Nguyen Van B - Email: b@test.com - Python Senior")

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
