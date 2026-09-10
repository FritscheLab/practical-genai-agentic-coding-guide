---
layout: default
title: Working with coding agents
parent: Agent setup
nav_order: 7
description: Make sense of planning, tool use, shared skills, delegation, and longer coding tasks through one lab example.
---

# Working with coding agents

A coding agent can read, edit, run a check, and act on its result. Your job is to keep the task clear and judge the evidence.

**Documentation reviewed: September 5, 2026.** See the [client pages](index.md) for exact controls. The examples below suggest things to try, not a ranking of tools.

## Ask, plan, or start the work

“Which settings clip the labels?” calls for an explanation. “Repair the plot to meet the figure specification” calls for edits and checks.

Clients offer Ask, Plan, and Agent modes, or equivalents. Planning can still use tools to inspect code. Mode names and permitted operations vary; [check your client](index.md#choose-how-you-want-to-work).

Plan when a decision could change the method, affect several files, or be costly to undo. For a small, clear repair, make a direct request. The repository instructions and [local specification](../reference/figure-specifications.md) already carry the details.

## Follow the tools and their results

A failed check can lead the agent to inspect code, make a correction, and rerun. Follow that evidence rather than accepting “done.” [Agent feedback loops](https://www.anthropic.com/engineering/building-effective-agents).

Open the new PNG: passing tests can coexist with unreadable labels. Check accessibility too—contrast, group identification without color, and accurate alternative text. See [tool use](../practices/tool_selection.md) and [testing](../practices/testing.md).

## Keep useful context with the project

Store recurring instructions in `AGENTS.md` and procedures in skills. Skills usually expose a description first, then load the procedure when relevant. [Check discovery](portable-context.md) in your client. [Agent Skills specification](https://agentskills.io/specification), [Codex discovery](https://developers.openai.com/codex/skills).

Long sessions may be summarized or split into separate conversations. Keep decisions in the brief and actual results in the handoff so a fresh session—or labmate—can continue. [Context management](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

## Give another agent a question it can answer

A named role defines instructions and tools; delegation starts work in a separate conversation. Support differs by client. [Codex](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude Code](https://code.claude.com/docs/en/sub-agents), [Cursor](https://cursor.com/docs/subagents), [Gemini CLI](https://geminicli.com/docs/core/subagents/), [Copilot support](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).

Try “Have plot-reviewer review my plotting changes.” Give it the diff, image, and check results. Assign separate files if two agents edit in parallel, and decide who combines the work. Verify findings yourself; agreement between agents is not an acceptance test.

## Move a task to the cloud with its environment

Hosted agents can return a branch, diff, and review material from a separate environment. Your local interpreter, skills, and credentials may be absent. [Cursor Cloud Agents](https://cursor.com/docs/cloud-agent), [Codex cloud execution](https://learn.chatgpt.com/docs/agent-approvals-security).

Rehearse setup in a clean environment. Supply the same brief and checks, state where work should stop, and inspect returned evidence before merging. Check execution and usage limits before a long task.

## Connect or automate something you already use

MCP connects clients to external tools and context; plugins can package connections and skills. Check the operations a connection exposes and the receiving client's support. [MCP introduction](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro), [Plugin packaging](https://developers.openai.com/plugins/build/plugins).

Hooks run at client events, such as before a tool call or after an edit. Timing matters: a check after a write cannot prevent that write. Try both passing and failing cases, and keep required checks in CI too. [Claude hooks](https://code.claude.com/docs/en/hooks).

The lessons need only local tools. Read downloaded skill instructions and scripts before installing them. [Skill installation guidance](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## Compare runs you can explain

Change one variable at a time: model, mode, or reviewer. Start from the same revision and task. Record versions, permissions, corrections, time, and available usage data, including failed attempts.

| Question | Evidence |
| --- | --- |
| Does the code meet the contract? | Reproducible tests and image review |
| Did the agent follow the request? | Tool activity, honest check reporting, reviewable diff |
| Is the method appropriate for a study? | Analysis plan and subject-matter review |

Gemini CLI documents behavioral evaluations of agent workflows; these do not rank clients on this exercise. [Behavioral evaluations](https://geminicli.com/docs/behavioral-evals/).

Use the [source index](../reference/sources.md) to revisit documentation before teaching these features.
