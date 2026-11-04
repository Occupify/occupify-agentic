from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


class SourceMetadata(BaseModel):
    source_id: Literal["roadmap.sh", "esco", "onet"]
    source_record_id: str
    source_url: str | None = None
    source_version: str = "v1"
    source_type: Literal["learning_roadmap", "occupation_taxonomy", "skill_competency"]
    domain: str | None = None
    geography: str | None = None  # e.g., "EU" for ESCO, "US" for O*NET, "Global" for roadmap.sh
    language: str = "en"
    license: str | None = None
    extra: dict[str, Any] = Field(default_factory=dict)


class CareerKnowledgeRecord(BaseModel):
    source_meta: SourceMetadata
    title: str
    content: str
    summary: str | None = None
    skills: list[str] = Field(default_factory=list)
    competencies: list[str] = Field(default_factory=list)
    relations: list[dict[str, Any]] = Field(default_factory=list)
    sections: list[dict[str, Any]] = Field(default_factory=list)
    raw_attributes: dict[str, Any] = Field(default_factory=dict)


class IngestionManifestRecord(BaseModel):
    source_id: str
    source_version: str
    manifest_hash: str
    status: Literal["running", "completed", "failed"] = "running"
    chunks_count: int = 0
    created_at: datetime | None = None
    finished_at: datetime | None = None
    details: dict[str, Any] = Field(default_factory=dict)


class Citation(BaseModel):
    chunk_id: str
    source_id: str
    source_record_id: str
    title: str
    source_url: str | None = None
    snippet: str


class CareerRecommendation(BaseModel):
    claim: str
    evidence_citations: list[Citation] = Field(default_factory=list)
    confidence_level: Literal["high", "medium", "tentative_reasoning"] = "high"


class GroundedCareerResponse(BaseModel):
    answer: str
    recommendations: list[CareerRecommendation] = Field(default_factory=list)
    citations: list[Citation] = Field(default_factory=list)
    abstention: bool = False
    abstention_reason: str | None = None
    conflicting_sources: list[str] = Field(default_factory=list)
