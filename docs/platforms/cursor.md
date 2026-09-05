---
layout: default
title: Cursor
parent: Agent setup
nav_order: 5
description: Start a lesson in Cursor with the shared project instructions, then add review tools if they help.
---

# Cursor

Cursor can read the repository’s `AGENTS.md` directly, so the first lesson needs little extra configuration. Start in a local repository session, where you can check the Python environment and open each changed file.

**Documentation reviewed: September 5, 2026.** If you need to install Cursor or set up an account, follow its [quickstart](https://cursor.com/docs/get-started/quickstart).

## First session

1. Open this repository in Cursor and complete the [Python quickstart](../quickstart.md) in its terminal. This gives you a known working environment for the agent to use.
2. Open the Agent panel, choose **Ask** in its mode picker, and send the [orientation prompt](index.md#check-the-agents-understanding).
3. Check the instruction sources and compare the reported entrypoint and commands with the files you just used.

Cursor supports a root `AGENTS.md` for project guidance, which is what this repository uses. If you later need rules for particular files, put them in `.cursor/rules/*.mdc`; the rules system ignores plain `.md` files in that directory. Personal rules are managed in Cursor’s settings. [Cursor rules](https://cursor.com/docs/rules).

For those more specific rules, Cursor’s rule editor can create the `.mdc` file. Check its `description`, `globs`, and `alwaysApply` settings, then try opening files that should and should not use the rule. That is a useful rehearsal before sharing it in a workshop.

## Ask, plan, or implement

Use the Agent panel's mode picker, or **Shift+Tab** in the chat input, to choose how you want to work. **Ask** helps you read and understand the repository without editing files. **Agent** can search the code, change files, and run terminal commands. Its edits appear as it works, so open the diff to see what changed; use **Stop** if the work heads away from your task. [Ask mode](https://cursor.com/help/ai-features/ask-mode), [Agent behavior](https://cursor.com/help/ai-features/agent).

Choose **Plan** when you want to settle the approach before changing several files. Cursor researches the repository and proposes a plan you can revise before selecting **Build**. Use **Save to workspace** if you want to keep that plan with the project; plans otherwise start in your home directory. A small, well-understood change can go directly to Agent. [Plan mode](https://cursor.com/docs/agent/plan-mode).

Check **Settings → Agents → Approvals & Execution** before handing over implementation. These execution controls are separate from Ask, Plan, and Agent. **Auto-review**, the current default, combines allowlists, shell sandboxing where possible, and a model's assessment of other calls. It can approve actions automatically and can make mistakes. **Allowlist** gives you explicit rules for repeat actions; an empty allowlist is the documented replacement for the retired Ask Every Time setting. **Run Everything** runs all calls automatically without sandboxing or a classifier. These controls apply to local agents; cloud agents use a different execution environment. [Run Modes](https://cursor.com/docs/agent/security/run-modes).

## Choose a model in this client

Open the **model selector in the chat or Agent panel** and choose from the models available to your account. Your plan and team settings can affect that list. Selecting a model from another provider keeps you in Cursor, using Cursor's rules, skills, and execution controls. For a comparison, keep those settings and the task fixed. If you choose **Auto**, record that choice: the routed model can vary between requests, and team settings may hide its identity. [Cursor model selection and availability](https://cursor.com/help/models-and-usage/available-models).

You do not need a provider API key to try the models included with your Cursor access. Bringing your own key is a separate option under **Cursor Settings → Models**, with provider-specific support limits. It supports documented chat models; it does not make every API model or feature available, and Tab completion keeps using Cursor's built-in models. If you instead move to Claude Code, Codex, or Gemini CLI, follow that client's setup even when the model family is familiar. [Cursor API key support](https://cursor.com/help/models-and-usage/api-keys).

## Try the review skill

The shared review skill is already in `.agents/skills/pipeline-review/`. Ask Agent to use `pipeline-review` and check the instructions it loads. Cursor also supports `.cursor/skills/`; personal skills can live under `~/.agents/skills/` or `~/.cursor/skills/`. Use the included copy for this project. The [folder map](portable-context.md) explains where each part of the setup belongs. [Cursor skills](https://cursor.com/docs/skills).

If you move the task to a cloud or remote environment, check which skills are available there. Personal skills do not automatically appear everywhere; Cursor documents additional synchronization or packaging requirements. Keeping a skill in the repository makes the version you intend to share easier to identify. [Cursor skill locations and remote availability](https://cursor.com/docs/skills).

## Create a reviewer agent

To give review its own role, save the following as `.cursor/agents/pipeline-reviewer.md`. The `readonly: true` setting restricts writes, while `model: inherit` uses the main agent’s selected model. A personal role used across projects can live under `~/.cursor/agents/`. [Cursor subagents](https://cursor.com/docs/subagents).

```markdown
---
name: pipeline-reviewer
description: Check the synthetic pipeline against its contract and test evidence.
model: inherit
readonly: true
---

Read AGENTS.md and docs/reference/io_contract.md.
Inspect the requested code and tests without editing files.
Report each discrepancy with a file location, a minimal synthetic example,
and the expected behavior. Identify checks you could not perform.
```

Ask Agent to delegate a specific review to this role, then read its findings alongside the changed code. A question such as “Does the quality gate count a row with both reasons only once?” gives the reviewer something concrete to check. For a short single-file exercise, the main agent may be enough; separate agents also take time to start and coordinate. [Cursor subagent tradeoffs](https://cursor.com/docs/subagents).

## Check the interpreter and test results

Check that the implementation session used the intended Python interpreter and ran the repository checks. The reviewer should say which checks it could not perform. Read each changed file before accepting the work. If you try another model, keep the task brief and acceptance cases the same so you can make a useful comparison.
