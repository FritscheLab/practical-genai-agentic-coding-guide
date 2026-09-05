# Practical GenAI Agentic Coding Guide

**Part 2: build, verify, and maintain a research repository with coding agents.**

A hands-on companion to the [Practical GenAI Coding Guide](https://fritschelab.org/practical-genai-coding-guide/), created by [Lars G. Fritsche](https://medschool.umich.edu/profile/4980/lars-fritsche) and the [Fritsche Lab](https://fritschelab.org/) at the University of Michigan.

In Part 1, we work through planning a coding task, giving an assistant useful context, and checking the result. Here we put those habits to work in a project a labmate could pick up and maintain. You will make one change to a Python pipeline, test it, review it, and leave a useful record of what happened.

## Start here

- **[Set up and run the baseline](docs/quickstart.md)** — install the package and inspect your first run.
- **[Work through the six lessons](docs/lessons/index.md)** — orient, specify, implement, verify, review, and hand off.
- **[Configure your coding agent](docs/platforms/index.md)** — current setup for Codex, Claude Code, GitHub Copilot, Cursor, and Gemini CLI.
- **[Teach the workshop](docs/lab_meeting/index.md)** — a 45-minute facilitated session and a tested instructor solution.

You should be comfortable running a Python script and using a terminal. We explain the Git steps as we go. R is optional for regenerating data. The baseline needs no model API or credentials. Use your institution-approved coding assistant for the agent exercise; [Start here](docs/quickstart.md) also describes a manual path.

Please keep the exercise synthetic, including anything shown in chat, logs, or screenshots. Before bringing these habits to a study, check your university's policies for the actual service and data you plan to use. Our [lab data guidance](docs/reference/lab-data-policy.md) covers U-M requirements, PHI and PII, and the small ways information can travel while coding.

## Run locally

From this repository's root, using Python 3.10–3.12:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest
python -m pgacg demo \
  --ehr data/example/ehr_bmi_simulated_data.tsv \
  --demo data/example/demographics_simulated_data.tsv
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. See [setup and troubleshooting](docs/quickstart.md) if your system uses `python3` or limits script activation.

Each run creates `runs/<run_id>/` with cleaned and flagged TSVs, a data dictionary, logs, a summary, and a manifest recording input and output checksums and the software environment. The inputs are synthetic, and the cleaning thresholds and category labels are teaching rules. See the data contract before adapting them to a study.

## Find your way around

| Path | Purpose |
| --- | --- |
| `docs/lessons/` | The participant learning sequence. |
| `docs/platforms/` | Client setup, folder conventions, modes, and a dated review of agentic coding practices. |
| `docs/reference/` | Data contract, provenance, and source references. |
| `docs/templates/`, `examples/` | Task briefs, handoffs, and workshop reference solution. |
| `.codex/`, `.agents/skills/` | Shared Codex settings, a reviewer definition, and the portable review skill. |
| `src/pgacg/`, `tests/` | Working pipeline and independently specified checks. |
| `scripts/r/`, `data/example/` | Synthetic simulator and reproducible example inputs. |
| `AGENTS.md`, `REPO_MAP.md` | Repository instructions and entrypoints for contributors and agents. |

## Build the guide

Use Ruby 3.3 and Bundler:

```bash
bundle install
bundle exec jekyll build
python scripts/py/check_site.py _site
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Preview at `http://127.0.0.1:4000/practical-genai-agentic-coding-guide/`. [Contributor setup](docs/contributing.md) covers the website, slides, checks, and release workflow. The site shares the lab's styling and Part 1's Just the Docs navigation.

## Contribute and cite

Open an issue or pull request with a reproducible problem, a clearer exercise, or a source-backed correction. Read [contribution guidance](docs/contributing.md) and [AGENTS.md](AGENTS.md). Use [CITATION.cff](CITATION.cff) for citation metadata; [release notes](CHANGELOG.md) describe the published teaching scope.

[GNU General Public License v3.0](LICENSE).
