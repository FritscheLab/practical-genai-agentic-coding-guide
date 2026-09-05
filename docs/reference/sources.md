---
layout: default
title: Sources and update policy
parent: Reference
nav_order: 5
description: Find the official documentation behind the setup examples and see what to recheck before teaching.
---

# Sources and update policy

Use this page when you want to check a setup detail, adapt an example, or prepare a session for colleagues. It collects the official documentation behind the [agent setup guide](../platforms/index.md) and notes what each source helps explain.

**Source review date: September 5, 2026.** We retrieved the relevant pages to check modes, tool access, paths, configuration fields, instruction discovery, and documented capabilities. The examples use those formats with tasks and file paths from this repository.

A feature described in documentation still needs a hands-on check in the client you plan to use. We distinguish those two kinds of evidence throughout the guide. Installation and sign-in links lead to the provider’s current instructions because account and operating-system requirements can change.

## Shared concepts

| Source | Used for |
| --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) | Skill structure, required metadata, and optional resources |
| [Model Context Protocol introduction](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) | Connecting clients to external tools and context |
| [MCP server concepts](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts) | Distinguishing tools, resources, and prompts |
| [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | A foundational explanation of tool use and feedback; originally published in 2024 |
| [Context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Context retrieval, conversation compaction, and notes for longer tasks |

## Codex

| Source | Used for |
| --- | --- |
| [CLI setup](https://learn.chatgpt.com/docs/codex/cli) | Installation, sign-in, and launching in a project |
| [Desktop quickstart](https://learn.chatgpt.com/docs/quickstart) | Selecting the coding experience in the desktop app |
| [CLI commands](https://learn.chatgpt.com/docs/developer-commands) | Planning, permissions, model selection, and inspecting connected tools |
| [Desktop commands](https://learn.chatgpt.com/docs/reference/slash-commands) | Planning in the desktop interface |
| [Configuration basics](https://learn.chatgpt.com/docs/config-file/config-basic) | Shared `.codex/config.toml`, personal configuration, trust, and precedence |
| [Advanced configuration](https://learn.chatgpt.com/docs/config-file/config-advanced) | Project configuration limits, relative paths, and personal state |
| [Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference) | Supported model-provider fields and API compatibility |
| [Permissions](https://learn.chatgpt.com/docs/permissions) | Beta permission profiles and their incompatibility with mixed sandbox settings |
| [AGENTS.md discovery](https://developers.openai.com/codex/guides/agents-md) | Project hierarchy, personal instructions, and overrides |
| [Skills](https://developers.openai.com/codex/skills) | Project/user locations and explicit or implicit use |
| [Subagents and custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | TOML definitions, inherited settings, and delegation |
| [Approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security) | Sandbox, approvals, external tools, and hosted execution |
| [Plugin packaging](https://developers.openai.com/plugins/build/plugins) | Distributing reusable workflows and connections |

## Claude Code

| Source | Used for |
| --- | --- |
| [Quickstart](https://code.claude.com/docs/en/quickstart) | Installation, authentication, and first session |
| [Permission modes](https://code.claude.com/docs/en/permission-modes) | Entering Plan, exploration tools, plan approval, and implementation access |
| [Settings](https://code.claude.com/docs/en/settings) | Project and personal configuration locations |
| [Model configuration](https://code.claude.com/docs/en/model-config) | Session model choice, saved defaults, aliases, and planning/execution routing |
| [LLM gateways](https://code.claude.com/docs/en/llm-gateway) | Provider connections and supported model scope |
| [Tools reference](https://code.claude.com/docs/en/tools-reference) | File reading, editing, shell execution, and other tools |
| [Project memory](https://code.claude.com/docs/en/memory) | CLAUDE.md locations, imports, context inspection, and enforcement limits |
| [Skills](https://code.claude.com/docs/en/skills) | Discovery paths and invocation |
| [Subagents](https://code.claude.com/docs/en/sub-agents) | Markdown definitions and restricted reviewer tools |
| [Hooks reference](https://code.claude.com/docs/en/hooks) | Lifecycle events and their limits |

## GitHub Copilot

| Source | Used for |
| --- | --- |
| [CLI quickstart](https://docs.github.com/en/copilot/get-started/cli-quickstart) | Current CLI setup |
| [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) | CLI planning and permission commands |
| [CLI configuration directories](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference) | Current project and personal settings files |
| [VS Code session targets and roles](https://code.visualstudio.com/docs/agents/run/agent-harnesses) | Local Ask/Plan/Agent roles, execution locations, and handoffs |
| [VS Code planning](https://code.visualstudio.com/docs/agents/run/planning) | Reviewing a plan and starting implementation |
| [VS Code tools](https://code.visualstudio.com/docs/agents/run/tools) | Enabling tools and inspecting their results |
| [VS Code approvals](https://code.visualstudio.com/docs/agents/run/approvals) | Tool approval controls and their relationship to sandboxing |
| [VS Code language models](https://code.visualstudio.com/docs/agent-customization/language-models) | Model selection, external providers, and tool-calling support |
| [Changing the Copilot model](https://docs.github.com/en/copilot/how-tos/use-ai-models/change-the-chat-model) | Session model selection across clients |
| [Customization cheat sheet](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) | Instructions and feature support in different clients |
| [Adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | Supported locations, skill selection, and package review |
| [About custom agents](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents) | Agent profiles and project scope |
| [Custom agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration) | Front matter, tool aliases, and differences between clients |

## Cursor

| Source | Used for |
| --- | --- |
| [Quickstart](https://cursor.com/docs/get-started/quickstart) | Current setup |
| [Ask mode](https://cursor.com/help/ai-features/ask-mode) | Orientation and code explanation |
| [Plan mode](https://cursor.com/docs/agent/plan-mode) | Discussing a proposal and starting a build |
| [Agent](https://cursor.com/help/ai-features/agent) | Editing, command execution, and reviewing changes |
| [Run Modes](https://cursor.com/docs/agent/security/run-modes) | Approval settings for local execution and differences from cloud operation |
| [Available models](https://cursor.com/help/models-and-usage/available-models) | Selecting a model and checking availability |
| [API keys](https://cursor.com/help/models-and-usage/api-keys) | Personal provider keys and feature limitations |
| [Rules](https://cursor.com/docs/rules) | AGENTS.md and .mdc rule discovery |
| [Skills](https://cursor.com/docs/skills) | Shared/native skill paths and remote availability |
| [Subagents](https://cursor.com/docs/subagents) | Reviewer format, inherited model, and restricted writes |
| [Cloud Agents](https://cursor.com/docs/cloud-agent) | Hosted environments and review artifacts |

## Gemini CLI

| Source | Used for |
| --- | --- |
| [Getting started](https://geminicli.com/docs/get-started/) | Installation and authentication options |
| [Configuration reference](https://geminicli.com/docs/reference/configuration/) | Project and personal settings locations |
| [Settings dialog](https://geminicli.com/docs/cli/settings/) | Inspecting the configuration during the lesson |
| [Model selection](https://geminicli.com/docs/cli/model/) | Manual and automatic model choice and subagent differences |
| [Authentication](https://geminicli.com/docs/get-started/authentication/) | Access through Google sign-in, Gemini API keys, or Vertex AI |
| [Plan Mode](https://geminicli.com/docs/cli/plan-mode/) | Interactive planning, allowed tools, model routing, and headless differences |
| [Planning tools](https://geminicli.com/docs/tools/planning/) | Plan approval and the transition to implementation |
| [Policy engine](https://geminicli.com/docs/reference/policy-engine/) | Rules for allowing, denying, or asking about tool use |
| [Sandboxing](https://geminicli.com/docs/cli/sandbox/) | Isolation of tool execution |
| [GEMINI.md context](https://geminicli.com/docs/cli/gemini-md/) | Imports, custom filenames, and context inspection |
| [Skills](https://geminicli.com/docs/cli/skills/) | Shared/native locations, activation, and management commands |
| [Subagents](https://geminicli.com/docs/core/subagents/) | Agent files, tool restrictions, and invocation |
| [Behavioral evaluations](https://geminicli.com/docs/behavioral-evals/) | Distinguishing agent-workflow checks from ordinary code tests |

## University policy and lab data

These sources support [lab data and university policy](lab-data-policy.md). We reviewed the public guidance; the detailed Sensitive Data Guide service listings require U-M sign-in and were not inspected. Check those listings for the exact service and data type before a real study task.

| Source | Used for |
| --- | --- |
| [AI and U-M data](https://safecomputing.umich.edu/protect-the-u/safely-use-sensitive-data/AI-and-UM-Data) | Service agreements, permitted data use, and where to ask for help |
| [Data classification examples](https://safecomputing.umich.edu/protect-the-u/safely-use-sensitive-data/examples-by-level) | PHI, identifiable records, and context-dependent sensitivity |
| [Claude Code via U-M GPT Toolkit](https://its.umich.edu/computing/ai/claude-code-gpt-toolkit) | Eligibility, university setup, and the explicit ePHI exclusion |
| [ITS AI FAQ](https://its.umich.edu/computing/ai/faq) | Eligibility details that need checking against the service page and Toolkit portal |
| [Secure coding at U-M](https://safecomputing.umich.edu/protect-the-u/secure-coding) | Human review and risk in logs, dependencies, and deployment |
| [AI in human research](https://hrpp.umich.edu/aiinhumanresearch/) | Research use, study documentation, and IRB amendment scope |
| [Appropriate AI use](https://genai.umich.edu/resources/appropriate-use) | University responsibilities, review, and acknowledgment of AI assistance |
| [Incident reporting](https://safecomputing.umich.edu/report-it-security-incident) | Prompt reporting and unit-specific support routes |

## Maintaining these pages

A short rehearsal is useful before teaching a session or publishing a release. Focus on the clients you will actually demonstrate:

1. Reopen the pages for installation, mode selection, discovery paths, configuration examples, permissions, and feature availability. A working link is only part of the check; make sure its content still supports the instructions.
2. Try orientation, a plan-to-implementation handoff, skill discovery, and one small review in each client you intend to show. Record the version, model, selected modes and permissions, whether you used an editor, CLI, or hosted service, the operating system, and the result. These details will help a colleague troubleshoot a different outcome.
3. Update the review date for the material you actually checked. If a feature is unavailable or its documentation no longer supports an example, explain the limitation and remove the unsupported instructions.
4. Keep the exercise’s agreed behavior the same while updating client setup files. After changing filenames or navigation, recheck the examples and links.

The [agent workflow discussion](../platforms/trends.md) brings these documented features together and suggests ways to explore them in this repository. The sources establish what the tools describe as available. Claims about productivity, model rankings, scientific validity, or how much human review a task needs would require additional evidence.
