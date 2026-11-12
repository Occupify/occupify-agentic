from app.features.cv_generator.renderer import render_cv
from app.features.cv_generator.schemas import GenerateCvInput
from tests.unit.cv_generator.helpers import sample_payload


def test_render_preserves_unicode_escapes_tex_and_has_no_sample_identity():
    payload = sample_payload()
    payload["cv"]["experience"][0]["bullets"] = [r"Literal \input{/etc/passwd} & 20% #1_$"]
    tex = render_cv(GenerateCvInput.model_validate(payload))
    assert r"\documentclass[a4paper,10pt]{article}" in tex
    assert "[YOUR NAME]" in tex and "[YOUR EMAIL]" in tex
    assert "Minh Tien Vo" not in tex and "tienvm886" not in tex
    assert r"\input{/etc/passwd}" not in tex
    assert r"\textbackslash{}input\{/etc/passwd\} \& 20\% \#1\_\$" in tex
    assert "Phát triển" in tex
    assert "Backend Developer, DevOps Engineer" in tex
    assert "mailto:" not in tex
    assert "HỌC VẤN" not in tex


def test_empty_roles_and_nullable_dates_do_not_print_none_or_dangling_separators():
    payload = sample_payload()
    payload["cv"]["experience"][0].update(roles=[], team_size=None, start_date=None, end_date=None)
    tex = render_cv(GenerateCvInput.model_validate(payload))
    assert "None" not in tex
    assert "Demo Company" in tex
    assert "DevOps Engineer" not in tex
