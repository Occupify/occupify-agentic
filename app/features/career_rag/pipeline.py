from collections.abc import Iterator, Sequence
from datetime import UTC, datetime
from pathlib import Path

from sqlalchemy import and_, func, select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import CareerIngestionRun, CareerKnowledgeChunk
from app.features.career_rag.chunking import Chunk, chunk_record
from app.features.career_rag.connectors.esco import load_esco_occupations, load_esco_skills
from app.features.career_rag.connectors.onet import load_onet_occupations
from app.features.career_rag.connectors.roadmap import load_roadmap_directory
from app.features.career_rag.manifest import (
    compute_directory_manifest_hash,
    compute_files_manifest_hash,
)
from app.features.career_rag.schemas import CareerKnowledgeRecord
from app.ml.embedder import Embedder
from app.ml.fakes import FakeEmbedder


def utc_now() -> datetime:
    return datetime.now(UTC)


class IngestionPipeline:
    """Ingestion runner for career knowledge sources (roadmap.sh, ESCO, O*NET).

    Responsibilities:
    - Uses connectors to load records from datasets.
    - Runs semantic chunking.
    - Generates 1024-dim embeddings (with batching).
    - Persists chunks to CareerKnowledgeChunk in PostgreSQL with TSVector search text.
    - Records run in CareerIngestionRun and respects ManifestRegistry for idempotency.
    - Supports optional domain/sample filter for fast execution and testing.
    """

    def __init__(
        self,
        session: AsyncSession,
        embedder: Embedder | FakeEmbedder | None = None,
        batch_size: int = 64,
    ) -> None:
        self.session = session
        self._embedder = embedder
        self.batch_size = batch_size

    def _get_embedder(self) -> Embedder | FakeEmbedder:
        if self._embedder is None:
            self._embedder = Embedder()
        return self._embedder

    async def get_last_completed_run(
        self, source_id: str, source_version: str = "v1"
    ) -> CareerIngestionRun | None:
        """Retrieves last completed ingestion run for a given source."""
        stmt = (
            select(CareerIngestionRun)
            .where(
                and_(
                    CareerIngestionRun.source_id == source_id,
                    CareerIngestionRun.source_version == source_version,
                    CareerIngestionRun.status == "completed",
                )
            )
            .order_by(CareerIngestionRun.created_at.desc())
            .limit(1)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one_or_none()

    async def ingest_records(
        self,
        records: Sequence[CareerKnowledgeRecord] | Iterator[CareerKnowledgeRecord],
        source_id: str,
        source_version: str = "v1",
        manifest_hash: str = "manual",
        force: bool = False,
    ) -> CareerIngestionRun:
        """Ingests a sequence or iterator of records with idempotency checking and batch embedding."""
        last_run = await self.get_last_completed_run(source_id, source_version)
        if not force and last_run and last_run.manifest_hash == manifest_hash:
            # Manifest unchanged, already completed
            print(
                f"[IDEMPOTENCY] Manifest match for '{source_id}' (hash={manifest_hash[:16]}...). "
                f"Skipping duplicate ingestion. Run ID: {last_run.id}, existing chunks: {last_run.chunks_count}."
            )
            return last_run

        run = CareerIngestionRun(
            source_id=source_id,
            source_version=source_version,
            status="running",
            chunks_count=0,
            manifest_hash=manifest_hash,
            created_at=utc_now(),
        )
        self.session.add(run)
        await self.session.commit()
        await self.session.refresh(run)

        try:
            embedder = self._get_embedder()
            all_chunks: list[Chunk] = []

            for record in records:
                chunks = chunk_record(record)
                all_chunks.extend(chunks)

            total_chunks = len(all_chunks)
            print(
                f"[INGESTION] Source: {source_id} | Chunks generated: {total_chunks} | "
                f"Generating embeddings & persisting to database..."
            )
            if total_chunks > 0:
                # Process in batches for embeddings and DB persist
                for i in range(0, total_chunks, self.batch_size):
                    batch = all_chunks[i : i + self.batch_size]
                    texts_to_embed = [f"{c.title}\n{c.content}" for c in batch]
                    embeddings = embedder.embed(texts_to_embed)

                    is_pg = self.session.bind and "postgresql" in str(
                        getattr(self.session.bind.dialect, "name", "")
                    )

                    for chunk_obj, vec in zip(batch, embeddings):
                        doc_text = f"{chunk_obj.title} {chunk_obj.content}"
                        if is_pg:
                            insert_stmt = pg_insert(CareerKnowledgeChunk).values(
                                id=chunk_obj.chunk_id,
                                source_id=chunk_obj.source_id,
                                source_record_id=chunk_obj.source_record_id,
                                source_url=chunk_obj.source_url,
                                source_version=chunk_obj.source_version,
                                source_type=chunk_obj.source_type,
                                title=chunk_obj.title,
                                content=chunk_obj.content,
                                chunk_metadata=chunk_obj.chunk_metadata,
                                embedding=vec,
                                search_tsv=func.to_tsvector("simple", func.unaccent(doc_text)),
                            )
                            upsert_stmt = insert_stmt.on_conflict_do_update(
                                constraint="uq_career_chunk_source_record",
                                set_={
                                    "source_url": insert_stmt.excluded.source_url,
                                    "source_version": insert_stmt.excluded.source_version,
                                    "source_type": insert_stmt.excluded.source_type,
                                    "content": insert_stmt.excluded.content,
                                    "chunk_metadata": insert_stmt.excluded.chunk_metadata,
                                    "embedding": insert_stmt.excluded.embedding,
                                    "search_tsv": func.to_tsvector(
                                        "simple", func.unaccent(insert_stmt.excluded.content)
                                    ),
                                },
                            )
                            await self.session.execute(upsert_stmt)
                        else:
                            # Generic/fallback (e.g. SQLite tests)
                            existing_chunk = await self.session.get(
                                CareerKnowledgeChunk, chunk_obj.chunk_id
                            )
                            if existing_chunk:
                                existing_chunk.source_url = chunk_obj.source_url
                                existing_chunk.source_version = chunk_obj.source_version
                                existing_chunk.source_type = chunk_obj.source_type
                                existing_chunk.content = chunk_obj.content
                                existing_chunk.chunk_metadata = chunk_obj.chunk_metadata
                                existing_chunk.embedding = vec
                            else:
                                new_chunk = CareerKnowledgeChunk(
                                    id=chunk_obj.chunk_id,
                                    source_id=chunk_obj.source_id,
                                    source_record_id=chunk_obj.source_record_id,
                                    source_url=chunk_obj.source_url,
                                    source_version=chunk_obj.source_version,
                                    source_type=chunk_obj.source_type,
                                    title=chunk_obj.title,
                                    content=chunk_obj.content,
                                    chunk_metadata=chunk_obj.chunk_metadata,
                                    embedding=vec,
                                    search_tsv=None,
                                )
                                self.session.add(new_chunk)

                    await self.session.commit()

            run.status = "completed"
            run.chunks_count = total_chunks
            run.finished_at = utc_now()
            await self.session.commit()
            await self.session.refresh(run)
            print(
                f"[COMPLETED] Source: {source_id} | Chunks: {total_chunks} | Run ID: {run.id} | "
                f"Manifest: {manifest_hash[:16]}..."
            )
            return run

        except Exception as e:
            run.status = "failed"
            run.finished_at = utc_now()
            await self.session.commit()
            raise e

    async def ingest_source(
        self,
        source_id: str,
        base_dir: str | Path = "resource",
        domain_filter: str | None = None,
        sample_size: int | None = None,
        force: bool = False,
    ) -> CareerIngestionRun:
        """High-level runner to ingest a specific source with optional sample_size/domain filter."""
        res_path = Path(base_dir)

        if source_id == "roadmap.sh":
            roadmap_dir = res_path / "roadmap.sh"
            manifest_hash = compute_directory_manifest_hash(roadmap_dir, "*.md")
            records = list(
                load_roadmap_directory(roadmap_dir, domain_filter=domain_filter, limit=sample_size)
            )
            return await self.ingest_records(
                records=records,
                source_id="roadmap.sh",
                source_version="v1",
                manifest_hash=manifest_hash,
                force=force,
            )

        elif source_id == "esco":
            esco_dir = res_path / "esco"
            occ_file = esco_dir / "1_occupation_classification" / "occupations_en.csv"
            rel_file = esco_dir / "3_occupation_skill_mapping" / "occupationskillrelations_en.csv"
            skills_file = esco_dir / "2_skills_competencies" / "skills_en.csv"

            files_to_hash = [f for f in (occ_file, rel_file, skills_file) if f.exists()]
            manifest_hash = compute_files_manifest_hash(files_to_hash)

            records: list[CareerKnowledgeRecord] = []
            if occ_file.exists():
                records.extend(
                    list(
                        load_esco_occupations(
                            occ_file,
                            skill_relations_csv_path=rel_file if rel_file.exists() else None,
                            limit=sample_size,
                            domain_filter=domain_filter,
                        )
                    )
                )
            if skills_file.exists() and (sample_size is None or len(records) < sample_size):
                rem_limit = sample_size - len(records) if sample_size else None
                records.extend(
                    list(
                        load_esco_skills(
                            skills_file,
                            limit=rem_limit,
                            domain_filter=domain_filter,
                        )
                    )
                )

            return await self.ingest_records(
                records=records,
                source_id="esco",
                source_version="v1",
                manifest_hash=manifest_hash,
                force=force,
            )

        elif source_id == "onet":
            onet_dir = res_path / "onet"
            occ_file = onet_dir / "1_occupation_information" / "occupation_data.csv"
            skills_file = onet_dir / "2_skills_competencies" / "essential_skills.csv"
            abilities_file = onet_dir / "2_skills_competencies" / "abilities.csv"
            tasks_file = onet_dir / "3_occupational_requirements" / "task_statements.csv"

            files_to_hash = [
                f for f in (occ_file, skills_file, abilities_file, tasks_file) if f.exists()
            ]
            manifest_hash = compute_files_manifest_hash(files_to_hash)

            records: list[CareerKnowledgeRecord] = []
            if occ_file.exists():
                records.extend(
                    list(
                        load_onet_occupations(
                            occ_file,
                            essential_skills_csv_path=skills_file if skills_file.exists() else None,
                            abilities_csv_path=abilities_file if abilities_file.exists() else None,
                            task_statements_csv_path=tasks_file if tasks_file.exists() else None,
                            limit=sample_size,
                            domain_filter=domain_filter,
                        )
                    )
                )

            return await self.ingest_records(
                records=records,
                source_id="onet",
                source_version="v1",
                manifest_hash=manifest_hash,
                force=force,
            )

        else:
            raise ValueError(f"Unsupported source_id: {source_id}")


async def cli_main() -> None:
    import argparse

    from app.db.session import get_sessionmaker

    parser = argparse.ArgumentParser(description="Career Knowledge RAG Ingestion CLI")
    parser.add_argument(
        "--source",
        choices=["roadmap.sh", "esco", "onet", "all"],
        default="all",
        help="Source repository to ingest (default: all)",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=None,
        help="Sample size limit for testing / fast ingestion",
    )
    parser.add_argument(
        "--domain",
        type=str,
        default=None,
        help="Domain filter string (e.g., 'Software Engineering', 'AI')",
    )
    parser.add_argument(
        "--base-dir",
        type=str,
        default="resource",
        help="Base directory containing resource folders",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-ingestion even if manifest hash matches",
    )
    parser.add_argument(
        "--fake-embedder",
        action="store_true",
        help="Use deterministic FakeEmbedder instead of heavy neural model",
    )
    args = parser.parse_args()

    sessionmaker = get_sessionmaker()
    async with sessionmaker() as session:
        embedder = FakeEmbedder() if args.fake_embedder else None
        pipeline = IngestionPipeline(session=session, embedder=embedder)
        sources = ["roadmap.sh", "esco", "onet"] if args.source == "all" else [args.source]

        print("=" * 60)
        print("Occupify Career RAG Ingestion Pipeline CLI")
        print(f"Sources: {sources} | Sample Size: {args.sample_size} | Force: {args.force}")
        print("=" * 60)

        for src in sources:
            print(f"\n>>> Running ingestion for: {src}")
            run = await pipeline.ingest_source(
                source_id=src,
                base_dir=args.base_dir,
                domain_filter=args.domain,
                sample_size=args.sample_size,
                force=args.force,
            )
            print(
                f"[SUMMARY] Source: {run.source_id} | Status: {run.status} | "
                f"Chunks: {run.chunks_count} | Run ID: {run.id}"
            )


if __name__ == "__main__":
    import asyncio

    asyncio.run(cli_main())
