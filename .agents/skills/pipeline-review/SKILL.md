---
name: pipeline-review
description: Review changes to this synthetic BMI pipeline against its documented data contract and independent test cases. Use for a requested pipeline review, not general prose edits or unrelated repositories.
---

Resolve all repository-relative paths below from the project root containing `AGENTS.md`.

Read the applicable repository instructions, `docs/reference/io_contract.md`, the requested diff, and the relevant tests. The method is a teaching specification; do not invent a clinical interpretation or replace the agreed thresholds.

Trace changed behavior from inputs to selected encounters, flags, run status, and recorded artifacts. Useful failure cases include repeated demographics keys, tied measurements, missing values, equality at thresholds, and a run that fails after initialization. Use only the cases relevant to the requested change.

For the workshop QC gate, read `docs/lessons/02-specify.md` and compare the implementation with its hand-worked cases. A row with both implausibility reasons counts once. Preserve the distinction between a completed QC failure and a runtime error.

When execution is available and within scope, run focused tests. For an implemented workshop gate, also run `python examples/qc_gate/check_acceptance.py`; the baseline intentionally lacks this feature. Do not modify that checker or the instructor solution to make a review pass. If tools are restricted to reading, inspect the checks and explicitly state that they were not executed. Never claim agreement with another agent establishes scientific validity.

Return concrete findings with a file location, a small synthetic reproducing case, expected behavior, actual behavior, and impact. Separate observed defects from uncertainties and optional improvements. Do not edit files as part of a review unless the user requests fixes.
