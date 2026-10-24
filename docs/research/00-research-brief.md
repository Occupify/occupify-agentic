# Research brief — occupify-agentic stack (from claude-code/chief-architect)

**For:** Gemini (Antigravity main agent) — web research only, no code.
**Write your answer to:** `occupify-agentic/docs/research/01-research-findings.md`
**Date context:** 2026-10-24. Prefer sources from the last 6 months; give a date for every fact.

## Context (short)

We are building `occupify-agentic`: a lightweight Python service that runs 5 AI agents for a freelance platform
(career roadmap, CV↔job matching, applicant ranking, job recommendation, project-requirement drafting —
see `occupify-agentic/docs/usecases.md`). The LLM is **GLM (Zhipu AI / Z.ai)**. Other services are Spring Boot 3
(Java 25) talking over **RabbitMQ 3.13**; databases are **PostgreSQL 16**. Our current shortlist:
FastAPI · Pydantic AI · aio-pika · PostgreSQL 16 + pgvector · SQLAlchemy 2 async + Alembic · uv · ruff · pytest.

Your findings decide whether that shortlist holds. Where the answer is "it depends", say on what.

## Questions

### R1 — GLM API (most important)
1. Current model IDs: flagship, cheap/fast tier, any free tier. Context window and price per 1M input/output tokens for each.
2. Base URLs: international (`api.z.ai`) vs mainland (`open.bigmodel.cn`). Exact OpenAI-compatible path for each. Is an API key from one valid on the other?
3. Tool/function calling in OpenAI format: supported models, `tool_choice` values, parallel tool calls, known bugs.
4. Structured output: is `response_format` `json_object` and/or `json_schema` supported? On which models?
5. "Thinking" / reasoning mode: how it is switched on/off, and how it interacts with tool calls and billing.
6. Embeddings: model ID, output dimensions (configurable? which values?), max input tokens, price.
7. Rate limits / concurrency limits per account tier.
8. Data policy for API inputs: retention, training on API data, region of processing. (We will send CV-like personal data.)
9. Official Python SDK (`zai-sdk` / `zhipuai`) status vs simply using the `openai` Python SDK with a custom `base_url`.

### R2 — Agent framework on GLM
1. Pydantic AI: latest version; does it ship a provider for Z.ai/Zhipu, or must we use `OpenAIProvider(base_url=...)`? Any reported issues with GLM tool calls or structured output (GitHub issues)? Confirm `TestModel` / `FunctionModel` for LLM-free unit tests.
2. One-paragraph comparison against: a hand-written loop on the `openai` SDK, OpenAI Agents SDK, LangGraph. Criteria: dependency weight, GLM compatibility, testability without network, maintenance activity.

### R3 — RabbitMQ RPC: Python (aio-pika) ⇄ Spring AMQP
1. aio-pika latest version; recommended request/reply pattern with **direct reply-to** (`amq.rabbitmq.reply-to`), `correlation_id`, client-side timeout and per-message `expiration`.
2. Spring AMQP `@RabbitListener` that **returns a value**: does it reply to `amq.rabbitmq.reply-to` automatically? With `Jackson2JsonMessageConverter` + `TypePrecedence.INFERRED`, what must a Python publisher set (`content_type`, `__TypeId__` header?) for the Java listener to deserialize it? What headers does the Java reply carry?
3. Gotchas (e.g. direct reply-to needs a no-ack consumer on the same channel before publishing; behaviour changes in RabbitMQ 3.13 / 4.x).
4. Is **FastStream** (RPC via `broker.request`, in-memory `TestRabbitBroker`) worth using instead of raw aio-pika for a small service? Yes/no with reason.

### R4 — pgvector
1. Docker image tag for Postgres 16 + pgvector and the pgvector version inside it.
2. Index dimension limits today (`vector` HNSW, `halfvec`), compared with the GLM embedding dimensions from R1.6.
3. Python: `pgvector` package with SQLAlchemy 2 async + asyncpg — any caveats.

### R5 — Python tooling (2026)
1. Python 3.13 vs 3.14: do FastAPI, Pydantic AI, aio-pika, asyncpg, pgvector, SQLAlchemy all ship 3.14 wheels? Recommend one.
2. uv in Docker: current official best practice (multi-stage, `--frozen`/`--locked`, cache mounts, `UV_COMPILE_BYTECODE`, non-root user). Link the Astral doc.
3. GitHub Actions: current major of `astral-sh/setup-uv`; example `services:` block for pgvector Postgres + RabbitMQ with health checks.

### R6 — Prior art on GitHub
Up to 5 open-source FastAPI + LLM-agent service templates/repos (e.g. Pydantic AI examples, agent-service-toolkit, FastAPI agent templates).
For each: link, stars, last commit date, and the one idea about folder structure or testing worth borrowing.

## Addendum (sent as message #2) — the human answered: key is from **z.ai**; CVs arrive as **PDF** and must become text

### R1.10 — z.ai key types
Pay-as-you-go API key vs "GLM Coding Plan" subscription key: which base URL each one works on (`/api/paas/v4` vs a coding endpoint?), and do z.ai's terms allow a Coding Plan key inside a product backend?

### R7 — PDF CV → text with an AI-model library
1. Compare for 1–3 page CVs (two-column layouts, icons, some scanned): **Docling**, **Marker**, **MinerU**, **Unstructured**, **PyMuPDF4LLM**, and the non-AI baseline **pypdf / pypdfium2**. For each: licence (commercial use OK?), CPU-only seconds per page, extra Docker image size (torch? model downloads?), quality on two-column reading order and scanned pages, Python 3.13 support.
2. z.ai itself: is there a document-parsing / OCR / layout API, or a vision model (GLM-*V) suited to PDF→text? Model id, price per page or per image, max file size, can a PDF be sent directly or only images?
3. Can Docling run with OCR off by default and on only when a page has no text layer? How to pre-download its models at Docker build time (no network at runtime)?

## Output format (`01-research-findings.md`)

For each `R<n>.<m>`: **answer** (1–4 lines) · **source URL** · **date of source** · **confidence** (high/med/low).
End with a section **"Shortlist changes"**: which item of our shortlist you would swap, and why — or "none".
Keep it under ~300 lines.

## Rules
- Do not read or quote `.env*`, `ref.md` or any key.
- Do not write code or change any file other than `01-research-findings.md`.
- Do not write into `.handoffs/`.
