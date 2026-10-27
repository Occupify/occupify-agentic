from datetime import datetime
from decimal import Decimal
from typing import Any, Literal, Protocol

from pydantic import BaseModel, Field

from app.features.job_match.schemas import (
    ErrorCode,
    MatchCriteria,
    RunOutcome,
    RunStatus,
)


class IndexRow(BaseModel):
    job_id: str
    project_id: str
    project_title: str
    project_description: str
    job_title: str
    job_description: str
    skills: list[str] = Field(default_factory=list)
    requirements: list[str] = Field(default_factory=list)
    salary_type: str | None = None
    budget_min: Decimal | None = None
    budget_max: Decimal | None = None
    experience_level: str | None = None
    period: str | None = None
    hours_per_day: float | None = None
    project_status: str
    job_status: str
    doc_text: str
    active: bool = True
    missed_sweeps: int = 0
    content_hash: str | None = None
    embedding: list[float] | None = None
    embedding_model: str | None = None
    indexed_at: datetime | None = None


class IndexHit(BaseModel):
    job_id: str
    project_id: str
    rank: int
    score: float


class IndexMeta(BaseModel):
    embed_model: str
    dim: int
    source: str
    built_at: datetime
    jobs_n: int


class UpsertStats(BaseModel):
    inserted: int
    updated: int
    reembed_queued: int
    unchanged: int


class JobIndex(Protocol):
    async def upsert(self, rows: list[IndexRow]) -> UpsertStats: ...

    async def hybrid_search(
        self,
        dense_queries: list[list[float]],
        lexical: str,
        criteria: MatchCriteria,
        top: int = 50,
    ) -> tuple[list[list[IndexHit]], list[IndexHit]]: ...

    async def get_rows(self, job_ids: list[str]) -> list[IndexRow]: ...

    async def mark_inactive(self, job_ids: list[str]) -> None: ...

    async def meta(self) -> IndexMeta | None: ...

    def is_usable(self) -> bool: ...


class PipelineOptions(BaseModel):
    dense: bool = True
    lexical: bool = True
    rerank: bool = True
    features: bool = True
    search_agent: bool = True
    prompt_mode: Literal["skill", "plain"] = "skill"
    list_size: int = 50
    pool_size: int = 40


class RunState:
    """Mutable run state read by the service on timeout or progress."""

    def __init__(self, run_id: str = "", fitting_projects_count: int = 0, exhausted: bool = False):
        self.run_id: str = run_id
        self.stage: str = "init"
        self.fitting_projects_count: int = fitting_projects_count
        self.exhausted: bool = exhausted
        self.ranking: list[dict[str, Any]] = []
        self.warnings: list[dict[str, str]] = []
        self.tokens_in: int = 0
        self.tokens_out: int = 0
        self.cost_usd: float = 0.0
        self.stages: list[dict[str, Any]] = []
        self.pool_job_ids: list[str] = []


class RunResult(BaseModel):
    status: RunStatus = RunStatus.SUCCEEDED
    outcome: RunOutcome | None = None
    stop_reason: str | None = None
    error_code: ErrorCode | None = None
    message: str = ""
    warnings: list[Any] = Field(default_factory=list)
    items: list[Any] = Field(default_factory=list)
    top_missing_skills: list[str] = Field(default_factory=list)
    profile: dict[str, Any] | None = None
    skill_versions: dict[str, str] = Field(default_factory=dict)
    scoring_version: str = "v1"
    tokens_in: int = 0
    tokens_out: int = 0
    cost_usd: float = 0.0
    stages: list[dict[str, Any]] = Field(default_factory=list)


PipelineResult = RunResult
