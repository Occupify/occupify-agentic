from enum import StrEnum
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator

from app.core.errors import AppError


class SalaryTypeFilter(StrEnum):
    FIXED = "FIXED"
    HOURLY = "HOURLY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class ExperienceLevelFilter(StrEnum):
    ENTRY = "ENTRY"
    INTERMEDIATE = "INTERMEDIATE"
    EXPERT = "EXPERT"


class HoursPerDayFilter(StrEnum):
    UNDER_FOUR = "under-4h"
    FOUR_TO_EIGHT = "4h-8h"
    ABOVE_EIGHT = "above-8h"


class RunStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    PARTIAL = "partial"
    FAILED = "failed"


class RunOutcome(StrEnum):
    OK = "OK"
    NO_MATCH = "NO_MATCH"
    INSUFFICIENT_PROFILE = "INSUFFICIENT_PROFILE"
    NOT_A_CV = "NOT_A_CV"


class ErrorCode(StrEnum):
    EXTRACTION_FAILED = "EXTRACTION_FAILED"
    PII_REMOVAL_FAILED = "PII_REMOVAL_FAILED"
    LLM_UNAVAILABLE = "LLM_UNAVAILABLE"
    JOB_MATCH_CONTEXT_FULL = "JOB_MATCH_CONTEXT_FULL"
    RUN_BUDGET_EXCEEDED = "RUN_BUDGET_EXCEEDED"
    RUN_TIMEOUT = "RUN_TIMEOUT"
    CORE_UNAVAILABLE = "CORE_UNAVAILABLE"
    SERVICE_RESTARTED = "SERVICE_RESTARTED"
    INTERNAL_ERROR = "INTERNAL_ERROR"


class WarningCode(StrEnum):
    INDEX_UNAVAILABLE = "INDEX_UNAVAILABLE"
    INDEX_STALE = "INDEX_STALE"
    RERANKER_UNAVAILABLE = "RERANKER_UNAVAILABLE"
    SKILL_MATCH_FALLBACK = "SKILL_MATCH_FALLBACK"
    ASSESSMENT_FALLBACK = "ASSESSMENT_FALLBACK"
    JOBS_UNVERIFIED = "JOBS_UNVERIFIED"
    SEARCH_STOPPED_EARLY = "SEARCH_STOPPED_EARLY"
    HOURS_UNKNOWN = "HOURS_UNKNOWN"


class MatchCriteria(BaseModel):
    salary_type: SalaryTypeFilter | None = Field(default=None, alias="salaryType")
    min_budget: float | None = Field(default=None, alias="minBudget", ge=0)
    max_budget: float | None = Field(default=None, alias="maxBudget", ge=0)
    experience_level: ExperienceLevelFilter | None = Field(default=None, alias="experienceLevel")
    hours_per_day: HoursPerDayFilter | None = Field(default=None, alias="hoursPerDay")
    limit: int = Field(default=10, ge=1, le=20)
    lang: str = Field(default="vi")

    model_config = {
        "populate_by_name": True,
        "extra": "ignore",
    }

    @model_validator(mode="after")
    def validate_budget_bounds(self) -> "MatchCriteria":
        if (
            self.min_budget is not None
            and self.max_budget is not None
            and self.min_budget > self.max_budget
        ):
            raise AppError(
                status_code=422,
                message=f"Validation error: minBudget ({self.min_budget}) cannot exceed maxBudget ({self.max_budget}).",
                error_code="VALIDATION_ERROR",
            )
        return self


class MatchedSkill(BaseModel):
    name: str
    inferred: bool = False


class RequirementCheckItem(BaseModel):
    text: str
    status: Literal["met", "not_met", "unclear"]
    note: str = ""


class JobMatchJobItem(BaseModel):
    job_id: str = Field(alias="jobId")
    title: str
    match_score: int = Field(alias="matchScore")
    matched_skills: list[MatchedSkill] = Field(default_factory=list, alias="matchedSkills")
    missing_skills: list[str] = Field(default_factory=list, alias="missingSkills")
    requirements: list[RequirementCheckItem] = Field(default_factory=list)
    summary: str = ""
    assessment: Literal["llm", "rules"] = "llm"
    budget_min: float | None = Field(default=None, alias="budgetMin")
    budget_max: float | None = Field(default=None, alias="budgetMax")
    salary_type: str | None = Field(default=None, alias="salaryType")

    model_config = {"populate_by_name": True}

    def __getitem__(self, key: str) -> Any:
        if hasattr(self, key):
            return getattr(self, key)
        for field_name, field_info in self.model_fields.items():
            if field_info.alias == key:
                return getattr(self, field_name)
        raise KeyError(key)


class JobMatchProjectItem(BaseModel):
    rank: int
    project_id: str = Field(alias="projectId")
    project_title: str = Field(alias="projectTitle")
    match_score: int = Field(alias="matchScore")
    verified: bool = True
    jobs: list[JobMatchJobItem] = Field(default_factory=list)

    model_config = {"populate_by_name": True}

    def __getitem__(self, key: str) -> Any:
        if hasattr(self, key):
            return getattr(self, key)
        for field_name, field_info in self.model_fields.items():
            if field_info.alias == key:
                return getattr(self, field_name)
        raise KeyError(key)


class JobMatchWarning(BaseModel):
    code: str
    message: str

    def __getitem__(self, key: str) -> Any:
        if hasattr(self, key):
            return getattr(self, key)
        raise KeyError(key)


class JobMatchRunDetail(BaseModel):
    run_id: str = Field(alias="runId")
    status: RunStatus
    stage: str
    outcome: RunOutcome | None = None
    stop_reason: str | None = Field(default=None, alias="stopReason")
    error_code: ErrorCode | None = Field(default=None, alias="errorCode")
    message: str | None = None
    warnings: list[JobMatchWarning] = Field(default_factory=list)
    criteria: dict[str, Any] | None = None
    top_missing_skills: list[str] = Field(default_factory=list, alias="topMissingSkills")
    items: list[JobMatchProjectItem] = Field(default_factory=list)

    model_config = {"populate_by_name": True}


class JobMatchRunAccepted(BaseModel):
    run_id: str = Field(alias="runId")
    status: str = "queued"

    model_config = {"populate_by_name": True}
