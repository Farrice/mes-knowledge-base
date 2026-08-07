# MAP — Loop / Compound Engineering Integration

Label: wayfinder:map · Charted 2026-07-24 · Tracker: local markdown (tickets/)

## Destination

A **ranked integration brief**: every candidate loop-engineering / compound-engineering upgrade scored on fit, cost, and risk against this system as it actually exists — with an explicit go/no-go per candidate, "this is a waste" verdicts where earned, and execution routed to the owning OS for each go. Decisions, not deliverables.

## Notes

- **Constraint (Farrice, 2026-07-24): zero context cost as much as possible.** New loops must live in deterministic code (hooks, Python, launchd) and existing files — no new always-on CLAUDE.md prose. Earn-your-tokens exceptions allowed only when a loop works within the existing subscription at minimal marginal cost and maximum effectiveness; each exception priced explicitly in the brief.
- **Extend, never rebuild** (standing rule): the system already runs ~10 compound loops — solution recorder, feedback ratchet, learning router, evolution orchestrator, steering loop, memory harvest→distill, wargame failure-maps, calibration, revenue-tracker outer loop, offer red-team. Candidates compose with these or die.
- Skills every session should consult before proposing anything: `nate-b-jones-auto-improvement-loops` (nate-auto-* workflows), `harness-evolve`, `self-evolving`, `ray-amjad-agentic-ladder` (Boris Cherny ladder), `patrick-debois-cdlc`.
- Research is Receipt-carrying, never from training memory. Proven-vs-hype discipline is explicit in every research ticket.
- Farrice's ask includes a standing kill-switch: "point me away from it if it's a waste." The brief must be allowed to conclude mostly-no.

## Decisions so far

- (charting session, 2026-07-24) Destination = ranked integration brief; all four surfaces in scope (existing-loop audit first, delivery quality, harness self-improvement, revenue ops); canon = researched, proven-vs-hype; constraint = zero context cost.
- **(Farrice, 2026-07-24) REPAIR-FIRST LOCKED**: making existing loops actually work — designed, integrated, engineered properly, maximum value — outranks any new addition. "A bunch of things built without actually working" is the named failure mode. New loops enter the brief only if genuinely novel, proven, and not already covered by a repairable existing loop. Canon research explicitly widened to lesser-known/underrated loop patterns (incl. how Boris Cherny, Claude Code's creator, runs compound engineering).
- [Canon research: proven vs. hype](tickets/0001-canon-research-proven-vs-hype.md) — **compound engineering (learning loop) and loop engineering (autonomy loop) are two different canons wrongly fused**; Cherny belongs to the latter. Verification is the load-bearing primitive. Underrated: metric-ratchet loop (only independently-replicated pattern), "map not encyclopedia" rules files (validates our zero-context-cost constraint from both frontier labs), fresh-context Ralph ≠ official plugin. Full receipts: [research/2026-07-24-canon-proven-vs-hype.md](../research/2026-07-24-canon-proven-vs-hype.md).
- [Existing-loop inventory audit](tickets/0002-existing-loop-inventory-audit.md) — **4 of 12 loops compounding, 7 OPEN, 1 DEAD (wargame failure-maps: no reader code exists).** Repair-first vindicated: the learning arms mostly work; the *closing* arms (review, outcome-chase, weekly-closeout — never run) are where loops stay open. Top repairs are one-plist-key / one-mission-card sized. Full evidence: [research/2026-07-24-loop-inventory-audit.md](../research/2026-07-24-loop-inventory-audit.md).

- [Farrice verdict pass](tickets/0004-farrice-verdict-pass.md) — **ALL 12 GO** (Farrice on record 2026-07-24): #7 pull-half only, #12 under lock-and-cap conditions after #8, DO-NOT-DO list ratified as standing refusals. **Scope change: destination redrawn from brief-only to brief + execution.**
- [Assemble the brief](tickets/0005-assemble-integration-brief.md) — destination artifact shipped: [04-deliverables/LOOP-ENGINEERING-INTEGRATION-BRIEF.md](../04-deliverables/LOOP-ENGINEERING-INTEGRATION-BRIEF.md); doubles as the execution checklist. **Map is DONE as decision record; execution in flight.**
- [Gap map: canon × audit](tickets/0003-gap-map-candidate-list.md) — **12 draft candidates: 10 REPAIR (ranks 1–10) + 2 NEW (token ratchet, capped metric-ratchet pilot), all zero context cost, plus a 7-item DO-NOT-DO list** (no Every plugin, no Ralph here, no append-to-CLAUDE.md compounding, no human-optional review, no LEDGER_ENFORCE yet). Draft asset: [research/2026-07-24-gap-map-draft-candidates.md](../research/2026-07-24-gap-map-draft-candidates.md). Awaiting Farrice verdict pass (ticket 0004).

## Not yet specified
- Which go'd candidates get an in-session proof-of-concept first, and in what order. Hangs on the ranking.
- Where each go lives (which owning OS / hook / launchd job). Per-candidate; hangs on the brief.
- How compounding gets *measured* going forward — the metric that distinguishes "loop exists" from "loop compounds." Likely graduates from the canon + audit tickets together.
- Whether Codex-coexistence (two harnesses, one tree) changes which loop patterns are safe to run. Surfaced if research shows loop patterns that assume a single writer.

## Out of scope

- **Executing the integrations.** The map ends at the brief; wiring routes to the owning OS as fresh work.
- **Rebuilding any existing loop.** Extend-never-rebuild is standing; a candidate that requires a rebuild is auto-no in the brief.
- **Anything with paid-API marginal cost** beyond the existing subscription (cost-gated services stay out of loop machinery).
