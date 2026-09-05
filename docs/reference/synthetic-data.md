---
layout: default
title: Synthetic data
parent: Reference
nav_order: 3
---

# Synthetic data

The included example contains **1,074 measurements for 12 synthetic people**. The R simulator creates every value without using patient records, then introduces missing values, implausible measurements, and BMI mismatches so we have concrete problems to work through.

## Provenance

The simulator comes from Part 1, revision `34830a3d1323d9f81a395f5d4fda48b5ee80566b` (September 5, 2026), with its script path updated for Part 2. Both guides use the same synthetic schemas and install dependencies as a separate setup step. The [upstream source](https://github.com/FritscheLab/practical-genai-coding-guide/blob/34830a3d1323d9f81a395f5d4fda48b5ee80566b/scripts/simulate_ehr_data.R) and local file hashes let you identify the version used here.

We generated these files with **R 4.6.1**, **optparse 1.8.2**, seed **123**, and **12 people**. The simulator requires R 4.3 or later; use the recorded versions when you want to reproduce the files exactly. You only need R to regenerate data—the included files are ready to use with the Python pipeline.

The demographic `age` is measured as of December 31, 2019. A person's age at an earlier measurement can therefore be different, and some measurements concern minors. The [data contract](io_contract.md) explains how this teaching pipeline treats those records.

## Regenerate in a separate directory

Install `optparse` explicitly if your R environment lacks it:

```bash
Rscript -e 'install.packages("optparse", repos = "https://cloud.r-project.org")'
```

For an R project with an existing lockfile, restore that project's environment instead. The simulator checks dependencies and does not install them during an analysis run.

```bash
Rscript scripts/r/simulate_ehr_data.R \
  --output_ehr tmp/regenerated/ehr_bmi_simulated_data.tsv \
  --output_ehr_dict tmp/regenerated/data_dictionary.txt \
  --output_demo tmp/regenerated/demographics_simulated_data.tsv \
  --output_demo_dict tmp/regenerated/demographics_data_dictionary.txt \
  --seed 123 --n_individuals 12
python scripts/py/check_example_data.py --directory tmp/regenerated
```

The checker compares the four files with the hashes recorded in `data/example/provenance.json`. If they differ, first compare your R and package versions and the simulator revision with those above. If you intend to update the included example, review the regenerated data and counts with a collaborator, then update the provenance record and this page together.

## Expected baseline

Run the quickstart command with the default mismatch threshold of 2.0.

| Metric | Expected value |
| --- | ---: |
| Input measurements | 1,074 |
| Demographics people | 12 |
| Selected people | 12 |
| Excluded measurement rows | 218 |
| Retained measurements before selection | 856 |
| People with no selected measurement | 0 |
| Per-person IQR outliers | 11 |
| Rows carrying a BMI mismatch flag | 51 |

A row can have both a height or weight issue and a BMI mismatch, so reason counts can overlap. These totals provide a quick check that the full pipeline still behaves as expected. Smaller test datasets with answers worked out independently check individual calculations and selection rules.

For a larger practice dataset, use the same command with output paths under `data/raw/` and a larger `--n_individuals`. Its counts will differ from this baseline. You can inspect the included files, dictionaries, and provenance in the [repository](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/tree/main/data/example).
