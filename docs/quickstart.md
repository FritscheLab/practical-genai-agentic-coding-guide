---
layout: default
title: Start here
nav_order: 2
has_children: true
has_toc: false
---

# Choose your language

Keep this guide open in your browser. Each setup page downloads the [example repository](https://github.com/FritscheLab/practical-genai-agentic-coding-example), which contains the runnable code, synthetic data, tests, and offline walkthroughs.

Choose the language you are comfortable reading. You will follow its setup, demo, and six lessons from start to finish. Each page gives you the commands and prompts for that language, with a **Next** link to continue.

{% include path_choices.html %}

Both paths use the same synthetic data and exclusion-report exercise. You need Git, a terminal, and only your chosen language. Prepare the environment before a presentation, or follow the steps at your own pace. No model API or credentials are needed to run the demo; you can also complete the exercise manually.

## What you will do

1. Run the baseline and inspect its results.
2. Orient yourself in the repository and set up your coding agent.
3. Work out the exclusion counts from six visible measurements.
4. Implement the change, verify it, and review the diff.
5. Leave a short handoff describing the change, checks, and any unfinished work.

Your path's setup page also lists all six lessons so you can pick up where you left off. Bookmark that page or your current lesson. Use **Change language** on any lesson if you want to return to this choice.

## Coming from Part 1

In the [Part 1 quickstart](https://fritschelab.org/practical-genai-coding-guide/docs/QuickStart.html), you asked an assistant to write a small base-R function. Here you will maintain an existing pipeline that selects a representative BMI measurement after filtering. The [data contract](reference/io_contract.md) explains the teaching rule.

Use the included synthetic files throughout. Keep patient, participant, student, and employee records out of this workspace and its agent conversations. See the [lab data guidance](reference/lab-data-policy.md) before adapting the workflow to a study.

Teaching a group? Use the [45-minute workshop](lab_meeting/45min_runbook.md), with each participant's setup completed beforehand.
