---
thread: crossing-waves
status: ready
resume_hint: Send Monday's 10 founder DMs (V1 free-screenshot lead), then log real replies to councils/buyers/calibration.jsonl
unfinished: Calibration ledger has 3 pending predictions; bench crossings geoff-woods-handshake-bos + baldacci-x-kdp; no first case study yet
branch: main
pin: true
---

# Antigravity Crossings — Waves 2+3 & Buyer Council OS (10 blends, Mike Taylor forge)

## Purpose
- **Next session should do:** Send Monday's 10 founder DMs from the shipped cold-DM set, then log real replies/bookings against the 3 falsifiable predictions already written to `councils/buyers/calibration.jsonl` — this is the first ground-truth test of the whole predictive stack. Secondary: finish the crossing bench (`geoff-woods-handshake-bos`, `baldacci-x-sean-dollwet-kdp`).
- **Not in scope:** Re-forging any shipped crossing (10 exist, all PoC-proven); re-extracting Mike Taylor (watched-source forge complete); re-running the buyer council on the current offer (v2 retest done — S1 SHIP, S3 SHIP-with-watch).

## Load First
- `_active/linkedin-launch/05-lead-gen/outreach/cold-dm-set-founder-walkthrough.md` — the 5 first-touch variants + 3-step follow-up to send Monday; V1 free-screenshot lead is the sharpest.
- `_active/linkedin-launch/02-offer/buyer-council-verdict-v2-2026-07-19.md` — latest panel verdict; names the one binding constraint (no first case study).
- `councils/buyers/calibration.jsonl` — 3 prediction lines awaiting `real_outcome`; the ledger is the reason this stack compounds.
- `_active/linkedin-launch/02-offer/PROOF-TO-MARKET-OS.md` (v2.1) — founder-primary, cold/warm/hot ladder, make-right clauses both rungs (ratified 2026-07-19).
- `councils/buyers/corpora/proof-to-market-founders/zeitgeist-digest.md` — 26 receipt-carrying founder quotes; key finding: founders frame the problem as invisibility-inside-noise, not "unclear positioning."

## Current State
- **Objective:** Revive and extend the cross-skill "crossing" pattern (design-time fusion of two expert extractions), then put the new assets to work on the live revenue sprint.
- **What is already done:**
  - **Crossing Wave 2 (5):** `godin-handshake-dunford`, `dunford-handshake-haynes`, `haynes-handshake-geoff-stakeholder`, `kallaway-x-jenny-hoyos`, `meg-heckman-handshake-proof-ladder`.
  - **Crossing Wave 3 (4):** `kallaway-x-dunford`, `kallaway-x-priestley-sll`, `jenny-hoyos-handshake-diandra`, `hawley-handshake-vicious-hooks`.
  - **Buyer Council OS:** `/buyer-council` (TRIAGE + COUNCIL modes), standing roster `councils/buyers/`, calibration ledger; deep source `skills/mike-taylor-synthetic-research/` (watched-source forge, 7 `/mt-*` workflows, grounding ladder incl. new Tier 2.5 social-grounded rung with `/social-listen` binding + $0 fallback).
  - **Offer work:** founder-primary restage, 5 pillars realigned, cold-tier walkthrough LIVE, make-right clauses both tiers, DM set shipped and re-expressed via `kallaway-x-dunford`.
- **What is uncertain or stale:** Buyer panel seats 2/4/5 remain cold-generated (corpus speaks only for sub-$15M founder + gatekeeper voice). No first case study exists — the panel's binding constraint. Corpus expires ~2026-09-02 (45-day freshness rule).
- **Latest proof/receipt:** 9 finalizes this session, all PASS (8.33–8.67); commits `71c7132ca`, `52903712f`, `03c7d4627`, `20ab09ba4`, `3a39b0a35`, `00f98ae47` — local and `origin/main` in sync at `00f98ae47`.

## Suggested Skills / Workflows
- `/buyer-council` — panel verdicts on any artifact; TRIAGE for 5-minute directional calls, COUNCIL for stakes.
- `/mt-persona-grounding` — upgrade panel seats when new voice data (e.g. Monday's real replies) lands.
- `/kallaway-x-priestley-sll` — daily content cadence that stays novel past week 3; PoC already drafted a 5-day week.
- `/hawley-handshake-vicious-hooks` + `/jenny-hoyos-handshake-diandra` — season-arc series with arc-aware hooks, then structural specs per post.
- `/weekly-closeout` — 5 outcome check-ins due; 89 deliverables awaiting revenue data.

## Exact Next Prompt
```text
Monday DM send + calibration: send the 10 founder DMs from _active/linkedin-launch/05-lead-gen/outreach/cold-dm-set-founder-walkthrough.md (V1 free-screenshot lead), then log the real replies, bookings, and dominant objection to councils/buyers/calibration.jsonl against the 3 existing prediction lines. Run /mt-persona-grounding on any real founder replies to upgrade seats 1+3 toward transcript-grounded, and tell me where the panel was wrong.
```

## Acceptance Criteria
- 10 DMs sent; every `real_outcome: "pending"` line in `calibration.jsonl` updated with observed reply count, bookings, and the objection that actually dominated.
- An explicit written verdict on whether the panel's predictions held (reply band 1–3, booked 1–2, "$350 vs free ChatGPT" + opportunity-cost objections).
- If ≥1 walkthrough is booked and delivered: capture the case-study receipt that dissolves seat S2's block.

## Risk Notes
- **Concurrent sessions:** 6 sibling sessions were active on this tree at close. GOLDEN RULE — one live writer per tree; session lock `f6c6b1a1f81f` still held by this session and needs release (`python3 execution/session_lock.py release f6c6b1a1f81f`, classifier blocked it here twice).
- **Grounding honesty:** never report a panel verdict above the seat's tagged tier; cold-generated seats stay labeled as such.
- **Prose classifier:** structured workflow specs score FLAGGED ~5–8/10 by convention — do not sand crossing specs to chase a copy-tuned classifier.
- No secrets, credentials, or client PII in any artifact referenced here.
