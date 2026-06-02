# SFV First-Time Homebuyer — Lead Copy (grounded + fact-checked)

**For:** Jen Santulan's first-time-buyer lead engine.
**Produced by:** `/copy-engine` (grounded → assembled → verified), 2026-06-02.
**Mechanism:** "The Stacked-Door Path."

## Files
- **`sfv-fthb-lead-copy.md`** — the deliverable: lead-magnet opt-in + VSL lead + re-engagement email.
- `proof-claims-ledger.md` — every factual claim with its label + source (provenance).
- `market-intel-warm-core.json` — the cached market psychology (emotion, core wound, beliefs, VOC). Reuse for free on any future SFV-FTHB copy.

## How it was grounded
Real research, not modeled guessing: Gemini Search-grounding (market landscape) + Tavily (web/forum sources) + Apify (YouTube VOC). Verbatim buyer language pulled from r/FirstTimeHomeBuyer, r/SFV, r/LosAngelesRealEstate, FB FTHB groups.

## Claims — verified against primary sources (LAHD / LACDA / CalHFA, 2026-06-02)
✅ **CONFIRMED** (safe to state):
- **LIPA up to $161,000** — active; funding limited via reservation dates (the scarcity is real).
- **Greenline grant up to $35,000.**
- **HOP purchase-price caps: HOP80 ≤ $700,000, HOP120 ≤ $850,000** — below the ~$1M Valley median (this is why the copy steers to under-cap pockets; do NOT drop this caveat).
- **FHA 3.5% down.**
- **Stacking is real but rule-bound** — not all programs combine (e.g. CalHFA Dream For All ≠ MyHome); lien-position order matters. Copy says "compatible ones," which is correct.

## ⚠️ VERIFY BEFORE SEND (3 items — flagged by the high-stakes proof gate)
These are time-sensitive or illustrative and were NOT primary-source-verified — confirm them with your current data before publishing, since your license is behind them:
1. **~6.5% 30-year rate** — confirm the *current* rate (it moves weekly). Update or soften to "near multi-year highs."
2. **"$200,000" / "$200k" down-payment figure** (headline + email subject) — this is ~20% of a typical Valley home (illustrative). Fine as a round-number hook, but confirm it reads as illustrative, not a quoted figure.
3. **~$1M median price** — confirm against current MLS/SFV data at send.

Re-run the gate any time: `python3 execution/verify_proof_ledger.py --draft <file> --ledger proof-claims-ledger.md --high-stakes`

## Refining this copy (free)
The SFV market is grounded and cached (WARM). Any refinement — `/craves-polish`, `/writers-room`, `/copy-block-audit`, or a new asset via `/copy-engine` — reuses the cache at **$0**. Only re-ground (`--refresh`, ~$0.04) if the market materially moves.
