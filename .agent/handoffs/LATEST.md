# Latest Handoff

**Thread:** global-org-sweep  
**Full path:** .agent/handoffs/2026-08-04-global-org-sweep.md  
**Date:** 2026-08-04 (today)  
**Status:** ready  
**Title:** Global Org Sweep — One Tree + Generated PROJECTS.md (filing, anti-decay, status stamps)

> Not auto-loaded. Run `/resume` to choose any thread, or `/resume global-org-sweep` for this one.

---

---
thread: global-org-sweep
status: ready
resume_hint: Wire the 4 triaged orphans (design_md_extract, test_video_enhance, publishable_copy_guard, client_package_lint), then archive the 4 one-shot audits
unfinished: 4 wire + 4 archive orphan decisions; 5 deliverables/ files Farrice deferred; FARRICE-MASTER-CONTEXT.md rebuild (too narrow, diluted richer context)
branch: main
pin: true
---

# Global Org Sweep — One Tree + Generated PROJECTS.md (filing, anti-decay, status stamps)

## Purpose
- **Next session should do:** (1) execute the 4 wire-or-archive orphan decisions already triaged below; (2) rebuild `FARRICE-MASTER-CONTEXT.md` — Farrice's verdict is that it is too narrow and has *diluted* the richer context already held in sovereign memory, Notion, and prior work.
- **Not in scope:** re-running the org sweep (done, verified, committed), re-deciding project statuses (Farrice stamped them), re-litigating the ONE TREE choice.

## Load First
- `PROJECTS.md` — generated retrieval front door. **Never hand-edit.** `python3 execution/projects_index.py sync|check|json`
- `.agent/missions/global-org-sweep/move-plan.md` — the plan + an EXECUTED header with real outcomes
- `execution/projects_index.py` · `execution/project_relocate.py` · `execution/verify_project_filer.py` — the three assets this session created
- `directives/artifact-placement.md` — the standing filing contract these enforce
- `_active/farrice-brand/thought-bank/inbox/2026-07-29.md` — Farrice's master-context verdict, captured verbatim

## Current State
- **Objective:** make repo retrieval self-maintaining — "not something I have to housekeep."
- **What is already done:**
  - **~29,300 files relocated across 60 operations, 0 verify failures, nothing deleted.** `projects/` dissolved into `_active/` (ONE TREE); 14 cold projects archived to `_archive/2026-07-28-org-sweep/` each with a `MOVED.md` pointer; Ken's Fasting 3→1, PMF 4→1; `deliverables/` + repo root cleared.
  - `PROJECTS.md` generated from `status:` frontmatter in each project's own `INDEX.md`, deriving from git when unstamped. Regenerates at session close and in the 06:00 daily audit.
  - **Restored `execution/paths.py`** — an orphan sweep had archived it, killing `artifact_router` AND `project_filer` and silently no-opping `/end-session`'s artifact sweep.
  - **Closed the canon/frontmatter-guard conflict** — `--fix` would have stripped every canon stamp in the repo.
  - **Sweep watermark**: fixed lookback (720 min) → stateful. That fixed window is what killed the three prior organization attempts; files older than it were invisible forever.
  - Sweep 88s → 14.5s, so it stops silently timing out inside its 60s budget.
  - Farrice stamped **19 done + 1 parked**: active 43 → 21, drift 0.
  - `self_heal` wiring-orphan count corrected 46 → 9 (37 were already-archived scripts).
- **What is uncertain or stale:**
  - 5 files still in `deliverables/` with no correct default — the two MyBPM docs, `suzuki-general-use-demo-pack.md`, `prompt-course-consumer-posture.md`, `IN-BETWEENER_pitch_deck.html`. Farrice deferred these.
  - `_active/re-compliance` is Jen's work; arguably belongs folded into `_active/jen-listings`.
  - `ai_misfire_sprint_guard.py` — the only orphan Farrice hasn't ruled on; the suite still appears in 2 live workflows.
- **Latest proof/receipt:** `.agent/organization/receipts/` (26 filing receipts + relocate receipts) · `.agent/organization/REVERT-2026-07-28.sh` · verifiers `verify_artifact_router` / `verify_projects_index` / `verify_project_filer` all PASS.

## The 4 wire decisions (triaged, not executed)
| Script | Why wire |
|---|---|
| `design_md_extract.py` | 3 live workflows exist (`/design-md-extract`, `-from-codebase`, `-from-url`) and **none call it** |
| `test_video_enhance.py` | tests `video_enhance.py`, which is `PROVEN` wired — the test has simply never run |
| `publishable_copy_guard.py` | the *harvest* copy of `high-taste-writing-os.md` calls it; the live copy lost the call |
| `client_package_lint.py` | backs the BINDING "client-facing = implementation-grade" rule, with no deterministic backstop today |

**Archive (4):** `audit_extraction_integrity.py`, `perception_engineering_bridge_audit.py`, `system_efficiency_benchmark.py`, `generate_agent_stacking_registry.py` — all one-shot audits whose window closed.

## Suggested Skills / Workflows
- `python3 execution/wiring_audit.py status` — the orphan board; never rebuild this, it already exists
- `python3 execution/project_relocate.py plan|apply --stub|verify` — moving a directory or a file WITH its inbound links. Never bare `mv`.
- `python3 execution/project_filer.py plan --project "<abs dir>"` — loose files inside a project
- `/arsenal <task>` before building anything

## Exact Next Prompt
```text
Wire the 4 orphans from the org-sweep triage, one at a time with proof each is firing:
design_md_extract.py (3 live workflows never call it), test_video_enhance.py (tests a
PROVEN-wired script, never runs), publishable_copy_guard.py (live high-taste-writing-os
lost the call the harvest copy has), client_package_lint.py (backs a BINDING rule with no
backstop). Then archive the 4 one-shot audits via project_relocate --stub. Verify with
wiring_audit status after each.
```

## Acceptance Criteria
- `python3 execution/wiring_audit.py status` shows the 4 wired scripts as `PROVEN`, not `ORPHAN`
- The 4 archived scripts leave a `MOVED.md` pointer and appear in a relocate receipt
- `python3 execution/projects_index.py check` still reports 0 drift
- No verifier that passed before turns red

## Risk Notes
- **Concurrent sessions are live on this tree.** GOLDEN RULE: one live writer. Claim `python3 execution/session_lock.py claim "<mission>"` or use a git worktree before multi-file work. A sibling session's commit gate swept this session's in-flight edits once already.
- A `post-commit` git hook auto-pushes — commits leave the machine immediately, and `git push` will report a misleading "remote rejected" lock error even on success.
- `artifact_router.ensure_project_shapes()` writes boilerplate `INDEX.md` into any `_active/<dir>` lacking one. It now skips `MOVED.md` stubs, but any new gap-filling generator needs to know what a *deliberate* absence looks like.
- Never hand-author `project_filer` plan JSON — `apply` refuses plans without its provenance stamp (the 2026-07-08 crash left 19 moves with no receipt).

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.

