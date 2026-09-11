---
layout: default
title: 45-minute workshop
parent: Teaching
nav_order: 1
---

# Repair a plot, from request to handoff

## Prepare

Before the session, participants complete the [VS Code + Copilot setup](../setup/vscode-copilot.md) for [Python](../paths/python/index.md) or [R](../paths/r/index.md). They clone the example through Source Control, sign in to Copilot, and ask **Local → Agent** to prepare the environment, run behavior checks, and save `runs/baseline/summary.png` without changing source.

Confirm that participants can open the baseline PNG in Explorer, locate the **Ask/Plan/Agent** selector, and open an empty **Source Control → Changes** list. Check Copilot access and available allowance before the session. The figure checker must reject the unfinished baseline; behavior tests should pass.

Ask participants to read [permissions and independent work](../reference/agent-control.md). Rehearse explaining an approval's purpose, scope, consequences, and duration. Inspect actual sandbox availability before teaching it; the Manual/Default permission label alone does not mean a sandbox is active.

Facilitators should rehearse the exact language path in a fresh exercise copy. Keep the language environment, Chat tool output, Explorer, and Source Control visible enough for the audience to follow. The exercise uses invented counts; keep study data and logs outside this workspace.

Participants using the [Claude Code extension](../platforms/claude-code.md#use-the-vs-code-extension) can follow the same prompts using its Plan and Manual controls. Terminal users have the [CLI appendix](../appendix/command-line.md). The live demonstration uses Copilot in VS Code.

## Follow along

| Minutes | Activity and visible checkpoint |
| --- | --- |
| 0–5 | Open `runs/baseline/summary.png` in Explorer. Identify overlapping groups and clipped labels. Point out the four Chat controls and explain one approval decision. |
| 5–11 | Select **Ask**. Request a source explanation using Lesson 1. Open the cited plotting function and tests; check the answer against them. |
| 11–17 | Select **Plan**. Read the [fictional JUSF specifications](../reference/figure-specifications.md), send Lesson 2's prompt, and review the proposed layout changes, checks, and need for any added complexity. |
| 17–28 | Hand the reviewed plan to **Agent** using Lesson 3. Observe an edit and expand an execution request or tool result to show what actually ran. |
| 28–35 | In **Agent**, request Lesson 4's fresh verification without further repairs. Inspect both check results, compare the PNGs side by side, and review `runs/with-fix/summary.alt.txt`. |
| 35–41 | Open **Source Control → Changes**. Explain `M`, `U`, and `D`; open every changed/new source file. Read red removals and green additions, then demonstrate the inline/side-by-side switch. Close Chat and have a learner explain one edit and whether its complexity is needed. |
| 41–45 | Stage only reviewed source files with **+**, inspect **Staged Changes**, enter a message, and choose **Commit**. Leave a handoff, identify unfinished checks, and choose one small follow-up task to practise without an agent. |

## During the change

Use the selected path's prompts. Select the actual role each time so learners see how Ask, Plan, and Agent differ. Discuss the plan before starting implementation. Keep **Manual permissions** (**Default permissions** in the captured VS Code 1.137.0 client) and inspect the scope of requested actions; previously approved commands may run without another prompt.

Name **approval fatigue** explicitly: repeated successful requests can make Allow feel like a progress button. Present a hypothetical request to upload the exercise or change global settings, and ask participants to decline it and request a narrower action. Do not issue a real upload or destructive command for this demonstration. Discuss why running outside a sandbox is a separate access decision.

When a plan proposes a generalized pipeline, ask which current requirement needs it and what simpler alternative exists. Passing tests does not establish maintainability or efficiency. Keep useful validation and accessibility work while removing needless architecture.

Behavior tests should pass before and after; the separate figure checker should fail before and pass after. Expanded command results provide evidence of execution. Open the image personally too: checker success does not establish legibility, grayscale readability, or good alternative text. If an agent cannot view images, identify the human visual review explicitly.

In Source Control, explain why `runs/` outputs appear only in Explorer: Git ignores generated images and alt text. Copilot's chat summary can omit unrelated saved edits; the final review covers Git's full changed-file list. Git identity is separate from Copilot sign-in; the handoff lesson supplies a prompt to configure a participant's chosen name/email for this repository only.

The **Commit** action records a local snapshot. **Push**, **Sync**, and **Publish** are outside the workshop exercise.

## If time runs short

Save the current source and outputs and record unfinished checks or review. A local commit is not evidence that a repair passed; do not label an unfinished result verified. Continue from the next lesson at home. If Copilot access runs out, pair with a prepared participant or use the CLI appendix for checks and manual editing.

## Debrief

What did the tests establish? What did opening the image reveal? Did Git's changed-file list match the chat summary? Can you explain every staged change, and could a labmate reproduce the edited plot from the handoff?

Could you maintain this code if AI access became unavailable or prohibited after moving countries or institutions? Keep source, requirements, tests, and instructions independent of the chat. Encourage brief agent-free practice and personal time/spending limits; discuss overreliance as a habit to manage without assuming that every frequent user has lost coding skills.
