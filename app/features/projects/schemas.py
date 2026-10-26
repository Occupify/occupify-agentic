from enum import StrEnum

from pydantic import BaseModel, Field


class ProjectStatus(StrEnum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"


class ProjectPeriod(StrEnum):
    FIXED = "FIXED"
    HOURLY = "HOURLY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"


class ExperienceLevel(StrEnum):
    ENTRY = "ENTRY"
    INTERMEDIATE = "INTERMEDIATE"
    EXPERT = "EXPERT"


class ProjectFilterParams(BaseModel):
    """Parameters for searching and filtering projects on Occupify."""

    keyword: str | None = Field(
        default=None,
        description="Optional search keyword matching title and description.",
    )
    status: ProjectStatus | None = Field(
        default=None,
        description="Optional status filter (OPEN, CLOSED).",
    )
    employer_id: str | None = Field(
        default=None,
        description="Optional UUID of the employer.",
    )
    period: ProjectPeriod | None = Field(
        default=None,
        description="Optional period (FIXED, HOURLY, WEEKLY, MONTHLY).",
    )
    experience_level: ExperienceLevel | None = Field(
        default=None,
        description="Optional level (ENTRY, INTERMEDIATE, EXPERT).",
    )
    min_price: float | None = Field(
        default=None,
        ge=0,
        description="Optional minimum starting price.",
    )
    max_price: float | None = Field(
        default=None,
        ge=0,
        description="Optional maximum starting price.",
    )
    page: int = Field(
        default=0,
        ge=0,
        description="Zero-based page index (default 0).",
    )
    size: int = Field(
        default=20,
        ge=1,
        le=50,
        description="Page size (default 20, max 50).",
    )
    sort: str = Field(
        default="createdAt,desc",
        description="Sort expression (e.g. 'createdAt,desc', 'startPrice,asc').",
    )


class ProjectGetParams(BaseModel):
    """Parameters for retrieving project details."""

    project_id: str = Field(
        description="The UUID of the project to retrieve.",
    )
