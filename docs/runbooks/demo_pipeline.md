---
layout: default
title: Run the plotting example
parent: Reference
nav_order: 2
---

# Run the plotting example

Choose Python or R. Both plot invented totals embedded in source; see the [plotting contract](../reference/io_contract.md). No input dataset is needed.

Run these commands from the [example repository](https://github.com/FritscheLab/practical-genai-agentic-coding-example) root. Keep real study data, exports, and logs outside the workspace.

## Python

Complete the [Python setup](../paths/python/index.md), including `python -m pip install -r requirements-plotting.txt`, then run:

```bash
python -m unittest discover -s plotting/tests
python plotting/plot_summary.py --output runs/baseline/summary.png
```

## R

The plotting exercise uses base R. Run:

```bash
Rscript plotting/tests/run_tests.R
Rscript plotting/plot_summary.R --output runs/baseline/summary.png
```

## Open the image

Open `runs/baseline/summary.png`: groups overlap and labels are clipped. Behavior tests still pass because they protect values and command behavior.

The strict figure checker intentionally fails on the baseline. It checks the local [fictional journal specifications](../reference/figure-specifications.md). Python:

```bash
python plotting/check_figure.py --output runs/baseline/summary.png
```

R:

```bash
Rscript plotting/check_figure.R --output runs/baseline/summary.png
```

Follow the [exercise specification](../lessons/02-specify.md) to repair the layout in Python's `make_summary_figure()` or R's `plot_summary(output_path)`. Save the new image to a different path. Python:

```bash
python plotting/plot_summary.py --output runs/with-fix/summary.png
python -m unittest discover -s plotting/tests
python plotting/check_figure.py --output runs/with-fix/summary.png
```

R:

```bash
Rscript plotting/plot_summary.R --output runs/with-fix/summary.png
Rscript plotting/tests/run_tests.R
Rscript plotting/check_figure.R --output runs/with-fix/summary.png
```

Compare the repaired image with the [target](../lessons/02-specify.md#done-looks-like-this) and [figure specification](../reference/figure-specifications.md), then inspect the diff. Python and R images need not match pixel for pixel.

Review contrast, grayscale readability, and group identification without color. Write and review `runs/with-fix/summary.alt.txt` against the specification; the commands do not create it. See [accessibility review](../practices/testing.md#include-accessibility-in-the-review).

## Troubleshooting

| Problem | Next check |
| --- | --- |
| Python cannot import the plotting dependency | Activate your chosen environment and install `requirements-plotting.txt` there. |
| `Rscript` is unavailable | Complete the R installation in your language's setup page. |
| The command cannot write the image | Check the output path and workspace permissions. |
| The image still looks unchanged | Confirm the source file was saved, rerun the render command, and open the new output path. |
| Behavioral tests pass but bars overlap or labels are clipped | Run the strict figure checker, review the layout settings, and open the image. |
| The agent cannot view an image | Perform the visual check yourself and record that limitation in the handoff. |
