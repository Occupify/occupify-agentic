import hashlib
from typing import Any

from pydantic import BaseModel, Field

from app.features.career_rag.schemas import CareerKnowledgeRecord


class Chunk(BaseModel):
    chunk_id: str
    source_id: str
    source_record_id: str
    source_url: str | None = None
    source_version: str = "v1"
    source_type: str
    title: str
    content: str
    chunk_metadata: dict[str, Any] = Field(default_factory=dict)


def compute_chunk_id(source_id: str, source_record_id: str, title: str) -> str:
    """Deterministic hash key for chunk idempotency."""
    key = f"{source_id}:{source_record_id}:{title}".strip()
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:32]


def chunk_record(record: CareerKnowledgeRecord) -> list[Chunk]:
    """Semantic unit chunker adhering to rule.md Rule 3.25-32.

    - For roadmap records: Chunk by milestone / section (Beginner, Intermediate, Advanced)
      and specific topic modules, keeping parent context.
    - For ESCO / O*NET records: Chunk by occupation summary with core competencies,
      and by skill clusters. Avoid mixing unrelated occupations.
    - Preserves metadata (source_id, source_record_id, source_url, source_version,
      source_type, domain, language, tags, parent_title).
    """
    source_meta = record.source_meta
    source_id = source_meta.source_id
    source_record_id = source_meta.source_record_id
    source_url = source_meta.source_url
    source_version = source_meta.source_version
    source_type = source_meta.source_type
    domain = source_meta.domain
    language = source_meta.language or "en"
    geography = source_meta.geography
    tags = list(source_meta.extra.get("related_roles", []))

    chunks: list[Chunk] = []

    if source_id == "roadmap.sh":
        # Roadmap records: chunk by milestone / section
        # If record has parsed sections
        if record.sections:
            for sec in record.sections:
                sec_title = sec.get("title", "").strip() or "General"
                sec_content = sec.get("content", "").strip()
                if not sec_content and not sec_title:
                    continue

                full_title = f"{record.title} - {sec_title}"
                # Keep parent context in content
                content_text = f"# {record.title}\n## {sec_title}\n\n{sec_content}".strip()

                chunk_id = compute_chunk_id(source_id, source_record_id, full_title)
                chunk_meta = {
                    "domain": domain,
                    "language": language,
                    "geography": geography,
                    "tags": tags,
                    "parent_title": record.title,
                    "section_title": sec_title,
                    "source_type": source_type,
                }
                chunks.append(
                    Chunk(
                        chunk_id=chunk_id,
                        source_id=source_id,
                        source_record_id=source_record_id,
                        source_url=source_url,
                        source_version=source_version,
                        source_type=source_type,
                        title=full_title,
                        content=content_text,
                        chunk_metadata=chunk_meta,
                    )
                )
        else:
            # Fallback if no sections
            chunk_id = compute_chunk_id(source_id, source_record_id, record.title)
            chunk_meta = {
                "domain": domain,
                "language": language,
                "geography": geography,
                "tags": tags,
                "parent_title": record.title,
                "source_type": source_type,
            }
            chunks.append(
                Chunk(
                    chunk_id=chunk_id,
                    source_id=source_id,
                    source_record_id=source_record_id,
                    source_url=source_url,
                    source_version=source_version,
                    source_type=source_type,
                    title=record.title,
                    content=record.content,
                    chunk_metadata=chunk_meta,
                )
            )

    elif source_id in ("esco", "onet"):
        # Occupation / taxonomy records:
        # 1. Summary chunk with core competencies & description
        # 2. Skill clusters chunk if skills/competencies exist

        summary_title = f"{record.title} - Overview & Profile"
        summary_parts = [
            f"# {record.title}",
            record.summary or "",
        ]
        if record.raw_attributes.get("isco_group"):
            summary_parts.append(f"ISCO Group: {record.raw_attributes['isco_group']}")
        if record.raw_attributes.get("onet_soc_code"):
            summary_parts.append(f"O*NET-SOC Code: {record.raw_attributes['onet_soc_code']}")

        # Add description / content snippet
        if record.content:
            # First 1000 chars or summary section
            desc_lines = [
                line
                for line in record.content.splitlines()
                if not line.startswith("# Essential Skills")
                and not line.startswith("# Core Tasks")
                and not line.startswith("## Core Tasks")
            ]
            summary_parts.append("\n".join(desc_lines[:40]))

        summary_content = "\n\n".join([p for p in summary_parts if p.strip()]).strip()
        summary_chunk_id = compute_chunk_id(source_id, source_record_id, summary_title)

        summary_meta = {
            "domain": domain,
            "language": language,
            "geography": geography,
            "tags": tags,
            "parent_title": record.title,
            "profile_type": "summary",
            "source_type": source_type,
        }
        chunks.append(
            Chunk(
                chunk_id=summary_chunk_id,
                source_id=source_id,
                source_record_id=source_record_id,
                source_url=source_url,
                source_version=source_version,
                source_type=source_type,
                title=summary_title,
                content=summary_content,
                chunk_metadata=summary_meta,
            )
        )

        # 2. Skill clusters / competencies chunk
        all_skills = list(record.skills)
        all_competencies = list(record.competencies)
        if all_skills or all_competencies:
            skills_title = f"{record.title} - Core Skills & Competencies"
            skills_parts = [
                f"# {record.title}",
                "## Core Competencies and Skills",
            ]
            if all_skills:
                skills_parts.append("### Skills:\n" + "\n".join(f"- {s}" for s in all_skills))
            if all_competencies:
                skills_parts.append(
                    "### Competencies / Abilities:\n"
                    + "\n".join(f"- {c}" for c in all_competencies)
                )

            skills_content = "\n\n".join(skills_parts).strip()
            skills_chunk_id = compute_chunk_id(source_id, source_record_id, skills_title)

            skills_meta = {
                "domain": domain,
                "language": language,
                "geography": geography,
                "tags": tags + [s for s in all_skills[:10]],
                "parent_title": record.title,
                "profile_type": "skills_cluster",
                "source_type": "skill_competency"
                if source_type == "skill_competency"
                else "occupation_taxonomy",
            }
            chunks.append(
                Chunk(
                    chunk_id=skills_chunk_id,
                    source_id=source_id,
                    source_record_id=source_record_id,
                    source_url=source_url,
                    source_version=source_version,
                    source_type=skills_meta["source_type"],
                    title=skills_title,
                    content=skills_content,
                    chunk_metadata=skills_meta,
                )
            )

    else:
        # Default generic semantic chunk
        chunk_id = compute_chunk_id(source_id, source_record_id, record.title)
        chunk_meta = {
            "domain": domain,
            "language": language,
            "geography": geography,
            "tags": tags,
            "parent_title": record.title,
            "source_type": source_type,
        }
        chunks.append(
            Chunk(
                chunk_id=chunk_id,
                source_id=source_id,
                source_record_id=source_record_id,
                source_url=source_url,
                source_version=source_version,
                source_type=source_type,
                title=record.title,
                content=record.content,
                chunk_metadata=chunk_meta,
            )
        )

    return chunks
