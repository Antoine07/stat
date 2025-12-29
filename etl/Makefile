PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PY  := $(VENV)/bin/python

.PHONY: setup lint test run

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -U pip
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi

lint:
	@$(PY) -m ruff format .
	@$(PY) -m ruff check .

test:
	@$(PY) -m pytest

# Usage: make run INPUT=data/input.json
run:
	@$(PY) -m src.pipelines.stats_pipeline --input $(or $(INPUT),data/input.json)
