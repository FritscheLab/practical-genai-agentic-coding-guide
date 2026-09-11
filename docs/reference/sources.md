---
layout: default
title: Sources
parent: Reference
nav_order: 5
description: Find the official documentation behind the setup examples.
---

# Sources

Use this page when you want to check a setup detail, adapt an example, or prepare a session for colleagues. It collects the official documentation behind the [agent setup guide](../platforms/index.md) and notes what each source helps explain.

**Source review date: September 5, 2026.** These sources cover modes, tool access, paths, configuration fields, instruction discovery, and documented capabilities. The examples use those formats with tasks and file paths from the example repository.

A feature described in documentation still needs a hands-on check in the client you plan to use. Installation and sign-in links lead to the provider’s current instructions because account and operating-system requirements can change.

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

The [optional R refactoring walkthrough](../platforms/r-refactoring.md) has a narrower **September 10, 2026** documentation review: [Build skills](https://learn.chatgpt.com/docs/build-skills) supports the skill metadata, repository discovery, and explicit or description-based selection; [Custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents) supports the standalone TOML fields, inherited session settings, and delegation checks. Its formatting examples adapt Part 1's [R formatting conventions](https://fritschelab.org/practical-genai-coding-guide/docs/templates/R_CodeRefactoringPromptExample.html). These local examples require no Part 1 checkout. Documented discovery remains a separate check from observing it in a particular client.

## Claude Code

**Additional sandbox review: September 11, 2026.** [Claude sandbox scope](https://code.claude.com/docs/en/sandboxing#scope) distinguishes Bash subprocess restrictions from built-in file and computer-use tools. Copilot's terminal sandbox control does not configure Anthropic's native extension. Learners should actively select their intended mode in the [Claude prompt box](https://code.claude.com/docs/en/vs-code#use-the-prompt-box); do not infer it from sign-in. These controls were not tested in the Claude UI.

**Scoped review: September 11, 2026** for the [native VS Code extension](https://code.claude.com/docs/en/vs-code): installation, browser sign-in, bundled runtime, and edit review; the [VS Code permission-mode section](https://code.claude.com/docs/en/permission-modes#switch-permission-modes) supports the Plan/Manual controls in the short alternative path. CLI and customization material below retains its September 5 review date. Extension sign-in and mode transitions were not tested through the UI in this review.

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

**Additional permission/sandbox review: September 11, 2026.** The shared [permissions and independent-work guide](agent-control.md) uses the current [approval controls](https://code.visualstudio.com/docs/agents/run/approvals), [trust and safety concepts](https://code.visualstudio.com/docs/agents/concepts/trust-and-safety), and [security guidance](https://code.visualstudio.com/docs/agents/run/security). These support approval fatigue, saved-approval scope, terminal-only sandbox coverage, its preview/off-by-default status and documented macOS/Linux/WSL2 support, and separate approval handling for sandboxed commands. Current docs use Manual, Assisted, and Allow all; existing screenshots retain their observed Default permissions label. Sandbox activation, approval reset, and exception handling were not tested through the UI. Independent-work and proportionality advice is teaching guidance, not a clinical assessment or a claim about any country's laws.

**Scoped review: September 11, 2026** for the VS Code default workflow, current Student/Free account and Auto-model guidance, Chat targets/roles, approvals, models, and visual Git review. The CLI and optional customization references retain the September 5 review date. The planning URL was unavailable during the later review; plan handoff is supported by the session-target reference.

**Hands-on evidence, September 11, 2026:** in VS Code 1.137.0 on macOS 26.6.2, an authenticated Local session answered an Ask request, returned a Plan with an implementation handoff, and used Agent to run the Python behavior tests, render the flawed baseline, and verify a repaired figure. Source Control displayed real edits, staged the reviewed plotting source, and made a local commit in a disposable exercise copy. The captured client calls its approval control **Default permissions**; the documentation calls it **Manual permissions**. Windows installation and UI steps, student verification, and the Claude Code extension were not tested through their interfaces. Separate Python and R learner trials exercised the CLI appendix, including baseline rejection, repair verification, image/alt-text review, and local commits; those shell trials do not validate IDE controls.

| Interface step | macOS evidence | Windows evidence |
| --- | --- | --- |
| Install VS Code, Git, and a language runtime | Existing installations used; installers untested | Untested |
| Clone and trust a repository | Clone URL picker and opened exercise tested; complete network-clone and Trust-dialog flow untested | Untested |
| Select Python environment | Microsoft Python extension installed; workspace `.venv` selected | Untested |
| Use Copilot Chat | Authenticated Local Ask, Plan, and Agent tested, including command approval and expanded results | Untested |
| Compare files and plots | Explorer split PNG view and actual Python/R side-by-side diffs tested; inline-switch UI untested | Untested |
| Stage and commit | Source-only staging and local commit tested; identity-remedy prompt untested | Untested |

The screenshots show disposable public exercise copies. Repairs used for the diff and comparison illustrations came from the separate learner trials; the screenshots do not establish that Copilot authored those repairs. Physical print-size review and attaching alt text in a destination document remain untested.

| Source | Used for |
| --- | --- |
| [GitHub Copilot plans](https://docs.github.com/en/copilot/get-started/plans) | Copilot Student eligibility, Free/Student Auto selection, and current allowances |
| [VS Code Chat view](https://code.visualstudio.com/docs/agents/run/chat-view) | Opening Chat and distinguishing the four input controls |
| [VS Code Source Control](https://code.visualstudio.com/docs/sourcecontrol/overview) | Git integration and the repository workflow |
| [Staging, commits, and diffs](https://code.visualstudio.com/docs/sourcecontrol/staging-commits) | Changed-file badges, diff layouts, staging, and local commits |
| [CLI quickstart](https://docs.github.com/en/copilot/get-started/cli-quickstart) | Optional CLI appendix setup |
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

These sources support [lab data and university policy](lab-data-policy.md). Coverage is limited to public guidance; the detailed Sensitive Data Guide service listings require U-M sign-in and remain unverified here. Check those listings for the exact service and data type before a real study task.

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

## Using the sources

The [agent workflow discussion](../platforms/trends.md) brings these documented features together and suggests ways to explore them in the example repository. The sources establish what the tools describe as available. Claims about productivity, model rankings, scientific validity, or how much human review a task needs would require additional evidence.
