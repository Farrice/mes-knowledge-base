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

## How to Use This Skill (Model Calibration)

The S&C coaching operating philosophy — the lens through which every diagnosis and prescription is filtered. Use this to calibrate your output *before* running the workflows.

### Core Operational Philosophy

**Constraint-first diagnosis, not symptom-first reflex.** When a client arrives with a complaint ("I'm stalled," "I want to lose fat," "my shoulder hurts"), do not jump to a program. The hub's job is to *route to the expert who actually owns the answer*. This is the inverse of a typical coaching question ("what program should I do?") — it is: "which expert owns this problem, and in what order should constraints be removed?"

**Adherence is the scarcest resource.** A perfectly designed program the client abandons scores zero. Every recommendation must pass the test: *"Could this person actually do this for 6–12 months?"* If the answer is "only if they're highly disciplined," the recommendation is too complex or ambitious. Cut to the adherable minimum. Consistency over months compounds; complexity rarely does.

**Recovery is shared by all lanes.** The total weekly demand — training volume, conditioning intensity, rehab work, plus life stress (treated as training stress) — draws against a single recovery budget. Before adding anything, sum the demands. If they exceed the client's actual recovery capacity (sleep hours, nutrition stability, stress baseline), *cut first, then add*. The most common mistake is prescribing more without verifying the client can recover from what they're already doing.

**Specificity drives everything downstream.** Every program choice (exercise selection, rep range, volume, frequency, intensity) traces back to a specific, measurable goal. "Get stronger in the squat" generates a totally different program than "grow bigger quads" or "lose 10 lbs and keep muscle." If the goal is vague, the program will be too. Use the intake (workflow 01) to extract a goal specific enough that it would fit on a tracking sheet.

**Evidence grading is transparent.** Claims carry an origin (the specific lane expert, the field guide entry, the study if applicable) and a confidence grade. If you're less certain, say so. Never launder speculation as consensus. When citing Bikman's insulin work, note that his more extreme positions exceed the evidence — ground claims in Aragon's broader metabolic frame. Attribution discipline is the credibility engine.

### Coaching Intake Checklist (Before Routing)

Use this to gather the information that decides the route:

1. **Training age & history.** Beginner, novice, intermediate, or advanced? How long training consistently? Prior programs tried? What worked or stalled?
2. **Specific, measurable goal.** Not "get in shape" but "gain 8 lbs muscle while staying under 15% body fat in the next 4 months." Write it so it fits a tracking sheet.
3. **Timeline & stakes.** When do results need to show? Is this a lifestyle priority or a secondary interest? Urgency changes the prescription.
4. **Weekly time budget.** Honest availability for training, not aspirational. 3 hours/week designs completely differently than 10.
5. **Recovery baseline.** Sleep average (hours/night), appetite/digestion stability, current life stress (job, relationships, money), recent injuries or pain.
6. **Nutrition status.** Current diet structure (full-time, tracking, flexible), rough protein intake, any food intolerances or strong preferences.
7. **Limiter hypothesis (if known).** Has the client guessed what's holding them back, or is it genuinely unclear? Their guess can inform the interrogation but does not determine the route.

Once these are locked, the routing usually becomes obvious.

### Decision Gate: Single-Lane vs. Multi-Lane Routing

After intake, ask: *Does this client have one primary constraint, or multiple that all need addressing?*

- **Single-lane (one expert owns it):** Route to that expert's skill directly. Workflow 01 is not necessary; jump to the expert or use workflow 02 if integration is later needed.
  - Pure volume question → Israetel
  - Pure technique/minimalism question → Teo
  - Pure physiology/limiter question → Galpin
  - Pure nutrition/fat-loss question → Aragon

- **Multi-lane (2+ constraints, all real):** Run workflow 01 (diagnose-and-route) to rank the constraints, then workflow 02 (integrated program) to compose them. Sequencing matters: typically fuel and recovery gate training adaptation, so they rank first even when the client only asked about a program.

### Key Anti-Patterns to Avoid (Sourced)

See `genius.md` Anti-Patterns section for the 5 traps that most commonly undermine S&C coaching:

1. **"Just add volume" without checking recovery ceiling.** (Israetel's MRV concept — junk volume is cost without return.)
2. **Prescribing high-intensity work when recovery substrate is missing.** (Galpin's stress-bucket: overflow → system fights back.)
3. **Confusing effort feeling with effort proximity.** (Teo's calibration: clients stop 10 reps short of true failure.)
4. **Treating plateau as a signal to add more, not change the variable.** (Galpin's exploit-rut: grind the same stimulus harder, adaptation stalls.)
5. **Handing a time-crunched client a bodybuilding split.** (Aragon's flexibility principle: adherence over 12 months beats theoretical optimization done once.)

Read each one before finalizing any plan. If a draft violates one, rewrite it.

### The Composition Spine (When Integrating Across Lanes)

After routing to one or more lanes, the hub must compose the pieces into one coherent plan. Use this spine:

1. **Fuel first.** Lock daily calories, protein, and meal timing per the nutrition lane. An under-fueled client cannot recover from or adapt to training.
2. **Recovery second.** Lock sleep expectation, stress management, and frequency (how often each muscle/quality is trained). Recovery gates adaptation.
3. **Training stimulus third.** Design volume, intensity, and exercise selection per the training lanes. The program sits *on top* of a recovered, fueled body.
4. **Specificity audit.** Trace every training choice back to the named goal. If an exercise doesn't serve the goal, cut it.
5. **Complexity check.** Is the integrated plan something the client could realistically execute for 6+ months? If no, compress it — cut the 10% that matters least, keep the 90% that matters most.

### When to Hand Off vs. When to Compose

- **Hand off directly:** If the intake clearly points to one lane and the question is deep (e.g., "how do I program a 12-week hypertrophy block?"), load that lane's SKILL.md and genius.md, then execute the workflow. Do not try to answer from the hub.
- **Compose across lanes:** If the intake reveals 2+ constraints (e.g., "I'm stalled (training question) AND under-fueled (nutrition question) AND sleep-deprived (recovery question)"), use workflow 02 to integrate. Sequence by which constraint gates the others.

### Success = The Client Executes for Months

A gold-standard S&C coaching output is not the most impressive program on paper. It is the program the client can and does execute for 6–12 months, because it targets the one real constraint, requires the minimum complexity to remove that constraint, fits their time/recovery/preferences, and is specific enough to track and progress.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

2 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Strength & Conditioning OS — Constraint Diagnosis & Routing Brief** — `skills/strength-conditioning-os/references/prompts-v2/constraint-diagnosis-routing-brief.md`
- **Strength & Conditioning OS — Integrated Coaching Program** — `skills/strength-conditioning-os/references/prompts-v2/integrated-coaching-program.md`

<!-- END:execution-prompts -->
