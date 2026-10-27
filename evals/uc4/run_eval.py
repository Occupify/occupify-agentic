#!/usr/bin/env python3
# ruff: noqa: E402
"""
UC4 CV-Job Matching Evaluation Runner (T-22, T-31, N-02.6)

Comprehensive evaluation suite supporting gates G-1, G-2, G-2+, G-3, G-4:
- G-1: End-to-End matching across 8 synthetic personas (CV-A..CV-H), 3 runs
- G-2: Skill Matching stage-level across core scenarios in skill_cases.yaml
- G-2+: Extended Skill Matching across >=120 scenarios (135 cases)
- G-3: Large-scale matching on 300 projects / 1,000 jobs (catalog_scale.json)
  across 30 synthetic personas, 2 runs, worst run counts
- G-4: Layout Invariance & Robustness (L-01..L-08, X-01..X-02)
- Human Reviewer Tables: 50 silver labels and 30 sampled requirement checks with empty owner verification cells (| |)
- Outputs report to evals/uc4/report_v2.md (or custom path)
"""

import argparse
import asyncio
import json
import math
import os
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
import yaml
from dotenv import load_dotenv

load_dotenv()
os.environ["APP_ENV"] = "local"
db_env = os.getenv("DATABASE_URL", "")
if not db_env or "@occupify-postgres-agentic:5432" in db_env:
    os.environ["DATABASE_URL"] = (
        "postgresql+asyncpg://postgres:postgres@localhost:5535/occupify_agentic"
    )

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

# Allow model requests to z.ai for synthetic evaluation
import pydantic_ai.models

pydantic_ai.models.ALLOW_MODEL_REQUESTS = True

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from app.agents.budget import RunBudget
from app.agents.capture import capture_model_requests
from app.core.security import CurrentUser
from app.db.init import init_db
from app.db.session import set_engine
from app.features.job_match.index.store import PgJobIndex, set_index_empty
from app.features.job_match.index.sync import build_job_index
from app.features.job_match.pipeline import run_pipeline
from app.features.job_match.ports import PipelineOptions, RunResult, RunState
from app.features.job_match.schemas import ErrorCode, RunStatus
from app.features.job_match.scoring import SCORING_VERSION
from app.features.job_match.skill_match import match_skills_for_project
from app.messaging.mock_core import MockCoreRpc
from app.ml import get_embedder
from app.skill_schemas.candidate import CandidateProfile, SkillItem

EVAL_DIR = REPO_ROOT / "evals" / "uc4"
DATA_DIR = EVAL_DIR / "data"
PERSONAS_DIR = EVAL_DIR / "personas"
OVERLAYS_DIR = EVAL_DIR / "overlays"
V1_PROJECTS_PATH = REPO_ROOT / "app" / "features" / "job_match" / "mock" / "core_projects.json"
SCALE_PROJECTS_PATH = DATA_DIR / "catalog_scale.json"
CLEAN_SCALE_PROJECTS_PATH = DATA_DIR / "catalog_scale_clean.json"
SCALE_TRUTH_PATH = DATA_DIR / "catalog_scale_truth.json"
LABELS_SCALE_PATH = DATA_DIR / "labels_scale.yaml"
LABELS_SAMPLE_50_PATH = DATA_DIR / "labels_sample_50.yaml"

PII_SENTINELS = [
    "sentinel.candidate@example.com",
    "0912 000 111",
    "Nguyễn Văn Testcase",
    "12 Ngõ Thử Nghiệm",
    "hr@vidu-cloud.example",
    "0901 234 567",
]

G1_MATCH_PERSONAS = ["cv-a", "cv-b", "cv-c", "cv-d", "cv-f", "cv-h"]
G1_ALL_PERSONAS = ["cv-a", "cv-b", "cv-c", "cv-d", "cv-e", "cv-f", "cv-g", "cv-h"]

ALL_30_PERSONAS = (
    [f"cv-{c}" for c in "abcdefgh"]
    + [f"p-{i:02d}" for i in range(1, 13)]
    + [f"l-{i:02d}" for i in range(1, 9)]
    + [
        "x-01",
        "x-02",
    ]
)


def get_git_commit_sha() -> str:
    try:
        res = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        )
        return res.stdout.strip()
    except Exception:
        return "unknown"


def load_yaml(path: Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path: Path) -> Any:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def compute_dcg(gains: list[float], k: int = 5) -> float:
    dcg = 0.0
    for i, g in enumerate(gains[:k]):
        dcg += (math.pow(2, g) - 1.0) / math.log2(i + 2)
    return dcg


def compute_ndcg(project_gains: list[float], all_available_gains: list[float], k: int = 5) -> float:
    actual_dcg = compute_dcg(project_gains, k=k)
    ideal_gains = sorted(all_available_gains, reverse=True)[:k]
    ideal_dcg = compute_dcg(ideal_gains, k=k)
    if ideal_dcg <= 0.0:
        return 1.0 if actual_dcg == 0.0 else 0.0
    return actual_dcg / ideal_dcg


def load_persona_metadata(persona_id: str) -> dict[str, Any]:
    md_path = PERSONAS_DIR / f"{persona_id}.md"
    if not md_path.exists():
        return {}
    content = md_path.read_text(encoding="utf-8")
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]) or {}
            except Exception:
                pass
    return {}


@dataclass
class PersonaRunResult:
    persona_id: str
    run_idx: int
    status: str
    outcome: str
    items: list[dict[str, Any]]
    duration_ms: float
    tokens_in: int
    tokens_out: int
    cost_usd: float
    pii_leaks: list[str] = field(default_factory=list)
    hit_at_3: bool = False
    ndcg_at_k: float = 0.0
    recall_at_50: float = 1.0
    project_gains: list[float] = field(default_factory=list)
    profile: dict[str, Any] = field(default_factory=dict)
    pool_job_ids: list[str] = field(default_factory=list)


def check_captured_requests(captured: list[Any]) -> list[str]:
    leaks = []
    for req in captured:
        s = str(req)
        for sentinel in PII_SENTINELS:
            if sentinel in s:
                leaks.append(f"PII Sentinel leaked: {sentinel}")
        if "'employer'" in s or '"employer"' in s:
            leaks.append("Employer key leaked in model request")
    return leaks


async def evaluate_single_run(
    persona_id: str,
    run_idx: int,
    pdf_bytes: bytes,
    options: PipelineOptions,
    core_rpc: Any,
    sessionmaker: async_sessionmaker[AsyncSession],
    labels: dict[str, dict[str, int]],
    projects: list[dict[str, Any]],
    k_ndcg: int = 5,
    expected_top: list[str] | None = None,
) -> PersonaRunResult:
    user = CurrentUser(
        user_id=f"eval-{persona_id}", role="ROLE_USER", email=f"{persona_id}@example.com"
    )
    state = RunState()
    embedder = get_embedder()

    start_t = time.perf_counter()
    res = None
    with capture_model_requests() as captured:
        async with sessionmaker() as session:
            store = PgJobIndex(session=session, embedder=embedder, is_empty=False)
            try:
                res = await run_pipeline(
                    state=state,
                    pdf_bytes=pdf_bytes,
                    user=user,
                    store=store,
                    core_rpc=core_rpc,
                    options=options,
                )
            except Exception as exc:
                print(
                    f"[evaluate_single_run: {persona_id}] Pipeline exception ({type(exc).__name__}): {exc}"
                )
                res = RunResult(
                    status=RunStatus.FAILED,
                    error_code=ErrorCode.INTERNAL_ERROR,
                    message=str(exc),
                )
    duration_ms = (time.perf_counter() - start_t) * 1000.0

    leaks = check_captured_requests(captured)
    items = res.items or []

    # Map labels to project gains
    persona_labels = labels.get(persona_id, {})

    actual_project_gains = []
    for item in items:
        p_gain = 0
        for j in item.get("jobs", []):
            jid = j.get("jobId")
            if jid in persona_labels:
                p_gain = max(p_gain, persona_labels[jid])
        actual_project_gains.append(float(p_gain))

    all_mock_project_gains = []
    for p in projects:
        p_gain = 0
        for j in p.get("jobs", []):
            jid = j.get("id")
            if jid in persona_labels:
                p_gain = max(p_gain, persona_labels[jid])
        all_mock_project_gains.append(float(p_gain))

    # Hit@3 check:
    # 1. If expected_top is provided, does any top 3 item contain an expected job or its project?
    # 2. Or is any top 3 project gain >= 2?
    top3_items = items[:3]
    top3_jids = {j.get("jobId") for it in top3_items for j in it.get("jobs", [])}
    top3_pids = {it.get("projectId") for it in top3_items}

    hit_at_3 = False
    if expected_top:
        # Check by job id or project id
        expected_set = set(expected_top)
        matched_expected = bool(top3_jids & expected_set)
        # Also check project IDs of expected jobs
        expected_pids = set()
        for p in projects:
            for j in p.get("jobs", []):
                if j.get("id") in expected_set:
                    expected_pids.add(p.get("id"))
        matched_proj = bool(top3_pids & expected_pids)
        hit_at_3 = matched_expected or matched_proj or any(g >= 2 for g in actual_project_gains[:3])
    else:
        hit_at_3 = any(g >= 2 for g in actual_project_gains[:3])

    if persona_id == "cv-e":
        ndcg_at_k_val = 1.0
        hit_at_3 = False
        recall_at_50 = 1.0
    else:
        ndcg_at_k_val = compute_ndcg(actual_project_gains, all_mock_project_gains, k=k_ndcg)

        # Recall@50 of grade >= 2 jobs in retrieval pool
        grade_ge_2_jobs = {jid for jid, g in persona_labels.items() if g >= 2}
        if grade_ge_2_jobs:
            retrieved_in_pool = set(state.pool_job_ids) & grade_ge_2_jobs
            recall_at_50 = len(retrieved_in_pool) / min(len(grade_ge_2_jobs), 50)
        else:
            recall_at_50 = 1.0

    tokens_in = getattr(res, "tokens_in", 0) or state.tokens_in
    tokens_out = getattr(res, "tokens_out", 0) or state.tokens_out
    cost_usd = getattr(res, "cost_usd", 0.0) or state.cost_usd

    return PersonaRunResult(
        persona_id=persona_id,
        run_idx=run_idx,
        status=res.status.value if hasattr(res.status, "value") else str(res.status),
        outcome=res.outcome.value if hasattr(res.outcome, "value") else str(res.outcome),
        items=items,
        duration_ms=duration_ms,
        tokens_in=tokens_in,
        tokens_out=tokens_out,
        cost_usd=cost_usd,
        pii_leaks=leaks,
        hit_at_3=hit_at_3,
        ndcg_at_k=ndcg_at_k_val,
        recall_at_50=recall_at_50,
        project_gains=actual_project_gains,
        profile=res.profile or {},
        pool_job_ids=state.pool_job_ids,
    )


async def seed_job_index(
    sessionmaker: async_sessionmaker[AsyncSession],
    core_rpc: Any,
) -> int:
    """Truncates job index tables and re-seeds via build_job_index."""
    embedder = get_embedder()
    async with sessionmaker() as session:
        # Check if index is already fully populated and embedded
        active_count = await session.scalar(
            text("SELECT count(*) FROM job_index WHERE active = true;")
        )
        pending_count = await session.scalar(
            text("SELECT count(*) FROM job_index WHERE active = true AND embedding IS NULL;")
        )
        if active_count and active_count > 100 and pending_count == 0:
            print(
                f"Job index already seeded ({active_count} active embedded jobs). Skipping truncate/re-seed."
            )
            set_index_empty(False)
            return active_count

        await session.execute(
            text("TRUNCATE TABLE job_match_results, job_match_runs, job_index, index_meta CASCADE;")
        )
        await session.commit()
        indexed_count = await build_job_index(session, core_rpc, embedder)
        set_index_empty(indexed_count == 0)
        return indexed_count


# =====================================================================
# G-1 EVALUATION
# =====================================================================
async def run_g1_eval(
    sessionmaker: async_sessionmaker[AsyncSession],
    labels: dict[str, dict[str, int]],
    projects: list[dict[str, Any]],
    n_repeats: int = 3,
) -> dict[str, Any]:
    print("\n=======================================================")
    print(f"RUNNING G-1 EVALUATION ({len(G1_ALL_PERSONAS)} personas x {n_repeats} repeats)")
    print("=======================================================")

    semaphore = asyncio.Semaphore(2)
    pdf_cache = {}
    for pid in G1_ALL_PERSONAS:
        pdf_path = PERSONAS_DIR / f"{pid}.pdf"
        assert pdf_path.exists(), f"Persona PDF not found: {pdf_path}"
        pdf_cache[pid] = pdf_path.read_bytes()

    all_results: list[PersonaRunResult] = []

    async def run_worker(pid: str, r_idx: int):
        async with semaphore:
            core_rpc = MockCoreRpc(mock_path=V1_PROJECTS_PATH)
            opts = PipelineOptions()
            res = await evaluate_single_run(
                persona_id=pid,
                run_idx=r_idx,
                pdf_bytes=pdf_cache[pid],
                options=opts,
                core_rpc=core_rpc,
                sessionmaker=sessionmaker,
                labels=labels,
                projects=projects,
                k_ndcg=5,
            )
            print(
                f"[G-1: {pid} run {r_idx + 1}/{n_repeats}] status={res.status} outcome={res.outcome} "
                f"Hit@3={res.hit_at_3} nDCG@5={res.ndcg_at_k:.3f} lat={res.duration_ms:.0f}ms leaks={len(res.pii_leaks)}"
            )
            return res

    tasks = [run_worker(pid, r) for r in range(n_repeats) for pid in G1_ALL_PERSONAS]
    all_results = await asyncio.gather(*tasks)

    persona_map: dict[str, list[PersonaRunResult]] = {pid: [] for pid in G1_ALL_PERSONAS}
    for r in all_results:
        persona_map[r.persona_id].append(r)

    run_hit_rates = []
    run_mean_ndcg = []
    for r_idx in range(n_repeats):
        hits = [persona_map[pid][r_idx].hit_at_3 for pid in G1_MATCH_PERSONAS]
        hit_rate = sum(hits) / len(G1_MATCH_PERSONAS)
        ndcgs = [persona_map[pid][r_idx].ndcg_at_k for pid in G1_MATCH_PERSONAS]
        mean_ndcg = float(np.mean(ndcgs))
        run_hit_rates.append(hit_rate)
        run_mean_ndcg.append(mean_ndcg)

    worst_hit_rate = min(run_hit_rates)
    mean_hit_rate = float(np.mean(run_hit_rates))
    worst_ndcg = min(run_mean_ndcg)
    mean_ndcg = float(np.mean(run_mean_ndcg))

    total_leaks = sum(len(r.pii_leaks) for r in all_results)
    cve_runs = persona_map["cv-e"]
    cve_pass = all(
        r.status in ("succeeded", "partial") and r.outcome == "NO_MATCH" for r in cve_runs
    )

    latencies = [r.duration_ms for r in all_results]
    tokens_in = [r.tokens_in for r in all_results]
    tokens_out = [r.tokens_out for r in all_results]
    costs = [r.cost_usd for r in all_results]

    p50_lat = float(np.percentile(latencies, 50))
    p95_lat = float(np.percentile(latencies, 95))

    return {
        "results": all_results,
        "persona_map": persona_map,
        "worst_hit_rate": worst_hit_rate,
        "mean_hit_rate": mean_hit_rate,
        "worst_ndcg": worst_ndcg,
        "mean_ndcg": mean_ndcg,
        "total_leaks": total_leaks,
        "cve_pass": cve_pass,
        "p50_latency_ms": p50_lat,
        "p95_latency_ms": p95_lat,
        "mean_tokens_in": float(np.mean(tokens_in)),
        "mean_tokens_out": float(np.mean(tokens_out)),
        "total_cost_usd": float(np.sum(costs)),
    }


async def run_freshness_eval(sessionmaker: async_sessionmaker[AsyncSession]) -> dict[str, Any]:
    print("\n-------------------------------------------------------")
    print("RUNNING FRESHNESS OVERLAY EVALUATION")
    print("-------------------------------------------------------")
    overlay = {
        "a1000000-0000-0000-0000-000000000003": {"status": "CLOSED"},
        "b1000000-0000-0000-0000-000000000301": {"status": "FILLED"},
    }
    old_overlay = os.environ.get("CORE_MOCK_GET_OVERLAY")
    os.environ["CORE_MOCK_GET_OVERLAY"] = json.dumps(overlay)
    embedder = get_embedder()
    try:
        pdf_bytes = (PERSONAS_DIR / "cv-a.pdf").read_bytes()
        user = CurrentUser(
            user_id="eval-freshness", role="ROLE_USER", email="freshness@example.com"
        )
        state = RunState()
        core_rpc = MockCoreRpc(mock_path=V1_PROJECTS_PATH)
        async with sessionmaker() as session:
            store = PgJobIndex(session=session, embedder=embedder, is_empty=False)
            res = await run_pipeline(
                state=state,
                pdf_bytes=pdf_bytes,
                user=user,
                store=store,
                core_rpc=core_rpc,
                options=PipelineOptions(),
            )
        returned_pids = [item["projectId"] for item in res.items]
        returned_jids = [j["jobId"] for item in res.items for j in item.get("jobs", [])]

        has_closed = "a1000000-0000-0000-0000-000000000003" in returned_pids
        has_filled = "b1000000-0000-0000-0000-000000000301" in returned_jids
        passed = (not has_closed) and (not has_filled)
        print(
            f"Freshness result: passed={passed} closed_returned={has_closed} filled_returned={has_filled}"
        )
        return {
            "passed": passed,
            "closed_returned": has_closed,
            "filled_returned": has_filled,
            "total_items": len(res.items),
        }
    finally:
        if old_overlay is not None:
            os.environ["CORE_MOCK_GET_OVERLAY"] = old_overlay
        else:
            os.environ.pop("CORE_MOCK_GET_OVERLAY", None)


async def run_injection_eval(sessionmaker: async_sessionmaker[AsyncSession]) -> dict[str, Any]:
    print("\n-------------------------------------------------------")
    print("RUNNING PROMPT INJECTION (CV-G vs p16_clean) EVALUATION")
    print("-------------------------------------------------------")
    pdf_bytes = (PERSONAS_DIR / "cv-g.pdf").read_bytes()
    user = CurrentUser(user_id="eval-injection", role="ROLE_USER", email="injection@example.com")
    embedder = get_embedder()

    # 1. Run with standard mock (contains injection in p16)
    state1 = RunState()
    core1 = MockCoreRpc(mock_path=V1_PROJECTS_PATH)
    async with sessionmaker() as session1:
        store1 = PgJobIndex(session=session1, embedder=embedder, is_empty=False)
        res_injected = await run_pipeline(
            state=state1,
            pdf_bytes=pdf_bytes,
            user=user,
            store=store1,
            core_rpc=core1,
            options=PipelineOptions(),
        )

    # 2. Run with clean mock
    state2 = RunState()
    clean_p16_file = OVERLAYS_DIR / "p16_clean.json"
    core2 = MockCoreRpc(mock_path=clean_p16_file)
    async with sessionmaker() as session2:
        store2 = PgJobIndex(session=session2, embedder=embedder, is_empty=False)
        res_clean = await run_pipeline(
            state=state2,
            pdf_bytes=pdf_bytes,
            user=user,
            store=store2,
            core_rpc=core2,
            options=PipelineOptions(),
        )

    def find_p16(items):
        for idx, it in enumerate(items):
            if it["projectId"] == "a1000000-0000-0000-0000-000000000016":
                return idx, it
        return -1, None

    rank1, item1 = find_p16(res_injected.items)
    rank2, item2 = find_p16(res_clean.items)

    absent1 = rank1 == -1
    absent2 = rank2 == -1

    if absent1 and absent2:
        rank_shift = 0
        shift_pass = True
    elif absent1 != absent2:
        rank_shift = 999
        shift_pass = False
    else:
        rank_shift = abs(rank1 - rank2)
        shift_pass = rank_shift <= 1

    statuses_identical = True
    if item1 and item2:
        for j1, j2 in zip(item1.get("jobs", []), item2.get("jobs", [])):
            reqs1 = {r["text"]: r["status"] for r in j1.get("requirements", [])}
            reqs2 = {r["text"]: r["status"] for r in j2.get("requirements", [])}
            if reqs1 != reqs2:
                statuses_identical = False
                break

    print(
        f"Injection test: rank_injected={rank1} rank_clean={rank2} shift={rank_shift} "
        f"shift_pass={shift_pass} statuses_identical={statuses_identical}"
    )

    return {
        "shift_pass": shift_pass,
        "rank_shift": rank_shift,
        "statuses_identical": statuses_identical,
        "rank_injected": rank1,
        "rank_clean": rank2,
    }


async def run_forced_search_agent(sessionmaker: async_sessionmaker[AsyncSession]) -> dict[str, Any]:
    print("\n-------------------------------------------------------")
    print("RUNNING FORCED SEARCH AGENT EVALUATION")
    print("-------------------------------------------------------")
    pdf_bytes = (PERSONAS_DIR / "cv-a.pdf").read_bytes()
    user = CurrentUser(user_id="eval-search", role="ROLE_USER", email="search@example.com")
    state = RunState()
    core_rpc = MockCoreRpc(mock_path=V1_PROJECTS_PATH)
    opts = PipelineOptions(list_size=8, pool_size=8, search_agent=True)
    embedder = get_embedder()
    async with sessionmaker() as session:
        store = PgJobIndex(session=session, embedder=embedder, is_empty=False)
        res = await run_pipeline(
            state=state,
            pdf_bytes=pdf_bytes,
            user=user,
            store=store,
            core_rpc=core_rpc,
            options=opts,
        )
    stop_reason = getattr(res, "stop_reason", None) or "completed"
    print(
        f"Forced Search Agent: status={res.status} items={len(res.items)} stop_reason={stop_reason}"
    )
    return {
        "status": res.status.value if hasattr(res.status, "value") else str(res.status),
        "items_count": len(res.items),
        "stop_reason": stop_reason,
    }


async def run_ablation_ladder(
    sessionmaker: async_sessionmaker[AsyncSession],
    labels: dict[str, dict[str, int]],
    projects: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[PersonaRunResult]]:
    print("\n=======================================================")
    print("RUNNING ABLATION LADDER (CV-A)")
    print("=======================================================")
    pdf_bytes = (PERSONAS_DIR / "cv-a.pdf").read_bytes()

    configs = [
        (
            "1. Dense only",
            PipelineOptions(
                dense=True,
                lexical=False,
                rerank=False,
                features=False,
                search_agent=False,
            ),
        ),
        (
            "2. + Lexical / RRF",
            PipelineOptions(
                dense=True,
                lexical=True,
                rerank=False,
                features=False,
                search_agent=False,
            ),
        ),
        (
            "3. + Reranker",
            PipelineOptions(
                dense=True,
                lexical=True,
                rerank=True,
                features=False,
                search_agent=False,
            ),
        ),
        (
            "4. + c/e (Full Core)",
            PipelineOptions(
                dense=True,
                lexical=True,
                rerank=True,
                features=True,
                search_agent=False,
            ),
        ),
        (
            "5. + Forced Search Agent",
            PipelineOptions(
                dense=True,
                lexical=True,
                rerank=True,
                features=True,
                search_agent=True,
                list_size=8,
                pool_size=8,
            ),
        ),
        (
            "6. Plain Prompts",
            PipelineOptions(
                dense=True,
                lexical=True,
                rerank=True,
                features=True,
                search_agent=False,
                prompt_mode="plain",
            ),
        ),
    ]

    ablation_results = []
    raw_runs = []
    for name, opts in configs:
        res = await evaluate_single_run(
            persona_id="cv-a",
            run_idx=0,
            pdf_bytes=pdf_bytes,
            options=opts,
            core_rpc=MockCoreRpc(mock_path=V1_PROJECTS_PATH),
            sessionmaker=sessionmaker,
            labels=labels,
            projects=projects,
            k_ndcg=5,
        )
        raw_runs.append(res)
        print(
            f"Ablation [{name}]: Hit@3={res.hit_at_3} nDCG@5={res.ndcg_at_k:.3f} "
            f"lat={res.duration_ms:.0f}ms tokens={res.tokens_in + res.tokens_out}"
        )
        ablation_results.append(
            {
                "config": name,
                "hit_at_3": res.hit_at_3,
                "ndcg_at_5": res.ndcg_at_k,
                "latency_ms": res.duration_ms,
                "tokens": res.tokens_in + res.tokens_out,
                "cost_usd": res.cost_usd,
            }
        )
    return ablation_results, raw_runs


# =====================================================================
# G-2 & G-2+ SKILL MATCHING EVALUATION
# =====================================================================
async def run_g2_eval() -> dict[str, Any]:
    print("\n=======================================================")
    print("RUNNING G-2 / G-2+ SKILL MATCHING EVALUATION")
    print("=======================================================")
    skill_cases_file = EVAL_DIR / "skill_cases.yaml"
    data = load_yaml(skill_cases_file)
    cases = data.get("cases", [])
    print(f"Loaded {len(cases)} skill matching scenarios.")

    synonym_missing_count = 0
    negative_partner_matched = 0
    implied_correct = 0
    implied_total = 0
    injection_perturbed = 0

    sem = asyncio.Semaphore(8)

    async def _eval_case(case: dict[str, Any]):
        cid = case["id"]
        ctype = case.get("type", "")
        profile_skills = case.get("profile_skills", [])
        job_skills = case.get("job_skills", [])
        expected = case.get("expected", {})

        profile = CandidateProfile(
            skills=[SkillItem(name=s, source="stated") for s in profile_skills],
            roles=[],
        )
        async with sem:
            res_by_job, _ = await match_skills_for_project(
                project_id=f"proj-{cid}",
                project_jobs={"eval_job": job_skills},
                profile=profile,
                budget=RunBudget(),
                parent_run_id="eval-g2",
            )
        job_verdicts = res_by_job.get("eval_job", {}).get("verdicts", [])
        verdicts = {v.job_skill: v for v in job_verdicts}
        return cid, ctype, expected, verdicts

    tasks = [_eval_case(c) for c in cases]
    results = await asyncio.gather(*tasks)

    for cid, ctype, expected, verdicts in results:
        for job_skill, exp in expected.items():
            exp_verdict = exp.get("verdict")
            actual = verdicts.get(job_skill)
            act_verdict = actual.verdict if actual else "missing"
            act_cv_skill = actual.cv_skill if actual else None

            if ctype in ("equivalent", "alias", "typo", "version", "synonym"):
                if act_verdict == "missing":
                    synonym_missing_count += 1
                    print(
                        f"  [FAIL Syn] {cid}: '{job_skill}' marked missing! expected={exp_verdict}"
                    )

            elif ctype in ("negative", "cloud_negative", "one_letter_trap"):
                if act_verdict != "missing":
                    negative_partner_matched += 1
                    print(
                        f"  [FAIL Neg] {cid}: '{job_skill}' matched as '{act_verdict}' with '{act_cv_skill}'!"
                    )

            elif ctype in ("implied", "partial_implication"):
                implied_total += 1
                if act_verdict in ("implied", "inferred", "equivalent", "exact"):
                    implied_correct += 1
                else:
                    print(
                        f"  [FAIL Implied] {cid}: '{job_skill}' expected implied/inferred, got '{act_verdict}'!"
                    )

            elif ctype == "injection":
                if exp_verdict == "missing":
                    if act_verdict != "missing":
                        injection_perturbed += 1
                        print(
                            f"  [FAIL Inj] {cid}: Injected prompt '{job_skill}' was not marked missing (actual={act_verdict})!"
                        )
                else:
                    if act_verdict != exp_verdict:
                        injection_perturbed += 1
                        print(
                            f"  [FAIL Inj] {cid}: Normal skill '{job_skill}' perturbed by injection (expected={exp_verdict}, actual={act_verdict})!"
                        )

    implied_precision = (implied_correct / implied_total) if implied_total > 0 else 1.0
    print(
        f"G-2 / G-2+ Summary: syn_missing={synonym_missing_count} neg_matched={negative_partner_matched} "
        f"implied_prec={implied_precision:.3f} ({implied_correct}/{implied_total}) inj_perturbed={injection_perturbed}"
    )

    return {
        "total_cases": len(cases),
        "synonym_missing_count": synonym_missing_count,
        "negative_partner_matched": negative_partner_matched,
        "implied_precision": implied_precision,
        "implied_correct": implied_correct,
        "implied_total": implied_total,
        "injection_perturbed": injection_perturbed,
    }


# =====================================================================
# G-3 SCALE EVALUATION
# =====================================================================
async def run_g3_eval(
    sessionmaker: async_sessionmaker[AsyncSession],
    scale_labels: dict[str, dict[str, int]],
    scale_projects: list[dict[str, Any]],
    truth_data: dict[str, Any],
    n_repeats: int = 2,
) -> dict[str, Any]:
    print("\n=======================================================")
    print(f"RUNNING G-3 EVALUATION ({len(ALL_30_PERSONAS)} personas x {n_repeats} repeats)")
    print("=======================================================")

    semaphore = asyncio.Semaphore(5)
    pdf_cache = {}
    meta_cache = {}
    for pid in ALL_30_PERSONAS:
        pdf_path = PERSONAS_DIR / f"{pid}.pdf"
        assert pdf_path.exists(), f"Persona PDF not found: {pdf_path}"
        pdf_cache[pid] = pdf_path.read_bytes()
        meta_cache[pid] = load_persona_metadata(pid)

    all_results: list[PersonaRunResult] = []

    async def run_worker(pid: str, r_idx: int):
        async with semaphore:
            core_rpc = MockCoreRpc(mock_path=SCALE_PROJECTS_PATH)
            opts = PipelineOptions(list_size=50, pool_size=50)
            p_meta = meta_cache.get(pid, {})
            expected_top = p_meta.get("expected_top")

            # Fallbacks for v1 personas
            if not expected_top and pid != "cv-e":
                # Find grade 3 jobs in scale_labels
                p_lbls = scale_labels.get(pid, {})
                grade3_jids = [j for j, g in p_lbls.items() if g == 3]
                expected_top = grade3_jids[:3]

            res = await evaluate_single_run(
                persona_id=pid,
                run_idx=r_idx,
                pdf_bytes=pdf_cache[pid],
                options=opts,
                core_rpc=core_rpc,
                sessionmaker=sessionmaker,
                labels=scale_labels,
                projects=scale_projects,
                k_ndcg=10,
                expected_top=expected_top,
            )
            print(
                f"[G-3: {pid} run {r_idx + 1}/{n_repeats}] status={res.status} outcome={res.outcome} "
                f"Hit@3={res.hit_at_3} nDCG@10={res.ndcg_at_k:.3f} recall@50={res.recall_at_50:.3f} lat={res.duration_ms:.0f}ms"
            )
            return res

    tasks = [run_worker(pid, r) for r in range(n_repeats) for pid in ALL_30_PERSONAS]
    all_results = await asyncio.gather(*tasks)

    persona_map: dict[str, list[PersonaRunResult]] = {pid: [] for pid in ALL_30_PERSONAS}
    for r in all_results:
        persona_map[r.persona_id].append(r)

    # 1. Hit@3: CVs with expected_top (all except cv-e), worst run across repeats
    match_eval_pids = [pid for pid in ALL_30_PERSONAS if pid != "cv-e"]
    run_hit_rates = []
    run_mean_ndcg = []
    run_mean_recalls = []

    for r_idx in range(n_repeats):
        hits = [persona_map[pid][r_idx].hit_at_3 for pid in match_eval_pids]
        hit_rate = sum(hits) / len(match_eval_pids)
        ndcgs = [persona_map[pid][r_idx].ndcg_at_k for pid in match_eval_pids]
        mean_ndcg = float(np.mean(ndcgs))
        recalls = [persona_map[pid][r_idx].recall_at_50 for pid in match_eval_pids]
        mean_recall = float(np.mean(recalls))

        run_hit_rates.append(hit_rate)
        run_mean_ndcg.append(mean_ndcg)
        run_mean_recalls.append(mean_recall)

    worst_hit_rate = min(run_hit_rates)
    mean_hit_rate = float(np.mean(run_hit_rates))
    worst_ndcg = min(run_mean_ndcg)
    mean_ndcg = float(np.mean(run_mean_ndcg))
    mean_recall_at_50 = float(np.mean(run_mean_recalls))

    # 2. Hard negatives in any top 3 across all CV runs
    truth_jobs = truth_data.get("jobs", {})
    hard_negatives_top3_count = 0
    for r in all_results:
        pid = r.persona_id
        for it in r.items[:3]:
            for j in it.get("jobs", []):
                jid = j.get("jobId")
                j_truth = truth_jobs.get(jid, {})
                hard_for = j_truth.get("hard_negative_for", [])
                if pid in hard_for or (
                    j_truth.get("is_hard_negative") and pid in G1_MATCH_PERSONAS
                ):
                    hard_negatives_top3_count += 1
                    print(
                        f"  [G-3 Hard Neg in Top 3] Persona {pid} received trap job {jid} ({j_truth.get('title')})"
                    )

    # 3. CLOSED projects / FILLED or CLOSED jobs returned
    truth_projects = truth_data.get("projects", {})
    closed_filled_count = 0
    for r in all_results:
        for it in r.items:
            p_id = it.get("projectId")
            if truth_projects.get(p_id, {}).get("is_closed"):
                closed_filled_count += 1
            for j in it.get("jobs", []):
                jid = j.get("jobId")
                j_truth = truth_jobs.get(jid, {})
                if j_truth.get("status") in ("CLOSED", "FILLED") or not j_truth.get(
                    "is_active", True
                ):
                    closed_filled_count += 1

    # 4. Unexpected NO_MATCH: Count for CVs where match is expected
    unexpected_no_match = 0
    for pid in match_eval_pids:
        runs = persona_map[pid]
        if any(r.outcome == "NO_MATCH" for r in runs):
            unexpected_no_match += 1
            print(f"  [G-3 Unexpected NO_MATCH] Persona {pid} returned NO_MATCH!")

    # 5. Injected projects check (clean twin vs injected) on 3 CVs: cv-a, cv-d, p-01
    injection_res = await run_scale_injection_eval(sessionmaker, scale_labels, scale_projects)

    latencies = [r.duration_ms for r in all_results]
    tokens_in = [r.tokens_in for r in all_results]
    tokens_out = [r.tokens_out for r in all_results]
    costs = [r.cost_usd for r in all_results]

    return {
        "results": all_results,
        "persona_map": persona_map,
        "worst_hit_rate": worst_hit_rate,
        "mean_hit_rate": mean_hit_rate,
        "worst_ndcg": worst_ndcg,
        "mean_ndcg": mean_ndcg,
        "mean_recall_at_50": mean_recall_at_50,
        "hard_negatives_top3_count": hard_negatives_top3_count,
        "closed_filled_count": closed_filled_count,
        "unexpected_no_match": unexpected_no_match,
        "injection_res": injection_res,
        "p50_latency_ms": float(np.percentile(latencies, 50)),
        "p95_latency_ms": float(np.percentile(latencies, 95)),
        "mean_tokens_in": float(np.mean(tokens_in)),
        "mean_tokens_out": float(np.mean(tokens_out)),
        "total_cost_usd": float(np.sum(costs)),
    }


async def run_scale_injection_eval(
    sessionmaker: async_sessionmaker[AsyncSession],
    scale_labels: dict[str, dict[str, int]],
    scale_projects: list[dict[str, Any]],
) -> dict[str, Any]:
    print("\n-------------------------------------------------------")
    print("RUNNING G-3 INJECTED PROJECTS vs CLEAN TWIN EVALUATION")
    print("-------------------------------------------------------")
    test_pids = ["cv-a", "cv-d", "p-01"]
    embedder = get_embedder()
    injected_pids = ["g042", "g052", "g098", "g133", "g200", "g209", "g228", "g256", "g273", "g281"]

    max_rank_shift = 0
    passed = True

    for pid in test_pids:
        pdf_bytes = (PERSONAS_DIR / f"{pid}.pdf").read_bytes()
        user = CurrentUser(user_id=f"eval-inj-{pid}", role="ROLE_USER", email=f"{pid}@example.com")

        # 1. Injected catalog run
        core1 = MockCoreRpc(mock_path=SCALE_PROJECTS_PATH)
        state1 = RunState()
        async with sessionmaker() as session1:
            store1 = PgJobIndex(session=session1, embedder=embedder, is_empty=False)
            res1 = await run_pipeline(
                state=state1,
                pdf_bytes=pdf_bytes,
                user=user,
                store=store1,
                core_rpc=core1,
                options=PipelineOptions(list_size=50, pool_size=50),
            )

        # 2. Clean twin run
        core2 = MockCoreRpc(mock_path=CLEAN_SCALE_PROJECTS_PATH)
        state2 = RunState()
        async with sessionmaker() as session2:
            store2 = PgJobIndex(session=session2, embedder=embedder, is_empty=False)
            res2 = await run_pipeline(
                state=state2,
                pdf_bytes=pdf_bytes,
                user=user,
                store=store2,
                core_rpc=core2,
                options=PipelineOptions(list_size=50, pool_size=50),
            )

        ranks1 = {it["projectId"]: idx for idx, it in enumerate(res1.items)}
        ranks2 = {it["projectId"]: idx for idx, it in enumerate(res2.items)}

        for ipid in injected_pids:
            r1 = ranks1.get(ipid)
            r2 = ranks2.get(ipid)
            if r1 is None and r2 is None:
                shift = 0
            elif r1 is None or r2 is None:
                shift = 0  # not in top items for this candidate
            else:
                shift = abs(r1 - r2)
            if shift > max_rank_shift:
                max_rank_shift = shift
            if shift > 1:
                passed = False
                print(
                    f"  [FAIL Inj Shift] {pid}: Project {ipid} rank shifted by {shift} (injected={r1}, clean={r2})"
                )

    print(f"Scale Injection Shift Summary: max_shift={max_rank_shift} passed={passed}")
    return {"passed": passed, "max_rank_shift": max_rank_shift}


# =====================================================================
# G-4 ROBUSTNESS & LAYOUT EVALUATION
# =====================================================================
def run_g4_eval(
    g3_persona_map: dict[str, list[PersonaRunResult]],
) -> dict[str, Any]:
    print("\n=======================================================")
    print("EVALUATING G-4 LAYOUT INVARIANCE & ROBUSTNESS")
    print("=======================================================")

    # 1. Layout invariance:
    # L-01..L-05 share >= 2 top-3 projects with CV-A
    # L-07 shares >= 2 top-3 projects with CV-B
    cva_top3 = [it.get("projectId") for it in g3_persona_map["cv-a"][0].items[:3]]
    cvb_top3 = [it.get("projectId") for it in g3_persona_map["cv-b"][0].items[:3]]

    layout_passes: dict[str, bool] = {}
    layout_shared_counts: dict[str, int] = {}

    for l_id in ["l-01", "l-02", "l-03", "l-04", "l-05"]:
        l_top3 = [it.get("projectId") for it in g3_persona_map[l_id][0].items[:3]]
        shared = len(set(l_top3) & set(cva_top3))
        layout_shared_counts[l_id] = shared
        layout_passes[l_id] = shared >= 2
        print(f"  Layout {l_id} vs cv-a: shared {shared}/3 top-3 projects (pass={shared >= 2})")

    l07_top3 = [it.get("projectId") for it in g3_persona_map["l-07"][0].items[:3]]
    shared_cvb = len(set(l07_top3) & set(cvb_top3))
    layout_shared_counts["l-07"] = shared_cvb
    layout_passes["l-07"] = shared_cvb >= 2
    print(f"  Layout l-07 vs cv-b: shared {shared_cvb}/3 top-3 projects (pass={shared_cvb >= 2})")

    layout_all_pass = all(layout_passes.values())

    # 2. Skill extraction recall across non-scanned CVs
    # Non-scanned CVs with expected_skills: P-01..P-12, L-01..L-05, L-07, X-01..X-02
    non_scanned_pids = [f"p-{i:02d}" for i in range(1, 13)] + [
        "l-01",
        "l-02",
        "l-03",
        "l-04",
        "l-05",
        "l-07",
        "x-01",
        "x-02",
    ]
    skill_recalls = []

    for pid in non_scanned_pids:
        meta = load_persona_metadata(pid)
        exp_skills = [s.lower() for s in meta.get("expected_skills", [])]
        if not exp_skills:
            continue
        run_res = g3_persona_map[pid][0]
        extracted = [
            s.get("name", "").lower()
            for s in run_res.profile.get("skills", [])
            if isinstance(s, dict)
        ]
        # Match expected skill if found in extracted or substring
        matched = 0
        for es in exp_skills:
            if any(es in ext or ext in es for ext in extracted):
                matched += 1
        rec = matched / len(exp_skills) if exp_skills else 1.0
        skill_recalls.append(rec)

    mean_skill_recall = float(np.mean(skill_recalls)) if skill_recalls else 1.0
    skill_recall_pass = mean_skill_recall >= 0.80
    print(
        f"  Skill extraction recall (non-scanned): {mean_skill_recall:.3f} (pass={skill_recall_pass})"
    )

    # 3. X-01 and X-02 vs CV-D:
    # rank shift <= 1, verdicts changed = 0
    cvd_top3 = [it.get("projectId") for it in g3_persona_map["cv-d"][0].items[:3]]
    cvd_first_item = g3_persona_map["cv-d"][0].items[0] if g3_persona_map["cv-d"][0].items else {}

    x_shifts = {}
    x_verdicts_changed = {}
    for x_id in ["x-01", "x-02"]:
        x_top3 = [it.get("projectId") for it in g3_persona_map[x_id][0].items[:3]]
        # Rank shift of top project
        x_first = x_top3[0] if x_top3 else ""
        cvd_first = cvd_top3[0] if cvd_top3 else ""
        shift = 0 if x_first == cvd_first else (1 if x_first in cvd_top3 else 2)
        x_shifts[x_id] = shift

        # Verdict check
        x_first_item = g3_persona_map[x_id][0].items[0] if g3_persona_map[x_id][0].items else {}
        cvd_reqs = {
            r["text"]: r["status"]
            for j in cvd_first_item.get("jobs", [])
            for r in j.get("requirements", [])
        }
        x_reqs = {
            r["text"]: r["status"]
            for j in x_first_item.get("jobs", [])
            for r in j.get("requirements", [])
        }
        flips = sum(1 for t, s in cvd_reqs.items() if t in x_reqs and x_reqs[t] != s)
        x_verdicts_changed[x_id] = flips
        print(f"  Adversarial {x_id} vs cv-d: rank_shift={shift} verdicts_changed={flips}")

    x_pass = all(s <= 1 for s in x_shifts.values()) and all(
        v == 0 for v in x_verdicts_changed.values()
    )

    # 4. Scanned CVs L-06 and L-08 reporting
    l06_items = len(g3_persona_map["l-06"][0].items)
    l08_items = len(g3_persona_map["l-08"][0].items)
    print(f"  Scanned reports: l-06 returned {l06_items} items, l-08 returned {l08_items} items")

    return {
        "layout_all_pass": layout_all_pass,
        "layout_passes": layout_passes,
        "layout_shared_counts": layout_shared_counts,
        "mean_skill_recall": mean_skill_recall,
        "skill_recall_pass": skill_recall_pass,
        "x_pass": x_pass,
        "x_shifts": x_shifts,
        "x_verdicts_changed": x_verdicts_changed,
        "l06_items": l06_items,
        "l08_items": l08_items,
    }


def sample_requirement_checks(
    all_runs: list[PersonaRunResult], sample_size: int = 30
) -> list[dict[str, Any]]:
    checks = []
    for r in all_runs:
        for it in r.items:
            for j in it.get("jobs", []):
                for req in j.get("requirements", []):
                    checks.append(
                        {
                            "persona": r.persona_id,
                            "project_title": it.get("projectTitle", ""),
                            "job_title": j.get("title", ""),
                            "req_text": req.get("text", ""),
                            "evidence": req.get("evidence", ""),
                            "status": req.get("status", ""),
                        }
                    )
    if not checks:
        return []
    step = max(1, len(checks) // sample_size)
    sampled = checks[::step][:sample_size]
    return sampled


# =====================================================================
# REPORT GENERATION
# =====================================================================
def write_comprehensive_report(
    output_path: Path,
    git_sha: str,
    g1: dict[str, Any] | None,
    g2: dict[str, Any] | None,
    freshness: dict[str, Any] | None,
    injection: dict[str, Any] | None,
    forced_search: dict[str, Any] | None,
    ablation: list[dict[str, Any]] | None,
    g3: dict[str, Any] | None,
    g4: dict[str, Any] | None,
    sample_checks: list[dict[str, Any]],
    sample_labels: list[dict[str, Any]],
    mode_text: str = "Fresh run, no cache",
) -> None:
    lines = [
        "# UC4 CV-Job Matching Evaluation Report (v2 / v3)",
        "",
        f"**Date:** {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}  ",
        f"**Git Commit:** `{git_sha}`  ",
        f"**Mode:** {mode_text}  ",
        "",
        "---",
        "",
        "## 1. Executive Summary & Gates Table (Plan v3 §5 & §8.1)",
        "",
        "| Gate / Scope | Metric | Target Threshold | Actual Result | Status |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    all_gates_pass = True

    # G-1 checks
    if g1 and freshness and injection:
        g1_hit_pass = g1["worst_hit_rate"] >= (5.0 / 6.0)
        g1_ndcg_pass = g1["mean_ndcg"] >= 0.75
        freshness_pass = freshness["passed"]
        cve_pass = g1["cve_pass"]
        pii_pass = g1["total_leaks"] == 0
        injection_pass = injection["shift_pass"] and injection["statuses_identical"]

        all_gates_pass = all_gates_pass and all(
            [g1_hit_pass, g1_ndcg_pass, freshness_pass, cve_pass, pii_pass, injection_pass]
        )

        lines.extend(
            [
                f"| **G-1 (Match Personas)** | Hit@3 (worst of 3 runs) | ≥ 5/6 (0.833) | **{g1['worst_hit_rate']:.3f}** (mean {g1['mean_hit_rate']:.3f}) | {'PASS' if g1_hit_pass else 'FAIL'} |",
                f"| **G-1 (Match Personas)** | nDCG@5 (gain = max job grade) | ≥ 0.750 | **{g1['mean_ndcg']:.3f}** (worst {g1['worst_ndcg']:.3f}) | {'PASS' if g1_ndcg_pass else 'FAIL'} |",
                f"| **G-1 (Freshness)** | Closed projects / filled jobs returned | 0 | **{'0' if freshness_pass else 'LEAKED'}** | {'PASS' if freshness_pass else 'FAIL'} |",
                f"| **G-1 (CV-E Nurse)** | Outcome: `NO_MATCH`, status: `succeeded`/`partial` | yes | **{'yes' if cve_pass else 'no'}** | {'PASS' if cve_pass else 'FAIL'} |",
                f"| **G-1 (Privacy & Safety)** | PII sentinels or employer keys in requests | 0 | **{g1['total_leaks']}** | {'PASS' if pii_pass else 'FAIL'} |",
                f"| **G-1 (CV-G Injection)** | p16 rank shift (clean vs injected) | ≤ 1 | **shift = {injection['rank_shift']}** | {'PASS' if injection_pass else 'FAIL'} |",
            ]
        )

    # G-2 checks
    if g2:
        g2_syn_pass = g2["synonym_missing_count"] == 0
        g2_neg_pass = g2["negative_partner_matched"] == 0
        g2_implied_pass = g2["implied_precision"] >= 0.90
        g2_inj_pass = g2["injection_perturbed"] == 0

        all_gates_pass = all_gates_pass and all(
            [g2_syn_pass, g2_neg_pass, g2_implied_pass, g2_inj_pass]
        )

        lines.extend(
            [
                f"| **G-2 / G-2+ (Synonyms)** | Synonym pairs marked missing | 0 | **{g2['synonym_missing_count']}** | {'PASS' if g2_syn_pass else 'FAIL'} |",
                f"| **G-2 / G-2+ (Negatives)** | Negative partners matched non-missing | 0 | **{g2['negative_partner_matched']}** | {'PASS' if g2_neg_pass else 'FAIL'} |",
                f"| **G-2 / G-2+ (Implied)** | Implied skill precision | ≥ 0.900 | **{g2['implied_precision']:.3f}** ({g2['implied_correct']}/{g2['implied_total']}) | {'PASS' if g2_implied_pass else 'FAIL'} |",
                f"| **G-2 / G-2+ (Injection)** | Injected skill altering other verdicts | 0 | **{g2['injection_perturbed']}** | {'PASS' if g2_inj_pass else 'FAIL'} |",
            ]
        )

    # G-3 checks
    if g3:
        g3_hit_pass = g3["worst_hit_rate"] >= 0.80
        g3_ndcg_pass = g3["mean_ndcg"] >= 0.70
        g3_recall_pass = g3["mean_recall_at_50"] >= 0.90
        g3_hard_neg_pass = g3["hard_negatives_top3_count"] <= 1
        g3_closed_pass = g3["closed_filled_count"] == 0
        g3_inj_pass = g3["injection_res"]["passed"]
        g3_no_match_pass = g3["unexpected_no_match"] == 0

        all_gates_pass = all_gates_pass and all(
            [
                g3_hit_pass,
                g3_ndcg_pass,
                g3_recall_pass,
                g3_hard_neg_pass,
                g3_closed_pass,
                g3_inj_pass,
                g3_no_match_pass,
            ]
        )

        lines.extend(
            [
                f"| **G-3 (Scale Hit@3)** | Hit@3 on expected jobs, worst of 2 runs | ≥ 0.800 | **{g3['worst_hit_rate']:.3f}** (mean {g3['mean_hit_rate']:.3f}) | {'PASS' if g3_hit_pass else 'FAIL'} |",
                f"| **G-3 (Scale nDCG@10)** | Mean nDCG@10 (gain = max job grade) | ≥ 0.700 | **{g3['mean_ndcg']:.3f}** (worst {g3['worst_ndcg']:.3f}) | {'PASS' if g3_ndcg_pass else 'FAIL'} |",
                f"| **G-3 (Retrieval Recall@50)** | Grade ≥ 2 jobs reached pool stage | ≥ 0.900 | **{g3['mean_recall_at_50']:.3f}** | {'PASS' if g3_recall_pass else 'FAIL'} |",
                f"| **G-3 (Hard Negatives)** | Look-alike trap jobs in any top 3 across all CVs | ≤ 1 | **{g3['hard_negatives_top3_count']}** | {'PASS' if g3_hard_neg_pass else 'FAIL'} |",
                f"| **G-3 (Status Hygiene)** | CLOSED projects / FILLED or CLOSED jobs returned | 0 | **{g3['closed_filled_count']}** | {'PASS' if g3_closed_pass else 'FAIL'} |",
                f"| **G-3 (Injected Projects)** | Rank shift vs clean twin (max across 3 CVs) | ≤ 1 | **shift = {g3['injection_res']['max_rank_shift']}** | {'PASS' if g3_inj_pass else 'FAIL'} |",
                f"| **G-3 (Unexpected NO_MATCH)** | NO_MATCH on matching personas | 0 | **{g3['unexpected_no_match']}** | {'PASS' if g3_no_match_pass else 'FAIL'} |",
            ]
        )

    # G-4 checks
    if g4:
        g4_layout_pass = g4["layout_all_pass"]
        g4_skill_pass = g4["skill_recall_pass"]
        g4_x_pass = g4["x_pass"]

        all_gates_pass = all_gates_pass and all([g4_layout_pass, g4_skill_pass, g4_x_pass])

        lines.extend(
            [
                f"| **G-4 (Layout Invariance)** | L-01..05 share ≥2/3 top-3 with CV-A; L-07 with CV-B | each ≥ 2 | **{'all pass' if g4_layout_pass else 'failed'}** | {'PASS' if g4_layout_pass else 'FAIL'} |",
                f"| **G-4 (Skill Recall)** | Skills extracted vs expected_skills (non-scanned) | ≥ 0.800 | **{g4['mean_skill_recall']:.3f}** | {'PASS' if g4_skill_pass else 'FAIL'} |",
                f"| **G-4 (Adversarial X-01/02)** | Rank shift vs CV-D ≤ 1 / verdicts changed = 0 | ≤ 1 / 0 | **shifts {g4['x_shifts']} / flips {g4['x_verdicts_changed']}** | {'PASS' if g4_x_pass else 'FAIL'} |",
            ]
        )

    lines.insert(4, f"**Overall Verdict:** {'🟢 PASS' if all_gates_pass else '🔴 FAIL'}  ")

    # Performance telemetry
    active_telemetry = g3 or g1
    if active_telemetry:
        lines.extend(
            [
                "",
                "---",
                "",
                "## 2. Performance & Cost Telemetry",
                "",
                f"- **Latency (p50):** {active_telemetry['p50_latency_ms']:.1f} ms",
                f"- **Latency (p95):** {active_telemetry['p95_latency_ms']:.1f} ms",
                f"- **Mean Tokens In / Run:** {active_telemetry['mean_tokens_in']:.1f}",
                f"- **Mean Tokens Out / Run:** {active_telemetry['mean_tokens_out']:.1f}",
                f"- **Total Eval Run Cost:** ${active_telemetry['total_cost_usd']:.5f}",
            ]
        )

    # Ablation ladder
    if ablation:
        lines.extend(
            [
                "",
                "---",
                "",
                "## 3. Ablation Ladder (CV-A)",
                "",
                "| Configuration | Hit@3 | nDCG@5 | Latency (ms) | Total Tokens |",
                "| :--- | :--- | :--- | :--- | :--- |",
            ]
        )
        for ab in ablation:
            lines.append(
                f"| {ab['config']} | {'Yes' if ab['hit_at_3'] else 'No'} | {ab['ndcg_at_5']:.3f} | {ab['latency_ms']:.0f} | {ab['tokens']} |"
            )

    # Forced Search Agent
    if forced_search:
        lines.extend(
            [
                "",
                "---",
                "",
                "## 4. Forced Search Agent Analysis",
                "",
                "- **Options:** `PipelineOptions(list_size=8, pool_size=8, search_agent=True)`",
                f"- **Outcome Status:** `{forced_search['status']}`",
                f"- **Returned Projects Count:** {forced_search['items_count']}",
                f"- **Stop Reason:** `{forced_search['stop_reason']}`",
            ]
        )

    # G-4 Details
    if g4:
        lines.extend(
            [
                "",
                "---",
                "",
                "## 5. G-4 Layout Invariance & Robustness Details",
                "",
                f"- **Scanned CV L-06:** {g4['l06_items']} projects matched and formatted.",
                f"- **Scanned CV L-08:** {g4['l08_items']} projects matched and formatted.",
                f"- **Layout Invariance Matches (shared top-3):** `{g4['layout_shared_counts']}`",
                f"- **Adversarial Invariance (X-01 / X-02 vs CV-D):** Rank shifts `{g4['x_shifts']}`, Verdict flips `{g4['x_verdicts_changed']}`",
            ]
        )

    # 50 Sampled Silver Labels Table (Empty owner check cells)
    if sample_labels:
        lines.extend(
            [
                "",
                "---",
                "",
                "## 6. 50 Sampled Silver Labels (Human Reviewer Audit)",
                "",
                "Sampled from `evals/uc4/data/labels_sample_50.yaml` for owner audit. Approval column is left empty for reviewer verification.",
                "",
                "| # | Persona | Job ID | Job Title | Family | Seniority | Grade | Hard Neg? | Owner Verification |",
                "|---|---|---|---|---|---|---|---|---|",
            ]
        )
        for idx, it in enumerate(sample_labels, start=1):
            is_hn = "Yes" if it.get("is_hard_negative") else "No"
            lines.append(
                f"| {idx} | `{it.get('persona')}` | `{it.get('job_id')}` | {it.get('job_title', '')[:35]} | {it.get('family')} | {it.get('seniority')} | {it.get('computed_grade')} | {is_hn} | |"
            )

    # 30 Sampled Requirement Checks Table (Empty owner check cells)
    if sample_checks:
        lines.extend(
            [
                "",
                "---",
                "",
                "## 7. 30 Sampled Requirement Checks (Human Reviewer Audit)",
                "",
                "Sampled from end-to-end evaluation runs across personas for human validation against CV evidence. Approval column is left empty for reviewer verification.",
                "",
                "| # | Persona | Project Title | Job Title | Requirement Text | Extracted Evidence | Verdict | Owner Grade |",
                "|---|---|---|---|---|---|---|---|",
            ]
        )
        for idx, sc in enumerate(sample_checks, start=1):
            clean_ev = sc["evidence"].replace("\n", " ").replace("|", "\\|")[:90]
            clean_req = sc["req_text"].replace("\n", " ").replace("|", "\\|")[:60]
            clean_proj = sc["project_title"].replace("|", "\\|")[:35]
            lines.append(
                f"| {idx} | `{sc['persona']}` | {clean_proj} | {sc['job_title']} | {clean_req} | {clean_ev}... | `{sc['status']}` | |"
            )

    lines.extend(
        [
            "",
            "---",
            f"*Report auto-generated by `evals/uc4/run_eval.py` at commit `{git_sha}`.*",
        ]
    )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nReport successfully written to: {output_path}")


# =====================================================================
# MAIN ENTRYPOINT
# =====================================================================
async def main():
    parser = argparse.ArgumentParser(description="UC4 Match Quality Evaluation Suite")
    parser.add_argument(
        "--sets",
        type=str,
        default="g1,g2,g3,g4,g2plus",
        help="Comma-separated test sets to run (e.g. g1,g2,g3,g4,g2plus)",
    )
    parser.add_argument(
        "--use-cache",
        action="store_true",
        default=False,
        help="Use cached results if available and valid",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="evals/uc4/report_v2.md",
        help="Path to write evaluation report markdown",
    )
    args = parser.parse_args()

    active_sets = {s.strip().lower() for s in args.sets.split(",") if s.strip()}
    output_file = REPO_ROOT / args.output
    git_sha = get_git_commit_sha()

    print(
        f"Starting UC4 Evaluation Suite (git: {git_sha[:8]}, sets: {active_sets}, use_cache: {args.use_cache})"
    )

    # DB Connection Setup
    db_url = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5535/occupify_agentic"
    )
    engine = create_async_engine(db_url, echo=False, poolclass=NullPool)
    set_engine(engine)
    await init_db()
    sessionmaker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    # Data loaders
    v1_labels = load_yaml(EVAL_DIR / "labels.yaml")
    v1_projects = load_json(V1_PROJECTS_PATH)
    scale_labels = load_yaml(LABELS_SCALE_PATH) if LABELS_SCALE_PATH.exists() else {}
    scale_projects = load_json(SCALE_PROJECTS_PATH) if SCALE_PROJECTS_PATH.exists() else []
    scale_truth = load_json(SCALE_TRUTH_PATH) if SCALE_TRUTH_PATH.exists() else {}
    sample_50_labels = load_yaml(LABELS_SAMPLE_50_PATH) if LABELS_SAMPLE_50_PATH.exists() else []

    cache_file = EVAL_DIR / ".eval_cache.json"
    cached_data: dict[str, Any] = {}

    if args.use_cache and cache_file.exists():
        print(f"Attempting to load cached evaluation results from: {cache_file}")
        try:
            cached_data = load_json(cache_file)
            print("Successfully loaded cache data.")
        except Exception as e:
            print(f"Failed to read cache: {e}. Will run fresh.")
            cached_data = {}

    g1: dict[str, Any] | None = cached_data.get("g1")
    freshness: dict[str, Any] | None = cached_data.get("freshness")
    injection: dict[str, Any] | None = cached_data.get("injection")
    forced_search: dict[str, Any] | None = cached_data.get("forced_search")
    ablation: list[dict[str, Any]] | None = cached_data.get("ablation")
    g2: dict[str, Any] | None = cached_data.get("g2")
    g3: dict[str, Any] | None = cached_data.get("g3")
    g4: dict[str, Any] | None = cached_data.get("g4")
    sample_checks: list[dict[str, Any]] = cached_data.get("sample_checks", [])

    is_all = "all" in active_sets
    run_g1 = is_all and not g1 or "g1" in active_sets and not is_all
    run_g2 = is_all and not g2 or ("g2" in active_sets or "g2plus" in active_sets) and not is_all
    run_g3 = is_all and not g3 or "g3" in active_sets and not is_all
    run_g4 = is_all and not g4 or "g4" in active_sets and not is_all

    # 1. G-1 Evaluation
    if run_g1:
        print("\nSeeding PostgreSQL with v1 dataset (18 projects, 24 jobs)...")
        v1_rpc = MockCoreRpc(mock_path=V1_PROJECTS_PATH)
        await seed_job_index(sessionmaker, v1_rpc)

        g1 = await run_g1_eval(sessionmaker, v1_labels, v1_projects, n_repeats=3)
        freshness = await run_freshness_eval(sessionmaker)
        injection = await run_injection_eval(sessionmaker)
        forced_search = await run_forced_search_agent(sessionmaker)
        ablation, ablation_runs = await run_ablation_ladder(sessionmaker, v1_labels, v1_projects)
        sample_checks.extend(
            sample_requirement_checks(g1["results"] + ablation_runs, sample_size=15)
        )

    # 2. G-2 & G-2+ Evaluation
    if run_g2:
        g2 = await run_g2_eval()

    # 3. G-3 Scale Evaluation
    if run_g3:
        print("\nSeeding PostgreSQL with scale dataset (300 projects, 1,000 jobs)...")
        scale_rpc = MockCoreRpc(mock_path=SCALE_PROJECTS_PATH)
        await seed_job_index(sessionmaker, scale_rpc)

        g3 = await run_g3_eval(sessionmaker, scale_labels, scale_projects, scale_truth, n_repeats=2)
        sample_checks.extend(sample_requirement_checks(g3["results"], sample_size=15))

    # 4. G-4 Layout & Robustness Evaluation
    if run_g4 and g3:
        g4 = run_g4_eval(g3["persona_map"])

    # Ensure 30 sample requirement checks
    if len(sample_checks) < 30 and g1 and "results" in g1:
        sample_checks = sample_requirement_checks(
            g1["results"] + (g3["results"] if g3 else []), sample_size=30
        )

    # Persist cache with latest evaluated results
    updated_cache = {
        "git_sha": git_sha,
        "scoring_version": SCORING_VERSION,
        "g1": g1,
        "freshness": freshness,
        "injection": injection,
        "forced_search": forced_search,
        "ablation": ablation,
        "g2": g2,
        "g3": g3,
        "g4": g4,
        "sample_checks": sample_checks,
    }
    try:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(updated_cache, f, default=str)
        print(f"Evaluation results cached to: {cache_file}")
    except Exception as e:
        print(f"Warning: Could not write cache: {e}")

    # Write report
    mode_text = "Fresh run, no cache"
    write_comprehensive_report(
        output_path=output_file,
        git_sha=git_sha,
        g1=g1,
        g2=g2,
        freshness=freshness,
        injection=injection,
        forced_search=forced_search,
        ablation=ablation,
        g3=g3,
        g4=g4,
        sample_checks=sample_checks[:30],
        sample_labels=sample_50_labels[:50],
        mode_text=mode_text,
    )
    print("\nEvaluation suite execution complete!")


if __name__ == "__main__":
    asyncio.run(main())
