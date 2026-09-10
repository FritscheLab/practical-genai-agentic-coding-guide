---
layout: default
title: Cursor
parent: Agent setup
nav_order: 5
description: Start a lesson in Cursor with the shared project instructions, then add review tools if they help.
---

# Cursor

Cursor reads `AGENTS.md` directly. Open the example repository locally and complete your language setup before starting.

**Documentation reviewed: September 5, 2026.** If you need to install Cursor or set up an account, follow its [quickstart](https://cursor.com/docs/get-started/quickstart).

## First session

1. Open the example repository in Cursor and complete the [setup for your language path](../quickstart.md) in its terminal. This gives you a known working environment for the agent to use.
2. Open the Agent panel, choose **Ask** in its mode picker, and send the [orientation prompt](index.md#check-the-agents-understanding).
3. Check the instruction sources and compare the reported entrypoint and commands with the files you just used.

Use root `AGENTS.md` for shared guidance. For file-specific rules, use `.cursor/rules/*.mdc`; plain `.md` files there are ignored. Personal rules live in Cursor settings. [Cursor rules](https://cursor.com/docs/rules).

For specific rules, use Cursor's editor and check `description`, `globs`, and `alwaysApply`. Try files that should and should not trigger the rule.

## Ask, plan, or implement

Use the mode picker or **Shift+Tab**: **Ask** reads and explains; **Agent** searches, edits, and runs commands. Review edits as they appear; use **Stop** if the task drifts. [Ask mode](https://cursor.com/help/ai-features/ask-mode), [Agent behavior](https://cursor.com/help/ai-features/agent).

Choose **Plan** to discuss an approach, then **Build** to implement. **Save to workspace** keeps the plan in the project; otherwise plans start in your home directory. Small, clear changes can go straight to Agent. [Plan mode](https://cursor.com/docs/agent/plan-mode).

Check **Settings → Agents → Approvals & Execution** separately from the mode picker. **Auto-review** combines allowlists, available shell sandboxing, and model assessment; it can approve calls automatically and make mistakes. **Allowlist** sets explicit rules; an empty list replaces Ask Every Time. **Run Everything** removes those checks and sandboxing. Cloud execution differs. [Run Modes](https://cursor.com/docs/agent/security/run-modes).

## Choose a model in this client

Use the **model selector** in Chat or Agent. Account and team settings affect choices; switching models keeps Cursor's rules and controls. Record **Auto** if selected: routing can vary, and teams may hide the model identity. [Cursor model selection and availability](https://cursor.com/help/models-and-usage/available-models).

Included models need no separate API key. Your own key under **Cursor Settings → Models** supports documented chat models, with provider-specific limits; Tab still uses Cursor's models. Switching clients requires that client's setup. [Cursor API key support](https://cursor.com/help/models-and-usage/api-keys).

## Try the review skill

Ask Agent to use the included `.agents/skills/plot-review/` and check what loads. Cursor also supports `.cursor/skills/`; personal equivalents use `~/.agents/skills/` or `~/.cursor/skills/`. See the [folder map](portable-context.md). [Cursor skills](https://cursor.com/docs/skills).

For cloud or remote work, check skill availability: personal skills may need synchronization or packaging. A committed project skill identifies the shared version. [Cursor skill locations and remote availability](https://cursor.com/docs/skills).

## Create a reviewer agent

Save this role as `.cursor/agents/plot-reviewer.md`, or under `~/.cursor/agents/` for personal reuse. `readonly: true` restricts writes; `model: inherit` uses the main agent's model. [Cursor subagents](https://cursor.com/docs/subagents).

```markdown
---
name: plot-reviewer
description: Review plotting code and its rendered image against the contract.
model: inherit
readonly: true
---

Read AGENTS.md and use .agents/skills/plot-review/SKILL.md.
Review the requested diff, image, and alt text against the local figure
specifications. Use supplied test results; do not edit files.
Report findings with source locations and name any checks you could not perform.
```

Ask `Have plot-reviewer review my plotting changes.` Compare its findings with the source and tests. A single-file task may not need delegation; extra agents add coordination time. [Cursor subagent tradeoffs](https://cursor.com/docs/subagents).

## Check the interpreter and test results

Check the interpreter, actual test results, and every changed file. Record checks the reviewer could not perform. Keep the task fixed when comparing models.
