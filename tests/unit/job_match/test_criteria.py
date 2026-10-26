from decimal import Decimal

import pytest
from app.features.job_match.criteria import matches

from app.features.job_match.ports import IndexRow, MatchCriteria
from app.features.job_match.schemas import (
    ExperienceLevelFilter,
    HoursPerDayFilter,
    SalaryTypeFilter,
)


def make_row(
    salary_type: str | None = "MONTHLY",
    budget_min: float | None = 25000000,
    budget_max: float | None = 40000000,
    experience_level: str | None = "INTERMEDIATE",
    hours_per_day: float | None = 8.0,
) -> IndexRow:
    return IndexRow(
        job_id="j01",
        project_id="p01",
        project_title="Title",
        project_description="Desc",
        job_title="Job",
        job_description="Desc",
        skills=["Python"],
        requirements=["Req"],
        salary_type=salary_type,
        budget_min=Decimal(str(budget_min)) if budget_min is not None else None,
        budget_max=Decimal(str(budget_max)) if budget_max is not None else None,
        experience_level=experience_level,
        period="MONTHLY",
        hours_per_day=hours_per_day,
        project_status="OPEN",
        job_status="RECRUITING",
        doc_text="Doc text",
    )


@pytest.mark.parametrize(
    "criteria,row,expected",
    [
        # salaryType exact match
        (
            MatchCriteria(salary_type=SalaryTypeFilter.MONTHLY),
            make_row(salary_type="MONTHLY"),
            True,
        ),
        (
            MatchCriteria(salary_type=SalaryTypeFilter.MONTHLY),
            make_row(salary_type="HOURLY"),
            False,
        ),
        (MatchCriteria(salary_type=SalaryTypeFilter.HOURLY), make_row(salary_type=None), False),
        # budget overlap: min_budget
        # min -> budgetMax >= min OR budgetMin >= min
        (
            MatchCriteria(min_budget=30000000),
            make_row(budget_min=25000000, budget_max=40000000),
            True,
        ),
        (
            MatchCriteria(min_budget=45000000),
            make_row(budget_min=25000000, budget_max=40000000),
            False,
        ),
        (
            MatchCriteria(min_budget=20000000),
            make_row(budget_min=25000000, budget_max=40000000),
            True,
        ),
        (MatchCriteria(min_budget=30000000), make_row(budget_min=None, budget_max=None), False),
        # budget overlap: max_budget
        # max -> budgetMin <= max OR budgetMax <= max
        (
            MatchCriteria(max_budget=30000000),
            make_row(budget_min=25000000, budget_max=40000000),
            True,
        ),
        (
            MatchCriteria(max_budget=20000000),
            make_row(budget_min=25000000, budget_max=40000000),
            False,
        ),
        (
            MatchCriteria(max_budget=50000000),
            make_row(budget_min=25000000, budget_max=40000000),
            True,
        ),
        (MatchCriteria(max_budget=30000000), make_row(budget_min=None, budget_max=None), False),
        # experienceLevel exact match
        (
            MatchCriteria(experience_level=ExperienceLevelFilter.EXPERT),
            make_row(experience_level="EXPERT"),
            True,
        ),
        (
            MatchCriteria(experience_level=ExperienceLevelFilter.EXPERT),
            make_row(experience_level="ENTRY"),
            False,
        ),
        # hoursPerDay: under-4h (h < 4)
        (
            MatchCriteria(hours_per_day=HoursPerDayFilter.UNDER_FOUR),
            make_row(hours_per_day=3.0),
            True,
        ),
        (
            MatchCriteria(hours_per_day=HoursPerDayFilter.UNDER_FOUR),
            make_row(hours_per_day=4.0),
            False,
        ),
        # hoursPerDay: 4h-8h (4 <= h <= 8)
        (
            MatchCriteria(hours_per_day=HoursPerDayFilter.FOUR_TO_EIGHT),
            make_row(hours_per_day=4.0),
            True,
        ),
        (
            MatchCriteria(hours_per_day=HoursPerDayFilter.FOUR_TO_EIGHT),
            make_row(hours_per_day=8.0),
            True,
        ),
        (
            MatchCriteria(hours_per_day=HoursPerDayFilter.FOUR_TO_EIGHT),
            make_row(hours_per_day=2.0),
            False,
        ),
        (
            MatchCriteria(hours_per_day=HoursPerDayFilter.FOUR_TO_EIGHT),
            make_row(hours_per_day=9.0),
            False,
        ),
        # hoursPerDay: above-8h (h > 8)
        (
            MatchCriteria(hours_per_day=HoursPerDayFilter.ABOVE_EIGHT),
            make_row(hours_per_day=9.0),
            True,
        ),
        (
            MatchCriteria(hours_per_day=HoursPerDayFilter.ABOVE_EIGHT),
            make_row(hours_per_day=8.0),
            False,
        ),
        # hoursPerDay null passes
        (
            MatchCriteria(hours_per_day=HoursPerDayFilter.FOUR_TO_EIGHT),
            make_row(hours_per_day=None),
            True,
        ),
    ],
)
def test_matches_table(criteria: MatchCriteria, row: IndexRow, expected: bool):
    assert matches(criteria, row) is expected
