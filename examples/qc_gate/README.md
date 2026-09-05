# Quality-gate exercise checks

Complete [lessons 2–4](../../docs/lessons/02-specify.md) before inspecting `solution/`.

From the repository root, in the installed development environment:

```bash
python examples/qc_gate/check_acceptance.py
```

The published baseline intentionally has no quality gate. The checker returns a
clear nonzero result until the exercise is implemented. It contains hand-specified
expected fractions and constructs its own synthetic CLI inputs; it never imports
the reference solution. It also verifies normal artifacts and their checksums on
QC failure. Do not edit the checker to make your implementation pass.

The reporting contract is described in lesson 2. The checker reads numeric
`observed_fraction` and `max_implausible_fraction` and an `outcome` of `pass` or
`fail` from `manifest.json` under `qc`. It expects those same backtick-labelled
fields in `summary.md`, and overall status `success` or `qc_failed` in both.

For instructors and CI:

```bash
python examples/qc_gate/verify_solution.py
```

This copies the package, tests, and synthetic fixture into a temporary directory,
overlays the two reference modules, and runs the baseline regression suite plus
the acceptance checker. The `src/` working package remains unchanged. Temporary
copies are deleted when verification finishes, including when a check fails.
