import re
from functools import lru_cache
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from app.features.cv_generator.schemas import GenerateCvInput, display_date

_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}
_SPECIAL = re.compile(r"[\\&%$#_{}~^]")


def escape_tex(value: str) -> str:
    return _SPECIAL.sub(lambda match: _ESCAPES[match.group()], value)


@lru_cache(maxsize=1)
def environment() -> Environment:
    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent / "templates"),
        undefined=StrictUndefined,
        autoescape=False,
        block_start_string="((*",
        block_end_string="*))",
        variable_start_string="(((",
        variable_end_string=")))",
        comment_start_string="((#",
        comment_end_string="#))",
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["tex"] = escape_tex
    return env


def render_cv(payload: GenerateCvInput, contact: dict[str, str] | None = None) -> str:
    vi = payload.language == "vi"
    labels = {
        "summary": "TÓM TẮT" if vi else "PROFESSIONAL SUMMARY",
        "education": "HỌC VẤN" if vi else "EDUCATION",
        "certifications": "CHỨNG CHỈ" if vi else "CERTIFICATIONS",
        "skills": "KỸ NĂNG" if vi else "SKILLS",
        "experience": "KINH NGHIỆM" if vi else "EXPERIENCE",
        "projects": "DỰ ÁN" if vi else "PROJECTS",
        "present": "Hiện tại" if vi else "Present",
        "expected": "Dự kiến" if vi else "Expected",
        "members": "thành viên" if vi else "members",
    }

    def period(entry):
        start = display_date(entry.start_date, payload.language)
        end = display_date(entry.end_date, payload.language)
        if getattr(entry, "is_expected", False):
            end = f"{labels['expected']} {end}"
        elif entry.is_current:
            end = labels["present"]
        return " – ".join(value for value in (start, end) if value)

    return (
        environment()
        .get_template("classic.tex.j2")
        .render(
            cv=payload.cv,
            labels=labels,
            period=period,
            date=lambda value: display_date(value, payload.language),
            contact=contact or {},
        )
    )
