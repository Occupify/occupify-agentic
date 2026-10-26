FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=0
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project --no-dev
COPY . .
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked --no-dev
RUN .venv/bin/docling-tools models download --output-dir /opt/docling_models
RUN .venv/bin/python -c "\
from huggingface_hub import snapshot_download; \
snapshot_download('BAAI/bge-m3', local_dir='/opt/hf_models/BAAI/bge-m3', ignore_patterns=['*.onnx*', '*.bin', '*.pt', '*.safetensors.*', 'imgs/*'], allow_patterns=['*.safetensors', '*.json', '*.txt', '*.model', 'tokenizer*']); \
snapshot_download('BAAI/bge-reranker-v2-m3', local_dir='/opt/hf_models/BAAI/bge-reranker-v2-m3', ignore_patterns=['*.onnx*', '*.bin', '*.pt', '*.safetensors.*', 'imgs/*'], allow_patterns=['*.safetensors', '*.json', '*.txt', '*.model', 'tokenizer*'])"

FROM python:3.13-slim-bookworm AS runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr tesseract-ocr-vie tesseract-ocr-eng \
    && rm -rf /var/lib/apt/lists/*
RUN useradd --create-home --uid 10001 app
WORKDIR /app
COPY --from=builder --chown=app:app /app /app
COPY --from=builder --chown=app:app /opt/docling_models /opt/docling_models
COPY --from=builder --chown=app:app /opt/hf_models /opt/hf_models
ENV PATH="/app/.venv/bin:$PATH" \
    DOCLING_ARTIFACTS_PATH=/opt/docling_models \
    HF_MODELS_DIR=/opt/hf_models \
    HF_HUB_OFFLINE=1
USER app
EXPOSE 8186
HEALTHCHECK --start-period=180s CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8186/health')" || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8186"]

