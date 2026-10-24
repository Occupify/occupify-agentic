import re
import unicodedata

from app.core.errors import PiiRemovalFailedError
from app.core.logging import log_step
from app.privacy.detectors import has_pii_remnants, remove_patterns
from app.privacy.sections import drop_contact_header, drop_sections


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def replace_known_identifiers(
    text: str,
    known_email: str = "",
    known_name: str = "",
) -> tuple[str, dict[str, int]]:
    counts = {"known_email": 0, "known_name": 0}

    # Replace known email
    if known_email and known_email.strip():
        pattern = re.compile(re.escape(known_email.strip()), re.IGNORECASE)
        text, n = pattern.subn("[EMAIL]", text)
        counts["known_email"] += n

    # Replace known full name (whole name only, with and without accents)
    if known_name and len(known_name.strip().split()) >= 2:
        name = known_name.strip()
        # Direct match with accents
        pattern1 = re.compile(r"\b" + re.escape(name) + r"\b", re.IGNORECASE)
        text, n1 = pattern1.subn("[NAME]", text)
        counts["known_name"] += n1

        # Match unaccented
        name_no_accent = strip_accents(name)
        if name_no_accent != name:
            pattern2 = re.compile(r"\b" + re.escape(name_no_accent) + r"\b", re.IGNORECASE)
            text, n2 = pattern2.subn("[NAME]", text)
            counts["known_name"] += n2

    return text, counts


def clean(
    text: str,
    source: str = "your message",
    known_email: str = "",
    known_name: str = "",
) -> tuple[str, dict[str, int]]:
    """
    Cleans text by removing sections, contact headers, known identifiers,
    and PII pattern matches.
    If PII cannot be guaranteed clean, raises PiiRemovalFailedError.
    """
    if not text or not text.strip():
        return text, {}

    total_counts: dict[str, int] = {}

    # 1. Drop contact header block (top block of CV up to first section heading)
    text, header_dropped = drop_contact_header(text)
    if header_dropped:
        total_counts["contact_header"] = header_dropped

    # 2. Drop excluded sections (Education, Personal Info, Contact, References)
    text, sec_counts = drop_sections(text)
    total_counts.update(sec_counts)

    # 3. Replace known identifiers (e.g. user email)
    text, ident_counts = replace_known_identifiers(text, known_email, known_name)
    total_counts.update(ident_counts)

    # 4. Pattern detectors
    text, pat_counts = remove_patterns(text)
    total_counts.update(pat_counts)

    # 5. Second pass / check again
    # Run detectors one more time to catch any nested or exposed items
    text, pat_counts2 = remove_patterns(text)
    for k, v in pat_counts2.items():
        total_counts[k] = total_counts.get(k, 0) + v

    # Verification: check if any unmasked PII remnants survive
    if has_pii_remnants(text):
        log_step("pii.blocked", source=source, reason="PII remnants detected after cleaning")
        raise PiiRemovalFailedError(source=source)

    # Filter out 0 counts
    active_counts = {k: v for k, v in total_counts.items() if v > 0}
    log_step("pii.cleaned", source=source, counts=active_counts)

    return text.strip(), active_counts
