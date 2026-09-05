---
layout: default
title: 5. Review
parent: Lessons
nav_order: 5
---

# Review the change you will actually keep

Take about 15 minutes to read the change as if a labmate had sent it to you. Start with Git's overview, then look at the changed lines:

```bash
git status --short
git diff --stat
git diff
```

`git diff` shows changes to files Git already tracks. Open any new files listed by `git status` too, especially the fraction helper and new tests. Follow the change from the helper through the CLI to the summary and manifest, and check that the updated contract describes the same behavior.

A labmate or a fresh agent session can help spot assumptions you have stopped noticing. Give the reviewer the brief, diff, and test results so they can make their own assessment:

```markdown
Review the quality-gate change against docs/lessons/02-specify.md.
Read the implementation and tests. Run checks if your tools permit execution;
otherwise identify them as unrun and inspect the supplied test evidence.
Find defects with a concrete input, expected behavior, actual behavior, and
file location. Prioritize counting errors, equality at the limit, lost artifacts,
misreported status, and regressions. Do not edit files during this review.
Separate correctness findings from optional style preferences.
```

The included [review skill](../platforms/portable-context.md) supplies a reusable procedure for this kind of review. Keep the task brief and expected answers with the request, since they describe this particular change.

A second agent can offer another reading of the code, but agreement between agents does not validate the scientific method. If you work in parallel, give each agent a separate job—for example, one checks a source while another edits the code—and decide who will bring their results together. The [agent workflow discussion](../platforms/trends.md) explores this further.

## Check the gate and its outputs

- Does a row with two relevant reasons count once?
- Does exactly 20% pass, and more than 20% fail?
- Can the user distinguish QC failure from a malformed input or CLI argument?
- Are the files written before the QC failure is returned?
- Does the manifest describe the same decision as the summary?
- Are tests protecting the agreed method, or merely repeating its implementation?

Fix the problems that affect correctness, then rerun the affected tests and the full regression suite. You can leave optional refactoring ideas for another change. If a finding raises a question about the method itself, write down the question and who needs to decide it.

When you can explain the changed code and its test results together, you are ready to [hand it off](06-handoff.md).
