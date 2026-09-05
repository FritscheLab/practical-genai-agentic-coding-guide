---
layout: default
title: 2. Specify
parent: Lessons
nav_order: 2
---

# Work out what the quality gate should do

Before asking for code, spend about 15 minutes working through the rule and a few small examples. These will give you something to check the agent's answer against.

The pipeline currently writes its output files even when many measurements are implausible. We want to keep those files for investigation and also mark the run as failing quality control. The 20% limit below gives us a clear boundary to practice with; choosing a limit for a study would require its own justification.

## Define the quality gate

For this exercise, define the fraction as:

> Number of distinct input rows flagged for `implausible_height` or `implausible_weight`, divided by the number of input EHR rows.

A row with both reasons counts once. Missing values, BMI mismatch, and per-person IQR exclusions do not count toward this gate. The `reasons` column separates reason names with semicolons. Match each name exactly, rather than searching for part of a name. An empty input has fraction `0.0`.

Add `--max_implausible_fraction`, default `0.20`, accepting only finite numbers from `0` through `1`. Fail when the observed fraction is **strictly greater** than the configured maximum. Equality passes.

A failed gate returns exit code `2` after writing the normal outputs, logs, summary, and manifest. Report the observed fraction, configured maximum, and pass/fail outcome in the summary and manifest. Keep exit code `1` for runtime/input errors. The command-line parser, argparse, also uses `2` for invalid CLI syntax, so inspect the run files to distinguish a completed run that fails QC from a rejected command.

Use these exact fields in the manifest so the checker can find the decision:

```json
{
  "status": "success",
  "qc": {
    "observed_fraction": 0.2,
    "max_implausible_fraction": 0.2,
    "outcome": "pass"
  }
}
```

A failed gate uses `status: "qc_failed"` and `outcome: "fail"`. The summary's QC section uses the same three field labels and values. Add these to the existing manifest, keeping its record of the inputs, software, and output file checksums.

## Work these cases yourself

| Input rows | Relevant flagged rows | Limit | Expected fraction | Outcome |
| ---: | --- | ---: | ---: | --- |
| 10 | One height, one weight | 0.20 | 0.20 | Pass |
| 10 | One row with both reasons | 0.20 | 0.10 | Pass |
| 10 | Three different height/weight rows | 0.20 | 0.30 | Fail |
| 10 | Only missing height and BMI mismatch | 0.20 | 0.00 | Pass |
| 0 | None | 0.20 | 0.00 | Pass |

Try explaining the second row to a labmate: two flags on one measurement still mean one excluded input row. Keep these expected answers fixed while implementing. If you want a different method, change the task deliberately before asking for code.

## Write the brief

Use the [task brief template](../templates/task-brief.md) to collect the rule and examples in `tmp/qc-task.md`. Include the files the agent may change: the package, relevant tests, the data contract, and the pipeline runbook. Adding the new CLI flag and summary/manifest fields is part of this task. Adding a dependency or replacing the cleaning method would be a different task.

## Use planning to settle the open questions

This change touches a calculation, the CLI, and saved results, so a short planning conversation is useful. In your client's planning mode, or with an explicit request to inspect without implementing, ask:

```text
Read the task in tmp/qc-task.md and inspect the relevant code and tests.
Explain where the fraction will be calculated, how the CLI will record the
decision before returning, and which tests will check those choices.
Identify any unresolved question that would change the result.
Do not implement the change yet.
```

Read the plan for decisions you can assess. It should explain why a row with two reasons counts once and how a failed gate keeps the run files. A list saying “implement, test, document” has not answered those questions.

The [client setup pages](../platforms/index.md#choose-how-you-want-to-work) show how to enter planning and check its permissions. Some clients let the agent save a plan while restricting implementation edits. Once the method and checks are clear, move to [implementation](03-implement.md). A small wording fix would rarely need this separate planning step.
