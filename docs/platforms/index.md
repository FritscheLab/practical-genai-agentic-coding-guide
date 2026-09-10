---
layout: default
title: Agent setup
nav_order: 4
has_children: true
has_toc: false
description: Start with the coding tool you use, check that it understands the project, and add a review skill when you need one.
---

# Agent setup

**Use the coding client you already know.** One is enough. First run your [Python or R setup](../quickstart.md), then open the example repository in that client.

| Client or task | Read next |
| --- | --- |
| Codex | [Setup](codex.md) |
| Claude Code | [Setup](claude-code.md) |
| GitHub Copilot | [Setup](copilot.md) |
| Cursor | [Setup](cursor.md) |
| Gemini CLI | [Setup](gemini-cli.md) |
| Instructions, skills, and configuration folders | [Portable context](portable-context.md) |
| Modes and agent workflows | [Working with coding agents](trends.md) |
| One-line R formatting request | [Optional R refactoring skill](r-refactoring.md) |

**Documentation reviewed: September 5, 2026.** Pages link to current installation/sign-in guidance; actual features depend on client, version, account, and local versus hosted execution. Inclusion here is not approval for university data. Check the [lab data guidance](../reference/lab-data-policy.md).

## Choose how you want to work

| Your next step | Ask for |
| --- | --- |
| Understand the code | A short explanation, without edits |
| Resolve an uncertain approach | A plan |
| Make a clear change | Implementation and checks |

For this small repair, a direct request is enough. A **plan request**, **selected model**, and **tool permissions** are separate controls: inspect the client's indicators. Reading needs source access; repair needs editing and execution. Client pages cover the differences, including whether planning can write a plan file.

## Check the agent's understanding

With the example repository open, paste:

```text
Read AGENTS.md and REPO_MAP.md. I'm using R. Where is the plotting function,
and how do I run and check it? Cite the files; don't edit or execute anything.
```

Replace `R` with `Python` if needed. Open the cited files and compare the commands with your setup. Check the client's loaded-instructions display where available; a plausible answer is not proof that the instructions loaded.

## Let the first lesson guide your setup

Continue with [Python Lesson 1](../paths/python/01-orient.md) or [R Lesson 1](../paths/r/01-orient.md). Add the [review skill](portable-context.md#find-and-use-the-review-skill) when useful. Comparing clients, adding a reviewer agent, and connecting external tools are optional.

For a reproducible handoff, record the client/version, model, execution environment, and actual checks. Keep credentials and personal settings out of Git.
