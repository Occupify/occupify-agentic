import io
import sys
from pathlib import Path

# Ensure repo root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import pypdfium2
import yaml
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from app.documents.fetch import validate_pdf_bytes
from evals.uc4.render.layouts import render_layout_to_pdf


def render_markdown_to_pdf(markdown_text: str, output_path: Path) -> bytes:
    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    font_name = "Helvetica"
    for fc in [
        Path("/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf"),
        Path("/usr/share/fonts/liberation-sans-fonts/LiberationSans-Regular.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]:
        if fc.exists():
            try:
                pdfmetrics.registerFont(TTFont("CustomUnicodeFont", str(fc)))
                font_name = "CustomUnicodeFont"
                break
            except Exception:
                pass

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        fontName=font_name,
        fontSize=14,
        leading=18,
        spaceAfter=6,
    )
    heading2_style = ParagraphStyle(
        "CustomH2",
        parent=styles["Heading2"],
        fontName=font_name,
        fontSize=12,
        leading=15,
        spaceAfter=4,
    )
    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["Normal"],
        fontName=font_name,
        fontSize=10,
        leading=14,
        spaceAfter=4,
    )

    story = []
    lines = markdown_text.split("\n")
    for line in lines:
        stripped = line.strip()
        if not stripped:
            story.append(Spacer(1, 6))
            continue

        # Simple HTML escape for reportlab
        safe_line = stripped.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        if safe_line.startswith("# "):
            story.append(Paragraph(safe_line[2:], title_style))
        elif safe_line.startswith("## "):
            story.append(Paragraph(safe_line[3:], heading2_style))
        else:
            story.append(Paragraph(safe_line, body_style))

    doc.build(story)
    pdf_bytes = buf.getvalue()

    # Validate output
    page_count = validate_pdf_bytes(pdf_bytes, output_path.name)
    assert page_count >= 1, f"Generated PDF {output_path} has 0 pages"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(pdf_bytes)

    return pdf_bytes


def parse_frontmatter_and_body(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip()
            return fm, body
    return {}, text.strip()


def main():
    base_dir = Path(__file__).parent / "personas"

    # 1. Existing CV-A..H PDFs must NOT be re-rendered if they already exist
    for md_file in sorted(base_dir.glob("cv-*.md")):
        pdf_file = md_file.with_suffix(".pdf")
        if not pdf_file.exists():
            content = md_file.read_text(encoding="utf-8")
            pdf_bytes = render_markdown_to_pdf(content, pdf_file)
            print(f"Rendered {pdf_file.name}: {len(pdf_bytes)} bytes, validated.")
        else:
            print(f"Skipping existing {pdf_file.name} (CV-A..H preserved).")

    # 2. Render new stress CVs: l-*.md, p-*.md, x-*.md
    new_cv_files = (
        sorted(base_dir.glob("l-*.md"))
        + sorted(base_dir.glob("p-*.md"))
        + sorted(base_dir.glob("x-*.md"))
    )

    for md_file in new_cv_files:
        pdf_file = md_file.with_suffix(".pdf")
        content = md_file.read_text(encoding="utf-8")
        fm, body = parse_frontmatter_and_body(content)
        layout = fm.get("layout", "standard")

        pdf_bytes = render_layout_to_pdf(body, layout, pdf_file)

        # Write file
        pdf_file.write_bytes(pdf_bytes)

        # Verification check
        if layout.startswith("scanned"):
            doc = pypdfium2.PdfDocument(pdf_bytes)
            for page in doc:
                text_layer = page.get_textpage().get_text_range().strip()
                assert not text_layer, (
                    f"Scanned PDF {pdf_file.name} has non-empty text layer: {text_layer[:50]}"
                )
            print(
                f"Rendered {pdf_file.name} [{layout}]: {len(pdf_bytes)} bytes (Verified: ZERO text layer)."
            )
        else:
            page_count = validate_pdf_bytes(pdf_bytes, pdf_file.name)
            assert page_count >= 1, f"Generated PDF {pdf_file.name} has 0 pages"
            print(
                f"Rendered {pdf_file.name} [{layout}]: {len(pdf_bytes)} bytes ({page_count} pages validated)."
            )

    # 3. Ensure fixture invoice exists
    fixture_dir = Path(__file__).resolve().parents[2] / "tests" / "fixtures" / "job_match"
    fixture_dir.mkdir(parents=True, exist_ok=True)
    not_a_cv_pdf = fixture_dir / "not_a_cv.pdf"
    if not not_a_cv_pdf.exists():
        invoice_text = (
            "HÓA ĐƠN BÁN HÀNG DỊCH VỤ\n"
            "Mã số hóa đơn: INV-2026-9999\n"
            "Ngày xuất: 26/10/2026\n"
            "Đơn vị phát hành: Công ty TNHH Dịch vụ Thương mại Alpha\n"
            "Địa chỉ: Tầng 5, Tòa nhà Công nghệ, Hà Nội\n"
            "Nội dung cung cấp dịch vụ: Bản quyền phần mềm văn phòng\n"
            "Số lượng: 1 gói\n"
            "Đơn giá: 15.000.000 VNĐ\n"
            "Thuế suất GTGT: 10%\n"
            "Tổng thanh toán: 16.500.000 VNĐ\n"
            "Hình thức thanh toán: Chuyển khoản ngân hàng\n"
            "Cảm ơn quý khách đã sử dụng dịch vụ của chúng tôi."
        )
        render_markdown_to_pdf(invoice_text, not_a_cv_pdf)
        print(f"Rendered {not_a_cv_pdf.name} for NOT_A_CV test fixture.")


if __name__ == "__main__":
    main()
