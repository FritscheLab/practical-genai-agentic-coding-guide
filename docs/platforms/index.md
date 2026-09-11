---
layout: default
title: Agent setup
nav_order: 4
has_children: true
has_toc: false
description: Start with VS Code and Copilot, then explore alternative clients and optional review tools.
---

# Agent setup

**Start with [VS Code + GitHub Copilot](../setup/vscode-copilot.md).** The detailed setup covers installation, account access, cloning, language environments, and the first plot. The main lessons use Copilot Chat, Explorer, and Source Control throughout.

Prefer Claude Code? Its [VS Code extension](claude-code.md#use-the-vs-code-extension) supports the same prompts and visual Git workflow. Other clients below are optional references. For a complete terminal workflow, use the [CLI appendix](../appendix/command-line.md).

| Client or task | Read next |
| --- | --- |
| VS Code + GitHub Copilot (default) | [Detailed setup](../setup/vscode-copilot.md) · [Controls and optional features](copilot.md) |
| Claude Code in VS Code (alternative) | [Extension setup](claude-code.md#use-the-vs-code-extension) |
| Codex (optional) | [Setup](codex.md) |
| Cursor | [Setup](cursor.md) |
| Gemini CLI | [Setup](gemini-cli.md) |
| Instructions, skills, and configuration folders | [Portable context](portable-context.md) |
| Modes and agent workflows | [Working with coding agents](trends.md) |
| One-line R formatting request | [Optional R refactoring skill](r-refactoring.md) |

**Platform references reviewed: September 5, 2026**, with later scoped dates on refreshed pages. Pages link to current installation/sign-in guidance; actual features depend on client, version, account, and local versus hosted execution. Inclusion here is not approval for university data. Check the [lab data guidance](../reference/lab-data-policy.md).

<a id="choose-how-you-want-to-work"></a>

## Use the lesson sequence

| Your next step | Copilot role in a Local session |
| --- | --- |
| Understand the code | **Ask**: explain the source and cite files |
| Specify the repair | **Plan**: propose changes and checks for review |
| Implement and verify | **Agent**: edit, run checks, and show their results |

Select the actual role before each lesson prompt; writing “make a plan” does not itself show which role is active. **Session target**, **role**, **model**, and **permissions** are separate controls. Keep the **Local** target for the main path so edits appear in the open workspace. Other clients use their own planning and permission controls. [VS Code session targets and roles](https://code.visualstudio.com/docs/agents/run/agent-harnesses)

## Check the agent's understanding

With the example repository open, select **Local → Ask** in Copilot Chat and paste:

```text
Read AGENTS.md and REPO_MAP.md. I'm using R. Where is the plotting function,
and how do I run and check it? Cite the files; don't edit or execute anything.
```

Replace `R` with `Python` if needed. Open the cited files and compare the proposed checks with your setup. Check the client's loaded-instructions display where available; a plausible answer is not proof that the instructions loaded.

## Let the first lesson guide your setup

Continue with [Python Lesson 1](../paths/python/01-orient.md) or [R Lesson 1](../paths/r/01-orient.md). Add the [review skill](portable-context.md#find-and-use-the-review-skill) when useful. Comparing clients, adding a reviewer agent, and connecting external tools are optional.

For a reproducible handoff, record the client/version, model, execution environment, and actual checks. Keep credentials and personal settings out of Git.
