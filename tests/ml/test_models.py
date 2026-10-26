import time

import numpy as np
import pytest
from app.ml.embedder import Embedder
from app.ml.reranker import Reranker

from app.core.config import get_settings


@pytest.mark.ml
def test_embedder_dim_matches_setting():
    settings = get_settings()
    embedder = Embedder()
    vecs = embedder.embed(["Test text"])
    assert len(vecs) == 1
    assert len(vecs[0]) == settings.EMBEDDING_DIM
    assert len(vecs[0]) == 1024


@pytest.mark.ml
def test_skill_similarity_threshold():
    embedder = Embedder()

    positives = [
        ("React", "React.JS"),
        ("ReactJS", "React"),
        ("Postgres", "PostgreSQL"),
        ("NodeJS", "Node.js"),
        ("TS", "TypeScript"),
    ]

    negatives = [
        ("Java", "JavaScript"),
        ("React", "React Native"),
        ("Figma", "Photoshop"),
    ]

    print("\n--- ML Skill Similarity Report ---")
    for s1, s2 in positives:
        v = embedder.embed([s1, s2])
        cosine = float(np.dot(v[0], v[1]))
        print(f"POSITIVE: {s1} <-> {s2}: {cosine:.4f}")
        assert cosine >= 0.80, f"Positive pair {s1} <-> {s2} fell below 0.80: {cosine:.4f}"

    for s1, s2 in negatives:
        v = embedder.embed([s1, s2])
        cosine = float(np.dot(v[0], v[1]))
        print(f"NEGATIVE: {s1} <-> {s2}: {cosine:.4f}")
        assert cosine < 0.80, f"Negative pair {s1} <-> {s2} exceeded 0.80: {cosine:.4f}"


@pytest.mark.ml
def test_reranker_40_pairs_latency_report():
    reranker = Reranker()
    pairs = [
        (
            "Java Spring Boot Developer with PostgreSQL experience",
            f"Project requirement document number {i} with Java details",
        )
        for i in range(40)
    ]

    latencies_ms: list[float] = []
    print("\n--- ML Reranker Latency Report ---")
    for query, doc in pairs:
        t0 = time.perf_counter()
        score = reranker.score(query, doc)
        t1 = time.perf_counter()
        assert 0.0 <= score <= 1.0
        latencies_ms.append((t1 - t0) * 1000.0)

    p50 = np.percentile(latencies_ms, 50)
    p95 = np.percentile(latencies_ms, 95)
    print(f"Reranker 40 pairs latency: p50={p50:.2f}ms, p95={p95:.2f}ms")
