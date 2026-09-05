---
layout: default
title: Task brief
parent: Templates
nav_order: 1
---

# Explain the change you want

A useful brief answers the questions you would ask a labmate before changing their code: what should happen, where should I work, and how will we know it works? Fill in the expected results before asking for implementation. [Lesson 2](../lessons/02-specify.md) shows this with the quality-gate rule.

```markdown
## What I want to change
[One change and why it would help.]

## Where to work
Read AGENTS.md and REPO_MAP.md.
Relevant implementation: [paths]
Existing contract and examples: [paths]
Files allowed to change: [paths]
Out of scope: [specific adjacent work]

## Agreed method
Inputs and units: [schema/reference]
Rule: [exact calculation or selection]
Missing values, ties, boundaries, and errors: [explicit behavior]
Outputs and run status: [files/columns/exit codes]

## How to check it
[Small synthetic input -> independently worked expected result.]
Command: [exact command from repo root]
Expected behavior: [observable result]
Check existing behavior still works: [test commands]

## Working together
Read the relevant files and briefly explain your approach.
Ask if a missing method or access decision affects the work; otherwise proceed.
Implement the change, run the checks, inspect the diff, and update affected docs.
Tell me what changed, what you ran, the results, and anything still unresolved.
Do not edit expected results to make an implementation pass.
```
