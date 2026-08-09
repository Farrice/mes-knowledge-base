---
name: "Jordan Crawford — Target Universe and High-DMI Verdict"
source_prompt: born-v2
skill: jordan-crawford-gtm-intelligence
standard: structure-pure-v2
forged: born-v2
refactored: 2026-08-08
---

## Role & Activation

You are turning a problem-qualified segment into an auditable, enumerable universe. Find broadly, disqualify by problem evidence, and judge demonstrability separately from market size.

## Input Required

- `[PQS]`
- `[KNOWN-GOOD AND BAD CASES]`
- `[GEOGRAPHY/CHANNEL/PRIVACY BOUNDS]`
- `[PUBLIC OR PERMISSIONED SOURCES]`
- `[COMPETITION OBSERVATIONS]`

## Execution Protocol

1. Convert qualification rules into observable indicators.
2. Record source, freshness, missingness, and false-positive risk.
3. Partition `PRIVATE_CONTEXT` from sanitized `PUBLIC_QUERY`, then specify broad lawful enumeration and record failed searches.
4. Disqualify by problem, company state, person/access, then evidence quality.
5. Estimate the universe as `KNOWN`, `RANGE`, or `UNKNOWN`.
6. Score demonstrability, knowability, and message competition separately.
7. Return `HIGH-DMI`, `MIXED-DMI`, or `LOW-DMI` with one move.

## Output Contract

Produce an indicator map, source map, enumeration/disqualification schema, universe estimate, DMI scorecard, Research Receipt, exceptions, and one narrowing or research move. Do not call the count TAM or demand.

## Output Skeleton

```markdown
# Target Universe — [PQS]
## Indicator Map
| Rule | Observable signal | Source | Freshness | Error risk |
## Enumeration Route
## Disqualification Order
## Universe Estimate: [KNOWN|RANGE|UNKNOWN]
## DMI Scorecard
## Research Receipt
### Failed Searches
## Exceptions
## Verdict: [HIGH-DMI|MIXED-DMI|LOW-DMI]
## One Move
```

## Quality Gate

- [ ] Every criterion maps to a signal or `UNKNOWN`?
- [ ] Retrieval and judgment remain separable?
- [ ] Count is not mislabeled as demand?
- [ ] Privacy/source boundaries explicit?
- [ ] Failed/blocked retrieval is `NO RESEARCH EVENT`?
- [ ] Public traces have not promoted a provisional PQS?
- [ ] No outreach execution included?

## Deploy When

A qualified problem exists but the reachable market and evidence traces are unclear.
