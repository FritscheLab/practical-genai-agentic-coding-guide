---
layout: default
title: Logging and runs
parent: Repository practices
nav_order: 4
---

# Logging and runs

Each run gets its own `runs/<run_id>/` directory, making it easier to compare results after a change. The default ID combines a UTC timestamp with four random characters, for example `20260905_173000_a1b2`. Use `--runs_dir` to choose another parent directory or `--run_id` to provide your own name. The [data contract](../reference/io_contract.md) lists the allowed characters. Existing directories, including failed runs, are preserved.

## What to read after a run

- `logs/pipeline.log`: progress and diagnostic details for this run. The console also shows progress; add `--verbose` to see debug details there.
- `outputs/`: cleaned person-level data, flagged rows, flagged people, and the cleaned data dictionary.
- `summary.md`: human-readable status, inputs, parameters, counts, and category distributions; failed runs explain the error.
- `manifest.json`: the command, inputs, parameters, environment, and checksums, saved in a form that a script can read.

Start with `summary.md`. If a run fails, it explains the error and points you to the log for details. Input or processing errors after a run starts return exit code 1 and save the summary, log, and manifest if the directory is writable. Invalid arguments or a problem creating the run directory return exit code 2 before a run exists. A manifest marked `failed` or `running` records work that has not completed successfully.

Read these files before sharing them. The manifest records full input paths and the working directory, and errors can include details from the input. This pipeline does not redact them. Its “cleaned” files also retain identifying columns from the synthetic inputs. Keep the exercise synthetic; in a real study, outputs and logs belong in the approved environment until their release has been checked. See [lab data and university policy](../reference/lab-data-policy.md).

## Manifest schema (version 1)

| Field | Meaning |
|---|---|
| `schema_version`, `run_id` | Manifest format version and run identifier |
| `status` | `running`, `success`, or `failed` |
| `started_at`, `finished_at` | UTC ISO timestamps; finish is null while running |
| `command` | Command arguments saved as a list, preserving spaces within each argument |
| `command_source` | `process` for the invoked Python CLI; `equivalent_module_invocation` for a library call to `main(argv)` |
| `working_directory` | Directory from which the command was invoked |
| `parameters` | All effective `CleaningParams` values, including defaults |
| `inputs.ehr`, `inputs.demographics` | Absolute input `path` and file `sha256`; a hash can be null if the input could not be read or processing stopped before hashing it |
| `code.version`, `code.git.revision`, `code.git.dirty` | Package version, Git commit, and whether the checkout has uncommitted changes |
| `environment` | Python version, implementation, platform, and installed pandas/NumPy versions |
| `metrics` | Cleaning counts when available; included on success |
| `artifacts` | Paths relative to the run directory, each with `sha256` and `size_bytes` |
| `error` | Error type and message on failure; null otherwise |

Git fields are `null` when Git or checkout information is unavailable, including a wheel installation. A checkout with no commits may have a null revision and `dirty: true`. If `dirty` is true, the recorded commit does not fully describe the code that ran; keep a copy of those changes with any result you need to reproduce.

The SHA256 checksums let you compare file contents across runs. They cover `summary.md` and files in `outputs/`, excluding logs and the manifest itself. A checksum is a fingerprint rather than a saved copy, so reproducing a run still requires its input files, source code, and environment specification. Keep inputs unchanged while the pipeline is reading them.

## Comparing runs

When the inputs, parameters, code, and environment match, compare the output TSV hashes in the two manifests. Run IDs, timestamps, logs, and paths will naturally differ. Record selection breaks ties by latest measurement date and then encounter ID, so the chosen records are independent of input order. The flagged-row file preserves input order within each filtering stage; shuffling the input can therefore change that file's order and hash even when the selected records stay the same.

If the counts differ, use the [data contract](../reference/io_contract.md) to trace which rule or input changed. Remember that a row can carry more than one exclusion reason.
