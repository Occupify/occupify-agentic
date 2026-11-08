from app.features.career_rag.retrieval import RetrievalHit
from app.ml.fakes import FakeReranker
from app.ml.reranker import Reranker


class CareerKnowledgeReranker:
    """Reranks candidate chunks using cross-encoder reranker model.

    Retains retrieval diagnostics (initial vector rank, initial keyword rank,
    initial RRF score, rerank score) for auditability (rule.md Rule 4.39).
    """

    def __init__(self, reranker: Reranker | FakeReranker | None = None) -> None:
        self._reranker = reranker

    def _get_reranker(self) -> Reranker | FakeReranker:
        if self._reranker is None:
            self._reranker = Reranker()
        return self._reranker

    def rerank(
        self,
        query: str,
        candidates: list[RetrievalHit],
        top_n: int = 10,
    ) -> list[RetrievalHit]:
        """Reranks candidates against the query and updates scores and diagnostics."""
        if not candidates:
            return []

        reranker = self._get_reranker()

        # Build query-doc pairs for reranking
        pairs = [(query, f"{c.title}\n{c.content}") for c in candidates]

        if hasattr(reranker, "score_batch"):
            scores = reranker.score_batch(pairs)
        else:
            scores = [reranker.score(q, d) for q, d in pairs]

        scored_candidates: list[RetrievalHit] = []
        for cand, score in zip(candidates, scores):
            # Clone candidate to avoid mutating unexpected state
            updated = cand.model_copy(deep=True)
            updated.rerank_score = float(score)
            updated.score = float(score)
            scored_candidates.append(updated)

        # Sort descending by rerank score
        scored_candidates.sort(key=lambda x: x.rerank_score or 0.0, reverse=True)

        return scored_candidates[:top_n]
