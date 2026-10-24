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


def parse_heading(line: str) -> tuple[bool, int, str]:
    """
    Parses a markdown heading or emphasized all-caps heading.
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

    # Uppercase line or bold uppercase line without hash (e.g. **WORK EXPERIENCE** or HỌC VẤN:)
    m2 = re.match(
        r"^(?:\*{1,3}|_{1,3})?([A-ZÀ-Ỹ0-9\s&/\-]{3,60})(?:\*{1,3}|_{1,3})?\s*[:\-\—]?$", stripped
    )
    if m2:
        title = m2.group(1).strip()
        # Verify it looks like a section name, not a regular sentence
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
    Maintains skipping across sub-headings (e.g. ### inside ## Education)
    until a heading of equal or higher level that is not excluded is encountered.
    """
    lines = text.split("\n")
    cleaned_lines: list[str] = []
    skipping = False
    skip_level = 0
    counts = {"education": 0, "personal_info": 0, "contact_section": 0, "references": 0}

    for line in lines:
        is_hd, level, title = parse_heading(line)
        if is_hd:
            if skipping:
                # If currently skipping an excluded section:
                # Any subheading (level > skip_level) must also be skipped!
                if level > skip_level:
                    continue
                # If equal or higher level (level <= skip_level):
                # Check if this new heading is also excluded
                if is_excluded_heading(title):
                    skip_level = level
                    lower = title.lower()
                    if any(
                        k in lower
                        for k in [
                            "education",
                            "học vấn",
                            "đào tạo",
                            "bằng cấp",
                            "học tập",
                            "academic",
                        ]
                    ):
                        counts["education"] += 1
                    elif any(
                        k in lower for k in ["reference", "referee", "tham chiếu", "giới thiệu"]
                    ):
                        counts["references"] += 1
                    elif any(k in lower for k in ["contact", "liên hệ", "liên lạc"]):
                        counts["contact_section"] += 1
                    else:
                        counts["personal_info"] += 1
                    continue
                else:
                    # New valid content heading at equal or higher level
                    skipping = False
            else:
                # Not currently skipping; check if entering an excluded section
                if is_excluded_heading(title):
                    skipping = True
                    skip_level = level
                    lower = title.lower()
                    if any(
                        k in lower
                        for k in [
                            "education",
                            "học vấn",
                            "đào tạo",
                            "bằng cấp",
                            "học tập",
                            "academic",
                        ]
                    ):
                        counts["education"] += 1
                    elif any(
                        k in lower for k in ["reference", "referee", "tham chiếu", "giới thiệu"]
                    ):
                        counts["references"] += 1
                    elif any(k in lower for k in ["contact", "liên hệ", "liên lạc"]):
                        counts["contact_section"] += 1
                    else:
                        counts["personal_info"] += 1
                    continue

        if not skipping:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines), counts


def drop_contact_header(text: str) -> tuple[str, int]:
    """
    Drops the entire top block of a CV up to the first known content section heading
    (e.g. Work Experience, Skills, Summary, Objective), treating any top heading
    like '# Full Name' as part of the candidate header block to remove names and contact info.
    """
    lines = text.split("\n")
    first_known_section_idx = -1

    for idx, line in enumerate(lines):
        is_hd, _, title = parse_heading(line)
        if is_hd and (is_known_content_heading(title) or is_excluded_heading(title)):
            first_known_section_idx = idx
            break

    if first_known_section_idx > 0:
        return "\n".join(lines[first_known_section_idx:]), 1

    # Fallback if no known section heading was detected:
    # check if lines before any heading contain contact info
    first_any_heading_idx = -1
    for idx, line in enumerate(lines):
        is_hd, _, _ = parse_heading(line)
        if is_hd:
            first_any_heading_idx = idx
            break

    if first_any_heading_idx > 0:
        top_text = "\n".join(lines[:first_any_heading_idx])
        if (
            "@" in top_text
            or "[EMAIL]" in top_text
            or "[PHONE]" in top_text
            or re.search(r"\d{8,}", top_text)
        ):
            return "\n".join(lines[first_any_heading_idx:]), 1

    return text, 0
