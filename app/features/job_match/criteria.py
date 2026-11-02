from typing import Any

from app.features.job_match.ports import IndexRow
from app.features.job_match.schemas import (
    HoursPerDayFilter,
    MatchCriteria,
)


def matches(criteria: MatchCriteria, row: IndexRow | dict[str, Any]) -> bool:
    """Evaluates whether an IndexRow or job dict matches the user's MatchCriteria."""
    # Extract fields from IndexRow or dict
    if isinstance(row, dict):
        salary_type = row.get("salary_type") or row.get("salaryType")
        b_min = row.get("budget_min") or row.get("budgetMin")
        b_max = row.get("budget_max") or row.get("budgetMax")
        exp_level = row.get("experience_level") or row.get("experienceLevel")
        hpd = row.get("hours_per_day") or row.get("hoursPerDay")
    else:
        salary_type = row.salary_type
        b_min = row.budget_min
        b_max = row.budget_max
        exp_level = row.experience_level
        hpd = row.hours_per_day

    # 1. salaryType
    if criteria.salary_type is not None:
        if not salary_type or salary_type != criteria.salary_type.value:
            return False

    # 2. minBudget / maxBudget
    b_min_val = float(b_min) if b_min is not None else None
    b_max_val = float(b_max) if b_max is not None else None

    if criteria.min_budget is not None:
        if b_min_val is None and b_max_val is None:
            return False
        # Overlap min: budgetMax >= min OR budgetMin >= min
        cond1 = b_max_val is not None and b_max_val >= criteria.min_budget
        cond2 = b_min_val is not None and b_min_val >= criteria.min_budget
        if not (cond1 or cond2):
            return False

    if criteria.max_budget is not None:
        if b_min_val is None and b_max_val is None:
            return False
        # Overlap max: budgetMin <= max OR budgetMax <= max
        cond1 = b_min_val is not None and b_min_val <= criteria.max_budget
        cond2 = b_max_val is not None and b_max_val <= criteria.max_budget
        if not (cond1 or cond2):
            return False

    # 3. experienceLevel (project level)
    if criteria.experience_level is not None:
        if not exp_level or exp_level != criteria.experience_level.value:
            return False

    # 4. hoursPerDay: under-4h (h < 4), 4h-8h (4 <= h <= 8), above-8h (h > 8). Null passes!
    if criteria.hours_per_day is not None and hpd is not None:
        val = float(hpd)
        if criteria.hours_per_day == HoursPerDayFilter.UNDER_FOUR:
            if not (val < 4.0):
                return False
        elif criteria.hours_per_day == HoursPerDayFilter.FOUR_TO_EIGHT:
            if not (4.0 <= val <= 8.0):
                return False
        elif criteria.hours_per_day == HoursPerDayFilter.ABOVE_EIGHT:
            if not (val > 8.0):
                return False

    return True
