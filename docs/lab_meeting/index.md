---
layout: default
title: Teaching
nav_order: 8
has_children: true
has_toc: false
---

# Repair a plot together

The [45-minute runbook](45min_runbook.md) is a session you can lead with your group. Use the [six short steps](../lessons/index.md) to follow along or continue at home. Choose Python or R and complete the [VS Code + Copilot setup](../setup/vscode-copilot.md) before the session. Have Copilot run the starting checks and render the baseline; use the meeting for reasoning and visual review.

Participants and agents work with a plotting function, invented totals for two groups, rendered images, tests, and local [figure specifications](../reference/figure-specifications.md). The task separates overlapping bars and fixes clipped labels without changing the totals.

- [Runbook](45min_runbook.md): agenda, preparation, and checkpoints.
- [Demo prompts](demo_prompts.md): the Ask → Plan → Agent sequence and visual Git review.
- [Plot-repair exercise](../lessons/02-specify.md): baseline, target, and checks for either language.

To present the [Quarto slides](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/docs/lab_meeting/slide_deck.qmd), run `quarto render docs/lab_meeting/slide_deck.qmd` from a local copy of the [guide repository](https://github.com/FritscheLab/practical-genai-agentic-coding-guide) and open the resulting HTML file. Participants only need the example repository; the guide source is for presenting or editing the slides.

Participants should leave with a readable plot, reviewed alternative text, a source change they understand and have committed locally, actual check results, and a short handoff. The main path uses Chat, Explorer, and Source Control without requiring participants to type shell commands. The [CLI appendix](../appendix/command-line.md) remains available; learners who prefer Claude Code can use its [VS Code extension](../platforms/claude-code.md#use-the-vs-code-extension). Accessibility is part of the task and review from the start.
