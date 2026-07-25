# Visual Context — Dara Denney Creative Strategy Videos (watched 2026-07-25)

Source videos, both watched (36 keyframes @1024px, video 1; video 2 is talking-head, transcript-sufficient):

1. **"How I Build an Elite Creative Strategy for a Brand in One Sitting"** — yt `yRgPbqywUJ8`, 21:57, published 2026-07-25
2. **"I Hired 100+ Creative Strategists | Here's Exactly What Gets You Paid $10K/month"** — yt `gqnp-IdEEI8`, 29:44, published 2026-07-03

## Her actual Notion Research SOP (frame t=00:55 — page "Research SOP (NEW)", workspace "…dia's HQ / Creative Strategist")

Header line verbatim: *"This SOP outlines our entire creative strategy research process."*
Promise line: *"By the end of this research process, you will have the following context documents that will help you better prompt any AI tool."*

**Resources (the 4 produced documents):**
1. The Reputation Analysis Document
2. Customer Review Mining Sheet
3. AI Analysis on Ads Document
4. Competitors Document

**Quick links (the 4 steps, verbatim):**
- First: Conduct a "Reputation Analysis"
- Second: Customer Review Mining
- Third: **Persona and Desire Segmentation**
- Fourth: **Create the Mission Doc**

Below: "Creative Strategy Research SOP" rendered as a Notion **gallery view** (Gallery/Table/Feed tabs), one card per step with cover images: "Step 1: Reputation Analysis", "Step 2: Customer Review Mining" (Laura Geller review-mining spreadsheet visible as the card cover — columns include product names + ratings counts e.g. "30,320 ratings", "2,969 ratings"), plus further step cards.

## Product & Brand Analysis card (frames t=00:31, t=01:55 — yellow slide)

- **Brand:** Founder · Founding story (discover the WHY behind the brand) · Best selling products · Offers · Merchandising strategy
- **Product:** The promise · Evidence it works / proof · Features · Benefits · Bundles or potential to bundle

## Reputation Analysis channel cards (frames t=03:25, t=04:35 — verbatim)

- **Press:** "Older demographics still have a lot of trust in the press, while Gen Z tends to trust creators more. Press can be earned or bought. Here we're looking for: big moves the company is making, reoccurring value props or learnings that can be emphasized."
- **Reddit:** "The most honest and cutthroat place to figure out what people really think of your brand. Best in terms of learning how to speak like the customer. Pay attention to recent threads, comments with the most upvotes, reoccurring objections & desires."
- **Amazon:** "The clearest side-by-side [of] products… Their 'Ask Amazon' [AI feature] is act[ually…]" (partially occluded; transcript completes: Ask-Amazon persona probe — "what type of people are buying this product?" returns an Amazon-specific persona breakdown).

## Persona & Desire Segmentation SOP page (frame t=08:36 — THE MOAT ARTIFACT)

Her SOP shows the persona step with prompt + example output:
- *"Example 👇 You will get a response similar to this (in text form, not PDF). See below the details of each of the Persona segments and **Desire-based segments**. If your LLM does not give you details like this, simply copy my example below and tell your AI to format it like this."*
- Embedded example: **"Research Deck — [brand redacted]"**, 18 pages, subtitle verbatim: **"Named personas from 1,079 customer reviews + 424 survey responses — Mined for ad angles, emotional triggers & creative strategy."**
- Collapsed toggles visible: **"Step 2: Pick the audience segments with the most evidence and potential"** · **"Step 3: Create a deck with AI"**
- Inputs to the persona prompt (per transcript): reviews CSV + reputation analysis doc + her persona PDF + her prompt → outputs persona/desire segment deck for team review.

## Creative Testing Roadmap sheet (frame t=17:51 — Oats Overnight example, Google Sheets)

Title: "Creative Testing Roadmap" + brand logo. Columns: **Test # · Concept Name · Nº Variations (3-6) · Winning Elements (dropdown: Hook / Angle / Format / Storyline) · Creative Type (dropdown: UGC / Video / Image / Carousels)**.
Ten real concept rows verbatim: SHAKING OATS ASMR · DEAR DIY'ers... THIS IS NOT 4 U · I'M GLAD I STILL TRIED THIS · PARTNERSHIP ADS: THE WAREHOUSE · PARTNERSHIP ADS: THE EGC MAIN · FULLNESS CHASER STATICS · "THIS KEEPS ME FULL" CREATOR · TASTES LIKE... COMPILATION · TASTES LIKE CAROUSEL: NOSTALGIA · PA: BUSY WORKERS CREATORS.
(Note the direct research→concept traceability: DIY objection → "DEAR DIY'ers", satiety gap persona → "FULLNESS CHASER" + "THIS KEEPS ME FULL", partnership-ad platform trend → two PA tests, GLP-1/nostalgia angles.)

## Other frames

- t=02:44: Grüns Mother's Day Bundle ad ("1 bag adults + 1 bag kids × 28 daily servings") — merchandising/bundle analysis exhibit.
- t=05:58: Jones Road founder-content exhibit ("1. BODY CREAM: We almost launched our body collection with the Lorem Ipsum dummy copy on it…") — behind-the-scenes/EGC platform-trend exhibit.
- t=19:56: **Meta Ad Library** live search for "rhode" (Active ads filter, Library IDs, "2 ads use this creative and text") — this is her ad-account recon surface for the gap analysis; free and public.
- t=13:16: Gordon Ramsay "Rolls Royce of pans" TikTok — organic-signal exhibit.

## Implications for our build

- The SOP's deliverables are all reproducible on in-house infra at $0: Reddit/press/YouTube research (research.py / Tavily / Playwright), Amazon probe (manual, free), Meta Ad Library recon (ad_spy.py / Playwright), review mining (CSV + deterministic miner + in-session LLM analysis), persona deck (in-session), Notion for the client-facing surfaces.
- Her explicit framing: every research doc is **a context document for your LLM of choice** — i.e., the deliverables ARE an AI context engine. This maps 1:1 to our Context Engine / memory-facade philosophy and makes the harvested package directly usable as AI fuel for client work.
