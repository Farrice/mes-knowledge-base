# Recipe Card Standard — the post-prompt form factor for job-shaped work

**Born 2026-09-09** from Nate B Jones's manager-loop video (youtube ix8SsXjBc7M) and one
on-disk scar: 54 open missions, the oldest 41 days, compiled by `/go` and never driven.
A prompt can name a task. It cannot carry a job that crosses systems, has dependencies, and
changes mid-run. A **recipe card** can. It is "a map to the work" — Nate's words — and it is
what the manager agent reads instead of a fourteen-part spec nobody wants to write.

**Goal the rule serves:** Farrice hands off something ambiguous and light, walks away, and
comes back to decisions, not status. **Scar it closes:** every mission layer before this one
planned well and then handed the job back at the end of every turn.

## One card = one named job (LIVING doc)

- Lives at `recipes/<job-slug>.md`. **No date in the filename** — a card is updated in place,
  never re-issued (artifact-placement LIVING vs RECORD rule).
- Instantiated per run into `.agent/missions/<slug>/card.md` by `job_board.py open --recipe`,
  with the interview answers filled in. The instance is a RECORD; the recipe is the LIVING truth.
- Written **from the workflows that already run the job**, never invented. A card that names a
  lane no workflow can execute is drift; `recipe_cards.py lint` flags it.
- Fits on one page. Sub-jobs are a sketch, not a spec — the manager fills detail at run time.

## Schema (every section present; empty sections say `none`)

```markdown
---
job: <slug>                         # == filename
name: <Human name of the job>
family: client-content | harvest-research | revenue-launch | harness
tier_default: T1 | T2               # Blast-Radius tier most runs land in (orchestration-doctrine)
runs: <int>                         # incremented by job_board.py close
last_ratchet: <YYYY-MM-DD | never>
---

## The job
One sentence: the outcome, in the words Farrice would use.

## Sub-jobs / lanes
- L1 <name> — what it produces [parallel]
- L2 <name> — … [after: L1]
Tags: [parallel] = independent; [after: X] = dependency. The manager runs every lane whose
dependencies are met, at the same time.

## Ask me first
Only questions whose answer CHANGES EXECUTION. Each question names where to look on disk
before asking (Partner Posture 2 — facts are researched, only voice and verdicts are asked).
- Q: …  · look first: <path>

## Handles alone
What the manager does without interrupting: research, comparison, drafts, renders, file
moves, lints, verifiers, lane worktrees, background read-only seats.

## Comes back when
The moments that produce a DECISION PACKET: choices, irreversible calls, anything the card's
`Needs approval` names, sources that disagree on a fact that matters, a bar not met twice.

## Needs approval
T2/T3 actions by name (publish, send, spend, delete outside repo, ship AS Farrice). The
manager stops before these every time, standing grants excepted.

## Needs
Files, folders, access, tools, budgets. Missing = a lane marks `blocked:<what>` and the rest
keep moving.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| source missing | search the three locations, mark UNCONFIRMED | never invent |
| sources disagree | carry both, label LIKELY/UNCONFIRMED | the disagreement changes the deliverable |
| tool/site blocks | alternate route (Playwright, fetch-video-context, cached copy) | two routes fail |
| bar not met | one rewrite from the brief | second miss = packet, not a third take |
(extend per job; rows above are the floor)

## Done means
Verifiable receipts: paths that exist, commands that pass, a Drive folder populated. Never
"drafted" or "looked at".

## Ratchet log
- YYYY-MM-DD — what broke · what he answered · what changed in the card
```

## Decision packet (the come-back form)

```
DECISION PACKET — <job>/<lane>
Choice: <one line>
Irreversible? yes|no — <what can't be undone>
Options: A <…> / B <…> — recommend <A|B>: <one line why>
If no answer: <what the manager does / holds>
```

Packets are batched; the manager never asks mid-run except for a T3 action. He answers with
`job_board.py packet <slug> answer <n> "<his words>"` or in plain chat — the manager records
it either way.

## Closeout (Nate's four questions, answered with receipts)

1. Is it done? (paths)  2. Did the actions line up with what he asked?  3. Any unauthorized
actions? (every T2/T3 named)  4. Was he told each time approval was needed?  Then the recipe
gets one ratchet line and `runs` increments. A job without a closeout is a debt the pulse
board surfaces.

## Where cards come from

- `job_board.py open --recipe <slug>` when a match exists (`recipe_cards.py match "<ask>"`).
- `recipe-card-forge` workflow (skill `nate-b-jones-manager-loop`) when none does — written from
  the workflows/files that already run the job, then saved to `recipes/` so the next run matches.
- `/extract-approach` still owns solved-PROBLEM cards in `docs/solutions/`; recipe cards are
  JOB maps. A recipe may cite solution cards in its lanes.
