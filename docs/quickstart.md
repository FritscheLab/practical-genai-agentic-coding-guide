---
layout: default
title: Start here
nav_order: 2
has_children: true
has_toc: false
---

# Choose your language

The default path uses **VS Code + GitHub Copilot**. Keep the guide open alongside VS Code; the [example repository](https://github.com/FritscheLab/practical-genai-agentic-coding-example) includes code, tests, and offline lessons.

Choose the language you already use. Its entry page leads to the detailed [VS Code + Copilot setup](setup/vscode-copilot.md), then the **Next** links take you through six lessons.

{% include path_choices.html %}

You need VS Code, Git, your chosen language, and Copilot access. Setup explains installation, student access, cloning, and the Chat controls. Copilot runs the commands; you review their output and the resulting files. Prepare before a workshop or work at your own pace.

Before granting access, read [permissions and independent work](reference/agent-control.md). Practise evaluating requests, keep the repair understandable, and retain the ability to run and maintain the code without AI assistance.

Prefer Claude Code? Use the short [VS Code extension alternative](platforms/claude-code.md#use-the-vs-code-extension). Prefer a terminal? Follow the complete [CLI appendix](appendix/command-line.md) for Python or R. The exercise and acceptance criteria are the same.

## What you will do

1. In **Agent**, request setup checks and a baseline PNG; open it in Explorer.
2. In **Ask**, understand the plotting code and the overlapping bars and clipped labels.
3. In **Plan**, agree on a repair against the local figure specifications.
4. In **Agent**, implement the repair and rerun both checks against the latest source.
5. Compare the plots and alternative text, then inspect every file in **Source Control → Changes**.
6. Stage reviewed source, make a **local commit**, and leave a handoff with results and unfinished work.

Bookmark your path or current lesson. **Change language** returns to this choice.

## Coming from Part 1

The [Part 1 quickstart](https://fritschelab.org/practical-genai-coding-guide/docs/QuickStart.html) created a base-R function. Here you repair an existing plot using the [exercise brief](lessons/02-specify.md) and local [figure rules](reference/figure-specifications.md).

Use the supplied invented totals. Keep real records outside the workspace and conversations; read the [lab data guidance](reference/lab-data-policy.md) before adapting this to a study.

Teaching a group? Use the [45-minute workshop](lab_meeting/45min_runbook.md), with each participant's setup completed beforehand.
