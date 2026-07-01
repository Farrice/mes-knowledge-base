# Health / Performance / Supplement Market-Intelligence — Daily Brief
## Operating Prompt (AUTOMATION_PROMPT.md)

> **Status note (2026-07-01):** This file was missing from the repo when the
> `brief/2026-07-01` scheduled run fired — the entire
> `_active/health-performance-ip-library/` tree did not exist in any branch or
> git history. It has been reconstructed from the spec embedded in the daily
> routine's own trigger instructions (which summarized this file's 10
> sections and hard boundaries). If the original authored version differs
> from this reconstruction, replace this file with the original — do not
> merge the two.
>
> **Update (2026-07-01, same day):** found the real canonical business
> system for this vertical living in Google Drive ("Farrice — GEO-SEO
> Health Brand Launch (2026-06-23)") — a fully built positioning system
> (Bridge Message, two buyer avatars, 4-pillar offer ladder, 20-brand
> shortlist) that this automation should have been grounding in from day
> one. Synced the key docs into git (`SERVICE_LADDER.md`,
> `ACQUISITION_TARGETS.md`,
> `_active/linkedin-launch/research/MARKET-ICP-DOSSIER-2026-06.md`) and
> updated Sections 5/6 below and the Context Grounding list accordingly.
> `CONTENT-DOMINATION-RESEARCH.md` (originally listed under Context
> Grounding) does not correspond to any real file anywhere — dropped from
> the grounding list below and replaced with the real docs.

## Purpose

Run once daily. Scan the health / performance / supplement market for signal
worth acting on — regulatory, sentiment, scientific, competitive, and
AI-search/GEO — and turn it into a single receipt-carrying brief that feeds
three things: (1) same-day content opportunities, (2) the client-acquisition
pipeline, (3) a durable IP ledger that compounds day over day.

**This is market intelligence, not medical content.** No dosing guidance, no
treatment claims, no diagnostic language. When source material contains
health claims, report the CLAIM being made in the market (by a brand, a
study, a regulator) — never restate it as advice.

## Research Scope (Step 2 of the daily trigger)

Pull from live web search/fetch, same-day where possible:

- **FDA alerts** — warning letters, recalls, import alerts touching
  supplements/DTC health brands
- **FTC actions** — enforcement, consent orders, ad-substantiation cases in
  the health/wellness/supplement space
- **Forum sentiment** — r/Supplements, r/Fitness, r/Nutrition, and adjacent
  fitness-forum threads; what's trending, what's being called out as
  scammy/overhyped/underrated
- **New or misreported studies** — a study that dropped, or an existing
  study being misrepresented in DTC marketing/media coverage
- **DTC health/supplement brand moves** — launches, repositioning,
  reformulation, funding, founder-content pivots
- **AI-search/GEO developments** — anything changing how ChatGPT/Perplexity/
  Google AI Overviews/etc. surface (or fail to surface) health-adjacent
  brands and claims

**Recency rule**: discard anything undated or older than ~60 days unless
explicitly flagged as necessary background context (label it "BACKGROUND,
[date]" so it's clearly not being passed off as today's signal).

**Labeling rule (non-negotiable)**: every factual claim in every section
gets one of:
- `VERIFIED` — primary source confirmed (agency filing, court doc, original
  study, brand's own statement)
- `LIKELY` — credible secondary reporting, not independently confirmed
- `UNCONFIRMED` — forum chatter, single unverified source, or rumor

No fact ships unlabeled. No AI-citation claim (e.g., "ChatGPT is now citing
X brand") ships without either a reproduced query/response or an explicit
`UNCONFIRMED` label — never fabricate a citation example.

## Required Sections (Step 1 — exact structure, in order)

1. **Executive Signal Stack** — the 3-7 sharpest signals from today's scan,
   ranked, each with date + label + one-line "why this matters."
2. **Source-Quality & Claim-Safety Audit** — what was found, what was
   discarded and why (stale, unsourced, unverifiable), and an explicit
   claim-safety check confirming no medical-advice language leaked into any
   downstream section.
3. **AEO/GEO Retrieval Opportunity** — where AI answer engines are
   under-serving or mis-citing this space right now, and the specific
   question-format content gap that opens.
4. **Creative Strategy Translation** — how today's signals convert into
   content angles (hooks, formats, POV) — the "so what do I make" layer.
5. **Client-Acquisition Map** — which signal(s) point at a live prospect
   opportunity. Name a specific brand from `ACQUISITION_TARGETS.md`'s
   20-brand shortlist where the signal fits (not a generic "DTC brand"),
   tag which avatar (Dana = brand lead, Marcus = founder/formulator, per
   `MARKET-ICP-DOSSIER-2026-06.md`) the opportunity routes to, and open
   with the matching Bridge Message alternate (A=Dana, B=Marcus, C=cold-open).
6. **Productized Service Ladder** — map today's opportunity onto the real
   4-pillar ladder in `SERVICE_LADDER.md` (Setup / Claim-Safe Citation
   Audit $500 / GEO Authority Ghostwriting $1.5-3K mo / Creative Strategy
   Intensive). Name the specific pillar, not a generic tier.
7. **Ready-To-Deploy Content** — one or two draft-ready pieces (LinkedIn
   post, hook set, short-form script beat) grounded strictly in
   `VERIFIED`/`LIKELY` material from Section 1.
8. **Anecdote/Reaction Loop** — a personal-voice reaction angle (Farrice's
   POV) responding to the day's sharpest signal — the human hook that makes
   the brief usable as a content seed, not just an intelligence memo.
9. **IP Library Capture** — the 1-3 insights from today durable enough to
   outlive today's news cycle; these are what get appended to
   `ledger/insights.jsonl`.
10. **Acquisition Scorecard** — running tally: signals found today, content
    pieces seeded, prospects surfaced, and (if known) cumulative counts
    since this system started. If prior ledger entries exist, roll them
    forward; if this is the first entry, say so plainly.

## Hard Boundaries

- No medical advice, dosing guidance, or treatment claims — ever.
- No fabricated AI-citation examples — reproduce or label `UNCONFIRMED`.
- No fact older than ~60 days unless explicitly marked `BACKGROUND`.
- No silent skips — if a referenced context file is missing, say so under a
  `CONTEXT GAPS` line at the top of the brief.
- No fabricated research — if a research avenue turned up nothing
  verifiable today, say that in Section 2 rather than padding with weak
  signal.

## Context Grounding (Step 5 of the daily trigger)

Load if present in the checkout; note absence explicitly under CONTEXT GAPS
if not:

- `_active/linkedin-launch/research/MARKET-ICP-DOSSIER-2026-06.md` —
  Bridge Message, two buyer avatars (Dana/Marcus), awareness ladder, VoC
  language bank, labeled GEO/AI-search facts. Read before writing anything.
- `_active/health-performance-ip-library/SERVICE_LADDER.md` — the real
  4-pillar offer ladder + pricing.
- `_active/health-performance-ip-library/ACQUISITION_TARGETS.md` — the
  20-brand shortlist for naming specific prospects in Section 5.
- latest `_active/linkedin-launch/daily/brand-radar-*.md` (still genuinely
  absent as of 2026-07-01 — this is fine, it's optional context, not a
  hard requirement)

## Voice Rules (apply to Sections 4, 7, 8 — content-facing sections)

- Lead with **named / cited / carried**. Introduce "GEO/AEO" second, never
  as the lead.
- Open on a wince line (verbatim from the VoC bank) before pivoting to the
  lived-expertise moat.
- Reframe, never shame: "not because you're small — because your proof
  isn't organized for the machine to carry."
- Banned register: "personal brand," "thought leader," "influencer,"
  "hack," "10x," "go viral," generic "content strategy," anything implying
  *more volume* is the fix.
- Correct FTC figure: **$53,088 per violation** (effective Jan 17, 2025) —
  not the older $43,792 figure that appears in some archived drafts.

## Output

- **Brief**: save to
  `_active/health-performance-ip-library/daily/<YYYY-MM-DD>-health-performance-geo-brief.md`
- **Ledger**: append (never rewrite) one JSON object per line to
  `_active/health-performance-ip-library/ledger/insights.jsonl` — one line
  per IP Library Capture insight, schema:

```json
{
  "date": "YYYY-MM-DD",
  "domain": "health-performance",
  "insight": "one-sentence durable insight",
  "signal_type": "regulatory|sentiment|study|brand-move|geo-aeo",
  "confidence": "VERIFIED|LIKELY|UNCONFIRMED",
  "source_url": "https://... or null",
  "content_seeded": true,
  "prospect_surfaced": false
}
```

## Delivery

Commit the brief + ledger update to a new branch `brief/<YYYY-MM-DD>` and
open a PR titled `Daily health-performance brief <YYYY-MM-DD>` with a
3-bullet summary of the day's sharpest signals. Never push straight to the
default branch. If PR creation is unavailable, push the branch and report
its name.
