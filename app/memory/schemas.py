from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class MemoryItemCreate(BaseModel):
    category: str = Field(..., description="Memory namespace: career, skills, preferences, general")
    key: str = Field(..., description="Unique fact identifier within category, e.g. target_role")
    value: Any = Field(..., description="Structured fact value (string, list, or dict)")
    is_confirmed: bool = Field(
        default=False,
        description="True if explicitly stated/confirmed by user; False if inferred by agent",
    )
    confidence: float = Field(
        default=1.0, ge=0.0, le=1.0, description="Confidence score 0.0 to 1.0"
    )
    source: str = Field(
        default="user_chat", description="Origin: user_chat, cv_extracted, rag_reasoning"
    )
    ttl_seconds: int | None = Field(default=None, description="Optional retention TTL in seconds")


class MemoryItemRead(BaseModel):
    id: str
    user_id: str
    category: str
    key: str
    value: Any
    is_confirmed: bool
    confidence: float
    source: str
    created_at: datetime
    updated_at: datetime
    expires_at: datetime | None = None


class UserMemorySummary(BaseModel):
    items: list[MemoryItemRead] = Field(default_factory=list)

    def format_for_prompt(self) -> str:
        """Formats active memory into a concise markdown context block for LLM prompts."""
        if not self.items:
            return ""

        lines = ["<ACTIVE_USER_MEMORY>"]
        for it in self.items:
            status = (
                "user-confirmed" if it.is_confirmed else f"inferred (conf: {it.confidence:.2f})"
            )
            val_str = str(it.value)
            lines.append(f"- [{it.category}] {it.key}: {val_str} ({status}, src: {it.source})")
        lines.append("</ACTIVE_USER_MEMORY>")
        return "\n".join(lines)
