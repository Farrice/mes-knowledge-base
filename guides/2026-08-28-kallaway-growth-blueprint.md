---
date: 2026-08-28
session: kallaway-growth-blueprint
tier: operator-guide
status: enriched
---

# Growth Blueprint OS — What We Built 2026-08-27/28 and How to Use It

> Two-day forge: extracted Kallaway's "0→100K with Claude" system (his 6 free skill files + both videos + Sandcastles MCP docs), ran his skills verbatim as a falsifiable baseline, built the surpass suite, and had Farrice judge it side-by-side — **5/7 OURS CLEARLY WINS (EVAL-064)**, 2 losers rebuilt to his notes same-day. Companions: `growth-lab/DEPLOY-CARD.md` (commands) · `growth-lab/LEVERAGE-MAP.md` (money uses) · `extractions/kallaway/E2E-REPORT-2026-08-27.md` (receipts) · handoff `.agent/handoffs/2026-08-28-kallaway-growth-blueprint.md`.

## ⚡ If you only read 10 lines

1. `/growth-blueprint` = front door; `/gb-interview → /gb-whitespace → /gb-bullseye → /gb-topic-scan → /gb-format-find → /growth-blueprint` = a full client engagement; `/gb-orchestrate` routes mid-stream.
2. Data first, $0, keyless: `python3 execution/outlier_radar.py add-channels --niche <slug> @h1 @h2` then `refresh --niche <slug>` → pack at `.agent/outlier-radar/packs/<slug>/latest.json`.
3. Any niche → full branded 31-file client package: run the chain, then `python3 execution/export_growth_package.py package --niche <slug>`.
4. Lead magnet (step-down, per niche): `python3 execution/build_lead_magnet.py --pack <pack> --niche-label "<Label>" --cta-url <url> --out <html>`.
5. Enrichment is MANUAL-FIRE only: `/gb-enrich` (shows cost before spending; sourceless entries structurally rejected).
6. Intake pipeline exists end-to-end; it goes live when Farrice does the 15-min Google Form (`growth-lab/intake/google-form-kit.md` → `faces-config.json` → `python3 execution/build_intake_faces.py`).
7. Doctrine line: **reader-purity is binding** — client artifacts carry zero operator language; every claim labeled; ABSENT data = interview-only, never fabricate.
8. The Register Contract (genius.md, Farrice verbatim) + Q10 insight floor gate every artifact: coach-to-reader + strategist authority, every word earns its mark, every clickable ends insight+action+positioning.
9. NO Sandcastles sub, NO Acrobat Studio, Ahrefs API unfunded, Apify dead — TikTok/IG = ask the client for their own analytics exports (decision card: `growth-lab/DECISION-CARD-tiktok-ig-data.md`).
10. First thing to run next session: the lane merge if still parked — `python3 execution/worktree_lane.py merge --lane worktree-kallaway-sandcastles-forge`.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/growth-blueprint` | Loads the skill + flagship assembler | Any strategy ask; assembling the sellable Blueprint |
| `/gb-interview` | Positioning Dossier (identity avatar + receipted pain bank) | New engagement, no dossier |
| `/gb-whitespace` | Whitespace Map + Positioning Wheel | Positioning hypothesis needs testing vs the real niche |
| `/gb-bullseye` | Bullseye + Revenue Overlay + Ring Intelligence sourcing map | Audience → rings with offer economics |
| `/gb-topic-scan` | Topic buckets + live receipted Top-50 | Bucket picks need data validation |
| `/gb-format-find` | Format Playbook + structure×visual matrix w/ mechanism cards | Picking the delivery vehicle |
| `/gb-enrich` | Receipted market data merged INTO the pack (pennies, quoted first) | Artifacts should carry live demand/pulse/buyer language |
| `/gb-refresh` | Staleness + drift report, refresh order | Monthly, or after positioning changes |
| `/gb-intake` | Intake submission → engagement + free mini + Gmail DRAFT | A form submission lands |
| `outlier_radar.py refresh/add-channels/pack/status/emit-radar-rows` | The $0 data spine | Before any data-consuming workflow |
| `intake_bridge.py status/pull` | Pending submissions · frozen-shape intake-pack | Checking/working pipeline |
| `export_growth_package.py pdf/package` | Print-grade PDF · full client zip | Delivery |

## The mental model

1. **One data spine, everything inherits.** The signal pack is the interface: radar writes it, enrichment merges into it, every artifact and the lead magnet read it. New data sources (Sandcastles MCP, client-owned metrics, manual CSV) drop in behind the same contract — skills never change.
2. **Three forms per artifact, one register.** Working md (operator-side, state folder) → client HTML (reader-pure, Premium Minimal) → PDF/package. The reader never sees machinery; the operator notes carry it separately.
3. **Honesty is the product.** Tiers (fresh/stale/absent) never fabricate; the honest ceiling ("unvalidated against YOUR buyer") is the upsell. He degrades free output to sell credits; we degrade free output to sell judgment.
4. **His patterns, our depth.** Kallaway's genuinely good mechanics are adopted with attribution (rings by constraint-relaxation, 3-2-1 + chaos reserve, two-zone sourcing, menu-not-verdict, 5-beat teaching panels, folder-as-memory); the surpass axes are receipts, identity depth, revenue wiring, durable branded artifacts.

## Capabilities shipped

### The outlier radar (`execution/outlier_radar.py`)
**What:** keyless yt-dlp two-stage fetch (flat channel dump → enrich flagged outliers + captions), vpd/channel-median scoring, SQLite snapshots → measured velocity after 2+ runs (beats Sandcastles' static score). **When:** before any data-consuming run; 12 channels/run cap, 12h TTL. **When NOT:** TikTok/IG (coverage honestly `none` — owned-metrics lane or decision card instead). **Worked example:** farrice-parallax — 12 verified channels, 338 videos, 50 ranked rows, 10 transcripts, $0. **Honest edges:** velocity needs runs ≥1 day apart (flagship's two ran 64 min apart — one refresh fixes); yt-dlp breaks periodically (degrades loud, `pip install -U yt-dlp`); no auto-refresh scheduled (staged UNARMED, needs Farrice's yes).

### The skill suite (`skills/growth-blueprint-os/`)
**What:** 9 workflows + 6 born-v2 prompts + genius.md carrying the BINDING contracts (Register Contract verbatim, Q10 insight floor, Ring Intelligence six-field contract, reader-purity, adopted-pattern attributions). **When:** any content-strategy, positioning, or niche-intelligence work — self, client, or lead-magnet mode (each workflow has all three adaptations). **When NOT:** production-loop work (scripting/video) — that's Wave 2, PARKED, spec at extraction report §6.6-6.7; the existing kallaway-* roster is the substance layer meanwhile. **Honest edges:** revenue-overlay lead values are modeled until his first 10 sends (recalibration checklist in operator notes); voice-card dial pass deferred to public shipping.

### The delivery pipeline (`render_brief.py --client` · `template-client.html` · `export_growth_package.py`)
**What:** brief JSON → reader-pure Premium Minimal client HTML → headless-Chrome PDF → assembled package (client-clean CONTENTS + reading order; OPERATOR-NOTES kept outside the zip). **When:** every deliverable. **When NOT:** internal briefs (Readout OS internal dialect stays). **Honest edges:** wheel PDF paginates the SVG to page 2 (renders fully); interactives are the premium form — PDFs flatten them (CONTENTS says so per file).

### The lead magnet + intake funnel (`build_lead_magnet.py` · `templates/intake/` · `intake_bridge.py` · `build_intake_faces.py`)
**What:** per-niche baked mini-report (offline, zero network, honest-ceiling CTA, ≤2 enrichment nuggets, `--exclude` for off-avatar rows) + 6 landing faces + 9-question form kit + deterministic submission bridge producing frozen-shape intake-packs + `/gb-intake` manual fire with 48h promise. **When:** lead gen and pipeline. **When NOT live yet:** until Farrice's Google Form (15 min) and Stripe link (10 min) — `growth-lab/intake/operator/FARRICE-WHEN-BACK.md`. **Honest edges:** sheet-read mode specified but proven only against fixture CSV; first real submission is the proving run.

### The enrichment function (`pack_enrich.py` + `/gb-enrich`)
**What:** plan (slots + cost estimate, $0) → assistant-layer research (Tavily/research.py/Perplexity) → merge with structural anti-fabrication (no URL + label = dropped, visibly). **When:** Farrice fires it — never scheduled. **Worked example:** farrice-parallax run cost ~$0.11 vs $0.03-0.08 estimate, merged 5 topic trends + 4 buyer quotes + 5 pulse notes. **Honest edges:** Perplexity ledger governs (~$18.8/mo headroom at close).

## Composition (options, never forced)

| Stack | When it earns its cost |
|---|---|
| icp-deep-canvasser → gb-interview | Client engagements where identity-level depth sells the dossier |
| competitive-intel → gb-whitespace | Paid competitive-intel add-on |
| kallaway-* roster (hooks/storytelling/word) → after gb-format-find | Bridging into production until Wave 2 exists |
| VOICE-CARD layer | Anything shipping under Farrice's name — at delivery, never during analysis |

## Honest session lessons (why the contracts exist)
Two full rejections mid-mission: (1) operator language leaked into client artifacts → reader-purity rule (binding memory); (2) "receipts became the content" — artifacts narrated research at the reader → Register Contract + Q10 + the founder-persona cold-read gate (which then caught a 15-vs-13 receipt count and a fact error mechanical checks missed). The permanent fix was never patching content — it was rewriting the contract that produced it, then regenerating fresh.
