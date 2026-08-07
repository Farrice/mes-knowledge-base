---
status: closed
type: research
blocked_by: []
claimed_by: loop-eng-frontier-2026-07-24
---

# 0002 — Existing-loop inventory: which of our loops actually compound?

## Question

Enumerate every feedback/compounding loop already wired into this system, and for each answer: **does it actually close and compound, or does it merely exist?** Evidence, not vibes.

Known loops to audit (extend the list as found): solution recorder (`docs/solutions/` + resurfacing), feedback ratchet, learning router (harness frontier loops), `evolution_orchestrator.py auto` (daily launchd), steering loop hook, episodic→sovereign memory harvest/distill (launchd jobs), wargame failure-maps, calibration + ground-truth rubric, revenue-tracker outer loop, offer_gate / offer-redteam, session ledger observe-log, skill-evolution / autoresearch phases.

For each: (a) input signal, (b) where the learning lands, (c) evidence it changed later behavior, (d) verdict — COMPOUNDING / OPEN (loop exists but doesn't close) / DEAD. Known smells to chase: 101 deliverables awaiting outcome data + 24 check-ins due (outer loop open?), observe-log misses, evolution queue backlog, "Audit Stage 2 / Stage 4 lever decision pending (overdue)."

**Priority raised (Farrice, 2026-07-24, repair-first locked):** for every OPEN or DEAD loop, the deliverable must include a concrete repair recommendation — what would make it actually close — since repairs now outrank new integrations in the brief.

AFK — local files, `.agent/*.json` trackers, launchd state, git history. Deliverable: inventory table as a linked asset in the project folder.

## Resolution

Full report: [`../../research/2026-07-24-loop-inventory-audit.md`](../../research/2026-07-24-loop-inventory-audit.md) (evidence per loop: log tails, launchd state, mtimes, git).

**Verdict: 12 loops audited — 4 COMPOUNDING, 7 OPEN, 1 DEAD.**

| Loop | Verdict | One-line evidence |
|---|---|---|
| Solution recorder | COMPOUNDING | 51 cards through 07-24; router injects; appears in 31/64 facade fires |
| Feedback ratchet | COMPOUNDING | 99+29 finalize records, daily through 07-24; feeds phase-2 queue |
| Learning router | COMPOUNDING | skill-weights 0.5–1.67 spread, rewritten 07-23, applied in find_skill.rank() |
| evolution-auto | COMPOUNDING* | daily/weekly/monthly all ran; today's 07:00 missed (machine asleep) |
| Steering loop | OPEN | 54 misses logged; zero consumers of the log beyond byte-size |
| Memory pipeline | OPEN at review | harvest 5447/5447 daily; 9 distilled rules stuck pending-review since 07-19 |
| Wargame failure-maps | DEAD | zero banked artifacts on disk; no reader code exists |
| Calibration/ground-truth | OPEN | 66/68 human-calibrated; 19 seeds pending since 07-17; rubric not load-bearing |
| Revenue outer loop | OPEN | 4/177 deliverables have revenue data ($4,400); outcome-chase launchd log never created; /weekly-closeout has 0 finalize records ever |
| offer_gate | OPEN | 2 log entries, both from build day 07-21; no trigger wired |
| Session ledger | OPEN | 685 would_blocks unread; routing-enforce trial expires 07-24, review never ran |
| Skill-evolution Phase 2 | OPEN | 130 queued (93 in July); consumed once (07-06) |

**Top repairs (all zero-context-cost, deterministic):**
1. Sleep-proof launchd (`RunAtLoad`/catch-up keys) on evolution-auto + outcome-chase — one plist key each; fixes loops 4 and 9 and router cursor lag.
2. Ship the 19-seed calibration review as a mission card — 2 net reviews cross the 68 threshold and the already-written R2 blind-pass enforcement in chain_runner goes live for free.
3. Monthly orchestrator emits one Phase-2 mission card for the top auto_evolve_eligible candidate → mission-runner executes; closes the ratchet's fix-arm.

**Cross-cutting finding:** `/weekly-closeout` — designed closer for 4 of the open loops — has never been run. Every repair either routes around it or makes it fire deterministically.
