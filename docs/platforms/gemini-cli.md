---
layout: default
title: Gemini CLI
parent: Agent setup
nav_order: 6
description: Help Gemini CLI find the shared briefing and try an optional review skill or reviewer.
---

# Gemini CLI

The included `GEMINI.md` imports the shared briefing. Start there; the review skill and separate reviewer below are optional.

**Documentation reviewed: September 5, 2026.** For prerequisites, installation, and sign-in, follow the official [Gemini CLI getting-started guide](https://geminicli.com/docs/get-started/).

## First session

1. Complete the [setup for your language path](../quickstart.md), then launch an interactive session with `gemini --approval-mode=plan` from the example repository root. [Gemini Plan Mode](https://geminicli.com/docs/cli/plan-mode/).
2. Open `GEMINI.md` and follow its import of `AGENTS.md`. This is how Gemini reaches the shared briefing.
3. Run `/memory show`, then send the [orientation prompt](index.md#check-the-agents-understanding). Compare both the loaded context and the answer with the repository files.

Project context uses `GEMINI.md`; personal defaults use `~/.gemini/GEMINI.md`. The included import connects to the shared briefing. After edits, use `/memory reload`. [Gemini CLI context and imports](https://geminicli.com/docs/cli/gemini-md/).

```markdown
@./AGENTS.md
```

Alternatively, set `context.fileName` to choose context filenames. Check the combined context to avoid loading the briefing twice. [Gemini context configuration](https://geminicli.com/docs/cli/gemini-md/).

Inspect `/settings`. Project settings use `.gemini/settings.json`; personal settings use `~/.gemini/settings.json`. Record what applies; no new settings file is needed here. [Gemini settings](https://geminicli.com/docs/cli/settings/).

## Work through the plan together

Use `/plan` or cycle modes with `Shift+Tab`. Default Plan policy allows file inspection and Markdown plans in its designated directory, but no shell commands. Edit a proposed plan with `Ctrl+X`. [Gemini Plan Mode](https://geminicli.com/docs/cli/plan-mode/).

Approving a plan starts implementation with your chosen edit-approval setting; rejection stays in Plan mode. Default and Auto-Edit approve writes differently. Policy controls tool access; sandbox settings separately isolate execution. [Plan approval](https://geminicli.com/docs/tools/planning/), [tool policies](https://geminicli.com/docs/reference/policy-engine/), [sandboxing](https://geminicli.com/docs/cli/sandbox/).

Use an interactive session for this exercise: headless runs can approve plans and proceed without routine tool prompts. [Interactive and headless planning](https://geminicli.com/docs/cli/plan-mode/).

## Choose a model in this client

Use `/model`: **Manual** selects a model; **Auto** routes requests. Or launch `gemini --model MODEL_ID`. Auto can switch Pro planning to Flash implementation; record that routing. The main session's selection does not override subagent models. [Model selection](https://geminicli.com/docs/cli/model/), [planning and model routing](https://geminicli.com/docs/cli/plan-mode/).

Model changes keep Gemini CLI's context and policy setup. Choose the appropriate connection: Google sign-in, Gemini API key, or Vertex AI. A Gemini model in another editor uses that editor's workflow. [Gemini CLI authentication options](https://geminicli.com/docs/get-started/authentication/).

## Try the review skill

Use the included `.agents/skills/plot-review/`. Gemini also supports `.gemini/skills/`, with personal equivalents under `~/.agents/skills/` and `~/.gemini/skills/`. Within one scope, `.agents/skills/` wins name conflicts. See the [folder map](portable-context.md). [Gemini CLI skills](https://geminicli.com/docs/cli/skills/).

Check `/skills list`; use `/skills reload` after edits. Ask for `plot-review`. Activation requests consent to load the body and read bundled resources; check the displayed path. [Gemini skill activation](https://geminicli.com/docs/cli/skills/).

## Create a reviewer agent

Save this optional role as `.gemini/agents/plot-reviewer.md`, or under `~/.gemini/agents/` for personal reuse. It permits `read_file` and `grep_search`. [Gemini CLI subagents](https://geminicli.com/docs/core/subagents/).

```markdown
---
name: plot-reviewer
description: Review plotting code and its rendered image against the contract.
kind: local
tools:
  - read_file
  - grep_search
max_turns: 10
---

Read AGENTS.md and use .agents/skills/plot-review/SKILL.md.
Review the requested diff, image, and alt text against the local figure
specifications. Use supplied test results; do not edit files.
Report findings with source locations and name any checks you could not perform.
```

Find the role with `/agents`, then start a request with `@plot-reviewer`. Supply the change and test results. Subagents are currently enabled by default; check your version's documentation if it is missing. [Gemini subagent management](https://geminicli.com/docs/core/subagents/).

Leave Plan mode before trying this custom reviewer: its default policy allows the built-in research agents, while additional roles need an explicit policy. [Gemini planning tools and custom agents](https://geminicli.com/docs/cli/plan-mode/).

## Compare the review with code and tests

This role cannot run shell commands. Supply actual test results, then compare its findings with the diff and image. Perform visual checks yourself if its tools cannot show images.
