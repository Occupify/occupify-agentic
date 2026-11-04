import re
from typing import Any

from app.features.career_rag.chunking import Chunk, chunk_record
from app.features.career_rag.schemas import CareerKnowledgeRecord


def fixed_character_chunk(
    record: CareerKnowledgeRecord,
    chunk_size: int = 600,
    overlap: int = 100,
) -> list[Chunk]:
    """Naive baseline: fixed character window with fixed overlap."""
    text = record.content
    chunks: list[Chunk] = []
    start = 0
    idx = 1
    step = max(1, chunk_size - overlap)

    while start < len(text):
        end = min(len(text), start + chunk_size)
        slice_text = text[start:end]
        chunks.append(
            Chunk(
                chunk_id=f"fixed-{record.source_meta.source_record_id}-{idx}",
                source_id=record.source_meta.source_id,
                source_record_id=record.source_meta.source_record_id,
                source_type=record.source_meta.source_type,
                title=f"{record.title} (Part {idx})",
                content=slice_text,
                chunk_metadata={"strategy": "fixed_character", "slice": [start, end]},
            )
        )
        if end >= len(text):
            break
        start += step
        idx += 1

    return chunks


def naive_paragraph_chunk(record: CareerKnowledgeRecord) -> list[Chunk]:
    """Naive baseline: split by double newlines without parent context injection."""
    paragraphs = [p.strip() for p in record.content.split("\n\n") if p.strip()]
    chunks: list[Chunk] = []

    for idx, p in enumerate(paragraphs, start=1):
        chunks.append(
            Chunk(
                chunk_id=f"para-{record.source_meta.source_record_id}-{idx}",
                source_id=record.source_meta.source_id,
                source_record_id=record.source_meta.source_record_id,
                source_type=record.source_meta.source_type,
                title=f"Paragraph {idx}",
                content=p,
                chunk_metadata={"strategy": "naive_paragraph"},
            )
        )
    return chunks


def compute_chunking_metrics(
    chunks: list[Chunk],
    record_title: str,
) -> dict[str, float]:
    """Evaluates appropriateness of chunks against rule.md Rule 3:

    - Rule 3.25: Chunk by semantic unit, not arbitrary character count alone.
    - Rule 3.26: Keep each chunk understandable without requiring unrelated chunks (orphan test).
    - Rule 3.27: Preserve parent document context in chunk metadata and content.
    - Rule 3.28: Avoid boundary fragmentation (cutting through headers, lists, mid-sentence).
    """
    if not chunks:
        return {
            "total_chunks": 0,
            "avg_length": 0.0,
            "boundary_fragmentation_rate": 0.0,
            "orphan_chunk_rate": 1.0,
            "semantic_integrity_score": 0.0,
        }

    fragmented_count = 0
    orphan_count = 0
    lengths = []

    title_words = set(re.findall(r"\w+", record_title.lower()))

    for c in chunks:
        lengths.append(len(c.content))
        content = c.content.strip()

        # 1. Boundary fragmentation detection:
        # - Cuts off a markdown header (e.g. starts or ends with dangling #, ##, ### without title)
        # - Starts mid-sentence with lowercase or punctuation
        # - Ends mid-sentence without terminal punctuation or complete list item
        is_fragmented = False
        if re.search(r"#{1,4}\s*$", content):  # Trailing empty heading
            is_fragmented = True
        elif content and content[0] in ",;:)].?!":  # Starts with orphan punctuation
            is_fragmented = True
        elif content and content[0].islower() and not content.startswith("http"):
            is_fragmented = True
        elif not re.search(r"[.!?:\n]\s*$", content) and len(content) > 100:
            is_fragmented = True

        if is_fragmented:
            fragmented_count += 1

        # 2. Orphan check (understandability standalone):
        # A chunk is an orphan if neither its content nor title contains the parent role/skill context.
        combined = f"{c.title} {c.content}".lower()
        has_parent_context = any(w in combined for w in title_words if len(w) > 3)
        if not has_parent_context:
            orphan_count += 1

    total = len(chunks)
    frag_rate = fragmented_count / total
    orphan_rate = orphan_count / total
    # Semantic integrity: fraction of chunks that are self-contained and not fragmented
    integrity = max(0.0, 1.0 - (0.5 * frag_rate + 0.5 * orphan_rate))

    return {
        "total_chunks": float(total),
        "avg_length": float(sum(lengths) / total),
        "boundary_fragmentation_rate": round(frag_rate, 3),
        "orphan_chunk_rate": round(orphan_rate, 3),
        "semantic_integrity_score": round(integrity, 3),
    }


def compare_chunking_strategies(
    records: list[CareerKnowledgeRecord],
) -> dict[str, dict[str, Any]]:
    """Runs comparative evaluation of 3 chunking strategies across the provided records."""
    strategies = {
        "Fixed-Character (600 chars, 100 overlap)": fixed_character_chunk,
        "Naive Paragraph (Split on \\n\\n)": naive_paragraph_chunk,
        "Content-Aware Semantic (Occupify UC1)": chunk_record,
    }

    results: dict[str, dict[str, Any]] = {}

    for strat_name, chunk_fn in strategies.items():
        all_metrics: list[dict[str, float]] = []
        total_chunks_produced = 0

        for r in records:
            chunks = chunk_fn(r)
            total_chunks_produced += len(chunks)
            m = compute_chunking_metrics(chunks, record_title=r.title)
            all_metrics.append(m)

        if all_metrics:
            avg_frag = sum(m["boundary_fragmentation_rate"] for m in all_metrics) / len(all_metrics)
            avg_orphan = sum(m["orphan_chunk_rate"] for m in all_metrics) / len(all_metrics)
            avg_len = sum(m["avg_length"] for m in all_metrics) / len(all_metrics)
            avg_integrity = sum(m["semantic_integrity_score"] for m in all_metrics) / len(
                all_metrics
            )
        else:
            avg_frag = 0.0
            avg_orphan = 1.0
            avg_len = 0.0
            avg_integrity = 0.0

        results[strat_name] = {
            "total_chunks": total_chunks_produced,
            "avg_length": round(avg_len, 1),
            "boundary_fragmentation_rate": round(avg_frag, 3),
            "orphan_chunk_rate": round(avg_orphan, 3),
            "semantic_integrity_score": round(avg_integrity, 3),
            "adherence_verdict": (
                "PASS (Appropriate)" if avg_integrity >= 0.85 else "FAIL (Inappropriate)"
            ),
        }

    return results
