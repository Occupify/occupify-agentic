import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
APP_DIR = REPO_ROOT / "app"


def test_no_imports_from_tests_in_app():
    """Guard test (N-01): ensure production code under app/ never imports tests/."""
    violating_files = []
    import_pattern = re.compile(r"^\s*(from|import)\s+tests\b", re.MULTILINE)

    for py_file in APP_DIR.rglob("*.py"):
        content = py_file.read_text(encoding="utf-8")
        if import_pattern.search(content):
            violating_files.append(str(py_file.relative_to(REPO_ROOT)))

    assert not violating_files, (
        f"Production code in app/ illegally imports tests/: {violating_files}"
    )


def test_no_function_model_or_allow_model_requests_in_app():
    """Guard test (N-02.7): ensure no FunctionModel or ALLOW_MODEL_REQUESTS in app/ outside override seam."""
    violating_files = []
    pattern = re.compile(r"\b(FunctionModel|ALLOW_MODEL_REQUESTS)\b")

    for py_file in APP_DIR.rglob("*.py"):
        content = py_file.read_text(encoding="utf-8")
        if pattern.search(content):
            violating_files.append(str(py_file.relative_to(REPO_ROOT)))

    assert not violating_files, (
        f"Production code in app/ illegally uses FunctionModel/ALLOW_MODEL_REQUESTS: {violating_files}"
    )


def test_unscripted_model_call_in_unit_test_fails_loudly():
    """Ensure an unscripted model call in unit test fails loudly without silent fallbacks."""
    import pytest

    from app.agents.subagent import create_skill_agent

    agent = create_skill_agent("extract-candidate-profile")
    # With ALLOW_MODEL_REQUESTS=False in tests and no overrides, run must fail loudly
    with pytest.raises(RuntimeError) as exc_info:
        agent.run_sync("candidate cv text")
    assert "ALLOW_MODEL_REQUESTS is False" in str(
        exc_info.value
    ) or "Model requests are not allowed" in str(exc_info.value)
