---
thread: social-listening-head-spec
status: active
resume_hint: Date shaped: 2026-07-16 · Shaped via: /raw-intent-bridge + one question round (Farrice answered all)
pin: true
---

# Social Listening Head — Build Spec (SHAPED, READY TO EXECUTE)

**Date shaped**: 2026-07-16 · **Shaped via**: /raw-intent-bridge + one question round (Farrice answered all)
**Status**: Spec complete. Build NOT started. Execute in a fresh session: `/resume social-listening-head`

## Raw intent (verbatim felt standard — carry into the build)
- "start using apify more effectively and smartly while being budget aware"
- "have a true social listening head"
- "we underutilize it and underuse it"
- "pulling some data and certain research that could be so much better and enrich"
- On the pulse: "I've been trying to get a world pulse read... so that I can understand what's going on in the world. I can avoid doing scrolling and reading social media. It might be useful and help my content or views and perspectives."
- Budget (HARD requirement): "I love excellence, and I don't want us to be... reaching out with a bill that I can't afford to pay!"

## Farrice's decisions (locked 2026-07-16)
1. **Actor scope: ALL 10 Scrape Creators actors** (keep existing generic actors as cheap fallbacks — do NOT remove clockworks/apidojo).
2. **Done state = all three heads**:
   - Auto-routing: social/audience/trend research fires Apify first (raw data → synthesis), via routing binding + directive update.
   - `/social-listen` front door: niche/creator/hashtag/question → actor selection → budget-checked scrapes → synthesized listening brief with receipts.
   - **Recurring listening pulse (centerpiece)**: scheduled scans of tracked creators/hashtags per lane → standing "world pulse" brief. Feed it into the COS morning brief (see memory: COS World Pulse Brief — briefs need researched world-pulse). This replaces doomscrolling.
3. **Lanes: all four** — Farrice brand/content (LinkedIn/Substack/S&C/DWA), MyBPM streetwear, Jen/SFV real estate FTHB, client/prospect niches (on-demand).

## Ground truth (verified this session)
- Existing layer: `execution/apify_client.py` (7 whitelisted actors, $29 cap, 70%/90% thresholds, never-raise fallback contract), `directives/apify-usage-policy.md`, `.mcp.json` tools list, `execution/hooks/apify_mcp_bootstrap.py`. **EXTEND, never rebuild.**
- July usage: $2.21 of $29, 30 runs (~8%) — underuse confirmed. ~7x headroom exists.
- Scrape Creators catalog (via `https://api.apify.com/v2/store?username=scrape-creators`, all PAY_PER_EVENT):
  - `scrape-creators/best-tiktok-scraper` (search/trending/profile/hashtag/video)
  - `scrape-creators/best-tiktok-video-scraper`
  - `scrape-creators/best-tiktok-profile-scraper`
  - `scrape-creators/best-tiktok-hashtag-scraper`
  - `scrape-creators/best-tiktok-transcripts-scraper`
  - `scrape-creators/best-tiktok-followers-scraper`
  - `scrape-creators/best-tiktok-following-scraper`
  - `scrape-creators/best-youtube-transcripts-scraper`
  - `scrape-creators/best-youtube-channels-scraper`
  - `scrape-creators/best-youtube-comments-scraper`

## Build plan (fresh session)
1. **Wrapper extension** (`execution/apify_client.py`): add 10 actors to `ACTORS`. PAY_PER_EVENT actors don't have flat per-result cost — the wrapper MUST read actual cost from the run response (`usageTotalUsd` on the run object / `ACTOR_RUN` record) and log actuals, not estimates. Add per-run cost ceiling arg (default $0.25, refuse above without explicit flag).
2. **Budget architecture (the "can't afford the bill" guard)**:
   - Keep $29 hard cap + existing yellow/red thresholds (do not raise).
   - Pulse gets its own sub-ledger: **$5/mo pulse budget** inside the $29; pulse runs skip (not fail) when pulse sub-budget or global yellow is hit.
   - Per-run ceiling on every pay-per-event call; pre-run `budget-status` check mandatory in the pulse script.
   - Weekly cadence per lane, NOT daily (4 lanes × ~4 runs/mo × ~$0.15 ≈ $2.40/mo — verify actual pay-per-event pricing per actor during build with one cheap PoC run each).
3. **`.mcp.json`**: add the 10 actor IDs to the Apify MCP tools list (policy says both files must stay in sync).
4. **`directives/apify-usage-policy.md`**: update approved-actor table (7→17), add pay-per-event section + pulse sub-budget rules.
5. **`/social-listen` workflow** (`.agent/workflows/social-listen.md`): input = niche/creator/hashtag/question + optional lane; picks actors, runs budget-checked scrapes via apify_client, synthesizes brief (Apify → synthesis pipeline per policy), receipts on every claim. Route transcripts-heavy asks to transcript actors (the enrichment Farrice is missing today).
6. **Recurring pulse**: `execution/social_pulse.py` + launchd plist (weekly per lane, staggered). Lane config file `.agent/social-listening-lanes.json` (creators/hashtags/keywords per lane; client lanes on-demand only). Output: pulse brief to `.agent/cos/` so `/cos` morning brief picks it up. Deterministic backstop: log every pulse run to the apify ledger (never AI-memory-dependent observability).
7. **Routing**: add binding in `directives/routing-bindings.md` + `routing_enforcer.py` BINDINGS (update together) — social/audience/trend research → Apify-first pipeline; also point `research.py` users to it in the directive.
8. **PoC gate (required before shipping)**: one real run per actor category on a live lane (e.g. DWA Threads hashtag scan + one transcript pull), record ACTUAL per-event costs into the policy table, then finalize via chain_runner.
9. Cost gate note: Apify actor runs are paid — hook may require `cost_gate.py approve`. Work WITH the gate.

## Deferred / explicitly out of scope
- Asana / "Involve or orchestrator + Opus" — Farrice's framing referenced a separate orchestration test, not this build. No Asana integration here.
- Followers/following scrapers wired but no lead-gen workflow yet (build only when a lead-gen need appears).
