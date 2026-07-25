# Persona Intelligence System — The Moat Spec

> Frame-grounded from Dara Denney's Research SOP (watched 2026-07-25, yt `yRgPbqywUJ8`) + transcript. Flagged by Farrice as a foundational moat: "the whole concept surrounding the persona, marketing, intelligence brief and gap… could even be its own product or service."

## Why This Is a Moat

Most persona work in the market is invented (demographic avatars, "Marketing Mary" slop). Dara's system is **forensic**: personas are *named from evidence*, ranked by *measurable axes*, cross-checked against *what the account actually runs*, and shipped as a *reviewable deck*. The deck's own cover line is the category-difference in one sentence:

> **"Named personas from 1,079 customer reviews + 424 survey responses — mined for ad angles, emotional triggers & creative strategy."**

Nobody argues with 1,079 receipts. That's the moat: **evidence-ranked persona intelligence with gap traceability** — defensible in a pitch, compounding in an engagement, and directly promptable as AI context.

## The System (5 components)

### 1. Evidence Corpus
Reviews CSV (full site export) + top-20 ads' comments (last year) + manual clips from the reputation-analysis journey (Reddit/Amazon/YouTube/press) + surveys when they exist. Free persona source most strategists skip: the **Ask-Amazon AI probe** — "what type of people are buying this product?" returns an Amazon-native persona breakdown.

### 2. Dual Segmentation — WHO × WANT
- **Persona segments (WHO)**: recurring buyer identities — life stage, context, use case, self-description. Named memorably.
- **Desire-based segments (WANT)**: recurring desired outcomes that cut across personas (satiety, convenience, not-getting-scammed, younger-without-looking-done).
Angles are mined from BOTH families. Persona-only segmentation is half the system.

### 3. Receipts + Ranking
Every segment carries: evidence count · 3-5 hottest verbatim quotes · source spread. Rank on two axes:
- **Evidence volume** (frequency of appearance)
- **Emotional intensity** (heat of the language)
The money quadrant: **high-intensity + underrepresented in the current creative mix** (Oats Overnight "keeps me full" → FULLNESS CHASER tests). Her SOP verbatim: "Pick the audience segments with the most evidence and potential."

### 4. Gap Cross-Analysis (persona intelligence meets the live account)
Deck vs ad account: untargeted personas · over-indexed personas vs their evidence weight · the awareness-level spread per persona · creator-diversity read. Two signature strategist moves fall out:
- **Persona injection** — a segment the brand has NEVER targeted, with its wedge creative (Rhode: 40+ persona via Gen-X celebrity partnership ad → "a customer they're not seeing walk through their Sephora stores").
- **Winner × persona replication** — top construct templated across every core persona (D&G: perimenopausal women → GLP-1 men → new moms).

### 5. The Deliverable — Research Deck + Context Doc
18-page-standard deck (reviewed with the team) AND a text-form rendition, because "once you have this analysis, this is another really rich context document for you to upload to your LLMs." The deck is simultaneously: client deliverable · creative-team brief · AI grounding pack.

## Productization (standalone offer shapes)

| Shape | Scope | Use |
|---|---|---|
| **Persona Teardown** (lead magnet / spec) | Category-evidence version, 2-3 segments, public-safe | `/dara-spec-work-engine` ammo; free teardown → paid fix motion |
| **Persona Intelligence Brief** (entry product) | Full corpus, dual segmentation, ranking matrix, activation picks | Fixed-scope, fast, the moat as a unit |
| **Persona → Strategy Sprint** | Brief + gap analysis + mission doc + roadmap | The `/dara-research-sop` package |
| **Persona Governance** (retainer layer) | Quarterly re-rank, injection pipeline, replication matrices | Inside the own-the-outcome retainer |

House stacking (compose freely, never force): `/avatar-machine` Phase 0 GROUND or `icp-deep-canvasser` deepen the 1-2 activation segments to identity-level; `/mcraney-deep-canvass` for resistance mapping; `buyer-council` to pressure-test segments; Recall grounding fires automatically on this domain.

## Anti-Patterns (kill on sight)

- A segment without receipts (count + verbatim quotes). Invented personas void the moat claim.
- Persona-only output (missing desire segments).
- Ranking by gut instead of volume × intensity.
- A deck with no activation picks or no net-new injection proposal (or unverified "saturation").
- Shipping the deck without the text-form LLM context rendition.
- Demographic-slop naming ("Millennial Mary") — names come from the evidence's own language ("Fullness Chasers").

## In-House Execution Map ($0-first)

- Corpus compile: client export + `execution/review_miner.py` pre-pass (deterministic ranking + nugget candidates) + `/scrape-creator` for public comment harvests (pennies via Apify) + Playwright for Ad Library.
- Segmentation + deck: in-session (this skill) — deck copy per `templates/persona-research-deck-template.md`; render to Notion template for client delivery; Gamma/Canva optional for visual deck polish.
- Verification: Chain Step 5.5 on any real-brand claims before external delivery.
