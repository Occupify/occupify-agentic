"""Opt-in real, credential-free compiler tests. No OCI or model requests."""

import os
import subprocess
from pathlib import Path

import pytest

from app.features.cv_generator.compiler import validate_pdf
from app.features.cv_generator.renderer import render_cv
from app.features.cv_generator.schemas import GenerateCvInput
from tests.unit.cv_generator.helpers import handoff_examples, sample_payload

pytestmark = pytest.mark.skipif(
    not os.environ.get("CV_COMPILER_TEST_IMAGE"),
    reason="Set CV_COMPILER_TEST_IMAGE to run real TeX",
)


def compile_in_container(tex):
    result = subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "--network",
            "none",
            "--read-only",
            "--tmpfs",
            "/tmp:size=256m,mode=1777",
            "--cap-drop",
            "ALL",
            "--security-opt",
            "no-new-privileges",
            "--memory",
            "768m",
            "--pids-limit",
            "64",
            "-i",
            os.environ["CV_COMPILER_TEST_IMAGE"],
            "python",
            "-c",
            "import asyncio,sys; "
            "from app.features.cv_generator.compiler import LocalCvCompiler; "
            "sys.stdout.buffer.write(asyncio.run(LocalCvCompiler().compile(sys.stdin.read())))",
        ],
        input=tex.encode(),
        capture_output=True,
        timeout=50,
    )
    assert result.returncode == 0, result.stderr.decode(errors="replace")[-2000:]
    return result.stdout


@pytest.mark.parametrize("language", ["vi", "en"])
def test_standalone_cv_compiles_with_placeholders_and_unicode(language, tmp_path):
    payload = sample_payload()
    payload["language"] = language
    tex = render_cv(GenerateCvInput.model_validate(payload))
    pdf = compile_in_container(tex)
    assert validate_pdf(pdf) == 1
    artifact_dir = os.environ.get("CV_COMPILER_ARTIFACT_DIR")
    target = Path(artifact_dir) if artifact_dir else tmp_path
    target.mkdir(parents=True, exist_ok=True)
    (target / f"cv-{language}.tex").write_text(tex)
    (target / f"cv-{language}.pdf").write_bytes(pdf)


def test_real_two_pages_and_three_page_limit():
    from app.features.cv_generator.schemas import CvGenerationError

    tex = render_cv(GenerateCvInput.model_validate(sample_payload()))
    two = tex.replace(r"\end{document}", r"\newpage Second page\end{document}")
    assert validate_pdf(compile_in_container(two)) == 2
    three = tex.replace(r"\end{document}", r"\newpage Second\newpage Third\end{document}")
    with pytest.raises(CvGenerationError) as exc:
        validate_pdf(compile_in_container(three))
    assert exc.value.code == "CONTENT_TOO_LONG"


def test_real_renderer_flows_long_content_to_second_page():
    payload = sample_payload()
    payload["cv"]["experience"][0]["bullets"] = [
        "Phát triển API quản lý khóa học, kiểm thử luồng phân quyền và triển khai dịch vụ "
        "bằng container; phối hợp với nhóm để kiểm tra chất lượng trước mỗi lần phát hành."
    ] * 28
    pdf = compile_in_container(render_cv(GenerateCvInput.model_validate(payload)))
    assert validate_pdf(pdf) == 2


def test_literal_brackets_at_start_of_bullets_are_not_latex_optional_arguments():
    payload = sample_payload()
    payload["cv"]["experience"][0]["bullets"] = ["[draft chưa xác nhận", "[AWS] Triển khai API."]
    payload["cv"]["additional_sections"] = [
        {"title": "Ghi chú", "items": [{"label": None, "text": "[ghi chú chưa đóng"}]}
    ]
    tex = render_cv(GenerateCvInput.model_validate(payload))
    assert validate_pdf(compile_in_container(tex)) == 1


def test_complete_handoff_example_renders_all_sections(tmp_path):
    tex = render_cv(GenerateCvInput.model_validate(handoff_examples()[0]))
    pdf = compile_in_container(tex)
    assert validate_pdf(pdf) in {1, 2}
    target = Path(os.environ.get("CV_COMPILER_ARTIFACT_DIR", tmp_path))
    target.mkdir(parents=True, exist_ok=True)
    (target / "cv-complete.pdf").write_bytes(pdf)
