import pytest
from pydantic import ValidationError

from app.features.cv_generator.schemas import GenerateCvInput
from tests.unit.cv_generator.helpers import handoff_examples, sample_payload


def test_handed_off_examples_are_accepted():
    for payload in handoff_examples():
        assert GenerateCvInput.model_validate(payload).model_dump() == payload


@pytest.mark.parametrize(
    "change",
    [
        "unknown",
        "role_string",
        "duplicate_roles",
        "invalid_month",
        "reversed_dates",
        "current_with_end",
        "boolean_team",
        "missing_nullable",
        "blank_bullet",
        "oversize",
    ],
)
def test_rejects_invalid_contract_input(change):
    payload = sample_payload()
    experience = payload["cv"]["experience"][0]
    if change == "unknown":
        payload["user_id"] = "someone-else"
    elif change == "role_string":
        experience["roles"] = "Backend Developer"
    elif change == "duplicate_roles":
        experience["roles"] = ["Dev", "Dev"]
    elif change == "invalid_month":
        experience["start_date"] = "2024-13"
    elif change == "reversed_dates":
        experience.update(start_date="2026", end_date="2025")
    elif change == "current_with_end":
        experience["is_current"] = True
    elif change == "boolean_team":
        experience["team_size"] = True
    elif change == "missing_nullable":
        del experience["location"]
    elif change == "blank_bullet":
        experience["bullets"] = [" "]
    else:
        payload["cv"]["summary"] = "x" * 2001
    with pytest.raises(ValidationError):
        GenerateCvInput.model_validate(payload)


def test_partial_year_dates_are_not_fabricated_or_falsely_rejected():
    payload = sample_payload()
    payload["cv"]["experience"][0].update(start_date="2024-10", end_date="2024")
    model = GenerateCvInput.model_validate(payload)
    assert model.cv.experience[0].end_date == "2024"


def test_placeholder_only_document_is_rejected():
    payload = sample_payload()
    payload["cv"].update(summary=None, headline=None, skill_groups=[], experience=[])
    with pytest.raises(ValidationError):
        GenerateCvInput.model_validate(payload)
