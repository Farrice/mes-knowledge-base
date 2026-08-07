# Loop / Compound Engineering — Integration Brief (LOCKED)

**Date:** 2026-07-24 · **Verdict:** Farrice, on record: all 12 GO (0004) · **Decision record:** [wayfinder/MAP.md](../wayfinder/MAP.md)
**Evidence base:** [canon (proven-vs-hype)](../research/2026-07-24-canon-proven-vs-hype.md) · [loop inventory audit](../research/2026-07-24-loop-inventory-audit.md) · [gap map](../research/2026-07-24-gap-map-draft-candidates.md)

## The one-paragraph truth

The system's ~12 compound loops capture signal well (4 already compound) but fail at the *closing* arm — unread queues, never-run rituals, sleep-lost schedules. The integration is therefore 10 repairs + 2 constraint-defending additions, all zero always-on context cost, ~150 lines of deterministic code total. The two canon concepts stay distinct: compound engineering = learning loops (repairs 2, 4, 6, 7, 9), loop engineering = autonomy loops (1, 3, 8, 12). Verification is the load-bearing primitive throughout.

## Execution checklist

| # | Candidate | Verdict | Status |
|---|---|---|---|
| 3i | Routing-trial verdict (expired-today trial) | GO — same-day | ✅ 2026-07-24 — EXTENDED to 08-07, verdict in routing-enforce-trial.json |
| 1 | Sleep-proof launchd (RunAtLoad, 2 plists) | GO | ✅ 2026-07-24 — RunAtLoad live; outcome-chase fired first-ever run on load |
| 5 | Offer-gate routing binding | GO | ✅ 2026-07-24 — offer_redteam_gate binding live (33 bindings parse) |
| 9 | Solution-injection hit-rate logging | GO | ✅ 2026-07-24 — live-fire verified, solution-injections.jsonl |
| 2 | Calibration-closure mission card (19 seeds, ~15 min Farrice) | GO | ✅ 2026-07-24 — T2 card in mission queue awaiting Farrice's 15 min |
| 6 | Wargame failure-map home (docs/solutions/ route) | GO | ✅ 2026-07-24 — wargame step 8 banks failure-maps to docs/solutions/ |
| 7 | Memory-review line in /cos brief — pull half ONLY | GO (auto-provisional = NO) | ✅ 2026-07-24 — /cos brief line live (9 pending rules surface) |
| 4 | Phase-2 consumer: monthly orchestrator → 1 mission card | GO | ✅ 2026-07-24 — consumer live; first card emitted (oren-operational-systems, T2) |
| 3ii | session_ledger_report.py over 685 would-blocks | GO | ✅ 2026-07-24 — report live: 817 events = 92 sessions, 8.9x noise |
| 10 | Steering-loop escalation + miss-rate metric | GO-lean | ✅ 2026-07-24 — escalation fires at ≥2 misses; steering_misses_7d=23 |
| 11 | CLAUDE.md token ratchet in monthly CORE DRIFT scan | GO | ✅ 2026-07-24 — ratchet live, baselines: CLAUDE.md 18.9KB / MEMORY.md 20.1KB |
| 8 | Verify-fleet triage | GO, triage-capped | ✅ 2026-07-24 — audit's 30/86 was a STALE snapshot; live fleet 68/1/4, single fail = unblessed deliberate change (Extract v3.0 + Meg v1.1) → blessed, now 69/0/4; citation-integrity clean (295 sources) |
| 12 | Metric-ratchet overnight pilot | GO → ARMED-PARKED | ✅ 2026-07-24 — fleet went green during #8, no honest metric headroom; full design + non-negotiable terms banked as .agent/mission-queue/parked/card-metric-ratchet-pilot-ARMED.md with explicit triggers (≥5 real fleet failures or a Farrice-named metric). Running it tonight would violate standing refusal #3 |

Full per-candidate detail (footprint, risk, canon backing): [gap map](../research/2026-07-24-gap-map-draft-candidates.md).

## Standing refusals (ratified with the verdict — do not revisit without new evidence)

No Every compound-engineering plugin · no Ralph loops on this repo (either variant) · no new cron loops without a named consumer · no append-to-CLAUDE.md compounding · no human-optional review (Farrice's felt verdict is the calibration source) · no paid external critic tools · no ACE implementation · no LEDGER_ENFORCE flip until 3ii's report supports it · no 2–3x / 300–700% numbers as targets or citations.

## Compounding metric (graduated from fog)

A loop counts as COMPOUNDING only when both arms show receipts: signal captured AND later behavior demonstrably changed (file/log evidence). Next loop audit re-runs the 12-loop table against this bar; #9's injection log is the template for making arms measurable.

## Constraints that survived the whole effort

Zero always-on context cost · extend-never-rebuild · deterministic closers (no loop may depend on a human remembering a ritual, and none may depend on AI memory without a deterministic backstop) · single-writer tree (unattended writers take session_lock; only #12 edits source unattended).
