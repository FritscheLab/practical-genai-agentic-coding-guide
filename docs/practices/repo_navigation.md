---
layout: default
title: Navigate the repository
parent: Repository practices
nav_order: 2
---

# Navigate the repository

From the [example repository](https://github.com/FritscheLab/practical-genai-agentic-coding-example) root, read `README.md` for setup, `AGENTS.md` for working conventions, and `REPO_MAP.md` for commands and files. Then search:

```bash
rg --files plotting docs
rg -n 'plot_summary|Complete measurements' plotting
```

Choose `plotting/plot_summary.py` or `plotting/plot_summary.R`. Trace argument handling into `plot_summary(output_path)`. Python builds the layout in `make_summary_figure()`; R draws inside `plot_summary()`. Read the constants, layout settings, and tests alongside the [plotting contract](../reference/io_contract.md).

The source and invented aggregate chart give the agent enough context for a layout discussion. No input dataset is needed.

Resolve disagreements between code and tests before editing either. Update `REPO_MAP.md` when moving files or commands.
