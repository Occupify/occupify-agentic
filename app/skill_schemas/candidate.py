from typing import Literal

from pydantic import BaseModel, ConfigDict


class SkillItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    source: Literal["stated", "inferred"]
    from_section: str | None = None


class RoleItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    start: str | None = None
    end: str | None = None
    skills_used: list[str] = []
    summary: str | None = None


class CandidateProfile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: str = "ok"
    language: str = "en"
    skills: list[SkillItem | str] = []
    roles: list[RoleItem] = []
    domains: list[str] = []
    target_roles: list[str] = []
    experience_level: Literal["ENTRY", "INTERMEDIATE", "EXPERT"] | None = None
    experience_level_reason: str | None = None
    total_years: float | None = None
