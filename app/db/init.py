from datetime import UTC, datetime

from sqlalchemy import text, update

from app.core.logging import log_step
from app.db.models import AgentRun, Base, ChatSession
from app.db.session import get_engine, get_sessionmaker


async def init_db() -> None:
    """
    Initializes the database:
    - Runs CREATE EXTENSION IF NOT EXISTS vector/unaccent on PostgreSQL
    - Runs Base.metadata.create_all() (creates missing tables without migrations)
    - Updates stale 'running' AgentRun rows to 'failed'
    - Clears stale 'busy_since' flags on ChatSession rows
    """
    engine = get_engine()
    async with engine.begin() as conn:
        if conn.dialect.name == "postgresql":
            await conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
            await conn.execute(text("CREATE EXTENSION IF NOT EXISTS unaccent;"))
            await conn.execute(
                text(
                    "ALTER TABLE IF EXISTS index_meta ADD COLUMN IF NOT EXISTS doc_text_version VARCHAR(20) DEFAULT 'v1' NOT NULL;"
                )
            )
        await conn.run_sync(Base.metadata.create_all)

    sessionmaker = get_sessionmaker()
    async with sessionmaker() as session:
        # Mark interrupted/crashed runs as failed
        now = datetime.now(UTC)
        stmt_runs = (
            update(AgentRun)
            .where(AgentRun.status == "running")
            .values(status="failed", error="Process terminated unexpectedly", finished_at=now)
        )
        await session.execute(stmt_runs)

        # Clear busy flags on chat sessions
        stmt_sessions = (
            update(ChatSession).where(ChatSession.busy_since.is_not(None)).values(busy_since=None)
        )
        await session.execute(stmt_sessions)
        await session.commit()

    log_step("db.init", status="ready")
