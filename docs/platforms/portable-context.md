---
layout: default
title: Portable context and skills
parent: Agent setup
nav_order: 1
description: Keep the project instructions useful across coding tools, and check where each tool expects to find them.
---

# Portable context and skills

Keep the task and project conventions together; adapt where each client looks for them. You can share useful instructions without copying your personal setup.

**Documentation reviewed: September 5, 2026.**

## Model, provider, client, and mode

The **model** generates responses. The **provider** serves it and manages account controls. The **client**—Codex, Cursor, or another tool—gathers context, offers tools, and manages permissions.

Changing a model leaves the client's instruction format in place. A local terminal client can still send requests to a remote model.

Record all three when comparing runs, plus whether the workspace was local or hosted. See the [client setup pages](index.md) for installation and access.

The **mode** selects a workflow such as explaining, planning, or editing. Check permissions separately: the mode name alone does not tell you what can run. See [choosing a mode](index.md#choose-how-you-want-to-work).

## Start with the briefing and the task

Start with repository instructions and a task brief. Add the other pieces when you have a reason to use them.

| Piece | What it helps you do | A useful check |
| --- | --- | --- |
| Repository instructions | Share commands, file boundaries, and conventions through `AGENTS.md` | Did the client load that file or its adapter? |
| Task brief | Agree on one change, the files it may affect, and examples of correct behavior | Could a colleague explain the expected answers before reading the code? |
| Skill | Reuse a review or maintenance procedure and any supporting resources | Did the client find and read the right procedure for this task? |
| Custom agent | Define a named role with its own instructions and tool settings | Does the role have the tools and instructions you intended? |
| Subagent | Give part of the work to a separate running agent, often in its own conversation | Did the main agent read and use the returned evidence? |
| MCP connection | Reach tools or context supplied by an external server | Which server, operations, credentials, and data can it access? |
| Hook | Run a procedure when a client event occurs, such as before a tool call | When does it run, and what happens if it fails? |

Some of these pieces can travel between tools. The Agent Skills specification defines a reusable folder format, and MCP defines a connection protocol. You still need to check how your client discovers instructions and handles permissions. Hook events and agent configuration also depend on the client. [Agent Skills specification](https://agentskills.io/specification), [MCP introduction](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro), [Copilot customization reference](https://docs.github.com/en/copilot/reference/customization-cheat-sheet), [Claude hooks reference](https://code.claude.com/docs/en/hooks).

## Know which folder you are changing

Keep the shared briefing in `AGENTS.md`. The included Claude, Gemini, and Copilot instruction files point there; Codex and Cursor read it directly. Put client settings in its configuration file and reusable procedures in skills.

The [example](https://github.com/FritscheLab/practical-genai-agentic-coding-example) includes [Codex settings and roles](codex.md), plus a shared `plot-review` skill. Add other client folders from this map only when needed:

| Client | Project settings and named roles |
| --- | --- |
| [Codex](codex.md) | Settings: `.codex/config.toml`. Roles: `.codex/agents/*.toml`. [Settings reference](https://learn.chatgpt.com/docs/config-file/config-basic), [agent reference](https://learn.chatgpt.com/docs/agent-configuration/subagents). |
| [Claude Code](claude-code.md) | Settings: `.claude/settings.json`. Roles: `.claude/agents/*.md`. [Settings reference](https://code.claude.com/docs/en/settings), [agent reference](https://code.claude.com/docs/en/sub-agents). |
| [Copilot](copilot.md) | CLI settings: `.github/copilot/settings.json`. Roles: `.github/agents/*.md`. VS Code uses its own Settings editor. [CLI settings](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference), [agent reference](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents), [VS Code settings](https://code.visualstudio.com/docs/configure/settings). |
| [Cursor](cursor.md) | Execution settings: `.cursor/permissions.json` and `.cursor/sandbox.json`. Roles: `.cursor/agents/*.md`. [Execution settings](https://cursor.com/docs/agent/security/run-modes), [agent reference](https://cursor.com/docs/subagents). |
| [Gemini CLI](gemini-cli.md) | Settings: `.gemini/settings.json`. Roles: `.gemini/agents/*.md`. [Settings reference](https://geminicli.com/docs/reference/configuration/), [agent reference](https://geminicli.com/docs/core/subagents/). |

A leading `~` means your home directory: `~/.codex/config.toml` is personal; `.codex/config.toml` belongs to the project and loads after you trust it. Keep credentials and machine preferences personal. Check effective settings before sharing; session and organization rules also apply. [Codex configuration layers](https://learn.chatgpt.com/docs/config-file/config-basic).

## Find and use the review skill

A skill is a folder containing `SKILL.md`: YAML `name` and `description` fields, followed by the procedure. The description guides selection. Supporting scripts and references stay in that folder. [Agent Skills specification](https://agentskills.io/specification).

The included [plot-review skill](https://github.com/FritscheLab/practical-genai-agentic-coding-example/blob/main/.agents/skills/plot-review/SKILL.md) is ready for Codex, Copilot, Cursor, and Gemini CLI at `.agents/skills/plot-review/SKILL.md`.

| Client | Project skills | Personal skills |
| --- | --- | --- |
| [Codex skills](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/` | `~/.agents/skills/` |
| [Claude Code skills](https://code.claude.com/docs/en/skills) | `.claude/skills/` | `~/.claude/skills/` |
| [Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | `.agents/skills/` or `.github/skills/` | `~/.agents/skills/` or `~/.copilot/skills/` |
| [Cursor skills](https://cursor.com/docs/skills) | `.agents/skills/` or `.cursor/skills/` | `~/.agents/skills/` or `~/.cursor/skills/` |
| [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) | `.agents/skills/` or `.gemini/skills/` | `~/.agents/skills/` or `~/.gemini/skills/` |

Append `plot-review/SKILL.md` to these directories. Project skills travel with the repository; personal skills span local projects. Keep one discoverable copy per client and check its loaded path when names conflict.

For **Claude Code**, check that `.claude/skills/plot-review/` does not already exist, then copy the included skill from the example repository root:

```bash
mkdir -p .claude/skills
cp -R .agents/skills/plot-review .claude/skills/
```

Some other clients also discover `.claude/skills/`; check for duplicate names after copying. In another repository, adapt the skill's file references and checks. Only `SKILL.md` is required. [Codex skill format](https://learn.chatgpt.com/docs/build-skills), [Cursor discovery paths](https://cursor.com/docs/skills).

Use your [client's skill list or invocation](index.md) and check which file loads. Reload or restart if it is missing. An unrelated request, such as editing prose, should not trigger the review skill.

Try [Refactor this script into the lab format](r-refactoring.md) for a one-line request using a skill or named agent. It includes the complete reusable setup and checks.

## Match access to the work

Keep a narrow workspace, but remember that `.gitignore` controls tracking, not reading or sharing. Tool permissions, sandboxing, credentials, and service settings determine access. Check shell, browser, and connectors separately. [Codex approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security).

Give a reviewer read/search tools where supported; implementation also needs edits and test commands. “Do not edit” is an instruction; client restrictions enforce it. Each client page shows an optional reviewer.

Check the [lab data guidance](../reference/lab-data-policy.md) before adapting this setup to university work. Service approval depends on the data and connection, not just the model name.
