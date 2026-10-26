import pytest
from pydantic import ValidationError

from app.core.errors import AppError
from app.features.job_match.schemas import (
    ExperienceLevelFilter,
    HoursPerDayFilter,
    MatchCriteria,
    SalaryTypeFilter,
)


def test_match_criteria_validation():
    # 1. Valid defaults and fields
    c = MatchCriteria(
        salary_type=SalaryTypeFilter.MONTHLY,
        min_budget=10000000,
        max_budget=20000000,
        experience_level=ExperienceLevelFilter.INTERMEDIATE,
        hours_per_day=HoursPerDayFilter.FOUR_TO_EIGHT,
        limit=10,
        lang="vi",
    )
    assert c.limit == 10
    assert c.lang == "vi"

    # 2. Limit range check (1 to 20)
    with pytest.raises((ValidationError, AppError)):
        MatchCriteria(limit=0)

    with pytest.raises((ValidationError, AppError)):
        MatchCriteria(limit=25)

    # 3. min_budget > max_budget check must raise validation error (AppError 422 or ValidationError)
    with pytest.raises((ValidationError, AppError)):
        MatchCriteria(min_budget=50000000, max_budget=20000000)

    # 4. Enums
    with pytest.raises((ValidationError, ValueError)):
        MatchCriteria(salary_type="INVALID_SALARY")

    with pytest.raises((ValidationError, ValueError)):
        MatchCriteria(hours_per_day="invalid-hours")
