---
name: "gb-enrich"
description: "Manual-fire data enrichment for a niche signal pack: plan slots with pack_enrich.py, run cheap receipted research (Tavily/research.py first, Perplexity recency for freshness), merge a validated enrichment block INTO the pack. One data spine — every artifact and the lead magnet inherit. Fired by Farrice or on request; never scheduled."
expert: "Growth Blueprint OS"
produces: "enrichment block merged into .agent/outlier-radar/packs/<slug>/latest.json (+ enrichment-draft.json, dated pack snapshot)"
---

# Growth Blueprint OS — Enrich (Manual-Fire Live-Market Layer)

Turns artifacts from educated guesses into data-enriched, value-insightful ones. The radar
measures what the niche's own videos DID; this workflow adds what the market is SAYING —
demand direction per topic, verbatim buyer language, and what changed in the last 30 days.
Design principle (binding): enrichment writes INTO the existing signal pack via
`execution/pack_enrich.py merge` — one data spine, no parallel enrichment path. Every
consumer (all gb-* artifacts AND the lead-magnet mini-report, which shows at most a 2-nugget
taste) inherits from the same `enrichment` block. Lead magnet = extension, not duplication.

**Fired manually by Farrice or on request — never scheduled.** Ahrefs MCP is unfunded; never
route to it.

## Pre-Flight Gate

1. Pack exists and is trusted? Read `.agent/outlier-radar/packs/<niche-slug>/latest.json` —
   ABSENT or `status != "ok"` → run/offer the radar refresh first (enriching a stale or
   missing spine decorates bad bones).
2. Emit the plan ($0, offline):

   ```bash
   .venv/bin/python3 execution/pack_enrich.py plan --niche <niche-slug>
   ```

3. **Cost transparency (BINDING — state BEFORE any paid call):** from the plan output, quote
   the total estimate in chat — per-slot lane + estimate (Tavily ≈ $0.00–0.01/search,
   Perplexity ≈ $0.005–0.02/call, both estimates) — plus the plan's `perplexity_ledger`
   line (month spend / remaining of $30). Typical full run: well under $0.25. If the ledger
   is in a pivot band (`directives/perplexity-usage-policy.md`), say so and downshift lanes.
4. Pack already has an `enrichment` block? Say its `generated_at` age; re-running replaces
   it (the pack is snapshotted first), which is the intended refresh path.

## Skill Acquisition

SKILL.md `data_contract` (hot if this session loaded it) + the enrichment schema in the
`pack_enrich.py` docstring / `execution/specs/outlier-radar-pack.schema.md` §Enrichment.
This is a research-and-merge run, not an expert deliverable — no genius.md load required.

## Execution

### Step 1 — Fill the slots (assistant layer does the research)

Work the plan's slots in order. Lane discipline per slot:

- **Topic demand/freshness (top 5 leaderboard topics)** — Tavily / `execution/research.py`
  first (cheap, receipted). Verdict per topic: `trend_direction` rising/flat/falling/unknown
  + a one-line `demand_note` + ≥1 source URL.
- **Buyer language** — Tavily / `research.py` against forums, comments, reviews. Collect
  **≥3 verbatim quotes**, each with context + URL. Quotes stay EXACTLY as written (ICP
  verbatim > pageantry) — no elevation, no paraphrase.
- **Market pulse (last 30d)** — Perplexity with a recency filter (freshness needs a
  recency-aware lane); Tavily acceptable when the ledger is tight. Only dated, sourced
  changes.

Label every entry honestly: VERIFIED (primary source seen) / LIKELY (credible secondary) /
UNCONFIRMED (single weak source — keep only if worth carrying). No URL = the entry does not
exist; `merge` will drop it anyway. "I don't know" beats a confident guess — an empty slot
is a valid outcome.

### Step 2 — Write the draft

Write the collected block to `.agent/outlier-radar/packs/<niche-slug>/enrichment-draft.json`
in the schema from the plan/docstring (`generated_at`, `lanes_used`, `cost_usd_est` with the
ACTUAL estimated spend of this run, `topics`, `buyer_language`, `market_pulse`).

### Step 3 — Merge into the spine

```bash
.venv/bin/python3 execution/pack_enrich.py merge --niche <niche-slug> \
    --in .agent/outlier-radar/packs/<niche-slug>/enrichment-draft.json
```

The merge validates structurally (drops sourceless/label-less entries with a visible count),
snapshots the pack to a dated sibling, writes the additive `enrichment` block, and prints a
one-line receipt. A REJECTED merge (0 valid entries) means the research didn't land — say so
plainly; never pad entries to force a merge.

## Output Contract

1. The merge receipt line in chat, plus the cost line: estimate stated up front vs. what was
   actually spent (per lane).
2. **Re-render pointer** — enrichment only pays when consumers re-read the pack. Name which
   artifacts should re-render for this engagement: any existing `gb-whitespace` /
   `gb-topic-scan` / `gb-blueprint` outputs for the slug (their data is now behind the pack),
   and the lead magnet (`execution/build_lead_magnet.py` — picks up the 2-nugget taste
   automatically on next bake). Flag, never auto-rerun without an ask.
3. Draft (`enrichment-draft.json`) and dated pack snapshot left on disk as the receipts.

## Quality Gate

- **No entry without a URL; labels honest.** The merge enforces the floor structurally; the
  honesty of VERIFIED vs LIKELY is yours.
- **READER-PURITY:** `demand_note`, quotes-in-context, and `market_pulse` notes are
  reader-grade language — they flow verbatim into client artifacts. No operator jargon
  ("pack", "slot", "lane", system names) inside any entry text.
- Cost estimate stated BEFORE paid calls; actual-vs-estimate stated after.
- Buyer quotes verbatim, ≥3 or an honest note that fewer sourced quotes exist.
- One spine: everything merged via `pack_enrich.py merge` — never a side file that
  artifacts read directly, never edits to other pack fields.
