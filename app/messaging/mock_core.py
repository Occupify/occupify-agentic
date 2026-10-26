import json
import os
import unicodedata
from copy import deepcopy
from pathlib import Path
from typing import Any

from app.core.config import get_settings


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


class MockCoreRpc:
    """
    Mock RPC client simulating core's RabbitMQ replies for core.project.search and core.project.get.
    Returns exactly what RpcClient.call returns.
    """

    def __init__(self, mock_path: str | Path | None = None):
        settings = get_settings()
        self.mock_path = Path(mock_path or os.getenv("CORE_MOCK_PATH") or settings.CORE_MOCK_PATH)
        self._load_projects()

    def _load_projects(self) -> None:
        if not self.mock_path.is_absolute():
            # Resolve relative to repo root if possible
            base_dir = Path(__file__).resolve().parents[2]
            target = base_dir / self.mock_path
            if target.exists():
                self.mock_path = target

        if self.mock_path.exists():
            with open(self.mock_path, encoding="utf-8") as f:
                self._projects: list[dict[str, Any]] = json.load(f)
        else:
            self._projects = []

    def _get_overlay(self) -> dict[str, Any]:
        settings = get_settings()
        overlay_val = (
            os.getenv("CORE_MOCK_GET_OVERLAY") or settings.CORE_MOCK_GET_OVERLAY or ""
        ).strip()
        if not overlay_val:
            return {}
        try:
            # Check if it's a file path
            p = Path(overlay_val)
            if p.exists():
                return json.loads(p.read_text(encoding="utf-8"))
            # Otherwise JSON string
            return json.loads(overlay_val)
        except Exception:
            return {}

    async def call(self, routing_key: str, args: dict[str, Any]) -> dict[str, Any]:
        if routing_key == "core.project.search":
            return self._handle_search(args)
        elif routing_key == "core.project.get":
            return self._handle_get(args)
        else:
            return {
                "ok": False,
                "error": {
                    "code": "NOT_MOCKED",
                    "message": f"Routing key '{routing_key}' is not mocked.",
                },
            }

    def _handle_search(self, args: dict[str, Any]) -> dict[str, Any]:
        keyword = (args.get("keyword") or "").strip()
        status_filter = args.get("status")
        period_filter = args.get("period")
        exp_filter = args.get("experienceLevel")
        min_price = args.get("minPrice")
        max_price = args.get("maxPrice")
        skills_filter = [s.strip().lower() for s in (args.get("skills") or []) if s.strip()]

        page = int(args.get("page", 0))
        size = min(int(args.get("size", 20)), 50)

        results: list[dict[str, Any]] = []

        for p in self._projects:
            # Default search returns projects that are OPEN with >= 1 RECRUITING job
            p_status = p.get("status")
            if status_filter:
                if p_status != status_filter:
                    continue
            else:
                # Default behaviour: must be OPEN and have recruiting jobs
                if p_status != "OPEN":
                    continue

            recruiting_jobs = [j for j in p.get("jobs", []) if j.get("status") == "RECRUITING"]
            if not status_filter and len(recruiting_jobs) == 0:
                continue

            # Period
            if period_filter and p.get("period") != period_filter:
                continue

            # Experience Level
            if exp_filter and p.get("experienceLevel") != exp_filter:
                continue

            # Price overlap (on startPrice or job budgets)
            if min_price is not None or max_price is not None:
                has_overlap = False
                for j in p.get("jobs", []):
                    b_min = j.get("budgetMin")
                    b_max = j.get("budgetMax")
                    if b_min is None and b_max is None:
                        continue
                    min_ok = True
                    max_ok = True
                    if min_price is not None:
                        cond1 = b_max is not None and b_max >= min_price
                        cond2 = b_min is not None and b_min >= min_price
                        min_ok = cond1 or cond2
                    if max_price is not None:
                        cond1 = b_min is not None and b_min <= max_price
                        cond2 = b_max is not None and b_max <= max_price
                        max_ok = cond1 or cond2
                    if min_ok and max_ok:
                        has_overlap = True
                        break
                if not has_overlap:
                    continue

            # Skills filter (OR-ed accent-insensitive)
            if skills_filter:
                proj_skills = [
                    strip_accents(s).lower() for j in p.get("jobs", []) for s in j.get("skills", [])
                ]
                match_any_skill = any(
                    strip_accents(sf).lower() in proj_skills for sf in skills_filter
                )
                if not match_any_skill:
                    continue

            # Keyword filter (accent & case-insensitive over project & recruiting jobs)
            if keyword:
                kw_norm = strip_accents(keyword).lower()
                blob_parts = [
                    p.get("title", ""),
                    p.get("description", ""),
                ]
                for j in recruiting_jobs:
                    blob_parts.extend(
                        [
                            j.get("title", ""),
                            j.get("description", ""),
                            " ".join(j.get("skills", [])),
                        ]
                    )
                blob_norm = strip_accents(" ".join(blob_parts)).lower()
                if kw_norm not in blob_norm:
                    continue

            results.append(deepcopy(p))

        # Sort createdAt desc by default
        results.sort(key=lambda x: x.get("createdAt", ""), reverse=True)

        total = len(results)
        total_pages = (total + size - 1) // size if size > 0 else 1
        start_idx = page * size
        end_idx = start_idx + size
        paged_data = results[start_idx:end_idx]

        return {
            "ok": True,
            "data": {
                "statusCode": 200,
                "message": "Projects retrieved successfully.",
                "data": paged_data,
                "paging": {
                    "page": page,
                    "limit": size,
                    "total": total,
                    "totalPages": total_pages,
                },
            },
        }

    def _handle_get(self, args: dict[str, Any]) -> dict[str, Any]:
        project_id = str(args.get("projectId") or "").strip()
        found: dict[str, Any] | None = None
        for p in self._projects:
            if p.get("id") == project_id:
                found = deepcopy(p)
                break

        if not found:
            return {
                "ok": False,
                "error": {
                    "code": "PROJECT_NOT_FOUND",
                    "message": f"Project '{project_id}' not found.",
                },
            }

        # Apply overlay if present
        overlay = self._get_overlay()
        if project_id in overlay:
            overrides = overlay[project_id]
            for k, v in overrides.items():
                if k == "jobs" and isinstance(v, list):
                    # Merge jobs by ID
                    job_override_map = {j["id"]: j for j in v if "id" in j}
                    for j in found.get("jobs", []):
                        jid = j.get("id")
                        if jid in job_override_map:
                            j.update(job_override_map[jid])
                else:
                    found[k] = v

        return {
            "ok": True,
            "data": {
                "statusCode": 200,
                "message": "Project detail retrieved successfully.",
                "data": found,
            },
        }
