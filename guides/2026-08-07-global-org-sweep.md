---
date: 2026-08-07
session: global-org-sweep
tier: operator-guide
status: enriched
---

# The Arena Sweep — What We Built 2026-08-07 and How to Use It

> `_active/` went from 66 top-level folders to 12 (10 arenas + `_archive` + `_ledgers`) in 63 moves with **zero references broken**. The move tooling gained three fixes that make it safe to run again, and the session produced one transferable law: *a guard whose correctness depends on the layout it guards is not a guard*. Companion files: `.agent/organization/sweep-plan-2026-08-07.json` (plan of record) · `.agent/organization/REVERT-2026-08-07.sh` (72 move-backs) · `.agent/handoffs/2026-08-07-global-org-sweep.md` (next session) · `docs/solutions/2026-08-07-canonical-stamp-attractor-living-vs-record.md`.

## ⚡ If you only read 10 lines

1. **Never `mv` a project directory.** `python3 execution/project_relocate.py plan <src> <dst>` first — `plan` writes nothing and lists every referrer.
2. `"git does not track it"` ≠ `"nothing points at it"`. The untracked `claude-export` had **1,634** referrers.
3. `git mv` moves only TRACKED files **and exits 0** — it will silently relocate half a project. `apply` now drains the source; nothing may remain behind.
4. Front doors: `python3 execution/front_door.py build --all --quiet` (~4s, regenerates all). **Never hand-write an index.**
5. `front_door.py check` with **no args crashes** on `_resolve(None)`. Always `check --all`.
6. Arena shape is `_active/<arena>/<initiative>/<NN-bucket>/`. 10 arenas now: `clients harness offer-strategy knowledge farrice-brand video-studio linkedin publishing mybpm wagering`.
7. `_active/harness/codex-harvest-2026-06-11/` is a **copy of this repo**. Detection is depth-3; never narrow it, never rewrite inside it.
8. Archive is reversible: `_active/_archive/2026-08-07-sweep/` + `bash .agent/organization/REVERT-2026-08-07.sh`. Nothing was deleted.
9. Verify a move by mapping each missing pointer back through the plan against the **pre-sweep commit** — not by reading the tool's own success message.
10. Next job is **content** debt, not structure: `python3 execution/front_door.py check --all`.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `python3 execution/project_relocate.py plan <src-rel> <dst-rel>` | Referrer list + control-plane referrers. Writes nothing. | Always, before moving any directory. |
| `python3 execution/project_relocate.py apply <src-rel> <dst-rel> [--stub]` | `git mv` + rewrites every referrer + drains untracked leftovers + revert entry + receipt. | Moving a project for real. `--stub` only for archive moves. |
| `python3 execution/front_door.py build --all --quiet` | One `START-HERE.md` + `.html` per initiative (~4s). | After any move, rename, or archive. |
| `python3 execution/front_door.py check --all` | Drift report: competing versions, unabsorbed records, files claiming to be an index. Never blocks. | Deciding which duplicate is live. **`--all` is mandatory.** |
| `python3 execution/sweep_triage.py [--html] [--out OUT]` | Per-folder last-worked / inbound refs / control-plane citations / competing slots. | Before proposing any reorganisation. |
| `python3 execution/citation_integrity.py` | Every doc/memory pointer that references a missing file. | After a move, to prove nothing rotted. |
| `bash .agent/organization/REVERT-2026-08-07.sh` | Undoes the sweep, 72 move-backs. | Only if the shape is rejected. |

## The mental model

**Three ideas make the rest obvious.**

**1. A move is the operation that tests every path-dependent assumption at once.** Five bugs surfaced in this session and all five had one root cause: a rule written in terms of paths that did not survive the paths changing. The snapshot guard scanned a fixed depth. `is_arena()` assumed a directory is either project *or* arena. `git mv` silently means "tracked files only." `.gitignore` named an old path. And I assumed untracked meant unreferenced. None of these were wrong when written; all were wrong the moment the layout moved. **Before any migration, ask what each guard reads — if it reads the shape being migrated, widen it first.**

**2. Success and failure must not look identical.** The worst bug was not the loudest. `git mv` exiting 0 having moved half a project is far more dangerous than a crash, because every downstream check passed: the reference verifier confirmed all pointers valid, and it was right — *references* were correct, the *files* were elsewhere. Two different questions; only one was being asked. The same shape appeared in the push: `git push --quiet` hanging for an hour produces no output and no error, so the session that launched it believes it pushed.

**3. Verification inside the change cannot see what the change broke outside it.** The sweep looked perfect in its git lane. Merging to main is what revealed twelve projects split across old and new paths — because the gitignored halves only existed in the main tree.

## Capability 1 — `project_relocate.py`, hardened

**What it is.** Moves a project directory *with* its inbound links: `git mv` (history preserved), rewrites every referrer including control-plane files (`CLAUDE.md`, `directives/`, `execution/`), appends an inverse to `REVERT-<date>.sh`, writes a receipt. Three fixes landed this session.

- **Snapshot detection now walks to depth 3** (`_SNAPSHOT_SCAN_DEPTH`) and never descends into a snapshot it found. The old one-level scan would have found zero snapshots the instant the sweep landed — silently — and the next move would have rewritten history inside a 4,363-file harvest.
- **`apply` drains the source.** After `git mv`, anything remaining (gitignored `node_modules/`, `dist/`, `90-exports/`) is merged into the destination, destination always winning a name collision, then the empty shell is removed. Reported as `+ N untracked item(s) drained`.
- Frozen-by-design and unchanged: `_ledgers/`, `/move-plan.md`, `.agent/assets/manifest.jsonl`. A move-plan is a before/after record; rewriting it to its own after-state makes it describe moves it says haven't happened.

**When to reach for it.** Any time a project directory changes location or name.

**When NOT to.** Filing loose files *inside* a project — that is `project_filer.py`. And never for a snapshot directory's contents.

**Worked example.** `apply _active/claude-export _active/harness/claude-export` → **1,634 rewrites**. The same move done earlier as a plain `mv` orphaned all of them and broke six pointers visibly.

**Honest edges.** ~10s per move (a repo-wide grep per call), so 63 moves took 802s. The drain fix is proven by the repair it performed on main, but has not yet run inside a fresh `apply` on a project with gitignored content — the next such move is its real first test.

## Capability 2 — `front_door.py`, arena-aware

**What it is.** Generates the one `START-HERE.md` (+ Premium Minimal HTML) per initiative from the tree and from git. Dates mean *last actually worked on* — a 40+ file commit is housekeeping, a rename is not work.

- **`nested_initiatives()`** handles a directory that is both project and arena (`farrice-brand` has its own buckets *and* three initiatives moved in). A nested initiative must have its **own numbered buckets** — the first, broader rule ("any non-bucket child") wrote **48 front doors nobody asked for**.
- **`06-system/` never counts as evidence**, because this tool writes it. Counting it would mean the first bad run makes every later run agree.
- **`_archive/` is skipped.** An archive is a resting place, not a work surface.

**When to reach for it.** After any structural change; before trusting any index.

**When NOT to.** To *decide* anything. `build` describes; `check --all` reports drift. Neither picks the live file — that is a judgment call.

**Honest edges.** `check` with no args crashes (`_resolve(None)`) — one-line fix, unfixed. `farrice-master-context-2026-07-07` gets no front door of its own (no numbered buckets); it is covered by the parent's.

## What is NOT done

Content debt, untouched and deliberately so — it needs decisions, not tooling:

| Initiative | Competing slots | Unabsorbed records |
|---|---|---|
| `harness/codex-harvest-2026-06-11` | 86 | — (**snapshot — exclude, do not triage**) |
| `clients/andrea-dj` | 51 | — |
| `clients/coach-cooz` | 10 | — |
| `farrice-brand` | 8 | 2 |
| `linkedin` | 5 | 16 |

Also open: `.agent/content-finish-log.jsonl` and `guides/2026-07-27-.md` carry **committed conflict markers from July merges** — pre-existing, present at the merge-base, untouched here.

## Composition (options, never a pipeline)

| Stacks with | When it earns its cost |
|---|---|
| `worktree_lane.py merge` | Any restructure this size — the lane let 18 commits land as one reviewable merge, and parked cleanly on conflict rather than half-applying. |
| `sweep_triage.py` → Farrice's call → `project_relocate.py` | When the decision is "confirm N arenas," not "classify N projects." Grouping 66 folders into 18 turned an unanswerable question into a short one. |
| `citation_integrity.py` + pre-sweep commit | Proving a move broke nothing. Raw counts lie across checker versions — compare like for like. |
