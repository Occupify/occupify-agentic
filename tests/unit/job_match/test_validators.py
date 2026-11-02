import pytest

from app.features.job_match.ports import MatchCriteria
from app.features.job_match.schemas import SalaryTypeFilter
from app.features.job_match.validators import (
    clean_output_pii,
    validate_assessment_with_retry,
    validate_v3_criteria,
)
from app.skill_schemas.matching import ProjectAssessment, RequirementCheck
from tests.unit.job_match.scripts import raw_invalid


def test_v3_drops_items_failing_criteria():
    criteria = MatchCriteria(salary_type=SalaryTypeFilter.HOURLY)
    items = [
        {
            "project_id": "p1",
            "jobs": [
                {"job_id": "j1", "salary_type": "HOURLY"},
                {"job_id": "j2", "salary_type": "MONTHLY"},
            ],
        },
        {
            "project_id": "p2",
            "jobs": [
                {"job_id": "j3", "salary_type": "MONTHLY"},
            ],
        },
    ]

    filtered = validate_v3_criteria(items, criteria)
    assert len(filtered) == 1
    assert filtered[0]["project_id"] == "p1"
    assert len(filtered[0]["jobs"]) == 1
    assert filtered[0]["jobs"][0]["job_id"] == "j1"


def test_unknown_refs_dropped():
    from app.features.job_match.validators import validate_and_filter_assessment

    raw_assessment = ProjectAssessment(
        job_assessments={
            "j1": {
                "requirements": [
                    RequirementCheck(req_id="J1.R1", status="met", note="OK"),
                    RequirementCheck(req_id="J99.R99", status="met", note="Fake ref"),
                ],
                "summary": "Fit summary",
            }
        }
    )
    valid_req_ids = {"j1": {"J1.R1"}}

    cleaned = validate_and_filter_assessment(raw_assessment, valid_req_ids)
    j1_reqs = cleaned.job_assessments["j1"].requirements
    assert len(j1_reqs) == 1
    assert j1_reqs[0].req_id == "J1.R1"


@pytest.mark.asyncio
async def test_assessment_retry_then_rules_fallback():
    # Model that continuously emits invalid JSON/schema
    invalid_model = raw_invalid("Totally invalid non-JSON output")

    assessment, warnings = await validate_assessment_with_retry(
        project_id="p1",
        project_jobs={"j1": ["3+ years Java", "Docker"]},
        model=invalid_model,
        lang="vi",
    )

    assert "ASSESSMENT_FALLBACK" in warnings
    assert assessment["j1"]["assessment"] == "rules"
    assert "summary" in assessment["j1"]
    assert len(assessment["j1"]["requirements"]) == 2


def test_output_pii_dropped():
    text_with_sentinel = (
        "Candidate sentinel.candidate@example.com phone 0912 000 111 is recommended."
    )
    cleaned = clean_output_pii(text_with_sentinel)
    assert "sentinel.candidate@example.com" not in cleaned
    assert "0912 000 111" not in cleaned


def test_emptied_requirement_is_unclear():
    from app.features.job_match.validators import enforce_emptied_requirements_unclear

    requirements_input = [
        {"id": "J1.R1", "text": "Valid requirement"},
        {"id": "J1.R2", "text": ""},  # Emptied by sanitise
    ]
    checks = [
        RequirementCheck(req_id="J1.R1", status="met", note="Has experience"),
        RequirementCheck(req_id="J1.R2", status="met", note="Claimed met"),
    ]

    enforced = enforce_emptied_requirements_unclear(checks, requirements_input)
    assert enforced[0].status == "met"
    assert enforced[1].status == "unclear"
    assert "sanitized" in enforced[1].note.lower() or "unclear" in enforced[1].note.lower()
