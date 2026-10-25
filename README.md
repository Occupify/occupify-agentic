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
make infra                         # starts occupify-postgres-agentic (port 5535)
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
