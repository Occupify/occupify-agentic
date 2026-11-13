import uuid
from datetime import UTC, datetime
from decimal import Decimal
from typing import Any

from pgvector.sqlalchemy import Vector
from sqlalchemy import (
    JSON,
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import TypeDecorator


class TSVectorType(TypeDecorator):
    impl = Text
    cache_ok = True

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            return dialect.type_descriptor(TSVECTOR())
        return dialect.type_descriptor(Text())


class TZDateTime(TypeDecorator):
    impl = DateTime
    cache_ok = True

    def process_result_value(self, value: Any, dialect: Any) -> Any:
        if value is not None and isinstance(value, datetime) and value.tzinfo is None:
            return value.replace(tzinfo=UTC)
        return value


def utc_now() -> datetime:
    return datetime.now(UTC)


class Base(DeclarativeBase):
    pass


class AgentRun(Base):
    __tablename__ = "agent_runs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    use_case: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[str] = mapped_column(String(100), nullable=False)
    session_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, default="running"
    )  # running, succeeded, failed
    model: Mapped[str] = mapped_column(String(50), nullable=False)
    tokens_in: Mapped[int] = mapped_column(Integer, default=0)
    tokens_out: Mapped[int] = mapped_column(Integer, default=0)
    latency_ms: Mapped[int] = mapped_column(Integer, default=0)
    steps: Mapped[list[Any]] = mapped_column(JSON, default=list)
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    trace_id: Mapped[str] = mapped_column(String(64), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    sha256: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    extractor: Mapped[str] = mapped_column(String(20), nullable=False)
    page_count: Mapped[int] = mapped_column(Integer, nullable=False)
    cleaned_text: Mapped[str] = mapped_column(Text, nullable=False)
    removed_counts: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(100), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    message_count: Mapped[int] = mapped_column(Integer, default=0)
    busy_since: Mapped[datetime | None] = mapped_column(TZDateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, onupdate=utc_now
    )

    messages: Mapped[list["ChatMessage"]] = relationship(
        "ChatMessage",
        back_populates="session",
        cascade="all, delete-orphan",
        order_by="ChatMessage.seq",
    )

    __table_args__ = (Index("ix_chat_sessions_user_updated", "user_id", "updated_at"),)


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("chat_sessions.id", ondelete="CASCADE"),
        nullable=False,
    )
    user_id: Mapped[str] = mapped_column(String(100), nullable=False)
    seq: Mapped[int] = mapped_column(Integer, nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False)  # user | assistant
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, default="complete"
    )  # complete | interrupted
    display_text: Mapped[str] = mapped_column(Text, nullable=False)
    attachments: Mapped[list[Any]] = mapped_column(JSON, default=list)
    model_messages: Mapped[list[Any]] = mapped_column(JSON, default=list)
    client_message_id: Mapped[str | None] = mapped_column(String(64), nullable=True)
    run_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    tokens_in: Mapped[int] = mapped_column(Integer, default=0)
    tokens_out: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    session: Mapped["ChatSession"] = relationship("ChatSession", back_populates="messages")

    __table_args__ = (
        UniqueConstraint("session_id", "seq", name="uq_chat_messages_session_seq"),
        Index("ix_chat_messages_session_client_id", "session_id", "client_message_id"),
    )


class JobIndexRow(Base):
    __tablename__ = "job_index"

    job_id: Mapped[str] = mapped_column(String(64), primary_key=True)
    project_id: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    project_title: Mapped[str] = mapped_column(Text, nullable=False)
    project_description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    job_title: Mapped[str] = mapped_column(Text, nullable=False)
    job_description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    skills: Mapped[list[str]] = mapped_column(JSON, default=list)
    requirements: Mapped[list[str]] = mapped_column(JSON, default=list)
    salary_type: Mapped[str] = mapped_column(String(20), nullable=False)
    budget_min: Mapped[Decimal | None] = mapped_column(Numeric(15, 2), nullable=True)
    budget_max: Mapped[Decimal | None] = mapped_column(Numeric(15, 2), nullable=True)
    experience_level: Mapped[str] = mapped_column(String(50), nullable=False)
    period: Mapped[str] = mapped_column(String(20), nullable=False)
    hours_per_day: Mapped[float | None] = mapped_column(Float, nullable=True)
    project_status: Mapped[str] = mapped_column(String(20), nullable=False)
    job_status: Mapped[str] = mapped_column(String(20), nullable=False)
    doc_text: Mapped[str] = mapped_column(Text, nullable=False)
    embedding: Mapped[list[float]] = mapped_column(Vector(1024), nullable=False)
    search_tsv: Mapped[Any | None] = mapped_column(TSVectorType, nullable=True)

    __table_args__ = (
        Index("ix_job_index_filters", "salary_type", "experience_level"),
        Index(
            "ix_job_index_embedding_hnsw",
            "embedding",
            postgresql_using="hnsw",
            postgresql_ops={"embedding": "vector_cosine_ops"},
        ),
        Index("ix_job_index_search_tsv_gin", "search_tsv", postgresql_using="gin"),
    )


class IndexMetaModel(Base):
    __tablename__ = "index_meta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, default=1)
    embed_model: Mapped[str] = mapped_column(String(100), nullable=False)
    dim: Mapped[int] = mapped_column(Integer, nullable=False)
    source: Mapped[str] = mapped_column(String(50), nullable=False, default="rpc")
    doc_text_version: Mapped[str] = mapped_column(String(20), nullable=False, default="v1")
    built_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    jobs_n: Mapped[int] = mapped_column(Integer, default=0)


class CareerKnowledgeChunk(Base):
    __tablename__ = "career_knowledge_chunks"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    source_id: Mapped[str] = mapped_column(String(50), nullable=False)  # roadmap.sh, esco, onet
    source_record_id: Mapped[str] = mapped_column(String(255), nullable=False)
    source_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_version: Mapped[str] = mapped_column(String(50), default="v1", nullable=False)
    source_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # learning_roadmap, occupation_taxonomy, skill_competency
    title: Mapped[str] = mapped_column(Text, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    chunk_metadata: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    embedding: Mapped[list[float]] = mapped_column(Vector(1024), nullable=False)
    search_tsv: Mapped[Any | None] = mapped_column(TSVectorType, nullable=True)

    __table_args__ = (
        UniqueConstraint(
            "source_id", "source_record_id", "title", name="uq_career_chunk_source_record"
        ),
        Index(
            "ix_career_knowledge_chunks_embedding_hnsw",
            "embedding",
            postgresql_using="hnsw",
            postgresql_ops={"embedding": "vector_cosine_ops"},
        ),
        Index("ix_career_knowledge_chunks_search_tsv_gin", "search_tsv", postgresql_using="gin"),
        Index("ix_career_knowledge_chunks_source_filter", "source_id", "source_type"),
    )


class CareerIngestionRun(Base):
    __tablename__ = "career_ingestion_runs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    source_id: Mapped[str] = mapped_column(String(50), nullable=False)
    source_version: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, default="running"
    )  # running, completed, failed
    chunks_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    manifest_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class UserMemory(Base):
    __tablename__ = "user_memory"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(100), nullable=False)
    category: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # career, skills, preferences, general
    key: Mapped[str] = mapped_column(String(100), nullable=False)
    value: Mapped[Any] = mapped_column(JSON, nullable=False)
    is_confirmed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    source: Mapped[str] = mapped_column(
        String(100), default="user_chat", nullable=False
    )  # user_chat, cv_extracted, rag_reasoning
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, onupdate=utc_now
    )
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        UniqueConstraint("user_id", "category", "key", name="uq_user_memory_key"),
        Index("ix_user_memory_user_category", "user_id", "category"),
    )


class TaskCheckpoint(Base):
    __tablename__ = "task_checkpoints"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("chat_sessions.id", ondelete="CASCADE"),
        nullable=False,
    )
    user_id: Mapped[str] = mapped_column(String(100), nullable=False)
    task_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # career_consulting, job_matching, etc.
    stage: Mapped[str] = mapped_column(String(50), nullable=False)  # DISCOVERY, ASSESSMENT, etc.
    goal: Mapped[str] = mapped_column(Text, nullable=False)
    constraints: Mapped[list[Any]] = mapped_column(JSON, default=list)
    completed_steps: Mapped[list[str]] = mapped_column(JSON, default=list)
    pending_steps: Mapped[list[str]] = mapped_column(JSON, default=list)
    blockers: Mapped[list[str]] = mapped_column(JSON, default=list)
    decisions: Mapped[list[dict[str, Any]]] = mapped_column(JSON, default=list)
    next_action: Mapped[str | None] = mapped_column(Text, nullable=True)
    checkpoint_seq: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    __table_args__ = (
        Index("ix_task_checkpoints_session_seq", "session_id", "checkpoint_seq"),
        Index("ix_task_checkpoints_user_task", "user_id", "task_type"),
    )


class CvImprovementSession(Base):
    __tablename__ = "cv_improvement_sessions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    chat_session_id: Mapped[str | None] = mapped_column(String(36), nullable=True, index=True)
    status: Mapped[str] = mapped_column(String(30), nullable=False, default="INIT")
    # INIT -> ANALYZING -> WAITING_USER_REVIEW -> REVISING -> PDF_GENERATED -> COMPLETED (or CANCELLED)
    original_cv_text: Mapped[str] = mapped_column(Text, nullable=False)
    target_jd_text: Mapped[str] = mapped_column(Text, nullable=False)
    proposals: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    user_decisions: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)
    revised_resume_data: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)
    pdf_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utc_now, onupdate=utc_now
    )

    __table_args__ = (
        Index("ix_cv_improvement_sessions_user_updated", "user_id", "updated_at"),
    )

    @property
    def step(self) -> str:
        return self.status

    @step.setter
    def step(self, value: str) -> None:
        self.status = value

