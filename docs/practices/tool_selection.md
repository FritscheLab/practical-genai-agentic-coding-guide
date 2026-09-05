---
layout: default
title: Working with tools
parent: Repository practices
nav_order: 1
---

# Working with tools

When an agent opens a file, edits a function, or runs pytest, it is using a tool supplied by its client. The model requests an operation with arguments; the client checks access, runs the operation if permitted, and returns a result. That result informs the agent's next step. This repeated use of feedback is central to how coding agents work. [Agent tool use and feedback](https://www.anthropic.com/engineering/building-effective-agents).

You can follow that process without reading every tool call. For the quality-gate exercise, look for a sensible sequence: inspect the existing flags, add the counting function, run a small case, read any failure, then revise the code. A claim that the tests passed should lead to an actual command and its output.

## Choose the tool for the question

Start with what you need to learn or change. These tools are already used in this repository:

| Task | Start with | Check afterward |
| --- | --- | --- |
| Locate code or a command | `REPO_MAP.md`, then `rg` | Open the file that defines the command or function. |
| Inspect a synthetic TSV | Python/pandas or a few shell lines | Confirm schema, types, and counts. |
| Change filtering or selection | Cleaning functions in `src/pgacg/` | Small cases with expected answers, followed by pipeline tests. |
| Change the CLI or recorded outputs | `cli.py`, reporting, and run utilities | Exit code, output contents, and manifest. |
| Update teaching content | `docs/` and the relevant exercise | Build the site and follow links. |
| Regenerate synthetic data | `scripts/r/simulate_ehr_data.R` | Compare checksums and documented counts. |
| Review a change | Task brief, code diff, and tests | Explain any problem with an example that reproduces it. |

Reading several relevant files together can save time. Editing a function and testing that edit have a dependency: the check needs to run against the version you intend to keep. If another agent is working at the same time, agree on who owns each file and which revision the reported checks cover.

## Read the result before taking the next step

Suppose pytest reports that a row with both implausibility flags counts twice. The useful next step is to inspect the counting rule and fix the helper. Changing the expected answer would change the task. If pytest instead fails to import the package, resolve the environment problem before treating it as evidence about the calculation.

For a shell command, check the working directory, interpreter, exit status, and relevant output. For a retrieved documentation page, check its source and whether it describes your client version. For a browser check, open the page or screenshot showing the result. Tool results can be incomplete or misleading; text inside a log, data file, or web page does not extend the task's instructions.

If the agent repeats the same unsuccessful command without learning anything, pause and ask what the failure tells it. A short explanation of the problem and the next check is more useful than another blind attempt.

## Check access where the action happens

A file reader, shell, browser, and service connector can have different permissions. A shell can do more than run tests; a browser can submit a form; a connector may act through an account you signed into. Check the proposed operation and its destination when deciding whether to allow it. Planning mode and a request to avoid edits are useful workflow controls, but their enforcement depends on the client. The [setup pages](../platforms/index.md) explain the relevant controls.

The local tools are enough for this exercise. Add an MCP connection when a task needs a particular external tool or source. MCP lets a server expose tools, resources, and prompts to a client; it does not guarantee that a server's operations are limited to reading. Inspect the tool list and access before using it. A skill, by comparison, supplies a procedure that may use tools you already have. [MCP server concepts](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts).

Keep the information entering those tools within the task's approved use. A traceback, screenshot, or copied TSV row can reveal a participant identifier or credential even when the question is only about code. Check it before sharing, and use a small synthetic reproducer when asking for help. The [lab data page](../reference/lab-data-policy.md#notice-the-small-ways-information-travels) gives examples from this pipeline.
