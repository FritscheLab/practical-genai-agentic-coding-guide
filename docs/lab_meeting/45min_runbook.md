---
layout: default
title: 45-minute workshop
parent: Teaching
nav_order: 1
---

# A small change, from request to handoff

## Prepare

Have participants keep the guide open online and download the [example repository](https://github.com/ilarsf/practical-genai-agentic-coding-example). Choose the [Python path](../paths/python/index.md) or [R path](../paths/r/index.md). Run its setup, tests, and six-row example before the presentation. Prepare an approved [coding client](../platforms/index.md). Use synthetic files throughout.

Open the [six-row example and expected report](../lessons/02-specify.md). Find measurements d, e, and f in the input and `outputs/flagged_rows.tsv` so you can help participants check their counts.

## Follow along

| Minutes | Activity |
| --- | --- |
| 0–5 | Open the six input rows and baseline output. Find the three excluded measurements. |
| 5–12 | Ask the agent to explain where cleaning and reporting happen. Check the files it names. |
| 12–17 | Show the desired report: 3 of 6 excluded, missing height 2, missing weight 2. Explain the overlap. |
| 17–30 | Use the chosen path's implementation prompt. Watch the change and ask about anything unclear. |
| 30–40 | Run the example and existing tests. Read the summary and inspect the diff. |
| 40–45 | Write a short handoff: what changed, what was checked, and what remains. |

## The example

The [six-row table](../lessons/02-specify.md) fits on one screen. Measurements d/e/f are excluded; f lacks both height and weight. The task adds a readable summary of these existing decisions. Cleaning and record selection stay the same.

Use the complete-data file next. Its report should show no exclusions. Different wording and code can produce the same useful result.

## During the change

Use the prompts in the participant's language path. Ask for an explanation before edits, a short plan if needed, and implementation once the request is clear. Check the client's actual file and command permissions separately.

Existing tests help catch regressions. Reading the report checks whether the improvement makes sense. Reviewing the diff checks whether the agent changed more than requested. These are complementary habits learners can reuse in their own repositories.

## If time runs short

Save the current state and any failing command. Use the [expected report](../lessons/02-specify.md#describe-the-improvement) and the flagged rows to discuss what remains, and leave a short handoff so participants can continue at home.

## Debrief

What did you check yourself? What did the agent help you find? What would a labmate need to continue this work tomorrow?
