# Source Ledger — yuri-elkaim-health-coaching-business

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 18). Ground truth = six YouTube-transcript
conversation exports found in `_archive/claude-export-2026-07-01.tar.gz` under
`claude-export/normalized/conversations/`, located via a per-member content scan
(no `extractions/` directory match for "elkaim" or "yuri" — verified absent by
listing, not assumed). All six matched on "elkaim" or "healthpreneur" in a full-text
scan of the archive; sizes recorded with `wc -c` (byte counts, not line counts).

## Primary Sources (this repair pass)

| ID | File (in archive) | Title | Size (bytes, `wc -c`) | Label |
|----|---|---|---|---|
| S1 | `06ecf597-fa67-49ce-9da9-36bda86e2770.md` | Healthpreneur: How to start an online fitness business and kiss the gym goodbye | 79,166 | VERIFIED (raw transcript, timestamped) |
| S2 | `3c7fe82a-5236-4429-bae9-51d8756a6ede.md` | Healthpreneur: How to consistently generate leads without spending all day on social media | 76,062 | VERIFIED (raw transcript, timestamped) |
| S3 | `6420660c-5793-4c72-a756-abf841a1527d.md` | Healthpreneur: How to create an offer so good people beg you to buy it | 74,708 | VERIFIED (raw transcript, timestamped) |
| S4 | `b2443ff5-76db-482b-93f0-f811b110873e.md` | Healthpreneur: How to create an online coaching program step-by-step curriculum builder | 69,051 | VERIFIED (raw transcript, timestamped) |
| S5 | `d91d258e-903f-4679-8a6c-0c4473832990.md` | Healthpreneur: How to get high-paying clients for your online health coaching business | 47,115 | VERIFIED (raw transcript, timestamped) |
| S6 | `dcbc85af-a5d5-4390-8eb0-d39451094c44.md` | Healthpreneur: Starting a health coaching business — use this daily roadmap to make $100k | 66,204 | VERIFIED (raw transcript, timestamped) |

Each file is a Merlin-AI-generated YouTube transcript (MM:SS-stamped lines) pasted
into a claude.ai conversation, followed by the assistant's own analysis/synthesis.
**Only the timestamped transcript lines are treated as primary source.** The
assistant's downstream "Looking at the transcript..." commentary in each file is
Claude's own prior synthesis, not Yuri's words, and was NOT used as a citation
source for any claim below.

`skills/yuri-elkaim-health-coaching-business/SKILL.md` frontmatter already declared
`source: claude.ai export 2026-07-01` — this ledger makes that declaration auditable
by pointing at the exact six archive members and exact timestamps.

## Claim-by-Claim Ledger

### New anti-pattern items added this pass (genius.md → Anti-Patterns (Sourced))

| Claim | Label | Source |
|---|---|---|
| "a lot of people are making the mistake and doing too much too soon" (channel-stacking) | VERIFIED | S1, 20:29 |
| "one of the worst things you can spend your timeline" (posting before a system exists) | VERIFIED | S2, 16:14 |
| "this is one of the worst things you can do when building" (curriculum) — over-educating | VERIFIED | S4, 11:16 |
| "if you've never worked with a paying client and you start running ads, um, you're going to lose your shirt very quickly" | VERIFIED | S5, 4:58 |
| "chasing external validation whether it's in numbers or people praising your work — you will fail because you will give up very quickly" | VERIFIED | S6, 9:45 |
| "it's not copy paste out of Chatty G onto whatever platform it's to avoid the blank screen" | VERIFIED | S6, 16:30 |
| "the only thing more dangerous than free advice is the wrong advice" | VERIFIED | S5, 17:45 |

### Pre-existing genius.md / SKILL.md claims cross-checked this pass

| Claim | Label | Source |
|---|---|---|
| Started health-content work in 2005 | VERIFIED | S6, 19:09 ("I've been in it since 2005") |
| Lost hair to autoimmune condition at 17, resolved over 8 years | VERIFIED | S1, 0:39–0:42 |
| "my mess becoming my message" framing of his first business | VERIFIED | S1, 0:50–0:52 (paraphrase-adjacent — see caveat below) |
| Shared his journey with "half a million people" | VERIFIED | S4, 12:09 ("helped half a million people") |
| First business took 7 years to reach $1M | VERIFIED | S1, 18:53–18:56 ("took me 7 years to make my first million dollars") |
| Published 3,000+ YouTube videos across both businesses | VERIFIED | S6, 19:13 ("published more than 3,000 videos on YouTube alone") |
| Healthpreneur went zero to seven figures in seven weeks, no social/YouTube/podcast for first 3 years | VERIFIED | S2, 14:04–14:20 |
| Vehicle ("Saves You Serious Time, Energy and Money") + gasoline (messaging/offer) diagnosis | VERIFIED | S2, 2:31–2:59 |
| Track-record gate: proven coaches (~$5–10K/mo) scale with paid; newbies earn stripes organically | VERIFIED | S5, 4:44–5:03 |
| Messaging Blocks document as copy-paste foundation for all marketing | LIKELY | S2 (block-by-block section referenced but full enumerated list not re-verified line-by-line this pass — carried over from prior extraction, not re-audited) |
| Frustrations-over-fears (humans optimistic about the future) | VERIFIED | S2, 12:42–13:15 |
| False beliefs as unspoken objections + three dissolving questions | VERIFIED | S2, 13:29–15:23 |
| "Social media = media × social," daily post + Visibility Optimizer comments | LIKELY | S2/S6 general framing verified; the exact "media × social" phrasing is this skill's own compression of Yuri's point, not a direct quote — treat as paraphrase, not verbatim |
| The Trade: free cohort, testimonial-for-work, 625 opted in / ~20 finished | VERIFIED | S6, 29:52 (625) + 30:08–30:15 (~20 finished) |
| Niche = severe + persistent (migraine vs. tension headache framing) | LIKELY | Consistent with S2/S5 niche-severity discussion; the specific "migraine vs. tension headache" example was not located verbatim in the six scanned files this pass — treat the framework as VERIFIED, the specific example pairing as this skill's own illustrative gloss |
| "Time is expensive, money is cheap" / paid ads as fast feedback | VERIFIED | S2, 3:11–3:23 (leverage/feedback-speed framing) |
| Going viral as a failure mode for niche coaches | UNCONFIRMED | Not located verbatim in the six scanned files this pass; not re-verified against the original extraction session (predates this repair) — retained in genius.md as pre-existing content, flagged here rather than silently re-stamped VERIFIED |

## Gaps Named

- The original authorship trail (which agent/session first drafted genius.md's
  16 patterns + 5 insights) predates this repair pass and is not in `extractions/`.
  No extraction folder exists for this expert (verified by directory listing, not
  assumed) — the only recoverable ground truth is the six archive transcripts above.
- Two pre-existing claims ("Social media = media × social" exact phrasing; "niche =
  severe + persistent" migraine/tension-headache example pairing) read as reasonable
  compressions of verified source material but were not found as verbatim strings in
  the six files scanned this pass — labeled LIKELY, not VERIFIED, rather than invented
  as confirmed.
- One pre-existing claim ("going viral is a failure mode for niche coaches") could not
  be located in the six scanned transcripts at all this pass — labeled UNCONFIRMED.
  It is left in place (additive-first boundary; not deleting passing content) but
  should not be treated as a sourced quote until traced to its origin file.
