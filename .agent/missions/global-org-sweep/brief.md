# MISSION BRIEF — Global Organization Sweep (propose-first)

Self-contained: any conductor (any model — this is also Farrice's Opus 5 A/B test mission) runs this from a fresh session with zero prior context. Approved by Farrice 2026-07-28: **propose-first, binding — NOTHING moves until he approves the move-plan.**

## Why

Retrieval kills Farrice's flow: `_active/` holds ~55 entries with strays, some projects have no folder, some files sit outside any project, and superseded docs win greps. Per-project machinery exists (`execution/project_filer.py`, `execution/artifact_router.py`, the placement hook, the canon layer shipped 07-28) — it has just never run globally.

## Deliverables

1. **The move-plan** (`.agent/missions/global-org-sweep/move-plan.md`): one row per stray — current path, verdict (file into project X / archive / leave + why), destination, one-line reason. Built with `artifact_router.py classify` + `project_filer.py plan` per project. Group by confidence: CLEAR (router certain) / JUDGMENT (needs Farrice) / LEAVE. **Do not execute any move in the same session unless Farrice approves the plan in that session.**
2. **`PROJECTS.md` at repo root** — the retrieval front door: every live project, one line each: name, status (active/parked/done), canonical entry file (CAMPAIGN.md or INDEX.md), last-touched date. Parked and archived projects in a second table. This file ends the "where is that" hunt.
3. **Canon stamps repo-wide**: run `canon_audit.py --dry-run` on each project folder; stamp frontmatter where prose banners exist (the audit lists them); generate each project's CANON.md.
4. **Flag, don't build:** a one-line org-drift check proposal for `/weekly-closeout` so this sweep never needs repeating at full scale.

## Constraints

- Read-only until move-plan approval (worktree not needed; no writes beyond the plan/PROJECTS.md/CANON stamps).
- Never archive by inference alone — anything with activity in the last 30 days or referenced from a CAMPAIGN.md/memory is JUDGMENT tier, not CLEAR.
- `.tmp/`, `.agent/`, `evolution_store/`, `.claude/` are out of scope (system dirs, not projects).
- Subagent briefs (if any parallel classification is dispatched) must contain verbatim: "no Chain, no finalize, no Notion, no Next Moves, return only the artifact."
- Close: update CAMPAIGN.md row (LinkedIn campaign, system lane), missions.jsonl line, commit to main.

## Success test

Farrice can find any live project's entry point from PROJECTS.md in under 10 seconds, and a grep for any load-bearing topic surfaces a canonical doc, not a superseded one.
