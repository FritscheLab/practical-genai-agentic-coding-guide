# Repository map

## Learning and publication

| Entrypoint | Purpose |
| --- | --- |
| `README.md`, `index.md` | GitHub introduction and public website landing page. |
| `docs/quickstart.md` | Installation and baseline run. |
| `docs/lessons/index.md` | Six lessons from orientation through handoff. |
| `docs/platforms/index.md` | Client setup, planning and agent modes, skills, delegation, and current sources. |
| `docs/reference/io_contract.md` | Exact baseline behavior and artifacts. |
| `docs/reference/synthetic-data.md` | Fixture regeneration and provenance. |
| `docs/reference/lab-data-policy.md` | U-M policies, PHI/PII boundaries, practical data risks, and study adaptation. |
| `docs/lab_meeting/45min_runbook.md` | Facilitator agenda. |
| `docs/contributing.md` | Contributor setup, checks, and publication workflow. |
| `_config.yml`, `_includes/`, `_sass/custom/`, `assets/` | Jekyll navigation and lab styling. |

## Pipeline

| File | Responsibility |
| --- | --- |
| `src/pgacg/__main__.py`, `cli.py` | `python -m pgacg demo`, argument handling, run lifecycle. |
| `src/pgacg/io.py` | TSV reading and schema validation. |
| `src/pgacg/cleaning.py` | Filtering, representative selection, categories, and metrics. |
| `src/pgacg/reporting.py`, `run_utils.py` | Summary, dictionary, logging, and provenance. |
| `tests/` | Independent synthetic unit cases and complete CLI checks. |
| `scripts/r/simulate_ehr_data.R` | Optional seeded synthetic input generation. |

## Workshop and skills

- `examples/qc_gate/check_acceptance.py`: checks a learner's completed QC gate.
- `examples/qc_gate/verify_solution.py`: checks the instructor solution in isolation.
- `examples/qc_gate/solution/`: reference implementation, outside the baseline package.
- `.agents/skills/pipeline-review/SKILL.md`: shared review skill in its discovery path.
- `.codex/config.toml`: shared local Codex settings; personal and managed overrides still apply.
- `.codex/agents/pipeline-reviewer.toml`: named Codex reviewer with restricted writes.
- `docs/templates/`: task brief, data contract, and handoff.

## Commands from the repo root

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
python -m ruff check .
python -m pgacg demo --ehr data/example/ehr_bmi_simulated_data.tsv --demo data/example/demographics_simulated_data.tsv
python examples/qc_gate/verify_solution.py
bundle exec jekyll build --strict_front_matter
python scripts/py/check_site.py _site
```

`runs/`, `tmp/`, `.venv/`, `_site/`, `data/raw/`, and `data/derived/` are generated. See `AGENTS.md` for rules and `docs/contributing.md` for environment setup.
