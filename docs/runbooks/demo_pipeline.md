---
layout: default
title: Run the pipeline
parent: Reference
nav_order: 2
---

# Run the pipeline

This walkthrough takes you from setup to a first run, then shows how to compare results after changing a parameter. The included synthetic data are ready to use, so you do not need R. Use Python 3.10–3.12 with the tested dependency versions in the repository requirements files.

## Install

From the repository root, create an environment and install the development dependencies and package:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pip install -e .
```

These examples use Bash or zsh. In Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` and enter the multiline commands below on a single line, omitting the trailing `\` characters. The editable package install lets `python -m pgacg` find the local code and pick up your later edits.

## Make a first run

Run the tests, then process the included data:

```bash
python -m pytest
python -m pgacg demo \
  --ehr data/example/ehr_bmi_simulated_data.tsv \
  --demo data/example/demographics_simulated_data.tsv
```

The console prints the new run directory. Open `summary.md` first: with the included data and default parameters, you should see **1,074 input measurements, 12 selected people, and 218 excluded rows**. The [synthetic data page](../reference/synthetic-data.md) gives the remaining baseline counts and explains how the inputs were made.

Next, open `outputs/cleaned_bmi_person.tsv` to see the selected measurements and `outputs/flagged_rows.tsv` to see excluded measurements and their reasons. `outputs/flagged_people.tsv` lists people with no selected measurement. The generated data dictionary explains the standard output columns, and the [data contract](../reference/io_contract.md) explains the selection rules and their teaching scope.

Finally, look at `manifest.json` and confirm its status is `success`. It records the command, effective parameters, code and environment versions, and checksums for the inputs, summary, and outputs. This is the information a collaborator can use to compare or repeat your run.

## Change a parameter

```bash
python -m pgacg demo \
  --ehr data/example/ehr_bmi_simulated_data.tsv \
  --demo data/example/demographics_simulated_data.tsv \
  --mismatch_threshold 1.0
```

Compare the two summaries and manifests. Lowering the threshold can exclude additional rows: a mismatch means the absolute difference between reported and calculated BMI is strictly greater than the threshold. For example, a difference of 1.5 passes the default threshold of 2.0 but is excluded at 1.0. The threshold must be a finite number greater than or equal to zero.

Use `--runs_dir tmp/my_runs` to keep your practice runs in another directory. You can name a run with `--run_id practice_1`, provided that ID has not already been used there. Add `--verbose` when you want debug details in the console.

## Troubleshooting

| Symptom | Action |
|---|---|
| `No module named pgacg` | Activate the intended environment and run `python -m pip install -e .` from the repository root |
| Missing required columns | Check the TSV header against the [data contract](../reference/io_contract.md) |
| Duplicate person or encounter keys | Correct the synthetic input so demographics has one row per person and encounter IDs are unique |
| Existing run directory | Choose a new run ID; previous runs are preserved |
| Error after the run starts | Read `summary.md` for the explanation and `logs/pipeline.log` for details; the manifest records the failed status |
| Empty cleaned output | Check flagged rows and people; the baseline allows all-excluded and empty inputs and has no QC gate |

For more on comparing results and understanding checksums, see [Logging and runs](../practices/logging_and_runs.md).
