PYTHON = python
PIP = pip
MANAGE = $(PYTHON) manage.py
POETRY = poetry

.PHONY: help
help:
	@echo "Usage:"
	@echo "  make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  install-deps    Install all dependencies using Poetry"
	@echo "  run             Run the Django development server"
	@echo "  migrate         Apply migrations"
	@echo "  makemigrations  Create new migrations"
	@echo "  lint            Run ruff"
	@echo "  clean           Remove  __pycache__"

.PHONY: install-deps
install-deps:
	$(POETRY) install

.PHONY: run
run: migrate
	$(MANAGE) runserver

.PHONY: migrate
migrate:
	$(MANAGE) migrate

.PHONY: makemigrations
makemigrations:
	$(MANAGE) makemigrations

.PHONY: lint
lint:
	$(POETRY) run ruff check --fix

.PHONY: clean
clean:
	find . -name "__pycache__" -exec rm -rf {} +
