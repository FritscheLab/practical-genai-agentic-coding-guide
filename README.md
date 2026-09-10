# Practical GenAI Agentic Coding Guide

**[Read the online guide](https://fritschelab.org/practical-genai-agentic-coding-guide/).** Choose [Python](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/paths/python/) or [R](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/paths/r/), then repair a plot with a coding agent in six lessons.

This is Part 2 of the [Practical GenAI series](https://fritschelab.org/practical-genai-coding-guide/), from [Lars G. Fritsche](https://medschool.umich.edu/profile/4980/lars-fritsche) and the [Fritsche Lab](https://fritschelab.org/) at the University of Michigan.

## Get the exercise

Download the **[example repository](https://github.com/FritscheLab/practical-genai-agentic-coding-example)** for code, invented totals, tests, and offline lessons. Follow the website alongside it.

```bash
git clone https://github.com/FritscheLab/practical-genai-agentic-coding-example.git
cd practical-genai-agentic-coding-example
```

Start with its README and language setup. Bring basic Python/R and terminal skills; the lessons explain Git. Plotting needs no model API or credentials. Use an institution-approved coding assistant for the agent exercise.

Include accessibility in every figure: contrast, readable labels, and reviewed alternative text.

## Explore the guide

- [Agent setup](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/platforms/): configure your coding client and check its access.
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
