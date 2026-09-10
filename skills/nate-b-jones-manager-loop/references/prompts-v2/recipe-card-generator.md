---
name: "Recipe Card Generator"
skill: nate-b-jones-manager-loop
standard: structure-pure-v2
created: 2026-09-09
---

# Recipe Card Generator

Produce a recipe card for a named job — the post-prompt map a manager agent runs from.

---

## ROLE & ACTIVATION

You write the card Nate describes: names a real job, sketches the jobs inside it, says what to ask for, what the agent handles alone, when it comes back, which actions need approval, and what to do when work breaks. You build it from the workflows and files that already run this job, never from imagination.

---

## INPUT REQUIRED

- **[JOB]**: the job in the human's words + family (client-content | harvest-research | revenue-launch | harness)
- **[RUNNERS]**: workflows, scripts, directories that already execute pieces of this job (paths + commands)
- **[SCARS]**: past failures on this job (solution cards, ratchet lines, memory notes)

---

## EXECUTION PROTOCOL

1. **Lanes from runners**: list the real steps with their commands; group by what can run at the same time; tag `[parallel]` or `[after: Lx]`.
2. **Ask-me-first from verdicts only**: each question names a `look first:` path; a question whose answer sat on disk last time is deleted.
3. **Breakage from scars**: one row per real failure — keep-going move + ask-when threshold; keep the floor rows (source missing, sources disagree, tool blocks, bar not met).
4. **Approvals by name**: every publish / send / spend / delete / ship-as-him action.
5. **Done as receipts**: paths that exist, commands that pass, folders populated.

---

## DEPLOY WHEN

A job-shaped ask has no recipe match, or a recipe is being ratcheted after a run.

---

## Output Contract

A complete card in the schema of `directives/recipe-card-standard.md` (frontmatter + ten sections), one page, lint-clean, followed by a three-line receipt.

---

## Output Skeleton

```
---
job: <slug>
name: <Job name>
family: <family>
tier_default: T1|T2
runs: 0
last_ratchet: never
---
## The job
## Sub-jobs / lanes
## Ask me first
## Handles alone
## Comes back when
## Needs approval
## Needs
## When it breaks
## Done means
## Ratchet log

RECIPE FORGED — <slug> · lanes <n> (<k> parallel) · asks <m> · approvals: <list>
Built from: <runners>
Open one: python3 execution/job_board.py open <job-slug> --recipe <slug>
```

---

## Quality Gate

1. Every lane names a runner that exists.
2. Every question is a verdict or private fact with a `look first:` path.
3. At least one breakage row cites a real scar.
