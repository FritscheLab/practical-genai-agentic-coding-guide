---
layout: default
title: Codex
parent: Agent setup
nav_order: 2
description: Understand the included Codex project folders, check the active setup, and adapt it for your own repository.
---

# Codex

The [example repository](https://github.com/FritscheLab/practical-genai-agentic-coding-example) includes Codex instructions, settings, and optional review tools. Check what loads, then start your language path.

**Documentation reviewed: September 5, 2026.** For installation and sign-in, use the official [Codex CLI setup](https://learn.chatgpt.com/docs/codex/cli). The [desktop quickstart](https://learn.chatgpt.com/docs/quickstart) explains selecting Codex in the desktop app. The interface and available access may differ by account.

## Find the project setup

Use `ls -a` to see the included hidden folders:

```text
AGENTS.md
.codex/
├── config.toml
└── agents/
    ├── plot-reviewer.toml
    └── r-refactorer.toml
.agents/
└── skills/
    ├── plot-review/
    │   └── SKILL.md
    └── lab-r-refactor/
        ├── SKILL.md
        └── references/
            └── lab-r-template.md
```

Read [AGENTS.md](https://github.com/FritscheLab/practical-genai-agentic-coding-example/blob/main/AGENTS.md) for conventions. The included [.codex/config.toml](https://github.com/FritscheLab/practical-genai-agentic-coding-example/blob/main/.codex/config.toml) sets:

```toml
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = false
```

Local commands can write in the workspace; network access is off, and broader access can request approval. Model choice and sign-in use your existing setup. Review the files before trusting the project: that enables its configuration. [Project configuration](https://learn.chatgpt.com/docs/config-file/config-basic), [sandbox behavior](https://learn.chatgpt.com/docs/agent-approvals-security).

Your personal defaults live in `~/.codex/config.toml` (under `CODEX_HOME` if you changed it). Trusted project settings override those defaults; CLI overrides take precedence, and managed requirements can constrain the result. Provider and authentication-related settings belong in your personal setup: project configuration ignores keys such as `model_provider` and `model_providers`. [Configuration precedence](https://learn.chatgpt.com/docs/config-file/config-basic#configuration-precedence), [project and personal settings](https://learn.chatgpt.com/docs/config-file/config-advanced#project-config-files-codexconfigtoml).

Current documentation also offers **Beta permission profiles** using `default_permissions` and `[permissions]`. They are an alternative to the supported sandbox settings above. Do not mix the two formats: a loaded `sandbox_mode` or `--sandbox` option normally takes precedence over a permission profile. If you adopt profiles, review all loaded layers, including custom-agent settings. [Permission profiles and migration](https://learn.chatgpt.com/docs/permissions).

## Check the first session

1. Complete your [language setup](../quickstart.md). Launch `codex` from the example repository root, or open that folder in your Codex client.
2. Check access before the first prompt. In the CLI, use `/permissions` to choose Read Only for orientation and `/status` to inspect the active setup. Use `/debug-config` if the settings differ from the files: it shows configuration layers and policy constraints. The implementation lesson later needs workspace edits and test commands. [Codex commands](https://learn.chatgpt.com/docs/developer-commands).
3. Use the [orientation prompt](index.md#check-the-agents-understanding). Compare the files and commands in the answer with the ones you used yourself.

Codex discovers project `AGENTS.md` files along the path from the project root to the working directory. Your personal defaults can live in `~/.codex/AGENTS.md`, and an `AGENTS.override.md` can take precedence. If the agent reports unexpected instructions, check for those additional files. After changing instructions, start a fresh session and check what it loads. [Codex instruction discovery](https://developers.openai.com/codex/guides/agents-md).

## Choose a model for this run

Use `/model` to choose a model and supported reasoning effort, or start with `codex --model MODEL_ID`. Replace `MODEL_ID` with a supported identifier. Personal or trusted-project settings can set a default; this repository leaves it unset. [Model controls](https://learn.chatgpt.com/docs/developer-commands), [configuration options](https://learn.chatgpt.com/docs/config-file/config-basic).

Record the model and reasoning setting shown by `/status`; use `/debug-config` to investigate differences. Switching models keeps Codex's instruction and tool controls. Repeat orientation before asking the new setup to edit. [Session diagnostics](https://learn.chatgpt.com/docs/developer-commands), [model settings](https://learn.chatgpt.com/docs/config-file/config-reference).

A provider change needs its own setup. Personal `~/.codex/config.toml` can select `model_provider` and define `[model_providers.<id>]` with the endpoint and authentication method. The current custom-provider protocol is `responses`; an endpoint advertised as “OpenAI-compatible” may support a different API or only some capabilities. Follow the provider's Codex-specific instructions and verify the tools you need. Keep provider settings and credentials in your personal or managed setup. [Custom providers](https://learn.chatgpt.com/docs/config-file/config-advanced#custom-model-providers), [supported provider configuration](https://learn.chatgpt.com/docs/config-file/config-reference).

## Plan the change and choose its access

Use `/plan` when you want an approach before edits: `/plan How would you repair the plot to meet docs/reference/figure-specifications.md?` The desktop app also documents `/plan`, with its own command menu. [CLI planning command](https://learn.chatgpt.com/docs/developer-commands#switch-to-plan-mode-with-plan), [desktop commands](https://learn.chatgpt.com/docs/reference/slash-commands).

Planning and permissions have separate controls. When you move to implementation, check both again. The Auto permission preset allows workspace reads, edits, and commands; the sandbox limits where those commands can write and reach the network, while approval settings determine when an action needs permission. [Codex approvals and sandboxing](https://learn.chatgpt.com/docs/agent-approvals-security).

Tools do the practical work: opening a file, applying an edit, or running a check. In the CLI, `/mcp` shows connected tools, and `/model` selects the model separately from those controls. Check external tools individually because the local command sandbox does not cover every connector operation. For these lessons, start with repository files and the checks from your language path. [Codex tool commands](https://learn.chatgpt.com/docs/developer-commands), [scope of sandbox controls](https://learn.chatgpt.com/docs/agent-approvals-security).

## Try the review skill

The [plot-review skill](https://github.com/FritscheLab/practical-genai-agentic-coding-example/blob/main/.agents/skills/plot-review/SKILL.md) is already in `.agents/skills/plot-review/`. In the CLI or IDE extension, use `/skills` to find it or mention `$plot-review` in your request. Check its displayed path, especially if you also have personal skills under `~/.agents/skills/`. Codex can also select skills from their descriptions. [Codex skills](https://developers.openai.com/codex/skills).

```text
$plot-review Review my plotting changes, runs/with-fix/summary.png,
and its alt text against the journal specifications. Report findings
and anything you could not check; do not edit files.
```

## Try the named reviewer

The included [.codex/agents/plot-reviewer.toml](https://github.com/FritscheLab/practical-genai-agentic-coding-example/blob/main/.codex/agents/plot-reviewer.toml) defines the role below. A standalone custom agent file needs `name`, `description`, and `developer_instructions`; its model can inherit from the parent. Personal roles can live in `~/.codex/agents/`. [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

```toml
name = "plot-reviewer"
description = "Review plotting code, test evidence, and the rendered chart without inspecting participant data."
sandbox_mode = "read-only"
developer_instructions = """
Read AGENTS.md and use .agents/skills/plot-review/SKILL.md in the target repository.
Review source code, tests, and the chart made from invented summary counts.
Do not inspect data tables, participant records, or study logs.
Report code findings and visual observations separately, with actual check results.
Do not edit files. If permissions prevent execution or image inspection, report
which supplied evidence you reviewed and which checks remain unrun.
"""
```

Ask `Have plot-reviewer review my plotting changes.` Check the resulting threads with `/agent`. Subagents are currently enabled by default; check older setup recipes against your installed version. One reviewer is enough here. [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Before using the role, check its effective permission mode and any connected tools. The main session can override settings, and external connections can provide access beyond the local sandbox. [Codex approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security).

## Try a reusable R refactoring task

Try [Refactor this script into the lab format](r-refactoring.md): one request, a local skill and template, then a verifier and diff. It includes the complete setup and copying instructions. Guidance reviewed **September 10, 2026**.

## Bring the setup to another repository

From the new repository's root, replace this source path with your local example checkout. Existing files stay in place; merge them manually if needed.

```bash
example_repo=/path/to/practical-genai-agentic-coding-example
mkdir -p .codex/agents .agents/skills
cp -n "$example_repo/.codex/config.toml" .codex/config.toml
cp -n "$example_repo/.codex/agents/plot-reviewer.toml" .codex/agents/
cp -Rn "$example_repo/.agents/skills/plot-review" .agents/skills/
```

Write that project's own `AGENTS.md`, then update the reviewer and skill to use its contracts, commands, and examples. Start a fresh Codex session there and repeat the orientation, `/debug-config`, and `/skills` checks. Keep your personal `~/.codex` directory out of the copy: it can contain authentication state, history, and machine-specific settings. [Codex state locations](https://learn.chatgpt.com/docs/config-file/config-advanced#config-and-state-locations).

## Check the diff and test results

Read the diff and actual check results. With a new setup, run the checks yourself too. Ask the implementation agent to address findings you can confirm.
