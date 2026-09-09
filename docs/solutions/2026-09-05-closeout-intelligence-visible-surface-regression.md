---
name: closeout-intelligence-visible-surface-regression
problem_signature: "Closeout prompts regressed to thin generic continuations because the global invocation contract no longer required the visible retrieval title, expected outcomes, or quality bars, while the rich renderer remained optional."
domain: system
tags: [closeout, steering, visible-surface, regression]
date: 2026-09-05
status: active
session: "System: Closeout Intelligence - Restore High-Value Next Prompts"
---

## Problem

Substantial closeouts still returned three prompts, but they had become generic and low-leverage. The visible retrieval title disappeared, expected outcomes were implicit or absent, and no inspectable acceptance criterion separated a meaningful continuation from engagement bait.

## Root Cause

The rich renderer survived, but the always-on global contract had been simplified and the workspace contract said deep closeouts *may* use the richer format. The verifier then treated title/outcome/quality fields as renderer-only details. Fresh tasks therefore satisfied the thinner global template without invoking the stronger surface.

## Approach That Worked

1. Preserve the June 2026 Insightful Momentum behavior as a fixture, including a shallow negative control, before editing the contract.
2. Make the visible title, three differentiated paths, explicit expected outcome, and quality bar non-optional across the workspace contract, renderer, sync producer, and verifier; prove the positive control passes and the shallow control fails.

## Dead Ends

Checking only that `contextual_next_prompts.py` still contained rich fields was a false green. The actual failure was propagation into ordinary final answers. Applying the global sync before Farrice explicitly approved the `~/.codex` write was correctly blocked.

## Verification

- Python compilation: PASS.
- Workspace contract and renderer tests: PASS.
- Positive closeout control: PASS.
- Shallow negative control: FAILS for missing visible title, expected outcomes, and quality bars, as intended.
- Global sync transformation preview: PASS and reports a real change.
- Fresh global activation: PENDING explicit approval to update `~/.codex/AGENTS.md`.

## Weaker-Model Trap

A weaker model sees “exactly three prompts” and optimizes for count and brevity. It needs the non-negotiable visible fields plus a negative control proving that three generic continuations are still a failure.

## Pointers

- `directives/steering-loop.md`
- `execution/contextual_next_prompts.py`
- `execution/fixtures/closeout_intelligence/visible-surface-regression.json`
- `execution/verify_steering_compass_quality.py`
- `execution/verify_global_steering_persistence.py`
- `execution/sync_global_operator_core.py`
