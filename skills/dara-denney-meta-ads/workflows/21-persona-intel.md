---
description: "Persona & Desire Segmentation — Dara's evidence-ranked persona system: named personas + desire segments mined from the review corpus, ranked by evidence volume × emotional intensity, delivered as a client-grade research deck. The moat deliverable — also sellable standalone"
---

# `/dara-persona-intel` — Persona & Desire Segmentation (The Moat)

Step 3 of the Research SOP and the highest-leverage deliverable in it: **"one of the big things we ultimately do for brands is identifying new personas that we can then develop a creative strategy around so that they can reach net new audiences."** Personas here are not invented avatars — they are NAMED from evidence ("Named personas from 1,079 customer reviews + 424 survey responses — mined for ad angles, emotional triggers & creative strategy"), ranked, and shipped as a deck the team reviews. This deliverable is packageable as its own product (see `references/persona-intelligence-moat.md`).

## Genius Context (Load First)

Read `genius.md` — Creative Strategy OS layer:
- **Pattern 13**: Evidence-Ranked Personas — every segment carries receipts (count + hottest verbatim quotes)
- **Pattern 14**: Desire Segments Ride Alongside Personas — WHO and WANT are separate segment families
- **Pattern 15**: Persona Injection for Net-New Audiences — the Rhode 40+ play is the standard
- **Pattern 16**: Winner × Persona Replication
- `references/persona-intelligence-moat.md` — full system spec + productization

Deep-grounding option (stack, don't force): `/avatar-machine` Phase 0 GROUND or `icp-deep-canvasser` for identity-level depth on the 1-2 segments you'll actually activate first.

## Input Required

- **Evidence corpus**: review-mining output (from `/dara-review-mining`) + reputation analysis doc (from `/dara-reputation-analysis`); surveys if they exist
- **Current targeting** (if available): which personas the account targets today — enables the gap cross-analysis
- **Business intent**: scale existing / open net-new audiences / fix efficiency

## Execution

1. **Segment discovery** — from the corpus, surface BOTH families:
   - **Persona segments (WHO)**: recurring buyer identities — life stage, job/context, use case, self-description. Name them memorably ("Fullness Chasers", "Odd-Hours Workers", "Skeptical 40+ Skincare Convert").
   - **Desire-based segments (WANT)**: recurring desired outcomes/transformations that cut across personas (satiety, convenience, "not getting scammed," looking younger without looking done).
2. **Attach receipts per segment** — evidence count (how many reviews/comments express it), 3-5 hottest verbatim quotes, source spread (site/ad-comments/Reddit/Amazon). **A segment without receipts does not ship.**
3. **Rank** — two axes: **evidence volume** × **emotional intensity of language**. (Oats Overnight: the "keeps me full" segment had the MOST emotional language and was UNDERREPRESENTED in creative — that intersection is where money hides.)
4. **Pick activation segments** — SOP verbatim: "Pick the audience segments with the most evidence and potential." 2-4 max. For each: current awareness profile, the pillar angles (2-3 per persona — angles are big pillar pain-point ideas, not concepts), entry format recommendation (from the 8 video / 7 static archetypes), emotional triggers, objection set.
5. **Net-new persona injection** — propose ≥1 persona the brand has never targeted, with its wedge (Rhode standard: press+reviews signaled "not for me, but it worked on my skin" → 40+ celebrity partnership ad → a customer Sephora doesn't see). If saturation is real, verify and say so.
6. **Winner × persona replication matrix** (if the account has winners) — top creative construct × each activation persona (D&G for perimenopausal women → GLP-1 men → new moms). Storyblocks/asset notes per cell optional.
7. **Deck it** — client-grade research deck per `references/templates/persona-research-deck-template.md` (the 18-page standard). Also emit the text-form version (LLM context doc — Pattern 12).

## Output Schema

Deck sections: Cover (evidence line: "Named personas from N reviews + M …") · Method (1 page) · Persona Segments (1-2 pages each: name, portrait, receipts, angles, triggers, objections, awareness, entry format) · Desire Segments · Ranking Matrix (volume × intensity, with the underrepresented-hot quadrant flagged) · Activation Picks + rationale · Net-New Injection · Winner × Persona Replication Matrix · "How to use this deck" (for the client's team + their AI tools).

## Context Adaptations

| Context | Adaptation |
|---|---|
| Brand client | Full deck; the flagship deliverable of the research phase |
| Personal brand | Segments mined from YOUR audience evidence (comments/DMs/client convos); desire segments become content pillars; feeds /farrice-engine + voice work |
| Standalone product | See `references/persona-intelligence-moat.md` — Persona Intelligence Brief as a fixed-scope offer (spec-work teaser → paid deep version) |
| Creatives in general | Swap "reviews" for the evidence a creative has: audience comments, listener mail, community threads — same receipts discipline |

## Quality Gate

- **Zero segments without receipts** (count + verbatim quotes + source spread) — Rubric #1. An invented persona is a killed deck.
- Both families present (personas AND desire segments) — persona-only = fail.
- Ranking shows BOTH axes and flags the hot-but-underrepresented quadrant.
- ≥1 net-new injection or verified saturation statement — Rubric #7.
- Angles are pillar-level (2-3 per activation persona), not a concept list.
- Deck is reviewable by a team AND promptable by an LLM (both renditions shipped).

## When to Return

- New engagement (always) · quarterly re-rank (segments shift with the corpus) · after survey drops · when scaling stalls (usually a persona gap, not a creative gap).
