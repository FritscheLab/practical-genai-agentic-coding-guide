---
layout: default
title: Working with coding agents
parent: Agent setup
nav_order: 7
description: Make sense of planning, tool use, shared skills, delegation, and longer coding tasks through one lab example.
---

# Working with coding agents

Part 1 introduced the habit of giving an assistant a clear task and checking its answer. Here we put those habits to work in a runnable repository: the agent inspects files, edits code, runs tests, and continues from what it finds. We need to follow the result of each step, the decisions still open, and the work we have allowed it to do.

**Documentation reviewed: September 5, 2026.** Current clients offer more ways to plan, share procedures, delegate work, and run tasks away from your laptop. The discussion below connects those documented features to the quality-gate exercise. It is a guide to trying them, rather than a ranking of tools or a claim about research productivity. Exact controls are on the [client setup pages](index.md).

## Ask, plan, or start the work

Early in the exercise, you might ask, “Where do we decide that a measurement is implausible?” A useful answer names the function and follows a record through it. Later, you need to settle how the new quality gate will fit into that code. After those decisions, you can ask the agent to implement and check the change.

These are different requests even if you use the same model throughout. Clients often offer **Ask**, **Plan**, and **Agent** modes, or similar controls, to support them. Planning can still involve tools: the agent needs to inspect the code before proposing a useful design. Agent mode usually lets it continue through edits and checks, using the results to decide what to try next. The labels and permitted operations vary by client; check [how to choose a mode](index.md#choose-how-you-want-to-work).

Use a separate planning step when a decision could change the method, touch several parts of the project, or be expensive to undo. For this exercise, the plan should settle the counting rule and how outputs survive a failed gate. Once that is clear, start the work. Fixing a typo usually needs only a direct request. [Lesson 2](../lessons/02-specify.md#use-planning-to-settle-the-open-questions) gives you a planning prompt to try.

## Follow the tools and their results

An agent works through a feedback loop: choose an operation, receive its result, and decide what to do next. A test failure can prompt a code inspection and a correction. A missing dependency can prompt an environment check. The tool result gives you evidence to discuss; the agent's interpretation still needs checking. [Agent feedback loops](https://www.anthropic.com/engineering/building-effective-agents).

In the quality-gate exercise, watch what happens when one row has both implausibility reasons. Does the agent examine the failing case and fix the calculation, or quietly change the expected answer? That moment tells you more than a polished completion message. The [tool-use guide](../practices/tool_selection.md) explains how to check the command, its output, and the next action.

## Keep useful context with the project

Repository instructions and skills help colleagues share guidance they would otherwise repeat in chat. A skill commonly exposes its description first and loads the longer procedure when relevant. Client support for the shared format has grown, but discovery paths and invocation still differ. Use the [portable review example](portable-context.md) to check what your client actually loads. [Agent Skills specification](https://agentskills.io/specification), [Codex skill discovery](https://developers.openai.com/codex/skills).

Longer sessions also need a way to preserve decisions. Clients may compact a conversation into a summary; some provide persistent memory or delegate work into separate conversations. These are useful forms of context management, with their own limits. [Anthropic's context engineering discussion](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

For our exercise, keep the agreed fraction and expected answers in the task brief. Record completed checks and unfinished work in the handoff. When a new session starts, ask it to inspect those files and the current code. A future labmate should be able to recover the reasoning from the repository too.

## Give another agent a question it can answer

Custom roles and subagents can separate exploration, implementation, and review. Codex, Claude Code, Cursor, and Gemini CLI document subagents with separate conversational context; Copilot's support depends on the client. A named reviewer profile supplies instructions and tools. Delegating to it starts an actual piece of work. [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Claude subagents](https://code.claude.com/docs/en/sub-agents), [Cursor subagents](https://cursor.com/docs/subagents), [Gemini subagents](https://geminicli.com/docs/core/subagents/), [Copilot support matrix](https://docs.github.com/en/copilot/reference/customization-cheat-sheet).

Try asking a reviewer whether the gate counts each input row once while the main agent updates the runbook. Give the reviewer the contract, relevant files, and a request for an example with each finding. Decide who may edit which files and who will bring the results together. Parallel work helps when those jobs can proceed separately; it adds coordination when they cannot. Agreement between agents still needs the acceptance cases and your review of the method.

## Move a task to the cloud with its environment

A hosted agent can work in its own development environment and return a branch, diff, and review material. That makes longer tasks possible without keeping the same local session open. Cursor documents cloud machines and review artifacts; Codex describes a separate cloud setup phase before execution. [Cursor Cloud Agents](https://cursor.com/docs/cloud-agent), [Codex cloud execution](https://learn.chatgpt.com/docs/agent-approvals-security).

Rehearse the quickstart from a clean environment first. Then give the hosted task the same synthetic inputs, setup commands, and acceptance criteria. State what a finished result should include and where work should stop, such as returning a change for review. Check the service's execution limits and usage before starting a long task. Your local interpreter, personal skills, and credentials may not be present there; inspect the returned evidence before merging.

## Connect or automate something you already use

MCP provides a way for clients to reach external tools and context. Plugins can package connections and skills together. These are useful when a colleague wants to share a working procedure, or when a task needs a source outside the repository. Check the receiving client's support and the operations a connection exposes. [MCP introduction](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro), [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins).

Hooks take a different role: they run a command at a client event, such as before a tool call or after an edit. Their timing and failure behavior matter. A check that runs after a write has different consequences from a check that can block it. [Claude hooks reference](https://code.claude.com/docs/en/hooks).

The local tools are enough for the lessons. If you later add a hook for a familiar check, run it by hand first, then try a passing case and a failure through the hook. Keep required checks in CI as well, since a collaborator may not have your local setup. Read downloaded skill instructions and scripts before installing them. [GitHub skill installation guidance](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

## Compare runs you can explain

If you try a different model, mode, or reviewer setup, repeat a task from the same repository revision with the same expected answers. Record the client and model versions, permissions, where it ran, the corrections you made, time, and any available usage data. Read failed attempts too.

When discussing the result with a colleague, keep these questions separate:

| Question | Useful evidence |
| --- | --- |
| Does the code implement the agreed contract? | Fixed synthetic cases, boundary cases, and reproducible tests |
| Did the agent handle the task as requested? | Relevant context, appropriate tool use, honest check reporting, and a reviewable diff |
| Is the method appropriate for the study? | A reviewed analysis plan and subject-matter review |

Gemini CLI's development documentation includes behavioral evaluations of agent workflows, illustrating the second kind of check. Those evaluations do not establish which client works best on this repository. [Gemini CLI behavioral evaluations](https://geminicli.com/docs/behavioral-evals/).

Change one part of the setup at a time so you can discuss what made a difference. The [source index](../reference/sources.md) collects the official documentation to revisit before teaching these features.
