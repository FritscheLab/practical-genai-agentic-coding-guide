---
layout: default
title: Instructor solution
parent: Teaching
nav_order: 3
---

# Compare notes with the reference solution

Use this page after you or your group have attempted the [quality-gate exercise](../lessons/02-specify.md). The working demo deliberately remains gate-free so every new group starts with the same task.

## Check a learner's implementation

Run these commands from the repository root in the development environment:

```bash
python -m pytest
python examples/qc_gate/check_acceptance.py
```

The [acceptance checker](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/examples/qc_gate/check_acceptance.py) calculates its expected answers independently. It tests equality at 20%, failure at 30%, both reasons on one row, exact reason tokens, irrelevant exclusions, empty input, custom limits, rejected arguments, retained outputs, and final artifact checksums. A missing-exercise message on the published baseline is expected.

Ask someone in the group to explain which rows count and what we divide by before opening the code. Then inspect one failing run: its normal outputs should still exist, its summary and manifest should agree on the QC result, and the command should return `2`. An input-schema error returns `1` and records a runtime failure instead.

## Verify the reference in isolation

```bash
python examples/qc_gate/verify_solution.py
```

The verifier copies the package, baseline tests, and small synthetic fixture to a temporary directory. It overlays the [reference fraction helper](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/examples/qc_gate/solution/qc.py) and [reference CLI](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/examples/qc_gate/solution/cli.py), runs the regression suite and acceptance checker against that copy, then removes it. It does not edit your working package or install dependencies.

The full CLI is included so the solution is readable and executable. It reuses the working pipeline's cleaning, reporting, and manifest helpers. The added code computes the fraction, records a QC section, and finalizes the manifest after the summary changes so its checksum remains valid.

## Compare after an attempt

```bash
diff -u src/pgacg/cli.py examples/qc_gate/solution/cli.py
```

Different implementations can satisfy the same contract. Look for exact token matching, one count per row, the original input count as denominator, a strict `>` comparison, and ordinary artifact creation before the QC exit.

If you want to run the reference in a disposable checkout **after completing your attempt**, first save your own work, then copy the two modules:

```bash
cp examples/qc_gate/solution/qc.py src/pgacg/qc.py
cp examples/qc_gate/solution/cli.py src/pgacg/cli.py
python -m pytest
python examples/qc_gate/check_acceptance.py
```

These copy commands replace the exercise implementation in that checkout. Keep the published baseline unchanged so the next learner can implement the gate themselves.
