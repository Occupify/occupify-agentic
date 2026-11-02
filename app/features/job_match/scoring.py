from collections import Counter
from typing import Any

SCORING_VERSION = "v2"


def compute_experience_score(
    profile_level: str | None,
    project_level: str | None,
) -> float:
    """
    Computes experience score e (ADR-001 / design §6):
    - 1.0 if profile level equals project level
    - 0.5 if one step apart (ENTRY <-> INTERMEDIATE <-> EXPERT)
    - 0.0 otherwise (e.g. ENTRY vs EXPERT)
    - 1.0 if either is unknown (None or unrecognized)
    """
    if not profile_level or not project_level:
        return 1.0

    levels = {"ENTRY": 1, "INTERMEDIATE": 2, "EXPERT": 3}
    p_lvl = levels.get(str(profile_level).upper().strip())
    prj_lvl = levels.get(str(project_level).upper().strip())
    if p_lvl is None or prj_lvl is None:
        return 1.0

    diff = abs(p_lvl - prj_lvl)
    if diff == 0:
        return 1.0
    elif diff == 1:
        return 0.5
    else:
        return 0.0


def compute_job_score(
    r: float | None,
    c: float,
    e: float,
    reranker_available: bool = True,
) -> tuple[int, bool]:
    """
    Computes overall job fit score:
    - Normal mode (reranker active): S = 0.60*r + 0.30*c + 0.10*e
    - Degraded mode (reranker failed): S = (0.30*c + 0.10*e) / 0.40
    - Threshold: S >= 0.45 implies fit = True
    - Returns: (round(100 * S), fits)
    """
    if reranker_available and r is not None:
        s = 0.60 * r + 0.30 * c + 0.10 * e
    else:
        s = (0.30 * c + 0.10 * e) / 0.40

    match_score = round(round(s, 6) * 100.0)
    fits = round(s, 6) >= 0.45
    return match_score, fits


def compute_project_scores(
    job_scores: list[dict[str, Any]],
) -> tuple[int, list[dict[str, Any]]]:
    """
    Computes project-level match score as the maximum match score among its jobs,
    and returns fitting jobs sorted descending by match score.
    """
    fitting_jobs = [j for j in job_scores if j.get("fits")]
    fitting_jobs.sort(key=lambda j: j.get("match_score", 0), reverse=True)

    max_score = max([j.get("match_score", 0) for j in job_scores], default=0)
    return max_score, fitting_jobs


def compute_project_ranking(
    projects_with_jobs: list[dict[str, Any]],
    limit: int = 10,
) -> tuple[str, list[dict[str, Any]], list[str]]:
    """
    Ranks projects based on fitting jobs:
    - If no fitting jobs found: returns ('NO_MATCH', [], top_missing_skills)
    - If fitting projects found: returns ('OK', ranked_projects[:limit], [])
    """
    ranked_projects: list[dict[str, Any]] = []
    all_missing_skills: list[str] = []

    for proj in projects_with_jobs:
        jobs = proj.get("jobs", [])
        for j in jobs:
            all_missing_skills.extend(j.get("missing_skills", []))

        proj_score, fitting_jobs = compute_project_scores(jobs)
        if fitting_jobs:
            ranked_projects.append(
                {
                    "project_id": proj.get("project_id", ""),
                    "match_score": proj_score,
                    "fitting_jobs": fitting_jobs,
                    "all_jobs": jobs,
                }
            )

    if not ranked_projects:
        counter = Counter(all_missing_skills)
        top_missing = [skill for skill, _ in counter.most_common(10)]
        return "NO_MATCH", [], top_missing

    ranked_projects.sort(key=lambda p: p["match_score"], reverse=True)
    return "OK", ranked_projects[:limit], []
