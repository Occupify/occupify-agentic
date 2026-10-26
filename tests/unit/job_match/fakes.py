from datetime import datetime, timezone
from typing import Any
from pydantic import BaseModel

from app.features.job_match.criteria import matches as criteria_matches
from app.features.job_match.ports import (
    IndexHit,
    IndexMeta,
    IndexRow,
    JobIndex,
    MatchCriteria,
    UpsertStats,
)


class FakeJobIndex:
    """In-memory fake implementation of JobIndex for unit tests."""

    def __init__(
        self,
        rows: list[IndexRow] | None = None,
        usable: bool = True,
        hits_override: tuple[list[list[IndexHit]], list[IndexHit]] | None = None,
    ):
        self._rows: dict[str, IndexRow] = {}
        if rows:
            for r in rows:
                self._rows[r.job_id] = r
        self._usable = usable
        self._hits_override = hits_override
        self.upsert_calls: list[list[IndexRow]] = []
        self.search_calls: list[dict[str, Any]] = []

    def set_usable(self, val: bool) -> None:
        self._usable = val

    def set_hits_override(self, val: tuple[list[list[IndexHit]], list[IndexHit]] | None) -> None:
        self._hits_override = val

    async def upsert(self, rows: list[IndexRow]) -> UpsertStats:
        self.upsert_calls.append(rows)
        ins = 0
        upd = 0
        for r in rows:
            if r.job_id in self._rows:
                upd += 1
            else:
                ins += 1
            self._rows[r.job_id] = r
        return UpsertStats(inserted=ins, updated=upd, reembed_queued=ins + upd, unchanged=0)

    async def hybrid_search(
        self,
        dense_queries: list[list[float]],
        lexical: str,
        criteria: MatchCriteria,
        top: int = 50,
    ) -> tuple[list[list[IndexHit]], list[IndexHit]]:
        self.search_calls.append({
            "dense_queries": dense_queries,
            "lexical": lexical,
            "criteria": criteria,
            "top": top,
        })
        if self._hits_override is not None:
            return self._hits_override

        # Filter by criteria and active status
        eligible_rows = [
            r for r in self._rows.values()
            if r.project_status == "OPEN" and r.job_status == "RECRUITING" and criteria_matches(criteria, r)
        ]

        # Lexical matching: simple keyword check on doc_text
        lex_tokens = [t.lower() for t in lexical.split() if t.strip()]
        lex_hits: list[IndexHit] = []
        for rank, r in enumerate(eligible_rows):
            doc_lower = r.doc_text.lower()
            score = sum(1.0 for t in lex_tokens if t in doc_lower) / max(len(lex_tokens), 1)
            if score > 0 or not lex_tokens:
                lex_hits.append(IndexHit(
                    job_id=r.job_id,
                    project_id=r.project_id,
                    rank=rank + 1,
                    score=float(score),
                ))

        # Sort and take top
        lex_hits.sort(key=lambda h: h.score, reverse=True)
        lex_hits = lex_hits[:top]

        # Dense matching simulation: produce top hits for each query
        dense_lists: list[list[IndexHit]] = []
        for _ in dense_queries:
            dense_hits = [
                IndexHit(
                    job_id=r.job_id,
                    project_id=r.project_id,
                    rank=idx + 1,
                    score=1.0 - (idx * 0.01),
                )
                for idx, r in enumerate(eligible_rows[:top])
            ]
            dense_lists.append(dense_hits)

        return dense_lists, lex_hits

    async def get_rows(self, job_ids: list[str]) -> list[IndexRow]:
        return [self._rows[jid] for jid in job_ids if jid in self._rows]

    async def mark_inactive(self, job_ids: list[str]) -> None:
        for jid in job_ids:
            if jid in self._rows:
                del self._rows[jid]

    async def meta(self) -> IndexMeta | None:
        return IndexMeta(
            embed_model="BAAI/bge-m3",
            dim=1024,
            source="mock",
            built_at=datetime.now(timezone.utc),
            jobs_n=len(self._rows),
        )

    def is_usable(self) -> bool:
        return self._usable and len(self._rows) > 0
