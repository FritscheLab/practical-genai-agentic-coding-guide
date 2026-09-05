---
layout: default
title: Demo prompts
parent: Teaching
nav_order: 2
---

# Prompts for the workshop

## Orientation

```markdown
Read AGENTS.md, REPO_MAP.md, the data contract, and the CLI.
Explain the baseline command, representative-record selection, run artifacts,
and the relevant tests. Cite the files you inspected. Do not edit yet.
```

## Implementation

If the group still has questions about the approach, use the [Lesson 2 planning prompt](../lessons/02-specify.md#use-planning-to-settle-the-open-questions) first. Discuss the counting rule and saved outputs, then switch to implementation.

Use the complete [Lesson 3 prompt](../lessons/03-implement.md). Its referenced [method and acceptance cases](../lessons/02-specify.md) are part of the request. Keep both visible so the agent does not have to invent what quality control means.

## Review

```markdown
Review the change against docs/lessons/02-specify.md. Inspect the actual diff,
new files, and tests. Report concrete defects with input, expected behavior,
actual behavior, and file location. Check the 20% boundary and preserved artifacts.
Do not edit files. Separate defects from optional style preferences.
```

## Handoff

```markdown
Use docs/templates/handoff.md to record the objective, verified state, decisions,
actual checks and results, and remaining work. Keep paths repository-relative.
Do not claim that proposed or unrun checks passed.
```
