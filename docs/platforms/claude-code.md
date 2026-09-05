---
layout: default
title: Claude Code
parent: Agent setup
nav_order: 3
description: Help Claude Code read the shared project instructions, then try an optional review skill or reviewer.
---

# Claude Code

This repository already includes a `CLAUDE.md` file that points Claude Code to the shared project instructions. You can start the lessons with that setup; the review skill and separate reviewer below are optional.

**Documentation reviewed: September 5, 2026.** If you need to install or sign in, follow the official [Claude Code quickstart](https://code.claude.com/docs/en/quickstart) for your operating system.

For U-M work, check the [Claude Code via U-M GPT Toolkit route](https://its.umich.edu/computing/ai/claude-code-gpt-toolkit), which explicitly excludes ePHI. Eligibility wording differs between that service page and the [ITS FAQ](https://its.umich.edu/computing/ai/faq), including student access. Confirm your eligibility through the Toolkit portal or ITS support, then follow the portal's configuration instructions if that is your approved route. The [lab data guidance](../reference/lab-data-policy.md) explains why service access and data approval need separate checks.

## First session

1. Complete the [Python quickstart](../quickstart.md), then start an interactive terminal session with `claude --permission-mode plan` from the repository root. This gives you time to discuss the project before implementing a change. [Claude permission modes](https://code.claude.com/docs/en/permission-modes).
2. Open `CLAUDE.md` and follow its reference to `AGENTS.md`. This short file lets us maintain one shared briefing.
3. Run `/context` to see the memory files, then use the [orientation prompt](index.md#check-the-agents-understanding) to check whether Claude found the expected commands and boundaries.

Claude Code looks for project instructions in `CLAUDE.md` or `.claude/CLAUDE.md`; personal defaults live in `~/.claude/CLAUDE.md`. It does not automatically use `AGENTS.md` in their place. The import below connects the two files. [Claude memory and imports](https://code.claude.com/docs/en/memory).

```markdown
@AGENTS.md
```

If you bring this pattern to another repository, put that line in its root `CLAUDE.md`, outside a code fence. In the next session, check that Claude loaded the imported instructions as well as `CLAUDE.md` itself.

For your setup note, open `/status` and inspect **Setting sources**. Shared project settings can live in `.claude/settings.json`; personal settings use `~/.claude/settings.json`, and `.claude/settings.local.json` holds local project overrides. This lesson can use the defaults without creating a project settings file. Record which sources actually loaded. [Claude settings and inspection](https://code.claude.com/docs/en/settings#confirm-what-loaded).

## Choose and record the model

Open `/model` to see your available choices. In the current CLI picker, `s` changes the model for this session; `Enter` saves it as your default too. For a separate trial, launch `claude --model MODEL_ID`, replacing `MODEL_ID` with a supported identifier. Check `/status` after selection. This changes the model within Claude Code, so the project still uses `CLAUDE.md` and Claude's tool controls. [Claude model selection](https://code.claude.com/docs/en/model-config).

Aliases such as `opus`, `sonnet`, and `haiku` can resolve to different versions over time and across providers. `opusplan` requests Opus for planning and Sonnet for implementation, subject to availability and policy. Record both the configured choice and the model reported in each phase, including any fallback. If the exact version is not exposed, say so. Record the selected `/effort` level where supported too. [Aliases, routing, and effort](https://code.claude.com/docs/en/model-config).

Changing the endpoint changes where requests go. If your lab uses a gateway, follow its connection instructions and confirm its model identifiers and supported features. Anthropic's gateway documentation supports routing to Claude models; it does not support substituting arbitrary non-Claude models. A colleague using another model family may need a different client and configuration. [Claude gateway setup and compatibility](https://code.claude.com/docs/en/llm-gateway).

## Discuss the plan before starting edits

In the terminal, `/plan` starts a planning request and `Shift+Tab` cycles permission modes. Plan mode can read files, run exploration commands, and write a plan. Under ordinary settings, source edits wait for plan approval; sessions launched with bypass permissions available have different restrictions. Check the displayed mode when returning to an existing session. [Claude Plan mode](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode).

Before approving, work through one example together: if the flagged fraction equals the threshold, what should happen? Then select how implementation edits should be approved. Accepting the plan exits Plan mode into that permission mode. Mode names and controls differ across the terminal, editor, and hosted sessions. [Plan approval and interface controls](https://code.claude.com/docs/en/permission-modes).

Claude’s `Read`, `Edit`, and `Bash` tools serve different purposes. A skill supplies a procedure that uses available tools; it does not automatically grant new access. Permission settings govern approval, and sandbox settings govern what a running command can reach. When Claude reports a passing check, look for the command and result in the transcript. [Claude tools](https://code.claude.com/docs/en/tools-reference), [permissions and isolation](https://code.claude.com/docs/en/permission-modes#common-setups).

## Try the review skill

Copy the [included skill](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/.agents/skills/pipeline-review/SKILL.md) from `.agents/skills/pipeline-review/` to `.claude/skills/pipeline-review/` using the [shared setup instructions](portable-context.md). If this creates your first `.claude/skills/` directory, restart Claude before invoking `/pipeline-review` or asking for a matching task. Check the loaded path. Personal skills live under `~/.claude/skills/`. Claude Code supports the Agent Skills format and adds optional fields of its own; keep those additions separate if you share the skill with colleagues using other clients. [Claude Code skills and change detection](https://code.claude.com/docs/en/skills#live-change-detection).

## Create a reviewer agent

A separate reviewer can be helpful once you have a change ready to discuss. To try one, save the following as `.claude/agents/pipeline-reviewer.md`. Its `tools` list allows reading and searching, so the reviewer can inspect the work without editing it. For a personal role used across projects, the same format can live under `~/.claude/agents/`. [Claude subagent configuration](https://code.claude.com/docs/en/sub-agents).

```markdown
---
name: pipeline-reviewer
description: Review synthetic pipeline behavior against its documented contract.
tools: Read, Grep, Glob
---

Read AGENTS.md and docs/reference/io_contract.md.
Inspect the requested code and tests without editing files.
Report each discrepancy with a file location, a minimal synthetic example,
and the expected result. State what you could not verify.
```

Ask Claude to delegate the review to `pipeline-reviewer`, then look for that delegation in the transcript. If the role does not appear after you create the first agent directory, restart the session. Include the task’s important constraints in the review request: the reviewer has a separate conversation and may not know what you agreed with the main agent. [Claude subagents](https://code.claude.com/docs/en/sub-agents).

## Check findings against the diff and tests

The reviewer above cannot run pytest because it has no shell tool. Have the implementation session run the tests and share the results with it. Then compare its findings with the diff and the example inputs. If you change the role’s access later, check the tool and permission settings too; memory files provide instructions, while those settings control what it can do. [Claude instruction and enforcement distinction](https://code.claude.com/docs/en/memory).
