---
layout: default
title: GitHub Copilot
parent: Agent setup
nav_order: 4
description: Use Copilot in VS Code or the CLI, with shared project instructions and optional review tools.
---

# GitHub Copilot

This page is for **Copilot in VS Code or Copilot CLI**. Start with whichever you already use. The repository includes a short Copilot instruction file and a shared review skill. Check that your chosen client finds them as you work through Lesson 1.

**Documentation reviewed: September 5, 2026.** Use the [CLI quickstart](https://docs.github.com/en/copilot/get-started/cli-quickstart) if you need to install the CLI, and check the [customization support matrix](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) for your editor. Support for custom agents, delegation, skills, hooks, and instruction formats varies across Copilot clients.

## First session

1. Install and sign in using your client’s official setup. Open this repository and complete the [Python quickstart](../quickstart.md) so you have a working run to compare with the agent’s results.
2. Open `.github/copilot-instructions.md` and follow its references to `AGENTS.md` and `REPO_MAP.md`. These are the project instructions you want Copilot to use.
3. Use **Ask** in a VS Code Local session, or `/plan` in Copilot CLI, as described below. Send the [orientation prompt](index.md#check-the-agents-understanding), compare the answer with the files, and check any instruction references the client shows.

Copilot’s repository-wide instructions live in `.github/copilot-instructions.md`; instructions for particular file paths use `.github/instructions/*.instructions.md`. Here, the first file simply points to the shared conventions in `AGENTS.md`. That keeps updates in one place. Check `AGENTS.md` support for your client, since editors can discover it differently. [Copilot customization reference](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).

## Ask, plan, or implement

In VS Code, open **Chat → Open Chat** from the title bar. For this walkthrough, start a new session with **Local** in the Session Target picker; these instructions use its **Ask**, **Plan**, and **Agent** roles. Ask helps you understand the code without changing it. Choose Plan, or enter `/plan <task>`, when you want to discuss the approach first. Refine the proposal, then choose **Start Implementation** when it matches your task. Agent can edit files, run commands, and work through failures. [Chat view](https://code.visualstudio.com/docs/agents/run/chat-view), [agent roles](https://code.visualstudio.com/docs/agents/run/agent-harnesses), [planning](https://code.visualstudio.com/docs/agents/run/planning).

Before implementation, choose **Default Approvals** in the chat-input permissions picker and inspect the tools enabled through **Configure Tools** in Local Agent. Tool availability controls what the agent can call; approval settings control which calls need confirmation. Default Approvals respects saved choices, so it does not mean every command will pause. Read command details and output as the work proceeds; **Chat: Manage Tool Approval** lets you inspect remembered approvals. [Tool selection](https://code.visualstudio.com/docs/agents/run/tools), [permissions](https://code.visualstudio.com/docs/agents/run/approvals).

In Copilot CLI, enter `/plan <task>` to work out the approach before implementation and `/permissions default` to use the normal approval policy. Review the proposed plan before accepting implementation. Plan mode blocks recognized project edits, but it is not a complete sandbox: some external tools and uncertain shell commands can still run. Check the requested action as well as the mode label. [CLI commands and plan-mode limits](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

## Choose a model in this client

In VS Code, use the **model picker in the chat input**; **Chat: Manage Language Models** shows providers and model capabilities. Agent use requires tool-calling support. In Copilot CLI, `/model` opens the selector and changes the current session's choice without saving a new default. The available choices depend on the client, selected harness, account, and organization controls, so compare the options you actually see. [VS Code models](https://code.visualstudio.com/docs/agent-customization/language-models), [Copilot model access](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model), [CLI model command](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

Selecting a model from another provider still leaves you in Copilot's workflow, with its instruction discovery and tool controls. Moving to that provider's own coding client means following a different setup page. For the lesson's comparison, keep the client, mode, task, and checks the same while changing the model; record **Auto** when you let the client choose, since it can route requests to different models. [VS Code model routing](https://code.visualstudio.com/docs/agent-customization/language-models).

## Try the review skill

The [shared review skill](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/.agents/skills/pipeline-review/SKILL.md) is already in `.agents/skills/pipeline-review/`. Ask Copilot to use `pipeline-review`, then check whether it loads that procedure. Other documented project locations include `.github/skills/` and `.claude/skills/`; personal skills can live under `~/.copilot/skills/` or `~/.agents/skills/`. Use the included copy here. The [folder map](portable-context.md) explains how to carry it to another project. [Adding Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## Create a reviewer profile

For a recurring review, save the following as `.github/agents/pipeline-reviewer.md`. Creating the file defines the role. You still need to select it or ask the main agent to delegate a task to it. [Copilot custom agents](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents).

```markdown
---
name: pipeline-reviewer
description: Inspect synthetic pipeline changes for contract violations.
tools: [read, search]
---

Read AGENTS.md and docs/reference/io_contract.md.
Review the requested files and tests without editing them.
Return concrete discrepancies with file locations and a minimal synthetic
example. Separate observed evidence from checks you could not run.
```

The `read` and `search` aliases limit this reviewer to those tool categories. Keep the `tools` field: omitting it grants all available tools. Because unsupported names may be ignored, check the effective tool list in your client after saving the profile. [Custom agent tool configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration).

Select the profile in your client’s agent selector, or ask the main agent to delegate to it where subagents are supported. Include the task contract and test results in the request. This reviewer cannot run tests itself with the tool list shown above.

## Check the diff and test results

Read the diff alongside the commands and check results before accepting the change. If you later move the exercise to Copilot in the cloud, set up that environment separately: it may not have your local interpreter, files, or personal skills. The support matrix and setup documentation will help you identify what to carry over.
