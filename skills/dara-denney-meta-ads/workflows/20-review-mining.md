---
description: Compile the full review corpus (site reviews + top-20 ad comments + manual clips), rank products, extract golden nuggets, and run Dara's AI analysis questions into an LLM-ready insights doc
---

# `/dara-review-mining` — Customer Review Mining + AI Analysis

Step 2 of the Research SOP. The corpus is everything customers have said — site reviews exported in bulk, the comments on the top ~20 ads of the last year, plus the standout quotes you clipped manually during the reputation analysis. The automation boundary is explicit: machines compile, **human judgment picks the golden nuggets** — "they don't quite have the judgment of what could be a really impactful review that could lead to a top performing ad."

## Genius Context (Load First)

Read `genius.md` — Creative Strategy OS layer:
- **Pattern 12**: Every Artifact Is LLM Fuel
- **Pattern 13**: Evidence-Ranked Personas (this doc feeds the persona step — quotes carry receipts)
- Hidden knowledge: ad-comment mining beats site-review mining for objection freshness
- Existing copy mechanic #7 (Borrow from customers / golden-nugget testimonials) — this workflow is its industrial version

## Input Required

- **Review corpus**: CSV/export from the review platform (Judge.me, Okendo, Yotpo, Amazon export…) — any columns, minimum: product, rating, text
- **Top ads list**: the brand's top ~20 ads over the last year (from client reporting or Meta Ad Library recon) — harvest their comments
- **Reputation analysis doc** (from `/dara-reputation-analysis`) — for the manual-clip seed list and cross-checking

## Execution

1. **Compile** — one sheet, three sources tagged: `site-review` / `ad-comment` / `manual-clip`. If a CSV exists, run the deterministic pre-pass first:
   ```bash
   python3 execution/review_miner.py <reviews.csv> --out .tmp/review-mine/
   ```
   It ranks products by review count × rating, surfaces candidate golden nuggets (emotion/specificity heuristics), and emits an analysis-ready markdown pack. $0, local, no API.
2. **Rank products** — by number of reviews AND rating; note deltas vs what the brand pushes on paid social (a beloved product with no ad spend = finding).
3. **Golden-nugget pass (HUMAN/MODEL JUDGMENT — never fully delegated)** — from the candidates, select quotes that could headline a top-performing ad: specific, emotional, self-selecting, taboo-touching, or objection-flipping. The Oats Overnight standard: DIY objection + its defender counter-voices ("I love the convenience… I work odd hours… when I do it myself it doesn't taste like that") → became "DEAR DIY'ers… THIS IS NOT 4 U."
4. **AI analysis** — run the corpus through Dara's questions:
   - What are our strengths and weaknesses as a brand?
   - Most common complaints/objections — similar or dissimilar to the reputation-analysis findings? (Convergence = confidence; divergence = investigate.)
   - Golden-nugget phrases — any trends among them?
   - What are the trigger points that cause someone to buy?
5. **Package** — the analysis doc is the second LLM context document. Template: `references/templates/review-mining-sheet.md`.

## Output Schema

- Ranked product table (reviews × rating × paid-social presence)
- Golden Nugget Bank (each: verbatim quote · source tag · why it could carry an ad · candidate mechanic from the 8 copy mechanics)
- AI Analysis (the 4 questions answered, convergence/divergence vs reputation analysis called out)
- Trigger Points (ranked buy-triggers with supporting quotes)
- Handoff line: "Feed this + the reputation analysis to `/dara-persona-intel`."

## Context Adaptations

| Context | Adaptation |
|---|---|
| Brand client | Full corpus; ad comments prioritized for freshness |
| Personal brand | Corpus = your post comments, DMs, testimonials, client feedback; nuggets become content hooks and offer copy |
| No review base yet (new brand) | Mine the CATEGORY: competitor reviews, Reddit, Amazon — label clearly as category evidence, not brand evidence |

## Quality Gate

- Three source types present or their absence explained.
- Every golden nugget is VERBATIM with a source tag — paraphrased nuggets are dead nuggets.
- Convergence/divergence vs reputation analysis explicitly stated.
- The doc prompts well: a stranger could attach it to an LLM and get better ads immediately (Rubric #8).

## When to Return

- Quarterly corpus refresh · after any viral ad (fresh comment goldmine) · before each new persona push.
