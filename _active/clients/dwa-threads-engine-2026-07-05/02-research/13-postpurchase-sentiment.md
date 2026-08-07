# Post-Purchase Sentiment Map — DWA / MRR Category
Source: Reddit digests captured 2026-07-05 (`reddit-dwa.txt`, 50 items; `reddit-mrr.txt`, 40 items). Trustpilot digest returned effectively empty (1 line, no content) — **treat as UNMEASURED**, not as "no complaints found." Do not cite Trustpilot sentiment anywhere downstream.

Data-quality note on `reddit-mrr.txt`: of 40 items, only the final thread (r/antiMLM, "Master Resell Rights," 2023-09-30, 6 comments) is genuinely on-topic. The rest is off-target scrape noise (Pokemon card threads, an inflation comic, a bakery AITA post) — excluded from this analysis. Effective sample is `reddit-dwa.txt` (50 items, 4 threads) + the 1 on-topic `reddit-mrr.txt` thread = 5 threads total, all Reddit, no first-party buyer reviews from a review platform. This is a real limitation: what follows is bystander/skeptic-heavy sentiment, not a representative sample of actual purchasers.

---

## 1. Overall Sentiment

Split and polarized, but the split is **not** happy-customer vs. angry-customer. It's **outside skeptics calling it a scam/pyramid** vs. **a small number of buyers defending it as legitimately useful** — with almost nobody in between and almost no discussion of the actual post-purchase experience (support, refunds, "does it still work six months later").

- Skeptic/scam threads (r/Scams, r/MLMHorrorStories, r/antiMLM — 3 of 5 threads) are the loudest and most upvoted-feeling in tone (piling-on comments, jokes, "pyramid scheme for sure").
- Buyer/curious threads (r/DigitalMarketing, r/AskMarketing) are calmer, more mixed, and contain the only real testimonials.
- **Nobody in the sample raises refund problems, support non-responsiveness, or "is this still working in 2026" directly.** That's a genuine data gap, not a clean bill of health — see Section 6.

## 2. Top Complaints (verbatim-grounded)

1. **"There's no product" / pure resell-the-course-to-sell-the-course structure.**
   - r/antiMLM, u/RunnyDischarge (`reddit-mrr.txt`): *"There is no product, it's pretty much a pure pyramid scheme. You're buying a script that tells you how to sell that script to the next sucker, and that's it."*
   - r/antiMLM, u/TheGodDMBatman (`reddit-dwa.txt`): *"So you pay $500 to 'learn' how to resell the course to other people. Those people then 'learn' how to resell that same course."*

2. **Math doesn't add up on the promised returns.**
   - r/MLMHorrorStories thread title itself: *"Digital Wealth Academy Math Ain't Mathing"* — u/plumbusmaker911: *"According to this Rep, you only need [5] sales of $100 to make 180k. It costs $500 to start."* Immediate replies: *"Anything that claims you can build multiple revenue streams and work from anywhere is definitely a pyramid scheme"* and *"Pyramid scheme for sure."*

3. **Unverifiable/incomplete course consumption by resellers.**
   - u/TheGodDMBatman: the acquaintance *"went live on their social media to explain their 'business'. They screen shared what the course looks like and immediately you can see that this person didn't complete a single course; it was all incomplete."* — a direct, specific credibility hit: people are reselling something they never finished.

4. **Earnings claims treated as inherently suspicious / used defensively when questioned.**
   - r/antiMLM, u/Puzzleheaded-Fix8182 (`reddit-mrr.txt`): sibling claims *"$20k months"* with no visible product; *"They got defensive when I said I couldn't see the product... I got called a wage slave."*

5. **Buyers themselves admit the free-information objection.**
   - Original poster in r/AskMarketing: *"I know Google and YouTube are free... I don't want to do that"* — i.e., even people leaning toward buying know the content is likely freely available elsewhere and are paying for packaging/handholding, not proprietary information. This is an implicit complaint about value-for-price even before purchase.

6. **"Have you actually sold anything?" — social proof gap surfaces inside the community itself.**
   - u/SpecificPut8961 presses u/Then_City_3364: *"how many times have you actually successfully sold the $497 course? And how?"* Reply: *"i havent sold that one yet"* — the buyer testifying positively about the course has not actually replicated the income claim it's built around.

## 3. Genuine Trust Signals (real, not manufactured)

Thin but present — worth naming precisely because the frame requires being honest about what's actually there:

- **Multiple independent buyers report real (if modest/unquantified) behavior change**, not just hype: u/Then_City_3364 (`reddit-dwa.txt`): *"once i got into this course everything changed, i am making income from tiktok shop, ugc/brand deals, selling courses and also my youtube channel has increased in views."* Later, to a direct follow-up: *"it has been really helpful to me, i have learn alot."*
- u/sarahgaines94 (`reddit-dwa.txt`, r/antiMLM — notable because it's a positive testimonial posted *inside a skeptic subreddit*, which raises its credibility slightly): *"I have DWA and love it. I've created a few different streams of income from it. I've also sold it a handful of times to other moms who wanted to start different income streams."*
- A marketer who explicitly bought DWA for **competitive research, not hype** gives a measured, non-hostile review — u/WayRevolutionary1 (`reddit-dwa.txt`): *"Most of these folks do make their money selling the course itself, not necessarily from what the course teaches... Whether something like [DWA] works for you depends on [1] your current skillset, [2] how clear you are on what business model you're actually trying to build, and [3] your tolerance for boring, behind-the-scenes work like market research, messaging, and testing content."* This is the single most credible line in the whole dataset — a non-buyer-hype, non-hater voice naming the real variable (behavior/consistency, not the course).
- Same commenter, follow-up: *"I actually love the creator"* while still critiquing the product's depth gap — sentiment toward the *person* fronting the product can be positive even when the *mechanism* (resell rights) draws skepticism.

## 4. Post-Purchase Anxiety Themes (the recurring fears, ranked)

1. **"Is this a scam / pyramid, and will I be the one left holding a course nobody wants to buy from me?"** — dominant theme, present in 3 of 5 threads unprompted.
2. **"Will the person who sold me this actually help me, or ghost me once I've paid?"** — implied, not stated outright anywhere in the sample. Nobody asks this directly, but it's the shadow behind every "is it worth it" thread — Section 6 flags this as the biggest data gap.
3. **"Everyone selling it seems to be reselling, not actually doing the underlying work"** (TikTok Shop, UGC, etc.) — u/Then_City_3364 admits *"i dont have my own course yet"* despite promoting reselling; this is the anxiety that the whole category is hollow, self-referential income.
4. **"Am I buying information I could get for free?"** — stated directly by the original r/AskMarketing poster.
5. **"If I question it, will I get gaslit / called negative / 'wage slave'?"** — the antiMLM sibling story shows defensiveness as the buyer's first response to scrutiny, which reads to bystanders as evasiveness, not confidence.
6. **Family-protection anxiety (secondary but recurring)** — two separate threads are literally "how do I warn my mom/sibling," meaning a chunk of the discourse isn't buyer sentiment at all, it's third-party alarm. This matters for content: the audience includes people trying to talk someone OUT of these purchases, and content that reads as "another MRR pitch" will get lumped in and dismissed by that audience before it's read.

## 5. Proof Opportunities for Farrice (pre-empt the anxiety, don't argue with it)

Each maps a real anxiety above to a concrete, compliant proof mechanic Farrice can run because he is a credentialed S&C/behavior-change coach, not a reseller of someone else's info-product.

| Anxiety (from data) | Proof mechanic Farrice can own |
|---|---|
| "No real product, just a script to sell the script" | Show the actual mechanism/system (his final-10%/90%-pattern framework, `_active/farrice-brand/farrice-final-10/strategy/offer-the-final-10.md`) in public — screen-recorded working sessions, not slides. Visible methodology kills the "no product" read instantly. |
| "The math doesn't add up on income claims" | Never state income numbers (compliance rule anyway). Instead prove the *behavioral* mechanism with before/after adherence data — attendance streaks, week-2 dropout rates he's reversed, client-reported consistency — outcomes he can actually substantiate without earnings claims. |
| "Will anyone answer me after I buy?" (the anxiety nobody states but everyone implies) | This is Farrice's single biggest structural edge over the DWA category: he is one person, reachable, coaching in real time. Content should show him *actually responding* — DM screenshots (with permission), office-hours clips, "here's me answering someone's stuck-at-week-2 message live." Responsiveness-as-proof, filmed, is the direct antidote and nobody in this category is doing it. |
| "Resellers haven't finished/don't use their own course" | Farrice should visibly use his own system on himself or his own household (stay-at-home-dad life, his own training log) — the extraction/credibility hit that killed the acquaintance in the antiMLM story (caught not having finished the course) becomes a strength if Farrice shows completed, lived proof. |
| "Buying info I could get free on YouTube" | Reframe: the value was never information, it's follow-through under real constraints (the 90% pattern). Content should explicitly acknowledge "you already know what to do" — validates the objection instead of denying it, then pivots to the actual gap (execution, not knowledge). This directly matches the u/WayRevolutionary1 insight above — skillset/clarity/tolerance-for-boring-work is the real variable, and that's Farrice's exact lane. |
| "Defensive/evasive when questioned" fear | Do the opposite on purpose: publicly answer hard/skeptical questions (screenshot real DMs asking "does this actually work," respond calmly, no recruitment pitch). Visible non-defensiveness is rare enough in this category to be a differentiator on its own. |
| Family-protection audience (people trying to warn relatives off MRR) | This audience will trust an anti-guru who explicitly criticizes the pyramid-resell model by name in content — positions Farrice as the person your skeptical brother-in-law would actually respect, expanding reach into people currently hostile to the whole category. |

## 6. Data Gaps — Be Explicit

- **Trustpilot: UNMEASURED.** The digest came back as a single empty line — no reviews, no star ratings, no support-complaint text. Any claim about Trustpilot sentiment in downstream content would be fabricated. If refund/support proof points are needed, they must come from a fresh, successfully-scraped source, not this run.
- **No first-party refund or support-ticket sentiment anywhere in Reddit sample.** The dominant anxieties documented above ("will anyone answer me," "is there a refund path") are *inferred* from category-level skepticism and the structure of the complaints, not from anyone directly reporting a bad refund/support experience. Flag any content claim like "buyers report being ghosted" as UNCONFIRMED — the data does not contain a direct quote to that effect.
- **`reddit-mrr.txt` is 90% off-topic scrape noise** (Pokemon TCG, an inflation comic, a bakery dispute) — only 1 of 4 threads is usable. This should be flagged to whoever owns the scrape pipeline; the query likely matched "MRR" as an unrelated acronym collision.
- **Sample size is small and Reddit-only** (5 usable threads, ~35 usable comments). No TikTok or YouTube comment data despite those being named as intended sources — this analysis is Reddit-only by what was actually present in the digests provided, not the full multi-platform picture the brief implies.
- **No longitudinal ("is it still working now / 6 months later") complaints found.** This specific anxiety named in the task brief did not surface in the sample — worth a targeted follow-up scrape (e.g., search "Digital Wealth Academy 2026 update" or similar) before building content that claims to address it directly.
