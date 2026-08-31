---
name: "Growth Blueprint OS"
description: "Premium content-strategy system: receipted positioning, whitespace mapping, revenue-wired bullseye, live top-50 topic scan, format mechanism matrix, and a sellable flagship Content Growth Blueprint — every claim receipted, every bucket wired to offer economics, every artifact durable and client-grade."
version: "1.0"
format: "flagship-skill"
workflows: 8
routing: core
---

# Growth Blueprint OS

## Domain

Content strategy for business owners and creators who monetize — positioning, audience architecture, topic selection, format selection, and the sellable strategy document that assembles them. Built to surpass Kallaway's free "Growth System" bundle on four falsifiable axes (receipts, identity depth, revenue wiring, durable artifacts); the extraction contracts live in `extractions/kallaway/ARCHITECTURE.md` and the surpass bars in `extractions/kallaway/anatomy-cards.md`. Premium depth is the floor: this skill produces (a) Farrice's own strategy runs, (b) paid client deliverables, and (c) a deliberately subtracted lead-magnet step-down. The step-down is a subtraction from premium, never a thinner original.

## Core Thesis

Strategy quality is an **evidence problem before it is a thinking problem** — but evidence alone is a scoreboard, not a strategy. This system runs both halves: a live, ungated data spine (outlier radar signal packs — no subscription, no vibes) supplies receipts for every competitive claim, and an identity-and-revenue layer his system never had supplies the *so-what*: who the buyer is at the belief/resistance level, and which content bucket feeds which offer in dollars. Where the data is missing, the system says so in labeled tiers — it never fabricates a metric to keep the artifact looking authoritative.

## Ownership Boundary

- `execution/outlier_radar.py` owns collection, normalization, and the versioned signal-pack contract.
- `kallaway-ai-content-engine` owns research judgment: metric class, cohort eligibility, signal hygiene, data maturity, and the human creative-ownership stop.
- **Growth Blueprint OS** owns downstream engagement state and sellable client artifacts: dossier, whitespace map, bullseye, topic scan, format playbook, and assembled blueprint.
- `kallaway-content-operating-system` routes end-to-end production. It may invoke this skill for a client strategy package, but it does not duplicate these artifacts.

The seam is `execution/specs/outlier-radar-pack.schema.md`. Public rows enter as `PUBLIC_PROXY`; cohort roles remain `UNCLASSIFIED` until the topic scan applies Kallaway's niche/scale rules. A polished client artifact never upgrades the truth class of its inputs.

The repeatable unit:

`Interview → Whitespace → Bullseye + Revenue Overlay → Topic Scan → Format Find → Blueprint → (Refresh loop)`

## Workflow Table

### Tier 1 — Foundation (the six deliverables)

| Workflow | Slash Command | Produces | Use When |
|---|---|---|---|
| `gb-interview` | `/gb-interview` | Positioning Dossier (identity-layer avatar + receipted pain bank) | Starting any engagement; no positioning dossier exists yet |
| `gb-whitespace` | `/gb-whitespace` | Whitespace Map + Positioning Wheel (8-attribute grid, every score receipted) | Positioning hypothesis exists and must be tested against the real niche |
| `gb-bullseye` | `/gb-bullseye` | Bullseye + Revenue Overlay (rings, 3-2-1 mix, dollar-defined calibration) | Audience must be mapped into aimable rings with offer economics attached |
| `gb-topic-scan` | `/gb-topic-scan` | Topic Buckets + live Top-50 (velocity, mechanisms, conversion column) | Bucket picks need validation against 50 real receipted rows |
| `gb-format-find` | `/gb-format-find` | Format Playbook + structure×visual Matrix (mechanism cards) | Topic buckets are chosen and the delivery vehicle must be picked |
| `gb-blueprint` | `/gb-blueprint` | Content Growth Blueprint — the sellable flagship report | All five state files exist; assemble the client-grade deliverable |

### Tier 2 — Practitioner loop

| Workflow | Slash Command | Produces | Use When |
|---|---|---|---|
| `gb-refresh` | `/gb-refresh` | Staleness + drift report, refresh order, refreshed pack | Any state file may be stale, or positioning changed and downstream must be checked |
| `gb-orchestrate` | `/gb-orchestrate` | Routing — reads the state folder, invokes the right workflow | User asks "what's next," arrives mid-engagement, or seems lost between steps |

Slash commands are declarative here — **registration (sync_registries, `.agent/workflows/` wrappers) is a later, separate step.** Until then, invoke by reading the workflow file directly.

### Recommended Chains

**Full engagement (client or self):**
`/gb-interview → /gb-whitespace → /gb-bullseye → /gb-topic-scan → /gb-format-find → /gb-blueprint`

**Returning engagement:** `/gb-orchestrate` (routes to the deepest incomplete step) · **Monthly:** `/gb-refresh` → re-run whatever it flags.

**Wave-2 production loop (spec banked, not in this tier):** engine-builder, topic-brainstormer, video-maker, channel-coach equivalents — §6.6–6.7 of `extractions/kallaway-growth-system/extraction-report.md` is the spec. The existing `kallaway-*` roster is the substance layer until then (see Stacking).

## Stacking Guide

Handoffs are options, never forced wiring. The proven composition:

| Layer | Stack With | When |
|---|---|---|
| Identity depth | `icp-deep-canvasser` (McRaney deep-canvass agent) | `gb-interview` Step 4 — upgrades the avatar from psychographics to belief/resistance/identity-cost mapping |
| Competitive intelligence | `competitive-intel` agent | `gb-whitespace` — pricing, positioning grids, and content-moat findings feed the 8-attribute grid |
| Client render | Readout OS (`execution/render_brief.py --client`, Premium Minimal) | Every artifact's client HTML form — see Output Contracts |
| Voice at delivery | `_active/farrice-brand/voice/VOICE-CARD.md` + dial mode | Any artifact shipping under Farrice's own name; layered at delivery, never during analysis |
| Wave-2 substance | `kallaway-hook-mastery` · `kallaway-addictive-storytelling` · `kallaway-word-mastery` · `kallaway-content-system` (production loop) | After `gb-format-find`: the existing roster is the hook/script/retention substance layer his video-maker never shipped |
| Generic research | `execution/research.py` (receipt-carrying) | `gb-interview` pain-mining; `gb-whitespace` watchlist discovery. Never answer research from training memory |

## data_contract

Every data-consuming workflow binds to the **outlier-radar signal pack**. This section is the single authority; workflows restate their own tier behavior inline.

**Pack path:** `.agent/outlier-radar/packs/<niche-slug>/latest.json` (dated siblings: `.agent/outlier-radar/packs/<niche-slug>/<YYYY-MM-DD>.json`). Producer: `execution/outlier_radar.py` (spec: `.scratch/kallaway-sandcastles-forge/spec-outlier-radar.md`). Refresh command — quote it exactly wherever staleness is reported:

```bash
python3 execution/outlier_radar.py refresh --niche <niche-slug>
```

**Freshness test** (checkable, no judgment calls):

- **FRESH** — pack exists, `status == "ok"`, and `now − generated_at ≤ freshness_ttl_hours`.
- **STALE** — pack exists but is older than `freshness_ttl_hours`, **or** `status == "degraded"` (partial fetch; the pack's `errors[]` says why).
- **ABSENT** — no pack file for the niche slug.

**Three-tier degradation (BINDING on every data-consuming step):**

| Tier | Behavior |
|---|---|
| **FRESH** | Cite receipts on every claim: specimen URL + views + outlier multiple + published date, straight from `ranked_videos`. Claims earn VERIFIED. |
| **STALE** | Claims ship date-stamped — *"as of `<generated_at>`"* — labeled LIKELY at best, and the artifact carries the exact refresh command above plus the pack's age in days. Never present stale numbers as current. |
| **ABSENT** | **Interview-only mode. ZERO fabricated metrics.** Every would-be data claim becomes UNCONFIRMED or a `[NEED]` slot naming the missing number. The artifact carries a top-of-document banner: *"INTERVIEW-ONLY — no performance data behind this run"* — the honest answer to the fallback his own bundle labels "unvalidated by performance data." An authoritative-looking artifact on vibes is the failure mode this tier exists to kill. |

**Minimum pack fields per workflow** (fields from the pack contract; a pack missing a workflow's minimum degrades that workflow one tier and says so):

| Workflow | Minimum fields consumed |
|---|---|
| `gb-interview` | None (pack optional). Pain-mining runs on `execution/research.py`, not the pack. |
| `gb-whitespace` | `channels[]` (handle, title, subscriber_count); `ranked_videos[]` (url, title, views, outlier_multiplier, published_at, channel_handle); `leaderboard.topics` + `leaderboard.formats` |
| `gb-bullseye` | `channels[]` (per-ring competition counts); `ranked_videos[]` (ring anchor proxies: views, outlier_multiplier, topic) |
| `gb-topic-scan` | Full outlier records: url, title, channel_handle, views, views_per_day, outlier_multiplier, outlier_score, published_at, confidence, `velocity_vpd_7d` (null until 2+ snapshots — say so), hook_text, topic, evidence_class, cohort_role, engagement_rate, signal_hygiene, rejection_reasons; pack-level data_maturity_state; `leaderboard`; `run_receipt_path`; `coverage` |
| `gb-format-find` | `ranked_videos[]` incl. hook_text, format_hint, transcript_path (null OK); `leaderboard.formats` |
| `gb-blueprint` | Freshness metadata only (`generated_at`, `status`, `coverage`) — it audits, it does not re-fetch |

**Coverage honesty:** the pack declares `coverage` per platform (`measured` / `partial` / `none`). TikTok/IG are `"none"` in the current build — every artifact that generalizes across platforms states this scope limit in its blind-spot section. `source_lanes` travels with every record; a future `sandcastles_bridge.py` or `manual_csv` lane drops in behind the same contract without touching this skill.

**Enrichment (optional):** the pack may carry an additive `enrichment` block — sourced topic demand/freshness, verbatim buyer language, 30-day market pulse (schema: `execution/specs/outlier-radar-pack.schema.md` §Enrichment) — produced manual-fire by `/gb-enrich` (`workflows/gb-enrich.md` + `execution/pack_enrich.py`); consumers cite it with its labels when present and degrade silently when absent.

## State Folder — `growth-lab/<niche-slug>/`

One folder per engagement — the client-visible memory (folder-as-memory adopted from Kallaway; schema, versioning, and staleness enforcement are ours — his gap #4 closed). Chats are ephemeral; the folder is the record.

```
growth-lab/<niche-slug>/
├── manifest.json                 # staleness ledger — THE machine-readable state (schema below)
├── positioning-dossier.md        # LIVING — gb-interview
├── whitespace-map.md             # LIVING — gb-whitespace
├── bullseye.md                   # LIVING — gb-bullseye
├── topic-buckets.md              # LIVING — gb-topic-scan
├── top-50.md                     # LIVING — gb-topic-scan (the shared data core downstream reads)
├── format-playbook.md            # LIVING — gb-format-find
├── growth-blueprint.md           # LIVING — gb-blueprint (flagship)
├── exports/                      # client HTML + PDF per artifact (see Output Contracts)
│   └── <artifact>-client.html, <artifact>.pdf, wheel/matrix/bullseye HTML
├── history/                      # RECORDs — dated snapshots written on every re-run
│   └── YYYY-MM-DD-<artifact>.md
└── ledger/
    └── performance-ledger.jsonl  # structured per-batch numbers (Wave-2 consumer; schema reserved now)
```

LIVING vs RECORD (house-binding, honored here): undated files at the root are the truth, updated in place; every re-run first copies the outgoing version to `history/YYYY-MM-DD-<name>.md`, then updates the living file and its `manifest.json` entry.

**`manifest.json` schema** (written by every workflow on completion; read by `gb-refresh` and `gb-orchestrate`):

```json
{
  "niche_slug": "…",
  "engagement": { "client": "…", "mode": "self | client | lead-magnet", "offer_map": "one line: what is sold, at what price" },
  "artifacts": {
    "positioning-dossier": {
      "file": "positioning-dossier.md",
      "workflow": "gb-interview",
      "produced_at": "ISO-8601",
      "data_tier": "fresh | stale | absent",
      "pack_ref": { "path": ".agent/outlier-radar/packs/<slug>/<date>.json", "generated_at": "ISO-8601" },
      "ttl_days": 90,
      "depends_on": [],
      "status": "fresh | stale | drifted"
    },
    "whitespace-map":   { "ttl_days": 90,  "depends_on": ["positioning-dossier"] },
    "bullseye":         { "ttl_days": 90,  "depends_on": ["positioning-dossier", "whitespace-map"] },
    "topic-buckets":    { "ttl_days": 45,  "depends_on": ["bullseye"] },
    "top-50":           { "ttl_days": 45,  "depends_on": ["bullseye"] },
    "format-playbook":  { "ttl_days": 60,  "depends_on": ["top-50", "whitespace-map"] },
    "growth-blueprint": { "ttl_days": 45,  "depends_on": ["positioning-dossier", "whitespace-map", "bullseye", "topic-buckets", "top-50", "format-playbook"] }
  },
  "refresh_order": ["positioning-dossier", "whitespace-map", "bullseye", "topic-buckets", "top-50", "format-playbook", "growth-blueprint"]
}
```

`status: "drifted"` means an upstream dependency was re-run after this artifact was produced — content rot his write-once folders could never detect. `gb-refresh` computes it; `gb-orchestrate` surfaces it in one line and routes. Nothing blocks: staleness is a flag and a quoted command, never a gate (Compass Doctrine).

## Output Contracts (all Tier-1 artifacts)

Every deliverable ships **three forms**:

1. **State markdown** — the living file in `growth-lab/<niche-slug>/` (schema per workflow).
2. **Client-grade branded HTML** — `python3 execution/render_brief.py <brief.json> --client` → `exports/<artifact>-client.html` (flag + `templates/research-brief/template-client.html` shipped in this lane). Premium Minimal governs the outward form (`_active/farrice-brand/premium-minimal/package/02-DESIGN-CONTRACT.md`); interaction canon: `references/artifact-design-language.md`. A client page never carries paths, costs, or write buttons.
3. **Export path** — PDF (and Express where asked) from the client HTML; every artifact carries an export row.

Every claim in every form carries a **VERIFIED / LIKELY / UNCONFIRMED** label. Delivery in Farrice's own voice layers VOICE-CARD last.

**READER-PURITY RULE (Farrice 2026-08-27 — BINDING on every client/product-facing form):** the document serves the reader only. Zero operator or inside language: no repo paths, no commands (refresh or otherwise), no tier jargon ("data_tier: absent", "pack", "niche slug", `[NEED]` markers), no system names (outlier radar, growth-lab, manifest), no workflow references. The claim labels stay — they serve the reader — but tier states translate to reader language: FRESH → "evidence current as of <date>"; STALE → "performance data as of <date>; refresh scheduled"; ABSENT → "built from founder interview; performance validation in progress." Everything operator-side — refresh commands, tier ledger, pack refs, production notes — goes to `growth-lab/<niche-slug>/operator/<artifact>-notes.md`, generated alongside every artifact, never inside it. `client_package_lint.py` runs on every client render; a lint hit is a fix, not a footnote.

## Quality Bar

The nine-criterion rubric lives in `genius.md` (§Quality Rubric) — any single 1/5 fails the artifact regardless of total. Load it before producing; every workflow's Quality Gate references it. Prose ships only after `python3 execution/prose_classifier.py check <file>` (ban-bank floor).

## Execution Prompts (structure-pure v2)

Six born-v2 prompts, one per Tier-1 deliverable, in `references/prompts-v2/`. When a deliverable matches one, Read it and honor its Output Contract instead of improvising the shape:

- Positioning Dossier — `references/prompts-v2/positioning-dossier.md`
- Whitespace Map + Positioning Wheel — `references/prompts-v2/whitespace-map.md`
- Bullseye + Revenue Overlay — `references/prompts-v2/bullseye-revenue-overlay.md`
- Topic Scan + Top-50 — `references/prompts-v2/topic-scan-top-50.md`
- Format Playbook + Matrix — `references/prompts-v2/format-playbook-matrix.md`
- Content Growth Blueprint — `references/prompts-v2/content-growth-blueprint.md`

## Source Evidence

- Binding spec: `extractions/kallaway/ARCHITECTURE.md` (artifact contracts + workflow tiers + stacking)
- Per-artifact teardown: `extractions/kallaway/anatomy-cards.md` (7 adopted patterns, 4 gaps closed)
- Deep extraction: `extractions/kallaway-growth-system/extraction-report.md` (P1–P21, SM1–SM10, rubric §5, artifact ledger §6)
- Source skills (pattern fidelity, not redistribution): `extractions/kallaway/source-skills/strategy-bundle/unpacked/*/`
- Data spine contract: `execution/specs/outlier-radar-pack.schema.md`
- Reconciliation and frozen proof: `extractions/kallaway/validation/`

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

6 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Bullseye + Revenue Overlay — [niche-slug]** — `skills/growth-blueprint-os/references/prompts-v2/bullseye-revenue-overlay.md`
- **Content Growth Blueprint — [operator/client] · [niche-slug]** — `skills/growth-blueprint-os/references/prompts-v2/content-growth-blueprint.md`
- **Format Playbook — [niche-slug]** — `skills/growth-blueprint-os/references/prompts-v2/format-playbook-matrix.md`
- **Positioning Dossier — [OPERATOR/CLIENT] · [niche-slug]** — `skills/growth-blueprint-os/references/prompts-v2/positioning-dossier.md`
- **Topic Buckets — [niche-slug]** — `skills/growth-blueprint-os/references/prompts-v2/topic-scan-top-50.md`
- **Whitespace Map — [niche-slug]** — `skills/growth-blueprint-os/references/prompts-v2/whitespace-map.md`

<!-- END:execution-prompts -->
