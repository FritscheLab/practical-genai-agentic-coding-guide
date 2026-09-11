# Practical GenAI Agentic Coding Guide

**[Read the online guide](https://fritschelab.org/practical-genai-agentic-coding-guide/).** Repair a Python or R plot in **VS Code + GitHub Copilot**. Use Chat to understand, plan, and run code; inspect plots in Explorer and color-coded diffs in Source Control.

This is Part 2 of the [Practical GenAI series](https://fritschelab.org/practical-genai-coding-guide/), from [Lars G. Fritsche](https://medschool.umich.edu/profile/4980/lars-fritsche) and the [Fritsche Lab](https://fritschelab.org/) at the University of Michigan.

**Practising what we teach:** this guide and exercise were developed with substantial AI assistance in writing, coding, testing, and review. They are provided **as is, without warranty**, to the extent permitted by applicable law. Review the code, agent instructions, permissions, and results before use. Read the [AI-assistance disclosure, use guidance, and warranty notice](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/reference/agent-control.html#about-ai-assistance-in-this-guide).

## Get the exercise

Follow the **[VS Code + Copilot setup](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/setup/vscode-copilot.html)** to install the tools, sign in, and clone the **[example repository](https://github.com/FritscheLab/practical-genai-agentic-coding-example)** through Source Control. The download includes code, invented totals, tests, and offline lessons.

Choose [Python](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/paths/python/) or [R](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/paths/r/), then follow six lessons through a reviewed local commit and handoff. Bring basic Python/R knowledge; the guide explains Git and requires no typed shell commands on the main path. Plotting itself needs no model API or credentials; Copilot requires account access.

Prefer another interface? Use the [Claude Code extension alternative](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/platforms/claude-code.html#use-the-vs-code-extension) or the complete [CLI appendix](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/appendix/command-line.html).

Include accessibility in every figure: contrast, readable labels, and reviewed alternative text.

## Explore the guide

- [Permissions and independent work](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/reference/agent-control.html): approval fatigue, sandbox limits, maintainable code, and avoiding overreliance.
- [Agent setup and alternatives](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/platforms/): understand Copilot's controls or adapt the exercise to another client.
- [Optional R refactoring example](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/platforms/r-refactoring.html): reuse a lab formatting skill or named Codex agent, then verify that results stay the same.
- [Repository practices](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/practices/): context, testing, logs, and handoffs.
- [Teaching materials](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/lab_meeting/): a 45-minute workshop and slides.
- [Lab data guidance](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/reference/lab-data-policy.html): institutional requirements before adapting the workflow to study data.

## Preview the website

This repository contains the Jekyll website and workshop slides. To preview the site locally with Ruby and Bundler installed:

```bash
bundle install
bundle exec jekyll serve
```

Open the address printed by Jekyll. To check a build:

```bash
bundle exec jekyll build --strict_front_matter
python3 scripts/py/check_site.py _site
```

With [Quarto](https://quarto.org/) installed, render the slides with `quarto render docs/lab_meeting/slide_deck.qmd` and open the resulting HTML. Website and slide output stays out of Git.

## Attribution and citation

The site uses the Fritsche Lab theme and Just the Docs. Synthetic data and reusable templates build on Part 1; see [synthetic data provenance](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/reference/synthetic-data.html).

Use [CITATION.cff](CITATION.cff) to cite this guide. [GNU General Public License v3.0](LICENSE).
