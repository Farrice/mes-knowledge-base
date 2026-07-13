# Solution Card — Merging a Premium External Skill System Without Forking or Blind-Installing

**Date**: 2026-07-10 · **Session**: Matt Pocock v1.1 extract-forge · **Domain**: system / harness

## Problem

A premium external skill source (Matt Pocock / AI Hero) ships a major version with genuinely superior structures. The naive moves both fail: blind-merge (installs stale/deprecated skills, misses renames — his own installer doesn't handle renames — and imports engineering assumptions into non-code domains) or fork-and-own (breaks `npx skills update`, creates permanent drift — standing memory binding).

## Solution — the ADOPT / ADAPT / SKIP merge map

1. **Extract first, install second.** Read the actual primary sources (repo skill files, not summaries) + the creator's own changelog narrative (video/post). Build a merge map: every asset gets ADOPT (refresh in place, upstream-managed), ADAPT (build a harness-native asset that COMPOSES with the import — invokes it and layers deltas, "where the two conflict, this file wins"), or SKIP (covered better natively).
2. **ADAPT = compose, never fork.** The native layer invokes the imported skill for mechanics and adds only the domain delta (e.g. `/wayfinder-work` → `/wayfinder` + local-markdown tracker + HITL/AFK→swarm wiring; `/operator-school` → `/teach` + pattern bridge + taste ladder + deploy gate). Config surfaces the import already reads (`docs/agents/issue-tracker.md`) are the cleanest composition points — extend those, not the skill.
3. **Renames need delete-and-re-add + archive.** Move superseded skills to `~/.agents/skills-archive-<date>/` (reversible), remove dangling symlinks, log the delta in `directives/external-skills-registry.md`.
4. **PoC on live work in-session** — the new assets charted real maps for two live projects and ran a real two-axis verify before shipping.

## Why it matters

The most valuable part of a great external system is rarely its files — it's the one or two structural moves that survive translation into your own domains (here: decision-maps-with-frontier, and never-merged review axes). Extract the move, compose the file.

## Reuse triggers

Any future "should we import/merge X's system" question · new Pocock releases (`npx skills update` + rename check) · any external source rated import-worthy in `directives/external-skills-registry.md`.
