import re

REMOVED_SECTION_KEYWORDS = [
    r"education",
    r"học vấn",
    r"trình độ học vấn",
    r"quá trình học tập",
    r"học tập",
    r"đào tạo",
    r"bằng cấp",
    r"academic",
    r"personal info",
    r"personal details",
    r"thông tin cá nhân",
    r"thông tin liên hệ",
    r"thông tin liên lạc",
    r"contact",
    r"liên hệ",
    r"liên lạc",
    r"references?",
    r"referee",
    r"người tham chiếu",
    r"người giới thiệu",
]

INCLUDED_SECTION_KEYWORDS = [
    r"experience",
    r"work experience",
    r"professional experience",
    r"employment",
    r"employment history",
    r"work history",
    r"career history",
    r"kinh nghiệm",
    r"kinh nghiệm làm việc",
    r"quá trình làm việc",
    r"dự án và kinh nghiệm",
    r"projects?",
    r"personal projects?",
    r"key projects?",
    r"selected projects?",
    r"dự án",
    r"dự án cá nhân",
    r"dự án tiêu biểu",
    r"skills?",
    r"technical skills?",
    r"core competencies",
    r"competencies",
    r"kỹ năng",
    r"kỹ năng chuyên môn",
    r"kỹ năng mềm",
    r"certifications?",
    r"certificates?",
    r"licenses?",
    r"chứng chỉ",
    r"bằng khen",
    r"awards?",
    r"honors?",
    r"achievements?",
    r"giải thưởng",
    r"thành tích",
    r"summary",
    r"professional summary",
    r"career summary",
    r"executive summary",
    r"profile",
    r"career profile",
    r"overview",
    r"tóm tắt",
    r"giới thiệu",
    r"tổng quan",
    r"career objective",
    r"objective",
    r"mục tiêu",
    r"mục tiêu nghề nghiệp",
    r"activities",
    r"volunteering",
    r"hoạt động",
    r"tình nguyện",
    r"publications",
    r"xuất bản",
]

EXCLUDED_HEADING_PATTERN = re.compile(
    r"\b(?:" + "|".join(REMOVED_SECTION_KEYWORDS) + r")\b",
    re.IGNORECASE,
)

INCLUDED_HEADING_PATTERN = re.compile(
    r"\b(?:" + "|".join(INCLUDED_SECTION_KEYWORDS) + r")\b",
    re.IGNORECASE,
)


def _categorize_excluded(title: str, counts: dict[str, int]) -> None:
    lower = title.lower()
    if any(
        k in lower for k in ["education", "học vấn", "đào tạo", "bằng cấp", "học tập", "academic"]
    ):
        counts["education"] += 1
    elif any(k in lower for k in ["reference", "referee", "tham chiếu", "giới thiệu"]):
        counts["references"] += 1
    elif any(k in lower for k in ["contact", "liên hệ", "liên lạc"]):
        counts["contact_section"] += 1
    else:
        counts["personal_info"] += 1


def parse_heading(line: str) -> tuple[bool, int, str]:
    """
    Parses a markdown heading or emphasized heading.
    Returns (is_heading, level, clean_title).
    """
    stripped = line.strip()
    if not stripped:
        return False, 0, ""

    # Markdown hash heading: #, ##, ###, ####, #####, ######
    m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
    if m:
        level = len(m.group(1))
        title = m.group(2).strip()
        return True, level, title

    # Uppercase or bold title line without hash (e.g. **WORK EXPERIENCE** or **Education** or HỌC VẤN:)
    m2 = re.match(
        r"^(?:\*{1,3}|_{1,3})?([A-Za-zÀ-ỹ0-9\s&/\-]{3,60})(?:\*{1,3}|_{1,3})?\s*[:\-\—]?$", stripped
    )
    if m2:
        title = m2.group(1).strip()
        if INCLUDED_HEADING_PATTERN.search(title) or EXCLUDED_HEADING_PATTERN.search(title):
            return True, 2, title

    return False, 0, ""


def is_excluded_heading(title: str) -> bool:
    return bool(EXCLUDED_HEADING_PATTERN.search(title))


def is_known_content_heading(title: str) -> bool:
    return bool(INCLUDED_HEADING_PATTERN.search(title))


def drop_sections(text: str) -> tuple[str, dict[str, int]]:
    """
    Drops entire sections like Education, Personal Info, Contact, References.
    Vocabulary-based: once inside an excluded section, skipping continues across
    subheadings and flat headings (like school names, degree titles, dates, referee names)
    until a heading whose title matches INCLUDED_SECTION_KEYWORDS is encountered, or another
    EXCLUDED_SECTION_KEYWORDS heading begins.
    """
    lines = text.split("\n")
    cleaned_lines: list[str] = []
    skipping = False
    counts = {"education": 0, "personal_info": 0, "contact_section": 0, "references": 0}

    for line in lines:
        is_hd, _, title = parse_heading(line)
        if is_hd:
            if is_excluded_heading(title):
                skipping = True
                _categorize_excluded(title, counts)
                continue
            elif is_known_content_heading(title):
                skipping = False

        if not skipping:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines), counts


def drop_contact_header(text: str) -> tuple[str, int, str, bool]:
    """
    Drops the entire top block of a CV up to the first known content section heading
    or excluded section heading.
    Returns (remaining_text, count_dropped, extracted_candidate_name, has_known_section).
    """
    lines = text.split("\n")
    first_known_section_idx = -1

    for idx, line in enumerate(lines):
        is_hd, _, title = parse_heading(line)
        if is_hd and (is_known_content_heading(title) or is_excluded_heading(title)):
            first_known_section_idx = idx
            break

    if first_known_section_idx == -1:
        return text, 0, "", False

    # Extract candidate name from top block (lines before first_known_section_idx)
    extracted_name = ""
    for line in lines[:first_known_section_idx]:
        stripped = line.strip()
        if not stripped:
            continue
        cleaned = re.sub(r"^[\s#*_\->|:]+", "", stripped)
        cleaned = re.sub(r"[\s*_\->|:]+$", "", cleaned).strip()
        if not cleaned:
            continue
        words = cleaned.split()
        if (
            2 <= len(words) <= 6
            and "@" not in cleaned
            and "http" not in cleaned.lower()
            and not re.search(r"\d{4,}", cleaned)
        ):
            extracted_name = cleaned
            break

    remaining_lines = lines[first_known_section_idx:]
    count = 1 if first_known_section_idx > 0 else 0
    return "\n".join(remaining_lines), count, extracted_name, True
