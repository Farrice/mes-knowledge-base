---
status: closed
type: research
blocked_by: [0001, 0002]
claimed_by: loop-eng-frontier-2026-07-24
---

# 0003 — Gap map: canon × inventory → scored candidate list

## Question

Crossing the proven canon (0001) against the audited inventory (0002): what are the concrete integration candidates, and how does each score?

Per candidate: what it is, which existing loop it extends (extend-never-rebuild — no host loop, no candidate), footprint (must satisfy zero-context-cost; any earn-your-tokens exception priced in tokens/$), risk to current system (what could it break, incl. Codex-coexistence single-writer concerns), expected compounding payoff, and a draft go/no-go with reasoning. Include repair candidates: an OPEN existing loop that the audit found may outrank any new integration. Rank the full list.

AFK. Deliverable: draft ranked candidate list as a linked asset — the raw material for the grilling pass (0004), not yet the brief.

## Resolution

Draft ranked list: [`../../research/2026-07-24-gap-map-draft-candidates.md`](../../research/2026-07-24-gap-map-draft-candidates.md) — 12 candidates (10 REPAIR, 2 NEW), all zero context cost, plus an explicit DO-NOT-DO section. Repair-first held: repairs occupy ranks 1–10.

| Rank | Candidate | Type | Draft verdict | Footprint |
|---|---|---|---|---|
| 1 | Sleep-proof launchd (RunAtLoad catch-up) | REPAIR | GO | 2 plist keys |
| 2 | Calibration-closure mission card (19 seeds) | REPAIR | GO | 1 card, ~15 min Farrice |
| 3 | Routing-trial verdict (expires 07-24) + session-ledger report | REPAIR | GO | ~50-line py |
| 4 | Phase-2 consumer on mission-runner train | REPAIR | GO | ~20 lines |
| 5 | Offer-gate routing binding | REPAIR | GO | 1 dict entry |
| 6 | Wargame failure-map canonical home | REPAIR (DEAD loop) | GO | ~30 lines or reuse docs/solutions/ |
| 7 | Memory-review pull surface in /cos | REPAIR | GO (auto-provisional half CONDITIONAL) | ~15 lines |
| 8 | Fix red verify-fleet (30/86) + citation-integrity | REPAIR | GO | triage-first |
| 9 | Solution-injection hit-rate logging | REPAIR | GO | 3 lines |
| 10 | Steering-loop escalation | REPAIR | GO-LEAN | ~11 lines |
| 11 | CLAUDE.md token ratchet in CORE DRIFT scan | NEW | GO | ~10 lines |
| 12 | Metric-ratchet pilot on verify-fleet pass rate | NEW | CONDITIONAL GO | 1 script, locked+capped |

**DO-NOT-DO (pointed away):** Every's compound-engineering plugin (ceremony + tokens duplicating loops we already run); Ralph loops on this repo (Huntley disowns existing-codebase use; the official plugin isn't even real Ralph); loop sprawl before consumers exist; append-to-CLAUDE.md compounding (both frontier labs warn against it); human-optional review (severs taste calibration); LEDGER_ENFORCE flip (premature); chasing HYPE numbers (300–700%, 2–3x claims).

**Time-sensitive:** rank 3's routing-enforce trial expires 2026-07-24 — extend/expire decision needed same-day.
