# Practical GenAI Agentic Coding Guide

**[Read the online guide](https://fritschelab.org/practical-genai-agentic-coding-guide/).** Choose [Python](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/paths/python/) or [R](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/paths/r/), then follow six lessons through one reporting change, verification, review, and a short handoff.

This is Part 2 of the [Practical GenAI series](https://fritschelab.org/practical-genai-coding-guide/), from [Lars G. Fritsche](https://medschool.umich.edu/profile/4980/lars-fritsche) and the [Fritsche Lab](https://fritschelab.org/) at the University of Michigan.

## Get the exercise

The runnable Python/R pipeline, synthetic data, tests, and agent instructions are in the **[example repository](https://github.com/FritscheLab/practical-genai-agentic-coding-example)**. Download only that repository and follow along online. It also includes the language walkthroughs for offline use.

```bash
git clone https://github.com/FritscheLab/practical-genai-agentic-coding-example.git
cd practical-genai-agentic-coding-example
```

Start with its README and your chosen language's setup. You should be comfortable running a Python or R script and using a terminal; the lessons explain the Git steps. The baseline uses synthetic data and needs no model API or credentials. Use an institution-approved coding assistant for the agent exercise.

## Explore the guide

- [Agent setup](https://fritschelab.org/practical-genai-agentic-coding-guide/docs/platforms/): configure your coding client and check its access.
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
