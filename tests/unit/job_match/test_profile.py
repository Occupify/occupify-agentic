from app.features.job_match.profile import map_profile_to_outcome
from app.skill_schemas.candidate import CandidateProfile


def test_profile_status_maps_to_outcome():
    # 1. Status not ok -> INSUFFICIENT_PROFILE
    p_insufficient = CandidateProfile(
        status="insufficient",
        skills=["Python", "FastAPI"],
    )
    assert map_profile_to_outcome(p_insufficient) == "INSUFFICIENT_PROFILE"

    # 2. Fewer than 2 skills -> INSUFFICIENT_PROFILE
    p_one_skill = CandidateProfile(
        status="ok",
        skills=["Python"],
    )
    assert map_profile_to_outcome(p_one_skill) == "INSUFFICIENT_PROFILE"

    # 3. Status ok with >= 2 skills -> OK
    p_ok = CandidateProfile(
        status="ok",
        skills=["Python", "FastAPI", "Docker"],
    )
    assert map_profile_to_outcome(p_ok) == "OK"
