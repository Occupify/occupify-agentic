COMPOSE ?= podman compose

.PHONY: install fmt lint test test-all infra up down reset-db logs run

install:
	uv sync

fmt:
	uv run ruff format .
	uv run ruff check --fix .

lint:
	uv run ruff format --check .
	uv run ruff check .

test:
	uv run pytest tests/unit/

test-all:
	uv run pytest --cov=app tests/

infra:
	$(COMPOSE) up -d postgres-agentic

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

reset-db:
	$(COMPOSE) down -v
	$(COMPOSE) up -d postgres-agentic

logs:
	$(COMPOSE) logs -f agentic

run:
	uv run uvicorn app.main:app --host 0.0.0.0 --port 8186 --reload
