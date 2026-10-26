from typing import Literal

from pydantic import BaseModel, ConfigDict


class RequirementCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ref: str
    status: Literal["met", "not_met", "unclear"]
    note: str


class JobAssessment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job: str
    requirements: list[RequirementCheck]
    summary: str


class ProjectAssessment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jobs: list[JobAssessment]


class SkillVerdict(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ref: str
    verdict: Literal["exact", "equivalent", "implied", "inferred", "missing"]
    cv_skill: str | None = None


class JobSkillVerdict(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job_skill: str
    verdict: Literal["exact", "equivalent", "implied", "inferred", "missing"]
    cv_skill: str | None = None


class SkillMatchResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    verdicts: list[SkillVerdict] = []
    job_verdicts: dict[str, list[JobSkillVerdict]] = {}
