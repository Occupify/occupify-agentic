# occupify-agentic

Lightweight Python AI service for the Occupify freelance platform.

## Architecture

- **Runtime:** Python 3.13 + FastAPI + Uvicorn
- **Agent Orchestration:** Pydantic AI with native Z.ai model (`ZaiModel`)
- **LLM Provider:** GLM models on z.ai (Pay-as-you-go API key), thinking turned off
- **Messaging & RPC:** FastStream with RabbitMQ (Direct Reply-To `amq.rabbitmq.reply-to`)
- **Document Processing:** Local Docling + Tesseract OCR (Vietnamese + English) with PDFium fallback
- **Privacy Gate:** personal data is removed before anything is sent to z.ai
- **Database:** PostgreSQL 16 + pgvector (tables auto-created at startup)

> ⚠️ **Use synthetic data only.** The privacy filter still misses names and addresses on some CV layouts (photo above the name, sidebar first). Don't send real CVs until it is fixed.

## Setup

### 1. Prerequisites

| Tool | Why | Check |
| :--- | :--- | :--- |
| [uv](https://github.com/astral-sh/uv) | installs Python 3.13 and the dependencies | `uv --version` |
| Podman + podman-compose (or Docker Compose) | runs PostgreSQL, RabbitMQ and the app container | `podman-compose version` |
| Tesseract OCR with `vie` and `eng` | OCR for scanned PDFs when running on the host (the container has it built in) | `tesseract --list-langs` |
| A z.ai API key (paid) | the AI model | — |

On Fedora: `sudo dnf install tesseract tesseract-langpack-vie tesseract-langpack-eng`.

To use Docker instead of Podman, add `COMPOSE="docker compose"` to every `make` command.

### 2. Shared infrastructure (once per machine)

RabbitMQ and the Docker network are shared by all Occupify services and live in `occupify-gitops`:

```bash
podman network create occupify-network        # skip if it already exists
cd ../occupify-gitops/compose
podman compose -f docker.infra.compose.yml up -d rabbitmq
```

### 3. Configuration

```bash
cp .env.example .env
```

Then edit `.env`:

- `ZAI_API_KEY`: your z.ai key. Never commit `.env`.
- `GLM_MODEL`: the model id (default `glm-4.5-air`). Use a **paid** model only, never the free `glm-4.7-flash` or `glm-4.5-flash`. Prices: <https://docs.z.ai/guides/overview/pricing>.
- `APP_ENV=local` turns on the local web page and the dev endpoints. Keep it `production` everywhere else.
- Leave `DATABASE_URL` and `RABBITMQ_URL` on the container hostnames. `make run` swaps them for `localhost` automatically.

### 4. Install dependencies

```bash
make install                       # uv sync (app + dev tools)
```

Without uv, the runtime packages are pinned in `requirements.txt`: `pip install -r requirements.txt` (Python 3.13). Regenerate it after changing dependencies:

```bash
uv export --frozen --no-dev --no-hashes --no-emit-project --format requirements-txt --output-file requirements.txt
```

### 5. Run on the host (recommended for development)

```bash
make infra                         # starts Postgres (5535) and CV compiler (localhost:8190)
make run                           # starts the app on http://localhost:8186 with auto-reload
```

Check it:

```bash
curl -s localhost:8186/ready       # {"status":"UP","checks":{"database":"UP","broker":"UP"}}
```

Open **<http://localhost:8186/ui>** for the local console: chat with streaming replies, plus a live log panel with the token usage of each AI call.

The first PDF can take ~10 s while Docling loads its models.

### 6. Or run everything in containers

```bash
make up                            # builds the image and (re)creates both containers
make logs                          # follow the app logs
make down                          # stop
```

The image is about 8 GB, so keep at least 15 GB of free disk space for a build.

### 7. Tests and lint

```bash
make test                          # unit tests; they ignore your .env
make test-all                      # with coverage
make lint                          # ruff format check + lint
make fmt                           # auto-fix formatting
```

## Local tools (`APP_ENV=local` or `test` only)

| URL | What |
| :--- | :--- |
| `GET /ui` | web console: sessions, streaming chat, PDF attachments, live logs |
| `GET /ai/dev/logs?limit=200&sessionId=` | recent log entries (newest last) |
| `GET /ai/dev/logs/stream?sessionId=` | live log entries (Server-Sent Events) |
| `POST /ai/dev/cv-preview` | upload a PDF and see the text that would be sent to z.ai |

In production these routes don't exist (404).

Every AI log entry (`llm.response`, `run.end`, `run.error`, `run.interrupted`) carries `model`, `tokens_in`, `tokens_out`, `tokens_cached`, `tokens_reasoning`, `tokens_total`, `requests` and `tokens_known`. Logs never contain message text, file text or model output.

## Endpoints

All `/ai/chat/*` calls need the `X-User-Id` header (set by the gateway in production).

- `GET /health` — Liveness probe
- `GET /ready` — Readiness probe (PostgreSQL + RabbitMQ)
- `POST /ai/chat/messages` — Send chat message (supports `stream=true` SSE and up to 3 PDF attachments)
- `GET /ai/chat/sessions` — List user chat sessions
- `GET /ai/chat/sessions/{sessionId}/messages` — Get session message history
- `DELETE /ai/chat/sessions/{sessionId}` — Delete chat session

## Troubleshooting

| Symptom | Fix |
| :--- | :--- |
| `make run`: `address already in use` on 8186 | the app container is running: `podman stop occupify-agentic` |
| `socket.gaierror` / name not resolved at startup | you ran `uvicorn` directly; use `make run`, which points the app at `localhost` |
| `/ready` shows `"broker": "DOWN"` | start the shared RabbitMQ (step 2) |
| `/ready` shows `"database": "DOWN"` | `make infra` |
| `make up` fails with `no space left on device` | remove old unused images (`podman image prune`) and retry |
| `/ui` returns 404 | `APP_ENV` is not `local`; or, in containers, the image is old: run `make up` again |
| Replies are slow to start | z.ai sometimes queues requests; try another paid model in `GLM_MODEL` |

## UC4 · CV Job Matching

UC4 performs candidate-job matching using a hybrid pipeline:
1. **CV Ingestion & Profiling:** Extracts text, redacts PII (`privacy.gate.clean`), structures candidate profile using the `extract-candidate-profile` skill.
2. **Hybrid Retrieval:** Query generation, dense vector search (`BAAI/bge-m3` via pgvector HNSW), BM25 full-text search (`tsvector` via GIN), fused with Reciprocal Rank Fusion (RRF `k=60`).
3. **Skill Verification & Re-ranking:** Verifies candidate vs required skills (`match-skills`), assesses job fit (`assess-job-fit`), applies cross-encoder reranker (`BAAI/bge-reranker-v2-m3`).
4. **Agentic Search:** If candidate has low or missing fit, `plan-job-search` expands search queries within budget caps.

### Settings (`.env`)
- `CORE_RPC_MODE`: `live` (RabbitMQ RPC to `occupify-core`) or `mock` (in-memory mock with catalog JSON).
- `CORE_MOCK_PATH`: path to mock projects catalog (e.g. `evals/uc4/data/catalog_scale_clean.json`).
- `ML_ENABLED`: `true` for local dense embeddings & reranking, `false` for unit testing fallback.
- `EMBEDDER_MODEL`: `BAAI/bge-m3` (1024-dim dense embeddings).
- `RERANKER_MODEL`: `BAAI/bge-reranker-v2-m3`.
- `JOB_MATCH_TOOL_TIMEOUT_S`: Maximum tool runtime (default 200s).
- `JOB_MATCH_LLM_CONCURRENCY`: Concurrency limit for model calls (default 4).

### Skill Library & Verification
- Skills reside in `skills/` with `SKILL.md` frontmatter.
- Check skill library validity: `make skills-check`
- Regenerate skill catalog: `make skills-catalog`

### Showcase Runbook
Follow these steps to run the complete end-to-end showcase:
1. Start the infra:
   ```bash
   make infra
   ```
2. Set `CORE_MOCK_PATH=evals/uc4/data/catalog_scale_clean.json` in `.env`. The app and the migration must use the **same** file; otherwise the source guard makes the index unusable.
3. Run the job index migration:
   ```bash
   make migrate-jobs
   ```
4. Start the service:
   ```bash
   make run
   ```
   Wait until `/ready` shows `models_loaded: true` and `index: ok`.
5. Open the web chat UI, or use the curl example in stream mode with a synthetic persona PDF from `evals/uc4/personas/`:
   ```bash
   curl -N -X POST http://localhost:8186/ai/chat/messages \
     -H "X-User-Id: test-user" \
     -F "message=Tìm cho mình công việc phù hợp với CV này" \
     -F "stream=true" \
     -F "files=@evals/uc4/personas/cv-a.pdf"
   ```

### Database & Image Notes
- `make reset-db`: Drops container volumes and recreates `postgres-agentic` with `vector` and `unaccent` extensions.
- Docker image: Uses CPU-only PyTorch and pre-downloads `bge-m3` and `bge-reranker-v2-m3` with `allow_patterns` (excluding ONNX and images) and `HF_HUB_OFFLINE=1`.

