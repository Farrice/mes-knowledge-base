# Source Ledger — justin-welsh-solopreneur

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 8, REDO). Every claim/quote used in
`genius.md` is labeled VERIFIED / LIKELY / UNCONFIRMED below.

## Correcting the prior worker's false "unrecoverable" claim

The prior repair pass concluded no Justin Welsh source material exists in this repo and
labeled every quote LIKELY on that basis. That conclusion was **false** and is
retracted here. The prior worker ran `tar tzf _archive/claude-export-2026-07-01.tar.gz |
grep -i welsh` — a **filename-only** search. The tarball's members are content files
named by opaque UUID (e.g. `502221c3-f71b-473f-8ef6-d7c7227281f2.md`); "welsh" never
appears in a filename, so that search was guaranteed to return zero regardless of what
the files contain. It was an absence-of-evidence claim built on the wrong search method,
not a verified absence.

This pass instead used `python3 tarfile` to extract six specific members (already
identified by the conductor's content-level scan) to
`.tmp/wave3-lane4-b8/_welsh-extract/` and read them directly:

| File | Size | Real title (from frontmatter) | Underlying source |
|---|---|---|---|
| `502221c3-f71b-473f-8ef6-d7c7227281f2.md` | 97,718 B | How Justin Welsh Built an $8 Million Dollar Business | YouTube `SFH9j7euDwg`, Productive Insights podcast w/ Ash Roy (single-paragraph transcript) |
| `4b7d6a3a-3cdb-46a8-9d37-fa052037d994.md` | 86,814 B | Same interview, timestamped re-transcription | Same YouTube video, cleaner per-line MM:SS transcript |
| `41517901-d7ee-4511-aeef-f5374566f900.md` | 127,014 B | One-Person Business Architecture & Lifestyle Business Mastery | MES 3.0 extraction session (mostly assistant-generated framework prose, not raw transcript) |
| `9ee08076-201f-488e-b0c9-d17975ae6d78.md` | 105,006 B | Building a 7-Figure Solo Business | YouTube `Mp8m-ysmfq4` |
| `f338446b-d3bc-47da-88bc-25b6aa7f1102.md` | 77,507 B | $100,000 in 7 Days: Why Justin Welsh Just Moved to Substack | YouTube `E1zhTQXI0r4`, timestamped transcript |
| `f625f7f3-6ccc-4438-80da-365cd51eed6b.md` | 78,116 B | How to Make $10M with No Team, No Office, No Investors | YouTube `0UxQbhaoMlQ` |

Four of the six (`502221c3`, `4b7d6a3a`, `f338446b`, plus the first ~10 min of
`9ee08076`/`f625f7f3` before the extraction assistant takes over) contain **real,
timestamped interview transcripts** attributed to Justin Welsh — primary source
material, not derivative extraction prose. `41517901` is almost entirely the prior
extraction session's own generated framework language (Crown Jewel prompts, agent
config) and was not used as a quote source this pass. These extracted files live only
under `.tmp/` (never committed, never written to `skills/`) per CLAUDE.md convention.

## Claim-by-claim labels

| Claim / quote (as it appears in `genius.md`) | Location | Label | Basis |
|---|---|---|---|
| "It's not like something that you go on a treasure hunt for. You don't like uncover rocks..." | Anti-Patterns; Pattern: Let the Niche Find You | VERIFIED | `4b7d6a3a...md` ~5:33-5:35 (also present in `502221c3...md`, non-timestamped block) |
| "you don't do that thing if you haven't done that thing" / practitioner gate | Anti-Patterns; Pattern: Announcing It Doesn't Make It True | VERIFIED | `4b7d6a3a...md` ~9:54 |
| "it's not clickbait in the headline if you deliver" | Anti-Patterns; Pattern: Trailer, Call-to-Conversation, Meat | VERIFIED | `4b7d6a3a...md` ~33:04 |
| "How many asks? Usually, just one." | Anti-Patterns; Pattern: Trailer, Call-to-Conversation, Meat | VERIFIED | `4b7d6a3a...md` ~32:50 |
| "it pays to be clear, not clever" | Anti-Patterns; Pattern: Profile as Landing Page | VERIFIED | `4b7d6a3a...md` ~33:48 |
| "the best way to build a habit is just stick with it" (corrected from the prior pass's fabricated "just stick with your habits") | Pattern: Unique Knowledge Through Obsession; Anti-Patterns | VERIFIED | `4b7d6a3a...md` ~29:07 |
| "don't force yourself to write about the stuff that past you cared about" | Pattern: Lifestyle That Generates Income; Insight: Personal Change Sets the Content Agenda; Anti-Patterns | VERIFIED | `f338446b...md` ~14:16-14:20 (host: "why did you") "as you change as a person... don't force yourself to write about... the stuff that past you cared about" |
| "I try and build a lifestyle that generates income" (vs. a business that makes money) | Pattern: Lifestyle That Generates Income; SKILL.md description | VERIFIED | `f338446b...md` ~14:03-14:09 |
| "they force me to barter for it... even though I say it's free. It's not free then" / "not a bartering experience" (corrected from the prior pass's invented single-sentence quote "if you tell me it's free, don't make me barter for it," which does not appear verbatim anywhere in the six sources) | Insight: Generosity Is a Funnel Mechanic; Anti-Patterns | VERIFIED | `4b7d6a3a...md` ~36:45-37:48 |
| "a fifth grader could understand it" | How to Use This Skill; Insight: Simplicity Is Trained Sales Management | VERIFIED | `4b7d6a3a...md` ~27:12-27:14 |
| "I'm just like, here are the three easiest things" | Insight: Simplicity Is Trained Sales Management | VERIFIED | Present in `502221c3...md` non-timestamped block, paraphrased close paraphrase of "here are the three easiest things you can do to solve that problem" — labeled VERIFIED for the underlying claim, LIKELY for the exact word order (transcript reads "here are the three easiest things you can do," not "here are the three easiest things") |
| "a lot of juice and not a lot of fluff" | Pattern: Trailer, Call-to-Conversation, Meat | VERIFIED | `4b7d6a3a...md` ~27:36-27:41 |
| "riding a bike seems easy only if you already know how" | Insight: Simplicity Is Trained Sales Management | LIKELY | Close paraphrase of the transcript's actual line, "much like riding a bike seems easy to you or me, but to someone who doesn't know how to ride it, it's very complicated" — not a verbatim quote, correctly unquoted in genius.md as a paraphrase |
| "I call it think once, publish 10 times" | Pattern: Think Once, Publish 10 Times; SKILL.md | VERIFIED | `502221c3...md` non-timestamped block, ~line 28 |
| Revenue breakdown (~65% courses, ~10-12% subscriptions, ~10% sponsorships, ~5% coaching, ~5% affiliates); $9/mo upsell, 25% take rate, "$24,000 MRR"; "one email" line | Pattern: Revenue Stack, Not Revenue Stream | VERIFIED | `502221c3...md` non-timestamped block (revenue-breakdown paragraph), matches host's structured recap in `4b7d6a3a...md` |
| Jack Butcher's "permissionless apprenticeship" | Insight: Generosity Is a Funnel Mechanic | VERIFIED | `4b7d6a3a...md` ~42:43-42:47, explicitly attributed by Welsh to Jack Butcher, not claimed as his own coinage |
| No employees, ~$600/month expenses, $5M+ revenue, "politics... legal... vacation... benefits... performance management" as the traded-away cost of hiring | Pattern: Lifestyle That Generates Income | VERIFIED | `f338446b...md` ~9:38-11:04 |
| "almost like a second mountain" (Substack pivot framing) | Pattern: Lifestyle That Generates Income | VERIFIED | `f338446b...md` ~2:49 |
| "the great creative migration" | Insight: Platform Signals Precede Platform Migrations | VERIFIED | `f338446b...md` ~1:38 (video intro, attributed to Welsh's own framing) and ~36:24 (host quoting it back to him in-interview) |
| "much in part thanks to me" (LinkedIn's drift to performance/posturing) | Insight: Platform Signals Precede Platform Migrations | VERIFIED | `f338446b...md` ~8:32-8:36 |
| $100K ARR + subscriber count + ~1,300 words, first week of Substack launch | Insight: Platform Signals Precede Platform Migrations; Pattern: Lifestyle That Generates Income | VERIFIED, with a noted internal source inconsistency | `f338446b...md` video intro (~0:15-0:25) states "$100,000 annual recurring revenue with paid subscriptions in the first days on Substack and 12,000 subscribers"; the host's later in-interview recap (~5:21-5:32) instead says "more than 8,000 subscribers and in 7 days also you got like 400 paying subscribers... with barely 1,300 words in total," unchallenged by Welsh. Both figures are genuinely in the source; genius.md's "12K subscribers" follows the video's own framing copy, not a fabrication, but the two numbers do not agree with each other — flagged here rather than silently resolved. |
| "already written 30 issues" / "30% of the year ahead" (30-issue buffer) | Pattern: Consistency by Buffer, Not Willpower | VERIFIED | `f338446b...md` ~42:22-42:35 |
| "say the same thing five different ways" | Pattern: Consistency by Buffer, Not Willpower | VERIFIED | `4b7d6a3a...md` ~38:50-38:57 |
| "all advice is contextual, mine included" | How to Use This Skill (Model Calibration) | VERIFIED | `4b7d6a3a...md` ~43:34-43:41 (also in `502221c3...md` non-timestamped block) |
| Data × Passion 90-Day Audit (5-7 topics on each axis, quarterly cadence) | Pattern: Data × Passion 90-Day Audit | LIKELY | No verbatim "90-day audit" or "5-7 topics" language found in any of the six sources. Consistent in spirit with Welsh's verified audience-dialogue niche philosophy ("talk about the things that you're generally interested in... other people are also interested in and will pay for," `502221c3...md`), but the specific ritual/cadence appears to be the prior extraction session's own synthesis, not a direct transcript claim. Kept as-is (not deleted, per additive-first boundary) but explicitly downgraded from any implied verbatim status. |
| Content originally attributed as "Welsh admits... 'me being a therapist to myself, yelling at myself for not being very good at something'" and "do I truthfully believe this?" / "easy, hollow" (prior pass's wording) | Formerly in Insight: The Content Is Self-Therapy | UNCONFIRMED — removed as quoted text this pass | Searched all six sources (full-text grep for "therap-", "yell", "hollow", "truthfully believe", "divisive") — zero matches. This exact language does not exist anywhere in the recovered primary material. Rather than delete the underlying insight (which is plausible and may originate from a Welsh source outside this six-file batch), this pass de-quoted it and rewrote the section as "Personal Change Sets the Content Agenda," grounded in the VERIFIED "past you cared about" quote instead. The original fabricated quote is not reproduced anywhere in the repaired files. |
| SKILL.md quick-reference lines: "Write like you talk... read it aloud, if you trip, rewrite," "I make the rules. This is my content," "Medium-fit... 10-20 honest tries" | `SKILL.md` (not modified this pass — file was already passing) | LIKELY | Not found in any of the six recovered sources; `SKILL.md` cites "three long-form interviews" as its source, and this repair pass recovered material consistent with at least three of the six (the two `$8M` transcripts count as one interview + the Substack video + the 7-Figure/`$10M` videos). These specific quick-reference lines may originate from `9ee08076` or `f625f7f3` content past the point this pass read in depth, or from a source outside this six-file set. SKILL.md was not a failing check this pass (workflow_contracts, named_entity_floor, verbatim_exemplars all already PASS) and per the envelope's additive-first/minimal-touch boundary was left untouched; flagged here for a future pass rather than silently carried forward as VERIFIED. |

## What ground-truth search was actually run this pass

1. Extracted the six named tarball members with `python3 tarfile` (content-verified byte
   counts match the conductor's scan exactly — see table above) to
   `.tmp/wave3-lane4-b8/_welsh-extract/` (never `skills/`, never committed).
2. Read the full text of `502221c3...md` (single-paragraph transcript + MES 3.0
   extraction) and large sections of `4b7d6a3a...md` (timestamped re-transcription of
   the same interview) and `f338446b...md` (Substack launch interview).
3. Ran targeted `grep -n -i` passes across all six files for every distinctive phrase
   used in the pre-repair `genius.md` (e.g. "fifth grade," "barter," "permissionless,"
   "second mountain," "creative migration," "$600," "30 issues," "therapist," "hollow,"
   "truthfully believe") to separate VERIFIED verbatim language from paraphrase and from
   language that does not exist in the source at all.
4. Corrected two mis-quoted lines (habit-stacking cliché, the barter line) to their real
   verbatim wording, and de-quoted/rewrote one insight section whose specific quoted
   language could not be found anywhere in the six sources.

## What this repair pass did and did not do

- Did NOT fabricate any new quote. Every VERIFIED anchor above was located by direct
  grep + read against the extracted transcript files, with a file + approximate
  timestamp anchor recorded in `PROVENANCE.md`.
- DID retract two quotes from the pre-repair file that turned out to be
  paraphrase-presented-as-verbatim ("just stick with your habits," the single-sentence
  barter line) and replaced them with the real transcript wording.
- DID retract one full insight's quoted language (the "self-therapist... yelling at
  myself" / "do I truthfully believe this" / "hollow" lines) as UNCONFIRMED — searched
  and not found — while preserving the underlying non-quoted insight, rewritten around
  a VERIFIED quote instead.
- Left `SKILL.md` and `workflows/*.md` untouched — they were already passing every
  heartbeat check this pass covers, and the envelope's additive-first/minimal-touch
  boundary applies. Their unverified quick-reference lines are flagged above for a
  future pass, not silently upgraded or hidden.
