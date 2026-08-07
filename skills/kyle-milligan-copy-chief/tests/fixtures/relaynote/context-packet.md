# RelayNote Shared Context Packet

> Fixture data. Not market evidence.

## Assignment

Create exactly three distinct, multi-line opening options for RelayNote and recommend one. The reader is an agency owner or operations lead at a 5–20-person agency. The only action is **Book a demo**.

- Placement: problem-aware B2B demo-page opening with unknown prior trust.
- Voice evidence: unavailable. Use a specific, operational, calm, non-shaming tone; imitate no person or unstated brand.
- Mechanism status: `NOT_VERIFIED_NON_APPLICABLE`. Mechanism-led claims and proprietary causal explanations are forbidden.

## Product Truth

- `PT-CAP-001` — RelayNote turns a completed call transcript into a draft follow-up email.
- `PT-CAP-002` — It extracts an assigned next-step owner and date when those details appear in the transcript.
- `PT-TEST-001` + `PT-TEST-002` + `PT-TEST-003` — The evidence is a 30-day synthetic test across 12 fictional agencies and 1,248 synthetic call records.
- `PT-MET-001` — 23% of assigned next steps were absent from the first manually drafted follow-up in that fixture.
- `PT-MET-002` — Median manual drafting time was 18 minutes in the fixture.
- `PT-MET-003` — Median RelayNote drafting time was 4 minutes in the fixture.
- `PT-MET-004` — Owner-and-date extraction accuracy was 91% on a held-out 200-call synthetic fixture.
- `PT-ACT-001` — Book a demo.

Use `product-truth.json` for exact qualifiers and prohibitions. These are synthetic fixture facts, never customer or market results.

## Frozen Opportunity Graph

Use this graph only when a route needs a promise spine. It is a synthesis of the listed PT IDs and introduces no new fact:

1. **Catalyst:** a completed agency call can produce a transcript containing an assigned owner/date when those details were stated (`PT-CAP-001`, `PT-CAP-002`).
2. **Recurring pattern:** the synthetic manual condition shows assigned-detail omission and drafting-time burden (`PT-TEST-001`, `PT-TEST-002`, `PT-TEST-003`, `PT-MET-001`, `PT-MET-002`).
3. **Bounded path:** RelayNote uses the completed transcript to prepare a follow-up draft and extract owner/date when present (`PT-CAP-001`, `PT-CAP-002`).
4. **Supported fixture result:** 4-minute median drafting in the synthetic condition and 91% owner/date accuracy on the held-out 200-call fixture (`PT-MET-003`, `PT-MET-004`).

This graph does not prove revenue, conversion, pipeline, customer, or causal business outcomes.

## Control Material

Five synthetic controls are available in `swipes/`. Use them only as the assigned route's method directs. Synthetic editorial labels are not response or market metrics and cannot substitute for audience/problem fit. Transfer structure only. `transfer-veto.json` forbids all control brands, metrics, testimonials, customer counts, source-video facts, and credentials.

## Existing Weak Draft

> Revenue teams are under pressure to move faster. RelayNote uses AI-powered conversation intelligence and workflow automation to help agencies optimize follow-up and improve pipeline efficiency. Our platform turns calls into action items and emails. Book a demo today.

## Truth Boundary

Do not claim or imply revenue lift, conversion lift, pipeline improvement, closed-won impact, customer adoption, endorsements, guaranteed capture, or live-market performance. Do not calculate or introduce `78% faster` or `14 minutes saved`; use the frozen 18-minute and 4-minute medians directly if needed.

## Output Contract

Follow `output-contract.json` exactly. Each factual clause must carry one or more supporting `PT-*` IDs in its annotation line. Produce no preamble, process diary, or extra alternatives.
