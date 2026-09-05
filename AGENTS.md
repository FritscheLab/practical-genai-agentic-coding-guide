# AGENTS.md

This is Part 2 of the Fritsche Lab Practical GenAI series: a public teaching guide and a runnable synthetic-data pipeline. The primary outcome is a clear, accurate learning experience backed by executable examples.

This file holds shared project instructions. Client configuration controls tools and access; it does not replace this briefing.

## Read first

1. `README.md`
2. `REPO_MAP.md`
3. `docs/lab_meeting/45min_runbook.md`
4. `docs/practices/tool_selection.md`

Inspect relevant files before editing. Use `rg` for navigation and search. Keep changes coherent and reviewable; preserve unrelated work.

## Code and data

- Use only synthetic fixtures in this teaching repository. Never add real patient or participant records, PHI, PII, or credentials to its files or agent context.
- Tracked source: `src/`, `scripts/`, `tests/`, `docs/`, `examples/`, `data/example/`, and site/configuration files.
- Generated and ignored: `runs/`, `tmp/`, `data/raw/`, `data/derived/`, `.venv/`, `_site/`, and dependency/build caches.
- `.gitignore` is not an access boundary. Follow the actual workspace and tool permissions.
- Keep transformations small and testable, use type hints and `pathlib.Path`, and keep I/O in CLI/reporting layers.
- The pipeline's simplified rules are teaching specifications, not validated clinical recommendations.
- Follow university data, privacy, secure-coding, and research requirements. `docs/reference/lab-data-policy.md` links to current U-M guidance; other labs must use their own institutional rules. A model name, subscription, or client permission does not establish approval for sensitive data.
- Treat outputs, logs, manifests, screenshots, and tool results as possible disclosure routes. This pipeline does not de-identify inputs or redact saved paths and errors. Keep study records in their approved environment and use a synthetic reproducer here.

## Implement and verify

State a short plan for substantial work. Locate the entrypoint, implement the agreed behavior, then inspect the diff and run relevant checks:

```bash
python -m pytest
python -m ruff check .
python -m pgacg demo --ehr data/example/ehr_bmi_simulated_data.tsv --demo data/example/demographics_simulated_data.tsv
```

Run `python examples/qc_gate/verify_solution.py` after changing the baseline or exercise. The QC gate is intentionally absent from the baseline package; do not implement the learner's task there unless that is the requested work.

For site/content changes:

```bash
bundle exec jekyll build --strict_front_matter
python scripts/py/check_site.py _site
```

Run `quarto render docs/lab_meeting/slide_deck.qmd` after changing slides when Quarto is available. Do not track rendered slides or site output.

## Documentation and platform guidance

- Keep `README.md` GitHub-facing and `index.md` site-facing.
- Preserve the lab theme and clear Part 1/Part 2 navigation.
- Give rendered pages Jekyll front matter with the correct parent and order.
- Keep copyable prompts in fenced blocks.
- Put portable repository rules here. `CLAUDE.md`, `GEMINI.md`, and Copilot instructions refer here; they should not fork the rules.
- Verify current provider claims against official sources. Cite the supporting page and update the review date; do not invent settings, paths, or feature parity.
- Update `REPO_MAP.md` when entrypoints move, and the contract, dictionary, and tests when output meaning changes.

## Agent configuration and skills

- Shared Codex settings are in `.codex/config.toml`; the named reviewer is `.codex/agents/pipeline-reviewer.toml`. Keep model choice, provider credentials, and machine-specific paths in personal settings. See `docs/platforms/codex.md` for setup and configuration precedence.
- The review procedure lives in `.agents/skills/pipeline-review/SKILL.md`. Use it for pipeline reviews; ordinary prose edits do not need it. `docs/practices/` contains reference prose rather than installed skills.
- `docs/platforms/portable-context.md` maps instruction, settings, agent, and skill locations across clients. Keep one maintained procedure; Claude Code users can copy it to their documented skill location as described there.
- Inspect the effective mode and tool permissions. A planning request does not prove the client entered a restricted mode, and an instruction file cannot grant access.
- For parallel work, give each agent a distinct task and clear file ownership. Integrate its findings and check the final files; agreement alone is not evidence that a method is correct.
- Share only the deliberate configuration files. Keep credentials, session history, caches, personal overrides, and generated plans out of commits. Do not copy a personal `.codex` directory into this repository.

## Decisions and completion

Proceed with routine choices and changes already authorized by the task. Ask about unresolved changes to scientific methods, public schemas, CLI semantics, dependencies, or access when the task does not settle them. Do not publish, deploy, or modify external services without authorization.

Report what changed, commands actually run, their outcomes, and remaining limitations. Never treat a generated test or another agent's agreement as proof of scientific correctness.
