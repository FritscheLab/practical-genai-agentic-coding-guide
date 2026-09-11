---
layout: default
title: Claude Code
parent: Agent setup
nav_order: 3
description: Help Claude Code read the shared project instructions, then try an optional review skill or reviewer.
---

# Claude Code

The included `CLAUDE.md` points to the shared project instructions. Start there; the skill and separate reviewer below are optional.

**Documentation reviewed: September 5, 2026.** If you need to install or sign in, follow the official [Claude Code quickstart](https://code.claude.com/docs/en/quickstart) for your operating system.

For U-M work, the [Toolkit route](https://its.umich.edu/computing/ai/claude-code-gpt-toolkit) excludes ePHI. Its eligibility wording differs from the [ITS FAQ](https://its.umich.edu/computing/ai/faq), including student access; confirm through the portal or ITS. Follow its configuration instructions and the [lab data guidance](../reference/lab-data-policy.md).

## Use the VS Code extension

*Extension setup and mode controls reviewed September 11, 2026; the optional CLI and customization material below keeps its earlier review date.*

If you prefer Claude Code, keep the same cloned exercise, Python/R environment, Explorer, and Source Control workflow. In **Extensions**, search for **Claude Code** and install Anthropic's extension. Open its Spark icon or use the Command Palette's **Claude Code: Open in New Tab**, then follow browser sign-in. The extension includes its runtime; a separate CLI installation is unnecessary. Use an eligible Claude subscription, Console account, or your institution's supported provider route. [Claude Code extension setup](https://code.claude.com/docs/en/vs-code)

Click the mode indicator below Claude's prompt box and choose **Plan** for orientation and the repair proposal. Reuse the lesson prompts, including the instruction not to edit during orientation. Review the plan, then choose the acceptance option for **manually approving edits** so implementation starts in **Manual** mode. Accepting a plan starts implementation; select manual approval at that decision, before editing begins. These are Claude permission modes; they are separate from Copilot's **Ask/Plan/Agent** roles. [Claude plan approval](https://code.claude.com/docs/en/permission-modes#review-and-approve-a-plan)

Have Claude run setup and verification checks and expand their results. Open the PNGs and alt text in Explorer, then inspect every diff, stage reviewed source, and commit through VS Code **Source Control** just as the lessons describe. Claude's proposed-edit view complements that final Git review. [Extension edit review](https://code.claude.com/docs/en/vs-code#review-changes)

## Optional terminal and customization reference

The sections below describe the terminal-oriented workflow and reusable reviewer tools. They are not prerequisites for the VS Code extension path. Use the [CLI appendix](../appendix/command-line.md) for the exercise's terminal setup and checks.

## First session

1. Complete the [setup for your language path](../quickstart.md), then start an interactive terminal session with `claude --permission-mode plan` from the example repository root. This gives you time to discuss the project before implementing a change. [Claude permission modes](https://code.claude.com/docs/en/permission-modes).
2. Open `CLAUDE.md` and follow its reference to `AGENTS.md`. This short file lets us maintain one shared briefing.
3. Run `/context` to see the memory files, then use the [orientation prompt](index.md#check-the-agents-understanding) to check whether Claude found the expected commands and boundaries.

Claude Code looks for project instructions in `CLAUDE.md` or `.claude/CLAUDE.md`; personal defaults live in `~/.claude/CLAUDE.md`. It does not automatically use `AGENTS.md` in their place. The import below connects the two files. [Claude memory and imports](https://code.claude.com/docs/en/memory).

```markdown
@AGENTS.md
```

In another repository, put that import in root `CLAUDE.md`, outside a code fence. Check that the next session loads both files.

Use `/status` → **Setting sources** to check what loaded: shared `.claude/settings.json`, personal `~/.claude/settings.json`, or project-local `.claude/settings.local.json`. This lesson needs no new settings file. [Claude settings and inspection](https://code.claude.com/docs/en/settings#confirm-what-loaded).

## Choose and record the model

Use `/model`: `s` changes this session; `Enter` also saves the default. Or launch `claude --model MODEL_ID` with a supported identifier. Check `/status` afterward. [Claude model selection](https://code.claude.com/docs/en/model-config).

Aliases such as `opus`, `sonnet`, and `haiku` vary over time and by provider. `opusplan` uses Opus for planning and Sonnet for implementation where allowed. Record the reported models, fallbacks, and `/effort`; say when the exact version is unavailable. [Aliases, routing, and effort](https://code.claude.com/docs/en/model-config).

For a lab gateway, follow its connection instructions and verify model identifiers and features. Anthropic documents routing to Claude models, not arbitrary non-Claude models. [Claude gateway setup and compatibility](https://code.claude.com/docs/en/llm-gateway).

## Discuss the plan before starting edits

Use `/plan` to plan; `Shift+Tab` cycles permission modes. Plan mode can read, explore, and write a plan. Source edits ordinarily wait for approval; bypass-enabled sessions differ. Check the displayed mode. [Claude Plan mode](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode).

Before approving, check the proposed layout changes and tests. Accepting a plan exits Plan mode into the chosen edit-approval mode. Controls differ between terminal, editor, and hosted sessions. [Plan approval and interface controls](https://code.claude.com/docs/en/permission-modes).

Tools perform actions; skills supply procedures. Permissions govern approval, while sandbox settings limit command access. For a reported passing check, find its command and result in the transcript. [Claude tools](https://code.claude.com/docs/en/tools-reference), [permissions and isolation](https://code.claude.com/docs/en/permission-modes#common-setups).

## Try the review skill

Copy the [included skill](https://github.com/FritscheLab/practical-genai-agentic-coding-example/blob/main/.agents/skills/plot-review/SKILL.md) to `.claude/skills/plot-review/` using the [shared instructions](portable-context.md). Restart after creating your first skills directory, invoke `/plot-review`, and check the loaded path. Personal skills use `~/.claude/skills/`. Keep Claude-specific optional fields separate when sharing across clients. [Claude Code skills and change detection](https://code.claude.com/docs/en/skills#live-change-detection).

## Create a reviewer agent

Save this optional role as `.claude/agents/plot-reviewer.md`, or under `~/.claude/agents/` for personal reuse. Its tools permit reading and searching. [Claude subagent configuration](https://code.claude.com/docs/en/sub-agents).

```markdown
---
name: plot-reviewer
description: Review plotting code and its rendered image against the contract.
tools: Read, Grep, Glob
---

Read AGENTS.md and use .agents/skills/plot-review/SKILL.md.
Review the requested diff, image, and alt text against the local figure
specifications. Use supplied test results; do not edit files.
Report findings with source locations and name any checks you could not perform.
```

Ask `Have plot-reviewer review my plotting changes.` Check the transcript for delegation; restart if a newly created agent directory is not detected. Supply the change and test results: the reviewer has its own conversation. [Claude subagents](https://code.claude.com/docs/en/sub-agents).

## Check findings against the diff and tests

This role has no shell tool. Have the implementation session run tests and supply pass/fail results; check findings against the diff. If you change its access, inspect effective permissions too. [Claude instruction and enforcement distinction](https://code.claude.com/docs/en/memory).
