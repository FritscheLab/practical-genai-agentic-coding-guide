---
layout: default
title: Test the method
parent: Repository practices
nav_order: 3
---

# Test the method

Before asking an agent to change a calculation or selection rule, work through a small example yourself. If a person's valid BMI values are 20, 22, and 24, the median-based rule should select the record with BMI 22. Writing down that answer first gives you something independent of the implementation to test.

Then consider where the rule could be misunderstood: a value exactly at the threshold, missing measurements, tied records, or empty input. Include an invalid input that should produce a useful error.

The tests check both individual cleaning rules and complete runs through the CLI. Run the commands for your chosen language after its setup. Python:

```bash
python -m pytest
```

R:

```bash
Rscript tests/r/run_tests.R
```

For the exclusion-report exercise, inspect the report using the six-row and complete-data examples in [Lesson 2](../lessons/02-specify.md). The expected answers are 3 of 6 excluded (missing height: 2; missing weight: 2) and 0 of 6 excluded. Add focused tests of those counts and verify that the same records are selected and excluded as before.

With both environments installed, you can also run `python scripts/py/check_language_parity.py`. It compares parsed outputs and counts across the two baselines; it supplements the independently specified native tests.

Choose assertions that would catch a plausible mistake. For example, checking the selected encounter ID catches a wrong record that a “file exists” assertion would miss. A saved output snapshot can help detect formatting changes, but you still need an independently worked answer to check the calculation.

After changing behavior, run the relevant tests, the full suite, and the documented CLI command. For a prose-only change, build the site and inspect the changed pages. In your handoff to a collaborator, name the checks you ran and any part you could not verify.
