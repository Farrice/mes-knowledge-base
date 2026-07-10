# DWA — Competitor Conversion Analysis: Does Honest/Credentialed Content Get Reach?

_Sources: `../intel/v2/digests/competitor-candidates-v2.txt` (31 handles), `../intel/v2/digests/tiktok-affiliate.txt` (60 vids), `../intel/v2/digests/tiktok-makemoney.txt` (60 vids), captured 2026-07-05. Prior: `11-competitor-inventory.md`. Plus 2 live Instagram scrapes run this session: `../intel/v2/ig-callmekevy.json`, `../intel/v2/ig-abbyxconway.json`._

**Platform caveat, stated up front and binding on every conclusion below: this is 100% TikTok + IG data. Zero Threads-native validation exists (`threads-native.txt` is empty — the Threads scrape failed, login-walled). Every finding here is cross-platform pattern evidence, not proof the same distribution holds on the platform Farrice would actually run on. Confidence ceiling: MEDIUM, capped by platform mismatch, not by sample size.**

## IG scrapes run this session (2 of 2 used)

1. **`@callmekevy`** — picked because he's the closest thing to a genuine non-hype tutorial creator in the dataset: 4 separate TikTok videos (2.17M total plays across the affiliate+makemoney sets), consistent "step-by-step, zero startup cost, free Pinterest traffic" format, no income-flex language, no drumroll reveals. Result: **`no_items` / "Empty or private data for provided input."** No usable IG presence. Second time in this intel effort a non-hype-coded TikTok handle turns out to have no scrapable cross-platform footprint (first was `@digitalmarketingexpert39` in the prior session, `not_found`). **UNCONFIRMED** whether this is a real pattern (non-hype creators in this niche don't invest in cross-platform brand-building) or coincidence — n=2 is not enough to call it, but it's directionally consistent.
2. **`@abbyxconway`** — picked because her TikTok post has the single highest like:play ratio of any high-reach handle in the dataset (18.45%, 631.5K plays, "watch this video to learn affiliate marketing... get my free guide"). Result: **12 real IG posts returned.** This is the load-bearing teardown of this session — see below.

## Does hype dominate the top of the distribution? CONFIRMED, high confidence.

Ranking both 60-video digests by plays, every single entry in the **top 10 by reach** runs one of: income-flex reveal, generic curiosity-gap hype, engagement-bait, or unrelated hashtag-stuffing. None carries a credential, a readiness screen, or a named behavior-change mechanism.

| Rank | Handle | Plays | Like% | Angle |
|---|---|---|---|---|
| 1 | @jillian_randall | 4.7M | 5.74% | Generic "get started tiday!" typo-hype, no credential |
| 2 | @alexissteinn | 4.2M | 11.93% | Joke/passive-income humor bit |
| 3 | @officialloucameron | 2.1–2.2M | 4.3–4.6% | Income-flex freedom-flex, comment/hashtag only |
| 4 | @itschelseadewlen | 1.8M | 5.68% | Generic "grab info from link in profile" |
| 5 | @callmekevy | 968K | 5.09% | Tutorial-style (closest to non-hype) but no credential, no IG footprint (see above) |
| 6 | @mandanazarghami | 856K | 0.21% | Mavely-partner "$10k+ as a beginner" — huge reach, near-zero engagement |
| 7 | @gabi.hustles | 836K | 8.31% | "20 min/day, be consistent" — simplest message in dataset, no credential |
| 8 | @coachtotty | 779.7K | 4.28% | "Will make people RICH in 2024" |
| 9 | @abbyxconway | 631.5K | 18.45% | Free-guide hook — see IG teardown below |
| 10 | @essentials_finds01 | 586.8K | 7.45% | Pure engagement-bait ("engage engage engage") |

**Zero credentialed or behavior-mechanism posts appear in either top-10.** This matches and extends the prior inventory's "`behavioral_claimed: false`" finding — it's not just that no competitor talks about behavior change, it's that the entire top of the reach distribution is structurally hype/curiosity/income-flex, and that shape holds whether you rank by total plays or by digest.

## Do honest/self-aware accounts get reach? CONFIRMED — no, they cluster at the bottom.

Every post in the dataset using explicitly anti-hype or self-effacing language sits in the bottom third to bottom decile of a 60-video, plays-ranked list:

| Handle | Plays | Like% | Honest/anti-hype signal |
|---|---|---|---|
| @steph.trenkamp | 89.4K | 1.6% | "Affiliate marketing — **the real truth** behind the business" |
| @profit.diva.nonni | 49.1K | 5.6% | "Learn real income online **without confusion or overwhelm**" |
| @thebizmomari | 24.5K | 4.7% | "You do not need experience... **this is not MLM**, no team" |
| @apple.user49626926 | 3.9K | 1.3% | "Starting from zero. **No hype. No shortcuts.** Just documenting." |
| @hollylynelleco | 1.7K | 2.6% | "I'm just a regular stay-at-home mom. **Not an influencer.** No fancy degree." |
| @akearahj | 1.6K | 9.2% | "Success didn't happen in 30, 60, 90 days. **Took a full year.**" |
| @.loganbidwell | 13K | 3.3% | `#sidehustlefordads`, realistic, no dollar claims |
| @moneymovesjake | 496–11.1K | ~4.5% | Carries visible FTC-style disclaimer ("results not typical") |

Best honest-cohort reach (`@steph.trenkamp`, 89.4K plays) is **52x smaller** than the top hype post (4.7M). And its engagement ratio (1.6%) is one of the worst in the entire 60-video set — the honesty framing isn't even winning on quality of engagement, just losing on reach. `@akearahj`'s 9.2% ratio is a bright spot but off a base of 1,603 plays — statistically meaningless at that scale.

## The `@abbyxconway` teardown: the sharpest single data point in this run

Her TikTok hook ("free affiliate guide," 18.45% like ratio — the best ratio of any high-reach handle) reads soft/helpful. Her actual IG account, the one she funnels people to, is **pure income-flex lifestyle content**:

- "screaming crying throwing up because i bought my dream car" — 5,557 likes / 42.3K views (13.1%)
- "celebrating 100k... TWICE today... made $100k in the last 30 days" — 2,061 likes (carousel)
- "how i was able to 30x my income in the past 3 years" — 1,950 likes / 13.8K views (14.1%)
- Best single post: "experiences > materials always" — 12,482 likes (carousel, lifestyle-flex, no income claim but part of the same aspirational identity)
- CTA pattern: "comment READY/finance/insurance and I'll send you..." on nearly every post — same comment-gate-to-DM mechanic as Lou Cameron

**This matters because it closes off the most tempting false hope in this whole dataset**: the single TikTok post that looked most like "honest, helpful, non-hypey content actually works here" turns out, once you follow it to the real account behind it, to be a hype-and-flex operator using a soft hook as a funnel entrance. There is no example anywhere in this two-scrape, two-digest sample of a credentialed, behavior-change-framed, non-flex account achieving real reach on either platform.

## Comment-gate-to-DM is the dominant mechanic, confirmed cross-platform

At least 10 distinct handles across the two TikTok digests plus the IG teardown use "Comment [word] and I'll DM you" as the primary CTA (`@sarasofiasocialmedia_` x4 posts, `@thebizmomari`, `@hollylynelleco`, `@romeeroelofs`, `@kathii.journey`, `@celina.luisaaaaaaaa`, `@makeitrainyb`, `@abbyxconway` on IG). This reconfirms the prior inventory's Lou Cameron finding at much higher n: comment-gate, not link-in-post, is the modal mechanic among operators with sustained reach. Worth testing on Threads rather than assuming link-in-post wins by default — but again, **zero Threads-native evidence either way.**

## Answering the two questions directly

**"Do honest/credentialed accounts actually get reach and engagement, or does income-flex hype dominate the top of the distribution?"**
Income-flex/hype dominates the top of the distribution — CONFIRMED, high confidence, from real numbers across 120 scraped videos plus one full IG teardown. Every top-10-by-reach post in both digests is hype, curiosity-gap, or engagement-bait. Every explicitly honest/anti-hype post sits in the bottom third of reach and has unremarkable-to-poor engagement ratios. The one post that looked like a counter-example (`@abbyxconway`'s free-guide hook) unwinds into pure income-flex lifestyle content on inspection.

**"Does anti-guru content CONVERT here, or does it merely exist as unclaimed space nobody's rewarded for occupying?"**
This dataset cannot answer the conversion (sales) question directly — plays/likes/comments are reach and engagement metrics, not attributed purchases, and none of these scrapes carry sales data. What it CAN answer, and does: anti-guru content is not rewarded with reach or engagement on TikTok. The honest reading, stated plainly: this is evidence for "unclaimed space nobody's rewarded for occupying," not evidence for "anti-guru secretly converts better per-viewer." Nobody in 120 videos is running the anti-guru play at scale, so there is no scaled anti-guru account to point to as proof it converts — the absence itself is the finding, and it cuts against optimism, not for it. **Label this UNCONFIRMED for conversion economics, CONFIRMED for near-zero reach/engagement reward.**

## What this adds to the GO/NO-GO calculus

This is incremental evidence, not new information about Farrice's odds specifically — it sharpens a risk the decision context already named. The confirmed-open white space (anti-guru + behavioral-change, 0 of ~15 competitors) is open partly because the mechanism (reach algorithm + audience taste on TikTok, the closest proxy we have) does not reward that content today. Occupying unclaimed space is necessary but not sufficient; this data gives no basis to assume the audience will reward it once occupied, and every honest-toned post in the sample is proof of concept for "content exists" but not for "content works." That gap is exactly what a $0-audience, 30-min/day, first-90-days operator cannot afford to bet on for a $3-5K/mo target without an actual Threads pilot. This does not by itself make DWA a NO_GO — the S&C-credential/behavior-change combination has never been tried at scale by anyone in this data, hype or honest — but it should lower confidence in the affiliate path's speed-to-revenue relative to the standalone Ship Sprint alternative, which has a real, direct behavioral pain point rather than relying on a currently-unrewarded content style to break through.

## Files
- `_active/dwa-threads-engine-2026-07-05/intel/v2/ig-callmekevy.json` — no_items (empty/private)
- `_active/dwa-threads-engine-2026-07-05/intel/v2/ig-abbyxconway.json` — 12 real posts, full captions/engagement
- `_active/dwa-threads-engine-2026-07-05/intel/v2/digests/competitor-candidates-v2.txt`
- `_active/dwa-threads-engine-2026-07-05/intel/v2/digests/tiktok-affiliate.txt`
- `_active/dwa-threads-engine-2026-07-05/intel/v2/digests/tiktok-makemoney.txt`
- `_active/dwa-threads-engine-2026-07-05/02-research/11-competitor-inventory.md` (prior session, referenced not re-derived)
