---
layout: default
title: Run the pipeline
parent: Reference
nav_order: 2
---

# Run the pipeline

This reference shows a six-row first run and an optional larger example. Choose Python or R; both use the included synthetic data and the same [data contract](../reference/io_contract.md). Complete the commands for your chosen path only.

## Install and make a first run

Run commands from your local [example repository](https://github.com/ilarsf/practical-genai-agentic-coding-example) root. If you have not downloaded it yet, start with the [Python or R setup](../quickstart.md). These multiline examples use Bash or zsh. In Windows PowerShell, enter the demo command on a single line without the trailing `\` characters.

### Python

Use Python 3.10–3.12. Create an environment and install the demo and test packages, including the editable pipeline:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest
python -m pgacg demo \
  --ehr data/example/exclusion_report/ehr.tsv \
  --demo data/example/exclusion_report/demographics.tsv
```

In PowerShell, activate with `.venv\Scripts\Activate.ps1`. The editable install lets `python -m pgacg` find local code and pick up later edits.

### R

Use R 4.1 or later (checked locally with R 4.6.1). Install `jsonlite` and `digest`, run the R checks, then process the included data:

```bash
Rscript scripts/r/install_dependencies.R
Rscript tests/r/run_tests.R
Rscript scripts/r/demo.R \
  --ehr data/example/exclusion_report/ehr.tsv \
  --demo data/example/exclusion_report/demographics.tsv
```

The R path does not require Python. Changes to the files in `R/` take effect on the next run.

## Inspect the shared outputs

The console prints the new run directory. Open `summary.md` first: with the small example, you should see **6 input measurements, 3 selected people, and 3 excluded rows**. Measurements d, e, and f are excluded. Height is missing in d/f; weight is missing in e/f.

Next, open `outputs/cleaned_bmi_person.tsv` to see the selected measurements and `outputs/flagged_rows.tsv` to see excluded measurements and their reasons. `outputs/flagged_people.tsv` lists people with no selected measurement. The generated data dictionary explains the standard output columns, and the [data contract](../reference/io_contract.md) explains the selection rules and their teaching scope.

Finally, look at `manifest.json` and confirm its status is `success`. It records the command, effective parameters, code and environment versions, and checksums for the inputs, summary, and outputs. This is the information a collaborator can use to compare or repeat your run.

## Optional: explore the larger example

The following commands use the larger simulated files. First run with `--mismatch_threshold 2.0` to establish their baseline, then with `1.0` as shown. Compare those two runs; they use different input files from the six-row exercise.

**Python:**

```bash
python -m pgacg demo \
  --ehr data/example/ehr_bmi_simulated_data.tsv \
  --demo data/example/demographics_simulated_data.tsv \
  --mismatch_threshold 1.0
```

**R:**

```bash
Rscript scripts/r/demo.R \
  --ehr data/example/ehr_bmi_simulated_data.tsv \
  --demo data/example/demographics_simulated_data.tsv \
  --mismatch_threshold 1.0
```

Compare the two summaries and manifests within your chosen path. Lowering the threshold can exclude additional rows: a mismatch means the absolute difference between reported and calculated BMI is strictly greater than the threshold. For example, a difference of 1.5 passes the default threshold of 2.0 but is excluded at 1.0. The threshold must be a finite number greater than or equal to zero.

Use `--runs_dir tmp/my_runs` to keep your practice runs in another directory. You can name a run with `--run_id practice_1`, provided that ID has not already been used there. Add `--verbose` when you want debug details in the console.

## Troubleshooting

| Symptom | Action |
|---|---|
| `No module named pgacg` | Activate the intended environment and run `python -m pip install -e .` from the example repository root |
| Missing R package | Run `Rscript scripts/r/install_dependencies.R` with the same R installation used for the demo |
| Missing required columns | Check the TSV header against the [data contract](../reference/io_contract.md) |
| Duplicate person or encounter keys | Correct the synthetic input so demographics has one row per person and encounter IDs are unique |
| Existing run directory | Choose a new run ID; previous runs are preserved |
| Error after the run starts | Read `summary.md` for the explanation and `logs/pipeline.log` for details; the manifest records the failed status |
| Empty cleaned output | Check flagged rows and people; the baseline allows all-excluded and empty inputs |

For more on comparing results and understanding checksums, see [Logging and runs](../practices/logging_and_runs.md).
