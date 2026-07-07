---
name: Anchor-Named Score Flattening in chain_runner Finalize
problem_signature: chain_runner finalize silently flattens submitted 9/8/8 scores to uniform 7.25, verdict MARGINAL, and it looks like a bug
domain: system
tags: [chain_runner, taste_signature, quality-gate, calibration, finalize]
date: 2026-07-07
status: active
session: system
---

## Problem

`chain_runner.py finalize --intent 9 --expert-score 8 --adversarial 8` returned 7.25
across all three dimensions and MARGINAL — not the submitted scores, not an obvious
transform. Looked like corruption in the scoring pipeline.

## Root Cause

Not a bug — `taste_signature.py` Rule 2 ("8-must-be-earned") firing as designed:
`apply_taste_signature()` caps any dimension ≥8 at `_EARNED_8_CAP = 7.25` unless the
caller passes `anchor_named=True`. 9/8/8 are all ≥8, so all three flatten to 7.25. The
cap sits BELOW `_PASS_COMPOSITE_FLOOR` (7.5) on purpose — fixes a 2026-05-22 plateau
where a 7.50 cap equaled the PASS floor and let capped scores slip through as PASS.
`--anchor-named` is a CLI flag asserting the caller can name the specific rubric
anchor (`evolution_store/ground_truth/rubric_v1.md`) justifying the ≥8.

## Approach That Worked

1. When a deterministic gate produces a suspiciously uniform value, grep the
   enforcement layer for the literal constant BEFORE assuming malfunction:
   `grep -n "_EARNED_8_CAP" execution/taste_signature.py`.
2. Read the module docstring (~lines 20-49) — documents Rule 2 and the cap value,
   including the historical reason for 7.25 over 7.5.
3. If the ≥8 scores are genuinely earned, re-run with `--anchor-named` AND name the
   matching anchor from `rubric_v1.md` in `--notes`.
4. If no anchor can be named, lower the submitted score instead of fighting the cap.

## Dead Ends

- Re-running finalize with identical flags expecting a different result.
- Suspecting `rubric_v1.md` was stale — the rubric is descriptive; enforcement lives
  entirely in `taste_signature.py`.

## Verification

Traced `anchor_named` from `chain_runner.finalize()` (~793/809) into
`taste_signature.apply()` Rule 2 block (~151-168); matched the exact 7.25/7.5 values
against the docstring's worked example by direct grep, not inference.

## Weaker-Model Trap

Two failure shapes: ignores the cap and reports 9/8/8 as uncapped (silently defeats
calibration), or reflexively adds `--anchor-named` without naming an anchor (defeats
it more visibly). Correct move: name the real anchor, or lower the score.

## Pointers

- `execution/taste_signature.py` (docstring 11-49; constants ~87-89; Rule 2 ~151-168)
- `execution/chain_runner.py` (`anchor_named` ~624; passthrough ~793/809; CLI flag
  ~1735)
- `evolution_store/ground_truth/rubric_v1.md`; `directives/quality_gate.md`
