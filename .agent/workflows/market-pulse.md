---
description: Twice-weekly supplement/performance market pulse — signals brief + content angles into the bank; the ear-to-the-ground loop for the Proof-to-Market lane
---

# /market-pulse — Supplement & Performance Market Pulse (2x/week)

**Cadence:** scheduled cloud routine Mon + Thu (see Trigger note at bottom) AND on-demand via `/market-pulse`.
**Modeled on:** `/platform-pulse` (delta-over-dump, receipts-labeled, propose-only). **Serves:** `revenue-5k-incumbency` → Proof-to-Market lane (`_active/linkedin-launch/02-offer/PROOF-TO-MARKET-OS.md`).

## What one run produces
1. **Signals brief** → `research_outputs/market-pulse/YYYY-MM-DD-pulse.md` (≤2 pages, density over completeness)
2. **5-8 fresh angles** → appended as a dated file in `_active/farrice-brand/content/bank/angles/`
3. (When warranted) **Dream 100 delta** — new/changed targets flagged as PROPOSED rows for `_active/linkedin-launch/05-lead-gen/dream-100-v1.md` — propose-only, Farrice ratifies

## Run protocol

### 1. DELTA BASELINE (read first, never re-derive)
- Last pulse in `research_outputs/market-pulse/` (founding brief `2026-07-18-founding-brief.md` = run #0)
- `PROOF-TO-MARKET-OS.md` §pillars — angles must map to P1-P5 (or flag a candidate P6 as PROPOSED, never silently add)
- Report ONLY what moved since last run. No re-summarizing the market.

### 2. SWEEP (WebSearch/Tavily floor — $0; Perplexity is DEAD, never propose credits)
Watchpoints, in priority order:
- **Launches & repositions:** new products, rebrands, retail expansions (Amazon/Target/GNC/Costco), category entries in supplement/performance/hydration/sleep/recovery/cognition
- **Funding & hiring:** raises, new CMO/Head of Brand hires (= fresh budget + fresh mandate = purchase occasion)
- **Regulatory heat:** FTC/FDA actions, warning letters, NAD cases in supplements (P2 fuel)
- **Category language drift:** new buzzword saturation, claim trends (P4 fuel)
- **AI-search shifts:** ChatGPT/Perplexity/Google-AIO changes affecting brand discovery; AI-referred commerce data in health/wellness (P5 fuel)
- **Voices:** what the named content-competitors published; white-space check (does the founding brief's category-of-one finding still hold?)

### 3. FILE
- Brief format: `## What moved` (dated items, each with source URL + VERIFIED/LIKELY/UNCONFIRMED label + "why it's a purchase occasion" line where applicable) → `## Angle candidates` (5-8, pillar-tagged, one line each) → `## Dream 100 deltas (PROPOSED)` → `## Watch next`
- Append angles file to the bank (same pillar-tag format as `2026-07-18-founding-angles.md`)
- Commit: `chore(pulse): market pulse YYYY-MM-DD` (per all-work-on-main)

### 4. GATES (non-negotiable)
- Named brands/people: label confidence; UNCONFIRMED = verify before any outreach use
- No angle ships to a post without truth-gate (no implied client scenes Farrice doesn't have), voice layer, prose gate
- Cost floor: $0 per run (WebSearch/Tavily). Gemini Deep Research only by explicit Farrice ask.
- Propose-only everywhere: the loop NEVER edits the OS doc, pillars, or Dream 100 directly.

## Trigger
Scheduled cloud routine: **Mon + Thu 13:00 UTC** (see `.agent/missions.jsonl` for the trigger id once registered). On-demand: `/market-pulse` any time. First run = the founding brief (2026-07-18, PoC satisfied).
