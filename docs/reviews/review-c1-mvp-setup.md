# Review c1 — MVP setup (`occupify-agentic`)

> **Verdict: CHANGES_REQUESTED**
> Reviewed: commit `3183b79` on `main` · against `docs/setup-plan.md` v6 · 2026-10-24 · Claude (lead)
> Severity scale from `.handoffs/PROTOCOL.md` §10: BLOCKER and MAJOR must be fixed before approval.

## What was checked

| Check | Result |
|---|---|
| `.env` tracked or in history | no — ignored and untracked ✅ |
| `ruff format --check .` / `ruff check .` | clean ✅ |
| `pytest tests/` | 46 passed ✅ — but see F-11: the suite misses the cases below |
| Privacy gate on Docling-style Markdown (fake data, real `clean()`) | **leaks** ❌ — see F-01 |
| Code read against plan §1–§10 | findings below |

Done well: folder structure, envelopes matching core, model per use case from `.env`, `sessionId` / `user_id` handling (new session when absent, 404 without creating one), "Failed to …" messages, Dockerfile/compose shape, `.gitignore`.

## Findings

### F-01 · BLOCKER · D-7 · `app/privacy/sections.py:128`, `app/privacy/detectors.py:12,40`, `app/privacy/gate.py:85`

**What.** On CV text shaped like Docling's Markdown output, `clean()` lets personal data through, and its own re-check passes it. Reproduced with fake data:

```markdown
# Nguyễn Văn An
Senior Backend Developer
- Email: an.nguyen@gmail.com
- Phone: 091 234 56 78
- Date of birth: 12/03/1995
- Address: 25 Lê Lợi, Quận 1, TP.HCM
## Work Experience
Backend Developer at FPT Software (2020-2024)
## Education & Training
### Đại học Bách Khoa TP.HCM
## References
### Trần Thị Bình
Engineering Manager, FPT Software
```

Output sent to z.ai still contains: **the name, the phone, date of birth, address, the school and the referee's name**. Only the email was removed.

Also leaking:
- table rows `| Date of birth | 12/03/1995 |`, `| Address | … |`, `| Nationality | … |`
- `**Ngày sinh:** 12/03/1995`
- the phone formats `+84 91 234 56 78` and `091 234 56 78`
- `Passport C1234567`

**Why.**
1. `drop_contact_header` only acts when the first heading is at index > 0. Docling renders the CV owner's name as a heading (`# Name`), so the index is 0 and nothing is dropped — and in the setup the name can only be removed by this rule.
2. `LABELLED_LINE_REGEX` is anchored at line start, so list items (`- `), bold (`**…**`) and table rows (`| … |`) never match.
3. `drop_sections` stops skipping at *any* Markdown heading, so a `###` sub-heading inside Education or References ends the drop. It also only matches exact headings, so "Education & Training" is kept.
4. `PHONE_REGEX` needs 3–4-digit groups, so the 2-digit groupings common in Vietnam pass. There is no passport pattern.
5. `has_pii_remnants` reuses the same regexes and never checks names, so the "check again, fail if unsure" step can't catch any of the above.

**Expected.**
- Drop the whole top block of a file up to the first section heading from the *known* list (Experience, Skills, Summary, …), counting `#`/`##` lines that aren't in that list as part of the block. This removes the name even before identity can tell us it.
- Match labels anywhere after list/bold/table markup.
- Keep skipping a dropped section until the next heading of the same or a higher level.
- Match headings that *start with* a removed keyword.
- Recognize phones by digit count (9–12 digits) across any separators. Add passport (`[A-Z]\d{7,8}`).
- The re-check must use the same normalization.
- Add the inputs above as regression tests (F-11).

### F-02 · BLOCKER · D-7 · `app/pydantic_ai_helpers.py:104`, `app/features/chat/service.py:126`

**What.** The attachment's file name goes into the prompt unchanged: `--- BEGIN ATTACHED FILE: {filename} ---`.

**Why.** CV files are routinely named after the person (`CV_Nguyen_Van_An.pdf`), so the name reaches z.ai. The name is also written to logs (`extract.py:99`, `gate.py` `source`).

**Expected.** Label files in the prompt as `Attachment 1`, `Attachment 2`, …. Keep the real name only in our DB and the API response. Log a hash or the index, not the name.

### F-03 · MAJOR · plan §6.2 (log of the agent flow) · `app/pydantic_ai_helpers.py:23-244`

**What.** The streaming path doesn't use the runner, so streamed turns write no `agent_runs` row and no `llm.request` / `llm.response` / `run.end` / `run.error` steps. The whole chat flow is duplicated between `service.py` and `pydantic_ai_helpers.py`, and the copies already differ:
- idempotency exists only in the non-stream path;
- the stream path has no run record.

**Expected.**
- One chat service function.
- A `stream_agent()` in `agents/runner.py` that does everything `run_agent()` does (context, run row, steps, limits, error mapping) and yields deltas.
- `pydantic_ai_helpers.py` removed (plan §5 puts this in `features/chat/service.py`).

### F-04 · MAJOR · plan §6.9 (context full) · `app/agents/runner.py:35-45`

**What.** Errors are classified by searching the exception text for "context window" / "too long" / "policy". With pydantic-ai 2.61, z.ai's `model_context_window_exceeded` becomes finish reason `length`. With no output, that raises `UnexpectedModelBehavior("Model token limit … exceeded before any response was generated…")`, which maps to `LLM_UNAVAILABLE` — "Failed to reach the AI model. Please try again." The user retries a session that can never succeed. With partial output, the truncated reply is saved as `complete`. `test_chat_context_full_error` raises a hand-written message, so it can't catch this.

**Expected.**
- Classify by type: `ModelContextWindowExceededError`, `ContentFilterError`, `UsageLimitExceeded`, `ModelHTTPError` 400 with the context-window body, and `UnexpectedModelBehavior` with finish reason `length` → `CHAT_CONTEXT_FULL`.
- On success, treat `response.finish_reason == "length"` as context full rather than saving a cut-off reply.
- Test with what the library actually raises.

### F-05 · MAJOR · D-6 · `app/documents/extract.py:41-44`

**What.** Docling's OCR is left at `OcrAutoOptions` with no language. `OCR_LANGS` is never read, so the `tesseract-ocr-vie` installed in the Dockerfile is never used, and scanned Vietnamese CVs are read with whatever engine and language Docling picks. Tests force `PDF_EXTRACTOR=pdfium`, so the Docling path has no test at all.

**Expected.** Configure Docling's Tesseract OCR with `OCR_LANGS` (`vie`, `eng`). Add at least one `docling`-marked test that runs Docling on a synthetic two-column PDF and a scanned Vietnamese PDF.

### F-06 · MAJOR · `service.py:102`, `pydantic_ai_helpers.py:80`, `api/dev.py:21`

**What.** `extract_pdf_text()` (Docling, seconds per page) is called synchronously inside `async` handlers.

**Why.** While one PDF is being read, every other request stalls, including other users' streams and `/health`.

**Expected.** `await asyncio.to_thread(extract_pdf_text, …)` (or Starlette's `run_in_threadpool`).

### F-07 · MAJOR · `app/db/repositories/documents.py:35-49`

**What.** `get_by_sha256` ignores expired rows, so after 30 days `save_document` inserts a second row with the same `sha256`. The unique constraint makes that an unhandled `IntegrityError`, so **every later upload of that same file returns 500**.

**Expected.** Upsert: on conflict on `sha256`, refresh `cleaned_text`, `removed_counts` and `expires_at`. Or delete the expired row first.

### F-08 · MAJOR · plan §6.9 (`CHAT_BUSY`) · `app/db/repositories/chat.py:73-84`

**What.** `mark_busy` reads, then writes, so two messages sent at the same moment both get through. Its 120 s "stale" window is also shorter than a turn can take (`GLM_TIMEOUT_S=120` plus streaming). Both turns call the model, then compute the same `seq`, and one dies on the `(session_id, seq)` constraint with a 500.

**Expected.**
- One atomic statement, `UPDATE chat_sessions SET busy_since = now() WHERE id = :id AND (busy_since IS NULL OR busy_since < now() - :stale) RETURNING id`, with the stale window longer than the maximum turn time.
- Compute `seq` in the same transaction as the insert.

### F-09 · MAJOR · security · `app/core/config.py:13`, `app/core/security.py:23`, `app/llm/glm.py:11`

**What.**
- `APP_ENV` defaults to `"local"`. Anywhere it isn't set:
  - a request without `X-User-Id` is served as the shared `local-dev-user`, so all such callers can read each other's sessions;
  - `/ai/dev/*` is mounted.
- A missing `ZAI_API_KEY` silently becomes `"dummy-key-for-test"`, so startup succeeds and every chat fails later with a misleading 502. Plan §9 asked for a clear failure at startup.

**Expected.**
- Default `APP_ENV` to a non-local value.
- Fail startup when `ZAI_API_KEY` is empty, except in tests.

### F-10 · MAJOR · plan §10 (`/ready`) · `app/api/health.py:33-36`, `app/messaging/broker.py:23-27`

**What.** Both branches set the broker to `"UP"`, and `start_broker()` swallows connection errors, so `/ready` is green with RabbitMQ down.

**Expected.**
- Report the real connection state.
- Log `broker.connect_failed` instead of `pass`.
- `/ready` returns 503 when the broker is down.

### F-11 · MAJOR · plan §9 (tests) · `tests/`

**What.** Several cases the plan requires are missing:
- **Privacy suite:** it is 20 *text strings*, not PDFs through extraction, with no Docling-style Markdown, no two-column or scanned input, and **no assertion that the person's name is gone**. `test_pii_failure_blocking` doesn't test blocking (its comments say so).
- **Integration tests:** there are no Postgres or RabbitMQ integration tests, although CI starts both services. CI runs only `tests/unit/`, on SQLite.
- **Streams:** no test for interrupted streams.

**Expected.**
- Plan §9 as written.
- At minimum: the F-01 inputs; a name-removal assertion on every CV; a real blocking test; one stub-responder request/reply test against the CI RabbitMQ; DB tests on the CI Postgres.

### F-12 · MAJOR · CI · `.github/workflows/ci.yml:87`

**What.** No `permissions:` block. On a repository with the default read-only token, `dorny/test-reporter` can't create its check run, so the job goes red even when tests pass. core's CI sets these permissions.

**Expected.** `permissions: { contents: read, checks: write, pull-requests: write }`, as in core, plus `continue-on-error: true` on the report step.

### F-13 · MINOR · settings that do nothing

`GLM_THINKING`, `GLM_TIMEOUT_S`, `CHAT_STREAM_HEARTBEAT_S` and `LOG_PAYLOADS` (plus `OCR_LANGS`, F-05) are in `.env` but never read. Wire them in:
- `ZaiModelSettings(thinking=…)`
- a request timeout
- an SSE comment line every N seconds
- payload logging only when true

### F-14 · MINOR · plan §6.9 · `pydantic_ai_helpers.py:162-228`

If the client disconnects mid-stream, nothing is saved. The plan says save the partial reply with status `interrupted`.

### F-15 · MINOR · `runner.py:98-101`, `pydantic_ai_helpers.py:178-181`

If stored history fails to parse, it is silently replaced by `[]`, so the model quietly forgets the conversation. Raise and log instead.

### F-16 · MINOR · `service.py:93`, `pydantic_ai_helpers.py:71`

Each upload is read fully into memory before the size check. Files are also extracted before the `sessionId` is checked, so a bad id still costs a full Docling run. Read at most `PDF_MAX_BYTES + 1`, and check the session first.

### F-17 · MINOR · `service.py:65-84`, `models.py:111`

Idempotency:
- It works only with a `sessionId` and only without streaming.
- It searches only the first 100 messages.
- `(session_id, client_message_id)` is a plain index, not unique as planned.

### F-18 · MINOR · plan §6.6 · `app/messaging/rpc.py:44-50`, `:39`

Requests go straight to the queue, not through the `occupify.agent.rpc` exchange (`RPC_EXCHANGE` is unused). `tool.call` logs the full `args` (plan: ids only).

### F-19 · MINOR · `pydantic_ai_helpers.py:144`, `runner.py:161,167`

Raw exception text is sent to the client (`INTERNAL_ERROR`) and stored in `agent_runs.error`. Send a fixed message; log the type and code.

### F-20 · MINOR · plan §5 · `app/main.py:32-35`

A failed `init_db()` is only logged, so the app runs without tables. Fail startup instead.

### NIT (not sent for fixing)

- Dockerfile `uv` image tag not pinned.
- The CI Docling cache step caches an empty path.
- `note.md` (your prompt notes) is committed.

## Fix order

1. **F-01, F-02** (privacy), with the F-11 privacy tests written first.
2. **F-03, F-04** (one chat path through the runner; real error types).
3. **F-05 to F-10.**
4. **F-12**, then the MINORs.
