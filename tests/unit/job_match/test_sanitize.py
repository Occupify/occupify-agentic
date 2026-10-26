from app.features.job_match.sanitize import sanitize_project


def test_each_field_cleaned_individually(monkeypatch):
    calls: list[str] = []

    def mock_clean(text: str, source: str = "project", is_file: bool = False, **kwargs):
        calls.append(text)
        return text, {"test": 0}

    monkeypatch.setattr("app.features.job_match.sanitize.clean", mock_clean)

    sample_project = {
        "id": "a1000000-0000-0000-0000-000000000001",
        "title": "Clean Project Title",
        "description": "Clean description.",
        "status": "OPEN",
        "jobs": [
            {
                "id": "b1000000-0000-0000-0000-000000000101",
                "title": "Clean Job Title",
                "description": "Clean job description.",
                "status": "RECRUITING",
                "skills": ["Python", "Docker"],
                "requirements": ["Req 1", "Req 2"],
            }
        ],
    }

    rows = sanitize_project(sample_project)
    assert len(rows) == 1
    # Check that each text field was cleaned on its own
    assert "Clean Project Title" in calls
    assert "Clean description." in calls
    assert "Clean Job Title" in calls
    assert "Clean job description." in calls
    assert "Python" in calls
    assert "Docker" in calls
    assert "Req 1" in calls
    assert "Req 2" in calls


def test_pii_in_skill_name_dropped(monkeypatch):
    def mock_clean(text: str, source: str = "project", is_file: bool = False, **kwargs):
        if "sensitive@example.com" in text:
            # gate fails/drops field
            raise ValueError("PII detected in skill name")
        return text, {}

    monkeypatch.setattr("app.features.job_match.sanitize.clean", mock_clean)

    sample_project = {
        "id": "proj-1",
        "title": "Safe Title",
        "description": "Safe Desc",
        "status": "OPEN",
        "jobs": [
            {
                "id": "job-1",
                "title": "Safe Job",
                "description": "Safe Job Desc",
                "status": "RECRUITING",
                "skills": ["React", "Contact sensitive@example.com", "TypeScript"],
                "requirements": ["Good communication"],
            }
        ],
    }

    rows = sanitize_project(sample_project)
    assert len(rows) == 1
    # PII skill was dropped, safe skills kept
    assert rows[0].skills == ["React", "TypeScript"]


def test_requirement_numbering_kept(monkeypatch):
    def mock_clean(text: str, source: str = "project", is_file: bool = False, **kwargs):
        if "bad requirement" in text.lower():
            raise ValueError("PII in requirement")
        return text, {}

    monkeypatch.setattr("app.features.job_match.sanitize.clean", mock_clean)

    sample_project = {
        "id": "proj-1",
        "title": "Title",
        "description": "Desc",
        "status": "OPEN",
        "jobs": [
            {
                "id": "job-1",
                "title": "Job",
                "description": "Desc",
                "status": "RECRUITING",
                "skills": ["Java"],
                "requirements": ["Req A", "Bad requirement with PII", "Req C"],
            }
        ],
    }

    rows = sanitize_project(sample_project)
    assert len(rows) == 1
    # The dropped requirement becomes empty string or marked so indices/count align
    assert len(rows[0].requirements) == 3
    assert rows[0].requirements[0] == "Req A"
    assert rows[0].requirements[1] == ""  # emptied but slot kept for original numbering
    assert rows[0].requirements[2] == "Req C"


def test_numbers_and_ids_untouched(monkeypatch):
    cleaned_fields: list[str] = []

    def mock_clean(text: str, source: str = "project", is_file: bool = False, **kwargs):
        cleaned_fields.append(text)
        return text, {}

    monkeypatch.setattr("app.features.job_match.sanitize.clean", mock_clean)

    proj_id = "a1000000-0000-0000-0000-000000000001"
    job_id = "b1000000-0000-0000-0000-000000000101"
    sample_project = {
        "id": proj_id,
        "title": "Title",
        "description": "Desc",
        "startPrice": 45000000,
        "status": "OPEN",
        "jobs": [
            {
                "id": job_id,
                "title": "Job Title",
                "description": "Job Desc",
                "quantity": 1,
                "salaryType": "MONTHLY",
                "budgetMin": 40000000,
                "budgetMax": 55000000,
                "status": "RECRUITING",
                "skills": ["Python"],
                "requirements": ["Req"],
            }
        ],
    }

    rows = sanitize_project(sample_project)
    assert len(rows) == 1
    row = rows[0]
    assert row.project_id == proj_id
    assert row.job_id == job_id
    assert row.budget_min == 40000000
    assert row.budget_max == 55000000
    # Ensure IDs and budgets were never sent to clean()
    assert proj_id not in cleaned_fields
    assert job_id not in cleaned_fields
    assert "40000000" not in cleaned_fields
    assert "55000000" not in cleaned_fields
