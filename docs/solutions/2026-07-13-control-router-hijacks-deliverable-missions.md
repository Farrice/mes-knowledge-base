---
name: Control Router Hijacks Deliverable Missions
problem_signature: a deliverable mission that invokes workflows by slash command ("run /extract-forge … we're not doing 12 separate workflows!") gets classified as a broken-system complaint and routed to /autopilot or /system-audit, suppressing the expert-skill suggestions the mission actually needed
domain: system
tags: [routing, control-intent, classifier, golden-set, hooks, misfire]
date: 2026-07-13
status: active
session: kdp-forge-extraction
---

## Problem

`classify_control_intent`'s `broad_front_door_complaint` branch fired on a forge-extraction
mission because the prompt contained "orchestrate" (a broad front-door SURFACE term) and
"not doing" (a substring-matched PROBLEM term, from "we're not doing 12 separate workflows
for every single video!"). The router emitted a CONTROL ROUTING OVERRIDE (Owner: /autopilot,
"broad broken-system complaint") on a prompt that was pure deliverable work explicitly
invoking `/extract-forge` and `/watch`. The same hook also classified background
task-notification turns as user prompts, producing further noise overrides mid-session.

## Root Cause

Three holes, one per layer:
1. **Classifier**: `broad_front_door_complaint` checked surfaces + problems + no-repair-verb,
   but — unlike the adjacent `weak_aggregate_match` — never checked `concrete_deliverable`
   or `content_context`, and had no concept of explicit slash-workflow invocation. Generic
   terms ("orchestrate", "not doing") matched as raw substrings.
2. **Hook skip-logic**: `_has_explicit_skill_invocation` only recognized markdown skill
   links; `prompt.startswith("/")` missed verb-led invocations ("run /extract-forge …").
3. **Hook input hygiene**: `[SYSTEM NOTIFICATION]` / `<task-notification>` turns were
   classified as if they were user prompts.

## Approach That Worked

Golden set FIRST, then patch (per the standing steering-loop doctrine):
1. Added the verbatim misfire prompt to `verify_control_intent.py` GOLDEN with expected
   route `""`, plus positive controls proving genuine complaints (including the fix request
   itself: "the control router keeps misfiring… patch it") STILL route to system-audit.
   Confirmed red (1/24 fail) before touching the classifier.
2. `control_intent.py`: computed `explicit_workflow_invoke` (slash token after start/whitespace,
   optionally verb-led — URL paths like `youtube.com/watch` can't match) and moved
   `concrete_deliverable` up; guarded `broad_front_door_complaint` with
   `not concrete_deliverable and not content_context and not explicit_workflow_invoke`,
   and the general-distress branch with `not explicit_workflow_invoke`. Anchored complaints
   still fire via `anchored_match` even when a slash command is present.
3. `skill_router_hook.py`: exit-0 on `[SYSTEM NOTIFICATION` / `<task-notification>` turns;
   extended the explicit-invocation skip to `^(run|use|execute|invoke)\s+/cmd`.
4. Verified: 24/24 classifier + 7/7 bindings golden cases green; live
   `codex_operator_preflight` shows the mission prompt in lane `general` and the genuine
   complaint in lane `system-failure`; piped-JSON hook tests confirm silent exit on
   invocation/notification turns and a full override on a real wiring complaint.

## Prevention Rule

Any control-plane classifier branch that can suppress expert routing MUST carry the same
three vetoes: deliverable-verb context, content-domain context, explicit workflow
invocation. New misfires go into `verify_control_intent.py` as a red golden case BEFORE
the classifier is edited — the golden set is the contract, the classifier is the
implementation.
