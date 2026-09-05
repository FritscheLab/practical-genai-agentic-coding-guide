---
layout: default
title: Portable context and skills
parent: Agent setup
nav_order: 1
description: Keep the project instructions useful across coding tools, and check where each tool expects to find them.
---

# Portable context and skills

When colleagues use different coding tools, you should still be able to share the task, the project conventions, and the expected results. The main difference is where each tool looks for those instructions. This page explains those pieces so you can carry a useful procedure from one setup to another.

**Documentation reviewed: September 5, 2026.**

## Model, provider, client, and mode

Three names often get mixed together when we talk about an agent. The **model** generates responses and decisions. The **provider** serves that model and manages account and service controls. The **client** is the tool you work in: it gathers context, offers tools, applies permissions, and manages the session.

This distinction helps when something behaves unexpectedly. Changing the model inside an editor leaves the editor’s instruction-file format in place. Running a client in your local terminal also does not mean the model itself runs on your computer.

When you compare results with a colleague, record all three, along with whether the work ran locally or in a hosted environment. The [client setup pages](index.md) link to installation and access documentation, since available models and sign-in options can vary by client and account.

The **mode** describes how you want the client to work in a session: explain, plan, or carry out a task. It can change the available tools and workflow without changing the model. Permissions are another setting to inspect: a mode's name alone does not tell you everything it can read, write, or run. See [choosing a mode](index.md#choose-how-you-want-to-work) before your first task.

## Start with the briefing and the task

For the first lesson, you need the repository instructions and a task brief. The other pieces below become useful when you have a procedure to repeat or work to delegate. You do not need to configure all of them.

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

Keep the shared briefing in the repository's root `AGENTS.md`. The included `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` connect their clients to that briefing; Codex and Cursor can read it directly. Those files explain the project. A client settings file, such as `.codex/config.toml`, configures how the tool runs. A skill supplies a procedure the agent can use for a matching task. Putting the same prose in all three places would make the setup harder to maintain.

This repository includes a small Codex configuration and reviewer definition under `.codex/`, plus the shared `pipeline-review` skill under `.agents/skills/`. The [Codex walkthrough](codex.md) explains the included settings. The other client folders in the map below are supported destinations you can add when needed; cloning this repository does not create every setup shown here. Defining a reviewer also does not mean a review has run.

| Client | Project settings and named roles |
| --- | --- |
| [Codex](codex.md) | Settings: `.codex/config.toml`. Roles: `.codex/agents/*.toml`. [Settings reference](https://learn.chatgpt.com/docs/config-file/config-basic), [agent reference](https://learn.chatgpt.com/docs/agent-configuration/subagents). |
| [Claude Code](claude-code.md) | Settings: `.claude/settings.json`. Roles: `.claude/agents/*.md`. [Settings reference](https://code.claude.com/docs/en/settings), [agent reference](https://code.claude.com/docs/en/sub-agents). |
| [Copilot](copilot.md) | CLI settings: `.github/copilot/settings.json`. Roles: `.github/agents/*.md`. VS Code uses its own Settings editor. [CLI settings](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference), [agent reference](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents), [VS Code settings](https://code.visualstudio.com/docs/configure/settings). |
| [Cursor](cursor.md) | Execution settings: `.cursor/permissions.json` and `.cursor/sandbox.json`. Roles: `.cursor/agents/*.md`. [Execution settings](https://cursor.com/docs/agent/security/run-modes), [agent reference](https://cursor.com/docs/subagents). |
| [Gemini CLI](gemini-cli.md) | Settings: `.gemini/settings.json`. Roles: `.gemini/agents/*.md`. [Settings reference](https://geminicli.com/docs/reference/configuration/), [agent reference](https://geminicli.com/docs/core/subagents/). |

A leading `~` means your home directory. For example, `~/.codex/config.toml` holds your personal Codex defaults, while `.codex/config.toml` belongs to this project and loads only after you trust it. Keep machine-specific preferences and credentials in your personal setup. Before sharing a settings file, check the effective configuration: client defaults, session choices, and organization rules can affect which values apply. [Codex configuration layers](https://learn.chatgpt.com/docs/config-file/config-basic).

## Find and use the review skill

A skill starts with a directory containing `SKILL.md`. At the top, YAML fields give its `name` and `description`; the procedure follows underneath. Make the description specific enough to explain when you would want the agent to use it. Supporting scripts and reference files can live in the same directory. [Agent Skills specification](https://agentskills.io/specification).

The [pipeline-review skill](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/.agents/skills/pipeline-review/SKILL.md) is already included at `.agents/skills/pipeline-review/SKILL.md`. Codex, Copilot, Cursor, and Gemini CLI support that project location. You can inspect the procedure before using it; no additional skill installation is needed for those clients.

| Client | Project skills | Personal skills |
| --- | --- | --- |
| [Codex skills](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/` | `~/.agents/skills/` |
| [Claude Code skills](https://code.claude.com/docs/en/skills) | `.claude/skills/` | `~/.claude/skills/` |
| [Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | `.agents/skills/` or `.github/skills/` | `~/.agents/skills/` or `~/.copilot/skills/` |
| [Cursor skills](https://cursor.com/docs/skills) | `.agents/skills/` or `.cursor/skills/` | `~/.agents/skills/` or `~/.cursor/skills/` |
| [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) | `.agents/skills/` or `.gemini/skills/` | `~/.agents/skills/` or `~/.gemini/skills/` |

Each entry is a parent directory: the complete path ends in `pipeline-review/SKILL.md`. Project skills travel with the repository when committed; personal skills are available across your local projects. This review procedure depends on this repository's contract and tests, so the project location is the useful starting point. The table shows supported choices, not every compatibility path. Keep one discoverable copy per client and check its loaded path when names conflict.

For **Claude Code**, check that `.claude/skills/pipeline-review/` does not already exist, then copy the included skill from the repository root:

```bash
mkdir -p .claude/skills
cp -R .agents/skills/pipeline-review .claude/skills/
```

If you use several clients in the same checkout, remember that some also discover `.claude/skills/`; check for duplicate names after this copy. When adopting the procedure in another repository, copy the skill directory into that client's project skills folder and adapt its contract, file references, and checks. A folder containing only `SKILL.md` is valid; scripts and client-specific metadata are optional. [Codex skill format](https://learn.chatgpt.com/docs/build-skills), [Cursor discovery paths](https://cursor.com/docs/skills).

Find the skill in your client's skill list or invoke it by name using the [client walkthrough](index.md). If it does not appear after adding a new folder, reload skills or start a fresh session as that client requires. Ask for a pipeline review and check which procedure loads. Then try an unrelated request, such as editing a short paragraph: the review skill should not take over that task.

## Match access to the work

We use synthetic fixtures in this repository so the lessons can be shared. When you bring the workflow to another project, remember that `.gitignore` only controls Git tracking: it does not stop an agent reading a file or sending data elsewhere. A narrow workspace helps you keep track of the work; tool permissions, sandboxing, credentials, and service settings determine its access. Check shell, browser, and connector access separately. [Codex approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security).

Give a reviewer reading and searching tools where the client supports that restriction. An implementation task also needs the edits and test commands in its brief. A request such as “do not edit” tells the agent what you want; the client’s restrictions are what enforce the limit. Each client page includes an optional reviewer example and explains what to check in your installed tool.

Those controls do not determine which university data a service is permitted to handle. Use the [lab data guidance](../reference/lab-data-policy.md) to check PHI, PII, and service approval before adapting the setup. Personal keys, new connectors, and hosted sessions can change the data route even when the model name stays familiar.
