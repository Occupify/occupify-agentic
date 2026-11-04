import math
from typing import Any


def recall_at_k(retrieved: list[str], relevant: list[str], k: int) -> float:
    """Recall@K = |Retrieved@K ∩ Relevant| / |Relevant|

    If relevant is empty, returns 0.0 (or 1.0 if both empty; here 0.0).
    """
    if not relevant or k <= 0:
        return 0.0
    retrieved_k = set(retrieved[:k])
    relevant_set = set(relevant)
    hits = len(retrieved_k & relevant_set)
    return hits / len(relevant_set)


def precision_at_k(retrieved: list[str], relevant: list[str], k: int) -> float:
    """Precision@K = |Retrieved@K ∩ Relevant| / K

    If k <= 0, returns 0.0.
    """
    if k <= 0:
        return 0.0
    retrieved_k = retrieved[:k]
    if not retrieved_k:
        return 0.0
    relevant_set = set(relevant)
    hits = sum(1 for item in retrieved_k if item in relevant_set)
    return hits / k


def mrr(retrieved: list[str], relevant: list[str]) -> float:
    """Mean Reciprocal Rank (MRR) for a single query.

    Returns 1.0 / rank of the first relevant item in retrieved (1-indexed).
    If no relevant item is found, returns 0.0.
    """
    if not relevant or not retrieved:
        return 0.0
    relevant_set = set(relevant)
    for rank, item in enumerate(retrieved, start=1):
        if item in relevant_set:
            return 1.0 / rank
    return 0.0


def ndcg_at_k(retrieved: list[str], relevant: list[str], k: int) -> float:
    """Normalized Discounted Cumulative Gain (nDCG@K) with binary relevance.

    DCG@K = sum_{i=1}^K rel_i / log2(i + 1)
    IDCG@K = sum_{i=1}^{min(K, |relevant|)} 1.0 / log2(i + 1)
    nDCG@K = DCG@K / IDCG@K
    """
    if not relevant or k <= 0 or not retrieved:
        return 0.0
    relevant_set = set(relevant)

    dcg = 0.0
    for i, item in enumerate(retrieved[:k], start=1):
        rel = 1.0 if item in relevant_set else 0.0
        dcg += rel / math.log2(i + 1)

    idcg = 0.0
    ideal_count = min(k, len(relevant_set))
    for i in range(1, ideal_count + 1):
        idcg += 1.0 / math.log2(i + 1)

    if idcg == 0.0:
        return 0.0
    return dcg / idcg


def citation_precision(
    citations: list[dict[str, Any] | Any], retrieved_chunk_ids: list[str]
) -> float:
    """Citation Precision / Faithfulness:
    Checks if citations point only to chunks actually retrieved (zero fabricated citations).
    Returns |Valid Citations| / |Total Citations|. If citations is empty, returns 1.0.
    """
    if not citations:
        return 1.0

    valid_chunks = set(retrieved_chunk_ids)
    valid_count = 0
    for c in citations:
        chunk_id = c.get("chunk_id") if isinstance(c, dict) else getattr(c, "chunk_id", None)
        if chunk_id and chunk_id in valid_chunks:
            valid_count += 1

    return valid_count / len(citations)


def abstention_accuracy(predicted_abstain: bool, expected_abstain: bool) -> float:
    """Abstention Accuracy: 1.0 if predicted matches expected, else 0.0."""
    return 1.0 if bool(predicted_abstain) == bool(expected_abstain) else 0.0
