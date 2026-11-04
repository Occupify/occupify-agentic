import tempfile
from pathlib import Path

from app.features.career_rag.connectors.esco import (
    load_esco_occupations,
    load_esco_skills,
)
from app.features.career_rag.connectors.onet import (
    load_onet_occupations,
)
from app.features.career_rag.connectors.roadmap import (
    load_roadmap_directory,
    parse_roadmap_markdown,
)

SAMPLE_ROADMAP_MD = """# Backend Developer

## Metadata
- Type: Role
- Domain: Software Engineering
- Source: roadmap.sh
- Source URL: https://roadmap.sh/backend
- Related Roles:
  - DevOps Engineer
  - Full Stack Developer

---

## 1. Internet Fundamentals
- **How does the internet work?**
  - Learn IP, DNS, HTTP/HTTPS.

## 2. Basic Frontend Knowledge
- **HTML, CSS, JavaScript**
  - Basics to interact with frontend engineers.
"""

SAMPLE_ESCO_OCC_CSV = """conceptType,conceptUri,iscoGroup,preferredLabel,altLabels,hiddenLabels,status,modifiedDate,regulatedProfessionNote,scopeNote,definition,inScheme,description,code,naceCode
Occupation,http://data.europa.eu/esco/occupation/1234-abcd,2512,software developer,"programmer
software engineer",,released,2023-01-01,,,"Developers build software.",,Designs and implements software applications.,2512.1,
"""

SAMPLE_ESCO_SKILL_RELATIONS_CSV = """occupationUri,occupationLabel,relationType,skillType,skillUri,skillLabel
http://data.europa.eu/esco/occupation/1234-abcd,software developer,essential,knowledge,http://data.europa.eu/esco/skill/sql-uri,SQL
http://data.europa.eu/esco/occupation/1234-abcd,software developer,optional,skill/competence,http://data.europa.eu/esco/skill/docker-uri,Docker
"""

SAMPLE_ESCO_SKILL_CSV = """conceptType,conceptUri,skillType,reuseLevel,preferredLabel,altLabels,hiddenLabels,status,modifiedDate,scopeNote,definition,inScheme,description
KnowledgeSkillCompetence,http://data.europa.eu/esco/skill/sql-uri,knowledge,transversal,SQL,"Structured Query Language",,released,2023-01-01,,Query relational databases.,,Standard language for relational databases.
"""

SAMPLE_ONET_OCC_CSV = """O*NET-SOC Code,Title,Description
15-1252.00,Software Developers,"Research, design, and develop computer and network software or specialized utility programs."
"""

SAMPLE_ONET_SKILLS_CSV = """O*NET-SOC Code,Title,Element ID,Element Name,Scale ID,Scale Name,Data Value,N,Standard Error,Lower CI Bound,Upper CI Bound,Recommend Suppress,Not Relevant,Date,Domain Source
15-1252.00,Software Developers,2.A.1.c,Programming,IM,Importance,4.50,8,0.1,4.3,4.7,N,,08/2023,Analyst
"""

SAMPLE_ONET_ABILITIES_CSV = """O*NET-SOC Code,Title,Element ID,Element Name,Scale ID,Scale Name,Data Value,N,Standard Error,Lower CI Bound,Upper CI Bound,Recommend Suppress,Not Relevant,Date,Domain Source
15-1252.00,Software Developers,1.A.1.a.1,Deductive Reasoning,IM,Importance,4.25,8,0.1,4.0,4.5,N,,08/2023,Analyst
"""

SAMPLE_ONET_TASKS_CSV = """O*NET-SOC Code,Title,Task ID,Task,Task Type,Incumbents Responding,Date,Domain Source
15-1252.00,Software Developers,1001,"Develop and direct software system validation and testing methods.",Core,90,08/2023,Incumbent
"""


def test_parse_roadmap_markdown():
    with tempfile.NamedTemporaryFile("w+", suffix=".md", delete=False) as f:
        f.write(SAMPLE_ROADMAP_MD)
        f_path = f.name

    try:
        record = parse_roadmap_markdown(f_path)
        assert record.title == "Backend Developer"
        assert record.source_meta.source_id == "roadmap.sh"
        assert record.source_meta.domain == "Software Engineering"
        assert record.source_meta.source_url == "https://roadmap.sh/backend"
        assert "DevOps Engineer" in record.skills
        assert len(record.sections) >= 2
    finally:
        Path(f_path).unlink(missing_ok=True)


def test_load_roadmap_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        role_dir = Path(tmpdir) / "1_role_based_roadmaps" / "web"
        role_dir.mkdir(parents=True)
        (role_dir / "backend.md").write_text(SAMPLE_ROADMAP_MD)

        records = list(load_roadmap_directory(tmpdir))
        assert len(records) == 1
        assert records[0].title == "Backend Developer"
        assert records[0].source_meta.source_type == "learning_roadmap"


def test_load_esco_occupations_and_skills():
    with tempfile.TemporaryDirectory() as tmpdir:
        p = Path(tmpdir)
        occ_file = p / "occupations.csv"
        rel_file = p / "relations.csv"
        skill_file = p / "skills.csv"

        occ_file.write_text(SAMPLE_ESCO_OCC_CSV)
        rel_file.write_text(SAMPLE_ESCO_SKILL_RELATIONS_CSV)
        skill_file.write_text(SAMPLE_ESCO_SKILL_CSV)

        # Test occupations loader
        occ_records = list(load_esco_occupations(occ_file, rel_file))
        assert len(occ_records) == 1
        rec = occ_records[0]
        assert rec.title == "software developer"
        assert rec.source_meta.source_id == "esco"
        assert rec.source_meta.source_type == "occupation_taxonomy"
        assert "SQL" in rec.skills
        assert "Docker" in rec.skills
        assert rec.source_meta.geography == "EU"

        # Test skills loader
        skill_records = list(load_esco_skills(skill_file))
        assert len(skill_records) == 1
        srec = skill_records[0]
        assert srec.title == "SQL"
        assert srec.source_meta.source_type == "skill_competency"


def test_load_onet_occupations():
    with tempfile.TemporaryDirectory() as tmpdir:
        p = Path(tmpdir)
        occ_file = p / "occupation_data.csv"
        skills_file = p / "essential_skills.csv"
        abilities_file = p / "abilities.csv"
        tasks_file = p / "task_statements.csv"

        occ_file.write_text(SAMPLE_ONET_OCC_CSV)
        skills_file.write_text(SAMPLE_ONET_SKILLS_CSV)
        abilities_file.write_text(SAMPLE_ONET_ABILITIES_CSV)
        tasks_file.write_text(SAMPLE_ONET_TASKS_CSV)

        onet_records = list(
            load_onet_occupations(
                occ_file,
                essential_skills_csv_path=skills_file,
                abilities_csv_path=abilities_file,
                task_statements_csv_path=tasks_file,
            )
        )
        assert len(onet_records) == 1
        rec = onet_records[0]
        assert rec.title == "Software Developers"
        assert rec.source_meta.source_id == "onet"
        assert rec.source_meta.source_record_id == "15-1252.00"
        assert rec.source_meta.geography == "US"
        assert "Programming" in rec.skills
        assert "Deductive Reasoning" in rec.competencies
        assert "Develop and direct software system validation" in rec.content
