# Angle Brief — headless run instructions (Mon/Thu 07:00)

You are producing Farrice's **Angle Brief**: a condensed, visual HTML intelligence
brief — hook angles + content angles for his active work, grounded in what his
niche actually engaged with this week. This is the run he reads with coffee.
Standard: the research-brief system he called "really dope" — dense, visual,
zero slop, every claim sourced from the input files.

**HARD BOUNDARIES:** No publishing, outreach, or contact of any kind. Drafts and
intelligence only. No Chain, no finalize, no Notion, no Next Moves, no subagents.
Never invent a statistic, quote, or engagement number — everything traces to an
input file below, labeled VERIFIED / LIKELY / UNCONFIRMED.

## Inputs (read in this order; skip gracefully if missing)

1. **Resonance + roster** — newest `_active/linkedin-launch/05-lead-gen/engager-rosters/ROSTER-*.md`
   (the runner refreshes this before you start). Hooks that pulled hand-raises,
   reaction mixes, ICP-verbatim comment language.
2. **Zeitgeist** — newest `deliverables/research-briefs/zeitgeist-*/` brief JSON(s)
   (there may be several lanes: ai-consulting-linkedin, supplement-brands, jen-sfv-realestate).
3. **Thought bank** — `_active/farrice-brand/thought-bank/inbox/` unprocessed items (his raw ideas; connect,
   don't consume — do not mark or move them).
4. **Active work context** — `_active/linkedin-launch/CAMPAIGN.md` (top section only:
   offer + queue) so angles serve live revenue work.

## Craft loads (before writing any hook or angle)

- `_active/farrice-brand/voice/VOICE-CARD.md` — his voice is the base LAYER.
- `skills/kallaway-content-psychology/workflows/hook-engineering-matrix.md`
- `skills/kallaway-ai-content-engine/workflows/trend-hook-radar.md`
- One Diandra hook reference from `skills/diandra-escobar-linkedin-growth/`
  (Diandra = hooks only, per standing rule — never body copy).

## Output

Build `brief.json` at `.tmp/angle-brief/angle-brief-YYYY-MM-DD.json` per the schema
documented at the top of `execution/render_brief.py`, then run:

    python3 execution/render_brief.py .tmp/angle-brief/angle-brief-YYYY-MM-DD.json

Brief shape (slug `angle-brief-YYYY-MM-DD`, chip `ANGLE BRIEF · SIGNAL SCOUT + ZEITGEIST`):
- **summary** — what's moving in his niche this week, 3–5 sentences, one thesis.
- **evidence** — resonance rows: hook → engagement numbers → why it pulled
  (confidence per row; roster data = VERIFIED, inferences = LIKELY).
- **bars** — one chart if the data supports it (e.g. reactions by post/topic).
- **prose — "ICP verbatim"** — 4–6 exact comment quotes from the roster worth
  stealing as copy language (quote EXACTLY; his ICP-verbatim rule is binding).
- **decision — "angles for what's live"** — 5–8 hook/content angles, each tied to
  a piece of active work (Cash Launch, Parallax, Jen) AND an evidence row. Action
  + why-with-the-number.
- **deploy** — 2–3 copy-paste first lines / hooks in HIS voice (drafts; he decides
  what ships). Run them through `python3 execution/prose_classifier.py check` via a
  temp file first; rewrite any flagged line before including.
- **caveats** — sample sizes, what the scout can't see (2nd-degree data, non-LinkedIn),
  staleness of any lane that didn't refresh.
- **ledger** — every input file used, with retrieved date + confidence.

Keep it ONE brief, dense over long. If an input is missing (e.g. zeitgeist skipped
today), say so in caveats and proceed with what exists — never pad, never invent.
