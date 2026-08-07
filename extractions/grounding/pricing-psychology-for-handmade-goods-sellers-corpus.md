# Grounding Corpus — pricing psychology for handmade goods sellers (2026-07-15)
Verdict: FORGE-READY — 12 receipted entries across 3 modalities (in-repo doctrine, Recall practitioner cards, live web at $0 tier), with named practitioners and one peer-reviewed anchor; enough to ground the majority of a practitioner-grade skill protocol.

Translation card: anchor exploratory/system · deliverable: eventually a skill · audience: handmade-goods sellers · felt standard: "practitioner-grade"

**Negative check (ran first):** `prompt_library.py search` + `ls skills/` + DOMAIN_REGISTRY sweep found 4 fuzzy candidates; all opened and cleared as adjacent, none own this concept:
- `skills/nicolas-cole-digital-products/references/prompts-v2/pricing-psychology-optimizer.md` — owns *digital info-product* pricing (6 vehicles, $350 threshold); physical handmade goods outside its taxonomy.
- `skills/paul-james-ai-automation/references/prompts-v2/pricing-psychology-system.md` — monthly-vs-project *service* pricing.
- `skills/oren-luxury-psychology/` — premium positioning; frontmatter explicitly excludes value-pricing strategy.
- `skills/kunal-shah-consumer-psychology/` — Delta-4 opportunity evaluation, not seller-side pricing mechanics.
- DOMAIN_REGISTRY nearest neighbor: Chris Do (value-based pricing for *creative services*) — couldn't ground the majority of a handmade-goods pricing protocol (cost floors, marketplace anchoring, maker underpricing psychology).

---

## Entry 1: The "handmade effect" — consumers pay a premium because handmade products are perceived to symbolically "contain love"
- Excerpt: "The study provides evidence for a positive handmade effect on product attractiveness... driven by perceptions that handmade products symbolically 'contain love'... validated by controlling for effort, product quality, uniqueness, authenticity, and pride. Consumers indicate stronger purchase intentions for handmade than machine-made products when buying gifts for their loved ones but not for more distant gift recipients."
- Receipt: Fuchs, Schreier & van Osselaer, *Journal of Marketing* 79 (March 2015), 98–110 — https://journals.sagepub.com/doi/10.1509/jm.14.0018 (cross-confirmed: https://www.sciencedaily.com/releases/2015/03/150324111544.htm)
- Confidence: VERIFIED

## Entry 2: Janet LeBlanc (Paper + Spark) — the maker pricing formula: (Supplies × 4) + Labor + Overhead = Retail
- Excerpt: "(Supplies x 4) + Labor + Overhead Rate = Retail Price"; labor is "Time x Wage — you must pay yourself an hourly rate"; the common Supplies×2=Wholesale, Wholesale×2=Retail formula "leaves out a whole bunch of other fees and expenses" → "tons of sales but NO MONEY IN YOUR BANK ACCOUNT." Worked example: druzy ring $3.67 supplies × 4 + $5 labor + $4.23 overhead = $23.91 → $24, leaving room for 50% wholesale discounting.
- Receipt: https://paperandspark.com/etsy-pricing-formula-how-to-price-for-handmade-part-1
- Confidence: LIKELY

## Entry 3: Charm pricing (.99) vs prestige round numbers — the split decision every handmade seller must make deliberately
- Excerpt: "people are more likely to buy a product that costs $9.99 than one that costs $10" (cites Capital One Shopping research: charm pricing can increase sales "up to 24%" — stat not independently chased); round numbers "if you want your products to be perceived as higher quality": a ceramic mug at $42 "reads very differently to buyers than the same mug at $39.99." Qualifier: "pricing psychology is about how you present a price, not how you set it."
- Receipt: https://craftybase.com/blog/pricing-psychology-magic-numbers
- Confidence: LIKELY

## Entry 4: Rory Sutherland — price is a quality signal and artisan cues are perceptual, not material
- Excerpt: "increasing the price can sometimes make a product more popular, as price can be a quality signal"; P&G "launching a premium product at a high price point to make subsequent products appear better value"; "illustration and hand drawing kind of says handmade... Charlie Bigham's genius was putting the thing in a bamboo thing rather than a plastic pot — fundamentally that completely changed our perception."
- Receipt: recall:aba7f896-61b3-4aff-b6c8-7cdd91aa8dc8 + recall:533e6771-3a2e-4c32-8188-672f964ad0f5 (two independent Sutherland talks)
- Confidence: VERIFIED

## Entry 5: Richard Shotton — change the comparison set to change willingness to pay
- Excerpt: "Seedlip's pricing strategy... consumers are comparing the price of Seedlip to that of alcoholic gin rather than other cordials, and are therefore willing to pay a higher price"; "Red Bull launched its product in a smaller, tall, and thin can, which broke the comparison with cheaper soft drinks"; Rolls-Royce sold "at yacht shows or air shows rather than car shows" to seem cheaper by comparison.
- Receipt: recall:a92afbd4-e3e4-446b-b3d0-411d09c4715c
- Confidence: LIKELY

## Entry 6: Simon Sinek's "Dave's Cashmere Shop" — material equivalence does not transfer price; story does
- Excerpt: "a guy who makes cashmere jerseys and he uses the exact same cashmere as Loro Piana... But the problem is it says like Dave's Cashmere Shop... That's the same everything. And you'd be like, 'Yeah, Dave's Cashmere Shop.' Because you're not buying the cashmere. You're buying the [brand]."
- Receipt: recall:fabcc002-17bb-45ae-b51a-25f744df05a9
- Confidence: LIKELY

## Entry 7: Jason Fladlien — underpricing is fear, not strategy (priced his first product at $4)
- Excerpt: "why do you think I priced a product at four dollars when I first launched it? because I was scared out of my mind... I didn't want to overcharge anybody... I didn't want people to be upset at me and I didn't want people to call me names."
- Receipt: recall:21e7e5b6-fa74-4d29-aa7d-8f07627686bb
- Confidence: LIKELY

## Entry 8: $50 → $5,000 for the same product — positioning, packaging, presentation set price; fear pricing attracts worse customers
- Excerpt: "The same digital product was sold for $50 and $5,000, with the difference in price due to positioning, packaging, and presentation, not the product itself"; "Pricing based on fear... attracts low-commitment customers who are more likely to complain and less likely to achieve results"; willingness-to-pay bands: "If somebody is willing to pay $85 for something, they will most likely pay $150 for the same thing."
- Receipt: recall:926eb814-b444-47bc-9837-8d0edc7a1899
- Confidence: LIKELY

## Entry 9: Eric Osuorah (AFOMA Marketplace) — value-based over cost-plus for artisans; underpricing red-flag diagnostic
- Excerpt: "Very low prices often signal low quality. Buyers of handmade goods expect fair pricing"; cost-plus "ignores skill level, rarity, cultural value, and emotional connection"; red flags: constant busyness with minimal earnings, guilt about charging fairly, dependency on discounts; "Underpricing doesn't create stability—it leads to burnout and short-lived businesses." Recommends good/better/best tiers so "buyers can choose without feeling pressured."
- Receipt: https://afomamarketplace.com/blogs/pricing-handmade-goods-guide
- Confidence: LIKELY

## Entry 10: Oren doctrine-on-disk — every price is a job (entry/core/aspirational/halo) and price-style must match brand position
- Excerpt: "Price is a signal, not only a number... Identify anchors, charm/rounded pricing, lost price points, underpricing risk, and quality-signal gaps... [Aspirational =] Higher-price item that anchors perception... Premium brand: favor rounded pricing, insider proof, and aspirational/halo anchors; Value brand: use charm pricing selectively and make value explicit without cheapening trust."
- Receipt: _active/harness/codex-harvest-2026-06-11/skills/oren-archetype-social-strategy/workflows/oren-pricing-psychology-map.md
- Confidence: VERIFIED (canonical doctrine-on-disk)

## Entry 11: Nicolas Cole doctrine-on-disk — below the impulse threshold, default to the TOP of the valid range (adjacent domain; transfer with care)
- Excerpt: "Below $350: This is 'blender territory' — impulse purchase zone. Default to the TOP of the range. Lower price attracts more buyers but generates LESS total revenue (empirically proven)... tested price points across 22+ product cohorts." [Adjacency flag: proven on digital products; the impulse-zone/top-of-range mechanism is the transferable part, not the $350 number.]
- Receipt: skills/nicolas-cole-digital-products/references/prompts-v2/pricing-psychology-optimizer.md
- Confidence: VERIFIED (canonical doctrine-on-disk; cross-domain transfer UNCONFIRMED)

## Entry 12: Mark Ford — roughly 10% of any audience wants to pay MORE; a missing premium tier is money refused
- Excerpt: "there are 10% of the people that want to pay you more... they don't feel like it's value [otherwise] — that's how I felt about Dale Carnegie. I wanted more of that and they didn't really provide it. I was willing to pay a lot more for it and I would have been happy for it."
- Receipt: recall:8f7e63d3-befd-4135-bf3f-f99363f49ffa
- Confidence: LIKELY

## Cut at ceiling (pointers only)
- Value-anchor sales sequence (old-way cost → value anchor → rationalized price) — recall:dfaf2286-7ba8-4b91-96db-df3f29b631dd ("How Founders Sell")
- Alen Sultanic: competing purchases pull down willingness-to-pay at higher prices — recall:0ae9e44e-a30d-4543-9615-6944259b7e8e
- "Price to demand and market, not hours invested" — recall:7c38b6f2-45ec-4821-9b46-6d65fa4f8573
- "15 Reasons Why You Should Sell At Higher Prices" (confidence = technique drilled + psychology) — recall:b16c0f8e-6cd1-479f-8adc-0f020f87c30c
- Etsy-specific fee/pricing mechanics — https://craftybase.com/blog/how-to-price-on-etsy · https://www.alura.io/post/mastering-etsy-pricing-for-profit-a-complete-strategy-guide

## Sprint Receipt
- Modalities swept: in-repo (grep across _active/, projects/, extractions/, research_outputs/ — 2 doctrine hits used) · Recall (exhaustive, 3 queries — ~28 cards returned, 8 used) · episodic (2 phrasings: "handmade goods pricing etsy", "pricing psychology anchoring" — 3 hits, all tangential, modality empty) · live web at $0 floor (research.py --depth quick → Tavily 15 sources/12 domains + WebFetch of 3 primaries + 1 WebSearch verification)
- Practitioners: Fuchs/Schreier/van Osselaer (peer-reviewed), Janet LeBlanc (Paper + Spark), Rory Sutherland, Richard Shotton, Simon Sinek, Jason Fladlien, Eric Osuorah, Mark Ford, + Oren/Cole doctrine-on-disk
- Confidence: 4 VERIFIED · 8 LIKELY · 0 UNCONFIRMED (one secondhand stat flagged unchased inside Entry 3)
- Research tier used: $0 floor only (research.py ran at --depth quick; no paid engines touched)
- Handoff: `/extract-forge` with `extractions/grounding/pricing-psychology-for-handmade-goods-sellers-corpus.md` as source
