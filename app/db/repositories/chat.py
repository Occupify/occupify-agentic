import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import desc, func, select
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
        session_id: str | None = None,
    ) -> ChatSession:
        now = datetime.now(UTC)
        chat_sess = ChatSession(
            id=session_id or str(uuid.uuid4()),
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

    async def mark_busy(self, session_id: str) -> bool:
        sess = await self.session.get(ChatSession, session_id)
        if not sess:
            return False
        if sess.busy_since is not None:
            # Check if stale (e.g. > 120s)
            elapsed = (datetime.now(UTC) - sess.busy_since).total_seconds()
            if elapsed < 120:
                return False  # Still busy
        sess.busy_since = datetime.now(UTC)
        await self.session.commit()
        return True

    async def clear_busy(self, session_id: str) -> None:
        sess = await self.session.get(ChatSession, session_id)
        if sess:
            sess.busy_since = None
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
            id=str(uuid.uuid4()),
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
