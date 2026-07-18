# Source Ledger — patrick-dang-online-business

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 13). SKILL.md declared `source: claude.ai
export 2026-07-01` but no `references/` ledger existed and no `extractions/` folder for
this expert was present (`ls extractions/ | grep -i dang` returns nothing — only
"Patrick Debois," a different expert in this batch). Ground truth was recovered from
the raw claude.ai conversation export archive per SOURCE-SEARCH DISCIPLINE: python
`tarfile` per-member content scan of `_archive/claude-export-2026-07-01.tar.gz`
(7,728 members) for the literal string `Patrick Dang`, sizes recorded below.

## Primary Source

**S1 — YouTube transcript**: "The Most Overlooked $10K/Month Online Business Anyone
Can Start (Even With a 9-5)" by Patrick Dang, `https://www.youtube.com/watch?v=lHfsW17Z7g0`,
transcribed by Merlin AI. Captured inside a claude.ai extraction conversation titled
"💎💰 Patrick Dang | The Most Overlooked $10K/Month Online Business Anyone Can Start
(Even With a 9-5)", created 2025-12-23T15:24:15Z, message_count 16, word_count 20,938.
Archive path: `_archive/claude-export-2026-07-01.tar.gz` →
`claude-export/normalized/conversations/7ea68873-caed-4cd8-af6f-a95e19d1aa7f.md`
(117,861 bytes, confirmed via `tarfile.getmember().size` 2026-07-18). Status: **VERIFIED
as a real Patrick Dang source** — contains the raw transcript body plus the Claude-side
MES 3.0 extraction artifacts that became this skill's SKILL.md / genius.md.

## Related conversations found in the same archive search (not used as primary grounding)

Three additional conversations matched "Patrick Dang" in the same tarball scan and were
opened to check for unique material; each turned out to be a duplicate pass, a partial
re-run, or a lower-quality re-extraction of the same underlying YouTube transcript, not
new source content:

- `claude-export/normalized/conversations/47775165-f134-441b-8bd0-41c646459ce6.md`
  (66,145 bytes) — same video, earlier/partial extraction pass.
- `claude-export/normalized/conversations/89f8a04d-9480-44d1-85c8-82f0709099d6.md`
  (59,745 bytes) — same video, another extraction pass.
- `claude-export/normalized/conversations/d4094ca5-d5d0-423a-aff9-cd5780d38a2d.md`
  (81,057 bytes) — a **different** Patrick Dang source: a ~130-minute interview with
  host Calum Johnson, embedded inside an "AI Consultant Playbook" extraction thread.
  Not confirmed as material actually used to build this skill's patterns (the skill's
  patterns all trace cleanly to S1); flagged UNCONFIRMED as a contributing source
  rather than claimed.

## Claim-by-Claim Verification (genius.md)

| Claim / Pattern | Label | Evidence |
|---|---|---|
| Gold Mine Positioning — "sitting on a gold mine" | VERIFIED | Verbatim phrase found twice in S1 ("most people are sitting on a gold mine"; "he was always sitting on a gold mine"). |
| Missing-Boxes Diagnosis | VERIFIED | S1: "when you look at these boxes, think of it like each box is a skill you need to start a business." |
| The Transformation Sentence | VERIFIED | S1: "I help this specific kind of person go from this kind of problem to this result... using my special process" (Brandon example); "I help tech professionals land 120K plus sales roles in 60 days at the top 1% of tech companies." |
| "Cannot be explained in one sentence" call-ending anecdote | VERIFIED | S1 verbatim: "I can't you know what I do cannot be explained in one sentence. And then at that point, you know, I pretty much just ended the call." |
| Restaurant, Not Kitchen | VERIFIED | S1 verbatim: extended restaurant/kitchen metaphor, "nobody cares how the food is made... they only care about the results." |
| One-One-One Constraint | VERIFIED | S1 verbatim: "one traffic source, one conversion method, and one offer"; platform-spreading passage below. |
| All Roads Lead to Long-Form (3-day short-form death, binge behavior) | VERIFIED | S1 verbatim: "3 days later that video is dead"; "they binge watch you, then they'll watch like 10 videos in a row." |
| Charge by Result, Never by Hour | VERIFIED | S1 verbatim: "you never want to charge by the hour. This is the biggest mistake I see." |
| High-Ticket First — Udemy 193,000 learners, 70,000 reviews | VERIFIED | S1 verbatim: "I've got 193,000 learners or students, 70,000 reviews." |
| High-Ticket First — Yvon: 693 subscribers, 3,528 LinkedIn followers, $7K/month | VERIFIED | S1 verbatim: "she only has 693 YouTube subscribers and 3,528 LinkedIn followers and she makes $7,000 per month." (genius.md rounds 3,528 → "3,528" exact figure now used, previously approximated as "3.5K.") |
| Past-Self Avatar + origin story (matcha ice-cream flop, younger/Asian contrast) | VERIFIED | S1 verbatim quotes on the matcha shop and on being "younger, closer to the trenches... I'm Asian, right?" |
| Flywheel of Boring Iteration | VERIFIED | S1 verbatim: "version one's not going to look pretty... do this like five times, 10 times... it's going to become a machine"; impatience quotes below. |
| Follower-DM Hack | VERIFIED (core mechanic) / LIKELY (exact phrasing "experience the DM as an honor") | S1 verbatim: "Hey man, are you here for the content, or are you looking to..."; "I've been watching Patrick's content for the last like 3 months and now he just DM'd me." The word "honor" is this skill's own gloss on that reaction, not a Dang quote — treat as interpretive, not verbatim. |
| Sell the Call Itself | VERIFIED (core mechanic) / LIKELY (bracketed inner quotes) | S1 verbatim: "I'm not sure if I have the money for this... I don't want to disappoint them... booking that call is like a big step." The bracketed phrase "they'll pressure me" in earlier drafts of this pattern is a paraphrase, not a located verbatim quote — removed/softened in this repair pass. |
| Positioning by Contrast, Not Superiority | VERIFIED | S1 verbatim: "I'm Asian, right?... universities in Asia... play my videos in their class"; "they don't even send any cold emails anymore." |
| Taste Is a Closing Variable | VERIFIED | S1 verbatim: "the fonts, the colors, your color grade... I'm going with a guy with taste because I connect with that more personally." |
| Social Proof as Mini-Documentary ("This is Brandon...") | VERIFIED | S1 verbatim: "this is Brandon and 30 days ago he had no idea how to do this and now he's making $10,000 per month." |
| Personal Network Before Personal Brand — Tyler, $56K/60 days | VERIFIED | S1 verbatim: "he was able to make 56K in 60 days doing this... went from... taking 10 sales calls at his sales job and closing none to making 56K in 60 days." |
| AI-Assisted Is the Offer Multiplier — "army of five full-time employees" | VERIFIED | S1 verbatim: "it's like having an army of five full-time employees helping you out with the sales, the marketing, the delivery of the service." |
| Brandon offer example, 10K first 30 days, 15 years construction VP | VERIFIED | S1 verbatim: "made 10K the first 30 days of working with me"; "he's been working in this construction business for like 15 years and he's a VP." |

## Claim-by-Claim Verification (Anti-Patterns, new section this pass)

All seven anti-pattern items are VERIFIED verbatim quotes from S1 — see inline citations
on each bullet in `genius.md`. No anti-pattern item in this pass carries an UNCONFIRMED
or fabricated quote; each was located via targeted Python regex search of the extracted
transcript text before being written into the skill.

## SKILL.md Quick Reference claims

The Quick Reference bullets in SKILL.md (flywheel, skill-audit questions, transformation
sentence, restaurant/kitchen, one-one-one, charge-by-result, high-ticket-first,
past-self-avatar, impatience failure mode) all restate patterns already verified above
against S1. No new unverified claims were introduced there this pass; SKILL.md was left
unmodified.

## Labels used

- **VERIFIED** — a matching verbatim quote or exact figure was located in S1 by direct
  text search this pass.
- **LIKELY** — the underlying mechanic/claim is grounded in a verbatim S1 passage, but a
  specific bracketed sub-phrase in the skill's prose is this skill's own paraphrase/gloss
  rather than a word-for-word Dang quote.
- **UNCONFIRMED** — not located in any source opened this pass (used only for the d4094ca5
  Calum Johnson interview's relationship to this skill's specific patterns, above).
