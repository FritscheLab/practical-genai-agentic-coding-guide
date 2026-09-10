---
layout: default
title: Demo prompts
parent: Teaching
nav_order: 2
---

# Prompts for the workshop

Use your language path's prompts; they already name the right source files and checks.

| Stage | Python prompt | R prompt |
| --- | --- | --- |
| Orient | [Python Lesson 1](../paths/python/01-orient.md) | [R Lesson 1](../paths/r/01-orient.md) |
| Describe the change | [Python Lesson 2](../paths/python/02-specify.md) | [R Lesson 2](../paths/r/02-specify.md) |
| Implement | [Python Lesson 3](../paths/python/03-implement.md) | [R Lesson 3](../paths/r/03-implement.md) |
| Verify | [Python Lesson 4](../paths/python/04-verify.md) | [R Lesson 4](../paths/r/04-verify.md) |
| Review | [Python Lesson 5](../paths/python/05-review.md) | [R Lesson 5](../paths/r/05-review.md) |
| Hand off | [Python Lesson 6](../paths/python/06-handoff.md) | [R Lesson 6](../paths/r/06-handoff.md) |

Open the baseline and [figure specifications](../reference/figure-specifications.md). Plan only while the approach is unclear, then implement.

Short prompts work because `AGENTS.md`, the skill, and the specification carry the reusable instructions. Point to those files instead of repeating their contents.

If alt text is still missing, ask:

```text
Write runs/with-fix/summary.alt.txt following the journal specification.
Check it against the image and report any accessibility checks you cannot do.
```

Review the draft yourself. Alt text is a separate deliverable; rendering creates only the PNG.

For the handoff:

```text
Write a short handoff with the changes, actual checks and results,
image and alt-text paths, and anything unfinished or untested.
```
