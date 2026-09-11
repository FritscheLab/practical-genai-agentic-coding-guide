---
layout: default
title: Demo prompts
parent: Teaching
nav_order: 2
---

# Prompts for the workshop

Open Copilot Chat with the **Local** target and keep your language path beside it. Select the listed role before pasting each prompt. The links name the right source files and checks for your language.

| Stage | Copilot role or VS Code view | Python prompt | R prompt |
| --- | --- | --- | --- |
| Setup and baseline | **Agent** | [Shared setup](../setup/vscode-copilot.md) | [Shared setup](../setup/vscode-copilot.md) |
| Orient | **Ask** | [Lesson 1](../paths/python/01-orient.md) | [Lesson 1](../paths/r/01-orient.md) |
| Specify the repair | **Plan** | [Lesson 2](../paths/python/02-specify.md) | [Lesson 2](../paths/r/02-specify.md) |
| Implement the reviewed plan | **Agent** | [Lesson 3](../paths/python/03-implement.md) | [Lesson 3](../paths/r/03-implement.md) |
| Verify the latest source | **Agent** | [Lesson 4](../paths/python/04-verify.md) | [Lesson 4](../paths/r/04-verify.md) |
| Review all saved edits | **Source Control → Changes** | [Lesson 5](../paths/python/05-review.md) | [Lesson 5](../paths/r/05-review.md) |
| Commit locally and hand off | **Staged Changes**, then **Commit** | [Lesson 6](../paths/python/06-handoff.md) | [Lesson 6](../paths/r/06-handoff.md) |

The repository instructions and [figure specifications](../reference/figure-specifications.md) hold the reusable details. Point to those files instead of duplicating their contents. The review skill is optional; participants can follow its checklist directly if skill activation is unavailable.

## Show the evidence

When an approval is unclear, choose **Skip** and ask:

```text
Do not execute yet. Explain this action's purpose, affected files or
destinations, possible external effects, and permission scope.
Propose a narrower action if possible.
```

Use the [permissions guide](../reference/agent-control.md) to compare the answer with the actual request. During the workshop, discuss a hypothetical upload or global-settings request; do not execute it as a demonstration.

During verification, expand the execution result. If the report is unclear, ask:

```text
Show the exact commands, working directory, and results for both checks
against the latest source. Identify any check you could not run.
Do not change the source or tests during this verification.
```

If alternative text is still missing, ask Agent:

```text
Write runs/with-fix/summary.alt.txt following the journal specification.
Check it against the image and report any accessibility checks you cannot do.
Do not change the plotting source.
```

Open the draft in Explorer and review it yourself. Rendering creates only the PNG; alternative text is a separate deliverable.

## Explain a diff

In Source Control, open a changed file and select a section you want to discuss. Switch to **Ask**, attach or reference that source, and ask:

```text
Explain this changed section in terms of the figure specification.
Which lines affect layout, and did any counts or command behavior change?
Do not edit files or run commands.
```

Compare the explanation with the diff. Open new files too. Review the staged snapshot after choosing **+**; typing a commit message does not stage files.

If the repair has grown beyond the task, select **Plan** and ask:

```text
Review this repair for unnecessary complexity. Identify added files,
abstractions, dependencies, and repeated work that the figure brief does
not require. Propose a simpler implementation that preserves behavior,
validation, and accessibility. Do not edit yet or claim speed gains
without measurement.
```

Review the proposal before requesting another implementation. Rerun both checks after simplification. Then close Chat and explain one changed section yourself.

## Leave a handoff

After the local commit, ask:

```text
Write a short handoff with the changes, actual checks and results,
image and alt-text paths, the local commit, and anything unfinished or untested.
Do not push or publish the repository.
```

Follow the language path's identity remedy if Git asks for a name/email. The [Claude Code extension alternative](../platforms/claude-code.md#use-the-vs-code-extension) uses the same prompts with its own Plan/Manual controls. The [CLI appendix](../appendix/command-line.md) provides the command-line equivalents.
