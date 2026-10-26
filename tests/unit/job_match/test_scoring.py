from app.features.job_match.scoring import compute_job_score, compute_project_scores


def test_score_formula_and_threshold():
    # S = 0.60*r + 0.30*c + 0.10*e
    # If r=0.8, c=1.0, e=0.5: S = 0.48 + 0.30 + 0.05 = 0.83 -> matchScore = 83, fits=True
    score, fits = compute_job_score(r=0.8, c=1.0, e=0.5, reranker_available=True)
    assert fits is True
    assert score == 83

    # Below threshold 0.45:
    # r=0.3, c=0.2, e=0.0: S = 0.18 + 0.06 + 0.0 = 0.24 -> matchScore = 24, fits=False
    score_low, fits_low = compute_job_score(r=0.3, c=0.2, e=0.0, reranker_available=True)
    assert fits_low is False
    assert score_low == 24


def test_project_score_is_max_fitting_job():
    job_scores = [
        {"job_id": "j1", "match_score": 75, "fits": True},
        {"job_id": "j2", "match_score": 90, "fits": True},
        {"job_id": "j3", "match_score": 40, "fits": False},
    ]
    proj_score, fitting_jobs = compute_project_scores(job_scores)
    assert proj_score == 90
    assert len(fitting_jobs) == 2
    assert [j["job_id"] for j in fitting_jobs] == ["j2", "j1"]


def test_no_match_returns_top_missing_skills():
    # When no project has any fitting job (max_score < 45)
    projects_with_jobs = [
        {
            "project_id": "p1",
            "jobs": [
                {
                    "job_id": "j1",
                    "match_score": 30,
                    "fits": False,
                    "missing_skills": ["Rust", "Go", "Docker"],
                }
            ],
        },
        {
            "project_id": "p2",
            "jobs": [
                {
                    "job_id": "j2",
                    "match_score": 20,
                    "fits": False,
                    "missing_skills": ["Rust", "Kubernetes", "Go"],
                }
            ],
        },
    ]
    outcome, items, top_missing = compute_project_ranking(projects_with_jobs)
    assert outcome == "NO_MATCH"
    assert len(items) == 0
    # Rust (2), Go (2) should be in top missing
    assert top_missing[:2] == ["Rust", "Go"] or top_missing[:2] == ["Go", "Rust"]


def test_degraded_formula_without_reranker():
    # Degraded formula: S = (0.30*c + 0.10*e) / 0.40
    # If c=1.0, e=0.5: S = (0.30 + 0.05) / 0.40 = 0.875 -> 88
    score, fits = compute_job_score(r=None, c=1.0, e=0.5, reranker_available=False)
    assert fits is True
    assert score == 88


def test_no_overlap_with_reranker_failure_gives_no_match():
    # c=0.0 (no skill overlap), e=1.0 (level matches):
    # S = (0.0 + 0.10) / 0.40 = 0.25 < 0.45 -> fits=False
    score, fits = compute_job_score(r=None, c=0.0, e=1.0, reranker_available=False)
    assert fits is False
    assert score == 25


from app.features.job_match.scoring import compute_project_ranking  # noqa: E402
