from fastapi import APIRouter, Depends, File, Form, Query, UploadFile
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.errors import SessionNotFoundError
from app.core.responses import page_response, success_response
from app.core.security import CurrentUser, get_current_user
from app.db.session import get_db_session
from app.features.chat.schemas import (
    ChatMessageItem,
    ChatSessionItem,
)
from app.features.chat.service import ChatService
from app.pydantic_ai_helpers import stream_chat_turn

router = APIRouter(prefix="/ai/chat", tags=["chat"])


@router.post("/messages")
async def send_chat_message(
    message: str = Form(...),
    sessionId: str | None = Form(None),
    context: str | None = Form(None),
    clientMessageId: str | None = Form(None),
    files: list[UploadFile] | None = File(None),
    stream: bool = Query(False),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    service = ChatService(db)

    if not stream:
        result = await service.send_message(
            user=user,
            message=message,
            session_id=sessionId,
            context=context,
            client_message_id=clientMessageId,
            files=files,
        )
        return success_response(result.model_dump())

    # Streaming mode
    return StreamingResponse(
        stream_chat_turn(
            service=service,
            user=user,
            message=message,
            session_id=sessionId,
            context=context,
            client_message_id=clientMessageId,
            files=files,
        ),
        media_type="text/event-stream",
    )


@router.get("/sessions")
async def list_chat_sessions(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    service = ChatService(db)
    sessions, total = await service.chat_repo.list_sessions(user.user_id, page=page, limit=limit)
    items = [
        ChatSessionItem(
            id=s.id,
            userId=s.user_id,
            title=s.title,
            messageCount=s.message_count,
            createdAt=s.created_at,
            updatedAt=s.updated_at,
        ).model_dump()
        for s in sessions
    ]
    return page_response(items, page=page, limit=limit, total=total)


@router.get("/sessions/{sessionId}/messages")
async def get_session_messages(
    sessionId: str,
    page: int = Query(1, ge=1),
    limit: int = Query(50, ge=1, le=100),
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    service = ChatService(db)
    sess = await service.chat_repo.get_session(sessionId, user.user_id)
    if not sess:
        raise SessionNotFoundError()

    messages, total = await service.chat_repo.get_messages(
        sessionId, user.user_id, page=page, limit=limit
    )
    items = [
        ChatMessageItem(
            id=m.id,
            sessionId=m.session_id,
            seq=m.seq,
            role=m.role,
            displayText=m.display_text,
            attachments=m.attachments,
            createdAt=m.created_at,
        ).model_dump()
        for m in messages
    ]
    return page_response(items, page=page, limit=limit, total=total)


@router.delete("/sessions/{sessionId}")
async def delete_chat_session(
    sessionId: str,
    user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db_session),
):
    service = ChatService(db)
    deleted = await service.chat_repo.delete_session(sessionId, user.user_id)
    if not deleted:
        raise SessionNotFoundError()
    return success_response({"deleted": True})
