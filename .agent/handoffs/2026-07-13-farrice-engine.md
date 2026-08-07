---
thread: farrice-engine
status: ready
resume_hint: Publish the Week-25 flagship article + run the 10-comment plan + DM the Gainful teardown
unfinished: Farrice hasn't published or logged metrics yet (ratchet is dark); fix 4 broken brand_radar IG handles (Gorgie/Momentous/Hilma/Joovv)
branch: main
pin: true
---

# Farrice Engine — Go-To-Market Layer + Week-25 Content Set

> For a fresh agent continuing Farrice Cain's LinkedIn content + client-acquisition build. Repo root: `/Users/farricecain/Google Antigravity`.

## Mission
Make Farrice a top-tier AI creative strategist on LinkedIn and **land his first paid client/role ASAP**. He has **18 years in human performance** (NASM CPT/CES/PES) — that lived-physiology expertise is the uncopyable wedge.

## Beachhead (locked)
**AI creative strategist for the wellness / fitness / supplement / performance BRAND world.** Hybrid win (a fractional/embedded **seat** OR independent **client** work — take whichever lands), **brands first**. NOT 1:1 coaching. Phase 2 = pro athletes/sports brands; Phase 3 = gaming/anime (personal voice-texture only for now).

## What's built — DO NOT REBUILD (read, then run)
Authoritative summary in memory: `~/.claude/projects/-Users-farricecain-Google-Antigravity/memory/project_linkedin-domination-os.md`. Approved plan: `~/.claude/plans/i-want-to-be-gentle-robin.md`.

**Engine (`.agent/workflows/`):**
- `farrice-engine.md` — master OS. Modes: `daily` · `acquire` (dual-track) · `offer "<who>"` · `weekly` · `repoint` · `radar` · `teardown "<brand>"` · `export`. One-command top-to-bottom.
- `linkedin-daily.md` — daily cook: **Creative Daily Brief** (players/themes/emotional-target/full-breakout/priming) → Farrice's raw dump → 3 variants → gates. Co-pilot; without his raw take it goes flat.

**Brain files (`_active/linkedin/`):** `CREATIVE-BOOK.md` (the ONE doc he opens daily) · `MASTER-STRATEGY.md` · `content-os.md` · `icp-emotional-map.md` (**the empathy moat** — "Dana" persona; broken promises, 2am replaceability fear, daily life, consumer-emotion; rule *reassure the human, indict the machine*) · `research/wellness-supplement-brand-niche.md` (22 named brands, 10 starred) · `offers/OFFER-LADDER.md` + `offers/teardown-system.md` (Teardown = keystone) · `voice-gate.md` · `pipeline.md` + `proof-tracker.md` (human-tagged, NEVER invent outcomes) · `daily/performance-log.md` (the ratchet) · `daily/brand-radar-2026-W25.md`.

**Depth/skills:** `skills/fresh-voice-system/genius.md` (Cognitive Signature: Paradox Reveal → False-Frame Demolition → Reframe Landing), `/aha-engine` + `kobi-brown-educational-virality`.

**Scripts (`execution/`):** `brand_radar.py` (Apify brand sweep), `export_to_drive.py` (markdown→Google Docs, idempotent, globs `daily/`), `apify_client.py`, `chain_runner.py`.

## Content already produced (ready to publish — paths under `_active/linkedin/99-archive/2026-08-07-dupe-trees/daily-pre-0623-snapshot/`)
- `2026-06-15-post-the-replaceable-fear.md` — enriched empathy post (gated PASS).
- `2026-06-15-brand-vertical-post.md` — the "sameness/divergence" post (Farrice rated **8/10, post as-is**).
- `2026-W25-content-set.md` — **the week's main content**: flagship article *"The Most Expensive Average in Wellness"* + 3 aha-engineered posts (Compliance / Fatigue / Consumer-Truth). All gated PASS (article breakthrough-leaning).
- `2026-06-15-parallax-industry-set.md` — 3 Parallax variations + brandjack menu.

## Quality bar (non-negotiable — every public piece)
Cognitive Signature + **Aha gate** (real before→after perception shift) + **Empathy gate** (says their truth better than they can; *reassure the human, indict the machine* — never make the ICP feel more replaceable). Voice gate bans: negate-reveal ("it's not X, it's Y"), twin-sentence aphorisms, "here's what" openers, cheap question closes, >2 em dashes, fabricated stats. **Gate every draft via `prose-doctor` + `fact-verifier` subagents.** Named brands must be primary-sourced (Brand Radar = the brands' own IG).

## State + quirks
- **The ratchet is DARK.** Farrice has not logged real metrics yet. The entire learning loop activates when he publishes + logs (impressions, **out-of-network %**, decision-maker profile views, DMs) in `performance-log.md`. Keep nudging — the #1 unlock.
- **Apify** works + is used (~$29/mo, self-governs, never hard-blocks). Brand Radar got real data on **6/10** brands; **Gorgie, Momentous, Hilma, Joovv** handles returned nothing — fix in `execution/brand_radar.py` (`BRANDS`).
- **Drive export** uses the `gws` CLI (auth ~7-day expiry). If it fails: `gws auth login -s drive,gmail,calendar,sheets,docs`. Folder: "Farrice LinkedIn Engine — Content & Strategy OS" (~20 Docs); links in `_active/linkedin/drive-export-manifest.json`.
- **`chain_runner.py finalize` logs 7.25 every time** — calibration discounts self-rated 9s. Accept with eyes open; do NOT loop cosmetic retries.
- **No `.claude/agents/` files** (Farrice's rule). In-session Agent-tool subagents (prose-doctor, fact-verifier, icp-deep-canvasser) are fine.

## Offer ladder
Teardown (free **Elite Magnet** + keystone proof) → **Angle Audit** $500–1.5K → **Proof Run** $1.5–3K (8 posts + VSL, 7 days) → **Embed** $4–9K/mo. Worked Gainful teardown in `offers/teardown-system.md`.

## Immediate next actions
1. **Farrice publishes** (the week's flagship article or the replaceable-fear post), runs the 10-comment plan, DMs the Gainful teardown. On him; agent supports + produces.
2. Metrics exist → log them → ratchet activates → `/farrice-engine weekly` tunes the lane mix.
3. Next content: `/farrice-engine daily` or `/farrice-engine teardown "<brand>"`.
4. Lead motion: `/farrice-engine acquire` (dual-track, teardown-DM opener → `pipeline.md`).
5. Fix the 4 broken Brand Radar handles.

## Suggested skills
- **`/farrice-engine`** (master front door) — start here.
- **`/linkedin-daily`** (Creative Daily Brief → raw dump → 3 variants).
- **`/aha-engine`** (flagship/long-form cognitive change).
- **`prose-doctor` + `fact-verifier`** (Agent subagents) — gate every draft.
- **`/farrice-engine teardown "<brand>"`** (keystone proof + lead asset).
- Read `project_linkedin-domination-os.md` first for full context.

## Notes
- No secrets appeared this session (nothing redacted). The Drive folder link is Farrice's own workspace.
- Conventions: durable work in `_active/linkedin/`; daily content in `daily/` (auto-exports to Drive). Match existing density + voice; client-facing docs ≤2 pages.
