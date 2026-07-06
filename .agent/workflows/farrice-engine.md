---
description: Farrice's master content + creative-strategy + client-acquisition OS — composes the daily Parallax cook, the brandjack engine, and the lead-gen motion, pointed at the beachhead
---

# /farrice-engine — Master Content & Creative-Strategy OS

The single front door. Composes Farrice's best assets — the Parallax voice, the daily content cook, the brandjack/newsjack engine, the expert roster, and the client-acquisition motion — into one content→authority→client machine, in his voice, pointed at the beachhead in `_active/linkedin-launch/01-research/MASTER-STRATEGY.md`.

This does NOT reinvent anything. It orchestrates what already exists.

Universal front door: `/create` composes this engine for personal-brand work.

## Usage

```
/farrice-engine                # default: daily mode (content + commenting + pipeline nudge)
/farrice-engine daily          # run the daily content cook + distribution + lead motion
/farrice-engine acquire        # focus the lead-gen motion: signal scan → DM targets → discovery prep
/farrice-engine offer "<who>"  # shape/pitch the offer for a specific warm lead
/farrice-engine weekly         # review ratchet + pipeline, set next week's lane mix + KPI read
/farrice-engine repoint        # change the beachhead/niche; updates MASTER-STRATEGY, re-aligns lanes
/farrice-engine export         # push all assets to the Google Drive folder as Docs (portable)
/farrice-engine radar          # refresh named-brand intelligence (Apify sweep of the Top-10)
/farrice-engine teardown "<brand>"   # build a named-brand teardown (proof post + Elite Magnet DM + audit on-ramp)
```

## Step 0 — Load the brain (every run)

Read `_active/linkedin-launch/01-research/MASTER-STRATEGY.md` (beachhead, lane sequence, ICP, offer, pipeline, KPIs) + `01-research/wellness-supplement-brand-niche.md` (the brand buyer + target list). Everything below serves that. If beachhead is empty/stale → run `repoint` first.

## Step 0.5 — Load the depth + empathy layer (every content/offer run — this is the apex bar)

Load before any public artifact: `_active/linkedin-launch/00-start-here/CREATIVE-BOOK.md` (the operating frame), `_active/linkedin-launch/01-research/icp-emotional-map.md` (**the empathy moat** — broken promises, the 2am replaceability fear, daily life; *reassure the human, indict the machine*), the latest `daily/brand-radar-*.md` (named specifics), `skills/fresh-voice-system/genius.md` (the **Cognitive Signature**), `aha-engine` + `kobi-brown` (cognitive-change). The bar: every piece creates a real perception shift, makes the ICP feel **seen better than their own team gets them**, leaves them better off. "Polished but flat" fails; "informs but doesn't make them feel seen" fails.

## Mode: `daily` (content + distribution + lead motion)

1. **Cook** — run `.agent/workflows/linkedin-daily.md` (v2): Apify-first research → brandjack menu + raw-take priming → HALT for Farrice's take → 3 cooked variants (Cognitive Signature) → voice gate + Aha gate + fact-verify. Lane = current beachhead (brand vertical). This is the content layer; do not duplicate it here.
2. **Finalize + self-improve** — `chain_runner.py finalize` the shipped variant(s); then `evolution_orchestrator.py` flags any underperforming format/lane (log-only if no traces). Harness-tuning only, never auto-rewrites content.
3. **Distribute** — 10 commenting targets per `_active/linkedin-launch/05-lead-gen/commenting-engine.md` (5 brand founders / marketing-content leads / category voices + 5 peers), each comment a micro-demo of the wedge (practitioner depth, not "great post") — in the rooms where brands hire.
4. **Lead motion** — scan `performance-log.md` + recent engagement for **decision-maker** signal (profile views, saves, substantive comments from brand founders/marketing leads). Surface 1-3 warm names + a soft, non-pitch DM opener (a real idea for their brand). Never mass-DM.
5. **Export (portability)** — `python3 execution/export_to_drive.py` syncs the updated strategy/content assets to the Google Drive folder as Docs (idempotent — updates in place, stable links). If gws auth is expired it fails loud with the re-auth command; not a blocker for the rest of the run.

## Mode: `acquire` (focus the dual pipeline — hybrid win condition)

Two tracks run in parallel (take whichever lands first):
- **ROLE / SEAT track** — target brand founders, marketing/brand directors, heads of content/social, and the agencies they use (from `01-research/wellness-supplement-brand-niche.md`). Content = portfolio/audition. The ask is a fractional/embedded/FTE creative-strategist seat. Use Apify/`research.py` to pull the brand's current content + pain, then a value-first DM that reads like a strategist already on their team.
- **CLIENT track** — same decision-makers; the ask is a project/retainer. Compose `skills/linkedin-cs-outreach/` or `skills/client-acquire/` (outreach + qualification) + `_active/linkedin-launch/02-offer/` + `skills/proof-copy-engine/` + `skills/authority-flywheel/`.

**The opener for both tracks = the Teardown** (`teardown "<brand>"`): a custom teardown DM'd to the lead is the warmest, most-proof-dense first touch there is (the research's "override signal"). Output per warm lead: track (role/client), stage (cold/warm/hot), the next single action, the asset to send (teardown → Angle Audit → Proof Run → Embed, per `02-offer/OFFER-LADDER.md`). Log lead stage to `_active/linkedin-launch/05-lead-gen/pipeline.md` and real outcomes to `_active/linkedin-launch/05-lead-gen/proof-tracker.md` (both **human-tagged only — never invent results**); register revenue via `execution/revenue_tracker.py`.

## Mode: `offer "<who>"`

For a specific warm lead (brand or expert), shape the engagement to their exact situation:
1. **Intel** — Apify/`research.py` on their brand: current content, the sameness/pain, who owns it.
2. **Value-based positioning (Chris Do)** — reuse `_active/farrice-brand/offers/offer_market_fit_blueprint.md`: price the transformation (un-averageable brand, methodology install), not the deliverable.
3. **Design panel** — `/convene` to co-design the offer + objection pre-emption (pulls the roster: positioning, persuasion, proof) → `/writers-room` to compress the deliberation into the final pitch.
4. **Output** — a tailored one-paragraph pitch (their language), the discovery-call frame, and the entry offer (project/retainer for the client track, or the fractional framing for the role track). Voice-gate + Aha-gate it (it represents Farrice).

## Mode: `weekly`

1. **KPI read** — `execution/revenue_tracker.py report` + 7 days of `performance-log.md`, priority order: decision-maker profile views → decision-maker DMs/connection requests → discovery calls / role conversations → signed engagement/seat. Reach last.
2. **Self-improving lane mix** — `evolution_orchestrator.py` over the week's traces: which pillar/cook-method/lane over-performed for *acquisition* (not reach). Route winners into next week. Absent traces → log-only.
3. **Consistency (Godin)** — run a `skills/seth-godin-brand/` consistency + remarkability check: did the week honor the lane commitment + Carry-Forward Directives; is anything drifting toward "better-not-louder" violations or false proxies (chasing likes)?
4. Set next week's lane mix + barbell (≥1 LOW reach + ≥1 HIGH true-fan); update Carry-Forward Directives.
5. Flag pipeline gaps (lots of authority, no DMs = distribution problem; DMs, no calls = offer/CTA problem).
6. **Export** — `python3 execution/export_to_drive.py` to sync the week's updated assets to the Drive folder.

## Mode: `repoint`

Change the beachhead. Ask Farrice: which lane leads, what proof he has, where his network is. Update `MASTER-STRATEGY.md` (beachhead + phase sequence + ICP + offer), re-align `content-os.md` lanes, note the change. Everything downstream re-points automatically next run.

## Mode: `export` (make the assets portable)

Run `python3 execution/export_to_drive.py` — pushes the strategy + content + research + workflow assets to the Google Drive folder **"Farrice LinkedIn Engine — Content & Strategy OS"** as Google Docs (markdown → Doc), so the content is usable anywhere. Deterministic + idempotent: find-or-creates the folder, **updates existing Docs in place (stable links)**, creates new ones. Links are written to `_active/linkedin-launch/90-exports/drive-export-manifest.json`. To add a new deliverable to the export set, append `(path, "Doc Name")` to `ASSETS` in the script. `--dry-run` previews; `--folder "<name>"` overrides. On gws auth expiry (the known 7-day quirk) it prints `gws auth login -s drive,gmail,calendar,sheets,docs` and exits non-zero — never silent.

## Mode: `radar` (refresh named-brand intelligence)

Run `python3 execution/brand_radar.py` — an Apify sweep of the Top-10 target brands → `daily/brand-radar-YYYY-WW.md` (real recent posts, formats, engagement). Deterministic, ~$1/mo, fallback contract (never blocks). The daily Creative Brief + the teardown both read the latest radar. Run weekly (or when a radar is stale). Fix any brand handle that returns no data in `execution/brand_radar.py`.

## Mode: `teardown "<brand>"` (the keystone proof asset)

Build a named-brand content teardown per `_active/linkedin-launch/02-offer/teardown-system.md`: read the brand's data from the latest `daily/brand-radar-*.md` (run `radar` first if stale) + `icp-emotional-map.md` §7 (the body-level consumer truth) + the divergence lens. Produce the 6-part teardown (credit → sameness tell → body-level truth → 3 angles I'd ship → compliance note → close). Voice + Empathy gate it. Triple-route the output: (1) a constructive **public proof post**, (2) the full **Elite Magnet DM** to the brand's founder/growth lead, (3) the **Angle Audit on-ramp**. Log the target + outcome in `pipeline.md`. **≥1/week** — it's the highest-leverage proof + lead act.

## Layer map (kill the redundancy)

- **`fresh-voice-system`** = the **voice + cognitive-signature layer** + planned **multi-week narrative arcs** (5-7 chapter serial content). Owned by `weekly`/long-form. Load its `genius.md` as the depth source everywhere.
- **`linkedin-daily`** = the **daily reactive cook** (brandjack + raw-take → 3 variants). The daily executor.
- **`farrice-engine`** = the **conductor** — loads the depth layer, routes between the two, runs acquire/offer/weekly. Glue, not a reimplementation.

## Standing principles

- **Depth standard** — every public artifact runs the Cognitive Signature (Paradox Reveal → False-Frame Demolition → Reframe Landing) and passes the **Aha gate** (real perception shift, left-better-off, addictive-in-a-good-way). Information-only = fail.
- **Voice first** — every public artifact passes `_active/linkedin-launch/04-content-os/voice-gate.md`. Polished-but-flat = fail (see `linkedin-daily` Step 8).
- **The content is the demo** — never ship a post that doesn't prove the service (AI + human depth).
- **Acquisition > applause** — optimize for decision-maker profile views/DMs/calls/seats, never likes.
- **Apify-first research, deterministic fallback** — raw data via `execution/apify_client.py` (budgeted, never blocks); degrade to `research.py`/Perplexity/Tavily; always report which was used.
- **Compose, don't rebuild** — point at existing skills/workflows; this file is glue.

## Finalize
Run the relevant sub-workflow's finalize (e.g., `linkedin-daily` Step 10). For `acquire`/`offer`/`weekly`, log via `chain_runner.py finalize ... --type Strategy --workflow farrice-engine`.
