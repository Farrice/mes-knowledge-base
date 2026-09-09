# Architecture + Artifact Contracts — Checkpoint 2
*2026-08-27 · lane: kallaway-sandcastles-forge · Vision approved at Checkpoint 1*

## Shape decision

ONE skill directory (house convention, mirrors `kallaway-content-operating-system`): `skills/<NAME>/` — SKILL.md + genius.md + workflows/ + references/prompts-v2/ + a `data_contract` section binding every data-consuming workflow to the outlier-radar signal pack (`.agent/outlier-radar/packs/<niche>/latest.json`) with three-tier degradation (fresh → cite receipts · stale → date-stamped claims + refresh command · absent → interview-only, zero fabricated metrics — his "unvalidated" label answered with our honest tiers).

Name (Farrice picks): **growth-blueprint-os** (recommended — skill and flagship report share the name) · content-strategy-os · angle-map-strategy.

State: `growth-lab/<niche-slug>/` per engagement (his folder-as-memory pattern, adopted) — but **dated, schema'd files with a staleness manifest** the orchestrator reads (his gap #4 closed). Client-visible.

## Table 1 — Per-artifact output contracts (the star)

Every artifact ships THREE forms: (a) working markdown in the state folder, (b) **client-grade branded HTML** via `render_brief.py --client` (Premium Minimal, 02-DESIGN-CONTRACT), (c) export path (PDF / Express). All claims carry VERIFIED/LIKELY/UNCONFIRMED labels. His artifact design language adopted where it's good: same-geometry-different-legend, 5-beat teaching panels, tap-a micro-instructions, export row on every artifact.

| # | Artifact (ours) | Elevated spec vs his | Surpass bar (falsifiable) |
|---|---|---|---|
| 1 | **Positioning Dossier** | His 7 sections + identity layer (belief/resistance/cost-of-admitting per McRaney) + pain bank pre-stocked with ≥10 real buyer verbatims w/ URLs (comments/reviews/forums via research.py) + each pain wired to the offer it feeds + viewer=buyer economics | Ours quotes ≥10 sourced buyers; his own doc calls itself "a hypothesis built from self-knowledge" |
| 2 | **Whitespace Map + Positioning Wheel** | His 7-attribute grid + our 8th attribute (belief positioning) + every score cites ≥2 specimen videos w/ URL/views/date from the radar pack + unclaimed-vs-graveyard verdicts on measured data + each whitespace entry ends in a decision-ready move | Click any score: ours opens receipts; his opens nothing without a $39/mo plan |
| 3 | **Bullseye + Revenue Overlay** | His 5-ring constraint-relaxation derivation (adopted verbatim — his best mechanic) + per-bucket offer wiring (funnel role, lead value, dollar-defined "working =") + chaos candidates pre-screened against whitespace + ring estimates anchored w/ real proxies | "Which bucket makes money, and how do you know by batch 3?" — ours answers in dollars; his tracker is blank |
| 4 | **Topic Scan (top-50 live)** | His ✓/✗ strikethrough pedagogy (adopted) on OUR ranked_videos: 50 real rows, outlier + velocity (2+ snapshots — beats his static score), per-bucket why-it-works mechanism, trend direction, conversion column mapping bucket→offer | 50 real receipted rows where his free tier rendered zero |
| 5 | **Format Matrix (live)** | His structure×visual split (adopted — real contribution) + per-format mechanism card (retention psychology + failure mode + transfer conditions) + cross-niche craft sourcing per his own two-zone rule + production recipe at user's real constraint level | "Why does this work and will it transfer?" — ours names the mechanism; his says "proven in-niche" with confounded stats |
| 6 | **Content Growth Blueprint** (flagship, no equivalent in his system) | Assembles 1-5 into ONE sellable client-grade report + executive verdict page + 90-day batch plan + refresh cadence. The demo artifact for the cash lane | A sellable document exists; his system has no sellable output at all |

## Table 2 — Workflow table (tiered)

**Tier 1 — Foundation (build now):**
| Workflow | Consumes | Emits |
|---|---|---|
| `/gl-interview` (niche interview, reflect-back mechanics adopted + identity-layer questions) | voice/text answers, FARRICE-MASTER-CONTEXT when self-run | positioning-dossier.md |
| `/gl-whitespace` (watchlist + 8-attribute grid + wheel) | dossier + radar pack + research.py receipts | whitespace-map.md + wheel HTML |
| `/gl-bullseye` (rings + 3-2-1 + revenue overlay) | dossier + whitespace | bullseye.md + 3 viz |
| `/gl-topic-scan` (live top-50 + buckets) | radar pack + bullseye | topic-buckets.md + top-50.md + viz |
| `/gl-format-find` (matrix + mechanism cards) | top-50 + pack + whitespace | format-playbook.md + matrix HTML |
| `/gl-blueprint` (flagship assembler) | all state files | Content Growth Blueprint (client HTML + PDF) |

**Tier 2 — Practitioner:** `/gl-refresh` (staleness manifest + radar refresh + drift report) · `/gl-orchestrate` (route-by-invoking, his orchestrator pattern + staleness detection).

**Tier 3 — Production loop (WAVE 2, spec banked):** our versions of his four UNDISTRIBUTED skills — engine-builder (hook/format engines w/ rinse-window strikethrough), topic-brainstormer (batch-bias marching orders), video-maker (substance sheet → 4-altitude pull → paired hooks → research-toggleable scripts), channel-coach (structured performance ledger, 24-hour maturity rule). §6.6–6.7 of the extraction report is the only public spec of these; ours would be the only buildable version outside his academy. Decision at this checkpoint: build in this lane after Tier 1, or park as the next mission.

**Stacking:** interview ← icp-deep-canvasser (McRaney) · whitespace ← competitive-intel + dunford positioning · artifacts ← Readout OS client template · voice layer at delivery ← VOICE-CARD · production loop (wave 2) ← kallaway-hook-mastery + addictive-storytelling + word-mastery (the existing roster becomes the substance layer his video-maker lacks).

**Prompts:** born-v2 per deliverable (6 Tier-1) in references/prompts-v2/, wired via renaissance_audit → prompt_library → wire_prompt_pointers.

## Factual hygiene (binding for all marketing/demo use)
Never repeat his growth claims as fact: "140K users" self-reported; "75K followers / $100K attributable" conflicts with the coach's own on-screen "12.6K" (UNCONFIRMED, logged in extraction report §7). Our surpass claims reference only what we can show side-by-side.

## Build order from here
1. (running) outlier_radar.py spine → verify
2. Skill scaffold + Tier 1 workflows + prompts-v2
3. `render_brief.py --client` + template-client.html + lint
4. Lead magnet template + baker
5. Flagship demo run on Farrice's niche (input pack) → surpass test vs baseline corpus
6. Registration + heartbeat + blind-pass record + homebase row
