from pydantic import BaseModel, ConfigDict


class CvSuggestionItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    section: str
    target_original_text: str
    suggested_revised_text: str
    reason: str


class CvImprovementProposal(BaseModel):
    model_config = ConfigDict(extra="forbid")

    target_role: str
    summary: str
    strengths: list[str] = []
    missing_skills: list[str] = []
    suggestions: list[CvSuggestionItem] = []


class ResumeExperienceItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    company: str
    role: str
    period: str
    bullet_points: list[str] = []


class ResumeProjectItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    role: str
    tech_stack: list[str] = []
    bullet_points: list[str] = []


class ResumeEducationItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    institution: str
    degree: str
    period: str


class ResumeAdditionalItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    label: str | None = None
    text: str


class ResumeAdditionalSection(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    items: list[ResumeAdditionalItem] = []


class ResumeCertificationItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    issuer: str | None = None
    issue_date: str | None = None
    expiry_date: str | None = None
    result: str | None = None


class ResumeData(BaseModel):
    model_config = ConfigDict(extra="forbid")

    full_name: str
    title: str
    contact_info: str = ""
    summary: str
    skills: list[str] = []
    experiences: list[ResumeExperienceItem] = []
    projects: list[ResumeProjectItem] = []
    education: list[ResumeEducationItem] = []
    certifications: list[ResumeCertificationItem] = []
    additional_sections: list[ResumeAdditionalSection] = []
