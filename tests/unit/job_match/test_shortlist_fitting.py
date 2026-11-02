from decimal import Decimal
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.core.security import CurrentUser
from app.documents.cv_text import CvText
from app.features.job_match.pipeline import run_pipeline
from app.features.job_match.ports import IndexRow, PipelineOptions
from app.features.job_match.schemas import RunOutcome


def make_mock_row(
    job_id: str,
    project_id: str,
    title: str = "Developer",
    skills: list[str] = None,
    budget_min: Decimal = None,
    budget_max: Decimal = None,
) -> IndexRow:
    return IndexRow(
        job_id=job_id,
        project_id=project_id,
        project_title=f"Project {project_id}",
        project_description="Project Description",
        job_title=title,
        job_description="Job Description",
        skills=skills or ["Python"],
        requirements=[],
        project_status="OPEN",
        job_status="RECRUITING",
        doc_text=f"{title} Python",
    )


@pytest.fixture
def mock_cv():
    return CvText(
        text=(
            "Candidate Test\n"
            "## Experience\n"
            "Software Engineer with 4 years Python and PostgreSQL experience.\n"
            "## Skills\n"
            "Python, PostgreSQL"
        ),
        removed={},
    )


@pytest.fixture
def test_user():
    return CurrentUser(user_id="u-fitting", role="ROLE_USER", email="u-fitting@test.com")


@pytest.fixture(autouse=True)
def default_skill_models():
    from app.agents.subagent import override_skill_models
    from tests.unit.job_match.fakes import default_test_overrides

    with override_skill_models(default_test_overrides()):
        yield


@pytest.mark.asyncio
async def test_only_fitting_projects_listed(mock_cv, test_user):
    rows = [
        make_mock_row("j1", "p1", "Python Dev", ["Python"]),
        make_mock_row("j2", "p2", "Golang Dev", ["Golang"]),
    ]

    mock_store = MagicMock()
    hit1 = MagicMock(job_id="j1", project_id="p1", rank=1, score=0.9)
    hit2 = MagicMock(job_id="j2", project_id="p2", rank=2, score=0.1)
    mock_store.hybrid_search = AsyncMock(return_value=([[hit1, hit2]], [hit1, hit2]))
    mock_store.get_rows = AsyncMock(return_value=rows)

    mock_rpc = MagicMock()
    mock_rpc.call = AsyncMock(
        return_value={
            "ok": True,
            "data": {
                "status": "OPEN",
                "jobs": [
                    {"id": "j1", "status": "RECRUITING"},
                    {"id": "j2", "status": "RECRUITING"},
                ],
            },
        }
    )

    with patch("app.features.job_match.pipeline.compute_project_scores") as mock_scores:

        def fake_compute(jobs):
            if any(j["job_id"] == "j1" for j in jobs):
                return 80, [jobs[0]]
            return 20, []

        mock_scores.side_effect = fake_compute

        res = await run_pipeline(
            cv_text=mock_cv,
            user=test_user,
            store=mock_store,
            core_rpc=mock_rpc,
            options=PipelineOptions(rerank=False, search_agent=False),
        )

    assert res.outcome == RunOutcome.OK
    assert len(res.items) == 1
    assert res.items[0]["projectId"] == "p1"


@pytest.mark.asyncio
async def test_only_fitting_jobs_inside_a_project(mock_cv, test_user):
    rows = [
        make_mock_row("j1", "p1", "Python Lead", ["Python"]),
        make_mock_row("j2", "p1", "Java Junior", ["Java"]),
    ]

    mock_store = MagicMock()
    hit1 = MagicMock(job_id="j1", project_id="p1", rank=1, score=0.9)
    hit2 = MagicMock(job_id="j2", project_id="p1", rank=2, score=0.2)
    mock_store.hybrid_search = AsyncMock(return_value=([[hit1, hit2]], [hit1, hit2]))
    mock_store.get_rows = AsyncMock(return_value=rows)

    mock_rpc = MagicMock()
    mock_rpc.call = AsyncMock(
        return_value={
            "ok": True,
            "data": {
                "status": "OPEN",
                "jobs": [
                    {"id": "j1", "status": "RECRUITING"},
                    {"id": "j2", "status": "RECRUITING"},
                ],
            },
        }
    )

    with patch("app.features.job_match.pipeline.compute_project_scores") as mock_scores:

        def fake_compute(jobs):
            fitting = [j for j in jobs if j["job_id"] == "j1"]
            return 85, fitting

        mock_scores.side_effect = fake_compute

        res = await run_pipeline(
            cv_text=mock_cv,
            user=test_user,
            store=mock_store,
            core_rpc=mock_rpc,
            options=PipelineOptions(rerank=False, search_agent=False),
        )

    assert len(res.items) == 1
    proj_jobs = res.items[0]["jobs"]
    assert len(proj_jobs) == 1
    assert proj_jobs[0]["jobId"] == "j1"


@pytest.mark.asyncio
async def test_fewer_than_10_when_fewer_fit(mock_cv, test_user):
    rows = [make_mock_row(f"j{i}", f"p{i}") for i in range(1, 16)]
    hits = [
        MagicMock(job_id=f"j{i}", project_id=f"p{i}", rank=i, score=1.0 - i * 0.05)
        for i in range(1, 16)
    ]

    mock_store = MagicMock()
    mock_store.hybrid_search = AsyncMock(return_value=([hits], hits))
    mock_store.get_rows = AsyncMock(return_value=rows)

    mock_rpc = MagicMock()
    mock_rpc.call = AsyncMock(
        side_effect=lambda method, args: {
            "ok": True,
            "data": {
                "status": "OPEN",
                "jobs": [{"id": f"j{args.get('projectId')[1:]}", "status": "RECRUITING"}],
            },
        }
    )

    with patch("app.features.job_match.pipeline.compute_project_scores") as mock_scores:

        def fake_compute(jobs):
            jid = jobs[0]["job_id"]
            if jid in ("j1", "j2"):
                return 80, [jobs[0]]
            return 20, []

        mock_scores.side_effect = fake_compute

        res = await run_pipeline(
            cv_text=mock_cv,
            user=test_user,
            store=mock_store,
            core_rpc=mock_rpc,
            options=PipelineOptions(rerank=False, search_agent=False),
        )

    assert len(res.items) == 2
    assert [it["projectId"] for it in res.items] == ["p1", "p2"]


@pytest.mark.asyncio
async def test_freshness_refill_uses_only_fitting_projects(mock_cv, test_user):
    rows = [make_mock_row(f"j{i}", f"p{i}") for i in range(1, 5)]
    hits = [
        MagicMock(job_id=f"j{i}", project_id=f"p{i}", rank=i, score=0.9 - i * 0.1)
        for i in range(1, 5)
    ]

    mock_store = MagicMock()
    mock_store.hybrid_search = AsyncMock(return_value=([hits], hits))
    mock_store.get_rows = AsyncMock(return_value=rows)

    def fake_rpc_refill(method, args):
        pid = args.get("projectId")
        return {
            "ok": True,
            "data": {
                "status": "CLOSED" if pid == "p1" else "OPEN",
                "jobs": [{"id": f"j{pid[1:]}", "status": "RECRUITING"}],
            },
        }

    mock_rpc = MagicMock()
    mock_rpc.call = AsyncMock(side_effect=fake_rpc_refill)

    with patch("app.features.job_match.pipeline.compute_project_scores") as mock_scores:

        def fake_compute(jobs):
            jid = jobs[0]["job_id"]
            if jid in ("j1", "j2", "j3"):
                return 80, [jobs[0]]
            return 20, []

        mock_scores.side_effect = fake_compute

        res = await run_pipeline(
            cv_text=mock_cv,
            user=test_user,
            store=mock_store,
            core_rpc=mock_rpc,
            options=PipelineOptions(rerank=False, search_agent=False, list_size=2),
        )

    pids = [it["projectId"] for it in res.items]
    assert "p1" not in pids
    assert "p4" not in pids
    assert pids == ["p2", "p3"]


@pytest.mark.asyncio
async def test_ranks_contiguous_after_drop(mock_cv, test_user):
    rows = [make_mock_row(f"j{i}", f"p{i}") for i in range(1, 4)]
    hits = [
        MagicMock(job_id=f"j{i}", project_id=f"p{i}", rank=i, score=0.9 - i * 0.1)
        for i in range(1, 4)
    ]

    mock_store = MagicMock()
    mock_store.hybrid_search = AsyncMock(return_value=([hits], hits))
    mock_store.get_rows = AsyncMock(return_value=rows)

    def fake_rpc_drop(method, args):
        pid = args.get("projectId")
        return {
            "ok": True,
            "data": {
                "status": "CLOSED" if pid == "p2" else "OPEN",
                "jobs": [{"id": f"j{pid[1:]}", "status": "RECRUITING"}],
            },
        }

    mock_rpc = MagicMock()
    mock_rpc.call = AsyncMock(side_effect=fake_rpc_drop)

    with patch("app.features.job_match.pipeline.compute_project_scores") as mock_scores:
        mock_scores.side_effect = lambda jobs: (80, [jobs[0]])

        res = await run_pipeline(
            cv_text=mock_cv,
            user=test_user,
            store=mock_store,
            core_rpc=mock_rpc,
            options=PipelineOptions(rerank=False, search_agent=False),
        )

    assert len(res.items) == 2
    ranks = [it["rank"] for it in res.items]
    assert ranks == [1, 2]


@pytest.mark.asyncio
async def test_no_match_unchanged(mock_cv, test_user):
    rows = [make_mock_row("j1", "p1")]
    hits = [MagicMock(job_id="j1", project_id="p1", rank=1, score=0.2)]

    mock_store = MagicMock()
    mock_store.hybrid_search = AsyncMock(return_value=([hits], hits))
    mock_store.get_rows = AsyncMock(return_value=rows)

    with patch("app.features.job_match.pipeline.compute_project_scores", return_value=(20, [])):
        res = await run_pipeline(
            cv_text=mock_cv,
            user=test_user,
            store=mock_store,
            options=PipelineOptions(rerank=False, search_agent=False),
        )

    assert res.outcome == RunOutcome.NO_MATCH
    assert len(res.items) == 0


@pytest.mark.asyncio
async def test_order_by_best_fitting_job(mock_cv, test_user):
    rows = [
        make_mock_row("j1", "p1"),
        make_mock_row("j2", "p2"),
    ]
    hits = [
        MagicMock(job_id="j1", project_id="p1", rank=1, score=0.8),
        MagicMock(job_id="j2", project_id="p2", rank=2, score=0.8),
    ]

    mock_store = MagicMock()
    mock_store.hybrid_search = AsyncMock(return_value=([hits], hits))
    mock_store.get_rows = AsyncMock(return_value=rows)

    mock_rpc = MagicMock()
    mock_rpc.call = AsyncMock(
        return_value={
            "ok": True,
            "data": {
                "status": "OPEN",
                "jobs": [
                    {"id": "j1", "status": "RECRUITING"},
                    {"id": "j2", "status": "RECRUITING"},
                ],
            },
        }
    )

    with patch("app.features.job_match.pipeline.compute_project_scores") as mock_scores:

        def fake_compute(jobs):
            if jobs[0]["job_id"] == "j1":
                return 75, [jobs[0]]
            return 90, [jobs[0]]

        mock_scores.side_effect = fake_compute

        res = await run_pipeline(
            cv_text=mock_cv,
            user=test_user,
            store=mock_store,
            core_rpc=mock_rpc,
            options=PipelineOptions(rerank=False, search_agent=False),
        )

    assert len(res.items) == 2
    assert res.items[0]["projectId"] == "p2"
    assert res.items[1]["projectId"] == "p1"
