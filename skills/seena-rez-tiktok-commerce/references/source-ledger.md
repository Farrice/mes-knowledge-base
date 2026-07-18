# Source Ledger — seena-rez-tiktok-commerce

Claim-by-claim provenance. Ground truth = YouTube transcripts of Seena Rez's
own videos, recovered from `_archive/claude-export-2026-07-01.tar.gz`
(no `extractions/seena*` or `extractions/*rez*` directory exists — this
skill was never re-verified against its original extraction conversations
until this repair pass). Full anchor→location table: `PROVENANCE.md`
(sibling file, this batch's output dir).

## Primary Sources (VERIFIED to exist and to contain the quoted text)

| # | Source | Type | Date (conversation) | Archive location | Size |
|---|--------|------|----------------------|-------------------|------|
| S1 | "💎💎💎 Seena Rez \| $49,140 tiktok dropshipping in 7 days from scratch (showing you my entire process)" — YouTube: https://www.youtube.com/watch?v=eF59p8zhbLM | YouTube transcript, extracted via Merlin AI into a Claude.ai extraction conversation | 2026-01-05 | `claude-export/normalized/conversations/aa769dc9-d497-4189-9400-5cf55a42b865.md` | 66,330 bytes (`wc -c`) |
| S2 | "💎💎💎 Seena Rez \| $1.8m tiktok dropshipping in 30 days (showing you my actual viral videos and how to create them)" — YouTube: https://www.youtube.com/watch?v=cZ-Gsow_ULo | YouTube transcript, same extraction pipeline | 2026-01-05 | `claude-export/normalized/conversations/b6ee8a13-8ddc-4130-ba5d-8471c4b8b5c7.md` | 51,625 bytes (`wc -c`) |
| S3 | "Fresh & Seena Rez \| how I built a $2.7M brand using a.i (my actual product, website, ads, viral videos) \| Market Fit & Research Mastery" — YouTube: https://www.youtube.com/watch?v=5FokzkHTpc0 | YouTube transcript, same extraction pipeline | 2026-02-05 | `claude-export/normalized/conversations/a9726445-2215-4e8e-af15-c125a7073060.md` | 105,434 bytes (`wc -c`) |
| S4 | "💎💎💎 Seena Rez \| $49,140 tiktok dropshipping in 7 days from scratch" pt.2 (continuation prompt-generation) | Claude.ai conversation, no new transcript content — continuation of S1's crown-jewel prompt generation | 2026-01-05/07 | `claude-export/normalized/conversations/ece83bcc-5004-481a-a086-125f6438e75a.md` | 12,864 bytes (`wc -c`) |
| S5 | Fresh & Seena Rez $2.7M brand video, duplicate extraction thread ("The [Expert]'s name is Seena Rez not 'Merlin Ai'") | Claude.ai conversation, same transcript as S3, different extraction pass | 2026-02-05 | `claude-export/normalized/conversations/8db41cd0-017d-4397-9bb9-2ce427feea80.md` | 49,712 bytes (`wc -c`) |

**Label**: VERIFIED. All five member files were extracted from the tarball with
`tarfile` (Python), read in full, and the exact quote strings used below were
located verbatim via `grep` against the extracted text before being placed in
`genius.md`. This confirms both that Seena Rez is a real, named TikTok
dropshipping/e-commerce creator whose videos exist at the cited URLs, and that
the quotes attributed to him in this repair pass are transcript-accurate.

## Claim-by-Claim Ledger

| Claim / genius.md location | Label | Basis |
|---|---|---|
| Seena Rez generated $1.8M in one month from 2 viral videos (SKILL.md intro) | VERIFIED | S2: "made two viral videos for it that generated 3 million views in total and ultimately made me $1.8 million in the month of January of this year." |
| $49,140 in 7 days (skill framing, workflow references) | VERIFIED | S1 video title + transcript: "how I took a product from 0 to $49,000 in just 7 days." |
| $2.7M / $3M Pilates grip-socks brand (referenced in workflows/market-opportunity-blueprint.md framing) | VERIFIED | S3/S5: "how I built a $3 million brand in just 30 days... They're called Pilates Grip Socks." |
| 5%+ conversion rate claim (SKILL.md: "converts viewers into buyers at 5%+ rates") | VERIFIED for the cited case, LIKELY as a general rule | S2: "5% of the people who visited my store out of 700,000 bought my product. That's a high conversion rate." — this is Seena's one documented result, not a stated universal guarantee. |
| PSAEP framework (Problem, Solution, Authority, Explanation, Product/CTA) — Pattern 2 | VERIFIED | S2: "Problem hook, solution, authority, explanation, product. This is how you structure a Tik Tok video." |
| "Hyperdopamine" content terminology — Pattern 1, throughout | VERIFIED | S2: "that is hyperdopamine content... That's why we call it hyperdopamine content." |
| High Smile as the "#1 brand" reference model — Pattern 11 | VERIFIED | S2: "this is High Smile... they're the most profitable brand on Tik Tok. They literally made a billion dollars in revenue last year." |
| Authority Speed-Stacking pivot line — Pattern 3 addition | VERIFIED | S2: "But you know what's also based upon real science?" |
| Aging-filter hook line — Pattern 7 addition | VERIFIED | S2: "Apparently, the aging filter is based upon real science." |
| Caption recoloring instruction — Pattern 10 addition | VERIFIED | S2: "Since our text is going to turn white, we don't want it to be white. So, we're going to turn into yellow." |
| "Speed = Legitimacy" self-description — Hidden Knowledge 4 addition | VERIFIED | S2: "Basically just putting it all over the screen very quickly. People will assume that this stuff is legit." |
| Reach-vs-conversion separation, 5%/700,000 proof point — Hidden Knowledge 5 addition | VERIFIED | S2, same passage as the 5% conversion claim above. |
| Variation-buffer case (1.4M/1.8M videos) — Hidden Knowledge 6 addition | VERIFIED | S2: "Most of them didn't go viral. It was only the 1.4 and the 1.8 million video that went viral." |
| "0.1% of what High Smile does" — Hidden Knowledge 3 | VERIFIED | S2: "if I can get 1% of their viewership, then I would have made a million [a] month in revenue... you literally just have to do 0.1% of what they were able to do." |
| Anti-pattern: abandoning a video instead of variating it | VERIFIED | S2: "this is the mistake that most people make when they're creating Tik Tok videos... 'I guess now what I have to do is come up with a completely new video idea.' Wrong. That is a mistake." |
| Anti-pattern: CBO instead of controlled ad-set budgets | VERIFIED | S1: "Sounds good in theory, but we do not want to do this. It adds complexity that we're not really looking for." |
| Anti-pattern: $200 paid Shopify theme / web designer | VERIFIED | S1: "Most people have you think that you need to spend $200 on a paid Shopify theme or get a web designer. A lot of those people are trying to give you their affiliate link, I believe." |
| Anti-pattern: naming the brand inside the hook | VERIFIED | S1: "I haven't sold the product yet. I haven't even named the product yet... This is because I don't want the content to seem like an ad." |
| Anti-pattern: scaling ad spend below 3:1 LTGP:CAC | VERIFIED | S1: "You don't want to go any lower than 3:1." |
| Anti-pattern: entering a stagnating/declining market | VERIFIED | S3: "You don't want to be getting into a stagnating or declining market because there's no opportunity there." |
| "make sure not to be a noob" quote — Model Calibration section | VERIFIED | S2: "So, make sure not to be a noob and do this. It's what a noob does. This is what a pro does. They create variations." |
| Numeric Success Metrics on all 14 Genius Patterns (e.g. "50%+ retention," "3%+ click-through rate," "Paid ROAS above 3x," "10x average view count") | UNCONFIRMED | These specific numeric thresholds do not appear verbatim in S1/S2/S3. They read as benchmarks synthesized by the original 2026-01/02 extraction pass (Claude.ai, MES 3.0 protocol), not statements Seena Rez made on camera. Treat as reasonable practitioner targets, not attributed claims — do not present them as Seena's own words in downstream deliverables. |
| Hall of Fame Exemplars ("YouthRestore Serum," "Celebrity Secret Jawline Tool," "Generic Coffee Maker Ad") | UNCONFIRMED | These are illustrative composites built by the original extraction to demonstrate pattern combinations — no matching product, brand, or campaign name appears in S1/S2/S3. Useful as teaching exemplars; must not be cited as real Seena Rez case studies. |
| "Attention Academy" community / "my brother Ali" / Alex Hormozi School games mention (background context, not currently in genius.md pattern text) | VERIFIED (mentioned), out of scope | S1/S2 both reference "Attention Academy," Seena's paid education platform, and a creator "Ali" described as his brother; not surfaced in current genius.md patterns, flagged here for future editors rather than fixed in this pass (additive-first scope). |
| 23 deployable prompts / workflow structure (SKILL.md, references/prompts-v2/) | LIKELY | Structurally derived from the patterns above by the original extraction pipeline; not independently re-verified line-by-line in this repair pass (out of scope — workflow_contracts check already passes and boundaries direct additive, minimal-touch work). |

## Absence Check (per envelope's provenance rule 2)

`extractions/` was searched for `seena` and `rez` fragments (case-insensitive,
no punctuation) — zero matches, confirmed via `ls extractions/ | grep -i`.
This is NOT treated as "no source exists": the archive tarball
(`_archive/claude-export-2026-07-01.tar.gz`, 332,779,255 bytes, 7,720 tar
members) was scanned member-by-member with a Python `tarfile` content scan
for `seena`, `rez`, `high smile`, `hyperdopamine`, and `psaep` (case-insensitive
regex over raw bytes, not filename matching). That scan found 13 matching
members; the 5 conversation files listed above (S1-S5) were extracted and
read in full, confirming the skill's origin is a real, traceable set of
Seena Rez YouTube transcripts processed through a Claude.ai MES 3.0 extraction
in Jan-Feb 2026 — not an invented persona.
