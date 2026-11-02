from decimal import Decimal
from typing import Any

from app.features.job_match.ports import IndexRow
from app.privacy.gate import clean


def _clean_field(text: str | None, default: str = "") -> str:
    if not text:
        return default
    try:
        cleaned, _ = clean(str(text), source="project", is_file=False)
        return cleaned.strip()
    except Exception:
        return default


DOC_TEXT_VERSION = "v1"


def sanitize_project(project: dict[str, Any]) -> list[IndexRow]:
    """
    Cleans free-text fields of a project individually using privacy.gate.clean.
    Numbers, IDs and enums are never passed through the gate.
    Returns one IndexRow per job.
    """
    proj_id = str(project.get("id") or "")
    proj_title = _clean_field(project.get("title"), default="")
    proj_desc = _clean_field(project.get("description"), default="")
    proj_status = str(project.get("status") or "OPEN")
    period = project.get("period")
    exp_level = project.get("experienceLevel") or project.get("experience_level")
    hpd = project.get("hoursPerDay") or project.get("hours_per_day")
    hours_per_day = float(hpd) if hpd is not None else None

    raw_jobs = project.get("jobs", [])
    rows: list[IndexRow] = []

    for job in raw_jobs:
        job_id = str(job.get("id") or "")
        job_title = _clean_field(job.get("title"), default="")
        job_desc = _clean_field(job.get("description"), default="")
        job_status = str(job.get("status") or "RECRUITING")
        salary_type = job.get("salaryType") or job.get("salary_type")

        b_min = job.get("budgetMin") or job.get("budget_min")
        b_max = job.get("budgetMax") or job.get("budget_max")
        budget_min = Decimal(str(b_min)) if b_min is not None else None
        budget_max = Decimal(str(b_max)) if b_max is not None else None

        # Clean each skill individually. A field that fails is dropped.
        raw_skills = job.get("skills", [])
        cleaned_skills: list[str] = []
        for s in raw_skills:
            if not s:
                continue
            try:
                c_skill, _ = clean(str(s), source="project", is_file=False)
                c_skill = c_skill.strip()
                if c_skill:
                    cleaned_skills.append(c_skill)
            except Exception:
                pass

        # Clean each requirement individually. An emptied requirement keeps its slot ("") for numbering.
        raw_reqs = job.get("requirements", [])
        cleaned_reqs: list[str] = []
        for r in raw_reqs:
            if not r:
                cleaned_reqs.append("")
                continue
            try:
                c_req, _ = clean(str(r), source="project", is_file=False)
                cleaned_reqs.append(c_req.strip())
            except Exception:
                cleaned_reqs.append("")

        doc_parts = [
            proj_title,
            proj_desc,
            job_title,
            job_desc,
            " ".join(cleaned_skills),
            " ".join(r for r in cleaned_reqs if r),
        ]
        doc_text = " ".join(p for p in doc_parts if p)

        rows.append(
            IndexRow(
                job_id=job_id,
                project_id=proj_id,
                project_title=proj_title,
                project_description=proj_desc,
                job_title=job_title,
                job_description=job_desc,
                skills=cleaned_skills,
                requirements=cleaned_reqs,
                salary_type=str(salary_type) if salary_type else None,
                budget_min=budget_min,
                budget_max=budget_max,
                experience_level=str(exp_level) if exp_level else None,
                period=str(period) if period else None,
                hours_per_day=hours_per_day,
                project_status=proj_status,
                job_status=job_status,
                doc_text=doc_text,
            )
        )

    return rows
