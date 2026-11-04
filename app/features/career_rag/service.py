import logging

from sqlalchemy.ext.asyncio import AsyncSession

from app.features.career_rag.rerank import CareerKnowledgeReranker
from app.features.career_rag.retrieval import CareerKnowledgeRetriever, RetrievalHit
from app.features.career_rag.schemas import (
    CareerRecommendation,
    Citation,
    GroundedCareerResponse,
)
from app.ml.embedder import Embedder
from app.ml.fakes import FakeEmbedder, FakeReranker
from app.ml.reranker import Reranker

logger = logging.getLogger(__name__)

# Minimum cross-encoder rerank score or RRF score threshold to accept chunk as sufficient evidence
DEFAULT_CONFIDENCE_THRESHOLD = 0.35


class CareerConsultantService:
    """Orchestrates hybrid retrieval, cross-encoder reranking, and grounded response generation.

    Adheres strictly to doc/rule.md:
    - Rule 5.44: Grounded recommendations supported by evidence or labeled as tentative reasoning.
    - Rule 5.45: Zero hallucinated citations, titles, or URLs.
    - Rule 5.46: Citations point strictly to actual chunks retrieved.
    - Rule 5.47: Claims traceable to supporting evidence.
    - Rule 5.48: Disclose conflicting sources when detected across jurisdictions/sources.
    - Rule 5.49: Clean abstention when evidence is missing or confidence is below threshold.
    - Rule 5.50: Clean markdown separation between verified facts and recommendations.
    """

    def __init__(
        self,
        session: AsyncSession,
        embedder: Embedder | FakeEmbedder | None = None,
        reranker: Reranker | FakeReranker | None = None,
        confidence_threshold: float = DEFAULT_CONFIDENCE_THRESHOLD,
    ) -> None:
        self.session = session
        self.retriever = CareerKnowledgeRetriever(session=session, embedder=embedder)
        self.reranker = CareerKnowledgeReranker(reranker=reranker)
        self.confidence_threshold = confidence_threshold

    async def consult(
        self,
        query: str,
        domain: str | None = None,
        source_type: str | None = None,
        source_id: str | None = None,
        top_k: int = 15,
        rerank_top_n: int = 5,
    ) -> GroundedCareerResponse:
        """Retrieves knowledge chunks, reranks them, and builds a grounded career response."""
        trimmed_query = query.strip() if query else ""
        if not trimmed_query:
            return self._build_abstention(
                reason="Query is empty.",
                user_msg="Vui lòng cung cấp câu hỏi hoặc chủ đề nghề nghiệp cụ thể để tôi có thể hỗ trợ tra cứu thông tin chính xác.",
            )

        # 1. Retrieve candidates via Hybrid Search (Vector + Full-text BM25 / RRF)
        candidates = await self.retriever.search_hybrid(
            query=trimmed_query,
            top_k=top_k,
            domain=domain,
            source_type=source_type,
            source_id=source_id,
        )

        if not candidates:
            return self._build_abstention(
                reason="No candidate knowledge chunks found for query.",
                user_msg=(
                    "Hiện tại hệ thống cơ sở tri thức nghề nghiệp chưa có thông tin chính thức phù hợp với yêu cầu: "
                    f"**{trimmed_query}**. Bạn có thể thử tìm kiếm với chức danh hoặc bộ kỹ năng chuẩn (như Backend, Frontend, DevOps, Data Engineer...)."
                ),
            )

        # 2. Rerank candidates with Cross-Encoder
        ranked_hits = self.reranker.rerank(
            query=trimmed_query,
            candidates=candidates,
            top_n=rerank_top_n,
        )

        if not ranked_hits:
            return self._build_abstention(
                reason="Reranker returned zero candidates.",
                user_msg="Không tìm thấy tài liệu phù hợp sau khi xếp hạng độ tin cậy.",
            )

        # 3. Check evidence sufficiency (Rule 5.49)
        top_score = ranked_hits[0].rerank_score
        if top_score is None:
            top_score = ranked_hits[0].score

        if top_score < self.confidence_threshold:
            return self._build_abstention(
                reason=f"Top candidate score {top_score:.3f} below confidence threshold {self.confidence_threshold:.3f}.",
                user_msg=(
                    f"Thông tin trong hệ thống chưa đủ độ tin cậy để đưa ra kết luận chắc chắn về: **{trimmed_query}** "
                    f"(độ tương đồng cao nhất: {top_score:.2f} < ngưỡng yêu cầu {self.confidence_threshold:.2f}). "
                    "Tôi xin phép không đưa ra suy đoán chưa được kiểm chứng. Bạn có thể diễn đạt cụ thể hơn hoặc cung cấp thêm ngữ cảnh."
                ),
            )

        # 4. Filter only hits meeting a minimum threshold for citation
        valid_evidence_hits = [
            h
            for h in ranked_hits
            if (h.rerank_score or h.score) >= (self.confidence_threshold * 0.8)
        ]
        if not valid_evidence_hits:
            valid_evidence_hits = ranked_hits[:1]

        # 5. Build citations strictly pointing to the retrieved chunks
        citations: list[Citation] = []
        citations_by_chunk_id: dict[str, Citation] = {}

        for hit in valid_evidence_hits:
            snippet = self._make_snippet(hit.content)
            cit = Citation(
                chunk_id=hit.chunk_id,
                source_id=hit.source_id,
                source_record_id=hit.source_record_id,
                title=hit.title,
                source_url=hit.source_url,
                snippet=snippet,
            )
            citations.append(cit)
            citations_by_chunk_id[hit.chunk_id] = cit

        # 6. Check for conflicting sources across geographies/sources (Rule 5.48)
        conflicts = self._detect_conflicting_sources(valid_evidence_hits)

        # 7. Grounded Recommendations formulation (Rule 5.44, 5.50)
        recommendations = self._formulate_recommendations(
            valid_evidence_hits, citations_by_chunk_id
        )

        # 8. Synthesize grounded answer markdown with citation footnotes
        answer_text = self._synthesize_answer(
            query=trimmed_query,
            recommendations=recommendations,
            citations=citations,
            conflicts=conflicts,
        )

        return GroundedCareerResponse(
            answer=answer_text,
            recommendations=recommendations,
            citations=citations,
            abstention=False,
            abstention_reason=None,
            conflicting_sources=conflicts,
        )

    def _build_abstention(self, reason: str, user_msg: str) -> GroundedCareerResponse:
        return GroundedCareerResponse(
            answer=user_msg,
            recommendations=[],
            citations=[],
            abstention=True,
            abstention_reason=reason,
            conflicting_sources=[],
        )

    def _make_snippet(self, text: str, max_chars: int = 240) -> str:
        clean_text = " ".join(text.replace("\n", " ").split())
        if len(clean_text) <= max_chars:
            return clean_text
        return clean_text[: max_chars - 3].rstrip() + "..."

    def _detect_conflicting_sources(self, hits: list[RetrievalHit]) -> list[str]:
        """Detects whether different authorities present contrasting scopes (e.g. ESCO vs O*NET)."""
        sources = {h.source_id for h in hits}
        conflicts = []
        if "esco" in sources and "onet" in sources:
            conflicts.append(
                "Phát hiện sự khác biệt hệ quy chiếu giữa Tiêu chuẩn nghề nghiệp Châu Âu (ESCO) và Tiêu chuẩn Hoa Kỳ (O*NET). "
                "Yêu cầu kỹ năng và phân loại nghề nghiệp có thể khác nhau tùy khu vực địa lý."
            )
        return conflicts

    def _formulate_recommendations(
        self,
        hits: list[RetrievalHit],
        citations_by_chunk_id: dict[str, Citation],
    ) -> list[CareerRecommendation]:
        """Formulates claims backed by citations with appropriate confidence levels."""
        recommendations: list[CareerRecommendation] = []

        for hit in hits:
            cit = citations_by_chunk_id.get(hit.chunk_id)
            evidence = [cit] if cit else []
            score = hit.rerank_score if hit.rerank_score is not None else hit.score

            if score >= 0.7:
                confidence = "high"
            elif score >= self.confidence_threshold:
                confidence = "medium"
            else:
                confidence = "tentative_reasoning"

            # Formulate claim based on source type
            if hit.source_type == "learning_roadmap":
                claim = f"Lộ trình đề xuất theo chuẩn Roadmap: {hit.title}"
            elif hit.source_type == "occupation_taxonomy":
                claim = f"Tiêu chuẩn nghề nghiệp & định nghĩa: {hit.title}"
            elif hit.source_type == "skill_competency":
                claim = f"Yêu cầu năng lực & kỹ năng thiết yếu: {hit.title}"
            else:
                claim = f"Thông tin tri thức nghề nghiệp: {hit.title}"

            recommendations.append(
                CareerRecommendation(
                    claim=claim,
                    evidence_citations=evidence,
                    confidence_level=confidence,
                )
            )

        return recommendations

    def _synthesize_answer(
        self,
        query: str,
        recommendations: list[CareerRecommendation],
        citations: list[Citation],
        conflicts: list[str],
    ) -> str:
        """Synthesizes structured Markdown with verified facts, tentative reasoning, and citation footnotes."""
        lines: list[str] = []
        lines.append(f"### Tư vấn lộ trình & tiêu chuẩn nghề nghiệp: {query}\n")

        # Disclose conflicting sources if present (Rule 5.48)
        if conflicts:
            lines.append("> ⚠️ **Lưu ý khác biệt nguồn chuẩn hóa:**")
            for c in conflicts:
                lines.append(f"> - {c}")
            lines.append("")

        # Section 1: Verified facts & structured recommendations
        verified = [r for r in recommendations if r.confidence_level in ("high", "medium")]
        tentative = [r for r in recommendations if r.confidence_level == "tentative_reasoning"]

        if verified:
            lines.append("#### 📌 Thông tin chuẩn hóa từ nguồn dữ liệu:")
            for idx, rec in enumerate(verified, start=1):
                citation_tags = "".join(f" [{cit.source_id}]" for cit in rec.evidence_citations)
                badge = (
                    "*(Độ tin cậy: Cao)*"
                    if rec.confidence_level == "high"
                    else "*(Độ tin cậy: Trung bình)*"
                )
                lines.append(f"{idx}. **{rec.claim}** {badge}{citation_tags}")
                for cit in rec.evidence_citations:
                    lines.append(f'   - *Trích dẫn:* "{cit.snippet}"')
            lines.append("")

        if tentative:
            lines.append("#### 💡 Gợi ý suy luận bổ sung (Tentative Reasoning):")
            for rec in tentative:
                lines.append(
                    f"- **{rec.claim}** *(Suy luận dựa trên ngữ cảnh tương đồng, cần tham chiếu thêm)*"
                )
            lines.append("")

        # Section 2: Traceable Citations Footnote Table (Rule 5.46)
        if citations:
            lines.append("---")
            lines.append("#### 📚 Nguồn trích dẫn (Citations):")
            for idx, cit in enumerate(citations, start=1):
                url_display = f" [Xem nguồn]({cit.source_url})" if cit.source_url else ""
                lines.append(
                    f"- `[{idx}]` **{cit.title}** ({cit.source_id} / ID: `{cit.source_record_id}`){url_display}\n"
                    f"  > *Chunk ID:* `{cit.chunk_id}`\n"
                    f'  > *Nội dung:* "{cit.snippet}"'
                )

        return "\n".join(lines)
