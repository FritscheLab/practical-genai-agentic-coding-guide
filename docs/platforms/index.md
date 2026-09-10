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

**Documentation reviewed: September 5, 2026.** Feature descriptions link to official documentation. Hands-on testing still depends on your client, operating system, account, and whether the work runs locally or remotely. Each page links to the provider's current installation and sign-in instructions.

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
| Resolve the approach before implementation | **Plan**, or ask for a proposal based on the code | Decide how to count excluded measurements and their existing reasons. |
| Make and check an agreed change | **Agent**, or the client's ordinary coding session | Add the exclusion report, run tests, and inspect the outputs. |

Model choice, workflow, and tool access are different things to check, even when a client combines their controls. Planning may use reading, search, and other exploration tools; some clients also allow a plan file to be written. Implementation needs editing and execution access. Asking for a plan does not itself confirm that the client switched modes: check its indicator. The pages below cover interactive use; scripts and unattended sessions can handle approvals differently. [VS Code roles](https://code.visualstudio.com/docs/agents/run/agent-harnesses), [Claude permission modes](https://code.claude.com/docs/en/permission-modes), [Gemini planning](https://geminicli.com/docs/cli/plan-mode/).

For a small, clear edit, a direct implementation request is enough. Use planning when you still have a question whose answer changes the work. The [agent workflow discussion](trends.md) develops these choices through the exercise.

## Check the agent's understanding

If you arrived from [Python Lesson 1](../paths/python/01-orient.md) or [R Lesson 1](../paths/r/01-orient.md), use that lesson's explanation prompt once your client can read the repository, edit files, and run commands. The prompt below is an optional alternative for a broader setup check.

Open your local [example repository](https://github.com/ilarsf/practical-genai-agentic-coding-example) as the working project and replace the language placeholder:

```text
Read AGENTS.md, README.md, and REPO_MAP.md.
Orient me without editing files or installing anything.
I am following the [Python or R] path.
Report the instruction files you actually read, that path's setup and test
commands, the demo command, and the tracked-versus-generated boundaries.
Locate the pipeline entrypoint and its I/O contract.
List any required tools or context you cannot access.
```

Compare the answer with the files you just used in the quickstart. For Python, it should identify `python -m pytest`, `python -m pgacg demo`, and `src/pgacg/cli.py`; for R, `Rscript tests/r/run_tests.R`, `Rscript scripts/r/demo.R`, and `R/cli.R`. Both should find `docs/reference/io_contract.md`. Open the files it cites. If your client shows which instructions it loaded, check that display too: a convincing summary can still miss the project instructions.

## Let the first lesson guide your setup

Return to [Python Lesson 1](../paths/python/01-orient.md) or [R Lesson 1](../paths/r/01-orient.md) to ask where the existing exclusion reasons and summary are written, then compare the explanation with the flagged file. One working client is enough for the exercise. Comparing clients and trying a named reviewer are optional follow-ups.

When you want a pipeline review, try the included [pipeline-review skill](https://github.com/ilarsf/practical-genai-agentic-coding-example/blob/main/.agents/skills/pipeline-review/SKILL.md). Your client page shows how to find it and whether an adapter or copy is needed. A separate reviewer is another optional step: it is useful when you can give it a specific question, the changed files, and the evidence it needs without holding up the main task.

External tool connections can wait until you need something the agent cannot already do, such as retrieve a particular documentation source. Check what that connection can access; its permissions may differ from the terminal’s.

The [practices library](../practices/index.md) is useful reading for you and your agent. Those pages are ordinary documentation. The [portable-context page](portable-context.md) maps the configuration folders and shows how to check skill discovery. The [Codex setup](codex.md) explains the included `.codex/config.toml` and reviewer definition, along with the personal settings a colleague should keep on their own machine.

When you share a workshop result with a colleague, include the client and version, selected model, where it ran, any setup changes, and the commands and results. That gives them a starting point for reproducing your work. Keep credentials and private account settings out of Git.
