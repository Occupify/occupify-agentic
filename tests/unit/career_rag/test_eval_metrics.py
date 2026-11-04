import math

import pytest

from evals.uc1.metrics import (
    abstention_accuracy,
    citation_precision,
    mrr,
    ndcg_at_k,
    precision_at_k,
    recall_at_k,
)


def test_recall_at_k():
    retrieved = ["c1", "c2", "c3", "c4"]
    relevant = ["c2", "c4", "c5"]

    # K = 1: retrieved=["c1"] -> hits=0 -> 0/3 = 0.0
    assert recall_at_k(retrieved, relevant, k=1) == 0.0

    # K = 2: retrieved=["c1", "c2"] -> hits=1 ("c2") -> 1/3
    assert recall_at_k(retrieved, relevant, k=2) == pytest.approx(1 / 3)

    # K = 4: hits={"c2", "c4"} -> 2/3
    assert recall_at_k(retrieved, relevant, k=4) == pytest.approx(2 / 3)

    # Edge cases
    assert recall_at_k([], relevant, k=5) == 0.0
    assert recall_at_k(retrieved, [], k=5) == 0.0
    assert recall_at_k(retrieved, relevant, k=0) == 0.0


def test_precision_at_k():
    retrieved = ["c1", "c2", "c3", "c4"]
    relevant = ["c2", "c4"]

    # K = 1: ["c1"] -> 0/1 = 0.0
    assert precision_at_k(retrieved, relevant, k=1) == 0.0

    # K = 2: ["c1", "c2"] -> 1/2 = 0.5
    assert precision_at_k(retrieved, relevant, k=2) == 0.5

    # K = 4: ["c1", "c2", "c3", "c4"] -> 2/4 = 0.5
    assert precision_at_k(retrieved, relevant, k=4) == 0.5

    # Edge cases
    assert precision_at_k([], relevant, k=3) == 0.0
    assert precision_at_k(retrieved, relevant, k=0) == 0.0


def test_mrr():
    relevant = ["target_chunk"]

    # Rank 1
    assert mrr(["target_chunk", "other"], relevant) == 1.0

    # Rank 2
    assert mrr(["other", "target_chunk"], relevant) == 0.5

    # Rank 3
    assert mrr(["a", "b", "target_chunk"], relevant) == pytest.approx(1 / 3)

    # Not found
    assert mrr(["a", "b"], relevant) == 0.0

    # Edge cases
    assert mrr([], relevant) == 0.0
    assert mrr(["a"], []) == 0.0


def test_ndcg_at_k():
    retrieved = ["doc1", "doc2", "doc3"]
    # Perfect ranking: first doc is relevant
    assert ndcg_at_k(retrieved, ["doc1"], k=3) == 1.0

    # Second doc is relevant:
    # DCG = 1 / log2(2 + 1) = 1 / 1.58496 = 0.6309
    # IDCG = 1 / log2(1 + 1) = 1.0
    # nDCG = 0.6309 / 1.0
    expected_ndcg = (1.0 / math.log2(3)) / (1.0 / math.log2(2))
    assert ndcg_at_k(retrieved, ["doc2"], k=3) == pytest.approx(expected_ndcg)

    # Edge cases
    assert ndcg_at_k([], ["doc1"], k=3) == 0.0
    assert ndcg_at_k(retrieved, [], k=3) == 0.0
    assert ndcg_at_k(retrieved, ["doc4"], k=3) == 0.0


def test_citation_precision():
    retrieved = ["chunk_1", "chunk_2", "chunk_3"]

    # All citations valid
    citations = [{"chunk_id": "chunk_1"}, {"chunk_id": "chunk_2"}]
    assert citation_precision(citations, retrieved) == 1.0

    # One fabricated citation
    citations_with_fake = [{"chunk_id": "chunk_1"}, {"chunk_id": "fake_chunk"}]
    assert citation_precision(citations_with_fake, retrieved) == 0.5

    # Empty citations -> 1.0 (no false citation made)
    assert citation_precision([], retrieved) == 1.0


def test_abstention_accuracy():
    assert abstention_accuracy(True, True) == 1.0
    assert abstention_accuracy(False, False) == 1.0
    assert abstention_accuracy(True, False) == 0.0
    assert abstention_accuracy(False, True) == 0.0
