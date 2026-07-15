# The Answer Audit: Hiya — AI Search Visibility Teardown

Retargeting ads on Instagram are absurdly fast and good now, especially health and wellness. Full "my phone is listening to me" territory. So I picked a brand from that exact world, Hiya, the kids' vitamin company USANA paid $205 million for, and asked a different question. When a parent asks an AI which vitamin to buy, does Hiya show up at all?

The ads are working. I wanted to know if the answers are.

## How I ran it

I call this the Answer Audit: build the 10 questions a buying parent actually asks (2 head, 3 shoulder, 2 tail, 3 follow-up), run them live against real answer surfaces, and score who gets named and where. No simulated results, ever.

This run, July 15, 2026: 24 scored runs across two surfaces. Surface 1 was the Tavily answer engine (an LLM answer generated over live retrieved sources), 14 runs, with the top 4 questions run twice. Surface 2 was Google-proxy web search (ranked results plus the search tool's synthesized digest), 10 runs.

Honest limitation, stated plainly: the full-strength standard for this audit is 3+ surfaces at 3 runs per question. This run is below it. Perplexity's API returned quota-exhausted errors on all 4 attempted calls, and I did not query ChatGPT or Gemini, so nothing in this teardown claims to describe those surfaces. Repeat runs on the answer engine also came back identical (cached), so answer variance is undersampled. Directional read, real transcripts, disclosed gaps.

## The scorecard

Hiya, per surface:

| Surface | Mention Rate | Avg Position | QA-SOV | Top competitor cited |
|---|---|---|---|---|
| Tavily answer engine (14 runs) | 30% (3/10 questions) | 1.0 | 30 | Renzo's |
| Google-proxy search (10 runs) | 60% (6/10 questions) | 1.3 | 45 | EllaOla |

Formula, shown once: Mention Rate = (questions where the brand appears in the answer ÷ 10 questions tracked) × 100. Avg Position = mean order of brand mention within the answer. QA-SOV = Mention Rate × (1 ÷ Avg Position).

Same rows for everyone who actually got cited (QA-SOV, answer engine / Google-proxy):

| Brand | Answer engine | Google-proxy |
|---|---|---|
| Hiya | 30 | 45 |
| Renzo's | 16 | 10 |
| EllaOla | 0 | 18 |
| Flintstones | 10 | 6 |
| Ritual | 5 | 5 |
| SmartyPants | 5 | 2.5 |

Note the divergence between surfaces. Google's ranked results carry hiyahealth.com on 4 of 10 questions. The answer engine, summarizing a different retrieval corpus, names Hiya on only 3, and the two surfaces disagree hardest on the single most valuable question in the set. That gap is the whole game in AI search: rank is not citation.

## Where Hiya wins

- The branded comparison. "Hiya vs Ritual" went to Hiya on both surfaces, and the corpus doing the selling is third-party review sites (Innerbody, Healthline, The Customer Digest, dietitian-mom blogs), not Hiya's own pages. Earned media is carrying them.
- The 2026 listicle question. "Best children's vitamins in 2026" named Hiya the overall pick, first position, on the answer engine.
- The emotional tail. My 25-word "6-year-old refuses vegetables, pasta and chicken nuggets" question got Hiya as the first recommendation. When the query sounds like a worried parent, Hiya wins.
- Owned-site retrieval on Google. hiyahealth.com ranks #2 for the no-added-sugar head term and #3 for the chewable-not-gummy question.

## Where Hiya bleeds

- The contrarian headline: a $205 million brand built on "zero sugar" loses the zero-sugar question. "Best kids multivitamin without added sugar" is the head query Hiya's entire positioning exists to win. The answer engine recommended Flintstones Sugar-Free Gummies. Both runs. Hiya wasn't in the answer or the cited sources, while their own site sat at #2 on Google for the identical words. Retrieval without citation.
- Renzo's owns "picky eater" by naming alone. Its product is literally called Picky Eater Multi, and it took first position on both picky-eater questions. A product name that matches the question is retrieval bait Hiya has no answer to.
- The protein launch is invisible. Hiya shipped Kids Daily Growth + Protein in May 2026, zero sugar, its first new category in years. "Best kids protein powder without artificial sweeteners" returned Healthy Heights, Transparent Labs, Else. Hiya appeared nowhere on either surface, eight weeks post-launch.
- A perfect-fit tail question is sitting on the table. "4-year-old, dairy allergy, won't take gummies, already has two cavities" describes Hiya's product almost clause by clause. The answers went to Renzo's and EllaOla.
- The teeth question has no brand in it at all. "Chewable vs gummy for kids' teeth" is answered entirely by pediatric dentist blogs. Nobody owns it. That is a sole-citation vacancy in Hiya's strongest argument.

## The one move

One asset drives most of the recoverable value here: a definitive sugar-audit page on hiyahealth.com titled something like "How much sugar is actually in kids' vitamins?" with an original data table across the 15 best-selling kids' vitamins: added sugar per serving, sweetener type, form factor, and the number nobody cited currently publishes, the cumulative annual sugar load of a daily gummy habit. Fold in the pediatric-dentistry evidence that currently answers the teeth question brand-free.

The information gain is real: across all 24 transcripts, no cited source computes that annual number or unifies the dental corpus with a brand comparison. Right now the no-sugar question gets resolved through Target category pages and Flintstones' own product page. A data-dense page gives every listicle, dietitian blog, and answer engine a reason to cite Hiya on the exact question it was built to win, and it's briefable tomorrow.

One line of scope-honesty: this teardown judges visibility, not vitamins. Every nutritional claim above ("15+ nutrients," "zero sugar") is the brand's or the cited reviewers' claim, reported as what the answer surfaces say, not endorsed.

This is the audit I run weekly on one funded health or performance brand. It takes a brand name and a week.

---

## Receipts

**Run metadata.** Date: 2026-07-15. Operator surfaces: Tavily Search API with generated answer (`include_answer: advanced`, 14 calls, raw JSON transcripts retained), WebSearch Google-proxy (10 scored runs + 2 verification searches). Perplexity API attempted first (4 calls): all returned `401 insufficient_quota`; no Perplexity data is used or implied anywhere above. ChatGPT and Gemini: not queried, not claimed. Tavily repeat runs (Q3, Q6, Q8) returned byte-identical answers, indicating caching; effective answer variance is undersampled and mention rates are computed per unique question, not per run.

**The 10 money questions (type · answer-engine runs · Google-proxy runs):**

| # | Type | Question | Tavily | Google |
|---|---|---|---|---|
| Q1 | Head | What is the best kids multivitamin without added sugar? | 2 | 1 |
| Q2 | Head | What are the best children's vitamins in 2026? | 1 | 1 |
| Q3 | Shoulder | What's the best daily multivitamin for a picky eater toddler? | 2 | 1 |
| Q4 | Shoulder | Best chewable kids vitamin that isn't a gummy and has no added sugar? | 1 | 1 |
| Q5 | Shoulder | What's the best kids protein powder without artificial sweeteners? | 1 | 1 |
| Q6 | Tail | My 6 year old refuses vegetables and mostly eats pasta and chicken nuggets. Which daily multivitamin actually fills the nutrition gaps without loading him up with sugar? | 2 | 1 |
| Q7 | Tail | Which kids multivitamin is best for a 4 year old with a dairy allergy who won't take gummies and already has two cavities? | 1 | 1 |
| Q8 | Follow-up | Hiya vs Ritual kids multivitamin, which one is better? | 2 | 1 |
| Q9 | Follow-up | Are chewable vitamins better than gummy vitamins for kids' teeth? | 1 | 1 |
| Q10 | Follow-up | Does my kid actually need a multivitamin if they eat a fairly balanced diet? | 1 | 1 |

**Per-question outcomes (answer engine → Google-proxy):**

- Q1: Flintstones Sugar-Free recommended, Hiya absent (both runs) → Google digest names Hiya first; hiyahealth.com ranked #2
- Q2: Hiya named overall best, then SmartyPants, Zarbee's, Wellements, MaryRuth's, Renzo's, Olly → digest: Hiya winner, EllaOla, First Day, SmartyPants, Baby Blues, Llama Naturals
- Q3: Renzo's Picky Eater Multi, sole brand (both runs) → Renzo's first, Hiya second, Zarbee's, Llama Naturals
- Q4: Dr. Berg chewable via shop.app/Amazon retail corpus → Hiya top of digest; hiyahealth.com ranked #3
- Q5: Healthy Heights; Hiya absent → Transparent Labs, Ora, Else, Healthy Heights; Hiya absent
- Q6: Hiya first, Renzo's second (both runs) → Tallori first, Hiya second; hiyahealth.com ranked #7
- Q7: Renzo's plus separate calcium citrate → EllaOla-dominated (allergen angle); Hiya absent both
- Q8: Hiya favored over Ritual (both runs); hiyahealth.com cited at source position 5 → digest favors Hiya for picky eaters, Ritual for moderate dosing
- Q9: no brands; pediatric dentist blogs (Bright Smiles, Sunshine Smiles, Tufts, Cleveland Clinic) → same corpus, zero brands
- Q10: no brands; AAP/Mayo/UPMC-class institutional corpus → same, plus Cleveland Clinic, WebMD

**Cited-source taxonomy (Smith classes, observed across all transcripts):** Owned: hiyahealth.com, renzosvitamins.com, flintstonesvitamins.com, ellaola.com. Earned: healthline.com, health.yahoo.com, innerbody.com, thecustomerdigest.com, therealfooddietitians.com, keatleymnt.com, thebump.com, thegoodtrade.com, health.usnews.com, sarahremmer.com, pediatric dentistry blogs. Paid-Affiliate: forbes.com/health, pickyeaterblog.com, an amzn.to affiliate short-link cited directly on Q4. Retail/UGC: target.com, amazon.com, shop.app, vitaminshoppe.com, youtube.com, reddit.com.

**Claim ledger:**

| Claim | Label | Source |
|---|---|---|
| USANA acquired 78.8% of Hiya for $205M cash, closed 2024-12-23 | VERIFIED | USANA IR press release (ir.usana.com); Nutraceuticals World |
| Hiya founded 2019 (Darren Litt, Adam Gillman); sugar-free non-gummy chewable kids multivitamin, DTC subscription | VERIFIED | uschamber.com/co; pulse2.com; hiyahealth.com |
| Hiya net sales ~$103M TTM through 2024-09-30 | VERIFIED | USANA IR press release |
| Hiya launched Kids Daily Growth + Protein (ages 2-12) May 2026 | VERIFIED | BusinessWire 2026-05-21; hiyahealth.com/products/kids-daily-protein |
| Answer engine recommended Flintstones, not Hiya, for the no-added-sugar head query (2/2 runs) | VERIFIED | Q1 transcripts |
| hiyahealth.com ranked #2 (Q1) and #3 (Q4) on Google-proxy | VERIFIED | WebSearch results 2026-07-15 |
| Hiya named first on Q2, Q6, Q8 answer-engine runs | VERIFIED | transcripts |
| Hiya absent from Q1, Q3, Q4, Q5, Q7 answer-engine answers | VERIFIED | transcripts |
| Q9/Q10 answered with zero brand mentions | VERIFIED | transcripts |
| All Mention Rate / Avg Position / QA-SOV figures | VERIFIED (computed) | tables above, raw transcripts on file |
| Perplexity API quota-dead at run time (4/4 calls, 401) | VERIFIED | API error responses |
| Tavily repeat runs byte-identical (caching) | VERIFIED | Q3/Q6/Q8 run pairs |
| Hiya took no venture capital; self-funded plus small friends-and-family round | LIKELY | founder interviews (Entrepreneur, US Chamber CO—); single-source class |
| "Zero sugar" is central to Hiya's brand positioning | LIKELY | hiyahealth.com copy + press coverage; "central" is inference |
| No source cited in these transcripts publishes an annual cumulative sugar-load comparison | LIKELY | absence verified only within the 24 collected transcripts, not globally |
| Renzo's picky-eater wins are driven partly by exact-match product naming | LIKELY | inference from Q3/Q7 transcripts |
| Hiya's retargeting spend/intensity | UNCONFIRMED | operator anecdote (the spark); no spend data used |
| Whether ChatGPT/Gemini mirror these patterns | UNCONFIRMED | not queried; excluded from all findings |

**Product-efficacy note:** nothing in this document evaluates whether any brand's vitamins work or are safe. Nutrient counts and "zero sugar" descriptions are the brands' and reviewers' claims as they appear in the transcripts.
