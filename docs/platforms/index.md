---
layout: default
title: Agent setup
nav_order: 4
has_children: true
has_toc: false
description: Start with the coding tool you use, check that it understands the project, and add a review skill when you need one.
---

# Agent setup

Start with the coding tool you already use, or choose one from the table below. You only need one to work through the lessons. Run the [repository quickstart](../quickstart.md) first; knowing what a successful run looks like will help you notice when an agent uses the wrong environment or command.

**Documentation reviewed: September 5, 2026.** We checked the features described here against official documentation. Hands-on testing still depends on your client, operating system, account, and whether the work runs locally or remotely. Each page links to the provider's current installation and sign-in instructions.

These pages explain how clients work; inclusion here does not certify a service for university data. Use the approved account and connection for your task, and recheck permitted data use when switching models, clients, or hosted environments. The [lab data and policy page](../reference/lab-data-policy.md) explains that part of setup.

| Your starting point | Read next |
| --- | --- |
| Understand which configuration belongs where | [Portable context and skills](portable-context.md) |
| Codex in a terminal, editor, or desktop app | [Codex](codex.md) |
| Claude Code | [Claude Code](claude-code.md) |
| GitHub Copilot in VS Code or the CLI | [GitHub Copilot](copilot.md) |
| Cursor | [Cursor](cursor.md) |
| Gemini CLI | [Gemini CLI](gemini-cli.md) |
| Understand modes, tool use, and newer agent features | [Working with coding agents](trends.md) |

## Choose how you want to work

Think about what you need from the next exchange. The names below are common, but clients implement them differently:

| What you need | Mode or request to start with | In this guide |
| --- | --- | --- |
| Understand existing code | **Ask**, or ask for inspection and explanation without edits | Follow one measurement through the cleaning function. |
| Resolve the approach before implementation | **Plan**, or ask for a proposal based on the code | Decide where to calculate the fraction and record the QC decision. |
| Make and check an agreed change | **Agent**, or the client's ordinary coding session | Add the gate, run tests, and inspect the outputs. |

Model choice, workflow, and tool access are different things to check, even when a client combines their controls. Planning may use reading, search, and other exploration tools; some clients also allow a plan file to be written. Implementation needs editing and execution access. Asking for a plan does not itself confirm that the client switched modes: check its indicator. The pages below cover interactive use; scripts and unattended sessions can handle approvals differently. [VS Code roles](https://code.visualstudio.com/docs/agents/run/agent-harnesses), [Claude permission modes](https://code.claude.com/docs/en/permission-modes), [Gemini planning](https://geminicli.com/docs/cli/plan-mode/).

For a small, clear edit, a direct implementation request is enough. Use planning when you still have a question whose answer changes the work. The [agent workflow discussion](trends.md) develops these choices through the exercise.

## Check the agent's understanding

Before asking for a change, give the agent a chance to find its way around. Open this repository as the working project and send this prompt:

```text
Read AGENTS.md, README.md, and REPO_MAP.md.
Orient me without editing files or installing anything.
Report the instruction files you actually read, the Python setup and test
commands, the demo command, and the tracked-versus-generated boundaries.
Locate the pipeline entrypoint and its I/O contract.
List any required tools or context you cannot access.
```

Compare the answer with the files you just used in the quickstart. It should identify `python -m pytest`, `python -m pgacg demo`, `src/pgacg/cli.py`, and `docs/reference/io_contract.md`. Open the files it cites. If your client shows which instructions it loaded, check that display too: a convincing summary can still miss the project instructions.

## Let the first lesson guide your setup

[Lesson 1](../lessons/01-orient.md) asks you to prepare one model/client combination, check which instructions and skills it loaded, and compare it with another setup. Use these pages while doing that work. The ordinary coding session is enough to begin; you can try a named reviewer when there is a change to inspect.

When you want a pipeline review, try the included [pipeline-review skill](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/.agents/skills/pipeline-review/SKILL.md). Your client page shows how to find it and whether an adapter or copy is needed. A separate reviewer is another optional step: it is useful when you can give it a specific question, the changed files, and the evidence it needs without holding up the main task.

External tool connections can wait until you need something the agent cannot already do, such as retrieve a particular documentation source. Check what that connection can access; its permissions may differ from the terminal’s.

The [practices library](../practices/index.md) is useful reading for you and your agent. Those pages are ordinary documentation. The [portable-context page](portable-context.md) maps the configuration folders and shows how to check skill discovery. The [Codex setup](codex.md) explains the included `.codex/config.toml` and reviewer definition, along with the personal settings a colleague should keep on their own machine.

When you share a workshop result with a colleague, include the client and version, selected model, where it ran, any setup changes, and the commands and results. That gives them a starting point for reproducing your work. Keep credentials and private account settings out of Git.
