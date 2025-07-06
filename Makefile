# Makefile for Python quality automation

.DEFAULT_GOAL := help

# Source and test directories
SRC=src
TESTS=tests

# === Help ===

help:
	@echo "Available commands:"
	@echo "  make install     - Install development dependencies"
	@echo "  make lint        - Run Ruff linter"
	@echo "  make format      - Run Ruff formatter"
	@echo "  make mypy        - Run mypy type checker"
	@echo "  make test        - Run pytest"
	@echo "  make cc          - Cyclomatic complexity analysis (Radon)"
	@echo "  make mi          - Maintainability index report (Radon)"
	@echo "  make quality     - Run lint, mypy, and Radon metrics"
	@echo "  make check       - Run all checks: lint, format, mypy, test, metrics"

# === Linting and formatting ===

lint:
	uv run ruff check .

format:
	uv run ruff format .

# === Static typing ===

mypy:
	uv run mypy $(SRC)

# === Testing ===

test:
	uv run pytest

# === Code metrics ===

cc:
	uv run radon cc $(SRC) --total-average -a

mi:
	uv run radon mi $(SRC)

quality: lint mypy cc mi

# === Installation ===

install:
	uv pip install -e .[dev]

# === Full check ===

check: lint format mypy test cc mi

.PHONY: help lint format mypy test cc mi quality install check
