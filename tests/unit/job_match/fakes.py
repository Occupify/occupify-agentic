from datetime import UTC, datetime
from typing import Any

from app.features.job_match.criteria import matches as criteria_matches
from app.features.job_match.ports import (
    IndexHit,
    IndexMeta,
    IndexRow,
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
        self.search_calls.append(
            {
                "dense_queries": dense_queries,
                "lexical": lexical,
                "criteria": criteria,
                "top": top,
            }
        )
        if self._hits_override is not None:
            return self._hits_override

        # Filter by criteria and active status
        eligible_rows = [
            r
            for r in self._rows.values()
            if r.project_status == "OPEN"
            and r.job_status == "RECRUITING"
            and criteria_matches(criteria, r)
        ]

        # Lexical matching: simple keyword check on doc_text
        lex_tokens = [t.lower() for t in lexical.split() if t.strip()]
        lex_hits: list[IndexHit] = []
        for rank, r in enumerate(eligible_rows):
            doc_lower = r.doc_text.lower()
            score = sum(1.0 for t in lex_tokens if t in doc_lower) / max(len(lex_tokens), 1)
            if score > 0 or not lex_tokens:
                lex_hits.append(
                    IndexHit(
                        job_id=r.job_id,
                        project_id=r.project_id,
                        rank=rank + 1,
                        score=float(score),
                    )
                )

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
            doc_text_version="v1",
            built_at=datetime.now(UTC),
            jobs_n=len(self._rows),
        )

    def is_usable(self) -> bool:
        return self._usable and len(self._rows) > 0

    async def index_state(self) -> str:
        if not self._usable:
            return "mismatch"
        if len(self._rows) == 0:
            return "missing"
        return "ok"


def get_default_test_model(name: str) -> Any:
    from pydantic_ai.messages import ModelResponse, ToolCallPart
    from pydantic_ai.models.function import AgentInfo, FunctionModel

    from app.skill_schemas.candidate import CandidateProfile, RoleItem
    from app.skill_schemas.matching import (
        JobAssessment,
        ProjectAssessment,
        RequirementCheck,
        SkillMatchResult,
    )
    from app.skill_schemas.search import SearchDecision

    def fn(messages: list[Any], info: AgentInfo) -> ModelResponse:
        tool_name = info.output_tools[0].name if info.output_tools else "final_result"
        prompt_text = ""
        for m in messages:
            for part in getattr(m, "parts", []):
                if hasattr(part, "content") and isinstance(part.content, str):
                    prompt_text += part.content + "\n"

        if name == "extract-candidate-profile":
            known_skills = [
                "Java",
                "Spring Boot",
                "PostgreSQL",
                "Docker",
                "Git",
                "RESTful API",
                "Microservices",
                "Python",
                "FastAPI",
                "React",
                "NodeJS",
                "TypeScript",
                "SQL Optimization",
                "CI/CD",
                "JPA/Hibernate",
                "JUnit 5",
                "Mockito",
            ]
            found = [s for s in known_skills if s.lower() in prompt_text.lower()]
            if not found:
                import re

                lines = prompt_text.splitlines()
                for line in lines:
                    m_line = re.match(r"^\s*-\s*([^:]+)", line)
                    if m_line:
                        found.append(m_line.group(1).strip())
            if not found:
                found = ["Java", "Spring Boot", "PostgreSQL"]

            target_roles = (
                ["Backend Developer"]
                if any(s in found for s in ["Java", "Python", "Spring Boot"])
                else ["Software Engineer"]
            )
            profile = CandidateProfile(
                status="ok",
                language="vi",
                skills=found,
                roles=[
                    RoleItem(
                        title="Senior Backend Engineer",
                        skills_used=found[:5],
                    )
                ],
                target_roles=target_roles,
            )
            return ModelResponse(parts=[ToolCallPart(tool_name, profile.model_dump(mode="json"))])

        elif name == "match-skills":
            import re

            c_skills = []
            m_c = re.search(r"<candidate-skills>(.*?)</candidate-skills>", prompt_text, re.DOTALL)
            if m_c:
                for line in m_c.group(1).splitlines():
                    cleaned_line = line.strip().lstrip("- ").strip()
                    if cleaned_line:
                        c_skills.append(cleaned_line)

            job_verdicts: dict[str, list[dict[str, Any]]] = {}
            m_pj = re.search(r"<project-jobs>(.*?)</project-jobs>", prompt_text, re.DOTALL)
            if m_pj:
                current_job = None
                for line in m_pj.group(1).splitlines():
                    m_job = re.match(r"Job\s+([^\s:]+):", line.strip())
                    if m_job:
                        current_job = m_job.group(1)
                        job_verdicts[current_job] = []
                    elif current_job:
                        m_sk = re.match(r"-\s+(.+)$", line.strip())
                        if m_sk:
                            sk = m_sk.group(1).strip()
                            matched_cv = None
                            for cs in c_skills:
                                if (
                                    cs.lower() == sk.lower()
                                    or sk.lower() in cs.lower()
                                    or cs.lower() in sk.lower()
                                ):
                                    matched_cv = cs
                                    break
                            if matched_cv:
                                job_verdicts[current_job].append(
                                    {
                                        "job_skill": sk,
                                        "verdict": "exact",
                                        "cv_skill": matched_cv,
                                    }
                                )
                            else:
                                job_verdicts[current_job].append(
                                    {
                                        "job_skill": sk,
                                        "verdict": "missing",
                                        "cv_skill": None,
                                    }
                                )

            result = SkillMatchResult(job_verdicts=job_verdicts)
            return ModelResponse(parts=[ToolCallPart(tool_name, result.model_dump(mode="json"))])

        elif name == "assess-job-fit":
            import re

            jobs_found = re.findall(r"-\s*Job\s+([^\s:]+)", prompt_text)
            if not jobs_found:
                jobs_found = ["j1"]

            jobs_asmts = []
            for jid in jobs_found:
                req_refs = re.findall(rf"({jid.upper()}\.[RD]\d*)", prompt_text)
                req_checks = [
                    RequirementCheck(
                        ref=r,
                        req_id=r,
                        status="met",
                        note="Candidate profile demonstrates capability.",
                    )
                    for r in req_refs
                ]
                if not req_checks:
                    req_checks = [
                        RequirementCheck(
                            ref=f"{jid.upper()}.D",
                            req_id=f"{jid.upper()}.D",
                            status="met",
                            note="Fits requirements.",
                        )
                    ]

                jobs_asmts.append(
                    JobAssessment(
                        job=jid,
                        job_id=jid,
                        requirements=req_checks,
                        summary="Candidate demonstrates strong experience aligned with role requirements.",
                    )
                )

            asmt = ProjectAssessment(jobs=jobs_asmts)
            return ModelResponse(parts=[ToolCallPart(tool_name, asmt.model_dump(mode="json"))])

        elif name == "plan-job-search":
            decision = SearchDecision(action="done", reason="Goal reached or catalog exhausted")
            return ModelResponse(parts=[ToolCallPart(tool_name, decision.model_dump(mode="json"))])

        return ModelResponse(parts=[ToolCallPart(tool_name, {})])

    return FunctionModel(fn)


def default_test_overrides() -> dict[str, Any]:
    return {
        "extract-candidate-profile": get_default_test_model("extract-candidate-profile"),
        "match-skills": get_default_test_model("match-skills"),
        "assess-job-fit": get_default_test_model("assess-job-fit"),
        "plan-job-search": get_default_test_model("plan-job-search"),
    }
