---
layout: default
title: Navigate the repository
parent: Repository practices
nav_order: 2
---

# Navigate the repository

Start with `README.md` for the purpose and setup, `AGENTS.md` for working conventions, and `REPO_MAP.md` for the main commands and files. Once you understand the task, use a focused search to find the code and tests you need.

```bash
rg --files src tests docs
rg -n 'mismatch_threshold' src tests docs/reference
```

The package has separate files for reading inputs, cleaning data, writing reports, and organizing runs. For example, a search for `mismatch_threshold` shows where the CLI accepts the value, where cleaning uses it, and which tests check it. Following that path helps you see the effect of a change before editing.

Read the relevant tests alongside the [data contract](../reference/io_contract.md). The tests show what is checked; the contract explains what should happen. If they disagree, discuss the intended behavior with your collaborator and update the appropriate code, test, or explanation.

When you move a main command or file, update `REPO_MAP.md` so the next person can find it.
