import json
import re
import sys
from pathlib import Path

# --- Regular Expressions & Lexicons ---
MONTH_NAME = r'(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)'
DATE_PART = rf'(?:{MONTH_NAME}\.?\s+\d{{4}}|\d{{2}}/\d{{4}}|\b\d{{4}}\b)'
END_PART = rf'(?:{DATE_PART}|Present|Current|Now)'
DATE_RANGE_RE = re.compile(rf'({DATE_PART}\s*(?:[-–—to\s]+)\s*{END_PART})', re.IGNORECASE)
SINGLE_DATE_RE = re.compile(rf'\b({DATE_PART})\b', re.IGNORECASE)

EMAIL_RE = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
PHONE_RE = re.compile(r'(?:\+?\d{1,3}[\s-]?)?\(?\d{2,4}\)?[\s.-]?\d{3,4}[\s.-]?\d{3,4}')
GITHUB_RE = re.compile(r'(?:https?://)?(?:www\.)?github(?:\.|\s*\.)\s*com/([a-zA-Z0-9_.-]+)', re.IGNORECASE)
LINKEDIN_RE = re.compile(r'(?:https?://)?(?:www\.)?linkedin(?:\.|\s*\.)\s*com/(?:in/)?([a-zA-Z0-9_.-]+)', re.IGNORECASE)
URL_RE = re.compile(r'((?:https?://)?(?:www\.)?github(?:\.|\s*\.)\s*com/[^\s]+|(?:https?://)[^\s]+)', re.IGNORECASE)
LANG_RE = re.compile(r'^([A-Za-z\s]{2,30})\s*[:=\-]\s*(.+)$')
GPA_RE = re.compile(r'GPA\s*:\s*([\d\.]+(?:/\s*[\d\.]+)?)|(?:\bGPA\b\s*)?([\d\.]+\s*/\s*[\d\.]+)', re.IGNORECASE)

DEGREE_KW = ['b.sc', 'b.s.', 'bachelor', 'master', 'm.sc', 'm.s.', 'phd', 'doctor', 'degree', 'diploma', 'associate']
INSTITUTION_KW = ['university', 'college', 'school', 'institute', 'academy', 'uit', 'vnu', 'polytechnic']
ROLE_KW = ['developer', 'engineer', 'leader', 'intern', 'manager', 'lead', 'architect', 'specialist', 'member', 'members', 'officer', 'consultant']
NOISE_RE = re.compile(r'^[a-z] [a-z] [a-z]\d+$')
CONTACT_LABELS = {'phone:', 'e-mail:', 'email:', 'linkedin:', 'github:', 'phone', 'email', 'linkedin', 'github'}

SECTION_PATTERNS = [
    ('objective', re.compile(r'^(?:career\s+)?objective|summary|professional\s+summary|about(?:\s+me)?|profile$', re.IGNORECASE)),
    ('education', re.compile(r'^education(?:al\s+background)?|academic(?:\s+background)?$', re.IGNORECASE)),
    ('skills', re.compile(r'^(?:technical\s+)?skills?(?:\s+highlights)?|skills?\s*(?:&|and)\s*(?:expertise|tools)?|technical\s+competencies|core\s+competencies$', re.IGNORECASE)),
    ('experience', re.compile(r'^(?:work\s+|professional\s+)?experience|employment(?:\s+history)?|work\s+history$', re.IGNORECASE)),
    ('projects', re.compile(r'^(?:academic\s+|personal\s+|key\s+)?projects?$', re.IGNORECASE)),
    ('key_highlights', re.compile(r'^(?:key\s+)?technical\s+highlights|highlights$', re.IGNORECASE)),
    ('languages', re.compile(r'^languages?$', re.IGNORECASE)),
    ('certifications', re.compile(r'^certifications?|certificates?|licenses?$', re.IGNORECASE)),
    ('references', re.compile(r'^references?$', re.IGNORECASE)),
]


def match_section(line: str):
    s = line.strip().lower()
    for sec_id, pattern in SECTION_PATTERNS:
        if pattern.match(s):
            return sec_id
    return None


def clean_bullet(text: str) -> str:
    text = re.sub(r'(\w+)\s*-\s*-\s*(\w+)', r'\1-\2', text)
    text = re.sub(r'(\w+)\s+-\s*(\w+)', r'\1-\2', text)
    text = re.sub(r'(\w+)\s*-\s+(\w+)', r'\1-\2', text)
    text = re.sub(r'\s+([.,;:!?])', r'\1', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()


def stitch_bullets(lines: list[str]) -> list[str]:
    bullets = []
    current = ''
    for line in lines:
        s = line.strip()
        if not s or NOISE_RE.match(s):
            continue
        s = re.sub(r'^[•\-\*]\s*', '', s)
        if not current:
            current = s
        else:
            if current.endswith('-') and not current.endswith(' -'):
                current = current[:-1] + s
            elif current.endswith('- ') or current.endswith(' - ') or current.endswith(' -'):
                current = current.rstrip('- ') + s
            elif current.endswith('.') or current.endswith(';'):
                bullets.append(clean_bullet(current))
                current = s
            else:
                current = current + ' ' + s
    if current:
        bullets.append(clean_bullet(current))
    return bullets


def clean_text_block(lines: list[str]) -> str:
    return ' '.join(stitch_bullets(lines))


def normalize_date(date_str: str) -> str:
    m = re.match(rf'^({DATE_PART})\s+({END_PART})$', date_str, re.IGNORECASE)
    if m:
        return f'{m.group(1)} - {m.group(2)}'
    return date_str


def _extract_contact(lines: list[str]) -> dict[str, str]:
    contact = {'name': '', 'phone': '', 'email': '', 'github': '', 'linkedin': ''}
    for line in lines:
        s = line.strip()
        if not s or NOISE_RE.match(s) or s.lower() in CONTACT_LABELS:
            continue
        if not contact['email']:
            m = EMAIL_RE.search(s)
            if m:
                contact['email'] = m.group(0)
                continue
        if not contact['github']:
            m = GITHUB_RE.search(s)
            if m:
                contact['github'] = re.sub(r'github\s*\.\s*com', 'github.com', m.group(0), flags=re.IGNORECASE)
                continue
        if not contact['linkedin']:
            m = LINKEDIN_RE.search(s)
            if m:
                contact['linkedin'] = m.group(0)
                continue
        if not contact['phone'] and PHONE_RE.search(s) and sum(c.isdigit() for c in s) >= 9:
            contact['phone'] = PHONE_RE.search(s).group(0).strip()
            continue
        if not contact['name'] and re.match(r'^[A-Za-zÀ-ỹ\s\.\-]+$', s) and not re.search(r'\d', s):
            words = s.split()
            if 2 <= len(words) <= 5 and not match_section(s):
                contact['name'] = s
    return contact


def _find_sections(lines: list[str]) -> dict[str, list[str]]:
    sections = {'preamble': []}
    current = 'preamble'
    for line in lines:
        s = line.strip()
        sec_id = match_section(s)
        if sec_id:
            current = sec_id
            if current not in sections:
                sections[current] = []
        else:
            sections[current].append(line)
    return sections


def _parse_entries(lines: list[str], is_project: bool = False) -> list[dict]:
    raw_entries = []
    current_entry_lines = []

    for line in lines:
        s = line.strip()
        if not s or NOISE_RE.match(s):
            continue
        has_bullets = any(len(line_text.split()) > 10 for line_text in current_entry_lines)
        is_date = bool(DATE_RANGE_RE.search(s))
        is_link = bool(URL_RE.search(s))

        if has_bullets and (is_date or (len(s.split()) <= 6 and not is_link and not s.endswith('.'))):
            raw_entries.append(current_entry_lines)
            current_entry_lines = [line]
        else:
            current_entry_lines.append(line)

    if current_entry_lines:
        raw_entries.append(current_entry_lines)

    entries = []
    title_key = 'name' if is_project else 'company'
    for chunk in raw_entries:
        entry = {
            title_key: '',
            'role': '',
            'period': '',
            'link': '',
            'highlights': []
        }
        meta_lines = []
        desc_lines = []
        is_desc = False

        for line_item in chunk:
            s = line_item.strip()
            m_link = URL_RE.search(s)
            if m_link and not is_desc:
                norm_link = re.sub(r'github\s*\.\s*com', 'github.com', m_link.group(0), flags=re.IGNORECASE)
                entry['link'] = norm_link
                continue

            m_date = DATE_RANGE_RE.search(s)
            is_role = any(kw in s.lower() for kw in ROLE_KW)
            if not is_desc and (m_date or is_role or len(meta_lines) == 0):
                meta_lines.append(s)
            else:
                is_desc = True
                desc_lines.append(s)

        for m in meta_lines:
            m_date = DATE_RANGE_RE.search(m)
            if m_date:
                entry['period'] = normalize_date(m_date.group(0).strip())
                rem = m.replace(m_date.group(0), '').strip(' -|,')
                if rem:
                    if not entry[title_key] and not any(kw in rem.lower() for kw in ROLE_KW):
                        entry[title_key] = rem
                    else:
                        entry['role'] = rem
                continue
            if ' - ' in m and not entry[title_key] and not entry['role']:
                parts = m.split(' - ', 1)
                entry['role'] = parts[0].strip()
                entry[title_key] = parts[1].strip()
                continue
            if any(kw in m.lower() for kw in ROLE_KW):
                entry['role'] = m
            elif not entry[title_key]:
                entry[title_key] = m
            elif not entry['role']:
                entry['role'] = m

        entry['highlights'] = stitch_bullets(desc_lines)
        if entry[title_key] or entry['role'] or entry['highlights']:
            entries.append(entry)

    return entries


def _parse_education(lines: list[str]) -> list[dict]:
    entries = []
    current = {'degree': '', 'institution': '', 'period': '', 'gpa': '', 'location': ''}

    for line in lines:
        s = line.strip()
        if not s or NOISE_RE.match(s):
            continue
        m_gpa = GPA_RE.search(s)
        if m_gpa:
            gpa_val = m_gpa.group(1) or m_gpa.group(2)
            current['gpa'] = gpa_val.replace(' ', '')
            s = GPA_RE.sub('', s).strip(' ,|')
            if not s:
                continue

        m_date = DATE_RANGE_RE.search(s)
        if m_date:
            date_str = normalize_date(m_date.group(0).strip())
            if current['period'] and (current['degree'] or current['institution']):
                entries.append({k: v for k, v in current.items() if v})
                current = {'degree': '', 'institution': '', 'period': '', 'gpa': '', 'location': ''}
            current['period'] = date_str
            s = s.replace(m_date.group(0), '').strip(' ,|')
            if not s:
                continue

        s_lower = s.lower()
        if any(kw in s_lower for kw in INSTITUTION_KW) and not current['institution']:
            current['institution'] = s
        elif any(kw in s_lower for kw in DEGREE_KW) and not current['degree']:
            current['degree'] = s
        elif ',' in s and any(c in s_lower for c in ['vietnam', 'viet nam', 'city', 'usa', 'state', 'district']) and not current['location']:
            current['location'] = s
        elif not current['institution']:
            current['institution'] = s
        elif not current['degree']:
            current['degree'] = s
        else:
            if current['institution']:
                current['institution'] += ' ' + s
            elif current['degree']:
                current['degree'] += ' ' + s

    if current['degree'] or current['institution']:
        entries.append({k: v for k, v in current.items() if v})
    return entries


def _parse_skills(lines: list[str]) -> tuple[list[str], dict[str, list[str]]]:
    flat_skills = []
    by_category = {}
    for line in lines:
        s = line.strip()
        if not s or NOISE_RE.match(s):
            continue
        if ':' in s:
            cat, val = s.split(':', 1)
            cat = cat.strip()
            items = [item.strip() for item in val.split(',') if item.strip()]
            if items:
                by_category[cat] = items
                flat_skills.extend(items)
        else:
            items = [item.strip() for item in s.split(',') if item.strip()]
            flat_skills.extend(items)
    return flat_skills, by_category


def parse_cv(lines: list[str]) -> dict:
    contact = _extract_contact(lines)
    sections = _find_sections(lines)

    # Summary
    obj_lines = sections.get('objective', [])
    preamble_lines = [
        line_item for line_item in sections.get('preamble', [])
        if not NOISE_RE.match(line_item.strip())
        and not any(contact.get(k) and contact[k].lower() in line_item.lower() for k in ['name', 'email', 'phone', 'github', 'linkedin'])
        and line_item.strip().lower() not in CONTACT_LABELS
    ]

    summary = clean_text_block(obj_lines) if obj_lines else clean_text_block(preamble_lines)

    # Education
    education = _parse_education(sections.get('education', []))

    # Skills
    skills, skills_by_category = _parse_skills(sections.get('skills', []))

    # Experience
    experience = _parse_entries(sections.get('experience', []), is_project=False)

    # Projects
    projects = _parse_entries(sections.get('projects', []), is_project=True)

    # Key Technical Highlights
    key_highlights = stitch_bullets(sections.get('key_highlights', []))

    # Languages
    languages = []
    for line_item in sections.get('languages', []):
        s = line_item.strip()
        if not s or NOISE_RE.match(s):
            continue
        m = LANG_RE.match(s)
        if m:
            languages.append({'language': m.group(1).strip(), 'level': m.group(2).strip()})
        else:
            languages.append({'language': s, 'level': ''})

    # Certifications
    certifications = [
        line_item.strip() for line_item in sections.get('certifications', [])
        if line_item.strip() and not NOISE_RE.match(line_item.strip()) and not LANG_RE.match(line_item.strip())
    ]

    # References
    references = [
        line_item.strip() for line_item in sections.get('references', [])
        if line_item.strip() and not NOISE_RE.match(line_item.strip())
    ]

    return {
        'personal_info': contact,
        'summary': summary,
        'education': education,
        'skills': skills,
        'skills_by_category': skills_by_category,
        'experience': experience,
        'projects': projects,
        'key_technical_highlights': key_highlights,
        'languages': languages,
        'certifications': certifications,
        'references': references,
    }


if __name__ == '__main__':
    json_path = None
    if len(sys.argv) > 1:
        json_path = Path(sys.argv[1])
    elif Path('doctr_extracted_lines.json').exists():
        json_path = Path('doctr_extracted_lines.json')
    elif Path('./docTR/new_resume_001.json').exists():
        json_path = Path('./docTR/new_resume_001.json')

    if json_path and json_path.exists():
        with open(json_path, encoding='utf-8') as f:
            raw = json.load(f)
        if isinstance(raw, list):
            lines = raw
        elif isinstance(raw, dict) and 'pages' in raw:
            lines = []
            for p in raw['pages']:
                lines.extend(p.get('lines', []))
        elif isinstance(raw, dict) and 'lines' in raw:
            lines = raw['lines']
        else:
            lines = []
        cv = parse_cv(lines)
        print(json.dumps(cv, indent=2, ensure_ascii=False))
    else:
        print('Usage: python3 cv_parser.py [path_to_lines.json]')
