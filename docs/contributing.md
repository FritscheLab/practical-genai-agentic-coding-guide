---
layout: default
title: Contribute
nav_order: 9
---

# Contribute to the guide

If a step is confusing, a command fails, or a provider has changed its setup, please help us improve it. A small example showing the problem is often the most useful contribution. For tool guidance, include the current official source so the next person can check it too. Repository instructions are in [AGENTS.md](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/AGENTS.md).

## Set up Python and check the exercise

Use **Python 3.12** for the documented workshop environment. Python **3.10–3.12** is supported by its pinned dependencies; newer interpreters need a separately reviewed dependency update. The package's broader runtime requirements in `pyproject.toml` are distinct from this reproducible teaching environment.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest
python -m ruff check .
python scripts/py/check_example_data.py
python examples/qc_gate/verify_solution.py
```

See [Start here](quickstart.md) for Windows activation. `requirements-dev.txt` installs the editable package and `constraints-dev.txt` records the resolved dependencies. After deliberately updating dependencies, test a fresh environment, review the resolved versions, update the recorded constraints, and rerun the baseline and instructor solution. Do not regenerate the file from a global environment containing unrelated packages.

Keep the quality gate outside the published baseline. The instructor verifier copies the package into a temporary directory and runs both baseline and exercise checks against the reference solution. If changing the underlying CLI, update the reference CLI and rerun that verifier.

## Website

The site uses Ruby **3.3**, Jekyll **4.4.1**, and Just the Docs **0.12.0**, matching Part 1. Dependencies are recorded in `Gemfile` and `Gemfile.lock`.

```bash
bundle install
bundle exec jekyll build --strict_front_matter
python scripts/py/check_site.py _site
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Open `http://127.0.0.1:4000/practical-genai-agentic-coding-guide/`. The link checker validates rendered internal pages, assets, and fragment targets without using the network; it does not check external source availability or visual accessibility. Inspect the changed pages on desktop and mobile, test keyboard navigation and search, and check cited external sources separately.

If Conda or Miniforge exports compiler variables, native gem builds can fail. On macOS with Homebrew Ruby 3.3, use:

```bash
env -u CC -u CXX -u LD -u LDFLAGS -u CPPFLAGS -u CFLAGS \
  PATH=/opt/homebrew/opt/ruby@3.3/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin \
  bundle exec jekyll build --strict_front_matter
```

Adapt the Ruby path to the installed environment. Keep `_site/`, `.bundle/`, `.jekyll-cache/`, and installed gems ignored.

## Navigation and content

Give public pages front matter with `layout`, `title`, `parent` where appropriate, and `nav_order`. Keep `README.md` for GitHub and `index.md` for the website. Use relative Markdown links between guide pages; link to GitHub for source files excluded from the website. Maintain the Part 1 link and lab navigation when editing the theme.

Use plain language and specific examples. Keep copyable prompts in fenced blocks. Remove superseded content rather than adding a second competing explanation. General R templates remain in Part 1. Part 2's synthetic rules must stay explicit and must not be presented as clinical guidance.

Keep examples and screenshots synthetic. Follow [lab data and university policy](reference/lab-data-policy.md) when reviewing material for publication, including logs, paths, credentials, and acknowledgments of AI assistance. University service permissions and study approvals must be checked for the actual use; the presence of a client setup page here is not an approval.

For platform changes, fetch the current official documentation, verify the exact command or path, update the affected setup page and its review date, and record the source in the [source index](reference/sources.md). A documented configuration is not the same as a tested account/client session; report that distinction.

## Regenerate data and build slides

The [data reference](reference/synthetic-data.md) explains regeneration and expected counts. If changing the simulator or fixtures, reproduce them in a separate directory and update provenance deliberately. Only small synthetic examples belong in Git.

The slide source is `docs/lab_meeting/slide_deck.qmd`, rendered with Quarto **1.8.26**:

```bash
quarto render docs/lab_meeting/slide_deck.qmd
```

Open the generated HTML and inspect all slides at presentation size. Keep generated HTML and its supporting directory ignored. The runbook and lessons are the primary teaching instructions; update the slides when their exercise changes.

## Getting a release ready

The repository includes two workflows: Python tests, lint, fixture regeneration and slide rendering; and the website build with internal link checks. The website workflow builds pull requests and deploys only from the default branch.

For the first public release:

1. Review the candidate diff, metadata, and generated-file exclusions; commit the intended source files.
2. Create or connect the GitHub repository, push the reviewed revision, and confirm the workflows actually pass there.
3. Configure GitHub Pages to use **GitHub Actions**, then verify the public site and reciprocal Part 1/lab links. See [GitHub Pages setup](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
4. Tag the checked revision, publish release notes, and record the actual release version/date in `CITATION.cff`. Add an archive identifier only after it exists.

After pushing, open the workflow results and visit the public site. Local checks help us prepare; this final check tells us what readers can actually reach.

## Attribution

The simulator derives from Part 1 at the revision recorded in [synthetic data provenance](reference/synthetic-data.md). The task and handoff templates adapt Part 1's maintained teaching approach. The website's design and lab marks are shared with the Fritsche Lab website and Part 1. The guide and examples use the repository's [GPL-3.0 license](https://github.com/FritscheLab/practical-genai-agentic-coding-guide/blob/main/LICENSE). Third-party build dependencies retain their own licenses.
