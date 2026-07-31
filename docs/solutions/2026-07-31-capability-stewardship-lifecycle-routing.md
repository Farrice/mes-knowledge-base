---
name: Capability Lifecycle Language No Longer Triggers End Session
problem_signature: a persistent start-mid-closeout behavior request contains closeout and is misclassified as a request to end the current session
domain: system
tags: [routing, operating-alignment, lifecycle, capability-stewardship, end-session]
date: 2026-07-31
status: active
session: capability-stewardship-phase-1
---

## Problem

The routing governor treated any prompt containing broad closeout language as a
current-session wrap request. A request to make capability awareness persistent
at session start, mid-session, and closeout therefore ranked `/end-session`
first even though the requested outcome was an operating-layer repair owned by
`/system-audit`.

## Root Cause

`is_end_session_closeout_intent()` accepted generic `closeout` signals, while
`is_operating_alignment_intent()` had no shape for capability awareness,
context-container judgment, proactive leverage, or multi-phase session
lifecycle language. The specific closeout keyword outweighed the broader
behavioral objective.

## Approach That Worked

1. Detect Capability Stewardship from capability + lifecycle + persistent-default language.
2. Let the operating-alignment classifier claim that shape before domain routing.
3. Exclude that shape from generic end-session matching while preserving direct `/end-session` invocation.
4. Carry one container decision and capability move through Launchpad, Raw Intent, Autopilot, and receipts.
5. Lock both sides with fixtures: lifecycle behavior -> `/system-audit`; genuine current-session wrap -> `/end-session`.

## Preservation Lock

- `/end-session` remains strong for real wrap/closeout requests.
- No new command, skill, plugin, router, or super-agent is introduced.
- Tiny mechanical turns remain quiet.
- User-owned task creation, real subagents, external actions, and global writes retain explicit approval boundaries.

## Dead Ends

- Weakening `/end-session` globally would repair the fixture by breaking genuine closeout intent.
- Adding a Capability Stewardship command would preserve the operator burden of remembering the harness.
- Restoring obsolete always-on steering wording would make tiny and diagnostic turns noisy again.

## Verification

- Exact lifecycle request ranks `/system-audit` first.
- Natural “capabilities at the start, middle, and end” request ranks `/system-audit` first.
- “Wrap this task and prepare the closeout” ranks `/end-session` first.
- Autopilot lifecycle verifier passes all required container and approval cases.
- Raw Intent lifecycle verifier passes.
- System integrity verifier reports all clear.

## Weaker-Model Trap

Do not fix this by lowering `/end-session` globally or by adding another hot
front door. Classify the intent shape first, then preserve the narrow current-
session closeout behavior with an explicit regression.

## Pointers

- `execution/routing_governor.py`
- `execution/co_creative_launchpad.py`
- `execution/verify_autopilot_runtime_preflight.py`
- `execution/verify_google_operator_core.py`
- `semantic_libraries/antigravity/primitives/operating-alignment-contract.md`

## Phase 2 Bridge Pattern

After local proof, install only invocation policy and canonical pointers in the
global instruction surface. Do not mirror classifiers, packet fields, fixtures,
or transfer workflows into `~/.codex`.

Verify the bridge and delegated runtime as separate layers. A projectless helper
can pass against the verified worktree while its default canonical-main target
remains stale. Report that as an integration gap; do not redirect the persistent
global bridge to an ephemeral worktree or patch a dirty shared checkout merely
to manufacture an end-to-end green result.
