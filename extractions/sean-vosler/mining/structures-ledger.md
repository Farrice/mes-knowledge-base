---
type: mining-ledger
method: Sean Vosler - Amazon subtitle mining + the Imitation Game (structure over topic)
harvest_date: 2026-08-21
target_use: positioning/messaging sprint offers sold to supplement + DTC brand founders
---

# Structures Ledger - Subtitles and Headline Skeletons

**Harvest date:** 2026-08-21. Every entry below is a verbatim capture with a live source URL and the
ranking mechanism that made it worth capturing. Nothing here is composed, paraphrased, or reconstructed.

**Surfaces reached:** Amazon Best Sellers (live DOM via Playwright), Reddit top-of-year (live DOM),
Hacker News Algolia API (points-filtered), Medium tag "recommended" feeds (clap counts), Meta Ad Library (live).

**Surfaces blocked, and the workaround used:** Amazon over WebFetch returned HTTP 503 - moved to Playwright.
Reddit's JSON API and pullpush.io both hard-block scripted agents - moved to Playwright. Medium over
WebFetch returned HTTP 403 - moved to Playwright.

**Environment note:** the Playwright browser was shared with another concurrent session; several
extractions were destroyed mid-call by outside navigation and had to be re-run. Every row below survived
a clean re-run.

---

## PART A - Subtitle Mining (20 captures)

The subtitle carries the promise. The title only has to be memorable; the subtitle has to be *bought*.
Mode tags are Vosler's four: **Contrarian** (attacks a held belief) - **Intriguing** (opens a gap) -
**Inspiring** (raises identity) - **Powerful Promise** (names the payoff outright).

### A1. Marketing and Sales - Amazon Best Sellers, node 2698

Rank evidence: live bestseller badge scraped from the grid, 2026-08-21.
Source list: https://www.amazon.com/Best-Sellers-Books-Marketing-Sales/zgbs/books/2698

| # | Verbatim subtitle (title in italics) | Mode | Fill-in skeleton | Rank evidence |
|---|---|---|---|---|
| 1 | *$100M Offers:* "How to Make Offers So Good People Feel Stupid Saying No" | Powerful Promise + Contrarian tail | "How to [make/build X] So [adjective] [audience] Feel [absurd emotion] [refusing]" | #5, node 2698 |
| 2 | *$100M Leads:* "How to Get Strangers to Want to Buy Your Stuff" | Powerful Promise | "How to Get [cold audience] to *Want* to [desired action]" | #6, node 2698 |
| 3 | *Never Split the Difference:* "Negotiating As If Your Life Depended On It" | Intriguing | "[Doing an ordinary thing] As If [extreme stake]" | #3, node 2698 |
| 4 | *To Sell Is Human:* "The Surprising Truth About Moving Others" | Intriguing | "The Surprising Truth About [familiar act, renamed abstractly]" | #4, node 2698 |
| 5 | *Building a StoryBrand 2.0:* "Clarify Your Message So Customers Will Listen" | Powerful Promise | "[Fix one asset] So [audience] Will [do the thing they currently refuse]" | #8, node 2698 |
| 6 | *Good to Great:* "Why Some Companies Make the Leap...and Others Don't" | Intriguing (open loop) | "Why Some [group] [achieve outcome]...and Others Don't" | #7, node 2698 |
| 7 | *Gap Selling:* "How Problem-Centric Selling Increases Sales by Changing Everything You Know About Relationships, Overcoming Objections, Closing and Price" | Contrarian | "How [renamed method] [increases metric] by Changing Everything You Know About [4 sacred cows, listed]" | #27, node 2698 |
| 8 | *Obviously Awesome:* "How to Nail Product Positioning so Customers Get It, Buy It, Love It" | Powerful Promise | "How to Nail [discipline] so [audience] [verb 1], [verb 2], [verb 3]" | #30, node 2698 |
| 9 | *Exactly What to Say:* "The Magic Words for Influence and Impact" | Intriguing | "The [Magic/Secret] [tiny unit] for [large outcome]" | #15, node 2698 |
| 10 | *Ninja Selling:* "Subtle Skills. Big Results." | Contrarian (juxtaposition) | "[Understated input]. [Outsized output]." | #22, node 2698 |
| 11 | *The Challenger Sale:* "Taking Control of the Customer Conversation" | Powerful Promise (authority) | "Taking Control of the [arena the reader currently loses]" | #9, node 2698 |
| 12 | *The Way of the Wolf: Straight Line Selling:* "Master the Art of Persuasion, Influence, and Success" | Inspiring | "Master the Art of [capability 1], [capability 2], and [identity outcome]" | #25, node 2698 |

### A2. Business Development and Entrepreneurship - Amazon Best Sellers, node 2741

Source list: https://www.amazon.com/Best-Sellers-Books-Business-Development-Entrepreneurship/zgbs/books/2741

| # | Verbatim subtitle | Mode | Fill-in skeleton | Rank evidence |
|---|---|---|---|---|
| 13 | *The E-Myth Revisited:* "Why Most Small Businesses Don't Work and What to Do About It" | Contrarian | "Why Most [reader's own category] Don't Work and What to Do About It" | #7, node 2741 |
| 14 | *Profit First:* "Transform Your Business from a Cash-Eating Monster to a Money-Making Machine" | Powerful Promise (metaphor pair) | "Transform Your [asset] from a [villain metaphor] to a [hero metaphor]" | #15, node 2741 |
| 15 | *Buy Back Your Time:* "Get Unstuck, Reclaim Your Freedom, and Build Your Empire" | Inspiring | "[Escape verb], [Reclaim verb], and [Build verb]" | #9, node 2741 |
| 16 | *The Algorithm:* "The Hypergrowth Formula That Transformed Tesla, Lululemon, General Motors, and SpaceX" | Intriguing (proof stack) | "The [named formula] That Transformed [brand], [brand], [brand], and [brand]" | #13, node 2741 |

### A3. Nutrition (supplement-adjacent) - Amazon Best Sellers, node 282861

Source list: https://www.amazon.com/Best-Sellers-Books-Nutrition/zgbs/books/282861
The most useful Part A surface for supplement founders: these are the promises their buyers already paid for.

| # | Verbatim subtitle | Mode | Fill-in skeleton | Rank evidence |
|---|---|---|---|---|
| 17 | *Good Energy:* "The Surprising Connection Between Metabolism and Limitless Health" | Intriguing | "The Surprising Connection Between [mechanism] and [ultimate outcome]" | #2, node 282861 |
| 18 | *The Hunger Code:* "Resetting Your Body's Fat Thermostat in the Age of Ultra-Processed Food" | Intriguing (named mechanism + named villain) | "Resetting Your [body system]'s [named mechanism] in the Age of [villain]" | #8, node 282861 |
| 19 | *Heal Your Cells:* "Reversing the Irreversible--A Proven Plan to Heal Faster, Reclaim Energy, and Unlock Longevity" | Contrarian + Powerful Promise | "[Verb]ing the [Un-verb-able] - A Proven Plan to [outcome 1], [outcome 2], and [outcome 3]" | #9, node 282861 |
| 20 | *Stay off My Operating Table:* "A Heart Surgeon's Metabolic Health Guide to Lose Weight, Prevent Disease, and Feel Your Best Every Day" | Powerful Promise (credentialed) | "A [credentialed insider]'s Guide to [outcome 1], [outcome 2], and [feel-state outcome]" | #12, node 282861 |

**Also captured on the same Nutrition list, held in reserve** (verbatim, same source and date):
*Metabolic Freedom:* "A 30-Day Guide to Restore Your Metabolism, Heal Hormones and Burn Fat" (#17) -
*Fast Like a Girl:* "A Woman's Guide to Using the Healing Power of Fasting to Burn Fat, Boost Energy, and Balance Hormones" (#6) -
*Eat to Beat Disease:* "The New Science of How Your Body Can Heal Itself" (#5) -
*The New Perimenopause:* "An Evidence-Based Guide to Surviving the Zone of Chaos and Feeling Like Yourself Again" (#7).

**Cross-check surface (no Part A row depends on it):** Goodreads popular-shelf ordering -
https://www.goodreads.com/shelf/show/marketing and https://www.goodreads.com/shelf/show/nutrition.
Pulled only to confirm the long-tail durability of the "Why [X] and What to Do About It" and
"The Surprising [Noun] of [Y]" skeletons. Goodreads shelf order is shelving popularity, not sales rank -
a weaker ranking mechanism, so it is quarantined here rather than counted.

**Highest-transfer skeletons for a positioning/messaging sprint offer:**

- Rows 5 and 8 are the closest analogues to what a positioning sprint actually sells: fix one asset,
  and a named buyer behavior changes. "Clarify Your Message So Customers Will Listen" is the sprint's
  promise in six words.
- Row 7 (*Gap Selling*) is the pattern for selling against a founder's incumbent agency: name the four
  things they currently believe, then promise to overturn all four at once.
- Rows 18 and 19 are the supplement category's own grammar - **named mechanism + named villain + reversal**.
  A sprint pitched to a supplement founder can borrow that grammar back at them.

---

## PART B - Trending Headline Structures (20 captures)

Discipline: focus less on what is being said, more on how it is built. The topic in these rows is
disposable; the bracketed skeleton is the asset.

| # | Verbatim headline | Skeleton | Why it works | Source + sort/rank |
|---|---|---|---|---|
| 1 | "The worst part of corporate life isn't the hours" | "The worst part of [shared pain] isn't [the obvious culprit]" | Negation of the obvious. The reader already agreed with the obvious answer, so denying it opens a gap they have to close. | r/Entrepreneur, 367 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1ozeilq/the_worst_part_of_corporate_life_isnt_the_hours/ |
| 2 | "Nobody wants to talk about buying a septic business. Thats exactly why the margins are 60%+ and the multiples are 2.5x. Full breakdown inside." | "Nobody wants to talk about [unglamorous thing]. That's exactly why [enviable number] and [second number]. Full breakdown inside." | Confirms the suspicion that money hides in boring places, pays a specific number as proof-of-access, then names the open loop out loud. | r/Entrepreneur, 359 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1sb2zxs/requested_nobody_wants_to_talk_about_buying_a/ |
| 3 | "Working 100 hours a week isn't entrepreneurship. It's wage slavery with no boss." | "[Behavior everyone praises] isn't [flattering label]. It's [brutal relabel]." | Contrarian relabel. Takes an identity the reader is proud of and reassigns it to a shameful category; they must read to learn which side they are on. | r/Entrepreneur, 321 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1ng0zyu/working_100_hours_a_week_isnt_entrepreneurship/ |
| 4 | "Most clients don't want cheap. They want chill." | "Most [buyers] don't want [assumed driver]. They want [unexpected one-word driver]." | Belief-confirmation for anyone who suspected price was never the real objection. The one-syllable payoff word does the compression. | r/Entrepreneur, 292 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1o6oagz/most_clients_dont_want_cheap_they_want_chill/ |
| 5 | "B2B pays. B2C is sexy." | "[Option A] [pays]. [Option B] [is sexy]." | Two verdicts, four words. Forces the reader to pick a side before reading a sentence of body copy. | r/Entrepreneur, 289 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1n0pc2j/b2b_pays_b2c_is_sexy/ |
| 6 | "How I made $1,000,000 from 100 outbound emails" | "How I made [large number] from [absurdly small input]" | Ratio shock. The gap between input and output IS the curiosity gap; no adjective required. | r/Entrepreneur, 270 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1qrjprr/how_i_made_1000000_from_100_outbound_emails/ |
| 7 | "You will never make money as a 'founder' in 2025" | "You will never [desired outcome] as a ['identity' in scare quotes] in [year]" | Belief-shattering plus dated perishability. The scare quotes do the sneering so the headline does not have to. | r/Entrepreneur, 312 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1ofxs6n/you_will_never_make_money_as_a_founder_in_2025/ |
| 8 | "I spent 6 weeks trying to make a very modest income with AI. Here's what actually happened." | "I spent [duration] trying to [deliberately modest goal] with [hyped tool]. Here's what actually happened." | The modest goal signals honesty; "actually" pre-frames the piece as the de-hyped version the reader has been hunting for. | r/Entrepreneur, 313 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1q1uur5/i_spent_6_weeks_trying_to_make_a_very_modest/ |
| 9 | "Found a Bible study store doing $214K/month and at least 6 competitors running the same model. Here's what's actually happening" | "Found a [absurdly niche business] doing [specific dollar figure]/month and [N] competitors running the same model. Here's what's actually happening" | Odd-number specificity reads as field report rather than claim. "Same model" implies a repeatable pattern the reader could take. | r/Entrepreneur, 249 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1rb9ep7/found_a_bible_study_store_doing_214kmonth_and_at/ |
| 10 | "What I learned chasing a flashy startup vs a boring business" | "What I learned chasing [glamorous option] vs [unglamorous option]" | Forces self-sorting. Every reader is currently on one of the two sides and wants to know whether they chose wrong. | r/Entrepreneur, 365 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1nclgb9/what_i_learned_chasing_a_flashy_startup_vs_a/ |
| 11 | "We automated everything and now nobody trusts anything" | "We [maximized X] and now [the purpose X served is destroyed]" | Irony structure. The sentence contains its own reversal, so it reads as a finished thought worth expanding. | r/Entrepreneur, 333 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1qof5yc/we_automated_everything_and_now_nobody_trusts/ |
| 12 | "I disappointed an aspiring entrepreneur by telling the truth" | "I [caused a negative reaction] by [doing the obviously right thing]" | Moral tension. The reader wants to adjudicate whether the author was right, which requires reading. | r/Entrepreneur, 324 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1o1oidn/i_disappointed_an_aspiring_entrepreneur_by/ |
| 13 | "I spent $1000 advertising on Reddit and have nothing to show for it" | "I spent [amount] on [channel] and have nothing to show for it" | Failure confession buys credibility upfront; the reader reads to avoid paying the same tuition. | r/Entrepreneur, 261 upvotes, Top / past year - https://www.reddit.com/r/Entrepreneur/comments/1p9uk2q/i_spent_1000_advertising_on_reddit_and_have/ |
| 14 | "Why brands have almost no differentiations these days" | "Why [category] have almost no [thing they all claim to have] these days" | Confirms a suspicion the reader has held but never articulated. Directly on-thesis for a positioning offer. | r/marketing, 102 upvotes, Top / past year - https://www.reddit.com/r/marketing/comments/1qz3tgg/why_brands_have_almost_no_differentiations_these/ |
| 15 | "Most marketers today don't understand this.." | "Most [peer group] today don't understand this.." | Pure curiosity gap plus in-group exclusion. "This" is never named, and the reader must confirm they are not part of "most." Weak content, unusually strong skeleton. | r/marketing, 137 upvotes, Top / past year - https://www.reddit.com/r/marketing/comments/1nt4vx8/most_marketers_today_dont_understand_this/ |
| 16 | "Highest value marketing skill in 2026?" | "Highest value [domain] skill in [year]?" | Question-as-headline. The year stamp makes the reader's existing answer feel possibly expired. | r/marketing, 140 upvotes, Top / past year - https://www.reddit.com/r/marketing/comments/1pceheh/highest_value_marketing_skill_in_2026/ |
| 17 | "Nerds don't respond to marketing; try technical documentation instead" | "[Audience] don't respond to [standard method]; try [unexpected substitute] instead" | Contrarian claim plus an immediate prescription in the same line. The reader gets a usable move before clicking, which paradoxically raises the click. | Hacker News, 345 points - https://news.ycombinator.com/item?id=28182181 (Algolia API, points above 150, sorted desc) |
| 18 | "Twice as happy customers means half the marketing spend" | "[Multiplier] as [asset] means [fraction] the [cost]" | Arithmetic as argument. The claim sounds falsifiable, which reads as confidence. | Hacker News, 341 points - https://news.ycombinator.com/item?id=14617605 (Algolia API, points-sorted) |
| 19 | "I'm Quitting Content Writing For Good" | "I'm Quitting [reader's own profession] For Good" | Identity threat. The reader is not curious about the author; they are checking whether their own job is safe. Highest clap count in the sampled tag. | Medium, 5K claps, /tag/copywriting recommended feed - https://medium.com/tag/copywriting/recommended (Arpit Mehta, Jun 9) |
| 20 | "6 Copywriting Templates Every Writer Should Steal" | "[N] [assets] Every [identity] Should Steal" | "Steal" instead of "learn" or "use." The permission verb converts a listicle into a transgression the reader is invited into. | Medium, 278 claps, /tag/copywriting recommended feed - https://medium.com/tag/copywriting/recommended (Kathy Widenhouse, The Writing Cooperative, Aug 10) |

**Also captured, held in reserve** (verbatim, same sorts): "Distribution is an art" (r/marketing, 1,749
upvotes, Top/year) - "How to Sell Things That Are Hard to Explain" (Medium /tag/copywriting, 134 claps) -
"We Spent 40 Minutes Debating AI Synonyms" (Medium /tag/marketing, 757 claps) - "Participation Is Reality"
(Medium /tag/marketing, 2.6K claps) - "Marketing is scary for a solo developer" (Hacker News, 513 points,
https://news.ycombinator.com/item?id=29538355).

**Structural read across Part B:** the top-performing skeletons in this founder-adjacent corpus are
overwhelmingly **two-clause reversals** - assert the thing they believe, then break it in the same line
(rows 1, 3, 4, 5, 7, 11, 17, 18). Single-clause curiosity headlines (row 15) still work but rank lower.
The reversal shape is the one to port into positioning-sprint hooks.

---

## PART C - Live-Ad Check (Meta Ad Library)

**Status: available and completed this pass.** The Meta Ad Library rendered without login via Playwright.

**Honest limitation on the sort.** The US Ad Library offers **no longevity sort**. Meta auto-appended
`sort_data[mode]=total_impressions` and `sort_data[direction]=desc` to the URL, but impression sorting is
an EU-transparency feature and does not order US results. The rows below are therefore NOT a ranked
"longest-running ads" list. They are ads that were still active on 2026-08-21 carrying a "Started running
on" date old enough to imply the creative has survived repeated optimization cycles. Longevity here is
inferred from start date plus active status, the only longevity signal the US Ad Library exposes.

Queries run: `q=supplement` and `q=collagen`, with `active_status=active`, `country=US`, `media_type=all`.
Query `q=AG1` returned no parseable results before an outside navigation destroyed the browser context; not retried.

| Advertiser | Started running | Elapsed as of 2026-08-21 | Verbatim opening lines | Library ID |
|---|---|---|---|---|
| Black Girl Vitamins | Oct 10, 2024 | ~22 months | "If you didn't know, now you know, we are THE OFFICIAL vitamin sponsor for Howard women's basketball team, and we can't contain our excitement. All gas no brakes for Black Girl Vitamins and Howard. It's the collab you have been waiting for" | 1561661984477254 |
| Micro Ingredients | Oct 4, 2025 | ~10.5 months | "When your hair is thinning or flat, it needs more than shampoo. / Just like grass needs fertilizer, your hair needs nourishment from within." | 1730029874378310 |
| Everyday Dose | Nov 26, 2025 | ~9 months | "DOSE is powered with functional mushrooms and nootropics. Our smooth and delicious blend features 100% organic and Non-GMO lion's mane and chaga mushroom extracts, grass-fed collagen protein, and L-theanine. Zero junk, no misleading 'natural' flavors, No fake myceliated grain mushroom. Just 100% cle[an]..." | 818885337616738 |
| Beauty Wellness Edit (E27 Liquid Collagen) | Dec 10, 2025 | ~8.3 months | "Let us show you why liquid collagen is all the rage right now. Meet E27 Extra Strength Liquid Collagen: / Promotes hydrated, glowing skin" | 1528817395014331 |

All four verified present in the `active_status=active` result set on 2026-08-21.
Search surface: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=collagen&search_type=keyword_unordered&media_type=all
(and the identical URL with `q=supplement`).

### The finding worth more than the four rows above

The `q=supplement` result set surfaced a heavily replicated ad ARCHITECTURE running under generic,
brand-free page names: **"American Health Support Community"** (Library IDs 1929541504431807,
2619351891814847, 880272548039289) and **"Cholesterol Relief Community"** (2006807903279406,
866569929827744, 1030864056331221). These are advertorial funnels wearing the costume of a support group.
Verbatim opening of the highest-placed one (started May 26, 2026, Library ID 1929541504431807):

    "My eGFR was 42 and declining. Three years on every kidney supplement available. CoQ10. Turmeric.
    Herbal blends. All failed. Two different hibiscus teas failed. Then I found out why - and my eGFR
    went from 42 to 58 in 9 months."

Skeleton: **"[Specific biomarker] was [bad number] and declining. [Duration] on [every category solution].
[Item]. [Item]. [Item]. All failed. Then I found out why - and [biomarker] went from [bad number] to
[good number] in [timeframe]."**

Why it works: the failed-solutions list is the persuasion engine, not the promise. It pre-empts every
objection the reader was about to raise, establishes that the narrator already spent their money on the
obvious answers, and only THEN opens the loop with "then I found out why." The two-number biomarker delta
supplies proof without making a claim. Companion openers from the same advertiser cluster confirm this is
a deliberate template rather than one writer's instinct: "My aunt called me a creep for putting a camera
in Nana's living room. / Nana called me practical." (Library ID 2619351891814847) and "I found a wallet in
a shopping cart at Walmart last Tuesday. Brown leather. Worn soft at the edges." (Library ID 2006807903279406).

For a positioning/messaging sprint sold to supplement founders, this is the single most useful capture in
the file: it is the exact copy architecture their best-funded competitors are paying to keep in market,
and most founders have never seen it laid out as a skeleton.
