---
name: provisional-content-signal-loop
problem_signature: "Deploy a source-grounded content signal loop when creator taste evidence exists but live platform metrics do not"
domain: system
tags: [content-system, evidence-boundary, provisional-profile, queue-state]
date: 2026-07-30
status: active
session: "extract-forge: youtube-cSz_6SNEirU"
---

## Problem

A creator had real content, explicit human taste scores, canonical audience
strategy, and current industry signals, but no live LinkedIn analytics. The
system still needed to produce a useful first idea queue without converting
approval into fake performance evidence.

## Root Cause

Earlier content ideation paths collapsed three different evidence classes:
published performance, human verdicts, and unscored strategy. Without a
platform-specific profile and persistent queue state, a model could call a
taste-approved structure a winner, invent trend confidence, or lose selection
decisions between sessions.

## Approach That Worked

1. Split the system into three stateful stages: a PROVISIONAL Winning Content
   Profile, evidence-backed idea cards, and a human-authorized queue with visible
   mutations.
2. Preserve evidence class, source freshness, creator bridge, confidence,
   staleness, and next action on every dependent item. Treat the user's direct
   queue-build instruction as operational selection authority while leaving
   item-level taste verdicts pending.

## Dead Ends

- Calling human-approved posts "performance winners" without analytics.
- Treating trade coverage as factual substantiation for every product claim it
  repeats.
- Adding all generated ideas to the queue instead of applying a small,
  strategy-bounded selection.
- Using the prose classifier's parallel-structure warning as a reason to remove
  required state fields from a structured queue.

## Verification

- Content Signal Loop regression verifier: 10/10 fixtures plus command wiring.
- Real deployment verifier: PASS for the provisional profile, eight idea cards,
  five selected queue items, four dated trend sources, and finished-content
  veto.
- All three Kieran skill heartbeats: 7/7.
- Full system verifier: ALL CLEAR.
- Deployment claim-risk scans: CLEAN.

## Weaker-Model Trap

A weaker model will treat "winning" as permission to invent metrics, confuse a
fresh article with validated demand, or draft posts before selection. Force it
to name the evidence class on every formula and carry PROVISIONAL status into
every idea and queue item.

## Pointers

- `_active/farrice-brand/content/signal-loop/`
- `extractions/kieran-flanagan-content-signal-loop/verification-checkpoint.md`
- `extractions/kieran-flanagan-content-signal-loop/verify_farrice_deployment.py`
- `skills/kieran-flanagan-audience-intelligence/workflows/05-winning-content-profile.md`
- `skills/kieran-flanagan-content-engine/workflows/09-content-signal-ideation.md`
- `skills/kieran-flanagan-content-ops/workflows/04-content-queue.md`

