---
layout: default
title: Test the method
parent: Repository practices
nav_order: 3
---

# Test the method

Before asking an agent to change a calculation or selection rule, work through a small example yourself. If a person's valid BMI values are 20, 22, and 24, the median-based rule should select the record with BMI 22. Writing down that answer first gives you something independent of the implementation to test.

Then consider where the rule could be misunderstood: a value exactly at the threshold, missing measurements, tied records, or empty input. Include an invalid input that should produce a useful error.

The tests in `tests/` check both individual cleaning rules and complete runs through the CLI. After installing the development environment, run them with:

```bash
python -m pytest
```

When you implement the workshop's QC gate, also run its acceptance checker:

```bash
python examples/qc_gate/check_acceptance.py
```

The acceptance checker tests the new workshop requirement. It is separate from the baseline suite, so it is expected to fail before you implement the exercise even when all baseline tests pass. It checks the command's behavior and saved results without requiring a particular code structure.

Choose assertions that would catch a plausible mistake. For example, checking the selected encounter ID catches a wrong record that a “file exists” assertion would miss. A saved output snapshot can help detect formatting changes, but you still need an independently worked answer to check the calculation.

After changing behavior, run the relevant tests, the full suite, and the documented CLI command. For a prose-only change, build the site and inspect the changed pages. In your handoff to a collaborator, name the checks you ran and any part you could not verify.
