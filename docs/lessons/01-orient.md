---
layout: default
title: 1. Orient
parent: Lessons
nav_order: 1
---

# Get to know the project and your agent

Spend 20–30 minutes getting your bearings after the [Python setup](../quickstart.md). You will prepare one model and client to work in the repository, check what it can see and do, and trace a small part of the pipeline. Comparing setups with a labmate is part of the exercise.

## Choose a model and a way to work with it

For university work, choose a service and account permitted for the task and its data. Access to a model is only part of that decision. Read the [lab data guidance](../reference/lab-data-policy.md), then keep this exercise entirely synthetic. Check what is visible in your editor and terminal before sharing them with a partner or an agent.

Start with one coding tool you have access to. Follow its setup page through sign-in, model selection, project configuration, and instruction discovery: [Codex](../platforms/codex.md), [Claude Code](../platforms/claude-code.md), [Copilot](../platforms/copilot.md), [Cursor](../platforms/cursor.md), or [Gemini CLI](../platforms/gemini-cli.md). Select an available model that supports the tools needed for editing and running checks. Use the model name shown by the client; do not rely on the assistant guessing its own identity.

A model and a client are two choices. For example, choosing a Claude model inside Copilot keeps Copilot's setup and tools. Opening Claude Code brings its own settings, permission modes, and instruction discovery. Account access, supported model features, and execution location can change too. The [folder map](../platforms/portable-context.md#know-which-folder-you-are-changing) helps you connect those choices to actual files.

If you do not have authorized access to an assistant, inspect the included configuration and work through the comparison below on paper. You can complete the code exercise manually. Keep accounts and API tokens personal; a labmate's access does not automatically extend to you.

## Make the project setup concrete

Open the root `AGENTS.md`, then the files your client uses. For Codex, that includes `.codex/config.toml`, `.codex/agents/pipeline-reviewer.toml`, and `.agents/skills/pipeline-review/SKILL.md`. For Claude Code, follow the `CLAUDE.md` import and the documented skill copy step. Use the corresponding paths on the other client pages. Read the contents before accepting project trust or adding configuration to another repository.

Explain these three pieces to a labmate: where the project conventions live, where the client gets its settings, and where it discovers a review procedure. Then inspect the client's active model, mode, and permissions. A settings file may be overridden or skipped; the effective setup is what matters.

Keep a short note in `tmp/agent-setup.md` with the client/version, selected model and provider, local or hosted execution, mode and permissions, and the instruction/configuration/skill paths you confirmed. If you are using defaults without a project settings file, say so. Record automatic model routing if enabled. Leave out credentials and account identifiers. You will return to this note when reviewing and handing off the change.

Include the data boundary in that note: this exercise uses synthetic fixtures, and study records stay elsewhere. Before adding a connector or another workspace folder, check what information it would expose and whether the permitted use covers that route.

## Check the agent's understanding of the code

Read `README.md`, `AGENTS.md`, `REPO_MAP.md`, and the [data contract](../reference/io_contract.md). Then open `src/pgacg/cli.py`, `src/pgacg/cleaning.py`, and one test. Follow `mismatch_threshold` from the command-line argument into the cleaning function and the run summary. This gives you a small, concrete path through the program.

Ask the assistant to explain that same project to you:

```markdown
Read AGENTS.md and REPO_MAP.md, then inspect the CLI, cleaning implementation,
data contract, and tests. Explain:
- how to run the included synthetic example;
- how a representative measurement is selected;
- where the input data, code, and run outputs live;
- which existing test checks actual expected records.
Point to the files you inspected. Do not edit anything yet.
```

Open the files it names and check its explanation. If a path does not exist or the explanation skips an important rule, point that out now. Find `pipeline-review` in the client's skill list or invoke it as described on its setup page. Confirm the loaded path. Discovery shows that the procedure is available; [Lesson 5](05-review.md) will use it to review an actual change.

## Compare with another setup

If another model is available in the same client, start a fresh session, select it, and repeat the orientation prompt from the same repository state. Keep the mode and permissions the same where possible. Compare which files it inspected, whether it found the real commands, and what you had to correct. Record any setting the client changed automatically. One short task gives you an observation to discuss, not a model ranking.

Now compare your setup note with a labmate using a different client, or use the folder map if you are working alone. Work through these cases:

| Change | What you should recheck |
| --- | --- |
| Choose a different model in the same client | Model availability, reasoning or routing options, and supported tools; the client's project-file conventions still apply. |
| Move from Codex to Claude Code | The `CLAUDE.md` import, `.claude/` settings and skill discovery, and that session's permissions; `.codex/config.toml` does not configure Claude Code. |
| Move the task from a local session to a hosted agent | Available files, environment setup, credentials, skills, and execution limits in the hosted environment. |

The task's counting rule and expected answers should survive each move. The setup needed to carry out the task may change. Add one difference you found to your note.

## Trace one person's records

Choose one synthetic person ID in the example TSVs and find that person's rows in the cleaned and flagged files. Can you explain why one encounter was selected and another was excluded? If you get stuck, read the relevant rule in the contract alongside the code that applies it.

The [data reference](../reference/synthetic-data.md) explains how these teaching records were generated. Our small pipeline applies fixed filtering and category rules across that input, including minors. Keep that scope in mind if you compare it with Part 1's more advanced adult-cohort analysis.

## Save your starting point

```bash
git status --short
git switch -c exercise/qc-gate
```

The new branch gives this exercise its own line of work. Put the baseline run ID and test result in a short note under `tmp/` so you can find them later.

Check `git status` again after running the pipeline: run folders and the virtual environment should stay ignored. Remember that `.gitignore` only controls Git tracking. The agent's workspace and tool permissions determine what it can access.

Once you can explain your agent's setup and find the cleaning rule, its tests, and your baseline output, move on to [Lesson 2](02-specify.md).
