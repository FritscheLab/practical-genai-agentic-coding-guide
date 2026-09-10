---
layout: default
title: Test the method
parent: Repository practices
nav_order: 3
---

# Test the method

Use three checks: behavior tests protect the [invented values](../lessons/02-specify.md), the figure checker tests journal requirements, and visual review checks readability. None replaces the others.

## Run the checks for your language

After setup, run these commands from the example repository root. Python:

```bash
python -m unittest discover -s plotting/tests
```

R:

```bash
Rscript plotting/tests/run_tests.R
```

Ask the agent about functions and assertions, using test pass/fail results. Keep study files and unrelated logs out of the conversation.

## Check the figure specifications

The fictional **Journal of Unnecessarily Specific Figures (JUSF)** demands purple, lime, typewriter text, and precise dimensions. Read its [figure specifications](../reference/figure-specifications.md) for the complete rules.

Run the strict checker for your language against the edited source. Python:

```bash
python plotting/check_figure.py --output runs/with-fix/summary.png
```

R:

```bash
Rscript plotting/check_figure.R --output runs/with-fix/summary.png
```

The starter passes behavior tests and fails the figure checker: its layout and formatting are unfinished. After repair, both should pass. An environment error is a separate problem.

## Compare the image with the task

Compare the baseline and edited PNGs against the figure specifications. Check separated bars, complete labels, colors, legend, axes, title, and all eight counts. The [plotting contract](../reference/io_contract.md) protects category names, group assignments, values, and order.

## Include accessibility in the review

Inspect the figure at its intended size and in grayscale. Check contrast, black bar outlines, and group names and positions that work without color. The checker cannot establish that every reader can use the result.

Write `runs/with-fix/summary.alt.txt`, or ask the agent for a draft and review it. In no more than 150 words, describe the purpose, groups, all eight counts, and main comparison; identify the totals as invented. This is a separate deliverable: rendering creates only the PNG. Follow the figure specification's full accessibility requirements.

## Choose useful assertions

A PNG-exists test misses changed values. Protect category/group/count combinations and order too. An image hash cannot measure readability; fonts and graphics devices can change image bytes.

Keep the original expectations. Investigate failures in the assertion and function. Report test results, visual observations, and untested work separately.
