.PHONY: help venv install test lint demo site preview slides

help:
	@echo "Targets:"
	@echo "  venv     - create venv in .venv"
	@echo "  install  - install dev dependencies"
	@echo "  test     - run pytest"
	@echo "  lint     - run ruff"
	@echo "  demo     - run demo pipeline on data/example"
	@echo "  site     - build the guide with Bundler"
	@echo "  preview  - serve the guide locally"
	@echo "  slides   - render the instructor slides with Quarto"

venv:
	python -m venv .venv

install:
	python -m pip install -r requirements-dev.txt

test:
	python -m pytest

lint:
	python -m ruff check .

demo:
	python -m pgacg demo --ehr data/example/ehr_bmi_simulated_data.tsv --demo data/example/demographics_simulated_data.tsv

site:
	bundle exec jekyll build
	python scripts/py/check_site.py _site

preview:
	bundle exec jekyll serve --host 127.0.0.1 --port 4000

slides:
	quarto render docs/lab_meeting/slide_deck.qmd
