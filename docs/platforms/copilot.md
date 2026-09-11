---
layout: default
title: GitHub Copilot
parent: Agent setup
nav_order: 4
description: Use Copilot Chat in VS Code, understand Ask/Plan/Agent, and review changes through Source Control.
---

# GitHub Copilot

**VS Code + GitHub Copilot is the default for this guide.** Start with the [detailed setup](../setup/vscode-copilot.md), then follow your [Python or R path](../quickstart.md). Copilot runs commands while you inspect the output, plots, and Git diff in VS Code. Copilot CLI is covered in the [CLI appendix](../appendix/command-line.md).

**VS Code controls and account guidance reviewed: September 11, 2026.** The optional customization reference below retains its September 5, 2026 review date. Documentation describes available behavior; the installed client, account, and organization determine which controls you see.

## First session

1. Complete the setup and confirm that Explorer shows the exercise repository and its baseline image.
2. Open `.github/copilot-instructions.md` and follow its references to `AGENTS.md` and `REPO_MAP.md`.
3. Open **Chat → Open Chat**, choose **Local**, then **Ask**. Send the [orientation prompt](index.md#check-the-agents-understanding), open the source references, and compare the answer with the actual files. [VS Code Chat view](https://code.visualstudio.com/docs/agents/run/chat-view)

Repository instructions use `.github/copilot-instructions.md`; the included adapter points to `AGENTS.md`. Check instruction references the client displays. A plausible answer alone does not prove the file was loaded. [Copilot customization reference](https://docs.github.com/en/copilot/reference/customization-cheat-sheet)

## Identify the four controls

| Control | Use in this exercise |
| --- | --- |
| Session target | **Local**, working in the open workspace |
| Agent role | **Ask** to understand, **Plan** to specify, **Agent** to implement and run checks |
| Model | Keep **Auto**, or choose an available model if your account allows it |
| Permissions | **Manual permissions** / **Default permissions**, then inspect execution requests and their scope |

Local sessions offer the three roles. After reviewing a plan, use **Start Implementation** and choose the local implementation agent, or switch the role to **Agent** and explicitly request the reviewed repair. The target named **Copilot** is a separate session option; choose **Local** for this walkthrough's role sequence. [Session targets, roles, and plan handoff](https://code.visualstudio.com/docs/agents/run/agent-harnesses)

The captured VS Code 1.137.0 client labels this **Default permissions**; the current documentation calls it **Manual permissions**. Some other versions show Default Approvals. Inspect the current permission picker and the actual approval request. Existing tool and terminal approvals can permit actions without another prompt even with **Manual permissions** selected. **Chat: Manage Tool Approval** shows saved tool approvals. Approval controls and filesystem/network sandboxing are separate. [VS Code permissions](https://code.visualstudio.com/docs/agents/run/approvals)

When Agent runs a check, expand the tool result to read the command, working directory, and output. Confirm that it used this repository's source and the selected language environment. An agent's summary of success is only a starting point for verification.

Before granting access, read [permissions, sandboxing, and independent work](../reference/agent-control.md). It explains approval fatigue, saved permissions, the separate terminal sandbox, and requests to leave that sandbox. Manual permissions alone do not enable isolation.

## Account access and models

**Copilot Student** is free for verified students; use the setup page's verification and activation steps. Copilot Free and Student currently use **Auto model selection only**. Other plans provide differing model choices and AI-credit allowances. Check the [current plans](https://docs.github.com/en/copilot/get-started/plans) for access and usage limits; manual model selection is optional for this exercise.

Where available, the model picker changes the session model. **Chat: Manage Language Models** shows configured models and capabilities. Agent work requires tool calling. Record **Auto** when selected, because requests can be routed to different models. [VS Code model selection and routing](https://code.visualstudio.com/docs/agent-customization/language-models)

## Review and commit in VS Code

Open **Source Control → Changes**, inspect each file's diff, and open generated plots in Explorer. The [repository navigation guide](../practices/repo_navigation.md) explains change badges, red/green differences, staging, and local commits. Copilot's chat summary does not replace Git's changed-file list.

## Optional customization

*The following instruction, skill, and reviewer examples were reviewed September 5, 2026. Check the linked support matrix for your client and account before adding them.*

### Try the review skill

Skill access depends on the plan; the current plans page excludes IDE Chat skills from Copilot Free. The lessons work without skill activation: point to the specification and review instructions directly. The included skill is at `.agents/skills/plot-review/`. Ask Copilot to use `plot-review` and check what loads. Other project locations include `.github/skills/` and `.claude/skills/`; personal locations include `~/.copilot/skills/` and `~/.agents/skills/`. See the [folder map](portable-context.md). [Adding Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

### Create a reviewer profile

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

### Check the diff and test results

Read the diff and actual check results. Cloud sessions need separate setup: your local interpreter, files, and personal skills may be unavailable there.
