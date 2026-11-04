import csv
from collections.abc import Iterator
from pathlib import Path

from app.features.career_rag.schemas import CareerKnowledgeRecord, SourceMetadata


def load_esco_occupations(
    occupations_csv_path: str | Path,
    skill_relations_csv_path: str | Path | None = None,
    limit: int | None = None,
    domain_filter: str | None = None,
) -> Iterator[CareerKnowledgeRecord]:
    """Parse ESCO occupations CSV and optionally join with skill relations."""
    occ_path = Path(occupations_csv_path)
    if not occ_path.exists():
        return

    # Optionally load occupation -> skills map if relations file provided and exists
    skills_by_occ: dict[str, list[dict[str, str]]] = {}
    if skill_relations_csv_path and Path(skill_relations_csv_path).exists():
        with open(skill_relations_csv_path, encoding="utf-8", errors="replace") as rel_f:
            reader = csv.DictReader(rel_f)
            for row in reader:
                occ_uri = row.get("occupationUri", "").strip()
                skill_label = row.get("skillLabel", "").strip()
                rel_type = row.get("relationType", "").strip()
                skill_type = row.get("skillType", "").strip()
                if occ_uri and skill_label:
                    if occ_uri not in skills_by_occ:
                        skills_by_occ[occ_uri] = []
                    skills_by_occ[occ_uri].append(
                        {
                            "label": skill_label,
                            "relation": rel_type,
                            "type": skill_type,
                            "skillUri": row.get("skillUri", "").strip(),
                        }
                    )

    count = 0
    with open(occ_path, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                uri = row.get("conceptUri", "").strip()
                title = row.get("preferredLabel", "").strip()
                description = (
                    row.get("description", "").strip() or row.get("definition", "").strip()
                )
                isco_group = row.get("iscoGroup", "").strip()
                code = row.get("code", "").strip()
                alt_labels_raw = row.get("altLabels", "")
                alt_labels = (
                    [
                        lbl.strip()
                        for lbl in alt_labels_raw.replace("\r", "\n").split("\n")
                        if lbl.strip()
                    ]
                    if alt_labels_raw
                    else []
                )

                if not title:
                    continue

                if domain_filter:
                    match_domain = (
                        domain_filter.lower() in title.lower()
                        or domain_filter.lower() in description.lower()
                        or any(domain_filter.lower() in alt.lower() for alt in alt_labels)
                    )
                    if not match_domain:
                        continue

                # Extract related skills if available
                related_skill_entries = skills_by_occ.get(uri, [])
                essential_skills = [
                    s["label"] for s in related_skill_entries if s["relation"] == "essential"
                ]
                optional_skills = [
                    s["label"] for s in related_skill_entries if s["relation"] == "optional"
                ]

                # Synthesize readable markdown content
                content_lines = [
                    f"# {title}",
                    f"**ISCO Group:** {isco_group}" if isco_group else "",
                    f"**Code:** {code}" if code else "",
                    "\n## Description",
                    description,
                ]

                if alt_labels:
                    content_lines.extend(["\n## Alternative Titles", ", ".join(alt_labels)])

                if essential_skills:
                    content_lines.extend(
                        ["\n## Essential Skills & Knowledge"]
                        + [f"- {s}" for s in essential_skills[:30]]
                    )

                if optional_skills:
                    content_lines.extend(
                        ["\n## Optional Skills & Knowledge"]
                        + [f"- {s}" for s in optional_skills[:20]]
                    )

                content = "\n".join(line for line in content_lines if line is not None).strip()

                source_record_id = uri.split("/")[-1] if uri else f"esco-occ-{count}"

                source_meta = SourceMetadata(
                    source_id="esco",
                    source_record_id=source_record_id,
                    source_url=uri
                    if uri.startswith("http")
                    else f"http://data.europa.eu/esco/occupation/{source_record_id}",
                    source_version="v1.1",
                    source_type="occupation_taxonomy",
                    domain=isco_group,
                    geography="EU",
                    language="en",
                    license="ODbL / European Commission",
                    extra={
                        "isco_group": isco_group,
                        "code": code,
                        "conceptUri": uri,
                        "alt_labels": alt_labels,
                    },
                )

                record = CareerKnowledgeRecord(
                    source_meta=source_meta,
                    title=title,
                    content=content,
                    summary=description[:250] + ("..." if len(description) > 250 else ""),
                    skills=essential_skills + optional_skills,
                    competencies=essential_skills,
                    relations=related_skill_entries,
                    raw_attributes=row,
                )
                yield record

                count += 1
                if limit and count >= limit:
                    break
            except Exception:
                continue


def load_esco_skills(
    skills_csv_path: str | Path,
    limit: int | None = None,
    domain_filter: str | None = None,
) -> Iterator[CareerKnowledgeRecord]:
    """Parse ESCO skills CSV into skill_competency records."""
    skills_path = Path(skills_csv_path)
    if not skills_path.exists():
        return

    count = 0
    with open(skills_path, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                uri = row.get("conceptUri", "").strip()
                title = row.get("preferredLabel", "").strip()
                skill_type = row.get("skillType", "").strip()
                reuse_level = row.get("reuseLevel", "").strip()
                description = (
                    row.get("description", "").strip() or row.get("definition", "").strip()
                )
                alt_labels_raw = row.get("altLabels", "")
                alt_labels = (
                    [
                        lbl.strip()
                        for lbl in alt_labels_raw.replace("\r", "\n").split("\n")
                        if lbl.strip()
                    ]
                    if alt_labels_raw
                    else []
                )

                if not title:
                    continue

                if domain_filter:
                    match_domain = (
                        domain_filter.lower() in title.lower()
                        or domain_filter.lower() in description.lower()
                        or any(domain_filter.lower() in alt.lower() for alt in alt_labels)
                    )
                    if not match_domain:
                        continue

                content = (
                    f"# Skill: {title}\n"
                    f"**Type:** {skill_type} | **Reuse Level:** {reuse_level}\n\n"
                    f"## Description\n{description}"
                ).strip()

                source_record_id = uri.split("/")[-1] if uri else f"esco-skill-{count}"

                source_meta = SourceMetadata(
                    source_id="esco",
                    source_record_id=source_record_id,
                    source_url=uri
                    if uri.startswith("http")
                    else f"http://data.europa.eu/esco/skill/{source_record_id}",
                    source_version="v1.1",
                    source_type="skill_competency",
                    domain=skill_type,
                    geography="EU",
                    language="en",
                    license="ODbL / European Commission",
                    extra={"reuse_level": reuse_level, "skill_type": skill_type},
                )

                record = CareerKnowledgeRecord(
                    source_meta=source_meta,
                    title=title,
                    content=content,
                    summary=description[:250],
                    skills=[title],
                    competencies=[],
                    raw_attributes=row,
                )
                yield record

                count += 1
                if limit and count >= limit:
                    break
            except Exception:
                continue
