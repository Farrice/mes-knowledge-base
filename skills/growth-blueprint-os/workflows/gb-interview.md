---
name: "gb-interview"
description: "Niche interview → Positioning Dossier: reflect-back interview mechanics, Chair Test, identity layer (belief/resistance/cost-of-admitting), and a pain bank pre-stocked with ≥10 sourced buyer verbatims wired to offers."
expert: "Growth Blueprint OS"
produces: "growth-lab/<niche-slug>/positioning-dossier.md"
---

# Growth Blueprint OS — Niche Interview → Positioning Dossier

## Pre-Flight Gate

- **Niche slug decided?** Pick `<niche-slug>` (kebab-case) — it names the state folder and the signal-pack lane for the whole engagement.
- **Self-run?** Load `FARRICE-MASTER-CONTEXT.md` FIRST and never interview about what's on disk — fold known facts into reflect-backs and ask only what's missing (identity/voice/offer canon rule).
- **Client run?** Confirm the offer map exists (what is sold, at what price, to whom) or make it Block 1's first question.
- **Existing dossier?** If `growth-lab/<niche-slug>/positioning-dossier.md` exists, this is a refresh: snapshot to `history/`, load it, and interview only the deltas.

## Skill Acquisition

Load `genius.md` (Surpass Doctrine §1.2 identity depth; adopted patterns §2 reflect-back, hypothesis-labeling; rubric §3). For identity-layer depth, optionally dispatch `icp-deep-canvasser` (brief it negatively: no Chain, no finalize, no Notion, return only the profile). Pain-mining uses `execution/research.py` — never training memory.

## Execution

### Step 1 — The interview (5 blocks, one question at a time)

Interview mechanics (adopted, non-negotiable):
- **One question at a time. Never stack.** Interview, not a form. Invite voice: messy rambles are perfect; structuring them is our job.
- **Reflect back after every answer** in one tightened sentence. Vague answer → reflect a *sharper guess* back ("Sounds like you mean practice-owner dentists, not associates — right?") instead of stacking a follow-up. The reflect IS the sharpening tool.
- **Never re-ask known information.** Fold it into the reflect-back and move to the next unknown.
- **Don't let them outsource the thinking.** A generic-persona answer ("busy professionals 25–45") gets one warm push: "Who's a *real* person you've sold to who fits this? Describe them."
- Questions are engineered to provoke ramble, not tidy bullets — end the unfair-advantage question with a one-word instruction to ramble.

**Block 1 — The business behind the content.** Offer, price point, how it's bought, revenue mix (which products/services actually make the money — not the offer list). **Viewer = buyer check:** if the people who'd watch aren't the people who pay, center everything on the buyer and record why in the dossier. This is the revenue anchor everything downstream references.

**Block 2 — The Chair Test.** Person-level specificity: the perfect viewer-turned-buyer sitting in the chair across from them. Age, what their day looks like, what they've already tried that failed, what they're afraid of, what they said that signaled "this is my buyer." The depth standard is ~350 words for this one answer — a portrait, not a demographic band. Capture demographics only where they matter; the gold is what they believe, fear, have tried, and say.

**Block 3 — Dream outcome.** One sentence. The terminal prize, not the feature.

**Block 4 — Pain points (seed only).** 5–10 from memory, seeded with: "What do buyers ask right before they buy?" and "What wrong belief do you constantly correct?" Rank by degree of pain. This is the *seed list* — Step 3 replaces memory with evidence.

**Block 5 — Target Authority Statement.** Draft all three canonical shapes ("I help X with Y" / "I help X do Y to achieve Z" / "Y for X"), iterate until one clicks. Specificity is the whole game.

**Unfair advantage (one final question).** Experiences, results, stories, credentials, or a way of communicating most people in the space can't honestly claim. Let them ramble; mine it, don't tidy it.

### Step 2 — The identity layer (the McRaney triad — his system stops before this)

From the interview material (plus `icp-deep-canvasser` if dispatched), map three levels beneath the psychographics, each answered in the buyer's own situation, not category language:

| Layer | Question it answers | What it feeds |
|---|---|---|
| **Belief** | What does the buyer currently believe about the problem, the solution category, and the people who sell it? | Content angles that meet the belief instead of arguing with it |
| **Resistance** | What does NOT buying protect? (identity, social standing, self-image, past investment) | Objection-aware bucket jobs; the villain slot — the villain is never the buyer |
| **Cost of admitting** | What does it cost this person socially/emotionally to admit they have this problem or want this outcome? | The register of every hook and CTA; what can be said out loud vs. shown obliquely |

Label each entry: sourced from interview (VERIFIED as *their* claim), inferred (LIKELY, state the inference), or unknown ([NEED]).

### Step 3 — Verbatim pain-mining (data step — degradation tiers apply)

Replace the memory-seeded pain list with observed language. Run `execution/research.py` across comments, reviews, forums, and Q&A surfaces where this buyer actually talks (competitor comment sections, Reddit, Amazon reviews of adjacent products, industry forums). Target: **≥10 real buyer verbatims, quoted EXACTLY, each with URL + date.** Never elevate the paraphrase — the buyer's words ship as-is (house rule: ICP verbatim > pageantry). Cross-validate the self-reported pains: which are confirmed in the wild (VERIFIED, receipts), which appear nowhere (UNCONFIRMED — keep, flagged), and which pains the wild surfaced that the operator never mentioned (the gold — flag as discovery). Rank by observed frequency, not seller memory.

**Degradation:** this step consumes `research.py`, not the signal pack — the pack is optional here. If web research is unavailable this session: ship the seed list labeled UNCONFIRMED throughout, add a `[NEED]` block naming the mining run as the missing evidence, and quote the exact command to close it. **Never present the memory-seeded list as validated.** If a FRESH pack exists, pull `ranked_videos[].hook_text` for the niche as a secondary language source (what hooks the niche already validates) and cite pack receipts.

### Step 4 — Pain → offer wiring (revenue layer)

Every pain point gets a wiring row: pain → the offer it feeds → the natural CTA shape. A pain that feeds no offer is flagged honestly (audience-building value only). This table is what `gb-bullseye` reads to compute bucket economics.

### Step 5 — The 7-attribute self-assessment (hypothesis, labeled)

Draft it yourself from everything said — do NOT run seven more questions. Attributes: topic selection, substance depth, unique stories/proof, avatar specificity, delivery style, storytelling format, visual format. Score each **Strong / Possible / Not-yet** with one evidence clause lifted from their own answers (compressed clauses, not paraphrase). The scale means *what kind of proof is missing*, not *how good it is*. Show the table, take one round of corrections. **Honesty rule (adopted):** this table is a hypothesis from self-knowledge — `gb-whitespace` crosses it against what the niche actually posts. Say so in the dossier; don't let anyone treat it as settled.

### Step 6 — Assemble, save, hand off

Write `growth-lab/<niche-slug>/positioning-dossier.md` (schema in Output Contract), update `manifest.json` (produced_at, data_tier, deps: []), snapshot any prior version to `history/`. Close with a one-line English state + next step: `gb-whitespace`.

## Output Contract

Execution prompt: `references/prompts-v2/positioning-dossier.md` — honor its Output Contract.

Three forms, all claims labeled VERIFIED / LIKELY / UNCONFIRMED:

1. **State markdown** — `growth-lab/<niche-slug>/positioning-dossier.md`: (1) the business + offer map + viewer=buyer verdict · (2) named avatar portrait (Chair Test) · (3) identity layer table (belief / resistance / cost-of-admitting) · (4) pain bank — ≥10 sourced verbatims w/ URLs, ranked by observed frequency, each wired to an offer · (5) dream outcome · (6) Target Authority Statement (final + two alternates) · (7) 7-attribute hypothesis table, marked "to be crossed against niche data" · (8) two filter questions (worth the avatar's time? builds trust?) · (9) data-tier declaration + `[NEED]` gaps.
2. **Client HTML** — `python3 execution/render_brief.py --client` → `exports/positioning-dossier-client.html` (Premium Minimal; interaction canon per `references/artifact-design-language.md`).
3. **Export** — PDF from the client HTML; export row on the artifact.

## Content-Type Adaptations

| Mode | Adaptation |
|---|---|
| **Self-run (Farrice)** | FARRICE-MASTER-CONTEXT.md is canon — interview only gaps; VOICE-CARD layered at delivery; pains cross-checked against the existing offer shelf, never re-invented |
| **Client engagement** | Implementation-grade always: full receipts in an appendix, ≤2-page executive layer up front; interview can run async (voice memos); client sees the verbatim pain bank as a named deliverable section. **Owned-metrics intake (standing step):** request the client's own analytics exports at kickoff — IG Professional Dashboard export, TikTok analytics CSV, YouTube Studio export — and feed them through the radar's owned_metrics lane; their measured numbers beat any scraper and close the TikTok/IG coverage gap for $0 (decision card: `growth-lab/DECISION-CARD-tiktok-ig-data.md`) |
| **Lead-magnet step-down** | Subtraction from premium: avatar portrait + top-3 pains (verbatims kept, receipts summarized) + authority statement only; identity layer and offer wiring withheld — they are the paid depth; one CTA row |

## Quality Gate

Score against `genius.md` §3 before shipping; any single 1 fails. Load-bearing checks here:
- **Q2:** ≥10 buyer verbatims with URLs — or the artifact says INTERVIEW-ONLY/[NEED] and the mining command is quoted. Never both absent.
- **Q3:** every pain wired to an offer or honestly flagged as unwired.
- **Q4:** the 7-attribute table is explicitly labeled a hypothesis with its falsification step named.
- **Q8:** zero invented buyer language; verbatims exact; paraphrase only where labeled as ours.
- **Q9:** manifest updated; prior version in `history/`; next step named in one line.
