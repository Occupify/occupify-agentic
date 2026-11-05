from datetime import datetime
from typing import Any

from pydantic import BaseModel


class AttachmentInfo(BaseModel):
    fileName: str
    pages: int
    removed: dict[str, int]


class TokenUsage(BaseModel):
    tokensIn: int
    tokensOut: int


class ChatReplyData(BaseModel):
    sessionId: str
    newSession: bool
    messageId: str
    reply: str
    attachments: list[AttachmentInfo]
    model: str
    usage: TokenUsage
    state: dict[str, Any] | None = None
    memory: list[dict[str, Any]] | None = None


class ChatSessionItem(BaseModel):
    id: str
    userId: str
    title: str
    messageCount: int
    createdAt: datetime
    updatedAt: datetime


class ChatMessageItem(BaseModel):
    id: str
    sessionId: str
    seq: int
    role: str
    displayText: str
    attachments: list[Any]
    createdAt: datetime
