---
name: david-perell-idea-courage-craft-triage
produces: Writing Bottleneck Verdict with one primary route
expert: David Perell
load_context: genius.md
routing: long-tail
when_to_use: A draft or idea feels weak and the true constraint is unclear.
---

# Idea-Courage-Craft Triage

## Pre-Flight Gate

Read `genius.md` and `references/claims-ledger-QsHm_0MEhX8.md`. Require a raw idea or draft, intended claim, supporting evidence, reader outcome, and any assertion the writer keeps softening or removing. If the evidence cannot distinguish the bottleneck, return `INSUFFICIENT EVIDENCE`. Do not invoke POP before a `CRAFT` verdict, and do not infer a hidden belief.

## Input Required

1. Raw idea or full draft.
2. Intended claim.
3. Supplied evidence or examples.
4. Desired reader outcome.
5. Any stronger supported assertion the writer softened or removed; `NOT SUPPLIED` is valid.

## Procedure

### 1. Build the Evidence Map

Record the claim, support, reader change, softened assertion, and missing evidence without upgrading user-supplied claims to verified world facts.

### 2. Test IDEA

Ask whether the material contains a specific observation, tension, and supportable claim rather than a topic label or reach ambition. If not, `IDEA` is primary.

### 3. Test COURAGE

Require both a worthwhile supported claim and explicit evidence that the writer is weakening, omitting, or distancing themselves from it. Identify only the exact sentence the user supplied or confirms. If no stronger sentence exists in the inputs, courage cannot be manufactured.

### 4. Test CRAFT

Run only after idea and willingness are sufficiently established. `CRAFT` applies when the claim and support exist but the execution blocks clarity, force, memorability, or medium fit.

### 5. Resolve Mixed Deficits

Use dependency order: IDEA before COURAGE before CRAFT. Name one primary bottleneck, then sequence bounded secondary support. Do not blend several interventions into one vague recommendation.

### 6. Route

- `IDEA` → `david-perell-observation-mind-mine`, then `david-perell-60-20-10-bit-refinery` when material exists.
- `COURAGE` → human confirmation of the feared supported sentence; only then route to refinement or craft.
- `CRAFT` → `01-diagnose-and-rebalance`, `02-compress-to-memorable`, or `03-draft-pop-first` according to the artifact needed.
- `INSUFFICIENT EVIDENCE` → stop and request only the missing discriminating fields.

## Output Schema

```text
## Writing Bottleneck Verdict
Primary verdict: IDEA | COURAGE | CRAFT | INSUFFICIENT EVIDENCE
Stop state: PROCEED | HUMAN DECISION | HOLD

## Evidence Map
- Intended claim:
- Supporting evidence:
- Reader outcome:
- Softened or removed assertion:
- Missing evidence:

## Three-Way Test
- IDEA:
- COURAGE:
- CRAFT:

## Weakest Link
[one evidence-backed explanation]

## Feared Supported Sentence
[verbatim supplied or confirmed sentence, or NOT SUPPLIED]

## Bounded Secondary Support
[ordered list]

## Exact Next Route
[workflow or human checkpoint plus required input]
```

## Quality Gate

- [ ] Exactly one primary verdict is named.
- [ ] The verdict cites supplied evidence rather than intuition about the writer.
- [ ] COURAGE contains no invented belief, controversy, or life experience.
- [ ] Mixed deficits are sequenced instead of blended.
- [ ] POP is used only after a CRAFT verdict and retains its older evidence lane.
- [ ] Empty viral ambition routes to IDEA or HOLD, never a manufactured hot take.

Execution prompt: references/prompts-v2/david-perell-idea-courage-craft-triage.md — honor its Output Contract.
