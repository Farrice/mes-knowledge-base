# Source Ledger — sunny-lenarduzzi-youtube

## Search discipline (per envelope)
1. `ls extractions/ | grep -i lenarduzzi` and `grep -i sunny` — **0 results**. No `extractions/` entry exists for this expert.
2. Because no local extraction was found, ran a full per-member CONTENT scan of `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes; confirmed with `wc -c`, never `wc -l`) via Python `tarfile`, matching `lenarduzzi` case-insensitively inside decoded UTF-8 member content. 7,728 members scanned, **49 matched**, all under `claude-export/normalized/conversations/*.md`.
3. Pulled the 10 most title-relevant matches (YouTube-strategy and business-build videos, MES-protocol extraction conversations) and read them in full for verbatim quotes, numbers, and timestamps. File sizes recorded below via `wc -c` on the extracted copies.

## Files consulted (all `claude-export/normalized/conversations/<id>.md` inside the tarball)

| ID (short) | Title | Size (bytes, `wc -c`) |
|---|---|---|
| 8585118b | "Sunny Lenarduzzi: The smartest way to make money on youtube from day one" | 74,432 |
| b17fabc8 | "Sunny Lenarduzzi: watch me create a $1M YouTube channel in 38 minutes using AI." (transcript of youtube.com/watch?v=swBwRtHVVlA) | 76,865 |
| 85bd453b | "💎💡 Sunny Lenarduzzi \| If I Wanted To Make $100k In 2026 This Is EXACTLY What I'd Do" | 105,902 |
| e970b085 | "Sunny Lenarduzzi \| The Blueprint To Make Money Without Social Media On Day 1 \| Online Course Mastery" | 54,559 |
| c8390c2b | "Sunny Lenarduzzi \| How I'd Make $100k a Year (Working Only 5 Hours a Week)" | 53,533 |
| 8443d424 | "💡💎 Sunny Lenarduzzi \| If I Had To Create an Online Business From Scratch, Here's What I'd Do" | 69,918 |
| ef4f510a | "11-26-25 Sunny Lenarduzzi: Watch Me Turn Your 9-5 Into A Million Dollar Business in 2026" | 59,405 |
| fc374eb1 | "💎💰💡 12-5-25 Sunny Lenarduzzi: How I Use Google Docs To Run My $5M/Year Business" | 46,244 |
| d3d31dbe | "💎💡 Sunny Lenarduzzi \| ...pt.2" (continuation of 85bd453b) | 38,870 |
| 99505229 | "Sunny Lenarduzzi: watch me create a $10K/month business in 10 minutes with AI." | 76,357 |

## Claim ledger (skill-file claims only — SKILL.md + genius.md)

| Claim | Label | Basis |
|---|---|---|
| CODE framework: Client, Offer, Differentiation, Engagement (order matters) | VERIFIED | b17fabc8, timestamp 0:47–1:09, verbatim: "...comes down to four critical elements that form what I call the code..." |
| Jeffrey: relationship coaching, $1.2M in 18 months from zero subscribers/clients/audience, $10M in 4 years | VERIFIED | b17fabc8, timestamp 2:36–2:51 |
| Denver: $1.36M on 2,632 subscribers | VERIFIED | 8585118b, timestamp 1:13–1:20 |
| Todd: $500K business, 536 subscribers | VERIFIED | 8585118b, timestamp 1:23–1:25 |
| One Viewer Model / subscriber count "virtually irrelevant" | VERIFIED | 8585118b, timestamp 1:43–1:51 |
| Reverse funnel / "hockey stick" mechanic, search → suggested → browse | VERIFIED | b17fabc8, timestamp 10:59–11:20 |
| Five-factor topic validation (stand out / keywords / competition / demand / genuine value), applied to "the truth about winning your wife back" | VERIFIED | b17fabc8, timestamp 15:29–16:59 |
| "Sam" HOT-script example ("Sam was one argument away from divorce...") and Market-of-One title ("How I helped Sam rebuild his marriage WITHOUT begging or therapy") | VERIFIED | b17fabc8, timestamp 14:39–14:57 (Market of One) and 24:18–24:48 (HOT script) |
| Congruent metadata / tag-flagging warning | VERIFIED | b17fabc8, timestamp 30:51–31:01 |
| CTR 2–10% healthy, retention >40% strong | LIKELY | Consistent with framing in multiple videos ("hitting 40%+ retention," CTR-in-range language); exact numeric ranges as stated were not located verbatim as a single sentence in the 10 files pulled — treat the ranges as accurately paraphrased, not a verbatim quote |
| Burnout hospitalized Sunny at 29 | VERIFIED | c8390c2b: "Burnout was knocking so loud that it actually sent me to the hospital at 29 with all of the symptoms of having a stroke." |
| A window and a webcam → first 50,000 subscribers | LIKELY | Consistent with the "authenticity over production" theme repeated across multiple videos; the specific "50,000 subscribers" figure tied to "window and webcam" was not located verbatim in the 10 files pulled — pre-existing claim, not independently re-verified this pass, flagged for a follow-up source pull |
| Mike: 50 interviews → 32 clients → $89K in 30 days (pre-sell before building) | **UNCONFIRMED** (partial) | Mike/restaurants/$89K is VERIFIED — c8390c2b: "Mike, who runs 12 restaurants and made $89,000 in 3 weeks using this method"; ef4f510a, timestamp 15:31–15:46: "He made $89,000 when he launched his POP originally." Neither file states "50 interviews," "32 clients," or "30 days" — those specific figures were not located anywhere in the 10 files pulled or in the 39 other tarball matches by filename/title relevance. Left the pre-existing genius.md line untouched (additive-first boundary — the section already passed the entity-floor check) but flagging here per the hard rule against invented provenance. Do not cite "50 interviews → 32 clients" as verified in any downstream deliverable until re-sourced. |
| 600K subscribers / ~$40M business (SKILL.md header) | LIKELY | c8390c2b opens "my online business has generated close to $40 million"; 8585118b references hundreds of thousands of subscribers and "millions" from her channel. The precise "600K subscriber" figure was not located verbatim in the 10 files pulled — plausible/consistent, not independently confirmed this pass |
| Anti-pattern quotes (expert's curse, pricing-by-time, program-before-people, post-without-offer, do-everything-at-once, tag-stuffing) | VERIFIED | See genius.md → Anti-Patterns (Sourced) section; each item carries its own file + timestamp/date anchor |

## Notes for the next worker or verifier
- The tarball has 39 additional matches for "lenarduzzi" not pulled this pass (lower title-relevance to YouTube/channel strategy specifically — several are program-build or Google-Docs-workflow videos). If a future claim needs verification and isn't in this ledger, check those first before declaring it unrecoverable.
- All timestamps cited (e.g., "30:51") are from the SRT-style auto-transcript embedded in `b17fabc8-4c47-4d3b-bbce-f29475fa0d44.md`; inline timestamp tokens were stripped from quoted text for readability but no words were altered — verify by opening the file and searching the timestamp.
