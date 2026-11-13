"""The handed-off CV input contract and sanitized tool responses."""

import calendar
import re
from datetime import datetime
from typing import Annotated, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

Text = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=2000)]
Texts = Annotated[list[Text], Field(max_length=30)]
Bullets = Annotated[list[Text], Field(min_length=1, max_length=30)]
TeamSize = Annotated[int, Field(gt=0)]


def date_interval(value: str) -> tuple[tuple[int, int], tuple[int, int]]:
    if not re.fullmatch(r"\d{4}(?:-\d{2})?", value):
        raise ValueError("Date must use YYYY or YYYY-MM")
    year = int(value[:4])
    month = int(value[5:]) if len(value) == 7 else None
    if year < 1 or (month is not None and not 1 <= month <= 12):
        raise ValueError("Invalid calendar date")
    return (year, month or 1), (year, month or 12)


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    @model_validator(mode="after")
    def check_dates(self) -> Self:
        for key in ("start_date", "end_date", "issued_date", "expiry_date"):
            value = getattr(self, key, None)
            if value is not None:
                date_interval(value)
        for start_key, end_key in (("start_date", "end_date"), ("issued_date", "expiry_date")):
            start, end = getattr(self, start_key, None), getattr(self, end_key, None)
            if start and end and date_interval(start)[0] > date_interval(end)[1]:
                raise ValueError("Date interval is reversed")
        return self


class SkillGroup(StrictModel):
    label: Text
    items: Bullets


class WorkEntry(StrictModel):
    roles: Texts
    start_date: Text | None
    end_date: Text | None
    is_current: bool
    team_size: TeamSize | None
    bullets: Bullets

    @model_validator(mode="after")
    def check_work(self) -> Self:
        if len(self.roles) != len(set(role.casefold() for role in self.roles)):
            raise ValueError("Roles must be unique")
        if self.is_current and self.end_date is not None:
            raise ValueError("Current work cannot have an end date")
        return self


class Experience(WorkEntry):
    company: Text
    employment_type: Text | None
    location: Text | None


class Project(WorkEntry):
    name: Text
    technologies: Texts


class Education(StrictModel):
    institution: Text
    degree: Text | None
    major: Text | None
    location: Text | None
    start_date: Text | None
    end_date: Text | None
    is_current: bool
    is_expected: bool
    gpa: Text | None
    highlights: Texts

    @model_validator(mode="after")
    def check_expected(self) -> Self:
        if self.is_expected and (not self.is_current or self.end_date is None):
            raise ValueError("Expected graduation requires current education and an end date")
        if self.is_current and self.end_date and not self.is_expected:
            raise ValueError("Current education end date must be expected")
        return self


class Certification(StrictModel):
    name: Text
    issuer: Text | None
    issued_date: Text | None
    expiry_date: Text | None
    result: Text | None


class AdditionalItem(StrictModel):
    label: Text | None
    text: Text


class AdditionalSection(StrictModel):
    title: Text
    items: Annotated[list[AdditionalItem], Field(min_length=1, max_length=30)]


class CvContent(StrictModel):
    headline: Text | None
    summary: Text | None
    skill_groups: Annotated[list[SkillGroup], Field(max_length=10)]
    experience: Annotated[list[Experience], Field(max_length=30)]
    projects: Annotated[list[Project], Field(max_length=30)]
    education: Annotated[list[Education], Field(max_length=30)]
    certifications: Annotated[list[Certification], Field(max_length=30)]
    additional_sections: Annotated[list[AdditionalSection], Field(max_length=10)]

    @model_validator(mode="after")
    def require_content(self) -> Self:
        if not any(
            (
                self.skill_groups,
                self.experience,
                self.projects,
                self.education,
                self.certifications,
                self.additional_sections,
            )
        ):
            raise ValueError("At least one substantive CV section is required")
        return self


class GenerateCvInput(StrictModel):
    template_id: Literal["classic"]
    language: Literal["vi", "en"]
    cv: CvContent

    @model_validator(mode="after")
    def check_size(self) -> Self:
        data = self.model_dump()
        lengths, objects = 0, 0

        def visit(value):
            nonlocal lengths, objects
            if isinstance(value, str):
                lengths += len(value)
                if any(ord(c) < 32 and c not in "\n\t" for c in value):
                    raise ValueError("Control characters are not supported")
            elif isinstance(value, dict):
                objects += 1
                for item in value.values():
                    visit(item)
            elif isinstance(value, list):
                for item in value:
                    visit(item)

        visit(data)
        if lengths > 40_000 or objects > 200 or len(self.model_dump_json().encode()) > 131_072:
            raise ValueError("CV payload is too large")
        return self


class CvGenerationError(Exception):
    """Only safe codes/messages cross the tool boundary, never raw underlying exceptions."""

    def __init__(self, code: str, message: str | None = None, retryable: bool = False):
        self.code = code
        self.retryable = retryable
        super().__init__(message or code.replace("_", " ").capitalize())


class ArtifactFile(BaseModel):
    format: Literal["tex", "pdf"]
    filename: str
    content_type: str
    download_url: str
    expires_at: datetime


class ToolError(BaseModel):
    code: str
    message: str
    retryable: bool = False
    fields: list[str] = Field(default_factory=list)


class GenerateCvResult(BaseModel):
    status: Literal["succeeded", "failed"]
    artifact_id: str | None = None
    page_count: int | None = None
    compiler: Literal["xelatex"] | None = None
    files: list[ArtifactFile] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    error: ToolError | None = None

    @classmethod
    def failure(cls, error: CvGenerationError) -> Self:
        return cls(
            status="failed",
            error=ToolError(code=error.code, message=str(error), retryable=error.retryable),
        )


def display_date(value: str | None, language: str) -> str:
    if not value:
        return ""
    if len(value) == 4:
        return value
    year, month = value.split("-")
    return f"{month}/{year}" if language == "vi" else f"{calendar.month_abbr[int(month)]} {year}"
