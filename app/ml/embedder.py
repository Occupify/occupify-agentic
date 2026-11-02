from pathlib import Path
from typing import Any

from sentence_transformers import SentenceTransformer

from app.core.config import get_settings


class Embedder:
    def __init__(self, model_id: str | None = None) -> None:
        settings = get_settings()
        self.model_id = model_id or settings.EMBEDDER_MODEL
        self.dim = settings.EMBEDDING_DIM

        # Resolve model path from local cache if present
        model_path = self.model_id
        hf_dir = Path(settings.HF_MODELS_DIR)
        candidate = hf_dir / self.model_id
        if candidate.exists() and candidate.is_dir():
            model_path = str(candidate)

        self._model = SentenceTransformer(model_path)

    def embed(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        embeddings: Any = self._model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        return embeddings.tolist()
