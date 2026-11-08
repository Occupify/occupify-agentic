import csv
from collections.abc import Iterator
from pathlib import Path

from app.features.career_rag.schemas import CareerKnowledgeRecord, SourceMetadata


def load_onet_occupations(
    occupation_data_csv_path: str | Path,
    essential_skills_csv_path: str | Path | None = None,
    abilities_csv_path: str | Path | None = None,
    task_statements_csv_path: str | Path | None = None,
    limit: int | None = None,
    domain_filter: str | None = None,
) -> Iterator[CareerKnowledgeRecord]:
    """Parse O*NET occupation_data.csv and join with essential skills, abilities, and tasks."""
    occ_path = Path(occupation_data_csv_path)
    if not occ_path.exists():
        return

    # Load skills indexed by SOC code
    skills_by_soc: dict[str, list[dict[str, str]]] = {}
    if essential_skills_csv_path and Path(essential_skills_csv_path).exists():
        with open(essential_skills_csv_path, encoding="utf-8", errors="replace") as f:
            reader = csv.DictReader(f)
            for row in reader:
                soc = row.get("O*NET-SOC Code", "").strip()
                name = row.get("Element Name", "").strip()
                scale = row.get("Scale ID", "").strip()
                val = row.get("Data Value", "").strip()
                # Focus on Importance scale (IM) or high value elements
                if soc and name and (scale == "IM" or not scale):
                    if soc not in skills_by_soc:
                        skills_by_soc[soc] = []
                    skills_by_soc[soc].append({"name": name, "value": val})

    # Load abilities indexed by SOC code
    abilities_by_soc: dict[str, list[dict[str, str]]] = {}
    if abilities_csv_path and Path(abilities_csv_path).exists():
        with open(abilities_csv_path, encoding="utf-8", errors="replace") as f:
            reader = csv.DictReader(f)
            for row in reader:
                soc = row.get("O*NET-SOC Code", "").strip()
                name = row.get("Element Name", "").strip()
                scale = row.get("Scale ID", "").strip()
                val = row.get("Data Value", "").strip()
                if soc and name and (scale == "IM" or not scale):
                    if soc not in abilities_by_soc:
                        abilities_by_soc[soc] = []
                    abilities_by_soc[soc].append({"name": name, "value": val})

    # Load core tasks indexed by SOC code
    tasks_by_soc: dict[str, list[str]] = {}
    if task_statements_csv_path and Path(task_statements_csv_path).exists():
        with open(task_statements_csv_path, encoding="utf-8", errors="replace") as f:
            reader = csv.DictReader(f)
            for row in reader:
                soc = row.get("O*NET-SOC Code", "").strip()
                task = row.get("Task", "").strip()
                task_type = row.get("Task Type", "").strip()
                if soc and task:
                    if soc not in tasks_by_soc:
                        tasks_by_soc[soc] = []
                    # Keep Core or all if few
                    tasks_by_soc[soc].append(f"[{task_type}] {task}" if task_type else task)

    count = 0
    with open(occ_path, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                soc_code = row.get("O*NET-SOC Code", "").strip()
                title = row.get("Title", "").strip()
                description = row.get("Description", "").strip()

                if not title or not soc_code:
                    continue

                if domain_filter:
                    match_domain = (
                        domain_filter.lower() in title.lower()
                        or domain_filter.lower() in description.lower()
                        or domain_filter.lower() in soc_code.lower()
                    )
                    if not match_domain:
                        continue

                occ_skills = skills_by_soc.get(soc_code, [])
                occ_abilities = abilities_by_soc.get(soc_code, [])
                occ_tasks = tasks_by_soc.get(soc_code, [])

                # Format human & embedding readable content
                content_lines = [
                    f"# {title} (O*NET-SOC {soc_code})",
                    "\n## Description",
                    description,
                ]

                if occ_skills:
                    content_lines.extend(
                        ["\n## Essential Skills"]
                        + [
                            f"- {s['name']}"
                            + (f" (Importance: {s['value']})" if s["value"] else "")
                            for s in occ_skills[:20]
                        ]
                    )

                if occ_abilities:
                    content_lines.extend(
                        ["\n## Key Abilities"]
                        + [
                            f"- {a['name']}"
                            + (f" (Importance: {a['value']})" if a["value"] else "")
                            for a in occ_abilities[:20]
                        ]
                    )

                if occ_tasks:
                    content_lines.extend(
                        ["\n## Core Tasks & Work Activities"] + [f"- {t}" for t in occ_tasks[:15]]
                    )

                content = "\n".join(content_lines).strip()

                source_meta = SourceMetadata(
                    source_id="onet",
                    source_record_id=soc_code,
                    source_url=f"https://www.onetonline.org/link/summary/{soc_code}",
                    source_version="v28.0",
                    source_type="occupation_taxonomy",
                    domain=soc_code.split("-")[0] if "-" in soc_code else None,
                    geography="US",
                    language="en",
                    license="CC BY 4.0 / US Department of Labor",
                    extra={
                        "soc_code": soc_code,
                        "skills_count": len(occ_skills),
                        "abilities_count": len(occ_abilities),
                        "tasks_count": len(occ_tasks),
                    },
                )

                skills_list = [s["name"] for s in occ_skills]
                abilities_list = [a["name"] for a in occ_abilities]

                record = CareerKnowledgeRecord(
                    source_meta=source_meta,
                    title=title,
                    content=content,
                    summary=description[:250] + ("..." if len(description) > 250 else ""),
                    skills=skills_list,
                    competencies=abilities_list,
                    relations=[{"type": "skill", "name": s["name"]} for s in occ_skills]
                    + [{"type": "ability", "name": a["name"]} for a in occ_abilities],
                    raw_attributes=row,
                )
                yield record

                count += 1
                if limit and count >= limit:
                    break
            except Exception:
                continue
