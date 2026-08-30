---
name: "gb-whitespace"
description: "Watchlist + 8-attribute competitive grid + Positioning Wheel: every score cites ≥2 specimen videos with receipts from the signal pack; unclaimed-vs-graveyard verdicts on measured data; every whitespace entry ends in a decision-ready move."
expert: "Growth Blueprint OS"
produces: "growth-lab/<niche-slug>/whitespace-map.md + exports/positioning-wheel.html"
---

# Growth Blueprint OS — Whitespace Map + Positioning Wheel

## Pre-Flight Gate

- **Dossier exists?** Read `growth-lab/<niche-slug>/positioning-dossier.md`. Missing → ask for a two-line version (who they serve + what they're known for) and proceed, or route to `gb-interview` if there's nothing. Never block on ceremony.
- **Pack state?** Check `.agent/outlier-radar/packs/<niche-slug>/latest.json` and classify FRESH / STALE / ABSENT per SKILL.md `data_contract`. Declare the tier out loud before Stage 1 — it governs every claim in this artifact.
- **Frame to carry:** an empty niche is homestead land; a crowded one is beachfront — deals exist only for buyers who study the market street by street. This workflow is the street-by-street study.

## Skill Acquisition

Load `genius.md` (§1.1 receipts-first; §2.4 menu-not-verdict; §2.6 five-beat panels; anti-pattern #1). Load `references/artifact-design-language.md` before rendering the Wheel. Optional stack: `competitive-intel` agent for pricing/moat findings beyond content (brief negatively; return only findings with sources).

## Execution

### Stage 1 — Build the watchlist (8–12 channels)

Target channels either doing exactly what the operator wants to do, or serving the same buyer a different way. Build paths, in order until full:

1. **Pack seed (default when pack exists).** `channels[]` from the signal pack is the measured starting roster — carry handle, subscriber_count, and each channel's best outlier rows as the why-they-matter evidence.
2. **Operator knows the players.** Add their handles; queue them for the next radar run: `python3 execution/outlier_radar.py add-channels --niche <slug> @h1 @h2`.
3. **Discovery research.** `execution/research.py` with 3–5 search terms derived from the dossier (one per bullseye ring once `gb-bullseye` has run) — platform search, "who do top channels follow," adjacent-buyer channels. Receipts on every candidate.
4. **Nothing surfaces.** Manual platform search on the niche's common terms; harvest the follow-lists of the one or two found.

Present as a table: `# | @handle | platform | followers | why-they-matter` — the note column does real work in ≤12 words (nearest analog / nearest *lane* competitor / format proof point). Flag channels that rank high but serve the wrong avatar: subscriber count is not fit. Menu-not-verdict: recommend the roster, let the operator swap.

**Degradation:** FRESH → follower counts and outlier evidence cited from pack receipts (VERIFIED). STALE → same, date-stamped "as of `<generated_at>`" + quote `python3 execution/outlier_radar.py refresh --niche <slug>`. ABSENT → watchlist builds from research.py + operator knowledge only; every performance characterization is UNCONFIRMED; the artifact banner reads INTERVIEW-ONLY and Stage 3 scores degrade as below.

### Stage 2 — Evidence pull per channel

For each watchlist channel, assemble the specimen pool from the pack: its `ranked_videos` rows (url, title, views, outlier_multiplier, published_at, hook_text, topic, format_hint), plus `leaderboard.topics` / `leaderboard.formats` at niche scope. Flagged outliers may carry transcripts (`transcript_path`) — read them for substance-depth and delivery-style scoring rather than guessing from titles. Free triage before any paid depth; if any paid enrichment lane is proposed (research.py at scale), itemize the bill first (§2.5 genius.md).

### Stage 3 — The 8-attribute competitive grid (the heart)

Score every channel on the seven attributes plus ours:

| # | Attribute | What to extract |
|---|---|---|
| 1 | Topic selection | What they cover; what they never touch |
| 2 | Substance depth | Surface motivation vs. tactical how-it-works vs. mechanism-level; is it actually applicable? |
| 3 | Unique stories/proof | The lived proof they lean on (results, case volume, scars) |
| 4 | Avatar specificity | Who they're really talking to; which slices they ignore |
| 5 | Delivery style | Tone, cadence, persona |
| 6 | Storytelling format | Recurring script skeletons |
| 7 | Visual format | Production style |
| **8** | **Belief positioning** *(ours — untouched by his attribute set)* | What this channel makes the audience BELIEVE — about the problem, the solution category, and themselves. Read hooks + transcripts for the implied worldview ("more filler is the answer" vs. "you've been sold the wrong fix"). The open lane is often a belief nobody is installing, not a topic nobody is covering. Cross-reference the dossier's identity layer: which buyer beliefs does each channel reinforce vs. challenge? |

**Specimen floor (Q2, hard):** every attribute score cites **≥2 specimen videos** with URL + views + outlier + date. A score that can't produce two specimens is written as UNCONFIRMED with the gap named — never silently confident. Scoring hygiene: a channel should be *strong* in only 2–3 attributes; if every channel scores everywhere, tighten.

Build two views:
- **Saturation map** — per attribute: the niche default, and how crowded each variant is (counts: "N of 12 channels here").
- **Whitespace list** — every defensible gap, each entry carrying: (a) which watchlist channels prove it's empty (named, with specimens), (b) the **unclaimed-vs-graveyard verdict on measured data** — zero videos = unclaimed; many low-outlier videos = graveyard; the pack's outlier multiples are what tell these apart, and without them the verdict is UNCONFIRMED, (c) **a decision-ready move**: "claim it with these 3 topics this batch" — a whitespace entry that ends in analysis instead of a move is unfinished.

### Stage 4 — Verdict on the positioning hypothesis

Cross the whitespace list against the dossier's 7-attribute hypothesis table. Per claimed edge: **confirmed** (real white space + they can fill it — cite the specimens that prove emptiness) / **contested** (someone's there — name them, and say what it would take to win anyway) / **redirect** (a better gap nearby suits their unfair advantage — name it). Close with the one-paragraph **Unique Positioning Angle**: the lane, which attributes it stacks (attributes multiply — the win is an unoccupied *intersection*, not an outright attribute win), and the evidence. Be blunt: a comforting whitespace map that hides a dominant incumbent costs the operator six months.

### Stage 5 — The Positioning Wheel (signature artifact — never skip)

Render per `references/artifact-design-language.md`: 8-wedge radial (his 7 + belief positioning), channel bubbles sized by followers, saturation heat in Premium Minimal semantics (NOT his dark-navy chat style), star markers on the verdict's recommended wedges, and the **five-beat teaching panel per wedge** (definition → option menu → niche scoreboard with receipts → white space → what it means for you). Every bubble click opens a channel card with specimens; a click that does nothing is a bug. Same five beats appear in the markdown so the teaching survives outside the HTML. Export row on the artifact. **The surpass bar this artifact answers:** a judge clicks any score — ours opens receipts; his opens nothing without a paid plan.

### Stage 6 — Save + hand off

Write `growth-lab/<niche-slug>/whitespace-map.md`, render `exports/positioning-wheel.html`, update `manifest.json` (deps: [positioning-dossier], data_tier, pack_ref), snapshot priors to `history/`. One-line state + next: `gb-bullseye`.

## Output Contract

Execution prompt: `references/prompts-v2/whitespace-map.md` — honor its Output Contract.

1. **State markdown** — `whitespace-map.md`: watchlist table → per-channel 8-attribute grid (every score w/ ≥2 specimens or UNCONFIRMED) → saturation map → whitespace list (evidence + unclaimed/graveyard verdict + decision-ready move per entry) → hypothesis verdict (confirmed/contested/redirect per edge) → UPA paragraph → blind-spot section (platform coverage limits from pack `coverage`; what the grid can't see) → data-tier declaration.
2. **Client HTML** — Positioning Wheel via `render_brief.py --client` → `exports/positioning-wheel.html` + `whitespace-map-client.html`.
3. **Export** — PDF; export row on both artifacts.

## Content-Type Adaptations

| Mode | Adaptation |
|---|---|
| **Self-run (Farrice)** | Watchlist seeded from known-competitor canon on disk before discovery; belief-positioning wedge cross-read against his own thought-leadership lane |
| **Client engagement** | The Wheel is a named client deliverable; verdict paragraph written to be read aloud in a call; receipts appendix implementation-grade |
| **Lead-magnet step-down** | One wedge fully receipted as the proof-of-method + the saturation map summary; the full grid, verdicts, and moves are the paid depth; one CTA row |

## Quality Gate

Score against `genius.md` §3; any single 1 fails. Load-bearing here:
- **Q1/Q2:** every score ≥2 specimens w/ URL+views+outlier+date, or UNCONFIRMED; data tier declared at top.
- **Q4:** every claimed edge gets confirmed/contested/redirect — no edge left unadjudicated.
- **Q6:** every whitespace entry ends in a decision-ready move.
- **Q7:** blind-spot section names pack coverage limits and the one-channel-dominance trap where it applies.
- **Q9:** wheel + map both in exports/, manifest updated, next step named.
