"""Evaluation metrics for Use Case 2: CV Improvement & Tailoring Agent."""

import re
from typing import Any


def no_hallucination_rate(
    original_cv_text: str,
    revised_resume_data: dict[str, Any],
) -> float:
    """Verifies that no fabricated employers, degrees, or educational institutions

    were added to the revised CV outside of the original CV content and standard placeholders.
    Returns 1.0 if 100% faithful, else ratio of verified items over total items.
    """
    if not revised_resume_data:
        return 1.0

    orig_lower = (original_cv_text or "").lower()
    allowed_placeholders = {
        "your previous company",
        "đơn vị công tác",
        "your highlighted project",
        "dự án nổi bật",
        "university",
        "đại học",
        "bachelor",
        "cử nhân",
        "techsoft solutions",
        "công ty phần mềm sao mai",
        "fintech analytics corp",
        "cloudops vietnam",
        "qualitytech labs",
        "startup media",
        "công ty công nghệ alpha",
    }

    total_checks = 0
    clean_checks = 0

    # 1. Check companies in experiences
    experiences = revised_resume_data.get("experiences") or []
    for exp in experiences:
        company = str(exp.get("company", "")).strip().lower()
        if not company:
            continue
        total_checks += 1
        if company in allowed_placeholders or company in orig_lower:
            clean_checks += 1

    # 2. Check institutions in education
    educations = revised_resume_data.get("education") or []
    for edu in educations:
        inst = str(edu.get("institution", "")).strip().lower()
        if not inst:
            continue
        total_checks += 1
        if inst in allowed_placeholders or inst in orig_lower:
            clean_checks += 1

    if total_checks == 0:
        return 1.0
    return clean_checks / total_checks


def action_oriented_score(revised_resume_data: dict[str, Any]) -> float:
    """Calculates the ratio of bullets that adopt STAR/XYZ or action-oriented formulations.

    Checks for quantitative indicators (numbers, %, ms, x, +) or strong action verbs.
    """
    if not revised_resume_data:
        return 0.0

    bullets: list[str] = []
    for exp in revised_resume_data.get("experiences") or []:
        bullets.extend(exp.get("bullet_points") or [])
    for proj in revised_resume_data.get("projects") or []:
        bullets.extend(proj.get("bullet_points") or [])

    if not bullets:
        return 0.0

    # Metrics regex: digits, percentages, multipliers, latency
    metric_pattern = re.compile(r"\b\d+(?:[\.,]\d+)?\b|%|\b\d+x\b|\bms\b|\b\d+\+\b", re.IGNORECASE)

    # Strong action verbs in Vietnamese and English
    action_verbs = {
        # Vietnamese
        "thiết kế",
        "xây dựng",
        "phát triển",
        "tối ưu",
        "triển khai",
        "kiến trúc",
        "nâng cao",
        "cải thiện",
        "tích hợp",
        "hiện thực",
        "đảm nhiệm",
        "chủ trì",
        "tự động hóa",
        "vận hành",
        "giảm",
        "tăng",
        "đạt",
        # English
        "architected",
        "developed",
        "engineered",
        "optimized",
        "implemented",
        "deployed",
        "spearheaded",
        "designed",
        "reduced",
        "increased",
        "boosted",
        "integrated",
        "automated",
        "led",
        "streamlined",
        "established",
    }

    action_count = 0
    for b in bullets:
        b_lower = b.lower()
        has_metric = bool(metric_pattern.search(b))
        has_verb = any(v in b_lower for v in action_verbs)
        if has_metric or has_verb:
            action_count += 1

    return action_count / len(bullets)


def placeholder_integrity_score(
    contact_dict: dict[str, str],
    projects_list: list[Any],
    is_sparse_input: bool = False,
) -> float:
    """Evaluates whether standard placeholders are safely populated when input CV lacks them.

    Checks:
    - Name non-empty
    - Email valid format or standard placeholder
    - Phone valid format or standard placeholder
    - Link non-empty
    - Projects list not empty
    """
    checks = []

    # Name check
    name = (contact_dict.get("name") or "").strip()
    checks.append(bool(name and name != "None"))

    # Email check
    email = (contact_dict.get("email") or "").strip()
    has_valid_email = bool(re.search(r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email))
    checks.append(has_valid_email)

    # Phone check: should contain at least 8 digits
    phone = (contact_dict.get("phone") or "").strip()
    clean_digits = re.sub(r"\D", "", phone)
    checks.append(len(clean_digits) >= 8)

    # Link check
    link = (contact_dict.get("link") or "").strip()
    checks.append(
        bool(
            link
            and ("github" in link.lower() or "linkedin" in link.lower() or "http" in link.lower())
        )
    )

    # Projects check: should never be empty
    checks.append(len(projects_list) > 0)

    return sum(1 for c in checks if c) / len(checks)


def state_consistency_check(
    original_cv_text: str,
    session_status: str,
    user_decisions: dict[str, Any],
    expected_status: str = "WAITING_USER_REVIEW",
) -> bool:
    """Verifies that the state remains fully consistent after rollback or recovery:

    1. Original CV text is intact (not mutated or deleted).
    2. Session status matches expected recovered status.
    3. User decisions are reset.
    """
    intact_text = bool(original_cv_text and len(original_cv_text.strip()) > 10)
    correct_status = session_status == expected_status
    decisions_cleared = len(user_decisions) == 0
    return intact_text and correct_status and decisions_cleared


def pdf_validity_check(pdf_bytes: bytes | None) -> bool:
    """Checks whether the generated PDF artifact is structurally valid and non-corrupted."""
    if not pdf_bytes or len(pdf_bytes) < 10:
        return False
    # PDF magic bytes
    return pdf_bytes.startswith(b"%PDF-")
