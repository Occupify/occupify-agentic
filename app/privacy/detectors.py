import re

# Email regex
EMAIL_REGEX = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    re.IGNORECASE,
)

# Phone regex (Vietnamese +84, 0..., international with spaces/dots/dashes)
# Matches 2-4 digit groupings: 091 234 56 78, +84 91 234 56 78, (028) 3822 1234, 0901234567, +1-555-0199
PHONE_REGEX = re.compile(
    r"(?:(?:\+84|\(\+84\)|0|\+\d{1,3})[\s.-]?(?:\(?\d{1,4}\)?[\s.-]?){2,5}\d{2,4}\b|\b\+?[1-9]\d{0,2}[\s.-]?(?:\(?\d{2,4}\)?[\s.-]?){1,4}\d{2,4}\b)",
    re.IGNORECASE,
)

# ID / Citizen Identity / Tax / Bank numbers
# Vietnam CCCD (12 digits), CMND (9 digits), tax codes
ID_NUMBER_REGEX = re.compile(
    r"\b(?:\d{12}|\d{9})\b",
)

# Passport numbers: 1-2 uppercase letters followed by 7-9 digits (e.g. C1234567, UK987654321)
PASSPORT_REGEX = re.compile(
    r"\b[A-Z]{1,2}\d{7,9}\b",
)

# Social links & portfolio links
SOCIAL_LINK_REGEX = re.compile(
    r"(?:https?://)?(?:www\.)?(?:linkedin\.com|facebook\.com|fb\.com|zalo\.me|twitter\.com|x\.com|instagram\.com|tiktok\.com|t\.me)/[A-Za-z0-9_.-]+",
    re.IGNORECASE,
)

PORTFOLIO_LINK_REGEX = re.compile(
    r"(?:https?://)?(?:www\.)?(?:github\.com|gitlab\.com|behance\.net|dribbble\.com)/[A-Za-z0-9_.-]+",
    re.IGNORECASE,
)

GENERIC_URL_REGEX = re.compile(
    r"https?://[^\s<>\"']+|www\.[^\s<>\"']+",
    re.IGNORECASE,
)

# Labelled lines (EN + VI) supporting markdown lists (- * +), bold (**), and table rows (|)
LABELLED_LINE_REGEX = re.compile(
    r"(?im)^\s*(?:[-*+•]\s+)?(?:\|\s*)?(?:\*{1,3}|_{1,3})?(?:"
    r"date of birth|dob|ngày sinh|năm sinh|birth\s*date|"
    r"address|địa chỉ|permanent address|current address|nơi ở|quê quán|"
    r"gender|sex|giới tính|"
    r"marital status|tình trạng hôn nhân|hôn nhân|"
    r"nationality|quốc tịch|dân tộc|"
    r"religion|tôn giáo|"
    r"id number|số cmnd|số cccd|hộ chiếu|passport(?:\s*no\.?|\s*number)?|tax id|mã số thuế|"
    r"current salary|expected salary|mức lương|thu nhập"
    r")(?:\*{1,3}|_{1,3})?\s*(?:[:\-\—|]|\s*\|\s*)[^\r\n]*$",
)


def remove_patterns(text: str) -> tuple[str, dict[str, int]]:
    counts = {
        "email": 0,
        "phone": 0,
        "id_number": 0,
        "passport": 0,
        "social_link": 0,
        "portfolio_link": 0,
        "labelled_line": 0,
        "url": 0,
    }

    # 1. Labelled personal lines (including table rows, lists, bold)
    def _lbl_sub(m: re.Match) -> str:
        counts["labelled_line"] += 1
        return ""

    text = LABELLED_LINE_REGEX.sub(_lbl_sub, text)

    # 2. Emails
    def _email_sub(m: re.Match) -> str:
        counts["email"] += 1
        return "[EMAIL]"

    text = EMAIL_REGEX.sub(_email_sub, text)

    # 3. Phones
    def _phone_sub(m: re.Match) -> str:
        digits = re.sub(r"\D", "", m.group(0))
        if 8 <= len(digits) <= 13:
            counts["phone"] += 1
            return "[PHONE]"
        return m.group(0)

    text = PHONE_REGEX.sub(_phone_sub, text)

    # 4. Passports
    def _passport_sub(m: re.Match) -> str:
        counts["passport"] += 1
        return "[ID_NUMBER]"

    text = PASSPORT_REGEX.sub(_passport_sub, text)

    # 5. Social links & Portfolios
    def _social_sub(m: re.Match) -> str:
        counts["social_link"] += 1
        return "[SOCIAL_LINK]"

    text = SOCIAL_LINK_REGEX.sub(_social_sub, text)

    def _portfolio_sub(m: re.Match) -> str:
        counts["portfolio_link"] += 1
        return "[PORTFOLIO_LINK]"

    text = PORTFOLIO_LINK_REGEX.sub(_portfolio_sub, text)

    # 6. Generic URLs
    def _url_sub(m: re.Match) -> str:
        counts["url"] += 1
        return "[LINK]"

    text = GENERIC_URL_REGEX.sub(_url_sub, text)

    # 7. ID Numbers (Vietnam CCCD 12 digits, CMND 9 digits)
    def _id_sub(m: re.Match) -> str:
        counts["id_number"] += 1
        return "[ID_NUMBER]"

    text = ID_NUMBER_REGEX.sub(_id_sub, text)

    return text, counts


def has_pii_remnants(text: str) -> bool:
    """Returns True if any unmasked personal identifier is still present."""
    if EMAIL_REGEX.search(text):
        return True

    for m in PHONE_REGEX.finditer(text):
        digits = re.sub(r"\D", "", m.group(0))
        if 8 <= len(digits) <= 13:
            return True

    if ID_NUMBER_REGEX.search(text):
        return True

    if PASSPORT_REGEX.search(text):
        return True

    if LABELLED_LINE_REGEX.search(text):
        return True

    return False
