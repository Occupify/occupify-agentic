COMPOSE ?= podman compose
CV_COMPILER_PORT ?= 8190

.PHONY: install fmt lint test test-all test-integration skills-check skills-catalog network infra up down reset-db logs run migrate-jobs migrate-jobs-container

install:
	uv sync

fmt:
	uv run ruff format .
	uv run ruff check --fix .

lint:
	uv run ruff format --check .
	uv run ruff check .

skills-check:
	uv run python -m app.agents.skill_registry --check

skills-catalog:
	uv run python -m app.agents.skill_registry --write-catalog

test:
	uv run pytest tests/unit/

test-integration:
	TEST_PG_URL="postgresql+asyncpg://postgres:postgres@localhost:5535/occupify_agentic" uv run pytest -m integration tests/integration/

test-all:
	uv run pytest --cov=app tests/

network:
	$(firstword $(COMPOSE)) network inspect occupify-network >/dev/null 2>&1 || $(firstword $(COMPOSE)) network create occupify-network

infra: network
	$(COMPOSE) up -d --build postgres-agentic cv-compiler

up: network
	$(COMPOSE) up -d --build --force-recreate

down:
	$(COMPOSE) down

reset-db:
	$(COMPOSE) down -v
	$(COMPOSE) up -d postgres-agentic

logs:
	$(COMPOSE) logs -f agentic

run:
	DATABASE_URL="postgresql+asyncpg://postgres:postgres@localhost:5535/occupify_agentic" RABBITMQ_URL="amqp://guest:guest@localhost:5672/" CV_COMPILER_URL="http://127.0.0.1:$(CV_COMPILER_PORT)" uv run uvicorn app.main:app --host 0.0.0.0 --port 8186 --reload

migrate-jobs:
	DATABASE_URL="postgresql+asyncpg://postgres:postgres@localhost:5535/occupify_agentic" uv run python -m app.features.job_match.index.migrate

migrate-jobs-container:
	$(COMPOSE) exec agentic uv run python -m app.features.job_match.index.migrate
