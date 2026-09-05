---
layout: default
title: Start here
nav_order: 2
---

# Run the pipeline before you change it

Start by running the code already here. Having a result you can inspect makes it much easier to tell whether a later change helped or broke something. Allow 20–30 minutes, including setup.

Use the included synthetic files throughout. Keep patient, participant, student, and employee records out of this workspace and its agent conversations. The [lab data guidance](reference/lab-data-policy.md) explains how university policy applies when you later adapt the workflow to your own work.

## Coming from Part 1

In the [Part 1 quickstart](https://fritschelab.org/practical-genai-coding-guide/docs/QuickStart.html), you asked an assistant to write a small base-R function that selects the latest valid measurement. Here you will work with an existing Python project. It uses related synthetic EHR data, but a different rule: it selects a representative BMI measurement after filtering. We spell out that rule in the [data contract](reference/io_contract.md), the document describing what the inputs and outputs mean.

If R is more familiar, `python -m pgacg` plays a similar role to `Rscript`: it runs the program. The Python code lives in `src/pgacg/`, and `pytest` runs the checks in `tests/`. You can learn this workflow without translating the pipeline into R. The same habits carry back to the R projects discussed in the [Part 1 playbook](https://fritschelab.org/practical-genai-coding-guide/docs/AgenticCodingPlaybook.html).

## 1. Prepare a workspace

You need Python 3.10–3.12, Git, and a terminal. Python 3.12 matches one of the automated test environments. Check your version with `python --version` before creating the environment below. If your system uses the command `python3`, use that for the version check and environment creation. Open this repository and its synthetic examples as their own workspace; you can leave R and Quarto setup until you want to regenerate data or build slides.

The last command creates `.venv`, a folder for this project's Python packages so they can be managed separately from your other work.

```bash
git clone https://github.com/FritscheLab/practical-genai-agentic-coding-guide.git
cd practical-genai-agentic-coding-guide
python -m venv .venv
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use `.venv\Scripts\python.exe` in place of `python` in the following commands. After activating, run `python --version` to confirm you are using the version you intended.

## 2. Install and check

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
python -m ruff check .
```

The requirements file installs the package in *editable mode*, so your code changes take effect without reinstalling it. It also selects the package versions used for this teaching setup. `pytest` checks the program's behavior, while `ruff` checks the code for common mistakes and style issues. Get these checks passing before starting the exercise so you have a clear comparison later.

## 3. Run the baseline

```bash
python -m pgacg demo --ehr data/example/ehr_bmi_simulated_data.tsv --demo data/example/demographics_simulated_data.tsv --run_id baseline --verbose
```

Open `runs/baseline/summary.md` first. It describes what happened in this run. Then look at `manifest.json`, the machine-readable record of the inputs, software, and output files. Its checksums are fingerprints you can use to compare files between runs.

The name `baseline` is your run ID. Each run gets a fresh folder, so choose a different ID when you rerun the command, or omit `--run_id` to have one generated for you. This lets you compare runs without overwriting the earlier result.

| File inside the run folder | What you will find |
| --- | --- |
| `outputs/cleaned_bmi_person.tsv` | The selected encounter for each retained person, with the added columns. |
| `outputs/flagged_rows.tsv` | Excluded measurements with one or more reasons. |
| `outputs/flagged_people.tsv` | People in the demographics file who have no retained measurement. |
| `outputs/cleaned_bmi_person_data_dictionary.md` | Column definitions. |
| `logs/pipeline.log`, `summary.md` | What happened and which parameters were used. |
| `manifest.json` | Which inputs, code, and software were used, plus output file checksums. |

Compare the counts with the [synthetic data reference](reference/synthetic-data.md). Did the program select the expected records? Did it explain the exclusions? Small test datasets, often called *fixtures*, help us check individual rules by hand. This larger example lets us see those rules working together.

## 4. Set up your agent in Lesson 1

Begin [Lesson 1](lessons/01-orient.md), where you will choose a model and client, configure the project, and compare setups. The [client pages](platforms/index.md) provide the commands and folder locations you will use during that lesson. The assistant will help you change and review the code. The pipeline itself runs ordinary Python computations and makes no LLM calls.

You can also work through the lessons without an assistant account. Write the brief, implement the function yourself, and run the same checks. You will still practice the parts a collaborator needs to understand and reproduce your work.

## When setup fails

| Symptom | Next check |
| --- | --- |
| `No module named pgacg` | Activate the environment and repeat `python -m pip install -r requirements-dev.txt` from the repo root. |
| `pytest` or `ruff` missing | Use `python -m pytest` / `python -m ruff` with the environment's Python. |
| Run directory already exists | Choose a new `--run_id` so you can keep the earlier result for comparison. |
| Missing input columns | Compare the file with the [data contract](reference/io_contract.md). |
| Download or login unavailable | Check the connection or account setup with your local support team. Once the Python packages are installed, you can run the baseline without an assistant login. |

When you are ready to build the website or regenerate the synthetic data, follow [contributor setup](contributing.md).
