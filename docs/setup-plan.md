# occupify-agentic — MVP setup plan

> **Status:** **v6 — complete, ready for approval** · **Date:** 2026-10-24 · **Author:** Claude (lead)
> **Scope:** set up the repo, the shared building blocks every agent will use, and a **chat endpoint** (sessions + PDF attachments).
> The five use cases are not built in this step; anything not needed now is in §11 "Later".

---

## 0. Decisions

| # | Decision |
|---|---|
| D-1 | Lightweight Python service, one repo `occupify-agentic`, Python 3.13 |
| D-2 | LLM = GLM on **z.ai** (pay-as-you-go key), base URL `https://api.z.ai/api/paas/v4` |
| D-3 | **Model chosen in `.env`**: one default model + an optional override per use case (chat included), changed by hand without code changes |
| D-4 | Agent runtime = **Pydantic AI** with its native z.ai model (`ZaiModel`) |
| D-5 | Agent tools = request/reply calls to other services **over RabbitMQ**, through **FastStream** |
| D-6 | PDFs are turned into text **locally** with **Docling** (+ Tesseract OCR, Vietnamese + English) |
| D-7 | **Personal data never goes to z.ai** (or any third party) — not from files, not from typed text. A local **privacy gate** cleans everything first; if it can't confirm the text is clean, the request fails with a "Failed to …" message and nothing is sent |
| D-8 | Matching uses **skills and experience only** — education/school is removed before the LLM |
| D-9 | Database = PostgreSQL 16 (pgvector image). **No migration tool**: tables are created at startup if missing |
| D-10 | **Chat** = one send endpoint. No `sessionId` → a new session is created (stored with `user_id`) and its id is returned; with `sessionId` → the conversation continues. The **full history is sent every turn** (no trimming); when it goes off the rails, the user starts a new session. Replies can be **streamed** (confirmed on z.ai, §6.9) |
| D-11 | Code organized **by feature** (one folder per use case, chat is the first) + shared folders |
| D-12 | Local containers join the shared `occupify-network` and use the shared `occupify-rabbitmq` |
| D-13 | CI = lint + tests + image build check; no CD |

---

## 1. MVP setup scope

**Built in this step**
1. Repo bootstrap: `git init`, `.gitignore`, `.dockerignore`, `.env.example`, `pyproject.toml` + `uv.lock`, `Makefile`, `README.md`.
2. App skeleton: FastAPI app, config, **log helper**, error/response envelopes, current user from gateway headers, `/health`, `/ready`.
3. GLM access: model factory reading the models from `.env`; agent runner that logs every step and saves the run.
4. Tools plumbing: RabbitMQ broker + request/reply client (tested against a stub, because the Java listeners don't exist yet).
5. Documents: PDF upload → Docling text → **privacy gate**.
6. Database: tables created at startup (`agent_runs`, `documents`, `chat_sessions`, `chat_messages`).
7. **Chat endpoints** (§6.9).
8. One local-only endpoint to check the privacy gate by eye (§6.8).
9. `Dockerfile`, `docker-compose.yaml`, `.github/workflows/ci.yml`.

**Not in this step:** the five use cases, embeddings, event consumers, notifications, background job queue (see §11).

---

## 2. What the design relies on (from the existing services)

| Fact | Where | Used for |
|---|---|---|
| Profile: headline, bio, experience, skills (proficiency, years) | `occupify-identity` | future tool `identity.profile.get` |
| Projects → jobs (skills, budget) → bids (rate, message, `attachmentCvUrl`) | `occupify-core` | future tools `core.*` |
| CV files in S3-compatible storage, public URLs | identity storage | downloader with host allow-list (later, UC3) |
| RabbitMQ JSON via `Jackson2JsonMessageConverter`, type precedence `INFERRED` | core, identity, noti | Python sends `content_type=application/json`, no type header needed |
| Gateway forwards `X-User-Id`, `X-User-Role`, `X-User-Email` | gateway | same auth model; chat sessions belong to `X-User-Id` |
| Envelopes `{statusCode, message, data}`, `{statusCode, message, errorCode}`, `{statusCode, message, data, paging{page, limit, total, totalPages}}` | core `dto/base` | same response shapes |
| Ports 8181–8185 / Postgres 5530–5534; `podman compose` | gitops, Makefiles | agentic **8186**, Postgres **5535** |

---

## 3. Architecture (MVP)

```
 web ─▶ nginx ─▶ gateway ──/ai/**──▶ occupify-agentic :8186
                                      ├─ chat router ── sessions, messages, PDF attachments
                                      ├─ documents: PDF → text (Docling + Tesseract, local)
                                      ├─ privacy gate ── only clean text passes ──┐
                                      ├─ agents/runner ───────────────────────────┴──▶ api.z.ai (GLM)
                                      ├─ tools ── FastStream request/reply ──▶ occupify-rabbitmq ──▶ core / identity
                                      └─ db ── occupify-postgres-agentic :5535
```

---

## 4. Libraries

| Package | Purpose |
|---|---|
| `fastapi`, `uvicorn[standard]` | HTTP API (incl. streaming replies) |
| `python-multipart` | multipart form uploads (chat message + PDF files) |
| `pydantic`, `pydantic-settings` | models; config from env / `.env` |
| `pydantic-ai-slim[zai]` | agent loop, tools, message history, streaming, native z.ai model; `TestModel` / `FunctionModel` for LLM-free tests |
| `faststream[rabbit]` | RabbitMQ request/reply (direct reply-to, correlation id, timeout); `TestRabbitBroker` for in-memory tests |
| `sqlalchemy[asyncio]`, `asyncpg` | DB access; `create_all` at startup |
| `httpx` | downloads (later: bid CV URLs); also used by tests |
| `docling` | PDF → text with layout models (two-column CVs, tables), OCR only on pages without text |
| `pypdfium2` | page count, encryption check, fast fallback extractor |
| Tesseract (`tesseract-ocr`, `-vie`, `-eng`) — system package | OCR engine Docling uses for scanned pages |

Dev: `pytest`, `pytest-asyncio`, `pytest-cov`, `respx`, `ruff`, `reportlab` (generates synthetic CV PDFs for tests).

Logging uses the standard library only (§6.3).

**Not used, and why:**
- **z.ai OCR / vision for CVs:** z.ai would see the raw CV before anything is removed (D-7).
- **PyMuPDF4LLM:** AGPL, which is a problem in a closed web service.
- **Marker, MinerU:** model licences restrict commercial use.
- **LangChain / LangGraph:** heavier than we need.
- **Alembic:** not wanted (D-9).

```toml
[project]
name = "occupify-agentic"
requires-python = ">=3.13,<3.14"
dependencies = [
  "fastapi", "uvicorn[standard]", "python-multipart",
  "pydantic", "pydantic-settings",
  "pydantic-ai-slim[zai]",
  "faststream[rabbit]",
  "sqlalchemy[asyncio]", "asyncpg",
  "httpx",
  "docling", "pypdfium2",
]

[dependency-groups]
dev = ["pytest", "pytest-asyncio", "pytest-cov", "respx", "ruff", "reportlab"]

[tool.uv.sources]                        # Docling pulls PyTorch: CPU-only wheels
torch = { index = "pytorch-cpu" }
torchvision = { index = "pytorch-cpu" }

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[tool.ruff]
line-length = 100
target-version = "py313"

[tool.pytest.ini_options]
asyncio_mode = "auto"
markers = ["integration: needs Postgres + RabbitMQ", "docling: loads Docling models"]
```

Versions are pinned by `uv.lock` at init.

---

## 5. Folder structure

```
occupify-agentic/
├── app/
│   ├── main.py                    # FastAPI app; lifespan: create tables, open DB + broker
│   ├── core/
│   │   ├── config.py              # Settings (incl. model per use case, chat limits)
│   │   ├── logging.py             # JSON logs, bind_context(), log_step()
│   │   ├── errors.py              # AppError → {statusCode, message, errorCode}
│   │   ├── responses.py           # single / page envelopes (mirror core)
│   │   └── security.py            # CurrentUser from X-User-* headers
│   ├── llm/
│   │   └── glm.py                 # model_for(use_case) → ZaiModel
│   ├── agents/
│   │   ├── runner.py              # run_agent() / stream_agent(): logging, limits, gate, saves the run
│   │   └── deps.py                # what tools receive: current user, rpc, db
│   ├── privacy/
│   │   ├── detectors.py           # email, phone, ID numbers, URLs, labelled lines (EN + VI)
│   │   ├── sections.py            # sections and contact header removed whole (EN + VI headings)
│   │   └── gate.py                # clean(text, source) → cleaned text, or fails — same rule for files and typed text
│   ├── documents/
│   │   ├── fetch.py               # upload checks (+ URL download with host allow-list, later)
│   │   └── extract.py             # DoclingExtractor, PdfiumExtractor
│   ├── messaging/
│   │   ├── broker.py              # FastStream RabbitBroker, tied to FastAPI lifespan
│   │   ├── topology.py            # exchange / queue / routing-key names in one place
│   │   └── rpc.py                 # call(tool, args) → reply envelope; timeout + errors
│   ├── tools/                     # one file per service; filled as use cases arrive
│   ├── db/
│   │   ├── session.py             # async engine + session
│   │   ├── init.py                # create_all() at startup
│   │   ├── models.py              # agent_runs, documents, chat_sessions, chat_messages
│   │   └── repositories/          # runs.py, documents.py, chat.py
│   ├── api/
│   │   ├── health.py              # /health, /ready
│   │   └── dev.py                 # local-only: /ai/dev/cv-preview
│   └── features/
│       ├── chat/                  # router.py · service.py · agent.py · prompts.py · schemas.py
│       └── README.md              # later: roadmap/ cv_match/ applicant_ranking/ job_recommendation/ project_draft/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── fixtures/                  # synthetic CVs (EN + VI) with fake personal data
│   └── conftest.py                # blocks real model calls
├── docs/
├── pyproject.toml · uv.lock · Makefile · README.md
├── .env.example · .gitignore · .dockerignore
├── Dockerfile · docker-compose.yaml
└── .github/workflows/ci.yml
```

Each feature folder has `router.py` (HTTP), `service.py` (orchestration), `agent.py` (Pydantic AI agent), `prompts.py`, `schemas.py`. Feature folders import shared folders, never the other way round.

---

## 6. Building blocks

### 6.1 `.env.example`

```dotenv
APP_ENV=local                          # local enables /ai/dev/* endpoints
APP_PORT=8186
LOG_LEVEL=INFO
LOG_PAYLOADS=false                     # true = also log prompts/outputs (already cleaned); local only

# --- GLM (z.ai) ---
ZAI_API_KEY=                           # rename your current glm_api_key to this
ZAI_BASE_URL=https://api.z.ai/api/paas/v4
# Model IDs on z.ai: glm-5.3, glm-5, glm-4.7, glm-4.7-flashx, glm-4.7-flash, glm-4.5-air, glm-4.5-flash
# (current list: https://docs.z.ai/guides/overview/pricing)
GLM_MODEL_DEFAULT=glm-4.7
GLM_THINKING=false                     # true = reasoning mode (slower, more tokens)
# Per-use-case model — leave empty to use GLM_MODEL_DEFAULT
GLM_MODEL_CHAT=
GLM_MODEL_ROADMAP=
GLM_MODEL_CV_MATCH=
GLM_MODEL_APPLICANT_RANKING=
GLM_MODEL_JOB_RECOMMENDATION=
GLM_MODEL_PROJECT_DRAFT=
GLM_TIMEOUT_S=120
GLM_MAX_REQUESTS_PER_RUN=10            # stops an agent stuck in a tool loop

# --- Chat ---
CHAT_MAX_MESSAGE_CHARS=20000           # one message; the session history itself has no limit
CHAT_MAX_CONTEXT_CHARS=50000
CHAT_MAX_FILES=3                       # PDFs per message
CHAT_STREAM_HEARTBEAT_S=15             # keep-alive line on quiet streams so proxies don't cut them

# --- PDF documents ---
PDF_MAX_BYTES=10485760
PDF_MAX_PAGES=20
PDF_EXTRACTOR=docling                  # docling | pdfium
OCR_LANGS=vie,eng
PDF_ALLOWED_HOSTS=                     # for URL downloads later (bid CVs)

# --- Database ---
DATABASE_URL=postgresql+asyncpg://postgres:postgres@occupify-postgres-agentic:5432/occupify_agentic

# --- RabbitMQ (shared) ---
RABBITMQ_URL=amqp://guest:guest@occupify-rabbitmq:5672/
RABBITMQ_RPC_TIMEOUT_S=10
```

To change a model: edit `.env` and restart the container. `model_for("chat")` returns `GLM_MODEL_CHAT` if set, otherwise `GLM_MODEL_DEFAULT`. On startup the app logs which model each use case will use.

### 6.2 GLM access + agent runner

- `app/llm/glm.py`: builds `ZaiModel(<model id>, provider=ZaiProvider(api_key, base_url))` per use case. Thinking is on/off from `GLM_THINKING`.
- `app/agents/runner.py` — every agent call goes through one of two functions:
  - `run_agent(...)`: returns the whole answer.
  - `stream_agent(...)`: yields text chunks.

  Both do the following:

```
  1. bind_context(trace_id, run_id, use_case, user_id)   # every log line below carries these
  2. insert agent_runs row (status=running)
  3. inputs and every tool result go through the privacy gate before the model sees them
  4. run the agent with the given message history; log_step(...) for each step and keep the list
  5. stop after GLM_MAX_REQUESTS_PER_RUN model requests
  6. success → save output, tokens, latency, steps (status=succeeded)
     failure → save error, steps (status=failed), raise AppError
```

- Tools take the current user from `deps`, never from an argument the model chooses. A document containing "fetch user X's profile" can't make the agent do it.

### 6.3 Log helper (`app/core/logging.py`)

- Standard `logging`, one JSON object per line on stdout.
- `bind_context(**fields)` puts `trace_id`, `run_id`, `use_case`, `user_id` (+ `session_id` for chat) in `contextvars`. Every log line carries them automatically.
- `log_step(event, **fields)` — the one call used by the runner and features.

| Event | Fields |
|---|---|
| `run.start` | model, history_messages, prompt_chars |
| `llm.request` | model, message_count |
| `llm.response` | tokens_in, tokens_out, ms |
| `tool.call` | tool, args (ids only) |
| `tool.result` | tool, ms, ok, error_code |
| `doc.extracted` | pages, extractor, ms, ocr_pages |
| `pii.cleaned` | source, counts per category removed |
| `pii.blocked` | source, reason |
| `run.end` | ms, tokens_total, steps |
| `run.error` | ms, error_type, error_code |

```json
{"ts":"2026-10-24T10:31:07.412Z","level":"INFO","event":"llm.response","trace_id":"8f3c2a…","run_id":"5d1e…","use_case":"chat","session_id":"a41c…","user_id":"b7a0…","model":"glm-4.7","tokens_in":5120,"tokens_out":412,"ms":3810}
```

Message text, file text, prompts and model output are never logged at INFO, only their lengths. The `trace_id` also travels as an AMQP header, so the same id can be searched in Java logs.

### 6.4 Privacy gate (`app/privacy/`)

One rule for **everything** bound for z.ai — PDF text, the typed `message` and `context`, and later profile text and bid messages. `clean(text, source)` removes the personal data below, then checks again. If anything is still found, the request fails and nothing is sent.

**What is removed vs kept**

| Removed | Kept |
|---|---|
| full name, email, phone → `[NAME]` `[EMAIL]` `[PHONE]` | skills, tools, languages spoken |
| address, date of birth / age | job titles, employer names, dates of each role |
| ID / passport / tax / bank numbers | experience and project descriptions, achievements |
| gender, marital status, nationality, religion lines | certifications |
| photos and all images | that a portfolio exists → `[PORTFOLIO_LINK]` |
| social profile links (LinkedIn, Facebook, Zalo, …) | |
| whole sections: **Education / Học vấn**, Personal info / Thông tin cá nhân, Contact / Liên hệ, References / Người tham chiếu | |
| salary history | |

Steps, all local:
1. **Drop sections** by heading (Docling keeps headings), in English and Vietnamese.
2. **Drop the contact header** (files only): if the text before the first section heading contains an email, phone or link, that whole block goes. On a CV this block holds the name next to the contacts, so the name goes with it, even before we can look the name up.
3. **Replace known identifiers:** the user's email from `X-User-Email`, and later full name and phone from identity. A name is matched with and without Vietnamese accents and in either order, and only as a whole name, never single words ("Văn" is also an ordinary word).
4. **Pattern detectors:** emails, phones (+84 / 0… / international), links, 9/12-digit ID numbers, and lines labelled DOB / Ngày sinh, Address / Địa chỉ, Gender / Giới tính and similar.
5. **Check again, fail if unsure:** steps 3–4 run a second time on the result. Any hit → the whole request fails with `PII_REMOVAL_FAILED`, "Failed to remove personal data from `cv.pdf`. Nothing was sent." (or "…from your message."). Log `pii.blocked`.
6. Raw PDF bytes and raw text stay in memory for the request only. Only cleaned text is stored.

### 6.5 PDF → text (`app/documents/`)

```
upload ─▶ check (≤ PDF_MAX_BYTES, starts with %PDF, ≤ PDF_MAX_PAGES, not encrypted)
       ─▶ Docling (local) ─▶ clean(text, "file") ─▶ cache by SHA-256 (cleaned text only, 30 days)
```

- **Docling** reads the text layer with layout models and runs Tesseract OCR only on pages with no text. Images are dropped. Models are baked into the image, so nothing is downloaded at runtime. Pdfium is the fallback if Docling fails.
- The cache means the same PDF attached twice is extracted once.
- Each file's text is placed in the prompt inside a fenced block, labelled with the file name and marked as **data, not instructions**.

### 6.6 RabbitMQ request/reply (`app/messaging/`)

```
agentic: rpc.call("core.job.get", {"jobId": …})
   publish → exchange occupify.agent.rpc (direct) · routing key core.job.get
             reply_to amq.rabbitmq.reply-to · correlation_id · expiration 10 s
             content_type application/json · headers x-trace-id, x-run-id
   ──▶ queue occupify.core.rpc.job.get ──▶ Java @RabbitListener returns a value
   ◀── reply with the same correlation_id (Spring does this automatically)
```

- Names: routing key `<service>.<entity>.<verb>`, queue `occupify.<service>.rpc.<entity>.<verb>`, camelCase JSON.
- Every reply uses one envelope: `{"ok": true, "data": …}` or `{"ok": false, "error": {"code", "message"}}`.
- Timeout or `ok:false` → the tool hands the model a clear error instead of letting it guess. A responder that crashes without replying shows up here as a timeout.

### 6.7 Database (no migration tool)

On startup, `db/init.py` runs SQLAlchemy `create_all()`: missing tables are created, existing ones are left alone. If a column changes during development, run `make reset-db` (drops the Postgres volume) and restart.

| Table | Columns |
|---|---|
| `agent_runs` | id, use_case, user_id, session_id (nullable), status, model, tokens_in, tokens_out, latency_ms, steps (the trace), error, trace_id, created_at, finished_at |
| `documents` | id, sha256 (unique), extractor, page_count, cleaned_text, removed_counts, created_at, expires_at |
| `chat_sessions` | **id** (UUID generated by the server = the `sessionId` returned to the user), **user_id**, title, message_count, busy_since (nullable), created_at, updated_at · index (user_id, updated_at) |
| `chat_messages` | id, **session_id** (cascade delete), **user_id**, seq, role (`user` / `assistant`), status (`complete` / `interrupted`), display_text, attachments (file name, pages, removed counts), **model_messages** (exactly what was sent to / received from z.ai, already cleaned — replayed as history), client_message_id, run_id, tokens_in, tokens_out, created_at · unique (session_id, seq), unique (session_id, client_message_id) |

`display_text` keeps what the user typed, so the chat UI shows their own words. Only `model_messages` holds what went to z.ai. On startup, runs left in `running` by a crashed container are marked `failed`, and stale `busy_since` flags are cleared.

### 6.8 HTTP endpoints in the setup

| Endpoint | Purpose |
|---|---|
| `GET /health` | process is alive |
| `GET /ready` | DB and RabbitMQ reachable |
| `/ai/chat/...` | chat (§6.9) |
| `POST /ai/dev/cv-preview` (upload a PDF) — **local only** | returns the cleaned text and what was removed, so you can check the gate by eye. Nothing goes to z.ai |

`/ai/dev/*` exists only when `APP_ENV=local`.

### 6.9 Chat

**Endpoints** (the user always comes from `X-User-Id`):

| Method + path | Purpose |
|---|---|
| `POST /ai/chat/messages` | send a message. **No `sessionId` → a new session**; the reply carries the new `sessionId` |
| `GET /ai/chat/sessions?page=&limit=` | list my sessions, newest first (core's page envelope) |
| `GET /ai/chat/sessions/{sessionId}/messages?page=&limit=` | history for the UI |
| `DELETE /ai/chat/sessions/{sessionId}` | delete a session and its messages. Otherwise sessions are **kept until deleted** |

**Sessions.**
- Every session is stored with the `user_id` (from `X-User-Id`) and a `session_id` (UUID) generated by the server. The client never makes up an id; it sends back the one we returned.
- A `sessionId` that doesn't exist, or belongs to another user → `404 CHAT_SESSION_NOT_FOUND`. A new session is **not** created in that case, so a wrong id can't silently split a conversation.
- Every message row also stores `user_id` and `session_id`.

**Fields of `POST /ai/chat/messages`** (`multipart/form-data`):

| Field | Type | Required | Why |
|---|---|---|---|
| `sessionId` | UUID | no | empty = start a new session |
| `message` | text ≤ `CHAT_MAX_MESSAGE_CHARS` | yes | what the user asks |
| `context` | text ≤ `CHAT_MAX_CONTEXT_CHARS` | no | background to keep in mind, e.g. goals, a pasted job description, "I'm a backend dev moving to freelance". Sent once, it stays in the session because the full history is replayed |
| `files` | PDF, repeatable, ≤ `CHAT_MAX_FILES` | no | CVs, project briefs, portfolios. Extracted locally and cleaned (§6.4–6.5) |
| `clientMessageId` | UUID | no | sent by the web app. If the same id arrives twice (network retry), the saved reply is returned instead of a duplicate turn |
| `stream` (query) | `true` \| `false` (default `false`) | no | `true` = reply streamed as Server-Sent Events |

Fields to add when the tools exist (§11): `jobId`, `projectId` (the agent loads the job or project itself), `includeProfile` (the agent loads the user's own cleaned profile). The reply language will be configured later.

**Reply** (`stream=false`):

```json
{
  "statusCode": 200,
  "message": "OK",
  "data": {
    "sessionId": "a41c…",
    "newSession": true,
    "messageId": "9e07…",
    "reply": "…markdown…",
    "attachments": [
      { "fileName": "cv.pdf", "pages": 2, "removed": { "name": 1, "email": 1, "phone": 1, "education": 1 } }
    ],
    "model": "glm-4.7",
    "usage": { "tokensIn": 5120, "tokensOut": 412 }
  }
}
```

**Streaming (`stream=true`) — checked against the docs, 2026-10-24**

| Layer | Support |
|---|---|
| **z.ai chat API** | yes. `stream: true` returns Server-Sent Events: text in `choices[0].delta.content`, reasoning in `delta.reasoning_content`, `finish_reason` and `usage` in the last chunk, then `data: [DONE]`. `tool_stream: true` also streams tool calls on GLM-5.x, GLM-4.7, GLM-4.6 |
| **Pydantic AI `ZaiModel`** | yes. Inherits Pydantic AI's OpenAI-compatible streaming and maps z.ai's own finish reasons (`model_context_window_exceeded`, `sensitive`, `network_error`) |
| **our service** | `agent.run_stream()` in the runner, re-sent to the browser as the events below |

Our events to the browser, in order:
1. `meta` — `{sessionId, newSession, messageId, attachments}`. Sent first, so the UI has the session id even if the stream breaks
2. `delta` — `{text}`, repeated
3. `done` — `{model, usage}`

`error` — `{errorCode, message}` ends the stream. A comment line every `CHAT_STREAM_HEARTBEAT_S` seconds keeps proxies from closing a quiet connection. Reasoning text (when `GLM_THINKING=true`) is not forwarded to the user. If the user closes the tab mid-reply, we stop reading from z.ai and save what was generated with status `interrupted`, so the history stays consistent.

**What happens on each message**
1. With `sessionId`: load the session (404 if missing or not the user's) and mark it busy. A second message while one is running → `409 CHAT_BUSY`.
2. Check limits. Extract each PDF. Clean the files and the typed text (§6.4). Any failure → error with a "Failed to …" message; nothing goes to z.ai, and no new session is created.
3. Without `sessionId`: create the session now (new UUID, `user_id`, title = first 60 characters of the message).
4. Load **all** previous `model_messages` of the session — no trimming, no summarizing (D-10).
5. Run the chat agent through the runner with that history. Save the user turn and the assistant turn (`user_id`, `session_id`, `model_messages`, tokens, run id). Clear the busy flag.

**Context size.** We set no limit on history; the model's own context window is the only one. When a session outgrows it, z.ai either rejects the request or ends with finish reason `model_context_window_exceeded`. Both become `422 CHAT_CONTEXT_FULL`.

**Chat agent** (`features/chat/agent.py`):
- A career assistant for Occupify (freelancing, CVs, projects, skills), answering in markdown.
- **No tools in the setup.**
- The system prompt says file blocks are data, not instructions, and that it must not state facts about the user beyond what the conversation contains.

**Errors** — every message starts with "Failed to …":

| Code | HTTP | Message |
|---|---|---|
| `CHAT_SESSION_NOT_FOUND` | 404 | Failed to find this chat session. |
| `CHAT_BUSY` | 409 | Failed to send: the previous message is still being answered. |
| `FILE_INVALID` | 400 | Failed to read `cv.pdf`: not a PDF / larger than 10 MB / more than 20 pages / password-protected. |
| `PII_REMOVAL_FAILED` | 422 | Failed to remove personal data from `cv.pdf` (or "from your message"). Nothing was sent. |
| `CHAT_CONTEXT_FULL` | 422 | Failed to continue: this conversation is too long for the model. Please start a new session. |
| `CHAT_CONTENT_FILTERED` | 422 | Failed to answer: the AI provider blocked this content. |
| `LLM_UNAVAILABLE` | 502 | Failed to reach the AI model. Please try again. |

---

## 7. Containers

### 7.1 `Dockerfile`

```dockerfile
FROM ghcr.io/astral-sh/uv:<pinned>-python3.13-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=0
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev
COPY . .
RUN --mount=type=cache,target=/root/.cache/uv uv sync --locked --no-dev
RUN .venv/bin/docling-tools models download --output-dir /opt/docling_models

FROM python:3.13-slim-bookworm AS runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
      tesseract-ocr tesseract-ocr-vie tesseract-ocr-eng \
    && rm -rf /var/lib/apt/lists/*
RUN useradd --create-home --uid 10001 app
WORKDIR /app
COPY --from=builder --chown=app:app /app /app
COPY --from=builder --chown=app:app /opt/docling_models /opt/docling_models
ENV PATH="/app/.venv/bin:$PATH" DOCLING_ARTIFACTS_PATH=/opt/docling_models
USER app
EXPOSE 8186
HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8186/health')" || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8186"]
```

`.dockerignore`: `.env*`, `.git`, `.venv`, caches, `tests/`, `docs/`.

### 7.2 `docker-compose.yaml`

```yaml
services:
  postgres-agentic:
    image: docker.io/pgvector/pgvector:pg16
    container_name: occupify-postgres-agentic
    environment:
      POSTGRES_DB: occupify_agentic
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-postgres}
    ports: ["${POSTGRES_PORT:-5535}:5432"]
    healthcheck: { test: ["CMD-SHELL", "pg_isready -U postgres"], interval: 5s, retries: 10 }
    volumes: [postgres_agentic_data:/var/lib/postgresql/data]
    networks: [occupify-network]

  agentic:
    build: .
    image: occupify-agentic:local
    container_name: occupify-agentic
    env_file: .env
    ports: ["${APP_PORT:-8186}:8186"]
    depends_on: { postgres-agentic: { condition: service_healthy } }
    restart: unless-stopped
    networks: [occupify-network]

volumes:
  postgres_agentic_data:

networks:
  occupify-network:
    external: true
```

No RabbitMQ service here: we use the shared `occupify-rabbitmq`.

**Before the first run:**
1. `podman network create occupify-network` (once).
2. Make sure `occupify-rabbitmq` is on that network. The gitops infra compose does this. If RabbitMQ was started from noti's or core's own compose file, run `podman network connect occupify-network occupify-rabbitmq`.

### 7.3 `Makefile`

`COMPOSE ?= podman compose` · `install` · `fmt` · `lint` · `test` (unit) · `test-all` (unit + integration) · `infra` (Postgres only) · `up` · `down` · `reset-db` (drop the Postgres volume) · `logs`.

---

## 8. CI (`.github/workflows/ci.yml`)

Runs on push/PR to `main` and on manual trigger; a new run cancels the previous one on the same branch (same as core).

**Job `lint-test`** (`ubuntu-latest`, service containers `pgvector/pgvector:pg16` and `rabbitmq:3.13-management-alpine` with health checks):
1. checkout → `astral-sh/setup-uv` (pinned major, cache on) → Python 3.13
2. `apt-get install tesseract-ocr tesseract-ocr-vie`
3. `uv sync --locked`
4. `uv run ruff format --check .` (message on failure: "run `make fmt`") and `uv run ruff check .`
5. `uv run pytest --junitxml=reports/junit.xml --cov=app` (tables are created by the test setup)
6. `dorny/test-reporter` publishes the results (as in core)
7. Docling models cached between runs

**Job `image-build`** (after `lint-test`): `docker build`, no push.

No z.ai key in CI. Real model calls are blocked in tests.

---

## 9. Tests in the setup

| Area | What is checked |
|---|---|
| config | per-use-case model falls back to `GLM_MODEL_DEFAULT`; missing key fails clearly at startup |
| log helper | context fields on every line; payloads hidden unless `LOG_PAYLOADS=true` |
| runner | with Pydantic AI `TestModel`: steps logged in order, request limit stops a loop, gate applied to tool results, `agent_runs` row saved |
| **privacy gate** | **≥ 20 synthetic CVs (EN + VI; one-column, two-column, scanned)** with planted fake names, emails, phones, IDs, addresses, birth dates, education and references. Fails if anything planted survives, or if skills/experience lines are lost. Typed-text cleaning tested separately |
| extraction | right reading order on two-column CVs; scanned Vietnamese page read by OCR |
| upload checks | rejects non-PDF, oversize, too many pages, encrypted, too many files |
| **chat** | with `FunctionModel`: no `sessionId` → new session created with the caller's `user_id`, id returned. Sending with that id continues the session, and the **second turn receives the full first turn** as history. An unknown or other user's `sessionId` → `404`, and no session is created. Personal data planted in a file **or in the typed message** never reaches the model. A failed clean → `422 PII_REMOVAL_FAILED`, the model is never called, and no session is left behind. `model_context_window_exceeded` → `CHAT_CONTEXT_FULL`. Second message while busy → `409`. Same `clientMessageId` twice → one turn. Streaming emits `meta`, `delta`…, `done`; a dropped client leaves an `interrupted` reply. Delete removes the messages |
| messaging | `TestRabbitBroker` (in memory) + real RabbitMQ with a Python stub responder: reply, timeout, `ok:false`, expired message |
| DB | tables created on an empty database; repositories save and read |

`tests/conftest.py` sets Pydantic AI's `ALLOW_MODEL_REQUESTS = False`, so no test can call z.ai.

---

## 10. Order of work and "done when"

1. `git init` + `.gitignore` (with `.env`) + `.dockerignore` + `.env.example` — **before any `git add`**, since `.env` holds your key today. Rename `glm_api_key` → `ZAI_API_KEY`.
2. `uv init --app`, add the libraries, commit `uv.lock`.
3. `core/` + `/health`, `/ready`.
4. `db/` (models, `create_all`, repositories).
5. `llm/` + `agents/runner.py`.
6. `privacy/` + synthetic CV fixtures.
7. `documents/` + `/ai/dev/cv-preview`.
8. `features/chat/`.
9. `messaging/`.
10. Tests (§9).
11. `Dockerfile`, `docker-compose.yaml`, `Makefile`, `README.md`.
12. CI workflow.

**Done when:**
- `make up` starts everything on the shared network; tables appear on an empty database; `/ready` is green.
- `make test-all` passes locally and CI passes on a PR.
- **Chat by hand:**
  - Send a message with a sample CV and no `sessionId`. You get a z.ai reply from the model set in `.env`, plus a new `sessionId`.
  - Send a follow-up with that `sessionId`. The agent remembers the first turn and the file.
  - The same call with `stream=true` shows the reply arriving piece by piece.
  - Logs show `run.start … run.end` with the session and user id.
  - Changing `GLM_MODEL_CHAT` and restarting switches the model.
- `POST /ai/dev/cv-preview` on a sample CV shows the name, contacts and education removed.

---

## 11. Later (not in the MVP setup)

| Item | Comes with |
|---|---|
| The five use cases (`features/*`) and their tools (`identity.profile.get`, `core.job.get`, `core.job.bids.list`, …) | each use case's own plan |
| Chat fields `jobId`, `projectId`, `includeProfile` (agent loads them through tools) | when those tools exist |
| Name and phone lookup for the privacy gate (today: contact-header rule + email from the gateway header) | when the identity tool exists |
| Background job queue for long runs (UC1, UC3) | UC1 / UC3 |
| Embeddings (local model — z.ai has no embeddings API) + pgvector tables + `project.*` event consumer | UC4 |
| "Ready" notifications through noti | UC1 / UC3 |
| A migration tool, once the schema must change without losing data | when real users' chats must survive changes |
| Detecting other people's names in free text with a small local model | only if gate tests show it's needed |
| `mypy` in CI, CD | after MVP |

---

## 12. Open questions

None. The scope is the setup only (including chat); no use case is built after it in this plan.

---

## Appendix A — use cases at a glance (reference for the structure)

| UC | Shape | Answer |
|---|---|---|
| 1 Career roadmap | one agent → skills held / missing, phases | later (background) |
| 2 CV ↔ job match | one agent; every strength/gap must quote the CV or the job | now |
| 3 Applicant ranking | rule-based pre-score → LLM assessment per applicant → ranking | later (background) |
| 4 Job recommendation | local embeddings search → LLM explains the top results | now |
| 5 Project requirements | multi-turn questions → draft shaped like core's `CreateProjectRequest` (can reuse the chat session tables) | now, per turn |

All five: tools are read-only, nothing is invented beyond the CV/profile/job, and only gate-cleaned text reaches z.ai.

## Appendix B — research used

Gemini's findings: `docs/research/01-research-findings.md`. I checked these against the official docs on 2026-10-24:
- z.ai model list ([pricing](https://docs.z.ai/guides/overview/pricing)).
- No embeddings endpoint on z.ai ([docs index](https://docs.z.ai/llms.txt)).
- GLM-OCR layout parsing ([API](https://docs.z.ai/api-reference/tools/layout-parsing.md)).
- Pydantic AI `ZaiModel` ([docs](https://pydantic.dev/docs/ai/models/zai/)).

Corrected Gemini claims:
- The flagship is not `glm-4-plus`; z.ai lists GLM-5.x and 4.x.
- `embedding-3` and the OCR prices are mainland-only figures.
- PyMuPDF4LLM's AGPL licence is not fine for a closed web service.

---

## Changelog

- **v6:** plan completed and limited to this service. Notes about other services' code and deployment removed; no open questions.
- **v5:**
  - Chat: one send endpoint; no `sessionId` → new session (server-generated id returned, stored with `user_id`); separate "create session" endpoint removed.
  - `language` field removed (configured later).
  - Streaming confirmed on z.ai and Pydantic AI; gateway and nginx needs added to §11.
  - Privacy: one rule for files **and** typed text — personal data never goes to z.ai; failures answer "Failed to …".
  - Sessions kept until deleted.
  - All open questions closed: scope is setup only; the public-link storage issue moved to §11 as a note for the identity team.
- **v4:**
  - Added the **chat endpoint**: sessions, full-history replay, PDF attachments, recommended fields, streaming, errors, tests.
  - Removed Alembic and the migrate step; tables are created at startup.
  - Privacy gate split into document (strict) and typed-text (replace only), plus a contact-header rule.
  - Dropped the `/ai/dev/llm-ping` check (chat covers it).
  - New Q-3 to Q-5.
- **v3:** cut to the MVP setup; models in `.env`; education removed from LLM input.
- **v2:** privacy gate, local Docling, FastStream, verified z.ai facts.
- **v1:** first draft.
