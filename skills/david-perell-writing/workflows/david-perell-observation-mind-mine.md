---
name: david-perell-observation-mind-mine
produces: private Mind-Mine Sheet with three evidence-labeled idea leads
expert: David Perell
load_context: genius.md
routing: long-tail
when_to_use: A writer needs to surface ideas from lived observation before drafting or publishing.
---

# Observation Mind-Mine

## Pre-Flight Gate

Read `genius.md` and the Constrained Mind Mining pattern. Require a question or domain, lived-material boundary, timebox, and privacy constraints. Treat the artifact as private unless publication is separately authorized. If no lived material exists yet, return a capture protocol marked `AWAITING LIVED MATERIAL`; do not perform the observation on the user's behalf.

## Input Required

1. Question or domain.
2. Lived-material boundary: what may and may not be used.
3. Timebox or page-fill constraint.
4. Optional raw notes or recollections.
5. Privacy and publication constraints.

## Procedure

### 1. Lock the Capture Boundary

Record allowed material, off-limits material, the finish condition, and whether the sheet is `PRIVATE ONLY` or within a user-authorized scope.

### 2. Capture or Ingest

If notes are absent, produce a pen/no-phone/page-fill protocol and stop. If notes exist, preserve their rough wording before synthesis; the unpolished phrase may be the useful bit.

### 3. Label Every Atom

Use `OBSERVATION` for a supplied concrete detail, `REACTION` for an explicitly supplied feeling or judgment, `INTERPRETATION` for meaning inferred from the material, and `UNCONFIRMED` for a claim needing evidence.

### 4. Extract Tensions

Find grounded objects, behavior, incongruities, recurring phrases, surprises, or contradictions. Do not assign symbolic meaning unsupported by the notes.

### 5. Form Three Leads

For each lead, preserve the raw detail, name the tension, draft a provisional claim, list evidence still needed, and identify a candidate bit. Mark every lead `RAW — NOT PUBLICATION READY`.

### 6. Route

Selected lead → `david-perell-60-20-10-bit-refinery`. Deeper analytical development → Dan Wang. Public practice → `david-perell-public-reps-learning-loop` only after authorization.

## Output Schema

```text
## Mind-Mine Status
READY | AWAITING LIVED MATERIAL
Privacy state: PRIVATE ONLY | USER-AUTHORIZED SCOPE

## Capture Boundary
- Question or domain:
- Timebox or finish condition:
- Allowed material:
- Off-limits material:

## Raw Capture
[unaltered or clearly delimited user material]

## Evidence-Labeled Atoms
| Atom | OBSERVATION / REACTION / INTERPRETATION / UNCONFIRMED | Exact support | Privacy note |

## Tensions and Incongruities
[grounded list]

## Three Promising Leads
### Lead [1-3]
- Raw detail:
- Tension:
- Provisional claim:
- Evidence needed:
- Candidate bit:
- Publication status: RAW — NOT PUBLICATION READY

## Exact Next Route
```

## Quality Gate

- [ ] No location, memory, sensory fact, dialogue, reaction, or emotion was invented.
- [ ] Observations and interpretations remain visibly separate.
- [ ] Raw wording survives before refinement.
- [ ] Three leads trace to supplied material or the artifact stays in capture mode.
- [ ] Privacy status is explicit; private notes do not become public copy.
- [ ] The artifact is a Mind-Mine Sheet, not a public-response learning receipt.

Execution prompt: references/prompts-v2/david-perell-observation-mind-mine.md — honor its Output Contract.
