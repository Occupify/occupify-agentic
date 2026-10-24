import re

REMOVED_SECTION_HEADINGS = [
    r"education",
    r"học vấn",
    r"trình độ học vấn",
    r"quá trình học tập",
    r"học tập",
    r"đào tạo",
    r"bằng cấp",
    r"academic background",
    r"academic history",
    r"academic qualifications?",
    r"personal info(?:rmation)?",
    r"thông tin cá nhân",
    r"thông tin liên hệ",
    r"thông tin liên lạc",
    r"contact(?: info(?:rmation)?)?",
    r"liên hệ",
    r"references?",
    r"người tham chiếu",
    r"người giới thiệu",
]

INCLUDED_SECTION_HEADINGS = [
    r"experience",
    r"work experience",
    r"professional experience",
    r"kinh nghiệm",
    r"kinh nghiệm làm việc",
    r"dự án và kinh nghiệm",
    r"dự án",
    r"projects?",
    r"personal projects?",
    r"dự án cá nhân",
    r"skills?",
    r"kỹ năng",
    r"technical skills?",
    r"kỹ năng chuyên môn",
    r"certifications?",
    r"chứng chỉ",
    r"awards?",
    r"giải thưởng",
    r"summary",
    r"tóm tắt",
    r"profile",
    r"giới thiệu",
    r"overview",
    r"tổng quan",
    r"career objective",
    r"mục tiêu",
    r"mục tiêu nghề nghiệp",
]

EXCLUDED_SECTION_REGEX = re.compile(
    r"(?i)^(?:#{1,4}\s*)?(?:" + "|".join(REMOVED_SECTION_HEADINGS) + r")\s*[:\-\—]?\s*$"
)

ANY_HEADING_REGEX = re.compile(
    r"(?i)^(?:#{1,4}\s*)?(?:"
    + "|".join(INCLUDED_SECTION_HEADINGS + REMOVED_SECTION_HEADINGS)
    + r")\s*[:\-\—]?\s*$"
)


def is_heading(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    # Markdown heading: # Heading
    if re.match(r"^#{1,4}\s+\S", stripped):
        return True
    return bool(ANY_HEADING_REGEX.match(stripped))


def is_excluded_heading(line: str) -> bool:
    stripped = line.strip()
    return bool(EXCLUDED_SECTION_REGEX.match(stripped))


def drop_sections(text: str) -> tuple[str, dict[str, int]]:
    """Drops entire sections like Education, Personal Info, Contact, References."""
    lines = text.split("\n")
    cleaned_lines: list[str] = []
    skipping = False
    counts = {"education": 0, "personal_info": 0, "contact_section": 0, "references": 0}

    for line in lines:
        stripped = line.strip()
        if is_heading(stripped):
            if is_excluded_heading(stripped):
                skipping = True
                lower = stripped.lower()
                if any(
                    k in lower
                    for k in ["education", "học vấn", "đào tạo", "bằng cấp", "học tập", "academic"]
                ):
                    counts["education"] += 1
                elif any(k in lower for k in ["reference", "tham chiếu", "giới thiệu"]):
                    counts["references"] += 1
                elif any(k in lower for k in ["contact", "liên hệ", "liên lạc"]):
                    counts["contact_section"] += 1
                else:
                    counts["personal_info"] += 1
                continue
            else:
                skipping = False

        if not skipping:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines), counts


def drop_contact_header(text: str) -> tuple[str, int]:
    """
    If the text before the first section heading contains contact info
    (email, phone, link, or [EMAIL], [PHONE]), drop that header block entirely.
    """
    lines = text.split("\n")
    first_heading_idx = -1

    for idx, line in enumerate(lines):
        if is_heading(line.strip()):
            first_heading_idx = idx
            break

    if first_heading_idx > 0:
        header_text = "\n".join(lines[:first_heading_idx])
        has_contact = (
            "@" in header_text
            or "[EMAIL]" in header_text
            or "[PHONE]" in header_text
            or "[LINK]" in header_text
            or "[SOCIAL_LINK]" in header_text
            or re.search(r"\d{7,}", header_text) is not None
        )
        if has_contact:
            return "\n".join(lines[first_heading_idx:]), 1

    return text, 0
