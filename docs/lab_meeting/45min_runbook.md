---
layout: default
title: 45-minute workshop
parent: Teaching
nav_order: 1
---

# Repair a plot, from request to handoff

## Prepare

Before the session, participants download the [example](https://github.com/FritscheLab/practical-genai-agentic-coding-example), complete [Python](../paths/python/index.md) or [R setup](../paths/r/index.md), and prepare an approved [coding client](../platforms/index.md). Run tests and save `runs/baseline/summary.png`.

Open the [exercise and target](../lessons/02-specify.md): two invented groups overlap and long labels are clipped. The task repairs that layout for a fictional journal.

Keep study data and logs outside this teaching workspace.

## Follow along

| Minutes | Activity |
| --- | --- |
| 0–5 | Open the baseline plot. Identify overlapping groups and clipped labels. |
| 5–12 | Ask the agent to explain the plotting functions, layout settings, and tests. Check the source files it names. |
| 12–17 | Compare the baseline with the target. Read the fictional JUSF specifications: grouped bars, exact dimensions, typewriter text, purple/lime groups, legend, and value labels. |
| 17–30 | Use the chosen path's implementation prompt. Watch the source change and ask about anything unclear. |
| 30–40 | Render the repaired PNG, run both checks, review contrast and grayscale readability, and write/review `runs/with-fix/summary.alt.txt`. |
| 40–45 | Write a short handoff: what changed, what was checked, and what remains. |

## The example

The [exercise table](../lessons/02-specify.md) fixes the values; the [figure specifications](../reference/figure-specifications.md) fix the format. Point the agent there.



## During the change

Use your language path's prompts. Ask about source and tests before edits; plan only if needed. Check actual file and command permissions.

Behavior tests should pass before and after; the strict figure checker should fail before and pass after. Open the image and diff too. If the agent cannot view images, a person performs that check.

Review contrast, grayscale readability, and `runs/with-fix/summary.alt.txt` against the figure specification. The plotting CLI does not create alt text.

## If time runs short

Save the source, latest image, commands, and unfinished work. Participants can continue from that handoff at home.

## Debrief

What did the tests establish? What did opening the image reveal? Could a labmate reproduce the edited plot from the handoff?
