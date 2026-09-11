---
layout: default
title: Home
nav_order: 1
description: Turn the coding practices from Part 1 into an agent workflow you can inspect, test, and repeat.
has_toc: false
---

<section class="guide-hero" aria-labelledby="guide-title">
  <p class="guide-eyebrow">Practical GenAI · Part 2</p>
  <h1 id="guide-title">Build research code<br>you can explain.</h1>
  <p class="guide-lead">Repair a Python or R plot in VS Code with GitHub Copilot. Ask about the code, review a plan, and inspect every change before saving it in Git.</p>
  <div class="guide-actions">
    <a class="btn btn-primary" href="{{ '/docs/paths/python/' | relative_url }}">Start with Python <span aria-hidden="true">→</span></a>
    <a class="btn btn-primary" href="{{ '/docs/paths/r/' | relative_url }}">Start with R <span aria-hidden="true">→</span></a>
  </div>
  <p class="guide-meta">A Fritsche Lab teaching guide · University of Michigan</p>
</section>

<div class="guide-strip" aria-label="What to expect">
  <div><strong>Two language paths</strong><span>Choose Python or R for the same plotting exercise.</span></div>
  <div><strong>Work in VS Code</strong><span>Use Copilot Chat to run code and Explorer to open plots.</span></div>
  <div><strong>See what changed</strong><span>Review changed files and color-coded diffs in Source Control.</span></div>
</div>

**Practising what we teach:** this guide and exercise were developed with substantial AI assistance in writing, coding, testing, and review. They are provided **as is, without warranty**, to the extent permitted by applicable law. Review the code, agent instructions, permissions, and results before use. Read the [AI-assistance disclosure, use guidance, and warranty notice](docs/reference/agent-control.md#about-ai-assistance-in-this-guide).

## Pick up where Part 1 leaves off

[Part 1](https://fritschelab.org/practical-genai-coding-guide/) introduced planning, prompting, and reviewing code. Here you put those habits to work on a plot with overlapping bars and clipped labels.

Choose Python or R, complete the [VS Code + Copilot setup](docs/setup/vscode-copilot.md), and follow six lessons online or offline. Clone the example through Source Control, repair the plot without changing its values, and leave a result a labmate can rerun. You can complete the main path without typing shell commands.

Prefer Claude Code? Its [VS Code extension](docs/platforms/claude-code.md#use-the-vs-code-extension) supports the same exercise and visual Git review. Command-line users have a complete [CLI appendix](docs/appendix/command-line.md).

**Keep your judgment and coding skills.** Working output can hide code you cannot explain or maintain. Review permissions, keep changes proportional to the task, and practise without AI so your work can continue if access becomes unavailable or prohibited. Read [permissions and independent work](docs/reference/agent-control.md).

![Grouped bars compare invented measurement-completeness counts for Groups A and B. Group B has more complete measurements, 64 versus 42; the linked specification lists all category values.](assets/images/plotting-target.png)

Your target: a readable chart for the fictional **Journal of Unnecessarily Specific Figures (JUSF)**. The [exercise](docs/lessons/02-specify.md) shows the problem; its local [figure specifications](docs/reference/figure-specifications.md) give the rules.

Make accessibility part of every figure: readable labels, sufficient contrast, groups identifiable without color, and reviewed alternative text.

If you are new to using GenAI for coding, begin with Part 1. If you already work in Python or R, [start here]({{ '/docs/quickstart.html' | relative_url }}); the lessons explain the agent controls and Git review.

<section class="guide-section" aria-labelledby="learning-heading">
  <div class="guide-section-heading">
    <p class="guide-eyebrow">A practical learning path</p>
    <h2 id="learning-heading">From the first run to a reviewed change</h2>
    <p>Keep the project small so you can see the whole workflow.</p>
  </div>
  <ol class="guide-learning-path">
    <li><span class="guide-step-number" aria-hidden="true">01</span><div><h3>Establish a working baseline</h3><p>Set up VS Code, ask Copilot to run the existing checks, and open the baseline plot in Explorer.</p><a href="{{ '/docs/quickstart.html' | relative_url }}">Open the quickstart <span aria-hidden="true">→</span></a></div></li>
    <li><span class="guide-step-number" aria-hidden="true">02</span><div><h3>Make the repository understandable</h3><p>Use a README, agent instructions, a repository map, and data contracts to make expectations explicit.</p><a href="{{ '/docs/practices/' | relative_url }}">Explore repository practices <span aria-hidden="true">→</span></a></div></li>
    <li><span class="guide-step-number" aria-hidden="true">03</span><div><h3>Choose one small improvement</h3><p>Use Ask to understand, Plan to agree on the repair, and Agent to implement and check it.</p><a href="{{ '/docs/lessons/' | relative_url }}">Work through the lessons <span aria-hidden="true">→</span></a></div></li>
    <li><span class="guide-step-number" aria-hidden="true">04</span><div><h3>Leave a useful result</h3><p>Compare the plots, review each diff in Source Control, and commit the source with a useful handoff.</p><a href="{{ '/docs/practices/repo_navigation.html' | relative_url }}">Learn visual Git review <span aria-hidden="true">→</span></a></div></li>
  </ol>
</section>

<section class="guide-section" aria-labelledby="resources-heading">
  <div class="guide-section-heading">
    <p class="guide-eyebrow">Make it useful in your own work</p>
    <h2 id="resources-heading">Choose what you need next</h2>
  </div>
  <div class="guide-resource-grid">
    <div><h3>Set up VS Code + Copilot</h3><p>Install the tools, sign in, clone the exercise, and make the first plot.</p><a href="{{ '/docs/setup/vscode-copilot.html' | relative_url }}">Detailed setup <span aria-hidden="true">→</span></a></div>
    <div><h3>Reuse the templates</h3><p>Write a task brief, agree on the data, or hand off unfinished work.</p><a href="{{ '/docs/templates/' | relative_url }}">Browse templates <span aria-hidden="true">→</span></a></div>
    <div><h3>Teach a lab session</h3><p>Use the 45-minute runbook and a focused live exercise.</p><a href="{{ '/docs/lab_meeting/' | relative_url }}">Teaching materials <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<aside class="guide-note" aria-labelledby="demo-heading">
  <h2 id="demo-heading">A teaching project you can inspect</h2>
  <p>The counts are invented and embedded in code. The agent works with source, tests, and images; no participant records are needed.</p>
  <p><a href="https://github.com/FritscheLab/practical-genai-agentic-coding-example">Get the exercise on GitHub</a>.</p>
</aside>
