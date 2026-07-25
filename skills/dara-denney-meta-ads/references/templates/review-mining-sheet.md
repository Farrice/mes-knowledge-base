# Customer Review Mining + AI Analysis — [BRAND]

> Context document — attach whenever prompting on this brand. Corpus: [N] site reviews + comments from top [N] ads (last 12 mo) + [N] manual clips. Pre-pass: `python3 execution/review_miner.py <reviews.csv>`.

## Product Ranking
| Product | # Reviews | Avg Rating | On paid social? | Note |
|---|---|---|---|---|
Deltas worth flagging (beloved-but-unadvertised, pushed-but-unloved):

## Golden Nugget Bank (human-judged — the ad-carrying quotes)
| # | Verbatim quote | Source (site/ad-comment/manual) | Why it could carry an ad | Candidate mechanic (of the 8) |
|---|---|---|---|---|

## AI Analysis (the 4 questions)
1. **Strengths / weaknesses as a brand**:
2. **Most common complaints & objections** — convergent or divergent vs the reputation analysis? [state which]:
3. **Golden-nugget phrase trends**:
4. **Trigger points that cause purchase** (ranked, with supporting quotes):

## Handoff
Feed this + the reputation analysis to `/dara-persona-intel` (Persona & Desire Segmentation).
