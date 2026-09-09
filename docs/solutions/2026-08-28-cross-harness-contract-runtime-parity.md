---
name: cross-harness-contract-runtime-parity
problem_signature: "A shared workflow contract was present in both Claude and Codex, but its executable dependency remained on an unmerged Claude branch and the bare Codex command lacked a hot bridge."
domain: system
tags: [codex, claude, parity, workflow, skill, verifier]
date: 2026-08-28
status: active
session: "01a04aa7-f39d-7ea3-8ea2-3ba040d7e63e"
---

## Problem

Bare `/cos` reached the canonical Chief of Staff workflow in Codex, but daily execution failed because `execution/cos_board_cast.py` was absent. The skill and workflow text looked healthy, which made the runtime break easy to misclassify as a prompt or routing problem.

## Root Cause

The production caster and its sabotage verifier were committed only on Claude branch `claude/dazzling-cannon-6ed186` (`5ec87ee42`) and never merged into the canonical runtime. Codex also had hot bridges for `/cos-status` and `/cos-weekly`, but no thin `source-command-cos` bridge for the bare command.

## Approach That Worked

1. Compare the canonical skill, genius layer, and workflow byte-for-byte across main and Claude before editing; this proved they were already shared and prevented a duplicate COS implementation.
2. Restore only the missing executable and verifier, add a thin Codex bridge that delegates to `.agent/workflows/cos.md`, then prove synthetic failure paths, current-data casting, route rank, live-surface discovery, harness health, and verifier-fleet discovery.

## Dead Ends

Treating a successful manual fallback as repair would leave the production path broken. Trusting the 22 synthetic caster checks alone also missed that the live specialist choice can be debatable; human felt-standard acceptance remains separate from structural parity.

## Verification

- `python3 execution/verify_cos_board_cast.py` — 22 positive and negative checks passed.
- `python3 execution/verify_cos_primer_gate.py` — 8 golden cases passed.
- Current `2026-08-28` brief cast successfully with three advisors.
- `python3 execution/codex_live_surface_audit.py --strict` — PASS and `/cos` discovered.
- `python3 execution/codex_harness_check.py` — PASS.
- `verify_fleet.discover()` includes `verify_cos_board_cast.py`.

## Weaker-Model Trap

A weaker repair copies the whole Claude skill tree into Codex because the command failed. That creates a second behavior contract while leaving the actual missing dependency or activation bridge unresolved. Prove contract equality first, then repair the smallest broken edge.

## Pointers

- `.agent/workflows/cos.md`
- `skills/chief-of-staff-os/SKILL.md`
- `skills/chief-of-staff-os/workflows/cos-daily.md`
- `.agents/skills/source-command-cos/SKILL.md`
- `execution/cos_board_cast.py`
- `execution/verify_cos_board_cast.py`
- `.agent/handoffs/2026-08-16-cos-standing-board.md`
