---
layout: default
title: Optional R refactoring skill
parent: Agent setup
nav_order: 8
description: Reuse the lab's R formatting conventions with a skill or named Codex agent, then check behavior and inspect the diff.
---

# Refactor this script into the lab format

Turn “refactor this” into a repeatable request. This optional example packages Part 1's [R formatting conventions](https://fritschelab.org/practical-genai-coding-guide/docs/templates/R_CodeRefactoringPromptExample.html) as a local template, a skill, and the named `r-refactorer` agent.

Organize an R script with a clear header, readable spacing, and emoji section comments. Preserve its behavior and starting image, including the flawed layout; the [main exercise](../lessons/02-specify.md) handles that repair.

The **template** shows the format, the **skill** applies it, and the **agent** gives it a name. [Read the complete files](#read-the-reusable-files) below. Optional packages, logging, and session information are added only when requested.

**Skill and custom-agent documentation reviewed: September 10, 2026.** This setup follows the official [skill format](https://learn.chatgpt.com/docs/build-skills) and [custom-agent format](https://learn.chatgpt.com/docs/agent-configuration/subagents). Check discovery in the client and session you use.

## Start in the example repository

The script uses invented totals and reads no data file. Open the teaching repository separately from real study data, exports, and logs. See the [lab data guidance](../reference/lab-data-policy.md) before adapting it.

You need Git, base R (`Rscript`), and a local [Codex setup](codex.md). Open your existing [example checkout](https://github.com/FritscheLab/practical-genai-agentic-coding-example), or download it:

```bash
git clone https://github.com/FritscheLab/practical-genai-agentic-coding-example.git
cd practical-genai-agentic-coding-example
```

Run all terminal commands below from that repository root:

```bash
git --version
Rscript --version
ls examples/r_refactor/
ls .agents/skills/lab-r-refactor/SKILL.md \
  .agents/skills/lab-r-refactor/references/lab-r-template.md \
  .codex/agents/r-refactorer.toml
```

You should see `starter.R`, `reference.R`, and `verify.R`. Save the reference for after your attempt.

## Make a scratch copy and render the starting image

Copy the starter to ignored scratch space. Repeating `cp` resets your attempt.

```bash
mkdir -p tmp/r-refactor
cp examples/r_refactor/starter.R tmp/r-refactor/summary.R
Rscript tmp/r-refactor/summary.R --output tmp/r-refactor/before.png
```

Open `tmp/r-refactor/before.png`. Your refactor should keep this image unchanged while making its source easier to follow.

## Check discovery, then make one request

Open Codex here with access to edit and run R checks. Find `lab-r-refactor` through `/skills` or the `$` picker in CLI/IDE. Check its repository path; restart if missing. Codex searches skills from the working directory up to the repository root. [Discovery](https://learn.chatgpt.com/docs/build-skills).

Paste **one** of these requests into Codex. To use the skill directly:

```text
$lab-r-refactor Refactor tmp/r-refactor/summary.R.
```

Or ask for the named agent:

```text
Have r-refactorer refactor tmp/r-refactor/summary.R.
```

Check tool activity for reads of `SKILL.md` and the local template. For the named-agent route, confirm delegation to `r-refactorer`. `/agent` shows resulting threads, not installed roles. If unavailable, check the file and project trust, then restart. [Custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

Look for a summary of edits, actual checks, and untested work. File presence alone does not prove discovery or refactoring.

## Verify behavior and review the formatting

Run the verifier yourself, passing the scratch script as its optional argument:

```bash
Rscript examples/r_refactor/verify.R tmp/r-refactor/summary.R
```

The verifier protects fixed counts and compares PNG contents, stdout, stderr, and exit status, including argument/write errors and paths with spaces. Success prints `PASS: summary.R (constants, PNG contents, streams, and exit status)`.

Inspect the source change separately:

```bash
git diff --no-index -- examples/r_refactor/starter.R tmp/r-refactor/summary.R
```

`--no-index` compares even ignored files. Exit **1 means differences found**—expected after refactoring; `0` means identical. Investigate other statuses or errors. Press `q` to leave the pager. Ordinary `git diff` skips this ignored scratch file.

Read that diff with these questions in mind:

- Does the header describe the script and preserve recorded authorship and dates, using `Not recorded` for unknown values?
- Do purposeful emoji section headings, indentation, spacing, and line breaks make the function and CLI easier to follow?
- Do comments explain useful decisions without narrating every expression?
- Are the category totals, plotting calls, argument checks, messages, and output handling preserved?

An unchanged starter also passes: behavior checks do not prove refactoring. If organization did not improve, ask for a specific correction and repeat both checks.

## Compare the reference after your attempt

After reviewing your candidate, open `examples/r_refactor/reference.R` for one possible organization. Your result need not match it line for line:

```bash
git diff --no-index -- examples/r_refactor/reference.R tmp/r-refactor/summary.R
```

To check the included starter and reference together, omit the candidate argument:

```bash
Rscript examples/r_refactor/verify.R
```

Record discovery, formatting, and behavior checks in the handoff. Mark unavailable client checks untested.

## Read the reusable files

All three files are local: the agent reads the skill, which reads the template. No Part 1 checkout or network request is needed.

A skill's YAML `name` and `description` guide discovery and selection. Explicit invocation makes this demonstration easier to verify. [Skill format](https://learn.chatgpt.com/docs/build-skills).

<details markdown="1">
<summary>Complete .agents/skills/lab-r-refactor/SKILL.md</summary>

````markdown
---
name: lab-r-refactor
description: Refactor an existing R script into the lab format with metadata, emoji section headings, readable code, and explanatory comments while preserving its behavior. Use for requests to organize or format R scripts.
---

# Refactor an R script into the lab format

Before editing, read the [lab R template](references/lab-r-template.md). Use its examples to organize the script.

Work from source code and invented examples. Do not inspect data tables or participant records, and do not diagnose individual data points. If a check needs study data, report it as not run.

## Procedure

1. Read the requested script and applicable repository instructions. Identify its arguments, dependencies, calculations, validation, outputs, and existing checks. Save an unchanged copy in permitted scratch space for comparison.
2. Add or tidy the metadata header. Preserve existing authorship, creation dates, and other recorded history. Use `Not recorded` for unknown values; do not infer authorship from the repository owner or use today's date as a creation date. Describe only what the script actually does.
3. Organize the code using only applicable sections from the local template. Add one relevant emoji to each section-heading comment, such as `⚙️ Constants`, `📊 Plotting function`, or `▶️ Command-line arguments`. Keep the words so headings remain clear without the symbol. Use emojis only in comments, never in strings, object names, chart text, or console output. Keep execution order and scope intact. Use two-space indentation, consistent spacing, readable line breaks, and descriptive names where safe. Add short comments explaining intent or a non-obvious decision; avoid narrating each expression.
4. Preserve the script's behavior: argument interface, dependencies, calculations, validation, output contents and formatting, stdout, stderr, and exit status. Do not redirect data from `cat()` or `write.table()` to `message()`. Do not add packages, dependency installation, `optparse`, flags, logging, timestamps, `sessionInfo()`, new validation, or other functional features unless the user requests them. If you notice a defect, report it separately rather than silently changing the calculation during formatting.
5. Run the available automated checks on the original and candidate with the same invented examples and arguments. Let the verifier compare image contents, stdout, stderr, and exit status; use its pass/fail results. For this repository's optional exercise, run `Rscript examples/r_refactor/verify.R <candidate-script>` from the repository root. Inspect the code diff separately to confirm that organization improved. Passing behavior checks alone does not show that refactoring occurred.
6. For repository work, edit the requested file and report the organization changes, commands actually run, outcomes, and any untested behavior. If the user asks for returned code instead, provide the complete refactored script in an R code block; do not replace that deliverable with file edits. Never imply checks ran when they did not.
````

</details>

Keep the template with the skill when copying it.

<details markdown="1">
<summary>Complete .agents/skills/lab-r-refactor/references/lab-r-template.md</summary>

````markdown
# Lab R formatting template

Use these header and section examples to organize an R script. This template is inspired by Part 1's R refactoring example. Keep the script's behavior unchanged.

## Header

Use the actual filename and preserve recorded authorship and dates. Write `Not recorded` when that information is unknown. This example describes the plotting exercise:

```r
# ==============================================================================
# Script: plot_summary.R
# Description: Draw a chart from invented aggregate measurement counts.
# Author: Not recorded
# Date: Not recorded
# Input: Fixed category labels and counts defined in the source code.
# Output: A PNG chart at the requested output path.
# ==============================================================================
```

## Sections and formatting

Give each useful section a small visual marker: `⚙️ Constants`, `📊 Plotting function`, or `▶️ Command-line arguments`. Keep the descriptive words and omit empty sections. Put emojis in comments only; preserve strings, object names, chart text, and console output. Save the script as UTF-8 and keep execution order unchanged.

```r
# --- ⚙️ Constants -------------------------------------------------------------
# Keep the supplied category order so before/after charts remain comparable.
counts <- rbind(
  "Group A" = c(42, 31, 18, 9),
  "Group B" = c(64, 18, 12, 6)
)

# --- 📊 Plotting function -----------------------------------------------------
# Keep the existing plotting calls here, with readable spacing and line breaks.

# --- ▶️ Command-line arguments ------------------------------------------------
args <- commandArgs(trailingOnly = TRUE)
```

These snippets show organization, not a replacement implementation. Keep the requested script's own values, plotting calls, validation, messages, and output handling. Do not add logging, packages, or session information just to fill a section.
````

</details>

The required fields are `name`, `description`, and `developer_instructions`. Model and permission settings inherit from the session. [Custom-agent format](https://learn.chatgpt.com/docs/agent-configuration/subagents).

<details markdown="1">
<summary>Complete .codex/agents/r-refactorer.toml</summary>

```toml
name = "r-refactorer"
description = "Refactor an existing R script into the lab format while preserving its results and command-line behavior."
developer_instructions = """
Use the shared lab-r-refactor skill at .agents/skills/lab-r-refactor/SKILL.md
in the target repository; read that file before editing.
Follow applicable repository instructions and the user's requested scope.
For repository work, edit the requested R file, inspect its diff, and report
changes and checks. If the user requests returned code, provide that deliverable.
Keep the formatting procedure in the shared skill rather than duplicating it here.
"""
```

</details>

## Reuse the setup in another repository

In a separate workspace, combine shareable code and images, this setup, and invented tests. Validate real study data in its approved environment; review sharing rules even for aggregate images. See the [lab data guidance](../reference/lab-data-policy.md#bring-reviewed-code-to-a-study-deliberately).

From the new repository root, replace the path below and copy the whole skill folder plus the agent:

```bash
example_repo="/path/to/practical-genai-agentic-coding-example"
mkdir -p .agents/skills .codex/agents
cp -Rn "$example_repo/.agents/skills/lab-r-refactor" .agents/skills/
cp -n "$example_repo/.codex/agents/r-refactorer.toml" \
  .codex/agents/r-refactorer.toml
```

`-n` preserves existing files; review and merge any existing setup. Adapt the verifier command and read the new project's `AGENTS.md`.

Check `git status --short` before committing; add narrow ignore exceptions if needed. Start a fresh session and repeat discovery and invocation with your script path.

For other clients, see [skill locations](portable-context.md#find-and-use-the-review-skill) and [role formats](portable-context.md#know-which-folder-you-are-changing). The TOML role is Codex-specific.
