---
layout: default
title: GitHub Copilot
parent: Agent setup
nav_order: 4
description: Use Copilot in VS Code or the CLI, with shared project instructions and optional review tools.
---

# GitHub Copilot

Use **Copilot in VS Code or Copilot CLI**. The repository includes shared instructions and a review skill; check their discovery during Lesson 1.

**Documentation reviewed: September 5, 2026.** Use the [CLI quickstart](https://docs.github.com/en/copilot/get-started/cli-quickstart) if you need to install the CLI, and check the [customization support matrix](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) for your editor. Support for custom agents, delegation, skills, hooks, and instruction formats varies across Copilot clients.

## First session

1. Install and sign in using your client’s official setup. Open the example repository and complete the [setup for your language path](../quickstart.md) so you have a working run to compare with the agent’s results.
2. Open `.github/copilot-instructions.md` and follow its references to `AGENTS.md` and `REPO_MAP.md`. These are the project instructions you want Copilot to use.
3. Use **Ask** in a VS Code Local session, or `/plan` in Copilot CLI, as described below. Send the [orientation prompt](index.md#check-the-agents-understanding), compare the answer with the files, and check any instruction references the client shows.

Repository instructions use `.github/copilot-instructions.md`; path-specific instructions use `.github/instructions/*.instructions.md`. The included adapter points to `AGENTS.md`. Discovery of `AGENTS.md` differs by client. [Copilot customization reference](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).

## Ask, plan, or implement

In VS Code, open **Chat → Open Chat** and choose **Local** in the Session Target picker. **Ask** explains code; **Plan** or `/plan <task>` proposes an approach. Choose **Start Implementation** when ready. **Agent** edits and runs commands. [Chat view](https://code.visualstudio.com/docs/agents/run/chat-view), [agent roles](https://code.visualstudio.com/docs/agents/run/agent-harnesses), [planning](https://code.visualstudio.com/docs/agents/run/planning).

Before implementation, inspect **Default Approvals** and **Configure Tools** in Local Agent. Tools determine available actions; approvals determine which pause. Saved approvals still apply. Use **Chat: Manage Tool Approval** to inspect them. [Tool selection](https://code.visualstudio.com/docs/agents/run/tools), [permissions](https://code.visualstudio.com/docs/agents/run/approvals).

In Copilot CLI, use `/plan <task>` and `/permissions default`. Review the plan before implementation. Plan mode blocks recognized project edits, but external tools and uncertain shell commands may still run; it is not a complete sandbox. [CLI commands and plan-mode limits](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

## Choose a model in this client

In VS Code, use the **model picker**; **Chat: Manage Language Models** lists providers and capabilities. Agent use requires tool calling. In CLI, `/model` changes this session without saving a default. Choices depend on client, harness, account, and organization. [VS Code models](https://code.visualstudio.com/docs/agent-customization/language-models), [Copilot model access](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model), [CLI model command](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

Switching models keeps Copilot's instruction and tool controls. For a comparison, hold the client, mode, and task fixed. Record **Auto** if selected: it can route requests to different models. [VS Code model routing](https://code.visualstudio.com/docs/agent-customization/language-models).

## Try the review skill

The included skill is at `.agents/skills/plot-review/`. Ask Copilot to use `plot-review` and check what loads. Other project locations include `.github/skills/` and `.claude/skills/`; personal locations include `~/.copilot/skills/` and `~/.agents/skills/`. See the [folder map](portable-context.md). [Adding Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## Create a reviewer profile

Save this optional profile as `.github/agents/plot-reviewer.md`. Then select it or request delegation. [Copilot custom agents](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents).

```markdown
---
name: plot-reviewer
description: Review plotting code and its rendered image against the contract.
tools: [read, search]
---

Read AGENTS.md and use .agents/skills/plot-review/SKILL.md.
Review the requested diff, image, and alt text against the local figure
specifications. Use supplied test results; do not edit files.
Report findings with source locations and name any checks you could not perform.
```

Keep `tools`: omitting it grants all available tools. The aliases restrict this role to read/search categories; check the effective list because unsupported names may be ignored. [Custom agent tool configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration).

Select the profile or ask for delegation where supported. Supply the change and test results; these tools cannot run tests.

## Check the diff and test results

Read the diff and actual check results. Cloud sessions need separate setup: your local interpreter, files, and personal skills may be unavailable there.
