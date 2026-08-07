---
thread: global-org-sweep
status: ready
resume_hint: Run front_door.py check --all and turn competing-versions into one decision surface grouped by slot
unfinished: Content debt: codex-harvest 86 competing slots (exclude - snapshot), andrea-dj 51, linkedin 16 unabsorbed records
branch: main
pin: true
---

# System: _active Arena Sweep - Shipped, Merged, Verified

## Purpose
- **Next session should do:** clear the CONTENT debt the sweep exposed. Structure is
  done and verified; what remains is deciding which of several near-duplicate files
  is the live one. Surface is `python3 execution/front_door.py check --all`.
- **Not in scope:** moving folders. The arena shape is settled and merged — 66
  top-level folders became 12. Re-opening it re-litigates a decision Farrice made.

## Load First
- `_active/clients/jen-listings/START-HERE.md` — a representative generated front
  door. Every initiative has one, and they are the ONLY files allowed to claim to
  be an index. Read the relevant one before touching that initiative.
- `.agent/organization/sweep-plan-2026-08-07.json` — the plan of record: what moved
  where, what was archived, and Farrice's two decisions with reasons.
- `_active/_ledgers/02-research/2026-08-07-sweep-decisions-proposal.md` — the
  PROPOSAL (18 arenas), superseded. Read only for how the call was made.
- `_active/_archive/MOVED.md` — living index of what was archived and how to undo.
- `docs/solutions/2026-08-07-canonical-stamp-attractor-living-vs-record.md`

## Current State
- **Objective:** make `_active/` navigable — one obvious front door per initiative,
  one living doc per slot, dated files understood as receipts.
- **What is already done:**
  - `_active/` 66 folders → **12** (10 arenas + `_archive` + `_ledgers`). 63 moves,
    0 failed. Farrice's calls: fold the 8 client arenas into one `clients/`, and
    archive the cold folders.
  - **0 references broken by the sweep** — verified by mapping every missing
    pointer back through the plan against the pre-sweep commit, not by assertion.
  - Merged to main (11 conflicts, resolved by class), lane torn down.
  - **Five bugs found and fixed**, all one root cause — *a path-shaped rule that
    does not survive the path changing*:
    1. `_snapshot_roots()` scanned one level deep; the sweep moves everything one
       level down, so it would have found zero snapshots *silently* and rewritten
       history inside a 4,363-file harvest.
    2. `is_arena()` is exclusive, but `farrice-brand` is now both project and
       arena. The naive fix wrote 48 front doors nobody asked for.
    3. Front doors generated inside `_archive/`, making retired work look live.
    4. `git mv` moves only TRACKED files and exits 0 — twelve projects ended up
       split across old and new paths (`node_modules/`, `dist/`, `90-exports/`).
       54 items reunited; `project_relocate.apply` now drains the source.
    5. A plain `mv` of the untracked `claude-export` orphaned **1,634** referrers,
       and put it at a path `.gitignore` didn't cover so 444 files got tracked.
- **What is uncertain or stale:**
  - **Content debt, untouched and the real next job:** `codex-harvest` 86 competing
    slots, `andrea-dj` 51, `coach-cooz` 10, `linkedin` 5 + 16 unabsorbed records,
    `farrice-brand` 8 + 2. "Competing" = several undated files claiming one slot.
  - `front_door.py check` with no args crashes on `_resolve(None)` — use `--all`.
  - **Pre-existing, NOT from this work:** `.agent/content-finish-log.jsonl` and
    `guides/2026-07-27-.md` carry *committed* conflict markers from July merges.
  - 58 `_active/` missing pointers remain — all pre-existing (baseline was 61).
- **Latest proof/receipt:** `.agent/organization/receipts/2026-08-07-relocate-*.json`
  (one per move) · `.agent/organization/REVERT-2026-08-07.sh` (72 move-backs,
  parses) · `.tmp/sweep-run.log`.

## Remaining Priority
Turn `front_door.py check --all` output into ONE decision surface grouped by slot —
rival files, last-worked date, inbound refs, recommended live file — and get
Farrice's confirmation before anything moves. `codex-harvest` (86 slots) is a repo
snapshot: exclude it, do not triage it.

## Do Not Rebuild
Already built and verified this session — extend, never redo:
- **The arena shape.** 66 → 12 is Farrice's decision, merged and verified. Do not
  re-propose 18 arenas, do not re-open the clients fold.
- **`execution/front_door.py`** — generates the one front door per initiative and
  understands arenas, hybrid project-arenas, and archives. Run `build --all`; do
  not hand-write a front door or write a second index file.
- **`execution/project_relocate.py`** — moves a directory WITH its inbound links,
  drains untracked leftovers, and refuses to rewrite inside repo snapshots. It is
  the only correct way to move a project. Do not write a new mover.
- **`execution/sweep_triage.py`** — computes last-worked / refs / control-plane /
  competing-slots per folder. Reuse it for the content pass instead of re-deriving.
- **The verification method:** map each missing pointer back through
  `sweep-plan-2026-08-07.json` and test it against the pre-sweep commit. That is
  how "0 broken by the sweep" was established — reuse it, don't re-invent it.

## Suggested Skills / Workflows
- `python3 execution/front_door.py check --all` — the decision surface. Start here.
- `python3 execution/front_door.py build --all` — regenerate after any move (~4s).
- `python3 execution/project_relocate.py plan <src> <dst>` — NEVER a bare `mv`;
  plan writes nothing and shows every referrer first.
- `/arsenal <task>` before building anything new.

## Exact Next Prompt
```text
Run `python3 execution/front_door.py check --all` and turn the "competing versions"
output into one decision surface, grouped by slot rather than by project — for each
slot show the rival files, when each was last actually worked on, and which one
inbound references point at, then recommend the live one. Start with codex-harvest
(86 slots) but treat it as FROZEN: it is a repo snapshot, so the answer there is
almost certainly "exclude it entirely," not "pick a winner." Do not move anything
until I confirm the recommendations.
```

## Acceptance Criteria
- One table per arena: slot · rival files · last-worked · inbound refs · recommended
  live file — Farrice confirms or overrides, nothing moves before that.
- `codex-harvest` correctly excluded as a snapshot rather than triaged.
- Any file promoted to living has no leading date; every dated rival stays as a record.

## Risk Notes
- **Never `mv` a project directory.** Use `project_relocate.py`. "Untracked" does
  not mean "nothing points at it" — claude-export had 1,634 referrers.
- `_active/harness/codex-harvest-2026-06-11/` is a copy of this repo. Rewriting
  inside it edits history. Detection is now depth-3; do not narrow it.
- `_ledgers/` and `move-plan.md` are FROZEN in `project_relocate` — a move-plan is a
  before/after record and must not be rewritten to its own after-state.
- Push COMPLETE and confirmed: `origin/main` == local `HEAD` (`6fb7dbde4`), verified
  by `git ls-remote`, not by the cached ref. Nothing outstanding.
- Four `git push --quiet` processes were found hung 1h+ at session start, launched by
  scripts. A `--quiet` push that stalls emits no output and no error, so the session
  that started it believes it pushed. If `origin` ever looks behind, check for hung
  pushes before assuming a failure.
