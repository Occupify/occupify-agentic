from dataclasses import dataclass
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import CurrentUser


@dataclass
class AgentDeps:
    user: CurrentUser
    session_id: str | None = None
    db: AsyncSession | None = None
    rpc: Any | None = None
