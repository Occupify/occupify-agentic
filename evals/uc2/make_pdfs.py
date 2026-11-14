"""PDF generation utility for Use Case 2: CV Improvement and Persona Evaluation.

Converts all markdown files (*.md) in evals/uc2/personas/ to corresponding
high-quality, Unicode-compliant (Vietnamese UTF-8) PDF files (*.pdf).

Usage:
    uv run python -m evals.uc2.make_pdfs
    uv run python evals/uc2/make_pdfs.py
"""

from __future__ import annotations

import io
import re
import sys
from pathlib import Path

import pypdfium2 as pdfium
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from app.documents.extract import validate_pdf_bytes

# Ensure repo root is on sys.path if run directly
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _register_unicode_font() -> tuple[str, str]:
    """Finds and registers a TrueType font supporting Vietnamese Unicode."""
    candidates = [
        # Windows system fonts
        (
            Path(r"C:\Windows\Fonts\arial.ttf"),
            Path(r"C:\Windows\Fonts\arialbd.ttf"),
        ),
        (
            Path(r"C:\Windows\Fonts\segoeui.ttf"),
            Path(r"C:\Windows\Fonts\segoeuib.ttf"),
        ),
        (
            Path(r"C:\Windows\Fonts\calibri.ttf"),
            Path(r"C:\Windows\Fonts\calibrib.ttf"),
        ),
        # Linux standard fonts
        (
            Path("/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf"),
            None,
        ),
        (
            Path("/usr/share/fonts/liberation-sans-fonts/LiberationSans-Regular.ttf"),
            Path("/usr/share/fonts/liberation-sans-fonts/LiberationSans-Bold.ttf"),
        ),
        (
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        ),
    ]

    for reg_path, bold_path in candidates:
        if reg_path.exists():
            font_name = "UC2VietFont"
            bold_name = "UC2VietFont-Bold" if bold_path and bold_path.exists() else "UC2VietFont"
            try:
                pdfmetrics.registerFont(TTFont(font_name, str(reg_path)))
                if bold_path and bold_path.exists():
                    pdfmetrics.registerFont(TTFont(bold_name, str(bold_path)))
                pdfmetrics.registerFontFamily(
                    font_name,
                    normal=font_name,
                    bold=bold_name,
                    italic=font_name,
                    boldItalic=bold_name,
                )
                return font_name, bold_name
            except Exception:
                continue

    return "Helvetica", "Helvetica-Bold"


_NORMAL_FONT, _BOLD_FONT = _register_unicode_font()


def _format_markdown_inline(text: str) -> str:
    """Safely escapes HTML and formats markdown bold/italic tags."""
    # First escape special characters
    safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # Replace bold **text** -> <b>text</b>
    safe = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", safe)

    # Replace italic *text* or _text_ -> <i>text</i>
    safe = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", safe)
    safe = re.sub(r"(?<!_)_(?!_)(.+?)(?<!_)_(?!_)", r"<i>\1</i>", safe)

    # Replace inline code `code` -> <font face="Courier">code</font>
    safe = re.sub(r"`(.+?)`", r'<font face="Courier" color="#0369A1">\1</font>', safe)

    return safe


def render_markdown_to_pdf(markdown_text: str, output_path: Path) -> bytes:
    """Compiles a Markdown text string into an A4 PDF document with Vietnamese support."""
    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "UC2Title",
        parent=styles["Heading1"],
        fontName=_BOLD_FONT,
        fontSize=15,
        leading=19,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=4,
    )
    contact_style = ParagraphStyle(
        "UC2Contact",
        parent=styles["Normal"],
        fontName=_NORMAL_FONT,
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#475569"),
        spaceAfter=6,
    )
    h2_style = ParagraphStyle(
        "UC2H2",
        parent=styles["Heading2"],
        fontName=_BOLD_FONT,
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=8,
        spaceAfter=3,
        borderPadding=(0, 0, 2, 0),
    )
    h3_style = ParagraphStyle(
        "UC2H3",
        parent=styles["Heading3"],
        fontName=_BOLD_FONT,
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#334155"),
        spaceBefore=4,
        spaceAfter=2,
    )
    body_style = ParagraphStyle(
        "UC2Body",
        parent=styles["Normal"],
        fontName=_NORMAL_FONT,
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=3,
    )
    bullet_style = ParagraphStyle(
        "UC2Bullet",
        parent=styles["Normal"],
        fontName=_NORMAL_FONT,
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#1E293B"),
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2,
    )
    subbullet_style = ParagraphStyle(
        "UC2SubBullet",
        parent=styles["Normal"],
        fontName=_NORMAL_FONT,
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155"),
        leftIndent=24,
        firstLineIndent=-8,
        spaceAfter=2,
    )

    story = []
    lines = markdown_text.splitlines()

    for idx, raw_line in enumerate(lines):
        line = raw_line.strip()
        if not line:
            story.append(Spacer(1, 4))
            continue

        if line.startswith("# "):
            story.append(Paragraph(_format_markdown_inline(line[2:]), title_style))
        elif line.startswith("## "):
            story.append(Paragraph(_format_markdown_inline(line[3:]), h2_style))
        elif line.startswith("### "):
            story.append(Paragraph(_format_markdown_inline(line[4:]), h3_style))
        elif idx == 1 and ("Email:" in line or "SĐT:" in line or "Phone:" in line):
            story.append(Paragraph(_format_markdown_inline(line), contact_style))
        elif line.startswith("* ") or line.startswith("• "):
            content = _format_markdown_inline(line[2:])
            story.append(Paragraph(f"&bull; {content}", subbullet_style))
        elif line.startswith("- "):
            content = _format_markdown_inline(line[2:])
            story.append(Paragraph(f"&bull; {content}", bullet_style))
        else:
            story.append(Paragraph(_format_markdown_inline(line), body_style))

    doc.build(story)
    pdf_bytes = buf.getvalue()

    # Validate output
    page_count = validate_pdf_bytes(pdf_bytes, output_path.name)
    assert page_count >= 1, f"Generated PDF {output_path.name} has 0 pages"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(pdf_bytes)
    return pdf_bytes


def generate_all_persona_pdfs(personas_dir: Path | None = None) -> list[Path]:
    """Generates PDF for every .md file in the specified personas directory."""
    if personas_dir is None:
        personas_dir = Path(__file__).parent / "personas"

    md_files = sorted(personas_dir.glob("*.md"))
    if not md_files:
        raise FileNotFoundError(f"No markdown files found in {personas_dir}")

    generated_pdfs: list[Path] = []
    print(f"Converting {len(md_files)} markdown files to PDF in {personas_dir}...")

    for md_file in md_files:
        pdf_file = md_file.with_suffix(".pdf")
        content = md_file.read_text(encoding="utf-8")
        pdf_bytes = render_markdown_to_pdf(content, pdf_file)

        # Quick text extraction check with pypdfium2
        doc = pdfium.PdfDocument(pdf_bytes)
        assert len(doc) >= 1, f"Empty document: {pdf_file.name}"
        extracted_text = "".join(p.get_textpage().get_text_range() for p in doc)
        assert len(extracted_text.strip()) > 20, (
            f"Extraction check failed for {pdf_file.name}: too short"
        )

        generated_pdfs.append(pdf_file)
        print(f"  [OK] Generated {pdf_file.name} ({len(pdf_bytes):,} bytes, {len(doc)} pages)")

    print(f"Successfully generated {len(generated_pdfs)}/{len(md_files)} PDF files.")
    return generated_pdfs


def main() -> None:
    personas_dir = Path(__file__).parent / "personas"
    generate_all_persona_pdfs(personas_dir)


if __name__ == "__main__":
    main()
