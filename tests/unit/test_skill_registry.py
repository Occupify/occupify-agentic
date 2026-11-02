from pathlib import Path

import pytest

from app.agents.skill_registry import (
    SkillRegistry,
    SkillValidationError,
    generate_catalog_markdown,
    validate_skills_directory,
)
from app.skill_schemas.candidate import CandidateProfile


def test_library_is_valid():
    # Validates service-wide skills library
    skills_dir = Path("skills")
    if skills_dir.exists():
        errors = validate_skills_directory(skills_dir)
        assert len(errors) == 0, f"Skills library validation failed: {errors}"


def test_registry_rejects_invalid_skill():
    fixtures_dir = Path("tests/fixtures/skills_invalid")

    # 1. Duplicate name
    with pytest.raises(SkillValidationError) as exc:
        validate_skills_directory(fixtures_dir / "broken_duplicate_name")
    assert "duplicate" in str(exc.value).lower()

    # 2. Unknown output model
    with pytest.raises(SkillValidationError) as exc:
        validate_skills_directory(fixtures_dir / "broken_unknown_output")
    assert "output" in str(exc.value).lower()

    # 3. Missing shared reference
    with pytest.raises(SkillValidationError) as exc:
        validate_skills_directory(fixtures_dir / "broken_missing_shared_ref")
    assert "reference" in str(exc.value).lower() or "missing" in str(exc.value).lower()

    # 4. Tool not allowed
    with pytest.raises(SkillValidationError) as exc:
        validate_skills_directory(fixtures_dir / "broken_tool_not_allowed")
    assert "tool" in str(exc.value).lower()

    # 5. Invalid example
    with pytest.raises(SkillValidationError) as exc:
        validate_skills_directory(fixtures_dir / "broken_invalid_example")
    assert "example" in str(exc.value).lower()


def test_catalog_is_current():
    catalog_file = Path("skills/catalog.md")
    if catalog_file.exists():
        expected_md = generate_catalog_markdown(Path("skills"))
        actual_md = catalog_file.read_text(encoding="utf-8")
        assert actual_md.strip() == expected_md.strip()


def test_output_type_comes_from_frontmatter():
    registry = SkillRegistry()
    registry.scan(Path("skills"))
    meta = registry.get("extract-candidate-profile")
    assert meta is not None
    assert meta.output_type is CandidateProfile


def test_skill_version_stable_and_changes_with_content(tmp_path):
    skill_dir = tmp_path / "test_skill"
    skill_dir.mkdir()
    skill_file = skill_dir / "SKILL.md"
    skill_file.write_text(
        "---\nname: ver-test\ndescription: Test\noutput: app.skill_schemas.candidate.CandidateProfile\n---\nPrompt v1\n",
        encoding="utf-8",
    )

    reg = SkillRegistry()
    reg.scan(tmp_path)
    v1 = reg.get("ver-test").skill_version
    assert len(v1) == 12

    # Stable on same content
    reg2 = SkillRegistry()
    reg2.scan(tmp_path)
    assert reg2.get("ver-test").skill_version == v1

    # Changes with prompt content
    skill_file.write_text(
        "---\nname: ver-test\ndescription: Test\noutput: app.skill_schemas.candidate.CandidateProfile\n---\nPrompt v2 modified\n",
        encoding="utf-8",
    )
    reg3 = SkillRegistry()
    reg3.scan(tmp_path)
    v2 = reg3.get("ver-test").skill_version
    assert v2 != v1
