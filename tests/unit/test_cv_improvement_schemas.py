import json
from pathlib import Path

from app.skill_schemas.cv_improvement import (
    CvImprovementProposal,
    CvSuggestionItem,
    ResumeData,
)


def test_cv_suggestion_item_creation():
    item = CvSuggestionItem(
        id="s1",
        section="Experience",
        target_original_text="Viết API CRUD",
        suggested_revised_text="Thiết kế RESTful API chuẩn",
        reason="Tối ưu mô tả",
    )
    assert item.id == "s1"
    assert item.section == "Experience"


def test_validate_suggest_cv_improvements_example():
    example_path = (
        Path("skills")
        / "cv_improvement"
        / "suggest-cv-improvements"
        / "examples"
        / "case1.output.json"
    )
    assert example_path.exists()
    data = json.loads(example_path.read_text(encoding="utf-8"))
    proposal = CvImprovementProposal.model_validate(data)
    assert proposal.target_role == "Python Backend Developer"
    assert len(proposal.suggestions) == 3


def test_validate_apply_cv_revisions_example():
    example_path = (
        Path("skills") / "cv_improvement" / "apply-cv-revisions" / "examples" / "case1.output.json"
    )
    assert example_path.exists()
    data = json.loads(example_path.read_text(encoding="utf-8"))
    resume = ResumeData.model_validate(data)
    assert resume.full_name == "Nguyễn Văn A"
    assert len(resume.experiences) == 1
    assert len(resume.projects) == 1
