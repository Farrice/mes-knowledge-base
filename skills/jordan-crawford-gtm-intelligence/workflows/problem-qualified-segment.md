---
name: "Problem-Qualified Segment"
produces: "Worst-version problem definition with coherent segment, company, and person qualification"
expert: "Jordan Crawford — Evidence-First GTM Intelligence"
load_context: "genius.md"
tier: 1
---

# Problem-Qualified Segment

## Pre-Flight Gate

Require a dossier or provisional zero-data evidence ledger plus its Research Receipt when external evidence was used. If the only inputs are demographic assumptions or public company traces, return `INSUFFICIENT EVIDENCE` or `PROVISIONAL` and route upstream.

## Skill Acquisition

Load patterns 5, 6, 9, and 11 from `genius.md`. Distinguish a problem-qualified segment (who demonstrably has the problem) from a personally valuable proposition (what useful information you can create for them).

## Input Required

- Evidence rows and problem clusters
- Consequences, triggers, alternatives, and urgency evidence
- Candidate segment, company, and person attributes
- Known counterexamples

## Execution

1. Generate candidate problem statements from the evidence, not from product features.
2. For each, identify the worst version: consequence, timing, failed alternative, and observable trace.
3. Score evidence coverage across customer, company, category, competition, and context.
4. Define concentric fit: segment conditions, company state, and person responsibility/access.
5. Write positive indicators, negative indicators, hard disqualifiers, and unresolved questions.
6. Test against known good fits and counterexamples; preserve exceptions.
7. Return `QUALIFIED`, `PROVISIONAL`, or `REJECTED` with rationale. `QUALIFIED` requires two independent evidence methods and case-level evidence tying an action, purchase, interview, or verbatim customer source to the stated problem, consequence, and segment. Aggregate survey behavior alone does not clear the floor.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| Enterprise | Buying group and access constraints join person fit |
| Founder-led sale | Founder problem ownership can satisfy person fit temporarily |
| Consumer | Situation/identity replaces company/person layers where appropriate |
| Category creation | Competition includes status quo and internal workaround |

## Output Requirements

PQS statement, worst-version problem card, Five-Cs evidence matrix, concentric qualification, indicator/disqualifier list, counterexample test, verdict, and next evidence need. Use `references/prompts-v2/problem-qualified-segment.md`.

## Quality Gate

- The problem is observable and consequential, not a vague aspiration.
- All three fit layers cohere.
- At least one counterexample is tested.
- A `QUALIFIED` verdict clears the direct-evidence floor; otherwise it is `PROVISIONAL`.
- Demographic proxies are labeled and justified or removed.
- PVP and message work are not performed here.
