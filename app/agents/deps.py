import asyncio
from dataclasses import dataclass, field
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import CurrentUser


@dataclass
class AgentDeps:
    user: CurrentUser
    session_id: str | None = None
    db: AsyncSession | None = None
    db_lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    rpc: Any = None
    parent_run_id: str | None = None
    agent_role: str = "primary"
    turn_documents: list[str] = field(default_factory=list)
    on_progress: Any = None
    job_match_memo: Any = None
    job_match_block: str | None = None
    pipeline_tokens_in: int = 0
    pipeline_tokens_out: int = 0
