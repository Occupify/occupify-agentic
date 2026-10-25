import uuid
from datetime import UTC, datetime, timedelta
from typing import Any

from sqlalchemy import desc, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import ChatMessage, ChatSession


class ChatRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_session(self, session_id: str, user_id: str) -> ChatSession | None:
        stmt = (
            select(ChatSession)
            .where(ChatSession.id == session_id)
            .where(ChatSession.user_id == user_id)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def create_session(
        self,
        user_id: str,
        title: str,
    ) -> ChatSession:
        now = datetime.now(UTC)
        chat_sess = ChatSession(
            id=str(uuid.uuid4()),
            user_id=user_id,
            title=title[:255],
            message_count=0,
            created_at=now,
            updated_at=now,
        )
        self.session.add(chat_sess)
        await self.session.commit()
        await self.session.refresh(chat_sess)
        return chat_sess

    async def list_sessions(
        self,
        user_id: str,
        page: int = 1,
        limit: int = 20,
    ) -> tuple[list[ChatSession], int]:
        offset = (page - 1) * limit
        total_stmt = select(func.count(ChatSession.id)).where(ChatSession.user_id == user_id)
        total_res = await self.session.execute(total_stmt)
        total = total_res.scalar() or 0

        stmt = (
            select(ChatSession)
            .where(ChatSession.user_id == user_id)
            .order_by(desc(ChatSession.updated_at))
            .offset(offset)
            .limit(limit)
        )
        res = await self.session.execute(stmt)
        return list(res.scalars().all()), total

    async def delete_session(self, session_id: str, user_id: str) -> bool:
        sess = await self.get_session(session_id, user_id)
        if not sess:
            return False
        await self.session.delete(sess)
        await self.session.commit()
        return True

    async def mark_busy(
        self, session_id: str, user_id: str | None = None, stale_timeout_s: int = 300
    ) -> datetime | None:
        now = datetime.now(UTC)
        stale_cutoff = now - timedelta(seconds=stale_timeout_s)
        stmt = update(ChatSession).where(ChatSession.id == session_id)
        if user_id is not None:
            stmt = stmt.where(ChatSession.user_id == user_id)
        stmt = (
            stmt.where(or_(ChatSession.busy_since.is_(None), ChatSession.busy_since < stale_cutoff))
            .values(busy_since=now)
            .returning(ChatSession.busy_since)
        )
        res = await self.session.execute(stmt)
        await self.session.commit()
        token = res.scalar_one_or_none()
        return token

    async def clear_busy(
        self, session_id: str, user_id: str | None = None, token: datetime | None = None
    ) -> None:
        if token is None:
            return
        stmt = (
            update(ChatSession)
            .where(ChatSession.id == session_id)
            .where(ChatSession.busy_since == token)
        )
        if user_id is not None:
            stmt = stmt.where(ChatSession.user_id == user_id)
        stmt = stmt.values(busy_since=None)
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_messages(
        self,
        session_id: str,
        user_id: str,
        page: int = 1,
        limit: int = 50,
    ) -> tuple[list[ChatMessage], int]:
        offset = (page - 1) * limit
        total_stmt = (
            select(func.count(ChatMessage.id))
            .where(ChatMessage.session_id == session_id)
            .where(ChatMessage.user_id == user_id)
        )
        total_res = await self.session.execute(total_stmt)
        total = total_res.scalar() or 0

        stmt = (
            select(ChatMessage)
            .where(ChatMessage.session_id == session_id)
            .where(ChatMessage.user_id == user_id)
            .order_by(ChatMessage.seq)
            .offset(offset)
            .limit(limit)
        )
        res = await self.session.execute(stmt)
        return list(res.scalars().all()), total

    async def get_all_model_messages(self, session_id: str) -> list[Any]:
        """Loads all historical model_messages in seq order for agent turn replay."""
        stmt = (
            select(ChatMessage.model_messages)
            .where(ChatMessage.session_id == session_id)
            .order_by(ChatMessage.seq)
        )
        res = await self.session.execute(stmt)
        all_msgs = []
        for row in res.scalars():
            if isinstance(row, list):
                all_msgs.extend(row)
            elif row:
                all_msgs.append(row)
        return all_msgs

    async def get_by_client_message_id(
        self,
        session_id: str,
        client_message_id: str,
    ) -> ChatMessage | None:
        stmt = (
            select(ChatMessage)
            .where(ChatMessage.session_id == session_id)
            .where(ChatMessage.client_message_id == client_message_id)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def save_turn(
        self,
        session_id: str,
        user_id: str,
        user_display_text: str,
        assistant_display_text: str,
        user_model_messages: list[Any],
        assistant_model_messages: list[Any],
        attachments: list[Any] | None = None,
        client_message_id: str | None = None,
        run_id: str | None = None,
        tokens_in: int = 0,
        tokens_out: int = 0,
        status: str = "complete",
        asst_message_id: str | None = None,
    ) -> tuple[ChatMessage, ChatMessage]:
        now = datetime.now(UTC)
        sess = await self.session.get(ChatSession, session_id)
        next_seq = (sess.message_count if sess else 0) + 1

        # 1. User message
        user_msg = ChatMessage(
            id=str(uuid.uuid4()),
            session_id=session_id,
            user_id=user_id,
            seq=next_seq,
            role="user",
            status="complete",
            display_text=user_display_text,
            attachments=attachments or [],
            model_messages=user_model_messages,
            client_message_id=client_message_id,
            run_id=run_id,
            tokens_in=0,
            tokens_out=0,
            created_at=now,
        )
        self.session.add(user_msg)

        # 2. Assistant message
        asst_msg = ChatMessage(
            id=asst_message_id or str(uuid.uuid4()),
            session_id=session_id,
            user_id=user_id,
            seq=next_seq + 1,
            role="assistant",
            status=status,
            display_text=assistant_display_text,
            attachments=[],
            model_messages=assistant_model_messages,
            run_id=run_id,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            created_at=now,
        )
        self.session.add(asst_msg)

        if sess:
            sess.message_count = next_seq + 1
            sess.updated_at = now
            sess.busy_since = None

        await self.session.commit()
        await self.session.refresh(user_msg)
        await self.session.refresh(asst_msg)
        return user_msg, asst_msg
