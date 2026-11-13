import json
import re
from pathlib import Path


def sample_payload():
    # Independent hand-off fixture, not built from the production models.
    return {
        "template_id": "classic",
        "language": "vi",
        "cv": {
            "headline": "Backend Developer",
            "summary": "Phát triển API với Java & Python; giảm 20% độ trễ.",
            "skill_groups": [{"label": "Backend", "items": ["Java", "C#"]}],
            "experience": [
                {
                    "company": "Demo Company",
                    "roles": ["Backend Developer", "DevOps Engineer"],
                    "employment_type": "Freelance",
                    "location": None,
                    "start_date": "2024",
                    "end_date": "2025-02",
                    "is_current": False,
                    "team_size": 4,
                    "bullets": ["Xây dựng API quản lý khóa học."],
                }
            ],
            "projects": [],
            "education": [],
            "certifications": [],
            "additional_sections": [],
        },
    }


def handoff_examples():
    path = Path("docs/CV_GENERATOR_TOOL_INPUT.md")
    return [json.loads(b) for b in re.findall(r"```json\n(.*?)\n```", path.read_text(), re.S)]


def make_pdf(pages=1, size="A4"):
    from io import BytesIO

    from reportlab.lib.pagesizes import A4, letter
    from reportlab.pdfgen.canvas import Canvas

    output = BytesIO()
    canvas = Canvas(output, pagesize=A4 if size == "A4" else letter)
    for i in range(pages):
        canvas.drawString(60, 780, f"Synthetic CV page {i + 1}")
        canvas.showPage()
    canvas.save()
    return output.getvalue()
