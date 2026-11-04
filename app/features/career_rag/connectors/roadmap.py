from collections.abc import Iterator
from pathlib import Path

from app.features.career_rag.schemas import CareerKnowledgeRecord, SourceMetadata


def parse_roadmap_markdown(
    file_path: str | Path, content: str | None = None
) -> CareerKnowledgeRecord:
    """Parse a single roadmap.sh markdown file into a normalized CareerKnowledgeRecord."""
    path = Path(file_path)
    if content is None:
        content = path.read_text(encoding="utf-8")

    lines = content.splitlines()

    title = ""
    domain = None
    source_url = None
    related_roles: list[str] = []

    # Parse title (first # Header)
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# ") and not title:
            title = stripped[2:].strip()
            break

    if not title:
        title = path.stem.replace("_", " ").title()

    # Parse metadata section
    in_metadata = False
    in_related = False

    for line in lines:
        stripped = line.strip()
        if stripped == "## Metadata":
            in_metadata = True
            continue
        elif in_metadata and stripped.startswith("## "):
            in_metadata = False
            in_related = False
        elif in_metadata and stripped.startswith("---"):
            in_metadata = False
            in_related = False

        if in_metadata:
            if stripped.startswith("- Type:"):
                # e.g., Role or Skill
                pass
            elif stripped.startswith("- Domain:"):
                domain = stripped.split("- Domain:", 1)[1].strip()
            elif stripped.startswith("- Source URL:"):
                source_url = stripped.split("- Source URL:", 1)[1].strip()
            elif stripped.startswith("- Related Roles:"):
                in_related = True
            elif in_related:
                if stripped.startswith("- "):
                    role = stripped[2:].strip()
                    if role:
                        related_roles.append(role)
                else:
                    in_related = False

    # Determine whether it's role or skill based from path or metadata
    is_role = "1_role_based" in str(path) or "/roles/" in str(path)
    source_type = "learning_roadmap" if is_role else "skill_competency"

    # Extract sections (e.g., ## 1. Beginner, ### 1.1 Intro)
    sections: list[dict[str, str]] = []
    current_sec_title = "Overview"
    current_sec_lines: list[str] = []

    for line in lines:
        if line.startswith("## ") and not line.startswith("## Metadata"):
            if current_sec_lines:
                sections.append(
                    {"title": current_sec_title, "content": "\n".join(current_sec_lines).strip()}
                )
                current_sec_lines = []
            current_sec_title = line[3:].strip()
        elif line.startswith("### "):
            if current_sec_lines:
                sections.append(
                    {"title": current_sec_title, "content": "\n".join(current_sec_lines).strip()}
                )
                current_sec_lines = []
            current_sec_title = line[4:].strip()
        else:
            if not in_metadata or not line.startswith("## Metadata"):
                current_sec_lines.append(line)

    if current_sec_lines:
        sections.append(
            {"title": current_sec_title, "content": "\n".join(current_sec_lines).strip()}
        )

    source_record_id = path.stem

    source_meta = SourceMetadata(
        source_id="roadmap.sh",
        source_record_id=source_record_id,
        source_url=source_url or f"https://roadmap.sh/{path.stem.replace('_', '-')}",
        source_version="v1",
        source_type=source_type,
        domain=domain,
        geography="Global",
        language="en",
        license="Community / CC BY-NC-SA 4.0",
        extra={"related_roles": related_roles, "file_path": str(path)},
    )

    return CareerKnowledgeRecord(
        source_meta=source_meta,
        title=title,
        content=content.strip(),
        summary=f"{title} ({domain or 'General'}) Roadmap",
        skills=related_roles,
        sections=sections,
        raw_attributes={"line_count": len(lines)},
    )


def load_roadmap_directory(
    base_dir: str | Path,
    domain_filter: str | None = None,
    limit: int | None = None,
) -> Iterator[CareerKnowledgeRecord]:
    """Recursively yields CareerKnowledgeRecords from roadmap.sh markdown directory."""
    dir_path = Path(base_dir)
    if not dir_path.exists():
        return

    count = 0
    for md_file in sorted(dir_path.rglob("*.md")):
        if domain_filter and domain_filter.lower() not in str(md_file).lower():
            continue
        try:
            record = parse_roadmap_markdown(md_file)
            yield record
            count += 1
            if limit and count >= limit:
                break
        except Exception:
            # Quarantine/skip malformed file without crashing pipeline
            continue
