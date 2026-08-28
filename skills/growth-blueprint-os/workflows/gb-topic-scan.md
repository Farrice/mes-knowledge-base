---
name: "gb-topic-scan"
description: "Live top-50 scan from the signal pack: ✓/✗ strikethrough pedagogy on real receipted rows, velocity + trend direction per bucket, per-bucket why-it-works mechanism, and a conversion column mapping every bucket to the offer it feeds."
expert: "Growth Blueprint OS"
produces: "growth-lab/<niche-slug>/topic-buckets.md + top-50.md + exports/topic-scan.html"
---

# Growth Blueprint OS — Topic Scan (Top-50 Live)

## Pre-Flight Gate

- **Read state:** `bullseye.md` (buckets + revenue overlay — the scan validates the trio and prices the pool) and `positioning-dossier.md` (avatar + filter questions). Bullseye missing → the scan still runs, but bucket overlay and conversion column degrade to "unassigned" — say so, and route to `gb-bullseye` after.
- **Pack state (this workflow's spine):** `.agent/outlier-radar/packs/<niche-slug>/latest.json` — FRESH / STALE / ABSENT per SKILL.md `data_contract`. This is the heaviest pack consumer in the system; the tier governs everything below.
- **Refresh offer, not gate:** STALE or ABSENT → quote `python3 execution/outlier_radar.py refresh --niche <slug>` (cost: $0, keyless), offer to run it now, proceed per tier on decline. Never block.

## Skill Acquisition

Load `genius.md` (§1.1 receipts, §1.3 revenue wiring, §2.4 menu-not-verdict; carried moves: name-the-trap, unclaimed-vs-graveyard, blind-spot declaration). Load `references/artifact-design-language.md` for the strikethrough + crowned-bar treatments.

## Execution

### Stage 1 — Build the working set (✓/✗ with visible verdicts)

Take `ranked_videos` (outlier-score-sorted, cap 50; the pack normalizes for channel size — `outlier_multiplier = N× that channel's normal`, define it inline in the artifact so no reader has to look it up). Screen every row with a **visible verdict, never a silent drop**: ✓ qualifies for the avatar / ✗ excluded, with a two-or-three-word reason on every ✗ ("wrong avatar," "too broad," "off-niche," "person-not-topic"). ✗ rows STAY in the table, struck through, in rank position — the operator overrules any call, and a beginner learns as much from the struck rows as the kept ones. Backfill from next-ranked candidates so ~50 rows carry ✓. Itemize exclusions by category with counts in the stage report (the free-triage report shape, adopted).

**Degradation:** FRESH → 50 real rows, each with url, channel, views, outlier multiple, date, confidence (VERIFIED). STALE → same table, date-stamped header "as of `<generated_at>` (N days old)", claims LIKELY, refresh command printed under the header. ABSENT → **no top-50 table is fabricated, ever.** The artifact renders the bucket *framework* (Stage 3 structure, empty), a banner "INTERVIEW-ONLY — no performance data; zero rows below this line are real until the radar runs", and the exact refresh + `add-channels` commands. This is the tier where his free user got an authoritative-looking table on pasted anecdotes; ours refuses.

### Stage 2 — Velocity + trend (the beats-static-scoring layer)

Where the pack carries `velocity_vpd_7d` (needs 2+ radar snapshots), attach it per row and compute per-bucket **trend direction: rising / steady / decaying** — a high-outlier bucket that is decaying is a different decision than one still climbing, and his static scores cannot tell them apart. Single-snapshot packs: velocity columns render as "— (needs 2nd snapshot; next refresh adds it)" — a named gap, not a blank.

### Stage 3 — Cluster into buckets (5–8), with mechanisms

Group the ✓ set by *subject matter the avatar cares about*, not surface keywords. Per bucket: plain-language name, video count, median outlier (median beats totals — one monster row shouldn't crown a bucket), total views, trend direction, top-3 linked examples, and:

- **Why-it-works mechanism (ours — stats are not an explanation):** one named mechanism per bucket — the psychological reason these videos hold and convert this avatar (status protection, insider access, fear-of-botched, permission-to-want, etc.), grounded in the dossier's identity layer and, where transcripts exist (`transcript_path` on flagged outliers), in what the winning videos actually do. Label the mechanism VERIFIED (visible in ≥2 transcripts/hooks, cite them) or LIKELY (inferred — say from what).
- **One-channel-dominance flag:** a bucket dominated by one channel is *a person winning, not a topic winning* — mark it weaker evidence. Print the trap callout inside the chart, adjacent to the row it disarms (adopted move: name the trap where the misread happens).
- **Format buckets (descriptive only):** cluster script skeletons from `format_hint` + `leaderboard.formats`; keep descriptive — selection happens in `gb-format-find`.

### Stage 4 — Bullseye overlay + conversion column

Tag each topic bucket with its ring. Check the shape of what's winning: winners clustering at Rings 4–5 means the niche's data skews broad and the operator must consciously *protect* their narrow picks rather than chase "what's working"; winners at Rings 2–3 confirm the narrow aim. Then the **conversion column (ours):** every bucket → the offer it feeds → funnel role → the "working =" threshold, pulled from the bullseye revenue overlay — so the table answers "which of these 50 makes the avatar *buy*?", not just "what reached." A bucket with no offer linkage is flagged honestly: reach-only.

### Stage 5 — Pick the 3 (positioning picks from the pool performance built)

Recommend 3 buckets in the 3-2-1 shape (2 narrow + 1 broad — never three at the same breadth). Weight and SHOW the reasoning per bucket: (1) **performance** — median outlier + trend, receipted; (2) **positioning fit** — serves the UPA/whitespace, cite the whitespace entry; (3) **substance advantage** — the operator can say something better here, cite the dossier evidence; (4) **conversion** — the overlay's economics. A high-performance bucket with zero substance advantage is a trap — flag it. Rank orders the pool; it does not dictate the pick — passing on high-ranked rows is correct behavior when the edge or the buyer isn't there (the two filter questions from the dossier: worth the avatar's time? builds trust?). Operator's read beats ours; bench stands.

### Stage 6 — Save + visualize + hand off

Write both files (schemas below), render `exports/topic-scan.html` (ranked bucket bars in ring colors, chosen buckets crowned, expandable specimen rows, trap callouts inline, bullseye-placement toggle reusing the ring geometry). Update `manifest.json` (deps: [bullseye], data_tier, pack_ref incl. run_receipt_path), snapshot priors. Refresh note: re-scan at ~45 days or on `gb-refresh` flag. One-line state + next: `gb-format-find`.

## Output Contract

Execution prompt: `references/prompts-v2/topic-scan-top-50.md` — honor its Output Contract.

1. **State markdown, two files:**
   - `topic-buckets.md`: working-set definition + itemized exclusions → topic bucket table (count / median outlier / views / **trend** / **mechanism** / examples) → format bucket table (descriptive) → bullseye overlay + **conversion column** → the 3 chosen with four-factor reasoning → refresh note → blind-spot section (pack `coverage` scope — platform limits; conversion data the pack cannot see: check DMs/comments match the avatar before crowning a conversion winner) → data-tier declaration.
   - `top-50.md` (the shared data core downstream reads): header block — created date, source pack path + `generated_at` + `run_receipt_path`, lookback window, "Read by: gb-format-find, gb-blueprint (+ Wave-2: engine-builder, topic-brainstormer, video-maker)"; key line defining ✓/✗, ★ (chosen-bucket rows), and outlier inline; then the ranked table: `# | ✓/✗+reason | bucket (★) | one-liner | channel | views | outlier | velocity | link`. ✗ rows struck through, dimmed, in rank position.
2. **Client HTML** — `render_brief.py --client` → `exports/topic-scan.html` + `top-50-client.html`.
3. **Export** — PDF; export row on both.

## Content-Type Adaptations

| Mode | Adaptation |
|---|---|
| **Self-run (Farrice)** | Chosen buckets cross-read against the content lanes already proven on his channels; triage applies his two filter questions with his actual offers as the conversion column |
| **Client engagement** | Stage report (itemized exclusions + what a refresh costs: $0 + minutes) shown to the client — the cost-transparency shape builds trust; top-50 is a named deliverable |
| **Lead-magnet step-down** | Top-10 rows fully receipted + one bucket with its mechanism card as proof-of-method; the full 50, conversion column, and picks are the paid depth; one CTA row |

## Quality Gate

Score against `genius.md` §3; any single 1 fails. Load-bearing here:
- **Q1 (hard):** ABSENT tier → zero fabricated rows; FRESH → all 50 receipted; STALE → date-stamped + command quoted.
- **Q3:** conversion column present on every bucket, or honestly "reach-only"/"unassigned (no bullseye yet)".
- **Q5:** every bucket carries a named why-it-works mechanism, labeled VERIFIED or LIKELY with its source.
- **Q7:** person-not-topic flags printed adjacent to the rows they disarm; blind-spot section names coverage + conversion invisibility.
- **Q9:** `top-50.md` header declares its consumers ("Read by:") and its source receipt; manifest updated; next step named.
