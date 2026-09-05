---
layout: default
title: 3. Implement
parent: Lessons
nav_order: 3
---

# Give the agent one change it can finish

You now have a rule and expected answers. Use them to ask for a change you can follow as it takes shape. Allow 20–30 minutes for this part.

Open the repository in your [configured client](../platforms/index.md). If you used planning mode in Lesson 2, use the client's controls to finish planning and begin implementation; approving the plan may make that switch for you. Confirm that it has read `AGENTS.md`, knows the test command, and has access to edit this workspace and run the checks. Then give it this prompt along with the brief you wrote in `tmp/qc-task.md`:

```markdown
Implement the quality gate specified in docs/lessons/02-specify.md.
Read AGENTS.md, REPO_MAP.md, the current CLI and reporting code, and tests first.

Add src/pgacg/qc.py with:
    implausible_fraction(flagged_rows: pandas.DataFrame, n_input: int) -> float
The input flagged_rows has one row per excluded input measurement and a reasons
column of semicolon-separated tokens. Follow the lesson's counting rules.

Add --max_implausible_fraction (default 0.20, finite in [0, 1]) to the CLI.
Write the usual run files before returning 2 on QC failure. Add a QC section to
summary.md and record the decision and threshold in manifest.json.
Preserve the existing failure behavior for bad inputs.

Use the existing dependencies. Update the data contract and runbook.
Add independent unit and CLI tests, including every boundary case in the lesson.
Do not modify examples/qc_gate/check_acceptance.py or the instructor solution.

Report the plan briefly, implement, run the tests and acceptance checker, inspect
the diff, and report commands/results and unresolved issues.
```

## Follow the change as it takes shape

Let the agent choose local variable names and organize the helper function. Keep decisions about the method, output meaning, and access with you. If it proposes a larger rewrite, ask which part of your request needs it. For this exercise, a function that calculates the fraction without reading or writing files, plus a small change to the CLI, should be enough.

Read the changed files while the agent works. It is easier to catch a misunderstanding in a small function than after it has spread through the program. Your brief remains the task: text the agent encounters in data, logs, or retrieved pages does not authorize extra work.

Agent mode lets the assistant choose and carry out several steps: read a file, make an edit, run a check, and use the result to decide what to do next. Follow that feedback. If a test fails, ask whether it exposed a coding error, a setup problem, or an unclear requirement. Keep the lesson's expected answers fixed. The [tool-use guide](../practices/tool_selection.md) walks through what to look for in commands and results.

You do not need to approve every local edit to stay involved. Use the client's permissions to allow the work in the brief, and step in when a new decision affects the method or scope. If the agent discovers a reason the agreed design cannot work, return to that question before continuing with a different design.

If the agent gets stuck, work on the fraction helper first. Once its small tests pass, connect it to the CLI and reporting. When the assistant says it is finished, open [Lesson 4](04-verify.md) and check the result.
