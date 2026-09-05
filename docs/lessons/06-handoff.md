---
layout: default
title: 6. Hand off
parent: Lessons
nav_order: 6
---

# Leave a result someone else can reproduce

Spend the last 10–15 minutes making the work easy to pick up again. Think of a collaborator opening the project next week: what would they need to know to rerun your result or continue where you stopped?

Use the [handoff template](../templates/handoff.md) for a short note covering what you changed, why, what you ran, and what remains unresolved. A person or agent returning later should check that note against the current files and Git state.

Bring forward the relevant details from `tmp/agent-setup.md`: the model and client you used, where the task ran, and any settings that affected it. If you changed models or clients during the exercise, explain the handoff and what you had to reconfigure.

This also helps when a session gets long. Clients may summarize earlier conversation to make room for new work, and a fresh session may not have the same history. Keep the agreed rule and current state in the brief and handoff. When resuming, ask the agent to read those files and inspect the repository before taking the next step. [Context management for longer tasks](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

## Reproduce a run

Run the same inputs and parameters into a new run directory. Compare the output TSV checksums in the two manifests: matching fingerprints mean the files match. Run IDs, timestamps, and paths may differ, while the analysis outputs should agree. The recorded package versions help a collaborator recreate the environment if their result differs.

Look at the manifest's Git state as well. If you ran with uncommitted edits, the recorded revision cannot recover those edits on its own. Commit the reviewed work, then rerun from that revision when you need a result you can refer back to. For published work, keep the required input versions in their approved storage and tell collaborators how to obtain them.

## Review and commit the changes

Stage the implementation, tests, and documentation you want to keep, using `git add` with their specific paths. Then inspect both the staged changes—the ones the commit will include—and any changes left unstaged:

```bash
git diff --cached
git diff
git status --short
git commit -m "Add an auditable implausible-measurement quality gate"
```

Leave `runs/`, `tmp/`, `.venv/`, protected data, and credentials out of the commit. Check that new files such as `src/pgacg/qc.py` are staged; it is easy to overlook a helper that works locally but would be missing from a collaborator's checkout.

Before posting a screenshot, error report, or handoff outside the project, read the actual contents. Names, paths, identifiers, and tokens can appear around an otherwise harmless coding example. Follow your institution's rules for sharing results and acknowledging AI assistance; the [lab data guidance](../reference/lab-data-policy.md) links to U-M's requirements.

## Finish the handoff note

A useful note might read: “The CLI now records the observed implausible fraction and returns 2 when it exceeds the requested maximum. The boundary fixture passed at 20% and failed at 30%; diagnostic outputs remained available. The existing regression suite passed.” Use the actual results from your session and add the commands needed to reproduce them.

Now compare your implementation with the [instructor solution](../lab_meeting/instructor-solution.md). The code may look different and still satisfy the same contract. If the behavior differs, use a small example to understand why before deciding which version to keep.

## Transfer this to your own project

Choose one maintenance task you expect to do again: perhaps adding a validation rule, updating a report, or fixing a join. Write down what should change, work through a small example, and decide how to test it before asking an agent to help.

As the project grows, put recurring conventions in its instructions and repeated procedures in a skill. A subagent can take on an independent piece of work; a connector can provide access to a needed service. The [platform map](../platforms/portable-context.md) helps you carry those choices to another client.
