"""K4 Evaluation Metrics Mathematical Engine.

Implements rigorous deterministic evaluation metrics for K4:
Global Memory, State & Context Harness:
- Fact Extraction Precision, Recall, and F1
- Precedence Accuracy (Rule 7: confirmed facts override inferred facts)
- Checkpoint Recovery Rate (Rule 8: stage and pending checklist fidelity post-crash)
- Compaction Retention Rate (Rule 9: preservation of all 9 essential fields)
- Multi-Tenant Leak Rate (Rule 7 & 10: 100% tenant boundary isolation, target: 0.0)
"""

import re
from typing import Any

# Canonical 9 Fields mandated by Rule 9 of doc/rule.md
MANDATORY_COMPACTION_FIELDS = [
    "ORIGINAL GOAL",
    "CONFIRMED PROFILE FACTS",
    "CONSTRAINTS & PREFERENCES",
    "DECISIONS MADE & RATIONALE",
    "COMPLETED WORK & ANALYSIS",
    "CURRENT STAGE & PROGRESS",
    "OPEN QUESTIONS & BLOCKERS",
    "NEXT RECOMMENDED ACTION",
    "EVIDENCE & HISTORY POINTERS",
]


def calculate_fact_accuracy(
    expected_facts: list[dict[str, Any]],
    recorded_facts: list[dict[str, Any]],
) -> dict[str, float]:
    """Calculates Precision, Recall, and F1 score for extracted/recorded memory facts.

    Matches expected items against recorded items based on (category, key) and optionally value.
    Returns:
        dict: {"precision": float, "recall": float, "f1": float}
    """
    if not expected_facts and not recorded_facts:
        return {"precision": 1.0, "recall": 1.0, "f1": 1.0}
    if not expected_facts:
        return {"precision": 0.0, "recall": 1.0, "f1": 0.0}
    if not recorded_facts:
        return {"precision": 1.0, "recall": 0.0, "f1": 0.0}

    def _normalize_val(val: Any) -> Any:
        if isinstance(val, list):
            return sorted(str(v).strip().lower() for v in val)
        return str(val).strip().lower()

    # Build lookup of recorded facts
    recorded_lookup: dict[tuple[str, str], Any] = {}
    for r in recorded_facts:
        cat = str(r.get("category", "")).strip().lower()
        key = str(r.get("key", "")).strip().lower()
        val = _normalize_val(r.get("value"))
        recorded_lookup[(cat, key)] = val

    true_positives = 0
    for exp in expected_facts:
        cat = str(exp.get("category", "")).strip().lower()
        key = str(exp.get("key", "")).strip().lower()
        exp_val = _normalize_val(exp.get("value"))

        if (cat, key) in recorded_lookup:
            rec_val = recorded_lookup[(cat, key)]
            # If expected value is specified, verify value match; otherwise match on key
            if exp_val is None or exp_val == "" or exp_val == rec_val:
                true_positives += 1

    precision = true_positives / len(recorded_facts) if recorded_facts else 0.0
    recall = true_positives / len(expected_facts) if expected_facts else 0.0
    if precision + recall > 0:
        f1 = (2.0 * precision * recall) / (precision + recall)
    else:
        f1 = 0.0

    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def calculate_precedence_accuracy(confirmed_overrides: list[bool]) -> float:
    """Calculates Rule 7 fact precedence accuracy.

    Verifies that explicit user-confirmed updates override inferred facts,
    and subsequent unconfirmed inferences are rejected from downgrading confirmed facts.
    Returns:
        float: Accuracy between 0.0 and 1.0 (1.0 = 100% compliant).
    """
    if not confirmed_overrides:
        return 1.0
    successes = sum(1.0 for passed in confirmed_overrides if passed)
    return round(successes / len(confirmed_overrides), 4)


def calculate_checkpoint_recovery_rate(
    expected_stage: str,
    recovered_stage: str,
    pending_match: bool,
) -> float:
    """Calculates Rule 8 checkpoint recovery rate post-crash.

    Evaluates whether the agent reloads the exact consulting stage and
    resumes from the correct pending checklist items without repeating work.
    Returns:
        float: 1.0 if both stage and pending match, 0.5 if only stage matches, 0.0 otherwise.
    """
    stage_match = str(expected_stage).strip().upper() == str(recovered_stage).strip().upper()
    stage_score = 0.5 if stage_match else 0.0
    pending_score = 0.5 if pending_match else 0.0
    return round(stage_score + pending_score, 4)


def calculate_compaction_retention(compacted_card: str) -> dict[str, Any]:
    """Calculates Rule 9 Context Compaction integrity across all 9 required fields:

    1. Original user goal.
    2. User-confirmed profile facts.
    3. Constraints and preferences.
    4. Decisions already made and rationale.
    5. Completed analysis or actions.
    6. Current task stage and progress.
    7. Open questions, blockers and risks.
    8. The next recommended action.
    9. References to supporting evidence / history pointers.

    Returns:
        dict: Summary containing retention_rate (0.0 to 1.0), missing_fields, field_status.
    """
    if not compacted_card or not isinstance(compacted_card, str):
        return {
            "fields_checked": len(MANDATORY_COMPACTION_FIELDS),
            "fields_present": 0,
            "retention_rate": 0.0,
            "missing_fields": list(MANDATORY_COMPACTION_FIELDS),
            "field_status": {field: False for field in MANDATORY_COMPACTION_FIELDS},
        }

    field_status: dict[str, bool] = {}
    missing_fields: list[str] = []

    for field_name in MANDATORY_COMPACTION_FIELDS:
        # Match case-insensitively with flexible delimiters (e.g. "1. ORIGINAL GOAL" or "ORIGINAL GOAL:")
        pattern = re.compile(rf"\b{re.escape(field_name)}\b", re.IGNORECASE)
        found = bool(pattern.search(compacted_card))
        field_status[field_name] = found
        if not found:
            missing_fields.append(field_name)

    present_count = sum(1 for status in field_status.values() if status)
    total_fields = len(MANDATORY_COMPACTION_FIELDS)
    retention_rate = present_count / total_fields if total_fields > 0 else 0.0

    return {
        "fields_checked": total_fields,
        "fields_present": present_count,
        "retention_rate": round(retention_rate, 4),
        "missing_fields": missing_fields,
        "field_status": field_status,
    }


def calculate_tenant_leak_rate(
    user_a_facts: list[dict[str, Any]],
    user_b_injected: list[dict[str, Any]],
) -> float:
    """Calculates cross-tenant data leakage rate between User A and User B.

    Per Rule 7 and Rule 10, cross-tenant leak rate must be strictly 0.0%.
    Returns:
        float: 0.0 if zero leakage detected, > 0.0 if any User A data leaks into User B.
    """
    if not user_a_facts or not user_b_injected:
        return 0.0

    # Build set of identifiable confidential tokens/keys/values from User A
    user_a_signatures: set[str] = set()
    for fact in user_a_facts:
        key = str(fact.get("key", "")).strip().lower()
        if key:
            user_a_signatures.add(key)
        val = fact.get("value")
        if isinstance(val, list):
            for v in val:
                user_a_signatures.add(str(v).strip().lower())
        elif val is not None:
            user_a_signatures.add(str(val).strip().lower())

    # Check if any signature appears in User B's injected items
    leaked_count = 0
    for fact_b in user_b_injected:
        key_b = str(fact_b.get("key", "")).strip().lower()
        val_b = fact_b.get("value")
        val_b_str = str(val_b).strip().lower()

        # If User B contains a unique key or sensitive value belonging to User A
        if key_b in user_a_signatures or any(
            sig in val_b_str for sig in user_a_signatures if len(sig) > 3
        ):
            leaked_count += 1

    leak_rate = leaked_count / len(user_a_facts) if user_a_facts else 0.0
    return round(leak_rate, 4)
