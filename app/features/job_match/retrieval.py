from typing import Any

from app.features.job_match.ports import IndexHit
from app.skill_schemas.candidate import CandidateProfile


def build_queries(profile: CandidateProfile) -> tuple[str, list[str], str]:
    """
    Constructs multi-query representations from candidate profile:
    - Q0: Main comprehensive query combining target roles, skills, and past titles
    - queries: [Q0] + individual queries for each target role
    - lexical: Disjunction (OR) of candidate skills and role titles
    """
    skill_names: list[str] = []
    for s in profile.skills:
        if isinstance(s, str):
            skill_names.append(s)
        elif hasattr(s, "name"):
            skill_names.append(s.name)

    role_titles: list[str] = [r.title for r in profile.roles if hasattr(r, "title")]
    target_roles: list[str] = profile.target_roles or []

    all_terms = target_roles + skill_names + role_titles
    q0 = " ".join(all_terms).strip()

    queries = [q0] if q0 else []
    for tr in target_roles:
        if tr and tr not in queries:
            queries.append(tr)

    lexical_terms = [t.strip() for t in (skill_names + role_titles) if t.strip()]
    lexical = " OR ".join(lexical_terms) if lexical_terms else ""

    return q0, queries, lexical


def rrf_fuse(hit_lists: list[list[IndexHit]], k: int = 60) -> list[IndexHit]:
    """
    Reciprocal Rank Fusion (RRF) across multiple search hit lists:
    Score(d) = sum_{m} 1.0 / (k + rank_m(d))
    """
    rrf_scores: dict[str, float] = {}
    hit_map: dict[str, IndexHit] = {}

    for hits in hit_lists:
        for idx, hit in enumerate(hits):
            # Use hit.rank or list position (1-based)
            rank = hit.rank if hit.rank > 0 else (idx + 1)
            rrf_scores[hit.job_id] = rrf_scores.get(hit.job_id, 0.0) + (1.0 / (k + rank))
            if hit.job_id not in hit_map:
                hit_map[hit.job_id] = hit

    sorted_job_ids = sorted(rrf_scores.keys(), key=lambda jid: rrf_scores[jid], reverse=True)

    fused_hits: list[IndexHit] = []
    for new_rank, jid in enumerate(sorted_job_ids, start=1):
        orig_hit = hit_map[jid]
        fused_hits.append(
            IndexHit(
                job_id=orig_hit.job_id,
                project_id=orig_hit.project_id,
                rank=new_rank,
                score=rrf_scores[jid],
            )
        )
    return fused_hits


def compute_exhausted(
    dense_lists: list[list[Any]],
    lex_hits: list[Any],
    list_size: int = 50,
) -> bool:
    """
    Exhausted is True when every retrieval list returned fewer than list_size items,
    indicating that there are no further uninspected candidates matching the filters.
    """
    for d_list in dense_lists:
        if len(d_list) >= list_size:
            return False
    if len(lex_hits) >= list_size:
        return False
    return True
