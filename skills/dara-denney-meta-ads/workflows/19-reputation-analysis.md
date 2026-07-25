---
description: Run Dara Denney's 7-station reputation analysis — retrace the skeptical customer's research journey (brand/product → Google → press → Reddit → Amazon → social → YouTube) into one LLM-ready context document with the friction point named
---

# `/dara-reputation-analysis` — The Customer-Journey Research Document

Step 1 of the Research SOP. You are not "doing research" — you are pre-living the purchase decision of a skeptical first-time customer, station by station, and logging every friction point they'd hit. Dara has run this for hundreds of brands; her rule: whenever she's nervous about a new brand, this process alone produces "a few really great ideas." The Grüns spec-work doc from this exact SOP earned public feedback from the brand.

## Genius Context (Load First)

Read `genius.md` — Creative Strategy OS layer:
- **Pattern 11**: Research-as-Customer-Journey Simulation — run the stations in the customer's order
- **Pattern 12**: Every Artifact Is LLM Fuel — the output doc is a context document, formatted to prompt with
- **Pattern 18**: Bundle-as-Creative-Lever — merchandising is inside your remit
- Quality Rubric criteria 2, 3, 8

## Input Required

- **Brand**: name + primary product for paid social focus (if multi-product, start with the one the creative strategy will lead with)
- **Mode**: client engagement / spec work (dream-client flywheel) / own brand
- **Category posture**: problem-solution direct (supplements, tools) or vibes-with-performance (beauty, fashion) — changes the punch level downstream

## Execution

Work through all 7 stations IN CUSTOMER ORDER. Use real tools only (`execution/research.py`, Playwright for JS surfaces, WebSearch) — no phantom research; every claim in the doc carries a source. Where a station is thin, say so — a verified "nothing found" is a finding.

1. **Brand & product analysis** —
   - Brand: founder + founding team, founding story and the big WHY, best-selling products, merchandising strategy, offers across the business (zoom on the paid-social offers).
   - Per focus product: the promise (the transformation it claims), evidence/proof it works, features, benefits, bundles or potential to bundle.
   - **AOV check**: can this unit price survive paid CAC? If not, draft a problem-solution bundle proposal — re-merchandising is a legitimate strategist move.
2. **First page of Google** — search as a customer would. Red flags a first-time buyer would see? Scam/complaint results? Competitor comparisons ranking above the brand?
3. **Press** — which publications; **earned vs bought** (batches of formulaic placements = bought; single in-depth legit media = earned); brand news that unlocks strategy (funding/IPO, retail launches, expansions). Older demographics still trust legacy print/web; Gen Z trusts creators.
4. **Reddit** — the most honest, anonymized, ruthless surface. Recent threads, most-upvoted comments, recurring objections AND desires, exact customer phrasing (this is where you learn to speak like the customer). Capture verbatim quotes with links.
5. **Amazon** (if present) — Amazon best-seller vs DTC best-seller delta; rankings, review counts, star distribution; **Ask-Amazon AI probe**: "what type of people are buying this product?" → log the Amazon-native persona breakdown (free, underutilized).
6. **Social media** — core content strategies actually working, community cultivation, storytelling style, employee-generated content / behind-the-scenes transparency, creator roster diversity.
7. **YouTube** — review videos (even bought ones reveal what attracts buyers through the buying experience); **the comments are the goldmine**: skepticism, objections, FAQs. Golden-nugget-style reviews hide here.

**Synthesis (the point of the whole doc)**:
- The common objections, ranked by frequency across stations.
- **THE friction point** — name ONE: trust-in-efficacy / worth-it skepticism / price-value framing. Not a list of ten.
- 3-5 immediate creative hypotheses that fell out of the journey (Grüns standard: "is this a scam" language everywhere → "Are Grüns a scam?" ad + negative-marketing twin).
- Anything you manually clipped along the way goes into the review-mining sheet seed list (hand off to `/dara-review-mining`).

## Output Schema

Write to the engagement folder (or `deliverables/` for spec work). Template: `references/templates/reputation-analysis-template.md`. Sections: Brand & Product Analysis · Google Page 1 · Press (earned/bought table) · Reddit (verbatim quote bank) · Amazon (incl. Ask-Amazon persona probe) · Social · YouTube (comment harvest) · Synthesis (objections ranked, THE friction point, creative hypotheses, bundle proposal if triggered). Header note: "This document is a context document — attach it whenever prompting on this brand."

## Context Adaptations

| Context | Adaptation |
|---|---|
| Brand client | Full 7 stations; deliverable-grade; feeds persona deck + mission doc |
| Personal brand (Farrice/creator) | Stations become: Google yourself, your platform comments, your DMs/replies, communities where your ICP talks; friction point = why they don't buy/follow/book |
| Spec work / dream client | Timebox to one sitting; prioritize Reddit + YouTube comments + ad library; output feeds `/dara-spec-work-engine` |

## Quality Gate

- All 7 stations present (thin stations explicitly marked, never silently skipped) — Rubric #2.
- ONE named friction point — Rubric #3. A list of co-equal objections = fail.
- Every hypothesis traces to a station finding (the "DEAR DIY'ers ← DIY objection" traceability standard) — Rubric #4.
- Verbatim quotes carry sources. Phantom research = kill the doc.
- Formatted as promptable LLM context (ranked, quote-rich, clean headers) — Rubric #8.

## When to Return

- Brand onboarding · quarterly refresh (reputation shifts) · before any pitch (timeboxed spec version) · when performance tanks (re-check whether the friction point moved).
