---
layout: default
title: Navigate the repository
parent: Repository practices
nav_order: 2
---

# Navigate the repository

Open the cloned exercise in VS Code. **Explorer** shows the files on disk; **Source Control** shows changes that Git can record. Both are useful throughout the exercise.

## Find the plotting code

1. In Explorer, open `README.md`, `AGENTS.md`, and `REPO_MAP.md` for setup, working conventions, and the file map.
2. Expand `plotting` and open `plot_summary.py` or `plot_summary.R`. Use VS Code's **Search** view to find `plot_summary` across the workspace, or **Edit → Find** to search the current file.
3. In Copilot Chat, choose **Local → Ask** and request an explanation with source references. Open those references and compare the explanation with the code and [plotting contract](../reference/io_contract.md).

Python builds the layout in `make_summary_figure()` and saves it through `plot_summary(output_path)`. R draws and saves inside `plot_summary()`. Read the fixed values and tests before changing the layout. No input dataset is needed.

## Read the changed-file list

After implementation, save the files and select the **Source Control** icon in the Activity Bar. Expand **Changes**. Its badges distinguish modified (`M`), untracked/new (`U`), and deleted (`D`) files. Open each entry, including new files. An unexpected deletion or environment file deserves an explanation before staging.

Copilot's change summary describes its work. Git's list includes other saved edits too, so compare both before committing. Generated PNGs and alternative text live under ignored `runs/`: open them in Explorer even though they do not appear in Source Control. Do not force-add those outputs to Git.

## Read a color-coded diff

Click a file under **Changes**. In a side-by-side diff, the previous content is on the left and your edited content is on the right. With the standard theme, red marks removals and green marks additions; `−` and `+` markers also identify changed lines. A changed value often appears as one removal and one addition.

For a narrow editor, open the diff toolbar's **… → Diff View → Inline**. **Side by Side** restores two columns; **Automatic** chooses based on width. The same menu offers **Open Accessible Diff Viewer**. These are views of the same edit. [VS Code diff layouts and accessibility](https://code.visualstudio.com/docs/sourcecontrol/staging-commits#review-changes-with-the-diff-editor)

Read each changed section against the task: layout may change, while invented counts and command behavior must remain stable. Ask Copilot to explain a specific section if needed, then check its answer in the source.

## Save, stage, and commit

Saving writes edits to disk. Staging selects the version of those edits for the next commit. A commit records that staged snapshot in the local repository.

Hover over a reviewed source file in **Changes** and choose **+** to stage it. Open it again under **Staged Changes** to check the proposed commit. If you edit a file afterward, it can appear in both lists: review and stage the later edit too. Enter a message explaining the repair and choose **Commit**. [VS Code staging and commits](https://code.visualstudio.com/docs/sourcecontrol/staging-commits)

Copilot sign-in and Git commit identity are separate. If Git requests a name or email, use your path's handoff lesson to ask Copilot to configure your supplied identity for this repository only. **Push**, **Sync**, and **Publish** send work to a remote; this exercise finishes with a local commit.

Continue with [Python review](../paths/python/05-review.md) or [R review](../paths/r/05-review.md). The [CLI appendix](../appendix/command-line.md) provides terminal equivalents.

*VS Code Source Control documentation reviewed September 11, 2026. Menu placement can differ by version and theme.*
