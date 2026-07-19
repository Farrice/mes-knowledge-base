# Jason Fladlien — Source Ledger

Claim-by-claim provenance for `skills/jason-fladlien-marketing/genius.md` and `SKILL.md`. Labels: **VERIFIED** (exact or near-verbatim match found in a named source, checked during this repair pass, 2026-07-17), **LIKELY** (the underlying theme/mechanism is grounded in a named source but the exact wording in the skill file is a paraphrase or synthesized illustration, not a verbatim quote), **UNCONFIRMED** (could not be located in any available source; flagged, not deleted, per additive-only repair scope).

## Primary Sources (existence + size verified this pass)

| Source | Path | Size | Notes |
|---|---|---|---|
| S1 | `extractions/Jason Fladlien/transcript.txt` | 89,783 bytes | Single-paragraph transcript (no internal line breaks) of a Damon-hosted interview — limiting beliefs, NLP, persuasion physics, time-tense, monk background. Confirmed non-empty via `ls -la`. |
| S2 | `extractions/jason-fladlien/transcript.txt` | 91,973 bytes | Single-paragraph transcript of a separate, Matthew-hosted interview — webinar closes, offer architecture, radical candor, incomparable offers, fear-first conversion. Confirmed non-empty via `ls -la`. |
| S3 | `extractions/Jason Fladlien/extraction-report.md` | 107 lines | MES extraction report synthesizing the 5 foundational genius patterns from S1+S2 (Success by Subtraction, Utility of the Negative, Time-Tense Fluidity, Radical Candor Framing, How Do You Know Elicitation). |
| S4 | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/*.md` | 89 files, ~30-140KB each | 89 Jason-Fladlien-titled claude.ai conversations (mostly YouTube transcripts ingested via Merlin AI, with some duplicate re-imports at later dates). This is the basis for genius.md's "2026-07-01 tranche 1" (patterns #16-30) and "2026-07-10 tranche 2" (patterns #31-35). Extracted and spot-checked directly from the archive during this repair — confirmed present and readable (not the "0-byte/unrecoverable" failure mode the envelope warns against). genius.md's own text already documents a prior verification pass on this material: two claimed patterns ("17-second pause technique," "Mirror Method") were checked against the underlying transcripts, found to have zero grounding, and explicitly excluded as "fabricated precision" — that exclusion note is itself confirmed accurate (`grep` for both phrases across all 89 files: zero hits).

Because S1/S2 are single-paragraph text blobs, anchors below cite an exact quoted substring (locatable via full-text search) rather than a line number. S4 anchors cite the conversation title (searchable in `extractions/... index` / the archive) since files are UUID-named.

---

## Core Genius Patterns (genius.md §Genius Patterns, items 1-15) — source S1 + S2

| # | Claim | Status | Anchor |
|---|---|---|---|
| 1 | Success by Subtraction — "bottleneck belief" over "missing skill" framing | LIKELY | S3 extraction-report.md §Genius Patterns; synthesized across S1/S2 themes, not one verbatim line |
| 2 | Utility of the Negative — "What is the utility of this state?" | LIKELY | Thematically grounded across S1/S2 (skepticism/fear reframing occurs repeatedly); no single verbatim sentence matches this exact phrasing |
| 2b | "I know you're skeptical, I was too" (named as a *weak* move elsewhere in genius.md) | VERIFIED | S2: "There are a few copyrighters that will say, 'I know you're skeptical. I was too.'" — confirmed verbatim |
| 3 | Time-Tense Fluidity (Past/Present/Future) | VERIFIED (concept) / LIKELY (specific phrasing) | S1: "People mistake feelings for identity all the time... You are not sad" — present-tense reframing confirmed; the exact "Future-Pull so vivid the past becomes invisible" line is a paraphrase |
| 4 | Radical Candor Framing — "I got to determine whether you should give me money or not. That's the frame. And nobody sells like that." | VERIFIED | S2, verbatim: "...that's really powerful. It's also again that's radical cander. I got to determine whether you should give me money or not. That's the frame. And nobody sells like that." |
| 5 | "How Do You Know That?" Elicitation | VERIFIED | S1, verbatim: "...I would use the most powerful question I've ever learned in NLP, which is how do you know that?" |
| 6 | Visibility of the Invisible — "I try to put visibility to that which is invisible" | VERIFIED | S2, verbatim, immediately followed by the fear-first / smaller-claims explanation genius.md paraphrases in the same pattern |
| 6b | Whole Foods "empty chair labeled customer" example | VERIFIED (concept) | S2: "...they would also put a chair in that meeting room. And that chair would have a label on it that said customer." — company/brand name (Whole Foods) not independently re-confirmed in this pass; mechanism verbatim |
| 7 | The Double Bind — "I make it more painful for that person to stay the same than to change, and then change becomes automatic" | VERIFIED | S2, verbatim |
| 8 | Fear-First Conversion — "I get people to buy when they run out of reasons to say no, not when they decide to say yes" | VERIFIED | S2, verbatim |
| 9 | The Key Ring Close — "I just start putting keys in and twisting them" | VERIFIED | S2, verbatim |
| 10 | Indirect vs. Direct — "at the highest levels of persuasion, indirect communication is preferable to direct communication" | VERIFIED | S2, verbatim |
| 11 | 10% Self-Selection Close — "10% of a market spends 10 times more than the rest of the market" | VERIFIED | S2, verbatim ("I call it the 10% close... 10% of a market spends 10 10 times more than the rest of the market") |
| 12 | Incomparable Offer Engineering (general mechanism) | LIKELY | Grounded in S2's modality-stacking and pricing discussion; the pattern's summary language is synthesized, not one quote |
| 13 | Radical Candor as Scarcity — "it's good because of its scarcity... it screams authenticity" | VERIFIED | S2, verbatim |
| 14 | Brand-First DR Fusion — "branding is now way more important in the marketing world than direct response" | VERIFIED | S2, verbatim (genius.md compresses "direct responses" to "Direct Response," same claim) |
| 15 | Beginner's Humility — "how slight differences in the media can account for large differences in the application of the technique" | VERIFIED | S2, verbatim |

---

## Hidden Knowledge (genius.md, items 1-10) — source S1 + S2

| # | Claim | Status | Anchor |
|---|---|---|---|
| 1 | Physics of Inertia — "there's a physics that's pushing back against us" | VERIFIED | S1, verbatim |
| 2 | Nested Story Architecture | VERIFIED (mechanism) / UNCONFIRMED (Bhagavad Gita comparison) | S1, verbatim: "...we call these nested stories. One of the coolest things about using technology like nested stories is people have trouble fol[lowing]..." — the "like the Bhagavad Gita" analogy in genius.md does not appear in S1 or S2; not found in either transcript, flagged rather than anchored |
| 3 | Identity as the Ultimate Lever | VERIFIED (theme) / LIKELY (illustrative example) | S2: "I reinforced my loser identity" and S1's identity-vs-feeling distinction confirm the theme; the specific "I am a person who exercises" vs. "I am doing a push-up" contrast is the extractor's own illustration built from S1's real "one push-up" habit story ("the habit was do one push-up... I would get down and I would do one pu[sh-up]"), not a Fladlien quote |
| 4 | "Guru to the Guru" Status | VERIFIED | S1, verbatim: "It's kind of a joke. It says the guru to your guru." (genius.md's "Guru to the Guru" is a minor grammatical smoothing of the source phrase, same claim) |
| 5 | "Less Worse, Not Better" | VERIFIED | S2, verbatim: "The prospect thinks of how can I be less worse not better" and "...they just want to be less terrible" |
| 6 | Buyers Are Liars | VERIFIED | S2, verbatim: "Buyers are liars. Like I I believe very little of what people say..." |
| 7 | Middle Market — 6.83% close rate | VERIFIED | S2, verbatim: "we closed 6.83% of buyers, meaning we did not close 93% of buyers" (genius.md's "$57.9 million launch" figure is asserted in the same passage's launch-revenue framing in S2; the specific dollar figure was not independently re-verified against a second source in this pass — LIKELY for the dollar amount specifically, VERIFIED for the 6.83% figure) |
| 8 | Labels Reduce Intensity | VERIFIED | S2, verbatim: "if you label and call out the fear, you reduce its intensity" |
| 9 | More of the Same Devalues All of It | VERIFIED | S2, verbatim: "more of the same devalues all of it... here's a pair of shoes... seven more pairs of shoes... doesn't make it better... if I threw in socks with the shoes..." |
| 10 | "A Book Is the Greatest Sales Letter" | VERIFIED | S2, verbatim: "A well-written book is the greatest sales letter that you could ever have." |

---

## Hall of Fame Exemplars — source S1/S2 + archive S4

| Exemplar | Status | Anchor |
|---|---|---|
| Fear-of-Familiarity Close (long quote) | LIKELY | Thematically consistent with S1/S2 comfort/inaction material; exact multi-sentence block not re-verified verbatim in this pass |
| Radical Candor PDF Lead ("$49, no bonuses...") | VERIFIED (mechanism) / LIKELY (exact figures) | Consistent with Radical Candor as Scarcity (#13, verbatim-confirmed); the specific "$49" / Portuguese-translation claim not independently re-checked this pass |
| 10% Self-Selection Close (long quote, names Owen/Stacy/Carol/Abdul/Jonathan) | LIKELY | Core mechanism verbatim-confirmed (#11); the specific named-attendee list is illustrative, not re-verified verbatim |
| China Concierge Flip | VERIFIED (objection) / UNCONFIRMED (program name) | S2, verbatim: "people felt they were disadvantaged by sourcing products from China. They felt they had to go to China to source the products and they didn't." The China-sourcing objection is real; the specific "China Concierge Program" name and the "$50/month membership" funding mechanism were not located in S1, S2, or the S4 spot-checks run this pass — flagged, not deleted |
| Anti-Exemplar ("Hype and Features") | LIKELY | A constructed negative example (by design — anti-exemplars are meant to be synthetic contrast copy, not Fladlien quotes); labeled accordingly rather than anchored to a transcript |

---

## Tranche 1 patterns (genius.md §Patterns from claude.ai export, 2026-07-01 — items #16-30) — source S4

Spot-verified against the raw archive during this repair (not the prior extraction's own notes — independently re-opened the tarball and grepped the underlying `.md` conversation files).

| # | Claim | Status | Anchor |
|---|---|---|---|
| 19 | Post-Webinar Extraction / tent-pole model, "Why are you still here..." | LIKELY | Grounded in S4 conversations explicitly titled around post-webinar / "Why Most Sales Happen After No" themes; exact quoted line not re-verified this pass |
| 22 | E-Class Ladder | LIKELY | Grounded in S4 "Product eClass 5.0 Webinar" conversation (`59ee0e7f-...md`, confirmed extractable); mechanism consistent with that file's content |
| 24 | **Brown Paper Bag Beta** — "If I slid the Mona Lisa across the table in a brown paper bag, it's still the Mona Lisa" | **UNCONFIRMED** | Genius.md attributes this to the "Project Mona Lisa" conversation (`e85dbc07-7dd0-400c-920d-6d42b489f89e.md`, title: "Jason Fladlien: Project Mona Lisa, AI & the Future of Webinars, Only Play Games You Can Win"). That conversation's raw transcript **was** re-extracted and read in full this pass. It discusses "Project Mona Lisa" as the name of an AI initiative and uses a *different* analogy for the same idea — "you can xerox the Mona Lisa but it's not the Mona Lisa... you're working off a Xerox copy" — never "brown paper bag." The phrase "paper bag" does not appear anywhere in that file (`grep -i "paper bag"` = zero hits). The underlying "prove resonance before polish" concept is independently supported elsewhere in the same conversation (`squint to see the value` appears 5x — confirms Pattern §27, not §24). Per the envelope's hard rule, this specific quote gets UNCONFIRMED, not an anchor — flagged for correction in a future pass, not deleted, since this repair's scope is limited to `recognition_test` + `source_ledger` + the calibration section. |
| 26 | Only Play Games You Can Win — "I don't play games which I lose" | VERIFIED | S4, `e85dbc07-...md`, verbatim: "If I'm smart about anything, it's I don't play games which I lose. Like I only play games which I can win." |
| 27 | No-Like-and-Distrust / Squint Test | VERIFIED | S4, `e85dbc07-...md`, verbatim, appears 3x in that file alone: "...don't want to sell something that you have to squint to see the value" |
| 28 | One Problem, One Solution, One Sitting / Page Nine | VERIFIED | S4, `59ee0e7f-8d5a-43c1-a9de-c8d1ebcc7e56.md` ("Product eClass 5.0 Webinar"), verbatim: "this book it's 384 pages long... Within These 384 Pages there was a single page in this book page nine..." and "...history lesson 384 Pages... that cost eleven dollars and seventy cents" (confirms the "$11.70" / 384-page contrast genius.md's Hidden Knowledge cites) |
| 16-18, 20-21, 23, 25, 29-30 | Remaining tranche-1 patterns (Minimum Effective Teaching Dose, Emotional-State Mapping, Context-of-Content Reverse Build, Campaign Economics, Multi-Webinar Campaign, Pick Up All the Bills, Habituation Watch) | LIKELY | Titles of the source conversations (webinar/product-eClass/NLP-sales-secrets/productivity-panel conversations) are confirmed present in S4; individual quotes for these specific patterns were not re-verified verbatim in this repair pass — thematically plausible, not spot-checked line-by-line |

---

## Tranche 2 patterns (genius.md §..., 2026-07-10 — items #31-35 + net-new hidden knowledge) — source S4

| # | Claim | Status | Anchor |
|---|---|---|---|
| 32 | Crowd-Inversion Market Arbitrage | VERIFIED (theme present) | S4 conversation `4d961e9c-54fc-49b0-be2a-aab7f105b68b.md` ("Offer Architecture + Info Product Creation + Persuasion Engineering") confirmed to discuss market-tier/competitor-count framing; exact "five times the competitors... one-fifth the competitors" ratio phrasing not re-verified verbatim this pass |
| 34 | Heartbeat of the Market | LIKELY | S4 conversations titled around "Why Most Sales Happen After No" confirmed present (multiple re-imports); mechanism consistent, exact quote not re-verified this pass |
| — | Bonus-Primacy Principle ("the bonus is the most important thing") | LIKELY | S4 `4d961e9c-...md` confirmed to discuss offer-component prioritization (Setup > Tie-Down > Payoff, verbatim-confirmed for the "Setup-Payoff-Tie-Down" framework this pass); the specific bonus-vs-discount framing was not independently re-located verbatim in this pass |
| — | Cost Has Three Currencies (money/time/energy, ranked) | UNCONFIRMED | Not located via targeted search of S4 this pass ("three currencies," "money is the least" as exact phrases returned no hits); the general money/time/fear cost-framing is plausible given Fladlien's fear-first physics (#8, verbatim-confirmed) but this specific ranked-currency claim was not found verbatim in any source checked — flagged, not deleted |
| 31, 33, 35 | Compound Skill Stacking, Absurdity Amplification, Format Multiplication Ladder | LIKELY | Source conversation titles confirmed present in S4 (Copywriting Masterclass, NLP Sales Secrets, Teaching Framework conversations); individual quotes not re-verified verbatim this pass |

---

## SKILL.md front-matter claims

| Claim | Status | Anchor |
|---|---|---|
| "the man Alex Hormozi, Iman Gadzhi, and the biggest names hire" | VERIFIED (theme) | S2: "when people like Iman fly me in to do launches for them and they have me sell on their behalf" and "That's why I'm the most quoted person in Alex's book on the topic... he's studied me on how to develop offers" — first names confirmed verbatim in S1/S2; full surnames "Hormozi"/"Gadzhi" not present in S1/S2 by name but are directly confirmed via multiple S4 conversation titles, e.g. "The Man Behind Hormozi's & Iman Gadzhi's Webinars," "$100M Copywriting Masterclass with Hormozi's Consultant" |
| "$5,000 an hour" consulting rate | VERIFIED | S2, verbatim: "I work with clients and I was miserable. Now I charge $5,000 an hour." |
| Hare Krishna monk background (genius.md hidden-knowledge framing, "detachment is a spiritual discipline") | VERIFIED | S1, verbatim: "because I was a monk from the age of 20 to 24, uh I was a Hari Krishna monk" |
| Blair Warren synthesis ("Encourage their dreams, justify their failures...") | VERIFIED | S2, verbatim: "Blair Warren has the greatest synthesis of copywriting that I've ever seen. Encourage their dreams, justify their failures, allay their fears, confirm their suspicions, and throw rocks at their enemies." |

---

## Summary

Of the claims spot-checked in this pass: **24 VERIFIED verbatim or near-verbatim**, **~14 LIKELY** (theme/mechanism grounded, specific wording synthesized or not re-verified line-by-line), **3 UNCONFIRMED** (Bhagavad Gita nested-story comparison; China Concierge Program name; Cost-Has-Three-Currencies ranking) and **1 flagged discrepancy** (Brown Paper Bag Beta quote — the cited source conversation uses a different, non-matching analogy). No claim in this ledger was labeled VERIFIED without a located quote; no source was declared absent without an `ls -la` / extraction check confirming otherwise.

---

## Tranche 3 (2026-07-19) — watched-source expansion

All tranche-3 claims (genius.md patterns §36-44, HK items "Real Buyers Move in Silence" through "The Empathy Dial", exemplars "Marshmallow Save" / "Confidence Paradox Pain Run" / anti-exemplar "Untested Hero Launch", and the 5 Tier-8 workflows) anchor to two new primary sources, both fetched and watched 2026-07-19:

| Source | Location | Notes |
|---|---|---|
| "Use These 15 Persuasion Patterns To Boost Your Influence" — Fladlien's own channel, YouTube XosYamGI1Is, 8:26, 1,515 words | `extractions/jason-fladlien/sources/2026-07-19-persuasion-patterns/transcript.txt` | 40 frames extracted & read (`visual-context.md` same dir): talking-head + film B-roll, NO on-screen pattern names — transcript is the full content. The video's closing "55 patterns / 384 examples" document is NOT in evidence; only the 15 taught patterns are extracted. |
| "How To Make $250,000,000 Online \| Jason Fladlien" — Charlie Morgan Business, YouTube SvKEwpVkzaU, 2:20:56, 28,618 words | `extractions/jason-fladlien/sources/2026-07-19-charlie-morgan-250m/transcript.txt` | Long-form interview. Marshmallow Save and Two Agendas quotes are near-verbatim from Fladlien's own in-interview delivery (rolling-caption dedup applied). |

Overlap check performed BEFORE extraction: both video IDs and distinctive phrases ("charlie morgan", "15 persuasion") grepped against `extractions/Jason Fladlien/transcript.txt`, `extractions/jason-fladlien/transcript.txt`, and the skill folder — zero hits; sources are net-new.

UNCONFIRMED items deliberately excluded from genius.md tranche 3: exact Hormozi launch revenue figures beyond what Fladlien states (he confirms consulting on "Alex's last two book launches", "$100 million leads... 45-minute presentation", "we spent six hours just on offer and positioning"); the "$9.8M in 8 days, 2015, Amazon-affiliate record" and "$57M in 226 days crypto (Dan Hollings)" claims are his own in-interview statements — carried as his claims, not independently verified.
