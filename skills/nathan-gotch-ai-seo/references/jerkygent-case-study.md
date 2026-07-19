# The JerkyGent Case Study — Gotch's Live Category Teardown (primary source, 2026-07-15)

The complete worked example behind Patterns 15-25. Source: youtube.com/watch?v=3sHPiOIHPTY
(18:57). Frame-level ledger: `extractions/nathan-gotch/visual-context.md`. Use this file as the
calibration anchor when executing workflows 06-14 — outputs should look like THIS, at this
altitude, with counted numbers.

## The setup

Random e-commerce brand (JerkyGent, healthy beef jerky), no association, free strategy on the
house. Target category: "best healthy beef jerky" — broad, competitive. Doctrine stated up front:
one category for 90-180 days, mile deep; strategy developable in one day.

## Step 1 — Benchmark (the split diagnosis)

- Traditional search: **#3 in Google organic**, coverage across 4 engines, 2 URLs in top 25. "They're doing a really good job in traditional search."
- AI answers: **absent** — not in ChatGPT answers, not in the product carousel (ChatGPT recommended Archer, People's Choice, Mission Meats, Nuts.com instead). AI Overview: not mentioned.
- Composite: SPI **33/100 "Weak"** — Traditional 76%, Video 7%, **AI mentions 0%**, AI citations 37%.
- The verdict frame: "They're missing out on sales right now by not being recommended."

## Step 2 — Citation autopsy

Citations for the category: 82 sources analyzed. Brand mentioned in **4** — three self-serving
(own site, linked), one unlinked google.com neutral. "Imagine you're the AI… you've got this brand
that no one ever talks about, no one ever recommends across any of your sources. It's working
through these different sources and then looking for consensus." Archer shows up everywhere
because it's mentioned across almost every citation.

## Step 3 — Export and mark

Run multiple keyword reports (best healthy / sugar free / plant based / gluten free beef jerky) →
"Export to spreadsheet" → one sheet, ~158 rows. Schema: Keyword | URL | Platforms (ai_mode,
perplexity, deepseek, brave_ai, google_organic, chatgpt, claude, gemini, copilot, grok,
duckduckgo, bing) | Avg. position | Opportunity (Y).

Hand-classification of the URLs:
- **Earned media (~20 opportunities)**: blogs, news sites, affiliate roundups, a BusinessWire press release picked up in AI mode ("we can run these ourselves"), Reddit threads ("you can infiltrate Reddit pretty easily these days").
- **Owned media signals**: Facebook groups, Instagram posts/reels, YouTube watch + Shorts URLs appearing in retrieval → attack on two fronts: build own content for those exact queries AND outreach to influencers already on those platforms.
- **Distribution gaps**: Target, Walmart, Amazon URLs in retrieval; brand on none of the three. "Three massive e-commerce distribution engines… and they're actually being used in retrieval as well."

Scaling law: ~20 earned opportunities from ~4 topics; "multiply by 10 or 20 topics, you'd have a
list of a couple hundred opportunities easily."

## Step 4 — Topic gap map (one Canva board)

Center node: "best healthy beef jerky". Green node = already covered (sugar free / high protein /
low sodium / keto / low fat / grass fed / gluten free) — "I can tell they have an in-house SEO
that's pretty solid… I'm impressed. But there are gaps still." Gap nodes from keyword research
(cluster vols from 14.8K down to 0): paleo / weight loss / bodybuilders / diabetics; zinc /
magnesium / vitamin d / iron / calcium / selenium / collagen peptides — "all separate dedicated
intents." Competitor node: Archer / Perky / People's Choice / Chomps + Alternatives → "[Competitor]
vs [Competitor] vs [us]". Plus Owned Media, Distribution, Earned/Paid Media nodes. If GSC access
existed, granular queries would be piped in directly.

## Step 5 — The alternatives ladder (template on screen)

"5 Best Alternatives to Archer Jerky for 2026 Snacking" (1,357 words, content score 66):
- Intro concedes competitor strength (People's Choice — "family recipe dating to 1929").
- **Quick Picks**: self gets ONE honest slot ("Best overall for craft discovery: JerkyGent") beside People's Choice (traditional butcher-style), Righteous Felon (big spicy flavors), EPIC (ingredient-conscious), Tillamook (store availability).
- **What We Looked For**: flavor range, texture, ingredient fit, value (price per ounce), availability — criteria disclosed.
Sequence: [X] alternatives for every competitor → [X] vs [Y] → [X] vs [Y] vs [us]. "These are
absolutely the best because it kills two birds with one stone."

## Step 6 — Owned media echo

Website is home base; build topic authority there first. Once tapped out → YouTube (long-form
first — "YouTube has so much influence"; Shorts appear in retrieval as a secondary play) → Facebook
→ Instagram. "Don't overthink this. You just take the same topics, but make sure the content
format matches whatever distribution channel you're using."

## Step 7 — Tracking: benchmark → annotate → scan

"A lot of people are just wasting money on tracking… there's no point tracking performance every
day if you aren't working on that category." Protocol: benchmark snapshot (not continuous
tracking) → annotate every shipped asset on the SPI timeline (date, title, category e.g. "Content
change") → run a scan after work → read movement against annotations. "You're not going to be able
to say that one asset's what did it, but you can clearly see over time."

## Step 8 — The linkbait chain (informational topic support)

Anti-exemplar named on the brand's own site: "Why high protein snacks are a great idea" — "not
just kind of generic stuff that AI could spin up in 2 seconds."

The chain he runs instead (verbatim prompts: `linkbait-prompt-bank.md`):
1. Category-focused ideation prompt → 25 grounded ideas (e.g. "State of Healthy Beef Jerky Report" — analyze 100-250 products across 8 nutrition dimensions, annual report, PR hook: "We analyzed 150 beef jerky products. Only X% met our healthy jerky criteria," seeded by USDA FoodData Central; "Beef Jerky Health Score Calculator" — calculators earn recurring links).
2. **Prioritize 5**: State of the Category Report, Sodium Index, A Decade of Recalls, Healthy Halo Audit, Blind Taste Test.
3. Deep research on the chosen angle — ran **12m 10s** → 18 recall/health-alert events 2016-2025, 99,628 lbs, **72% caused by labeling/allergen/inspection failures, not pathogens**.
4. QA the research: read the "Important limitations," adopt the **most defensible lead statistic**, reframe title ("Recalls and Health Alerts").
5. "Create a prompt for my design agent for the visual assets to support this data-driven study" → paste to Claude design → complete asset system (hero 1600×900, OG, mobile, findings card, cause donut, timeline, U.S. map, explainers, full infographic) in the brand's own design system, alt text included, "serious consumer research report, not a sensational food-scare campaign."
6. **Edit**: skip clarifying questions, let it cook, then "focus on editing… sometimes you'll see some hallucination" — the magic is in the edit.

## Close

"If we go into ChatGPT, we can see there were 25 different angles that you could attack just in
this one category. I can guarantee you your competitors are not doing this."

## Tool-agnostic note (for $0-tooling deployments)

Rankability provides the benchmark/citations/export conveniences, but every step is replicable
manually: run the query set across ChatGPT/Perplexity/Gemini/Copilot yourself, paste citations
into a sheet with the same schema (Keyword | URL | Platform | Position | Opportunity), classify by
hand, benchmark with dated screenshots, annotate work in the same sheet. The methodology is the
asset; the tool is a convenience.
