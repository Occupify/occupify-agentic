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
    known_name: str | list[str] = "",
) -> tuple[str, dict[str, int]]:
    counts = {"known_email": 0, "known_name": 0}

    # Replace known email
    if known_email and known_email.strip():
        pattern = re.compile(re.escape(known_email.strip()), re.IGNORECASE)
        text, n = pattern.subn("[EMAIL]", text)
        counts["known_email"] += n

    # Replace known names
    names = [known_name] if isinstance(known_name, str) else (known_name or [])
    for name_candidate in names:
        if name_candidate and len(name_candidate.strip().split()) >= 2:
            name = name_candidate.strip()
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
    is_file: bool = False,
    known_email: str = "",
    known_name: str = "",
) -> tuple[str, dict[str, int]]:
    """
    Cleans text by removing sections, contact headers (for files), known identifiers,
    and PII pattern matches.
    If PII cannot be guaranteed clean, raises PiiRemovalFailedError.
    """
    if not text or not text.strip():
        return text, {}

    total_counts: dict[str, int] = {}
    names_to_clean: list[str] = [n.strip() for n in [known_name] if n and n.strip()]

    # 1. Drop contact header block (files/attachments only, never typed message/context)
    is_file_target = (
        is_file
        or "attachment" in source.lower()
        or "file" in source.lower()
        or "preview" in source.lower()
        or "cv" in source.lower()
    )

    if is_file_target:
        text, header_dropped, extracted_name, has_known_section = drop_contact_header(text)
        if not has_known_section:
            log_step("pii.blocked", source=source, reason="File has no recognized section headings")
            raise PiiRemovalFailedError(source=source)
        if header_dropped:
            total_counts["contact_header"] = header_dropped
        if extracted_name and extracted_name not in names_to_clean:
            names_to_clean.append(extracted_name)

    # 2. Drop excluded sections (Education, Personal Info, Contact, References)
    text, sec_counts = drop_sections(text)
    total_counts.update(sec_counts)

    # 3. Replace known identifiers (e.g. user email, candidate names)
    text, ident_counts = replace_known_identifiers(text, known_email, names_to_clean)
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
    if has_pii_remnants(text, known_names=names_to_clean):
        log_step("pii.blocked", source=source, reason="PII remnants detected after cleaning")
        raise PiiRemovalFailedError(source=source)

    # Filter out 0 counts
    active_counts = {k: v for k, v in total_counts.items() if v > 0}
    log_step("pii.cleaned", source=source, counts=active_counts)

    return text.strip(), active_counts
