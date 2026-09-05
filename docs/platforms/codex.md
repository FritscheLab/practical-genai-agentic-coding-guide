---
layout: default
title: Codex
parent: Agent setup
nav_order: 2
description: Understand the included Codex project folders, check the active setup, and adapt it for your own repository.
---

# Codex

This repository includes a working example of Codex project setup: shared instructions, project settings, a review skill, and a named reviewer. Start by checking what Codex loads and whether it can use the Python environment you set up. The reviewer is there to try when you have a change ready for review.

**Documentation reviewed: September 5, 2026.** For installation and sign-in, use the official [Codex CLI setup](https://learn.chatgpt.com/docs/codex/cli). The [desktop quickstart](https://learn.chatgpt.com/docs/quickstart) explains selecting Codex in the desktop app. The interface and available access may differ by account.

## Find the project setup

These files serve different parts of the setup. Folders beginning with a dot may be hidden in your file browser; `ls -a` shows them in a terminal.

```text
AGENTS.md
.codex/
├── config.toml
└── agents/
    └── pipeline-reviewer.toml
.agents/
└── skills/
    └── pipeline-review/
        └── SKILL.md
```

Read [AGENTS.md](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/AGENTS.md) for the project conventions and [.codex/config.toml](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/.codex/config.toml) for the client settings. The included configuration is small:

```toml
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = false
```

This gives local commands workspace write access while keeping their network access off; operations outside the permitted access can request approval. It leaves model choice and sign-in to your existing setup. Codex reads project configuration only after you trust the project, so review these files before accepting the client's trust prompt. [Project configuration](https://learn.chatgpt.com/docs/config-file/config-basic), [sandbox behavior](https://learn.chatgpt.com/docs/agent-approvals-security).

Your personal defaults live in `~/.codex/config.toml` (under `CODEX_HOME` if you changed it). Trusted project settings override those defaults; CLI overrides take precedence, and managed requirements can constrain the result. Provider and authentication-related settings belong in your personal setup: project configuration ignores keys such as `model_provider` and `model_providers`. [Configuration precedence](https://learn.chatgpt.com/docs/config-file/config-basic#configuration-precedence), [project and personal settings](https://learn.chatgpt.com/docs/config-file/config-advanced#project-config-files-codexconfigtoml).

Current documentation also offers **Beta permission profiles** using `default_permissions` and `[permissions]`. They are an alternative to the supported sandbox settings above. Do not mix the two formats: a loaded `sandbox_mode` or `--sandbox` option normally takes precedence over a permission profile. If you adopt profiles, review all loaded layers, including custom-agent settings. [Permission profiles and migration](https://learn.chatgpt.com/docs/permissions).

## Check the first session

1. Complete the [Python quickstart](../quickstart.md), then launch `codex` from the repository root or open the repository in your Codex client. This keeps the agent’s work in the project you just tested.
2. Check access before the first prompt. In the CLI, use `/permissions` to choose Read Only for orientation and `/status` to inspect the active setup. Use `/debug-config` if the settings differ from the files: it shows configuration layers and policy constraints. The implementation lesson later needs workspace edits and test commands. [Codex commands](https://learn.chatgpt.com/docs/developer-commands).
3. Use the [orientation prompt](index.md#check-the-agents-understanding). Compare the files and commands in the answer with the ones you used yourself.

Codex discovers project `AGENTS.md` files along the path from the project root to the working directory. Your personal defaults can live in `~/.codex/AGENTS.md`, and an `AGENTS.override.md` can take precedence. If the agent reports unexpected instructions, check for those additional files. After changing instructions, start a fresh session and check what it loads. [Codex instruction discovery](https://developers.openai.com/codex/guides/agents-md).

## Choose a model for this run

Open `/model` in the CLI to choose an available model and, where supported, its reasoning effort. For a new session, `codex --model MODEL_ID` selects the model you name; replace `MODEL_ID` with an identifier your provider supports. A `model` setting can supply a personal or trusted-project default. This repository leaves it unset so you and a labmate can use different models with the same task. [Model controls](https://learn.chatgpt.com/docs/developer-commands), [configuration options](https://learn.chatgpt.com/docs/config-file/config-basic).

Record what you requested and what `/status` reports as active, along with the reasoning setting. Use `/debug-config` to investigate a difference. Changing the model keeps you in the Codex client, with its instruction discovery and tool controls; the available reasoning settings and model capabilities can still differ. Repeat the orientation task before giving the new setup implementation work. [Session diagnostics](https://learn.chatgpt.com/docs/developer-commands), [model settings](https://learn.chatgpt.com/docs/config-file/config-reference).

A provider change needs its own setup. Personal `~/.codex/config.toml` can select `model_provider` and define `[model_providers.<id>]` with the endpoint and authentication method. The current custom-provider protocol is `responses`; an endpoint advertised as “OpenAI-compatible” may support a different API or only some capabilities. Follow the provider's Codex-specific instructions and verify the tools you need. Keep provider settings and credentials in your personal or managed setup. [Custom providers](https://learn.chatgpt.com/docs/config-file/config-advanced#custom-model-providers), [supported provider configuration](https://learn.chatgpt.com/docs/config-file/config-reference).

## Plan the change and choose its access

In the CLI, `/plan` starts planning; you can include a request, such as `/plan Work through the QC gate task brief and propose the smallest change.` Use that discussion to settle the denominator and threshold examples before coding. The desktop app also documents `/plan`, with its own command menu. [CLI planning command](https://learn.chatgpt.com/docs/developer-commands#switch-to-plan-mode-with-plan), [desktop commands](https://learn.chatgpt.com/docs/reference/slash-commands).

Planning and permissions have separate controls. When you move to implementation, check both again. The Auto permission preset allows workspace reads, edits, and commands; the sandbox limits where those commands can write and reach the network, while approval settings determine when an action needs permission. [Codex approvals and sandboxing](https://learn.chatgpt.com/docs/agent-approvals-security).

Tools do the practical work: opening a file, applying an edit, or running a check. In the CLI, `/mcp` shows connected tools, and `/model` selects the model separately from those controls. Check external tools individually because the local command sandbox does not cover every connector operation. For these lessons, start with repository files and the Python checks. [Codex tool commands](https://learn.chatgpt.com/docs/developer-commands), [scope of sandbox controls](https://learn.chatgpt.com/docs/agent-approvals-security).

## Try the review skill

The [pipeline-review skill](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/.agents/skills/pipeline-review/SKILL.md) is already in `.agents/skills/pipeline-review/`. In the CLI or IDE extension, use `/skills` to find it or mention `$pipeline-review` in your request. Check its displayed path, especially if you also have personal skills under `~/.agents/skills/`. Codex can also select skills from their descriptions. [Codex skills](https://developers.openai.com/codex/skills).

```text
$pipeline-review
Review the pipeline and its documented contract. Report concrete discrepancies
with file locations and a small example. Do not modify files.
```

## Try the named reviewer

The included [.codex/agents/pipeline-reviewer.toml](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/.codex/agents/pipeline-reviewer.toml) defines the role below. A standalone custom agent file needs `name`, `description`, and `developer_instructions`; its model can inherit from the parent. Personal roles can live in `~/.codex/agents/`. [Codex custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

```toml
name = "pipeline-reviewer"
description = "Review the synthetic BMI pipeline against its documented contract."
sandbox_mode = "read-only"
developer_instructions = """
Resolve repository paths from the project root containing AGENTS.md.
Read AGENTS.md and docs/reference/io_contract.md.
Use the pipeline-review skill when reviewing a pipeline change.
Inspect the requested code and tests without editing files.
Report behavior discrepancies with file locations, a minimal synthetic example,
and the expected result. Distinguish verified findings from open questions.
Run checks only if the effective tools and permissions permit them;
otherwise state which supplied results you inspected and which checks are unrun.
"""
```

Ask the main agent to delegate a specific review to `pipeline-reviewer`. In the CLI, `/agent` lets you inspect the resulting agent threads. Current documentation describes subagents as enabled by default; if you find an older recipe with experimental switches, check it against your installed version. One reviewer is plenty for this lesson, since each additional agent adds context and token costs. [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Before using the role, check its effective permission mode and any connected tools. The main session can override settings, and external connections can provide access beyond the local sandbox. [Codex approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security).

## Bring the setup to another repository

From the new repository's root, replace the example source path below with your local checkout of this guide. These commands leave existing files in place. If you already have a setup, merge the settings and procedures you want to adopt in your editor.

```bash
guide_repo=/path/to/practical-genai-agentic-coding-guide
mkdir -p .codex/agents .agents/skills
cp -n "$guide_repo/.codex/config.toml" .codex/config.toml
cp -n "$guide_repo/.codex/agents/pipeline-reviewer.toml" .codex/agents/
cp -Rn "$guide_repo/.agents/skills/pipeline-review" .agents/skills/
```

Write that project's own `AGENTS.md`, then update the reviewer and skill to use its contracts, commands, and examples. Start a fresh Codex session there and repeat the orientation, `/debug-config`, and `/skills` checks. Keep your personal `~/.codex` directory out of the copy: it can contain authentication state, history, and machine-specific settings. [Codex state locations](https://learn.chatgpt.com/docs/config-file/config-advanced#config-and-state-locations).

## Check the diff and test results

Ask for the changed files, the commands that were run, their results, and anything still uncertain. When trying a new setup, run the repository checks yourself too. Use the reviewer’s examples to decide which changes need attention, then ask the implementation agent to address them.
