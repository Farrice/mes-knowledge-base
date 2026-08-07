---
name: david-perell-current-fit-diagnostic
produces: Current Fit Verdict with a gated downstream route
expert: David Perell
load_context: genius.md
routing: long-tail
when_to_use: A developed idea and supplied dated signal need a truth, audience, brand, and expiry fit decision.
---

# Current-Fit Diagnostic

## Pre-Flight Gate

Read `genius.md`, `references/claims-ledger-QsHm_0MEhX8.md`, and `references/cross-domain-patterns.md`. A positive route requires a developed Idea Card, sourced and dated Signal Packet, audience or brand territory, and expiry. Partial inputs may produce only a dispositive stop: unsupported evidence returns `HOLD`, and an already expired window may return `KEEP EVERGREEN` with `EXPIRED CURRENT`. Do not fill the missing axes or route onward. This workflow judges fit; it does not research, repair the signal, or draft a timely shell. Nathan Barry owns the explicit brand-fit refinement.

## Positive-Route Inputs Required

1. Idea Card: thesis, claims, evidence, reader outcome.
2. Signal Packet: source, observed date, event or object, relevance, uncertainty.
3. Audience and stated brand or reputation territory.
4. Expiry or future release window.
5. Distortion constraints.

If one or more fields are missing, report them as `UNKNOWN` or `NOT SUPPLIED`. A safe stop remains valid when the supplied evidence alone is dispositive; only `ROUTE CURRENT` and `SCHEDULE` require the full packet.

## Procedure

### 1. Lock the Idea

Record thesis, supporting claims, reader outcome, and prohibited distortions.

### 2. Validate the Current

Classify it `ACTIVE`, `FUTURE`, `EXPIRED CURRENT`, or `UNSUPPORTED` from the supplied source, date, connection, and expiry. Do not browse for missing proof.

### 3. Keep Five Judgments Separate

Rate idea quality, execution readiness, current velocity, audience fit, and brand fit as `STRONG`, `MIXED`, `WEAK`, or `UNKNOWN`, each with evidence. Do not calculate a false-precision score.

### 4. Run the Carrier Test

Ask whether the current naturally explains why the idea matters now, whether the audience recognizes the connection, whether it fits the stated reputation, whether it changes thesis or certainty, and whether it relies on invented news or visual facts.

### 5. Decide

- `ROUTE CURRENT`: active, supported, natural fit → `david-perell-timely-shell-timeless-core`.
- `KEEP EVERGREEN`: sound idea, weak or unnecessary current.
- `SCHEDULE`: legitimate future current → `david-perell-scheduled-current-archive`.
- `HOLD`: missing evidence, material mismatch, or unavoidable distortion.
- `EXPIRED CURRENT` is a proof state whose default decision is `KEEP EVERGREEN`.

Mission conflict may route to `david-perell-current-or-soul-portfolio`. Do not produce a shell in this workflow.

## Output Schema

```text
## Current Fit Verdict
Decision: ROUTE CURRENT | KEEP EVERGREEN | SCHEDULE | HOLD
Current state: ACTIVE | FUTURE | EXPIRED CURRENT | UNSUPPORTED
Proof state:

## Core Lock
- Thesis:
- Supporting claims:
- Reader outcome:
- Distortion constraints:

## Signal Validation
| Source | Date | Current | Connection | Expiry | State |

## Five-Axis Diagnostic
| Axis | STRONG / MIXED / WEAK / UNKNOWN | Evidence |

## Carrier Test
- Natural why-now connection:
- Audience recognition:
- Brand or reputation fit:
- Distortion risk:
- Truth or source risk:

## Decision Rationale
[evidence-bounded verdict]

## Evergreen Fallback
[unchanged core; no shell]

## Exact Next Route
```

## Quality Gate

- [ ] Source, observed date, connection, and expiry are present for any positive route; missing support returns `HOLD`, while a supplied past expiry may return `KEEP EVERGREEN` with `EXPIRED CURRENT`.
- [ ] Idea, execution, current, audience, and brand judgments stay separate.
- [ ] Nathan Barry's brand-fit refinement is not presented as David's sole framework.
- [ ] Unsupported, expired, wrong-audience, or thesis-distorting currents cannot reach workflow 09.
- [ ] No shell, publication-ready hook, live research, or visual inference appears.
- [ ] Evergreen material remains intact when the current fails.

Execution prompt: references/prompts-v2/david-perell-current-fit-diagnostic.md — honor its Output Contract.
