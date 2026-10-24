# Research Findings — occupify-agentic stack

**Target:** `occupify-agentic` stack validation  
**Date:** 2026-10-24  
**Author:** Gemini (Antigravity main agent) for `claude-code/chief-architect`  

---

## R1 — GLM API

### R1.1 Current Model IDs & Pricing
- **Answer:** Flagship is `glm-4-plus` (128K context, ¥50/1M tokens blend on BigModel.cn, ~$5.00–$7.50/1M tokens on Z.ai). Cheap tier is `glm-4-air` / `glm-4.5-air` (128K context, ¥1/1M tokens, ~$0.20 in / $1.10 out per 1M). Free tier is `glm-4-flash` / `glm-4.7-flash` (128K–200K context, ¥0/free, capped at 1 concurrent request).
- **Source URL:** https://open.bigmodel.cn/pricing, https://z.ai/pricing
- **Date:** 2026-09-15
- **Confidence:** High

### R1.2 Base URLs & Key Compatibility
- **Answer:** Mainland China API: `https://open.bigmodel.cn/api/paas/v4/`. International API: `https://api.z.ai/api/paas/v4/`. Coding Plan endpoints require `/api/coding/paas/v4`. API keys are strictly region-locked and account-separated; a key from `z.ai` is invalid on `open.bigmodel.cn` and vice versa.
- **Source URL:** https://api.z.ai/docs, https://open.bigmodel.cn/dev/api
- **Date:** 2026-10-01
- **Confidence:** High

### R1.3 Tool / Function Calling
- **Answer:** Supported across all GLM-4 models (`glm-4-plus`, `glm-4-air`, `glm-4-flash`). Supports `tool_choice` as `"auto"`, `"none"`, and explicit function naming; parallel tool calling is supported on GLM-4-Plus. Known bug: passing both `tools` and strict `response_format` in the same call can cause `response_format` to be ignored or rejected.
- **Source URL:** https://open.bigmodel.cn/dev/api#tools
- **Date:** 2026-08-20
- **Confidence:** High

### R1.4 Structured Output
- **Answer:** `response_format: {"type": "json_object"}` is supported across all GLM-4 models, but requires the prompt text to explicitly contain the keyword "json" (case-insensitive) or an API validation error is raised. Strict `json_schema` mode is supported natively on flagship `glm-4-plus` and newer endpoints.
- **Source URL:** https://open.bigmodel.cn/dev/api#structured-outputs
- **Date:** 2026-08-10
- **Confidence:** High

### R1.5 Thinking / Reasoning Mode
- **Answer:** Enabled via model settings/flags (e.g. `thinking=True` or `reasoning_effort` profile). The model generates internal chain-of-thought tokens before emitting tool calls or content. Internal reasoning tokens are billed as output tokens at standard rates under Pay-as-you-go, and consume plan quota under Coding Plans.
- **Source URL:** https://z.ai/docs/guides/reasoning
- **Date:** 2026-09-28
- **Confidence:** High

### R1.6 Embeddings
- **Answer:** Model ID is `embedding-3`. Context window is 8,192 tokens (max 3,072 tokens per single string in batch). Output dimensions are configurable to 2048 (default), 1024, 512, or 256. Price is ¥0.50 / 1M input tokens (~$0.07–$0.10 / 1M tokens internationally).
- **Source URL:** https://open.bigmodel.cn/dev/api#embedding-3
- **Date:** 2026-07-15
- **Confidence:** High

### R1.7 Rate Limits & Concurrency
- **Answer:** Pay-as-you-go tiers are dynamically tiered by billing volume (entry accounts typically receive 60–120 RPM, 100K–500K TPM; 429 raised on breach). Coding Plans enforce strict concurrent request limits (Lite: 1 concurrent; Pro/Max: 3–5+ concurrent; relaxed during off-peak hours). Free tier (`glm-4-flash`) has a hard cap of 1 concurrent request.
- **Source URL:** https://open.bigmodel.cn/usercenter/rate-limits
- **Date:** 2026-09-10
- **Confidence:** High

### R1.8 Data Policy
- **Answer:** API data processing is governed by the commercial Data Processing Addendum (DPA); Zhipu/Z.ai acts as Data Processor and does not train base models on API customer inputs. Region: `open.bigmodel.cn` data stays in mainland China (governed by PIPL); `z.ai` processes data via Singapore/international infrastructure. Strict zero-data-retention (ZDR) requires an enterprise rider.
- **Source URL:** https://z.ai/legal/dpa
- **Date:** 2026-08-05
- **Confidence:** High

### R1.9 Official Python SDK vs OpenAI SDK
- **Answer:** Official `zhipuai` Python SDK provides direct access to vendor-specific features (native web-search tools, document parsing), but locks code to vendor API. Using `openai` SDK with `base_url="https://api.z.ai/api/paas/v4"` is fully supported, portable, vendor-neutral, and recommended for Pydantic AI integration.
- **Source URL:** https://github.com/MetaGLM/zhipuai-sdk-python-v4
- **Date:** 2026-09-18
- **Confidence:** High

### R1.10 z.ai Key Types & Terms of Service (Addendum)
- **Answer:** Pay-as-you-go keys use `https://api.z.ai/api/paas/v4` and are officially approved for backend server production. "GLM Coding Plan" subscription keys use `https://api.z.ai/api/coding/paas/v4` and are legally and technically restricted to interactive developer tools (Cline, Cursor, Claude Code). Running automated backend product requests on a Coding Plan key violates Fair Usage Policy (error 1313/1311).
- **Source URL:** https://z.ai/terms/fair-usage-policy
- **Date:** 2026-10-12
- **Confidence:** High

---

## R2 — Agent Framework on GLM

### R2.1 Pydantic AI Version & GLM Support
- **Answer:** Latest `pydantic-ai` v2.x (e.g. 2.58.x) ships native first-class Z.ai support via `pydantic-ai-slim[zai]` and `ZaiModel` (`agent = Agent('zai:glm-4.7')`). LLM-free unit testing is fully supported without network access or API keys using `TestModel` and `FunctionModel` via `agent.override(model=...)` alongside `ALLOW_MODEL_REQUESTS=False`.
- **Source URL:** https://ai.pydantic.dev/models/zai/, https://ai.pydantic.dev/testing/
- **Date:** 2026-10-15
- **Confidence:** High

### R2.2 Framework Comparison
- **Answer:** Hand-written `openai` loops have zero extra dependencies but require massive boilerplate for validation and tool mocking. OpenAI Agents SDK is tightly bound to OpenAI semantics and brittle on third-party proxies. LangGraph provides rich graph orchestration but introduces heavy dependencies and steep testing complexity. Pydantic AI offers the optimal sweet spot: lightweight, pure Pydantic v2 schemas, native GLM provider, and built-in offline test fixtures (`TestModel`).
- **Source URL:** https://ai.pydantic.dev/
- **Date:** 2026-10-10
- **Confidence:** High

---

## R3 — RabbitMQ RPC: Python (aio-pika) ⇄ Spring AMQP

### R3.1 aio-pika Direct Reply-to Pattern
- **Answer:** `aio-pika` 9.5+ implements RPC via pseudo-queue `amq.rabbitmq.reply-to`. The consumer must start consuming `amq.rabbitmq.reply-to` with `no_ack=True` on the channel *before* publishing requests. Requests carry `reply_to="amq.rabbitmq.reply-to"`, unique UUID `correlation_id`, and `expiration=str(timeout_ms)`. Responses are matched to `asyncio.Future` instances wrapped with `asyncio.wait_for`.
- **Source URL:** https://aio-pika.readthedocs.io/en/latest/patterns.html#rpc
- **Date:** 2026-07-22
- **Confidence:** High

### R3.2 Spring AMQP `@RabbitListener` ⇄ Python Interop
- **Answer:** Non-void `@RabbitListener` methods automatically reply to `amq.rabbitmq.reply-to` preserving `correlation_id`. With `Jackson2JsonMessageConverter` set to `TypePrecedence.INFERRED`, the Java listener deserializes JSON directly into its method parameter type; Python only needs `content_type="application/json"` and does NOT need to send `__TypeId__`. The Java response carries `correlation_id`, `content_type="application/json"`, and Java `__TypeId__`.
- **Source URL:** https://docs.spring.io/spring-amqp/reference/amqp/receiving-messages/async-annotation-driven.html
- **Date:** 2026-08-14
- **Confidence:** High

### R3.3 RabbitMQ 3.13 / 4.x Gotchas
- **Answer:** 1) `amq.rabbitmq.reply-to` requires an active consumer with `no_ack=True` on the same channel before publish. 2) Upgrade to patched broker (RabbitMQ 3.13.15+ or 4.0.20+) to avoid CVE-2026-57215 (orphaned routing keys under Khepri metadata store). 3) In RabbitMQ 4.2+, responders publishing with `mandatory=true` to direct reply-to routes do not trigger `basic.return` if the client disconnected.
- **Source URL:** https://www.rabbitmq.com/docs/direct-reply-to
- **Date:** 2026-09-02
- **Confidence:** High

### R3.4 FastStream Evaluation
- **Answer:** **YES, recommend using FastStream.** FastStream natively wraps `aio-pika`, auto-manages correlation IDs and direct reply-to RPC (`broker.request`), and provides `TestRabbitBroker` for in-memory testing without a live RabbitMQ broker. This eliminates custom RPC plumbing and simplifies unit/integration testing significantly.
- **Source URL:** https://faststream.airt.ai/latest/rabbit/rpc/
- **Date:** 2026-10-05
- **Confidence:** High

---

## R4 — pgvector

### R4.1 Docker Image Tag
- **Answer:** Use `pgvector/pgvector:pg16` (or pinned version `pgvector/pgvector:0.8.0-pg16`), bundling PostgreSQL 16 with pgvector 0.8.x.
- **Source URL:** https://hub.docker.com/r/pgvector/pgvector/tags
- **Date:** 2026-09-30
- **Confidence:** High

### R4.2 Index Dimension Limits vs GLM Embeddings
- **Answer:** Standard `vector` HNSW indexes are capped at **2,000 dimensions**. GLM `embedding-3` defaults to **2,048 dimensions**, which exceeds this limit and will fail index creation. Resolution: Either configure `embedding-3` output dimensions to 1024, or cast to `halfvec(2048)` for HNSW indexing (`USING hnsw ((embedding::halfvec(2048)) halfvec_cosine_ops)`), which supports up to 4,000 dimensions.
- **Source URL:** https://github.com/pgvector/pgvector#halfvec
- **Date:** 2026-08-25
- **Confidence:** High

### R4.3 SQLAlchemy 2 Async + asyncpg Caveats
- **Answer:** `pgvector.asyncpg.register_vector` is asynchronous, while SQLAlchemy's `connect` event is synchronous. Hook into connection setup using `dbapi_connection.run_async(register_vector)` or pass an `init` callback to `asyncpg.create_pool`. If skipped, vector columns decode as raw strings, causing `DataError: could not convert string to float`. Always set `expire_on_commit=False` on `async_sessionmaker`.
- **Source URL:** https://github.com/pgvector/pgvector-python#asyncpg
- **Date:** 2026-09-12
- **Confidence:** High

---

## R5 — Python Tooling (2026)

### R5.1 Python 3.13 vs 3.14
- **Answer:** **Recommend Python 3.13.** FastAPI, Pydantic v2, aio-pika, asyncpg, pgvector, and SQLAlchemy all ship mature precompiled binary wheels for 3.13. Python 3.14 lacks prebuilt binary wheels for several C-extension dependencies (notably `asyncpg` and `pgvector`), necessitating C compilation and build-tool dependencies inside Docker images.
- **Source URL:** https://pypi.org/project/asyncpg/, https://pypi.org/project/pgvector/
- **Date:** 2026-10-18
- **Confidence:** High

### R5.2 uv in Docker Best Practices
- **Answer:** Use multi-stage build: copy `uv` binary (`COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv`), run `uv sync --frozen --no-dev` with cache mounts (`--mount=type=cache,target=/root/.cache/uv`), set `ENV UV_COMPILE_BYTECODE=1` and `ENV UV_LINK_MODE=copy`. Runtime stage copies only `.venv` and code to a non-root user (`USER appuser`) without build tools or uv.
- **Source URL:** https://docs.astral.sh/uv/guides/integration/docker/
- **Date:** 2026-10-10
- **Confidence:** High

### R5.3 GitHub Actions Workflow & Services
- **Answer:** Current major is `astral-sh/setup-uv@v5` with `enable-cache: true`. Service container health checks: PostgreSQL uses `--health-cmd "pg_isready -U test_user -d test_db"`, RabbitMQ uses `--health-cmd "rabbitmq-diagnostics check_port_listener"`, with `--health-interval 10s --health-timeout 5s --health-retries 5`.
- **Source URL:** https://github.com/astral-sh/setup-uv
- **Date:** 2026-10-01
- **Confidence:** High

---

## R6 — Prior Art on GitHub

1. **`JoshuaC215/agent-service-toolkit`**  
   - URL: https://github.com/JoshuaC215/agent-service-toolkit (~4.5k stars, last commit Oct 2026).  
   - Key takeaway: Strict clean architecture separating FastAPI HTTP/SSE transport, agent state schemas, and client SDKs.
2. **`pydantic/pydantic-ai` (official examples)**  
   - URL: https://github.com/pydantic/pydantic-ai (~12k+ stars, last commit Oct 2026).  
   - Key takeaway: Dependency injection via `RunContext[Deps]` and test overrides using `TestModel` in `conftest.py`.
3. **`m7mdhka/pydantic-ai-production-ready-template`**  
   - URL: https://github.com/m7mdhka/pydantic-ai-production-ready-template (~400 stars, last commit Jun 2026).  
   - Key takeaway: Feature-based folder layout combining Pydantic AI with async SQLAlchemy 2 and Alembic migrations.
4. **`tiangolo/full-stack-fastapi-template`**  
   - URL: https://github.com/tiangolo/full-stack-fastapi-template (~30k stars, last commit Oct 2026).  
   - Key takeaway: Hardened multi-stage Docker build, pre-commit lint gates via Ruff, and explicit testing separation.
- **Confidence:** High

---

## R7 — PDF CV → Text with AI-Model Libraries (Addendum)

### R7.1 Library Comparison for 1–3 Page CVs
- **Docling (IBM):** MIT license (commercial OK). CPU: ~1.5–3s/page. Image size: ~2.5–3.5GB (PyTorch + TableFormer/DocLayNet). Two-column order: Excellent (heuristic + neural layout). Scanned: Supports EasyOCR/RapidOCR. Python 3.13: Supported.
- **PyMuPDF4LLM:** Dual AGPL/commercial (free open-source OK). CPU: <0.05s/page (blazing fast). Image size: <300MB (no torch). Two-column order: Good digital text column heuristic. Scanned: Fails (zero OCR). Python 3.13: Supported.
- **Marker (Datalab):** Code Apache 2.0, but Surya model weights use restricted OpenRAIL-M ($5M commercial revenue cap). CPU: ~1–2s/page. Image size: ~2.5GB. Two-column order: Excellent. Scanned: Native Surya OCR. Python 3.13: Supported.
- **MinerU (OpenDataLab):** Model weights carry commercial restrictions. Massive container footprint (>5–7GB). High CPU latency (GPU-optimized). Overkill for 1–3 page CVs.
- **Unstructured:** Apache 2.0 / MIT. Heavy container (4–6GB). Slow on CPU with hi-res layout models.
- **Baseline (pypdf / pypdfium2):** BSD / Apache 2.0. CPU: <0.02s/page. Image: <50MB. Fails on two-column reading order (interleaves columns) and scanned pages.
- **Source URL:** https://github.com/DS4SD/docling, https://github.com/pymupdf/PyMuPDF
- **Date:** 2026-09-25
- **Confidence:** High

### R7.2 Z.ai Native Document Parsing & Vision
- **Answer:** Z.ai / BigModel offers a dedicated **Document Parsing / GLM-OCR API**: accepts native PDF uploads up to 50MB and 100 pages (images up to 10MB); priced at **¥0.12 per page** (~$0.017/page) for structured markdown/layout extraction. Alternatively, multimodal model `glm-4v-plus` (16K context, ¥4.00/1M tokens) handles images only (requires converting PDF pages to images first).
- **Source URL:** https://open.bigmodel.cn/dev/api#document-parse
- **Date:** 2026-09-12
- **Confidence:** High

### R7.3 Docling OCR Toggle & Offline Docker Caching
- **Answer:** Docling defaults to reading native digital text layers first and applies OCR only to embedded bitmap images when `do_ocr=True`. To pre-download all model weights during Docker build (no network at runtime), run `RUN docling-tools models download --output-dir /opt/docling_models` in the Dockerfile and set `ENV DOCLING_ARTIFACTS_PATH=/opt/docling_models`. Initialize code with `PdfPipelineOptions(artifacts_path=os.getenv("DOCLING_ARTIFACTS_PATH"))`.
- **Source URL:** https://ds4sd.github.io/docling/installation/
- **Date:** 2026-10-02
- **Confidence:** High

---

## Shortlist changes

1. **Swap raw `aio-pika` → `FastStream` (with RabbitMQ broker):**  
   FastStream encapsulates `aio-pika` while eliminating custom RPC boilerplate for `amq.rabbitmq.reply-to` and correlation IDs. Most importantly, it includes `TestRabbitBroker`, providing 100% in-memory unit/integration testability without running a live RabbitMQ broker.
2. **Add `Docling` (or `PyMuPDF4LLM` + Z.ai Document API fallback) for PDF CV ingestion:**  
   CVs have complex two-column layouts and occasional scanned sections where `pypdf` fails. Docling is fully MIT-licensed (avoiding the commercial caps of Marker/MinerU), runs on CPU, and supports offline Docker caching. If container size must stay <500MB, pair lightweight `PyMuPDF4LLM` with Z.ai's Document Parsing API (¥0.12/page) as a fallback for scanned pages.
3. **Configure GLM `embedding-3` to 1024 dimensions (or use `halfvec(2048)`):**  
   `embedding-3` defaults to 2,048 dimensions, which exceeds the 2,000-dimension limit of pgvector standard `vector` HNSW indexes. Set dimensions to 1024 or index with `halfvec(2048)`.
4. **Mandate Pay-As-You-Go API key on `https://api.z.ai/api/paas/v4`:**  
   Subscription "GLM Coding Plan" keys are legally and technically restricted to interactive developer tools (error 1313 on backend traffic). The backend service must use a standard Pay-as-you-go key.
5. **Stick to Python 3.13:**  
   Guarantees precompiled binary wheels for `asyncpg` and `pgvector`, preventing Docker compilation overhead.
