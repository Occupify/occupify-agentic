# occupify-agentic

Lightweight Python AI service for the Occupify freelance platform.

## Architecture

- **Runtime:** Python 3.13 + FastAPI + Uvicorn
- **Agent Orchestration:** Pydantic AI with native Z.ai model (`ZaiModel`)
- **LLM Provider:** GLM models on z.ai (Pay-as-you-go API key)
- **Messaging & RPC:** FastStream with RabbitMQ (Direct Reply-To `amq.rabbitmq.reply-to`)
- **Document Processing:** Local Docling + Tesseract OCR (Vietnamese + English) with PDFium fallback
- **Privacy Gate:** Zero raw personal data leaves our infrastructure; automatic PII filtering
- **Database:** PostgreSQL 16 + pgvector (tables auto-created at startup)

## Quick Start

### 1. Requirements

- Python 3.13 (managed via [uv](https://github.com/astral-sh/uv))
- Podman / Docker
- Tesseract OCR (optional for host dev, baked into Docker container)

### 2. Environment Configuration

Copy `.env.example` to `.env` and supply your `ZAI_API_KEY`:

```bash
cp .env.example .env
```

### 3. Install Dependencies

```bash
make install
```

### 4. Run Tests & Linter

```bash
make test        # Run unit tests
make lint        # Run ruff format and lint checks
```

### 5. Run Locally

```bash
make run         # Starts FastAPI server on http://localhost:8186
```

Or run via containers:

```bash
make up          # Starts postgres-agentic and agentic containers
```

## Endpoints

- `GET /health` — Liveness probe
- `GET /ready` — Readiness probe (PostgreSQL + RabbitMQ)
- `POST /ai/chat/messages` — Send chat message (supports `stream=true` SSE and PDF attachments)
- `GET /ai/chat/sessions` — List user chat sessions
- `GET /ai/chat/sessions/{sessionId}/messages` — Get session message history
- `DELETE /ai/chat/sessions/{sessionId}` — Delete chat session
- `POST /ai/dev/cv-preview` — Local-only preview to verify PII scrubbing on uploaded PDFs
