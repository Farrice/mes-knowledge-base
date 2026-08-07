---
date: 2026-08-04
session: global-org-sweep
tier: operator-guide
status: enriched
---

# Global Org Sweep — What We Built and How to Use It

> Repo retrieval is now self-maintaining. `projects/` was dissolved into `_active/` (one tree), ~29,300 files were relocated across 60 verified operations with nothing deleted, and `PROJECTS.md` became a **generated** front door that regenerates at session close and 06:00 daily. Three new tools shipped: `execution/projects_index.py`, `execution/project_relocate.py`, `execution/verify_project_filer.py`. Companions: `.agent/missions/global-org-sweep/move-plan.md` (the plan + executed outcomes), `directives/artifact-placement.md` (the filing contract these enforce), `.agent/handoffs/2026-08-04-global-org-sweep.md`.
>
> Tier note: the spine detected `session-brief` because this cycle's commit carried only telemetry — the operator assets landed in commits `10539d076`…`7d4efb489`. The session shipped operator assets, so this is written at operator-guide tier.

## ⚡ If you only read 10 lines

1. **`PROJECTS.md` is generated — never hand-edit it.** `python3 execution/projects_index.py sync`
2. Project status lives in that project's own `INDEX.md` frontmatter: `status: active | parked | done`.
3. **`done` is never derived.** Unstamped status derives from git (<30d = active); stamping is an opt-in override.
4. `python3 execution/projects_index.py check` — contradictions only, never a list of unstamped projects.
5. **Never bare `mv`.** Files inside a project → `project_filer.py`. A whole directory or a cross-project file → `project_relocate.py`.
6. `project_relocate.py apply <src> <dst> --stub` leaves a `MOVED.md` pointer. **Nothing is ever deleted.**
7. Filenames no sweep may ever move: `INDEX.md` `CANON.md` `CAMPAIGN.md` `MOVED.md` `CLAUDE.md` `README.md` `RISKS.md`.
8. The sweep window is a **watermark**, not a fixed lookback — a gap widens it instead of dropping files.
9. Org drift surfaces at SessionStart via `self_heal` as a JUDGMENT item. It never blocks.
10. First thing to run in a fresh session: `python3 execution/projects_index.py check`.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `python3 execution/projects_index.py sync` | `PROJECTS.md` + `.agent/health/projects-index.json` | After anything moves; runs automatically at session close + 06:00 |
| `python3 execution/projects_index.py check` | Drift list — contradictions only | "Is my project map lying to me?" |
| `python3 execution/projects_index.py json` | Machine-readable rows + drift | Feeding another tool |
| `python3 execution/project_filer.py plan --project "<abs dir>"` | Move plan for loose files at a project root | Files piled at a project root |
| `python3 execution/project_filer.py apply --plan <p.json> --dry-run` | The move table, touching nothing | Always, before a real apply |
| `python3 execution/project_filer.py verify --project "<abs dir>"` | 0 broken links / 0 residue / 0 empty dirs | After every apply. **A FAIL stops the run.** |
| `python3 execution/project_relocate.py plan\|apply\|verify <src> <dst> [--stub]` | Directory/file move **with inbound links rewritten** | Moving or archiving a whole project |
| `python3 execution/verify_project_filer.py` | PASS/FAIL on the sweep's safety contracts | After touching the filer or the placement hook |
| `python3 execution/canon_audit.py <dir> [--dry-run]` | `CANON.md` — canonical vs superseded map | Stale docs are winning greps |

## The mental model

**Frontmatter is truth; the generated file is the map.** This is `canon_audit`'s contract, reused. Judgment lives beside the thing it describes (a `status:` line in the project's own `INDEX.md`), and the index only aggregates. Rename-safe, dies with the project, visible when you open the file.

**Derive by default, stamp to override.** Three prior organization attempts died on an unfinished bootstrap. This one has none: status derives from git history, so `PROJECTS.md` is correct-shaped from commit one and stamping is only for the ~10–15 cases git gets wrong.

**Moving a file is a contract with everything that points at it.** `project_filer` rewrites referrers but *pins* control-plane files (a hardcoded path in `CLAUDE.md` is deliberately left alone). `project_relocate` does the opposite and rewrites them — because when a *directory* moves, that hardcoded path isn't a pin to respect, it's a broken path.

**A report that overstates is a report nobody reads.** Every detector here reports contradictions only. Learned three times in one session: the sweep that silently timed out, the orphan count that said 46 when 37 were already decided, and the done-but-live check that fired on its own housekeeping.

## What shipped

### `execution/projects_index.py` — the generated front door
**What it is.** One `git log` call (~0.22s) bucketed to `<root>/<project>`, plus each project's `INDEX.md` frontmatter, rendered to `PROJECTS.md` and a health JSON.

**When to reach for it.** Any "where is X" moment, and after any move.

**When NOT to.** Don't use it to track *mission* state — `CAMPAIGN.md` + `campaign_beacon.py` own that, singularly.

**How to invoke.** `sync` (write) · `check` (dry-run drift) · `json`.

**Honest edges.** Last-touched excludes bulk sweeps (≥10 projects in one commit) and generated maps, because raw mtime made 14 cold projects read "active" — but a housekeeping commit touching fewer than 10 projects still counts as activity. `_active/claude-export` is gitignored and falls back to filesystem mtime.

### `execution/project_relocate.py` — move a directory with its links
**What it is.** `git mv` (history preserved) + rewrite of every referrer including control-plane files + receipt + an inverse line flushed **before** the rewrite phase, so a mid-run crash is still undoable.

**When to reach for it.** Relocating or archiving a whole project; moving a file between projects.

**When NOT to.** Loose files *inside* one project — that's `project_filer.py`, which is cheaper and knows the lifecycle folders.

**How to invoke.** `plan` writes nothing · `apply … --stub` leaves a `MOVED.md` pointer · `verify` asserts 0 stale referrers.

**Worked example.** `_active/linkedin/04-content-os` → `04-deliverables/content-os`: 67 files, 42 files rewritten, 90 path replacements across 25 control-plane files including `/farrice-engine` and `/linkedin-daily`. Every rewritten workflow path was then spot-checked to resolve.

**Honest edges.** `*/move-plan.md` is frozen — a before/after record must not be rewritten to the after-state. Rewrites are idempotent: the destination usually *contains* the source as a substring, which would otherwise corrupt on a second run.

### `execution/verify_project_filer.py` — the regression net
**What it is.** Asserts the seven protected filenames, that the grep pathspec excludes rather than annihilates, that a sibling-loaded web asset is pinned, and that the placement hook's `PINNED_NAMES` agrees with the filer's `EXEMPT_NAMES`.

**When NOT to.** It doesn't test filing *correctness*, only the safety contracts.

**Honest edges.** Reads the hook by walking its AST — never executes it.

## Composition (options, not pipeline)

| Stacks with | When it earns its cost |
|---|---|
| `canon_audit.py` | After filing — stamps go stale if paths move first |
| `wiring_audit.py` | Same doctrine (propose-first, never deletes), different scope: assets not projects |
| `self_heal.py` | Already wired — `detect_org_drift` is a CLASSIFIER, never a healer |

## Honest edges — the whole session

- **Three self-inflicted breaks, all caught and fixed:** filed a live site's script into `03-working-drafts/` (site broken, restored, web assets now pinned); a benchmark sweep moved 27 protected files including the campaign file (all reversed from the ledger); a `git grep` speed fix used `:!` pathspec syntax that silently matches nothing, evaporating every control-plane pin. Each is now covered by a verifier proven to fail without the fix.
- **Open:** 5 files in `deliverables/` with no correct default; `_active/re-compliance` arguably belongs inside `jen-listings`; a **new** `05-assets` vs `05-lead-gen` collision in `linkedin-launch` created 2026-08-02 by the asset-board work.
- **Concurrent sessions are the live hazard.** A sibling session's commit gate swept this session's in-flight edits once. Claim `session_lock.py` or use a worktree.
- A `post-commit` hook auto-pushes; `git push` reports a misleading "remote rejected" lock error even on success.
