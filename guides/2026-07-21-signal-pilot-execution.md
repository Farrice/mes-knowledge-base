---
date: 2026-07-21
session: signal-pilot-execution
tier: operator-guide
status: enriched
---

# Signal Pilot — What We Built 2026-07-21 and How to Use It

> One marathon session: the COS daily board, three blind adversarial passes (audit kill → three-offer test → channel/pricing pressure test), a locked sprint offer with paste-ready LinkedIn assets and 30 prospects, and three permanent system organs — the $0 offer-truth gate, the /offer-redteam loop, and the dispatch seating law. Companions: `docs/solutions/2026-07-21-*.md` (three cards), `_active/linkedin-launch/{02-offer,03-launch,05-lead-gen}/`, `.agent/handoffs/2026-07-21-signal-pilot-execution.md`.

## ⚡ If you only read 10 lines

1. Sprint offer LOCKED: **Signal Pilot: Practitioner Edition** — $2,000 prepaid/14d; extraction → 7-email sequence SENT to their list + 4 posts + 1 sales asset. Spec: `_active/linkedin-launch/02-offer/OFFER-LANE-VERDICT-2026-07-21.md`
2. Pricing frame, verbatim, never improvised: *"Founder pricing for the first three pilots is $2,000 prepaid — less than what you charge one cohort of your own program. It goes up the day the first case study exists."* No Cooz citations. No discounting.
3. **Two-gate dispatch:** LinkedIn activity (30d) gates the SEND CHANNEL; authority-asymmetry gates the FLAGSHIP bet. Dormant prospect ≠ dead prospect ≠ dead lane — re-route to their live channel.
4. Day-1 flagships: **Rosner** (20K beehiiv) + **Broxterman** ($42K launch precedent). Rusin/Hanson = cycle two, IG/funnel only.
5. **Send-before-build:** no asset until the day's sends are logged (`python3 execution/revenue_tracker.py log`). Two prior plans died building.
6. New offer idea? `python3 execution/offer_gate.py check --offer X --outcome "..." --demand-receipt "..." --units-sold N` ($0, advisory) → `/offer-redteam` for the heavy loop.
7. **No unseated dispatches:** every Agent/agent() call names a model — `sonnet` executes, `opus` for hardest verification only, Fable conducts. Doctrine §Dispatch seating law.
8. Cold-read any sales asset against `councils/buyers/practitioner-founders.md` before sending.
9. Kill conditions live: day-7 <3 fit-conversations → Tier-1 brand-teardown side-bet primary; 20 convos/0 pilots → /offer-redteam with shelved re-aim (exec coaches / B2B consultants).
10. Dead, permanently: Alignment Audit (all forms), TrendScale, Cooz-as-pitch-target. Cards exist; don't re-solve.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `python3 execution/offer_gate.py check --offer "X" --outcome "..." --demand-receipt "..." --units-sold N` | PASS/FLAG + logged fire (`.agent/offer-gate-log.jsonl`) | Any new offer or revenue-spine idea, BEFORE building on it |
| `python3 execution/offer_gate.py history` | Recent gate fires | Auditing what got flagged |
| `/offer-redteam` | 3-agent blind verdict (prosecutor/defender/evidence) + cheapest real-world test | Gate flags, gut says "is this real?", or pre-commitment on a new spine |
| `/resume signal-pilot-execution` | This thread, full context | Every Signal Pilot work session |
| `python3 execution/revenue_tracker.py log "<send>" --revenue 0 --outcome "sent to <name>"` | Logged send (unlocks building for the day) | Immediately after EVERY outreach send |
| `/panel-sync` | Reloads the pressure-test panel (Ross/Lara/Oren) | Revisiting lane/pricing with new data |
| `councils/buyers/practitioner-founders.md` + gauntlet prompt | Seat-by-seat JUMP/LEAN/SCROLL/WINCE read | Before any cold asset ships |

## The mental model

**1. The market votes on outcomes, not diagnoses.** Three passes converged on one economics: nobody pays for a finding ("clarity"); they pay for the fix (emails sent, posts shipped, calls booked). Audits and diagnostics are free doors or $29 tools. Any future offer whose outcome sentence contains a process-benefit word is pre-failed — that's what offer_gate.py checks.

**2. Reachability is a channel variable, not a lane variable.** "Nobody's answering" feels identical to "wrong market" from inside. Sort prospects on two independent axes (active-here? / worth-pursuing-hardest?) before concluding anything about the lane. Most dead-lane verdicts are dead-channel verdicts in a bigger costume.

**3. The behavioral gate outranks the analytical ones.** Two plans died with clean strategy and blank scoreboards. Send-before-build is the only clause distinguishing plan three from plans one and two. Every other gate protects quality; this one protects existence.

**4. Cost-tier discipline is one principle at two altitudes.** No sentence at a higher polish tier than it earns (density rule); no dispatch at a higher model tier than the work requires (seating law). Both are "work smarter" made physical.

## Per-capability sections

### offer_gate.py — the $0 offer-truth guard
**What it is:** stdlib checker, three questions from the audit kill: concrete outcome? demand receipt? units sold? Advisory-only (compass-not-cage), exit 0 always, fires logged.
**When:** every offer-shaped idea before any downstream build.
**When NOT:** validated offers with ≥3 non-warm sales (market already voted); pricing tweaks (use /jam or the CFO seat).
**Worked example:** run against the dead Alignment Audit → 3/3 flags; against the Signal Pilot → 1 flag (zero units sold — true).
**Honest edges:** keyword heuristic for process-benefits — a cleverly worded bad outcome can pass; the red-team catches what the gate misses. Not hook-wired (deliberate: hook config was already drifted; wiring is a proposed follow-up, Farrice's call).

### /offer-redteam — the heavy anti-echo-chamber loop
**What it is:** three blind agents — prosecutor (default kill), defender (must concede), evidence (receipts only) — then synthesis with dissent preserved and the cheapest real-world test named. Workflow: `.agent/workflows/offer-redteam.md`.
**When:** new revenue spines; whenever Farrice's gut asks "is this a made-up offer?"
**When NOT:** questions answerable by one evidence sweep (cheaper); already-validated offers.
**Worked examples (same day):** killed the $400 audit in one pass; promoted the Signal Pilot ONLY-IF-MODIFIED with converging blind modifications.
**Honest edges:** costs ~6-9 agent runs; blind convergence is strong signal but still pre-sale — only a logged close is proof.

### councils/buyers/practitioner-founders.md — standing cold-buyer panel
**What it is:** 5 seats anchored to real prospect shapes (launch-mode educator, big-brand/dead-LinkedIn founder, 20K-list scientist, cohort-runner gatekeeper, NO-FIT), walked through assets in realistic order (DM → profile → post).
**When:** pre-send on any cold asset; re-run after copy changes.
**When NOT:** internal docs, warm comms.
**Worked example:** caught "1,000+ transformations" (unverifiable), the free-year story as boundary-risk, and a guru-cadence closer — all fixed same night; verdict "polite maybe, one live door" redirected effort to service-proof.
**Honest edges:** seats are LIKELY-labeled inferences until calibrated against real reply data (`councils/buyers/calibration.jsonl`).

### Dispatch seating law — token economy made law
**What it is:** doctrine section (orchestration-doctrine.md): unseated dispatches inherit the conductor's model, so every dispatch names a seat — sonnet executes, opus for hardest verification, Fable conducts only.
**When:** every Agent call, every workflow script pre-launch review.
**Honest edges:** advisory, not lint-enforced; a one-time sweep of standing workflow scripts for unseated agent() calls is the open follow-up.

### The day's strategy artifacts (use, don't rebuild)
Offer one-pager + qualification checklist (`02-offer/OFFER-LANE-VERDICT-2026-07-21.md`) · gauntlet-fixed profile pack, prose-clean 0/10 (`03-launch/PROFILE-REBUILD-2026-07-21.md`) · 15 practitioner prospects with per-prospect spec-sample angles (`05-lead-gen/PRACTITIONER-PROSPECTS-2026-07-21.md`; 12 prices need 2-min verification) · 13 funded-brand prospects for the side-bet (`05-lead-gen/PROSPECT-LIST-2026-07-21.md`) · avatar dossier as content layer (`01-research/AVATAR-DOSSIER-ALIGNMENT-AUDIT-2026-07-21.md`, offer-dead banner on top).

## Composition table

| Stack | When it earns its cost |
|---|---|
| offer_gate → /offer-redteam → buyer gauntlet | Full pipeline for a NEW offer: $0 filter → adversarial verdict → copy check. Skip stages for smaller bets |
| Two-gate dispatch × prospect lists | Re-rank any outreach list before spending sends; add "posted last 30d" ahead of audience size |
| VOICE-CARD (BLEND) + prose_classifier + gauntlet | Any cold asset under Farrice's name: voice-true → machine-clean → buyer-tested |
| /panel-sync + calibration.jsonl | Month-1 retro: panel predictions vs real reply data — the panel earns trust or gets rebuilt |
