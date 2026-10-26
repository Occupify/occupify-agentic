import pytest
from app.agents.capture import capture_model_requests
from app.features.job_match.normalize import normalize_skill_name
from app.features.job_match.skill_match import (
    compute_skill_coverage,
    match_skills_for_project,
)
from app.skill_schemas.candidate import CandidateProfile
from app.skill_schemas.matching import JobSkillVerdict, SkillMatchResult

from app.agents.subagent import override_skill_models
from tests.unit.job_match.scripts import structured


def test_coverage_weights():
    # c = sum(weights) / len(job.skills)
    # exact = 1.0, equivalent = 1.0, inferred = 0.8, missing = 0.0
    verdicts = [
        JobSkillVerdict(job_skill="React", verdict="exact", cv_skill="React"),
        JobSkillVerdict(job_skill="TypeScript", verdict="equivalent", cv_skill="TS"),
        JobSkillVerdict(job_skill="Java", verdict="inferred", cv_skill="Spring Boot"),
        JobSkillVerdict(job_skill="Docker", verdict="missing"),
    ]
    # Sum = 1.0 + 1.0 + 0.8 + 0.0 = 2.8 / 4 = 0.70
    c = compute_skill_coverage(verdicts)
    assert pytest.approx(c, 0.001) == 0.70


def test_code_fallback_normalises_reactjs_to_react():
    assert normalize_skill_name("ReactJS") == normalize_skill_name("React")
    assert normalize_skill_name("React.JS") == normalize_skill_name("React")
    assert normalize_skill_name("Node.js") == normalize_skill_name("NodeJS")
    assert normalize_skill_name("PostgreSQL") == normalize_skill_name("Postgres")
    assert normalize_skill_name("Tailwind CSS") == normalize_skill_name("TailwindCSS")


@pytest.mark.asyncio
async def test_equivalent_verdicts_never_missing():
    profile = CandidateProfile(
        status="ok",
        skills=["ReactJS", "NextJS", "TS", "TailwindCSS"],
    )
    job_skills = {"j01": ["React", "Next.js", "TypeScript", "Tailwind CSS"]}

    # Scripted model returning equivalent verdicts
    mock_result = SkillMatchResult(
        job_verdicts={
            "j01": [
                JobSkillVerdict(job_skill="React", verdict="equivalent", cv_skill="ReactJS"),
                JobSkillVerdict(job_skill="Next.js", verdict="equivalent", cv_skill="NextJS"),
                JobSkillVerdict(job_skill="TypeScript", verdict="equivalent", cv_skill="TS"),
                JobSkillVerdict(
                    job_skill="Tailwind CSS", verdict="equivalent", cv_skill="TailwindCSS"
                ),
            ]
        }
    )

    with override_skill_models({"match-skills": structured(mock_result)}):
        res, warnings = await match_skills_for_project(
            project_id="p06",
            project_jobs=job_skills,
            profile=profile,
        )

    assert "SKILL_MATCH_FALLBACK" not in warnings
    j01_res = res["j01"]
    assert len(j01_res["missing"]) == 0
    matched_names = [m["name"] for m in j01_res["matched"]]
    assert "React" in matched_names
    assert "TypeScript" in matched_names


@pytest.mark.asyncio
async def test_invalid_verdicts_retry_then_code_fallback():
    profile = CandidateProfile(
        status="ok",
        skills=["ReactJS", "Python"],
    )
    job_skills = {"j01": ["React", "Docker"]}

    # Scripted model returns bad references (referring to non-existent skills)
    bad_output = SkillMatchResult(
        job_verdicts={
            "j01": [
                JobSkillVerdict(job_skill="UnknownSkill", verdict="exact", cv_skill="NonExistent"),
            ]
        }
    )

    with override_skill_models({"match-skills": structured(bad_output)}):
        res, warnings = await match_skills_for_project(
            project_id="p01",
            project_jobs=job_skills,
            profile=profile,
        )

    # Must fall back to code fallback and record warning
    assert "SKILL_MATCH_FALLBACK" in warnings
    j01_res = res["j01"]
    # Code fallback normalises ReactJS -> React (matched), Docker is missing
    matched_names = [m["name"] for m in j01_res["matched"]]
    assert "React" in matched_names
    assert "Docker" in j01_res["missing"]


@pytest.mark.asyncio
async def test_one_call_per_project_with_boundary_tags():
    profile = CandidateProfile(
        status="ok",
        skills=["Python", "FastAPI"],
    )
    job_skills = {"j01": ["Python", "FastAPI"], "j02": ["Docker"]}

    mock_result = SkillMatchResult(
        job_verdicts={
            "j01": [
                JobSkillVerdict(job_skill="Python", verdict="exact", cv_skill="Python"),
                JobSkillVerdict(job_skill="FastAPI", verdict="exact", cv_skill="FastAPI"),
            ],
            "j02": [
                JobSkillVerdict(job_skill="Docker", verdict="missing"),
            ],
        }
    )

    with capture_model_requests() as captured:
        with override_skill_models({"match-skills": structured(mock_result)}):
            await match_skills_for_project(
                project_id="p01",
                project_jobs=job_skills,
                profile=profile,
            )

    # Exactly 1 request for the project
    assert len(captured) == 1
    prompt_str = str(captured[0])

    # Assert skill names sit inside boundary tags and NO description text is present
    assert "<candidate-skills" in prompt_str
    assert "</candidate-skills" in prompt_str
    assert "<project-jobs" in prompt_str
    assert "</project-jobs" in prompt_str
    # Ensure no project description leaked in
    assert "Ví điện tử với hơn 2 triệu" not in prompt_str
