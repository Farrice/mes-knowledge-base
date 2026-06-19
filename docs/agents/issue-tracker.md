# Issue tracker: Local Markdown

> Wired by `/setup-matt-pocock-skills` on 2026-06-15 for the Antigravity repo. Tracker = local markdown (sovereign, portable, no `gh`/`glab` dependency). Edit this file to switch trackers.

Issues and PRDs for this repo live as markdown files in `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- The PRD is `.scratch/<feature-slug>/PRD.md`
- Implementation issues are `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`
- Triage state is recorded as a `Status:` line near the top of each issue file (see `triage-labels.md` for the role strings)
- Comments and conversation history append to the bottom of the file under a `## Comments` heading

## When a skill says "publish to the issue tracker"

Create a new file under `.scratch/<feature-slug>/` (creating the directory if needed).

## When a skill says "fetch the relevant ticket"

Read the file at the referenced path. The user will normally pass the path or the issue number directly.

## Antigravity note

`.scratch/` is for transient dev-process artifacts (PRDs, issues, triage). It is NOT the same as the system's `.tmp/` intermediates or `deliverables/`. Keep client/content deliverables in their canonical locations; `.scratch/` is only for the engineering-skill issue workflow.
