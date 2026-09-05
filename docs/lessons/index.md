---
layout: default
title: Lessons
nav_order: 3
has_children: true
has_toc: false
---

# Work through one change from start to finish

Suppose a collaborator runs the pipeline and finds that many measurements were implausible. The output files are useful for investigating, but the command still reports success. In these lessons, you will add a *quality gate*: a check that marks the run as failing quality control when too many input rows have implausible height or weight.

Work on one branch through all six lessons. Allow about two hours after the [Python setup](../quickstart.md), with extra time if you want to compare several model/client combinations. The [45-minute workshop](../lab_meeting/45min_runbook.md) provides a guided introduction with setup prepared beforehand.

| Lesson | What you will work out |
| --- | --- |
| [1. Orient](01-orient.md) | How to configure your model and client, compare setups, and find the pipeline's code and baseline results. |
| [2. Specify](02-specify.md) | Exactly what should count toward the gate, with examples you can check by hand. |
| [3. Implement](03-implement.md) | How to give an agent enough direction to make the change. |
| [4. Verify](04-verify.md) | Whether the new behavior works and the existing behavior still holds. |
| [5. Review](05-review.md) | Which parts of the change need a closer look before you keep them. |
| [6. Hand off](06-handoff.md) | What to leave for a collaborator, or for yourself when you return to the project. |

The starting code works, and its ordinary tests should pass. The quality gate is intentionally absent from `src/pgacg/`, leaving you a real change to make. A separate checker will test your finished exercise, and an [instructor solution](../lab_meeting/instructor-solution.md) is available to compare afterward.

We will keep returning to one habit from Part 1: decide what the result should be, then check what the code actually does.
