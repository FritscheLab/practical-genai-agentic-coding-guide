---
layout: default
title: Working with tools
parent: Repository practices
nav_order: 1
---

# Working with tools

An agent uses client tools to read files, edit functions, and run tests. The client checks access and returns results that inform the next step. [Agent tool use and feedback](https://www.anthropic.com/engineering/building-effective-agents).

For this exercise: trace the source, inspect the invented chart, edit the layout, and check the result. Ask the agent to explain edits and report test outcomes.

## Choose the tool for the question

| Task | Start with | Check afterward |
| --- | --- | --- |
| Locate the plotting function | `REPO_MAP.md`, then `rg` | Open `plot_summary` in your language's source file. |
| Understand the fixed values | Source constants and the plotting contract | Check assertions for categories, groups, counts, and order. |
| Diagnose overlap and clipping | The baseline PNG, plotting code, and figure specifications | Locate bar positions, margins, size, and label settings. |
| Change the layout | `plotting/plot_summary.py` or `plotting/plot_summary.R` | Render a new PNG and run that language's tests. |
| Review the change | Task brief, source diff, tests, and before/after images | Check the figure specifications and unchanged values. |
| Review accessibility | Saved image, figure specifications, and `summary.alt.txt` | Check contrast, grayscale readability, group labels, and a useful text alternative. |

Read related source files together. Test the version you intend to keep. With multiple agents, agree on file ownership and which version the checks cover.

## Read the result before taking the next step

If a fixed count changes, inspect the assertion and function; keep the expected value. An import failure calls for an environment fix before a layout review.

Check each command's directory, interpreter, exit status, and result. Open the image rendered from the current source. If the client cannot view it, have a person perform the visual check.

Retry a failed command after addressing its cause.

## Check access where the action happens

A file reader, shell, browser, and connector can have different permissions. Client controls enforce access; planning instructions guide behavior. See the [setup pages](../platforms/index.md).

Local tools cover this exercise. Add external connections only for a task that needs them, and inspect their access. [MCP server concepts](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts).

Keep study data, exports, and logs outside this workspace. Review study code and images before sharing with an agent; aggregate plots also need a sharing review. See [lab data guidance](../reference/lab-data-policy.md).
