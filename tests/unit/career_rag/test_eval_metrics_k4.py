import pytest

from evals.uc1.metrics_k4 import (
    calculate_checkpoint_recovery_rate,
    calculate_compaction_retention,
    calculate_fact_accuracy,
    calculate_precedence_accuracy,
    calculate_tenant_leak_rate,
)


def test_fact_accuracy_perfect():
    expected = [
        {"category": "career", "key": "target_role", "value": "Senior Cloud Architect"},
        {"category": "career", "key": "years_experience", "value": 5},
        {"category": "skills", "key": "primary_skills", "value": ["Python", "FastAPI"]},
    ]
    recorded = [
        {"category": "career", "key": "target_role", "value": "Senior Cloud Architect"},
        {"category": "career", "key": "years_experience", "value": 5},
        {"category": "skills", "key": "primary_skills", "value": ["FastAPI", "Python"]},
    ]

    res = calculate_fact_accuracy(expected, recorded)
    assert res["precision"] == 1.0
    assert res["recall"] == 1.0
    assert res["f1"] == 1.0


def test_fact_accuracy_partial_and_mismatch():
    expected = [
        {"category": "career", "key": "target_role", "value": "Senior DevOps"},
        {"category": "career", "key": "years_experience", "value": 5},
    ]
    # Recorded has 1 correct, 1 wrong value, and 1 extra unexpected item
    recorded = [
        {"category": "career", "key": "target_role", "value": "Senior DevOps"},
        {"category": "career", "key": "years_experience", "value": 10},  # mismatch
        {"category": "general", "key": "extra", "value": "val"},
    ]

    res = calculate_fact_accuracy(expected, recorded)
    # 1 TP out of 3 recorded -> precision = 1/3 = 0.3333
    # 1 TP out of 2 expected -> recall = 1/2 = 0.5
    assert res["precision"] == pytest.approx(1 / 3, abs=1e-3)
    assert res["recall"] == 0.5
    assert res["f1"] == pytest.approx(0.4, abs=1e-3)


def test_fact_accuracy_edge_cases():
    assert calculate_fact_accuracy([], []) == {"precision": 1.0, "recall": 1.0, "f1": 1.0}
    assert calculate_fact_accuracy([], [{"category": "c", "key": "k"}]) == {
        "precision": 0.0,
        "recall": 1.0,
        "f1": 0.0,
    }
    assert calculate_fact_accuracy([{"category": "c", "key": "k"}], []) == {
        "precision": 1.0,
        "recall": 0.0,
        "f1": 0.0,
    }


def test_precedence_accuracy():
    assert calculate_precedence_accuracy([True, True, True]) == 1.0
    assert calculate_precedence_accuracy([True, False]) == 0.5
    assert calculate_precedence_accuracy([False, False]) == 0.0
    assert calculate_precedence_accuracy([]) == 1.0


def test_checkpoint_recovery_rate():
    # Both stage and pending match
    assert (
        calculate_checkpoint_recovery_rate(
            expected_stage="ASSESSMENT", recovered_stage="ASSESSMENT", pending_match=True
        )
        == 1.0
    )

    # Stage matches, pending differs
    assert (
        calculate_checkpoint_recovery_rate(
            expected_stage="ASSESSMENT", recovered_stage="ASSESSMENT", pending_match=False
        )
        == 0.5
    )

    # Stage differs, pending matches
    assert (
        calculate_checkpoint_recovery_rate(
            expected_stage="ASSESSMENT", recovered_stage="DISCOVERY", pending_match=True
        )
        == 0.5
    )

    # Neither matches
    assert (
        calculate_checkpoint_recovery_rate(
            expected_stage="ASSESSMENT", recovered_stage="DISCOVERY", pending_match=False
        )
        == 0.0
    )


def test_compaction_retention():
    sample_compacted_card = """
<COMPACTED_SESSION_STATE task_type="career_consulting" stage="ROADMAP_FORMULATION" checkpoint_seq="4">
1. ORIGINAL GOAL: Transition from QA Automation to SDET
2. CONFIRMED PROFILE FACTS: Python; Selenium; Pytest
3. CONSTRAINTS & PREFERENCES: 100% remote roles
4. DECISIONS MADE & RATIONALE: Focus on Playwright and Distributed Systems
5. COMPLETED WORK & ANALYSIS: Analyzed test automation gaps
6. CURRENT STAGE & PROGRESS: ROADMAP_FORMULATION (Pending: [Draft study schedule])
7. OPEN QUESTIONS & BLOCKERS: None
8. NEXT RECOMMENDED ACTION: Finalize 12-week study timetable
9. EVIDENCE & HISTORY POINTERS: Full raw turns archived (count: 14)
</COMPACTED_SESSION_STATE>
"""
    res = calculate_compaction_retention(sample_compacted_card)
    assert res["fields_checked"] == 9
    assert res["fields_present"] == 9
    assert res["retention_rate"] == 1.0
    assert len(res["missing_fields"]) == 0

    # Partial card missing DECISIONS MADE & RATIONALE and NEXT RECOMMENDED ACTION
    partial_card = """
1. ORIGINAL GOAL: Transition to DevOps
2. CONFIRMED PROFILE FACTS: Linux
3. CONSTRAINTS & PREFERENCES: None
5. COMPLETED WORK & ANALYSIS: None
6. CURRENT STAGE & PROGRESS: DISCOVERY
7. OPEN QUESTIONS & BLOCKERS: None
9. EVIDENCE & HISTORY POINTERS: Archived
"""
    res_partial = calculate_compaction_retention(partial_card)
    assert res_partial["fields_present"] == 7
    assert res_partial["retention_rate"] == pytest.approx(7 / 9, abs=1e-3)
    assert "DECISIONS MADE & RATIONALE" in res_partial["missing_fields"]
    assert "NEXT RECOMMENDED ACTION" in res_partial["missing_fields"]

    # Empty card
    res_empty = calculate_compaction_retention("")
    assert res_empty["fields_present"] == 0
    assert res_empty["retention_rate"] == 0.0
    assert len(res_empty["missing_fields"]) == 9


def test_tenant_leak_rate():
    user_a_facts = [
        {"category": "career", "key": "confidential_employer", "value": "StealthStartupCo"},
        {"category": "preferences", "key": "current_compensation", "value": "$195,000"},
    ]

    # Clean user B context: zero overlap
    user_b_clean = [
        {"category": "career", "key": "target_role", "value": "Frontend Engineer"},
        {"category": "skills", "key": "primary_skills", "value": ["React", "TypeScript"]},
    ]
    assert calculate_tenant_leak_rate(user_a_facts, user_b_clean) == 0.0

    # Leaked user B context: User A's confidential employer is leaked
    user_b_leaked = [
        {"category": "career", "key": "target_role", "value": "Frontend Engineer"},
        {"category": "career", "key": "confidential_employer", "value": "StealthStartupCo"},
    ]
    leak_rate = calculate_tenant_leak_rate(user_a_facts, user_b_leaked)
    assert leak_rate > 0.0
    assert leak_rate == 0.5  # 1 out of 2 leaked
