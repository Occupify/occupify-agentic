# Review c2 — MVP setup (`occupify-agentic`)

> **Verdict: CHANGES_REQUESTED**
> Reviewed: commit `bf4b014` (fixes for c1) against `docs/setup-plan.md` v6 and `review-c1-mvp-setup.md` · 2026-10-24 · Claude (lead)
> Severity scale from `.handoffs/PROTOCOL.md` §10. BLOCKER and MAJOR must be fixed. **F-29 is a direct request from the owner.**

## What was checked

| Check | Result |
|---|---|
| `ruff format --check .` / `ruff check .` | clean ✅ |
| `pytest tests/` | 55 passed ✅ |
| Privacy gate on the c1 input | fixed ✅ |
| Privacy gate on **real Docling output** (synthetic CV PDF → Docling 2.142.1 → `clean()`) | **leaks** ❌ (F-01) |
| App's own extractor on that PDF | **fell back to pdfium**; Docling never ran ❌ (F-05) |
| Streaming heartbeat pattern, reproduced in isolation | **kills the stream** ❌ (F-21) |

## Status of the c1 findings

| c1 | Status | Note |
|---|---|---|
| F-01 privacy gate | ❌ **still BLOCKER** | c1 input passes; real Docling output still leaks — see below |
| F-02 file name in prompt | ✅ fixed | |
| F-03 streaming bypasses runner | ✅ fixed | new stream issues in F-21, F-25 |
| F-04 error mapping | 🟡 mostly fixed | remaining: F-27 |
| F-05 Docling OCR language | ❌ **not fixed — worse** | see below |
| F-06 blocking extraction | ✅ fixed | |
| F-07 expired cache row | ✅ fixed | |
| F-08 busy lock | ✅ fixed | |
| F-09 `APP_ENV` default / missing key | ✅ fixed | |
| F-10 `/ready` | ✅ fixed | |
| F-11 tests | 🟡 partly | privacy tests better; still no Docling run, no Postgres/RabbitMQ tests — that's how F-05 went unnoticed |
| F-12 CI permissions | ✅ fixed | |
| F-13 settings that do nothing | ➡️ replaced by F-29 | |
| F-14 interrupted stream | 🟡 partly | saved on cancel, but F-21 cancels healthy streams |
| F-15 silent history loss | ✅ fixed | small leftover in F-27 |
| F-16 read before checks | ✅ fixed | regression: F-24 |
| F-17 idempotency | ❌ not fixed | still first 100 messages only; first-message retry (no `sessionId`) creates a second session; index not unique |
| F-18 RPC route / logged args | 🟡 partly | ids-only logging ✅; new double-send in F-26 |
| F-19 raw exception text | 🟡 partly | client side ✅; still in logs and `agent_runs.error` (`run.error`, `broker.connect_failed`, `history.parse_failed`) |
| F-20 `init_db` | ✅ fixed | |

### F-01 · BLOCKER · D-7 · `app/privacy/sections.py:132-212, 215-252` (still open)

**What.** A synthetic CV PDF was run through **real Docling**. **Every** bold line becomes `##`: the name, the job title, the contact line, each role, the school and the referee.

```markdown
## Tran Van Minh
## Senior Backend Developer
## minh.tran@example.com | 091 234 56 78 | Ho Chi Minh City
## WORK EXPERIENCE
## Backend Developer, Acme Software (2020 - 2024)
Built payment APIs with Spring Boot and PostgreSQL.
## EDUCATION
## Ho Chi Minh City University of Technology
B.Eng. Computer Science, 2013 - 2018
## REFERENCES
## Le Thi Hoa
Engineering Manager, Acme Software
```

After `clean()`, the text sent to z.ai still contains **`Ho Chi Minh City University of Technology`** and the referee's name **`Le Thi Hoa`**. `drop_sections` relies on heading *levels*, and Docling's output has none.

More leaks (fake data):
- **No known section heading:** a CV whose sections are `## Tech Stack` / `## Công việc đã làm` keeps `# Nguyễn Văn An` and `Signed: Nguyễn Văn An`.
- **Name repeated in the body:** the name is removed from the top but kept in `## Summary` → "Nguyễn Văn An is a backend developer…".

**Expected.**
1. Once inside a removed section, keep skipping until the next heading whose title is in the **known section vocabulary** (included or removed lists), whatever its level. Unknown `##` lines inside a removed section stay removed.
2. Use the first line of the dropped top block (the name) as `known_name`. Replace it everywhere, with and without accents, and make the final check fail if it still appears.
3. If a **file** has no known section heading at all, fail closed (`PII_REMOVAL_FAILED`) instead of sending it.
4. Add the Markdown above and the two leak cases as regression tests.

### F-05 · MAJOR · D-6 · `app/documents/extract.py:54, 61-62, 94-99` (still open)

**What.** `TesseractOcrOptions` needs the `tesserocr` Python package, which isn't installed (not in `pyproject.toml` or the image). Conversion fails, and `extract_pdf_text` silently falls back to `pdfium` for **every** PDF: no layout, no reading order, no OCR. Verified: `extract_pdf_text(<synthetic CV>)` returns `extractor == "pdfium"`. The Docker image has the same dependencies. `get_converter()` also swallows the reason (`except Exception: False`).

**Expected.**
- Use `TesseractCliOcrOptions(lang=…)`, which uses the `tesseract` binary the Dockerfile installs.
- Log a warning with the error type when falling back.
- Add a `docling`-marked test that asserts `extractor == "docling"` on a synthetic two-column PDF and on a scanned Vietnamese one.
- Run that test in CI: install `tesseract-ocr-vie`, already done, and cache the Docling models at the path Docling actually uses.

## New findings

### F-21 · BLOCKER · plan §6.9 (streaming) · `app/features/chat/service.py:321-326`

**What.** The heartbeat calls `asyncio.wait_for(stream_iter.__anext__(), timeout=15)`. When the timeout fires, `wait_for` **cancels** the pending `__anext__()`. That throws `CancelledError` into `stream_agent`, which marks the run interrupted and ends. The next `__anext__()` then raises `StopAsyncIteration`, so the client gets `: ping` and then nothing: no rest of the reply, no `done`, nothing saved.

Reproduced with a generator that pauses 1 s under a 0.3 s heartbeat: `got: first chunk` → `inner generator got CancelledError` → `heartbeat ping` → `stream ended`. Any reply where the model is quiet for 15 s (first token on a long history, thinking) is lost.

**Expected.** Run the agent stream in its own task that puts items on an `asyncio.Queue`. The response loop waits on `queue.get()` with the heartbeat timeout, which is safe to cancel. Cancel the producer task only when the client really disconnects. Add a test with a model that pauses longer than the heartbeat.

### F-22 · MAJOR · privacy / lost input · `app/privacy/gate.py:61-64`

**What.** The contact-header rule now runs on **typed** text too (the plan limits it to files). A pasted job description in `context` — "We are Acme, hiring…", "## Requirements …", "## Contact …" — becomes an **empty string**, and the model gets nothing, with no error.

**Expected.**
- Contact-header rule for files only.
- If cleaning leaves a typed `message` empty, fail with a "Failed to …" message instead of sending it.

### F-23 · MAJOR · D-8 (keep role dates) · `app/privacy/detectors.py:12`

**What.** The new phone pattern also eats numbers that aren't phones:
- `2020-2024` and `2013-2018` → `[PHONE]`;
- `1.200.000.000 VND` → `[PHONE]`.

Role dates are on the plan's "kept" list, because years of experience are what matching uses.

**Expected.** Don't treat year ranges (`(19|20)\d{2}\s*[-–]\s*(19|20)\d{2}`) or dotted amounts as phones. Add them as tests that must survive cleaning.

### F-24 · MAJOR · plan §6.9 ("no new session on failure") · `app/features/chat/service.py:73-87`

**What.** A new session is now created **before** the files are checked and cleaned, so a rejected PDF or `PII_REMOVAL_FAILED` leaves an empty session in the user's list. In the stream path the client never even learns its id.

**Expected.**
1. Existing session: check and lock it first.
2. Validate, extract and clean everything.
3. Only then create the new session.

### F-25 · MAJOR · API contract (plan §6.9) · `app/features/chat/service.py:278-280, 332-372, 396`

**What.** The Server-Sent Events no longer match the plan or the non-stream reply:

| Event | Plan | Now |
|---|---|---|
| `meta` | `sessionId, newSession, messageId, attachments` | `run_id, session_id, model` |
| `delta` | `text` | `content` |
| `done` | `model, usage{tokensIn, tokensOut}` | `output, tokens_in, tokens_out, ms, session_id, seq` |
| `error` | `errorCode, message` | `code, message` |

The idempotent replay (`service.py:278-280`) uses yet another shape.

**Expected.** Exactly plan §6.9, in camelCase like every other response, in both the normal and the replay path.

### F-26 · MAJOR · `app/messaging/rpc.py:56-71`

**What.** On **any** exception from the exchange request, *including a timeout*, the same request is sent again straight to the queue. A slow responder therefore gets the request twice, and the caller waits up to twice `RABBITMQ_RPC_TIMEOUT_S`. That is harmless for read-only tools, and a real bug as soon as a tool changes data.

**Expected.**
- One route only: exchange `occupify.agent.rpc` + routing key (plan §6.6), no fallback.
- Then `queue_name_for` is unused and goes too (F-29).

### F-27 · MINOR · `app/agents/runner.py`

- `finish_reason == "length"` always becomes `CHAT_CONTEXT_FULL`, but `length` also means the answer simply hit the output limit. Check the raw provider reason (`model_context_window_exceeded`) in the response's provider details instead.
- The run row is created before the history is parsed, so a parse failure leaves it `running` until restart.
- `run_agent` and `stream_agent` duplicate about 120 lines; share the setup and finish steps.

### F-28 · NIT

- A 12-digit CCCD is masked as `[PHONE]`, because the phone pattern runs before the ID pattern. It's still removed.
- `_broker_connected` isn't updated if the broker drops after startup.

### F-29 · REQUIRED (owner request) · whole repo — remove everything not used yet

**Rule:** if nothing in the current code uses a variable, setting, function, class, parameter or file, delete it. Add it back when the feature that needs it is built. Found by scanning the code:

| Remove | Where |
|---|---|
| `GLM_MODEL_CHAT`, `GLM_MODEL_ROADMAP`, `GLM_MODEL_CV_MATCH`, `GLM_MODEL_APPLICANT_RANKING`, `GLM_MODEL_JOB_RECOMMENDATION`, `GLM_MODEL_PROJECT_DRAFT` | `.env.example`, `config.py`. Keep one model setting; I suggest renaming `GLM_MODEL_DEFAULT` → `GLM_MODEL`, since nothing overrides it any more |
| the per-use-case mapping in `Settings.model_for()` and `llm/glm.py:model_for(use_case)` | use the single model setting directly |
| the six-entry `models_info` startup log | `main.py:25-34` → log the one model |
| `GLM_THINKING`, `LOG_PAYLOADS`, `PDF_ALLOWED_HOSTS` | `.env.example`, `config.py` |
| `RABBITMQ_RPC_EXCHANGE` **or** `topology.RPC_EXCHANGE` (keep one) | `config.py`, `topology.py` |
| `queue_name_for` (after F-26) | `topology.py` |
| `SingleResponse`, `PageResponse`, `ErrorResponse`, `PagingMeta` | `core/responses.py` (the dict helpers are what's used) |
| `known_name` parameter — **unless** used for the name replacement in F-01 | `privacy/gate.py` |
| `filename` parameter ("for backwards compatibility" — this repo has no old callers) | `documents/extract.py:81` |
| `ocr_pages` return value (always 0, every caller ignores it) and the `ocr_pages` log field | `documents/extract.py` |
| `session_id` parameter of `create_session()` | `db/repositories/chat.py:24` |
| `trace_id` parameter of `run_agent()` / `stream_agent()` (never passed) | `agents/runner.py` |
| `timeout_s` parameter of `RpcClient.call()` (never passed) | `messaging/rpc.py` |
| `AgentDeps.rpc` field (never set or read) | `agents/deps.py` |
| `app/tools/` (only a comment) | delete the package |
| "Planned features" list | `app/features/README.md` |
| the "rename your current glm_api_key" comment | `.env.example` |

**Keep, but wire up** — the chat uses these now:
- `GLM_TIMEOUT_S`: pass it as the model request timeout. Without it a hung z.ai call holds the session busy past the 300 s stale window.
- `CHAT_STREAM_HEARTBEAT_S`: used by the fixed heartbeat (F-21).
- `OCR_LANGS`: F-05.

**Kept on purpose:** `set_engine` / `set_broker` (tests use them) and the RabbitMQ request/reply client (in the approved setup scope).

## Fix order

1. **F-01 and F-05 together.** The privacy fix must be tested on real Docling output. Write the tests first.
2. **F-21, F-22, F-23.**
3. **F-24, F-25, F-26.**
4. **F-29 cleanup.**
5. The F-11 leftovers, then F-17, F-19, F-27.

Reply with a `REVIEW_REQUEST` naming the new commit.
