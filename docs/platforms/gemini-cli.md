---
layout: default
title: Gemini CLI
parent: Agent setup
nav_order: 6
description: Help Gemini CLI find the shared briefing and try an optional review skill or reviewer.
---

# Gemini CLI

The repository’s `GEMINI.md` file imports the shared project briefing, so you can begin with that setup. Use the optional skill and reviewer examples later if you want to make review a repeatable part of your work.

**Documentation reviewed: September 5, 2026.** For prerequisites, installation, and sign-in, follow the official [Gemini CLI getting-started guide](https://geminicli.com/docs/get-started/).

## First session

1. Complete the [Python quickstart](../quickstart.md), then launch an interactive session with `gemini --approval-mode=plan` from the repository root. [Gemini Plan Mode](https://geminicli.com/docs/cli/plan-mode/).
2. Open `GEMINI.md` and follow its import of `AGENTS.md`. This is how Gemini reaches the shared briefing.
3. Run `/memory show`, then send the [orientation prompt](index.md#check-the-agents-understanding). Compare both the loaded context and the answer with the repository files.

Gemini CLI uses `GEMINI.md` as its default project context file; personal defaults live at `~/.gemini/GEMINI.md`. The import below lets that project file refer to the shared briefing. After changing a context file, use `/memory reload` so the session sees the update. [Gemini CLI context and imports](https://geminicli.com/docs/cli/gemini-md/).

```markdown
@./AGENTS.md
```

You can also choose context filenames through `context.fileName` in settings. This repository already has the import it needs. If you choose the settings approach for another project, check the combined context so you do not load two copies of the same briefing. [Gemini context configuration](https://geminicli.com/docs/cli/gemini-md/).

Use `/settings` to inspect the settings dialog for your setup note. Project settings belong in `.gemini/settings.json`, while personal settings live in `~/.gemini/settings.json`. You can use the defaults for this lesson without creating a project settings file. Record any existing project settings and the choices shown in the session. [Gemini settings](https://geminicli.com/docs/cli/settings/).

## Work through the plan together

Use `/plan` for a planning request, or `Shift+Tab` to cycle modes. With the default Plan policy, Gemini can inspect files and write Markdown plans in its designated plans directory; shell commands are outside the allowed tool set. This is a useful place to settle the QC examples. You can edit the proposed plan with `Ctrl+X`. [Gemini Plan Mode](https://geminicli.com/docs/cli/plan-mode/).

When the interactive session presents a plan, approving it starts implementation with your chosen edit-approval setting; rejecting it keeps the discussion in Plan mode. Default and Auto-Edit differ in which writes need confirmation, and policy rules can change tool access. Sandboxing has separate settings for isolating tool execution. [Plan approval](https://geminicli.com/docs/tools/planning/), [tool policies](https://geminicli.com/docs/reference/policy-engine/), [sandboxing](https://geminicli.com/docs/cli/sandbox/).

Use an interactive session for this exercise: headless runs can approve plans and proceed without routine tool prompts. [Interactive and headless planning](https://geminicli.com/docs/cli/plan-mode/).

## Choose a model in this client

Run `/model` to open the model dialog. Choose **Manual** to select a specific available model, or **Auto** to let Gemini CLI route requests. You can also select a model at startup with `gemini --model MODEL_ID`, replacing `MODEL_ID` with an available identifier. With Auto, an approved plan can move the main session from a Pro model during planning to a Flash model for implementation. Record that routing choice when comparing results. The main session's `/model` choice does not override subagent models. [Model selection](https://geminicli.com/docs/cli/model/), [planning and model routing](https://geminicli.com/docs/cli/plan-mode/).

Changing the Gemini model keeps Gemini CLI's context files, skills, and policy setup in place. Google sign-in, a Gemini API key, and Vertex AI are different ways to connect this client; use the one appropriate to your account and lab environment. A colleague using a Gemini model inside another editor is using that editor's configuration and tool workflow. Compare models within one client first, then revisit the setup if you switch clients. [Gemini CLI authentication options](https://geminicli.com/docs/get-started/authentication/).

## Try the review skill

The [pipeline-review skill](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/.agents/skills/pipeline-review/SKILL.md) is already in `.agents/skills/pipeline-review/`. Gemini CLI also supports `.gemini/skills/`, with personal locations under `~/.agents/skills/` and `~/.gemini/skills/`. Use the included copy: within the same scope, `.agents/skills/` takes precedence when names conflict. See the [folder map](portable-context.md) when adapting the setup. [Gemini CLI skills](https://geminicli.com/docs/cli/skills/).

Run `/skills list` to check that Gemini found it, and `/skills reload` after making changes. Then ask for a review using `pipeline-review`. The documented activation flow asks for consent before loading the skill body and allowing reads of its bundled resources. Check the displayed path so you know which copy you are accepting. [Gemini skill activation](https://geminicli.com/docs/cli/skills/).

## Create a reviewer agent

If you want a separate review conversation, save the following as `.gemini/agents/pipeline-reviewer.md`. It uses the documented local-agent format and limits tools to `read_file` and `grep_search`. For a personal role across projects, use `~/.gemini/agents/`. [Gemini CLI subagents](https://geminicli.com/docs/core/subagents/).

```markdown
---
name: pipeline-reviewer
description: Inspect the synthetic pipeline for documented contract violations.
kind: local
tools:
  - read_file
  - grep_search
max_turns: 10
---

Read AGENTS.md and docs/reference/io_contract.md.
Review the requested code and tests without editing files.
Return findings with file locations, a minimal synthetic example,
and the expected result. State which checks remain unverified.
```

Run `/agents` to find the role, then start a prompt with `@pipeline-reviewer` to send it a review request. Include the behavior you want checked and the files it should read. Current documentation says subagents are enabled by default; if the role does not appear, check the documentation for your installed version. [Gemini subagent management](https://geminicli.com/docs/core/subagents/).

Leave Plan mode before trying this custom reviewer: its default policy allows the built-in research agents, while additional roles need an explicit policy. [Gemini planning tools and custom agents](https://geminicli.com/docs/cli/plan-mode/).

## Compare the review with actual outputs

The reviewer above cannot run shell commands, so have the implementation session run the checks and share their results. Compare the final diff, selected records, and flagged-row counts with the lesson’s expected answers. Keep sign-in details and personal overrides outside the repository when sharing your setup.
