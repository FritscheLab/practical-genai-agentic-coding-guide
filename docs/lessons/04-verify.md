---
layout: default
title: 4. Verify
parent: Lessons
nav_order: 4
---

# Check that the change does what you asked

Set aside about 20 minutes to check both the new gate and the behavior that was already working. The agent's completion message is a useful starting point; now you will look at the results yourself.

Start with the examples you worked through in [Lesson 2](02-specify.md). The *acceptance checker* in `examples/qc_gate/check_acceptance.py` is a script that checks those agreed answers independently of the solution. It also runs the modified CLI on a small synthetic dataset and opens the resulting files.

```bash
python -m pytest
python examples/qc_gate/check_acceptance.py
python -m ruff check .
```

If you run that checker before adding the gate, it reports that the exercise has not been implemented. That is expected. We keep it separate from the ordinary tests so you can check the starting code before beginning the exercise.

## Know what each check tells you

| Check | What to look for |
| --- | --- |
| Small unit cases | The helper counts rows correctly, matches exact reason names, and handles boundaries. |
| CLI acceptance run | The whole command returns the right status, keeps its output files, and records the QC decision. |
| Existing tests | Previously tested cleaning behavior still works. These are your *regression checks*: they help catch something you broke while adding the gate. |
| Your review of the diff | The code changes, method, and explanations agree. We will work through this in the next lesson. |

Run the included sample with a new run ID and read the summary. Then set the maximum to zero so you can see how a failed gate is reported:

```bash
python -m pgacg demo --ehr data/example/ehr_bmi_simulated_data.tsv --demo data/example/demographics_simulated_data.tsv --run_id qc-strict --max_implausible_fraction 0 --verbose
```

The example contains implausible height/weight records, so this command should return `2`, keep its output files, and report a failed gate. Check the status immediately afterward with `echo $?` on macOS/Linux or `$LASTEXITCODE` in PowerShell. Here, a nonzero exit code is the result you are looking for.

## Diagnose a failure

If a test fails, find the smallest input that shows the disagreement and work out the answer by hand. Ask the agent to explain what happened before changing code or expected results. Copying the program's current output into a test would only preserve whatever it currently does, including a possible mistake.

Keep the commands and results in your task note, including anything you could not run. Once the expected passing and failing cases behave correctly, move to [review](05-review.md). These checks tell us whether the code follows the teaching rule; deciding whether that rule belongs in a study still needs a review of the method.
