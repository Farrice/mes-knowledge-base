---
thread: jen-listings
status: ready
resume_hint: Farrice reviews 3 SFV FTHB Google Docs in Jen's Drive + confirms 3 verify-at-send figures; toggle pageless
unfinished: Verify-at-send: current rate / $200k illustration / current median. Optional: 2nd Jen asset via /copy-engine (WARM=$0). Outer loop stale: /weekly-closeout
branch: main
pin: true
---

# Handoff — Grounded Copy Engine + High-Stakes Proof Gate

**Session date:** 2026-06-02 · **Repo:** `/Users/farricecain/Google Antigravity` · **All work pushed:** `origin/main` @ `a3e644b7` (+ prior `07f67569`, `f0852c42`, `6847e403`).

## What this session built (one line)
A cost-safe, deterministically-grounded copywriting engine — from ungrounded "sophisticated guessing" to real research → verified claims → converting copy — proven end-to-end on a live market (Jen Santulan's SFV first-time-homebuyers).

## State: DONE + deployed. Nothing of mine is uncommitted.
Working tree's only dirty items are transient session ledgers + unrelated `_active/harness/elevation-track/e3/` work (not this session's — leave it).

## The system (all committed; don't rebuild — extend)
- **`execution/avatar_manifold_runner.py`** — the deterministic GROUND chokepoint. 3 tiers (`free $0` / `lean $0.11` / `deep $0.12`), per-market WARM reuse ($0 on iterations), STALE = $0 nudge (never auto-spends), budget-exhaustion fails **closed**. Research stack (fixed this session): **fast Gemini Search-grounding primary (~3s, ~$0)** → **Tavily free fallback** → free Reddit/HN + Apify YouTube for VOC → recall/[MODELED] degrade. **Perplexity dropped** (API key returns 401 quota-exceeded — consumer Pro ≠ API credits). The old slow Gemini Deep Research *interaction* API is now `--mode max` only.
- **`execution/verify_proof_ledger.py`** — deterministic exit-code proof gate. Standard mode: every stat/price/date present + labeled. **`--high-stakes`** mode (NEW): regulated markets (real-estate/financial/medical/legal) require every claim be **primary-source VERIFIED**, not merely labeled — LIKELY/UNCONFIRMED rejected.
- **`.agent/workflows/copy-engine.md`** — `/copy-engine` orchestrator. "Ground Once, Refine Free." 3 halt gates (intent / grounding-sufficiency / verification-with-high-stakes-detection). Registered in `routing_enforcer.py` (binding `cold_start_converting_copy`), CLAUDE.md routing table, SLASH_COMMANDS.
- **Retrofit:** 21 workflows (12 `luke-iha-copy-blocks` + 9 `luke-iha-avatar-machine`) carry a uniform FINALIZE tail; all 12 copy-blocks read `warm_core` cached intel. 6 avatar workflows had a re-grounding leak (fired paid research directly) — all repointed through the chokepoint.
- Freshness-tax hookify hook extended to recognize copy-grounding evidence.

## Deliverable produced (real, verified)
`_active/clients/jen-listings/deliverables/sfv-fthb-lead-copy/` — lead-magnet opt-in + VSL lead + re-engagement email for SFV first-time-homebuyers, mechanism "The Stacked-Door Path." Claims **primary-source verified** vs LAHD/LACDA/CalHFA (found+fixed 2 material errors: "stack-five" overstatement; missing $700k/$850k purchase-price caps below the $1M median). Uploaded to Jen's Drive folder "Jen Santulan — 2026 First-Time Buyer Engine" as 3 Google Docs (IDs in the folder; markdown converted clean).

## Next session focus (from Farrice)
1. **Review the 3 SFV Google Docs** + confirm the **3 Verify-At-Send figures** (current 30-yr rate, the "$200k" illustration, current $1M median) — they're LIKELY, not primary-verified (flagged by `--high-stakes`). Toggle each Doc to **Pageless** (View menu — the Docs API can't set it programmatically).
2. **Optional:** run `/copy-engine` on a 2nd Jen asset/market — grounding is now fast + ~$0 + cached (SFV is WARM).
3. **Outer loop is STALE** — 24 deliverables awaiting revenue/outcome data; run `/weekly-closeout` (~20 min).

## Gotchas / non-obvious
- "VERIFIED to the dossier" ≠ true. The Gemini grounding can misattribute; **always run `--high-stakes` for regulated markets** and cross-check primary sources.
- macOS `urllib` fails SSL (CERTIFICATE_VERIFY_FAILED) — the runner uses `requests` (certifi) deliberately.
- gws Drive query goes via `--params '{"q":...}'` (single quotes inside clash with bash — build the JSON with Python to a temp file).
- The design-workflow subagents no-op'd once (0 tokens) — for mechanical paste-retrofits, a deterministic Python script is more reliable than agent fan-out.

## Suggested skills (next session)
- **`/resume`** — pick up this thread by name.
- **`/copy-engine`** — produce more Jen copy ($0, WARM cache).
- **`/weekly-closeout`** — clear the stale outer loop (24 deliverables need outcomes).
- **`fact-verifier`** agent — for any new regulated-market claims before send.
- **`/craves-polish` / `/writers-room`** — refine the SFV copy off the cache at $0.
