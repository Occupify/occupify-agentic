import math
from pathlib import Path
from typing import Any

from sentence_transformers import CrossEncoder

from app.core.config import get_settings


class Reranker:
    def __init__(self, model_id: str | None = None) -> None:
        settings = get_settings()
        self.model_id = model_id or settings.RERANKER_MODEL

        model_path = self.model_id
        hf_dir = Path(settings.HF_MODELS_DIR)
        candidate = hf_dir / self.model_id
        if candidate.exists() and candidate.is_dir():
            model_path = str(candidate)

        self._model = CrossEncoder(model_path)

    def score(self, query: str, doc: str) -> float:
        logits: Any = self._model.predict([(query, doc)])
        logit = float(logits[0])
        # Sigmoid activation to map logit to [0, 1] probability
        return 1.0 / (1.0 + math.exp(-logit))

    def score_batch(self, pairs: list[tuple[str, str]]) -> list[float]:
        if not pairs:
            return []
        logits: Any = self._model.predict(pairs)
        return [1.0 / (1.0 + math.exp(-float(logit_val))) for logit_val in logits]
