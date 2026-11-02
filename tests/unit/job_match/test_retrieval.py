from app.features.job_match.ports import IndexHit
from app.features.job_match.retrieval import compute_exhausted, rrf_fuse


def test_rrf_k60_prefers_items_in_both_lists():
    # Item A is rank 5 in list 1, rank 5 in list 2
    # Item B is rank 1 in list 1, not in list 2
    # RRF score formula: sum(1.0 / (60 + rank))
    # Score A = 1/65 + 1/65 = 2/65 ≈ 0.03077
    # Score B = 1/61 + 0 ≈ 0.01639
    # Therefore A > B!
    list1 = [
        IndexHit(job_id="jB", project_id="pB", rank=1, score=1.0),
        IndexHit(job_id="jX", project_id="pX", rank=2, score=0.9),
        IndexHit(job_id="jY", project_id="pY", rank=3, score=0.8),
        IndexHit(job_id="jZ", project_id="pZ", rank=4, score=0.7),
        IndexHit(job_id="jA", project_id="pA", rank=5, score=0.6),
    ]
    list2 = [
        IndexHit(job_id="j1", project_id="p1", rank=1, score=1.0),
        IndexHit(job_id="j2", project_id="p2", rank=2, score=0.9),
        IndexHit(job_id="j3", project_id="p3", rank=3, score=0.8),
        IndexHit(job_id="j4", project_id="p4", rank=4, score=0.7),
        IndexHit(job_id="jA", project_id="pA", rank=5, score=0.6),
    ]

    fused = rrf_fuse([list1, list2], k=60)
    top_job_ids = [hit.job_id for hit in fused]
    assert top_job_ids[0] == "jA"
    assert "jB" in top_job_ids


def test_exhausted_when_all_lists_short():
    list_size = 10

    # Case 1: Every list returned fewer than list_size hits -> exhausted is True
    short_dense = [
        [IndexHit(job_id=f"jd_{i}", project_id=f"pd_{i}", rank=i, score=1.0) for i in range(5)],
        [IndexHit(job_id=f"jd2_{i}", project_id=f"pd2_{i}", rank=i, score=1.0) for i in range(8)],
    ]
    short_lex = [
        IndexHit(job_id=f"jl_{i}", project_id=f"pl_{i}", rank=i, score=1.0) for i in range(4)
    ]
    assert compute_exhausted(short_dense, short_lex, list_size=list_size) is True

    # Case 2: One dense list returned full list_size -> exhausted is False
    full_dense = [
        [IndexHit(job_id=f"jd_{i}", project_id=f"pd_{i}", rank=i, score=1.0) for i in range(10)],
    ]
    assert compute_exhausted(full_dense, short_lex, list_size=list_size) is False

    # Case 3: Lexical returned full list_size -> exhausted is False
    full_lex = [
        IndexHit(job_id=f"jl_{i}", project_id=f"pl_{i}", rank=i, score=1.0) for i in range(10)
    ]
    assert compute_exhausted(short_dense, full_lex, list_size=list_size) is False
