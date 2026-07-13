---
name: strength-conditioning-os
description: "CONDUCTOR hub for the strength-&-conditioning / fitness coaching package. Diagnoses a coaching need and routes it to the right lane — physiology & limiter diagnosis (Galpin), hypertrophy volume & programming (Israetel), technique & minimalist execution (Teo), nutrition & body composition (Aragon) — then composes across lanes into one integrated plan. Ships with an evidence-based field guide synthesizing 11 single-conversation experts."
version: "2.0"
format: "completion-engine"
workflows: 2
source: "claude.ai export 2026-07-01"
---

# Strength & Conditioning OS — The Coaching Conductor

This is the front door for the S&C coaching package. It does one job: take a real coaching need — a stalled lifter, a first program, a fat-loss request, a "my knees hurt" email — and route it to the lane(s) that actually own the answer, then integrate the pieces into a single coherent plan the client can execute. It never invents physiology; it hands the question to the expert who has the depth, and it uses `references/field-guide.md` to ground any claim that crosses lanes.

The hub exists because coaching failures are almost never a knowledge problem inside one domain — they are a *routing* problem across domains. A client who "can't gain muscle" might have a volume problem (Israetel), a recovery/limiter problem (Galpin), an execution problem (Teo), or a fueling problem (Aragon). Guessing wastes months. Diagnosing and routing correctly is the whole game.

## Available Workflows

| # | Workflow | Produces | Use when |
|---|----------|----------|----------|
| 01 | `01-diagnose-and-route` | Intake diagnosis + named lane assignment(s) + why | A coaching need arrives and you don't yet know which expert owns it |
| 02 | `02-build-integrated-program` | One integrated plan composed across lanes | The diagnosis names 2+ lanes and the client needs a single unified program, not four disconnected prescriptions |

## Routing Map

Route the coaching need to the lane whose ownership matches the *primary constraint*. Name the skill explicitly and hand off; do not answer a lane's question from the hub.

| Coaching need / signal | Route to lane skill | Owns |
|---|---|---|
| "What's actually holding me back?" · unexplained plateau · fatigue/recovery mystery · energy-system question ("gassed at rep 8" vs "gassed after 30s") · injury → return to performance · which limiter to attack first | **`andy-galpin-training-intelligence`** | Exercise physiology, limiter diagnosis, energy-system programming, rehab, periodization |
| "How much should I train this muscle?" · volume too low/too high · designing a hypertrophy mesocycle · MEV/MAV/MRV · deload timing · stimulus-to-fatigue triage · RIR progression | **`michael-israetel-hypertrophy`** | Volume landmarks, hypertrophy programming, mesocycle/deload design, junk-volume auditing |
| "Which exercise, and am I doing it right?" · exercise selection per movement pattern · technique/form breakdown · minimalist / time-poor client (<2–4 hrs/wk) · effort calibration (training too easy) · redundancy in the program | **`eugene-teo-training`** | Technique, one-lift-per-pattern selection, minimalist programming, true-failure calibration, mobility-in-rest |
| "What do I eat?" · fat loss / body recomposition · protein target · surplus/deficit sizing · reverse dieting · diet adherence & flexible dieting · macro periodization | **`alan-aragon-nutrition`** | Nutrition, energy balance, protein/macro targets, body composition, evidence-based diet strategy |

**Multi-lane rule:** If the intake names two or more constraints (e.g. stalled AND under-fueled AND training too easy), run `01-diagnose-and-route` to rank them, then `02-build-integrated-program` to compose one plan — sequenced by which constraint gates the others (fuel and recovery usually gate training adaptation).

## Quick Reference

- **The one question that routes 80% of cases:** *"Is the bottleneck stimulus (too little/wrong training → Israetel/Teo), recovery/physiology (can't absorb the training → Galpin), or fuel (can't build/reveal the result → Aragon)?"*
- **Diagnose before prescribing.** The hub's job is to find the #1 constraint. Attacking a non-constraint wastes the client's most limited resource: adherence over time.
- **Consistency compounds; complexity does not.** Every lane in this package agrees the base rate of progress is set by showing up over years. Route toward the smallest change that removes the actual constraint.
- **Ground cross-lane claims** with `references/field-guide.md` — 11 evidence-based experts (Nippard, Helms, Norton, Schoenfeld, Ethier, Nuckols, Beardsley, Magness, Lieberman, Bikman, Henselmans) — each entry names their signature contribution and which lane it complements.
- **Never copy a physique-athlete's exact program.** Shape is genetic, size is (hard training × years), exercise selection is personal biomechanics. This is a routing hub, not a template dispenser.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

2 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Strength & Conditioning OS — Constraint Diagnosis & Routing Brief** — `skills/strength-conditioning-os/references/prompts-v2/constraint-diagnosis-routing-brief.md`
- **Strength & Conditioning OS — Integrated Coaching Program** — `skills/strength-conditioning-os/references/prompts-v2/integrated-coaching-program.md`

<!-- END:execution-prompts -->
