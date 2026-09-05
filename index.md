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
  <p class="guide-lead">Work through a small project with a coding agent, learn how to check its work, and leave the next person a project they can pick up.</p>
  <div class="guide-actions">
    <a class="btn btn-primary" href="{{ '/docs/quickstart.html' | relative_url }}">Start with the demo <span aria-hidden="true">→</span></a>
    <a class="btn" href="{{ '/docs/lessons/' | relative_url }}">Explore the lessons</a>
  </div>
  <p class="guide-meta">A Fritsche Lab teaching guide · University of Michigan</p>
</section>

<div class="guide-strip" aria-label="What to expect">
  <div><strong>One working example</strong><span>A Python pipeline with synthetic BMI and demographics data.</span></div>
  <div><strong>Your choice of agent</strong><span>Use a supported coding tool with the same goals and checks.</span></div>
  <div><strong>Understand what changed</strong><span>Work out the answer, inspect the changes, and check the result.</span></div>
</div>

## Pick up where Part 1 leaves off

[Part 1: Practical GenAI Coding Guide](https://fritschelab.org/practical-genai-coding-guide/) takes us through planning, prompting, reviewing, and documenting code, including work with coding agents. Here we put those habits to work in a project with several moving parts: a Python package, tests, documentation, and saved results.

We use one small example throughout, so you can follow a change from the original request to the files you would share with a collaborator. Along the way, you will give the agent useful context, catch plausible mistakes, and decide when the result is ready to keep.

If you are new to using GenAI for coding, begin with Part 1. If you can already run a script and inspect a change, [start here]({{ '/docs/quickstart.html' | relative_url }}).

<section class="guide-section" aria-labelledby="learning-heading">
  <div class="guide-section-heading">
    <p class="guide-eyebrow">A practical learning path</p>
    <h2 id="learning-heading">From the first run to a reviewed change</h2>
    <p>Keep the project small so you can see the whole workflow.</p>
  </div>
  <ol class="guide-learning-path">
    <li><span class="guide-step-number" aria-hidden="true">01</span><div><h3>Establish a working baseline</h3><p>Install the demo, run the tests, and inspect a completed run before asking an agent to edit anything.</p><a href="{{ '/docs/quickstart.html' | relative_url }}">Run the quickstart <span aria-hidden="true">→</span></a></div></li>
    <li><span class="guide-step-number" aria-hidden="true">02</span><div><h3>Make the repository understandable</h3><p>Use a README, agent instructions, a repository map, and data contracts to make expectations explicit.</p><a href="{{ '/docs/practices/' | relative_url }}">Explore repository practices <span aria-hidden="true">→</span></a></div></li>
    <li><span class="guide-step-number" aria-hidden="true">03</span><div><h3>Choose one small improvement</h3><p>Describe the change and how you will check it. Review its plan and the files it changes.</p><a href="{{ '/docs/lessons/' | relative_url }}">Work through the lessons <span aria-hidden="true">→</span></a></div></li>
    <li><span class="guide-step-number" aria-hidden="true">04</span><div><h3>Leave a useful result</h3><p>Run the checks, inspect the outputs, and leave enough detail for a labmate to rerun the work.</p><a href="{{ '/docs/reference/' | relative_url }}">Read the pipeline reference <span aria-hidden="true">→</span></a></div></li>
  </ol>
</section>

<section class="guide-section" aria-labelledby="resources-heading">
  <div class="guide-section-heading">
    <p class="guide-eyebrow">Make it useful in your own work</p>
    <h2 id="resources-heading">Choose what you need next</h2>
  </div>
  <div class="guide-resource-grid">
    <div><h3>Set up your agent</h3><p>Prepare a coding tool to work with this repository.</p><a href="{{ '/docs/platforms/' | relative_url }}">Agent setup <span aria-hidden="true">→</span></a></div>
    <div><h3>Reuse the templates</h3><p>Write a task brief, agree on the data, or hand off unfinished work.</p><a href="{{ '/docs/templates/' | relative_url }}">Browse templates <span aria-hidden="true">→</span></a></div>
    <div><h3>Teach a lab session</h3><p>Use the 45-minute runbook and a focused live exercise.</p><a href="{{ '/docs/lab_meeting/' | relative_url }}">Teaching materials <span aria-hidden="true">→</span></a></div>
  </div>
</section>

<aside class="guide-note" aria-labelledby="demo-heading">
  <h2 id="demo-heading">A teaching project you can inspect</h2>
  <p>The example data are synthetic. The pipeline cleans measurements, flags quality issues, and summarizes one row per person. You can inspect the whole example and work out what its rules should do. For a study of your own, start by agreeing on the scientific method with your collaborators.</p>
  <p><a href="https://github.com/FritscheLab/practical-genai-agentic-coding-guide">Get the code and example data on GitHub</a> or <a href="{{ '/docs/contributing.html' | relative_url }}">help improve the guide</a>.</p>
</aside>
