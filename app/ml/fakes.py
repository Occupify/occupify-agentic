import hashlib
import math


class FakeEmbedder:
    def __init__(self, dim: int = 1024, model_id: str = "BAAI/bge-m3") -> None:
        self.dim = dim
        self.model_id = model_id

    def embed(self, texts: list[str]) -> list[list[float]]:
        results: list[list[float]] = []
        for text in texts:
            # Deterministic pseudo-embedding from text hash
            h = hashlib.sha256(text.encode("utf-8")).digest()
            vec = []
            for i in range(self.dim):
                byte_val = h[i % len(h)]
                val = ((byte_val + i * 17) % 256) / 128.0 - 1.0
                vec.append(val)
            norm = math.sqrt(sum(x * x for x in vec)) or 1.0
            norm_vec = [x / norm for x in vec]
            results.append(norm_vec)
        return results


class FakeReranker:
    def __init__(self, model_id: str = "BAAI/bge-reranker-v2-m3") -> None:
        self.model_id = model_id

    def score(self, query: str, doc: str) -> float:
        # Deterministic score based on simple overlap
        q_words = set(query.lower().split())
        d_words = set(doc.lower().split())
        if not q_words or not d_words:
            return 0.5
        overlap = len(q_words & d_words)
        jaccard = overlap / float(len(q_words | d_words))
        # Map to reasonable [0.2, 0.95] range
        return min(0.95, max(0.2, 0.3 + 0.65 * jaccard))
