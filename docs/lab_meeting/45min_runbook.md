---
layout: default
title: 45-minute workshop
parent: Teaching
nav_order: 1
---

# 45-minute lab workshop

## Prepare before the meeting

Follow [Start here](../quickstart.md), install and sign in to an [approved coding client](../platforms/index.md), and run the baseline tests and demo. Participants can use different clients and models; comparing how those setups use the same repository is part of the meeting. Prepare at least two setups across the group if available. The instructor should also run `python examples/qc_gate/verify_solution.py`. Keep the solution available as a fallback; do not place its files into the learner's baseline.

Use the synthetic fixtures throughout, and check open terminals and shared screens for PHI, PII, or keys before the meeting. Follow the [lab data policy](../reference/lab-data-policy.md): approval depends on the service, account, and data as well as the chosen model.

For a new participant environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest
```

Use the Windows activation command in Start here when appropriate. Render the Quarto slides in advance if using them. Participants without authorized assistant access can complete the exercise manually and compare the published client setup instructions.

For Claude Code through U-M GPT Toolkit, check the [current ITS eligibility guidance](https://its.umich.edu/computing/ai/faq) and your access in the university portal before the session. Each participant must use their own authorized account and token; do not share them.

Check how your client offers explanation, planning, and implementation. We use **Ask** for orientation, **Plan** when a method or implementation choice needs discussion, and **Agent** to edit and run checks once those choices are settled. Labels differ across clients; an explicit request can describe the same intent. Check workspace and tool permissions separately so participants know what the agent can access.

## Agenda

| Minutes | Activity | Learner checkpoint |
| --- | --- | --- |
| 0–5 | Connect Part 1's reviewed task to Part 2's working repository. | Explain the intended change. |
| 5–12 | Select and record the client/model, inspect its setup, and compare the same Ask request across participants. | Identify the instructions and skill it found, then check the files cited in its explanation. |
| 12–20 | Work the QC cases in [Lesson 2](../lessons/02-specify.md); use Plan to resolve open choices before editing. | Explain why exactly 20% passes and both reasons count once. |
| 20–32 | Use Agent to implement the agreed change and run checks. | Inspect changed files; return to discussion if a new method decision appears. |
| 32–40 | Run acceptance checks and review the diff. | Distinguish expected QC failure from runtime failure. |
| 40–45 | Write a short handoff and debrief. | State what was verified and what remains uncertain. |

## Compare the setups during orientation

Have participants open the model selector or session information and record their client, selected model, and whether the session runs locally or remotely. Choose the model at runtime; the repository's `.codex/config.toml` shares access settings without fixing a model for everyone.

Open `AGENTS.md`, `.codex/config.toml`, and `.agents/skills/pipeline-review/SKILL.md` together. The Codex settings and review skill are included in the repository. Use each [client's setup page](../platforms/index.md) to check which files it discovers and which settings apply; a shared repository does not give every client the same configuration.

In pairs, each using your own authorized account, send the same explanation-only prompt from [Lesson 1](../lessons/01-orient.md), then compare the files actually loaded, the commands reported, and the code cited in each answer. Record which parts of the setups differ so you can interpret the comparison. Without a second authorized setup, compare your observations with the published client instructions. Keep installation and sign-in out of these seven minutes; spend them checking how the prepared setups behave.

## Add the quality gate

Add the quality gate specified in [Lesson 2](../lessons/02-specify.md). This is intentionally absent from the baseline. The mismatch threshold and category tables already exist; they are useful orientation examples, not implementation tasks.

Before using the [implementation prompt](../lessons/03-implement.md), have participants explain the counting rule and agree where the fraction and QC decision belong. Use a planning conversation if those choices are still unclear. Once they are settled, let the agent edit and test, then run:

```bash
python -m pytest
python examples/qc_gate/check_acceptance.py
```

Show a passing case, equality at the maximum, and a completed run that fails QC while retaining outputs. Have participants inspect the summary and manifest themselves.

## If the live change does not finish

A live coding session sometimes ends with an unfinished change. Save the failing case and your best explanation, then use the isolated [instructor solution](instructor-solution.md) to show the expected behavior. Keep the original expected answers visible so everyone can see what still needs work. Participants can continue from their handoff afterward.

## Debrief

Ask participants to point to a file that helped them understand the code and a test that could catch a mistake. Compare what their chosen models and clients loaded or explained differently. Discuss when they needed an explanation or plan, when they allowed edits, and what they checked themselves. If a reviewer agent was used, identify what it found and what still required human judgment.
