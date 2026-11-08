from pathlib import Path

import pytest

from evals.uc1.run_eval import load_dataset, run_evaluation


@pytest.mark.asyncio
async def test_dataset_loading():
    dataset_path = Path("evals/uc1/dataset.yaml")
    assert dataset_path.exists()
    data = load_dataset(dataset_path)
    assert "cases" in data
    cases = data["cases"]
    assert len(cases) >= 25

    categories = {c["category"] for c in cases}
    assert "roadmap" in categories
    assert "esco" in categories
    assert "onet" in categories
    assert "out_of_domain" in categories

    # Verify abstention queries have expected_abstention == True
    out_of_domain_cases = [c for c in cases if c["category"] == "out_of_domain"]
    assert len(out_of_domain_cases) >= 3
    assert all(c.get("expected_abstention") is True for c in out_of_domain_cases)


@pytest.mark.asyncio
async def test_run_evaluation_mock(tmp_path):
    doc_out = tmp_path / "doc_report.md"
    eval_out = tmp_path / "eval_report.md"

    summary = await run_evaluation(
        dataset_path="evals/uc1/dataset.yaml",
        doc_report_path=str(doc_out),
        eval_report_path=str(eval_out),
        mock_run=True,
    )

    assert summary["total_cases"] >= 25
    assert doc_out.exists()
    assert eval_out.exists()

    content = doc_out.read_text(encoding="utf-8")
    assert "Career Consultant RAG — Evaluation Report" in content
    assert "Recall@1" in content
    assert "Recall@5" in content
    assert "Citation Faithfulness" in content
    assert "Abstention Accuracy" in content
    assert "Category Breakdown" in content
