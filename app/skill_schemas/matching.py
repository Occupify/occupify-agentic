from typing import Any, Literal

from pydantic import BaseModel, ConfigDict


class RequirementCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ref: str | None = None
    req_id: str | None = None
    status: Literal["met", "not_met", "unclear"]
    note: str

    def model_post_init(self, __context: Any) -> None:
        if self.ref is None and self.req_id is not None:
            self.ref = self.req_id
        elif self.req_id is None and self.ref is not None:
            self.req_id = self.ref


class JobAssessment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job: str | None = None
    job_id: str | None = None
    requirements: list[RequirementCheck] = []
    summary: str = ""
    assessment: str | None = None

    def model_post_init(self, __context: Any) -> None:
        if self.job is None and self.job_id is not None:
            self.job = self.job_id
        elif self.job_id is None and self.job is not None:
            self.job_id = self.job


class ProjectAssessment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    jobs: list[JobAssessment] = []
    job_assessments: dict[str, JobAssessment] = {}

    def model_post_init(self, __context: Any) -> None:
        if not self.job_assessments and self.jobs:
            for j in self.jobs:
                key = j.job or j.job_id or ""
                self.job_assessments[key] = j
        elif not self.jobs and self.job_assessments:
            for k, v in self.job_assessments.items():
                if not v.job and not v.job_id:
                    v.job = k
                    v.job_id = k
                self.jobs.append(v)


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
