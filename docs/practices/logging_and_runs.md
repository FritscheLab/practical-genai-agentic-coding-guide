---
layout: default
title: Record plot runs
parent: Repository practices
nav_order: 4
---

# Keep enough evidence to repeat the result

For this exercise, keep the baseline and edited plots in separate directories:

| File | Purpose |
| --- | --- |
| `runs/baseline/summary.png` | The original plot, including overlapping bars and clipped labels |
| `runs/with-fix/summary.png` | The plot rendered from your edited source |
| `runs/with-fix/summary.alt.txt` | The separately written and reviewed alternative text, no more than 150 words |

Use the commands in your [language path](../quickstart.md). Give each attempt a new output path. Keep generated plots under ignored `runs/` and source edits in Git.

## Record the commands and results

Record the source file, output paths, rendering command, behavior tests, figure checker, and actual outcomes. Add visual observations: separated bars, readable labels, and unchanged counts and order.

Include the alt-text path, contrast, group identification, and grayscale review. Write and review alt text separately; plotting commands create only the PNG.

Render and inspect again after the final source edit. If a check cannot run, record the environment problem and leave its result unverified.

## Share only reviewed evidence

Give the agent source, approved before/after images, and test results. This workshop uses invented totals. For a study, review code and images before sharing; keep study data and detailed logs in the approved analysis environment. See [lab data guidance](../reference/lab-data-policy.md).
