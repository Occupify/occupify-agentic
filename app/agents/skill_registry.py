import argparse
import hashlib
import importlib
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel

ALLOWED_TOOLS = {"search_more", "search_filter_projects", "get_project_detail"}


class SkillValidationError(Exception):
    """Raised when skill validation fails."""

    pass


@dataclass
class SkillMeta:
    name: str
    description: str
    output_str: str
    output_type: type[BaseModel]
    shared_references: list[str] = field(default_factory=list)
    tools: list[str] = field(default_factory=list)
    used_by: list[str] = field(default_factory=list)
    prompt: str = ""
    skill_version: str = ""
    path: Path | None = None


def _parse_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    fm_str = parts[1]
    body = parts[2].lstrip("\r\n")
    data = yaml.safe_load(fm_str) or {}
    return data, body


def _resolve_model(model_str: str) -> type[BaseModel]:
    if "." not in model_str:
        raise ImportError(f"Invalid model path: {model_str}")
    module_name, class_name = model_str.rsplit(".", 1)
    mod = importlib.import_module(module_name)
    cls = getattr(mod, class_name)
    if not isinstance(cls, type) or not issubclass(cls, BaseModel):
        raise TypeError(f"{model_str} is not a Pydantic BaseModel")
    return cls


def assemble_skill_prompt(
    skill_dir: Path,
    body: str,
    shared_refs: list[str],
    shared_root: Path | None = None,
) -> str:
    sections = [body.strip()]

    # 1. Shared references (in frontmatter order)
    if shared_root is not None:
        for ref in shared_refs:
            ref_path = shared_root / ref
            if ref_path.exists():
                sections.append(ref_path.read_text(encoding="utf-8").strip())

    # 2. Own references (alphabetically sorted)
    own_refs_dir = skill_dir / "references"
    if own_refs_dir.exists() and own_refs_dir.is_dir():
        for ref_file in sorted(own_refs_dir.glob("*.md")):
            sections.append(ref_file.read_text(encoding="utf-8").strip())

    # 3. Examples (alphabetically sorted)
    examples_dir = skill_dir / "examples"
    if examples_dir.exists() and examples_dir.is_dir():
        for ex_file in sorted(examples_dir.glob("*")):
            if ex_file.is_file():
                sections.append(ex_file.read_text(encoding="utf-8").strip())

    return "\n\n".join(s for s in sections if s)


class SkillRegistry:
    def __init__(self) -> None:
        self._skills: dict[str, SkillMeta] = {}

    def scan(self, root_dir: Path) -> None:
        self._skills.clear()
        if not root_dir.exists():
            return

        shared_root = root_dir / "_shared" / "references"
        skill_files = list(root_dir.rglob("SKILL.md"))
        for sf in skill_files:
            content = sf.read_text(encoding="utf-8")
            fm, body = _parse_frontmatter(content)
            name = fm.get("name")
            if not name:
                continue

            output_str = fm.get("output", "")
            try:
                out_type = _resolve_model(output_str)
            except Exception:
                out_type = None

            shared_refs = fm.get("shared_references", [])
            tools = fm.get("tools", [])
            used_by = fm.get("used_by", [])
            skill_dir = sf.parent

            prompt = assemble_skill_prompt(skill_dir, body, shared_refs, shared_root=shared_root)
            v = hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:12]

            self._skills[name] = SkillMeta(
                name=name,
                description=fm.get("description", ""),
                output_str=output_str,
                output_type=out_type,
                shared_references=shared_refs,
                tools=tools,
                used_by=used_by,
                prompt=prompt,
                skill_version=v,
                path=skill_dir,
            )

    def get(self, name: str) -> SkillMeta | None:
        return self._skills.get(name)

    def list_skills(self) -> list[SkillMeta]:
        return list(self._skills.values())


def validate_skills_directory(skills_dir: Path) -> list[str]:
    if not skills_dir.exists():
        return []

    errors: list[str] = []
    seen_names: dict[str, Path] = {}
    skill_files = list(skills_dir.rglob("SKILL.md"))

    # Shared root could be skills/_shared/references or inside skills_dir
    shared_root = skills_dir / "_shared" / "references"
    if not shared_root.exists() and skills_dir.name != "skills":
        parent_shared = Path("skills/_shared/references")
        if parent_shared.exists():
            shared_root = parent_shared

    for sf in skill_files:
        content = sf.read_text(encoding="utf-8")
        fm, _ = _parse_frontmatter(content)
        name = fm.get("name")
        if not name:
            errors.append(f"Missing skill name in {sf}")
            continue

        if name in seen_names:
            errors.append(f"Duplicate skill name '{name}' found in {sf} and {seen_names[name]}")
        seen_names[name] = sf

        # Check output model
        output_str = fm.get("output")
        if not output_str:
            errors.append(f"Missing output model in {sf}")
        else:
            try:
                out_cls = _resolve_model(output_str)
            except Exception as e:
                errors.append(f"Output model '{output_str}' in {sf} cannot be imported: {e}")
                out_cls = None

        # Check shared references
        shared_refs = fm.get("shared_references", [])
        for ref in shared_refs:
            ref_path = shared_root / ref
            if not ref_path.exists():
                errors.append(f"Missing shared reference '{ref}' in {sf} (looked at {ref_path})")

        # Check tools
        tools = fm.get("tools", [])
        for t in tools:
            if t not in ALLOWED_TOOLS:
                errors.append(f"Tool '{t}' in {sf} is not allowed")

        # Check examples
        if out_cls:
            examples_dir = sf.parent / "examples"
            if examples_dir.exists() and examples_dir.is_dir():
                for out_file in examples_dir.glob("*.output.json"):
                    try:
                        ex_data = json.loads(out_file.read_text(encoding="utf-8"))
                        out_cls.model_validate(ex_data)
                    except Exception as e:
                        errors.append(f"Example output {out_file} failed validation: {e}")

    if errors:
        raise SkillValidationError("; ".join(errors))
    return []


def generate_catalog_markdown(skills_dir: Path) -> str:
    registry = SkillRegistry()
    registry.scan(skills_dir)
    skills = sorted(registry.list_skills(), key=lambda s: s.name)

    lines = [
        "# Skills Catalog",
        "",
        "Auto-generated catalog of all verified skills in the service.",
        "",
        "| Skill Name | Version | Output Model | Tools | Description |",
        "|---|---|---|---|---|",
    ]
    for s in skills:
        tools_str = ", ".join(s.tools) if s.tools else "none"
        desc = s.description.replace("\n", " ").strip()
        lines.append(
            f"| `{s.name}` | `{s.skill_version}` | `{s.output_str}` | {tools_str} | {desc} |"
        )
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Skill registry validator and catalog builder")
    parser.add_argument("--check", action="store_true", help="Validate all skills in skills/")
    parser.add_argument("--write-catalog", action="store_true", help="Write skills/catalog.md")
    args = parser.parse_args()

    skills_path = Path("skills")
    if args.check:
        try:
            validate_skills_directory(skills_path)
            print("OK: All skills valid.")
            sys.exit(0)
        except SkillValidationError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(1)

    if args.write_catalog:
        md = generate_catalog_markdown(skills_path)
        out_file = skills_path / "catalog.md"
        out_file.write_text(md, encoding="utf-8")
        print(f"Catalog generated at {out_file}")
        sys.exit(0)
