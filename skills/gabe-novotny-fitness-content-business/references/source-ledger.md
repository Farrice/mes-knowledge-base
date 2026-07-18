# Gabe Novotny — Source Ledger

Repair pass 2026-07-17 (Wave 3 Lane 4 Batch 6). This ledger exists because
`extractions/` contains no matching directory for this skill — see "Provenance
status" below for the full recovery trail before trusting any claim in
`genius.md` or `SKILL.md` at face value.

## Provenance status (verify-absence, not assert-absence)

- `SKILL.md` frontmatter states `source: claude.ai export 2026-07-01`.
  `ls extractions/ | grep -i "novotny\|gabe"` → 0 of 200+ extraction
  directories matched (only an unrelated coincidental hit inside
  `extractions/rafa-conde/transcript.txt` that on closer inspection —
  `grep -n -i "novotny" extractions/rafa-conde/transcript.txt` — returns
  zero lines; the earlier case-insensitive directory match was a false
  positive from `grep -ril`'s handling of a binary-adjacent byte sequence,
  not an actual mention). Checked 2026-07-17.
- `_active/codex-harvest-2026-06-11/` (full mirrored repo snapshot) was
  checked the same way: no `extractions/gabe*` or `*novotny*` directory;
  a `grep -ril "novotny\|gabe"` hit inside a `research_outputs/.../gemini.json`
  file was verified to be a false positive (the string only appears inside a
  base64-encoded PNG blob, confirmed with `grep -a -i novotny <file> | grep -v '"data"'`
  returning zero lines).
- `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) — the
  already-imported claude.ai conversation export referenced in project memory
  (`project_claude-export-harvest.md`) — was checked by **content**, not
  filename, per the envelope's hard rule. `_active/claude-export/harvest/census-full.json`
  (a pre-built census of the same export, already on disk, 10 MB total for
  `_active/claude-export/`) contains a real entry: `{"expert": "Gabe Novotny",
  "count": 2, "max_richness": 8, "fitness": true, "ids": ["1d2c702c-9525-4b02-a10b-524afcae536e",
  "5827dfe6-b140-4cca-bc0d-e9354f6845bd"]}`. Cross-referencing those IDs against
  `_active/claude-export/index.json`'s `conversations` array resolved both to
  real, titled conversations:
  - `5827dfe6-b140-4cca-bc0d-e9354f6845bd` — "Gabe Novotny: How to make
    $10k-$25k month as an online fitness coach (no ads or cold dm)",
    created 2025-06-12, 6,147 words, 32,113 chars.
  - `1d2c702c-9525-4b02-a10b-524afcae536e` — "Coach Cooz: Gabe 'Solar
    Content System'", created 2025-09-21, updated 2025-10-14, 43,359
    words, 269,385 chars.
  Both conversations' `md_path` pointed at `.tmp/claude-export/normalized/conversations/*.md`,
  which no longer exists on disk (`.tmp/` is never committed). Both files
  **do** exist inside the tarball (`tar -tzf _archive/claude-export-2026-07-01.tar.gz
  | grep -i "1d2c702c\|5827dfe6"` → both paths present) and were extracted
  for this repair pass. Actual extracted sizes, confirmed with `wc -c`
  (not `wc -l`, per the fleet's provenance rule): `1d2c702c-...md` =
  271,054 bytes; `5827dfe6-...md` = 32,706 bytes. Both files were read in
  full (not sampled). Neither is empty, truncated, or corrupted.
- This means: real primary source material exists and was recovered — the
  "no extraction folder" state was a filing gap (the conversation was
  captured in the claude.ai export harvest, never promoted to
  `extractions/gabe-novotny/`), not an absence of source. Recovered copies
  live at `.tmp/wave3-lane4-b6/gabe-src/claude-export/normalized/conversations/`
  for the duration of this repair session.

## What the two conversations actually contain

Both conversations are MES 2.0 extraction requests: the user pastes a raw
YouTube auto-transcript (via Merlin AI) and asks Claude to run
`/extract-deep --ultra-think > /architect-enhanced > /transcend`. That means
each conversation contains two very different kinds of text, and they carry
different evidentiary weight:

1. **The raw pasted transcript itself** (verbatim YouTube captions, with
   timestamps) — this is Gabe's actual spoken words, unfiltered. Highest
   confidence source in this ledger.
2. **Claude's own extraction commentary** (Content Assessment blocks,
   "Genius Patterns," "Hidden Gems," expert-prompt artifacts) — this is a
   PRIOR AI's inference layered on top of the transcript. Some of it
   quotes the transcript verbatim (traceable, high confidence); some of it
   elaborates, invents illustrative numbers, or names things Gabe never
   named (untraceable, must be labeled UNCONFIRMED even though it now
   lives inside this skill's own `genius.md`).

Four distinct raw video transcripts are embedded across the two conversations:

| # | Video title | URL | Where |
|---|---|---|---|
| A | "How To Make $10k-$25K Month As An Online Fitness Coach (No Ads or Cold DM)" | youtube.com/watch?v=9Kao4nSgMHQ | `5827dfe6-...md`, lines 22-596 |
| B | "How I Make My Content REAL AS F*CK \| The 'Solar System' Content Framework" | youtube.com/watch?v=WFT_mynWEUc | `1d2c702c-...md`, lines 32-343 |
| C | "FITNESS COACHES SUCK AT BUSINESS" | youtube.com/watch?v=4ttM5qWnr2o | `1d2c702c-...md`, lines 1796-3196 |
| D | "I Helped My Friend Build a $400K/Year Coaching Business in Just 25 Minutes" | youtube.com/watch?v=mZ9yJ1juFic | `1d2c702c-...md`, lines 4178-4809 |

Video D covers Gabe coaching a media-freelance client (Pablo) on offer
construction (VSSL-style ICP/outcome/timeframe naming, "the rebound
method") — real Gabe material, but a different sub-domain (offer design,
not the Instagram content funnel) from what this skill currently covers.
Not drawn on for this repair pass beyond confirming it's genuine Gabe
material; flagged here for a future extraction pass rather than force-fit
into the current pattern set.

## Claim-by-claim labels (genius.md + SKILL.md)

| Claim | Label | Basis |
|---|---|---|
| "$253,723" 2023 annual revenue, 98% organic Instagram, no ads/cold DMs/website leads | VERIFIED | Verbatim in Video A transcript, ~0:00-0:19: "in 2023 my fitness coaching company did $53,723 [sic, garbled OCR reads as '$253,723' given the spoken cadence and the '2' fragment on the prior line] ... 98% of my Revenue came from Instagram... I didn't run ads I didn't do any cold DMs I didn't generate leads through my website." The exact digit sequence is slightly OCR-garbled in the auto-caption (line breaks split "$253,723" across two caption lines: "did $" / "53,723"), but the surrounding sentence is unambiguous and SKILL.md/genius.md's "$253,723" figure matches the standard reading of this line. |
| genius.md intro: "Built a $530K+/year coaching company" | **UNCONFIRMED — likely wrong** | "$530K" or "530" does not appear anywhere in either recovered transcript. The only annual-revenue figure either transcript states is $253,723 (Video A, VERIFIED above). This ledger recommends the intro be corrected to the verified figure in a future pass; left as-is this repair pass per the additive-first/no-rewrite boundary, flagged here so it is not mistaken for confirmed. |
| SKILL.md: "$1,000-$4,000 coaching offer" | **UNCONFIRMED — inconsistent with source** | Neither "$1,000" nor "$4,000" appears in either transcript. Video A (~16:07-16:34, ~19:56-20:35) states the coaching package price directly and repeatedly as "$2,500," with total contract value discussed up to "5K" (~20:31-20:35: "this could be anywhere from 2500 to 5K"). The verified range is **$2,500-$5,000**, not $1,000-$4,000. Flagged for correction in a future pass. |
| "reels = attention, stories = nurture, DMs = conversion" three-part funnel | VERIFIED | Video A, ~0:34-0:39 and throughout: "if we break down Instagram right into three parts reals stories and direct messages." |
| "People spend the most Instagram time in the DMs" (Instagram-as-communication-app insight) | VERIFIED | Video A, ~0:57-1:15: "they actually did a study on Instagram and... the study showed that people spend the most amount of time on Instagram in the DMS." (Gabe cites "a study" but names no source — the claim that a study exists is Gabe's own assertion, not independently verified by this repair pass; the fact that Gabe says this is VERIFIED, the underlying study's existence is UNCONFIRMED.) |
| Temperature Zone Theory (Too Hot / Too Cold / Earth Zone, "Solar System" framing) | VERIFIED | Video B, ~4:23-9:59, extensive verbatim match — see Anti-Patterns section of `genius.md` and `PROVENANCE.md` for exact quoted lines. |
| "I never talk about something that I didn't actually experience in real life. I'm never giving advice based off of something I didn't do. I'm only telling my own story." | VERIFIED | Verbatim, Video B ~9:59-10:11. |
| "If you have a tattoo on your face, show it." | LIKELY (paraphrase, not verbatim) | Video B ~8:50-8:54 says "if you have something that's like different about you or a quirk or a tattoo on your face you should be showing it" — the skill's phrasing is a tightened paraphrase of this line, not a direct quote; the underlying claim is real and sourced. |
| The Value Jar Principle ("jar full of money") | VERIFIED | Video B ~10:52-11:03: "imagine you had a Jar full of money and people were just coming in and putting their hand in the jar and taking money out of it." |
| CPR — Cash Per Reel Economics: the mechanic (revenue ÷ reels = a trackable unit) | LIKELY (mechanic consistent, term not confirmed) | No transcript uses the phrase "CPR" or "cash per reel." The underlying philosophy — track the data, don't judge off feelings, use volume to generate a rate you can then optimize — is well-supported (Video A ~23:36-24:35: "the difference between this and this [is] the data was being tracked... 1% improvements based off data not feelings"). The specific "CPR" branding appears to be the extraction assistant's own naming, not Gabe's. |
| CPR benchmark figures: "Evan $617/reel ($21K on 34 reels), Zach $547/reel ($18.6K on 34 reels)"; SKILL.md's "$300-$600/reel" range | **UNCONFIRMED — fabricated figures, not in source** | Checked exhaustively: `grep -n -i "617\|547\|Zach\|34 reels\|cash per reel\|per reel"` across both full transcripts returns zero matches for any of these numbers or the name "Zach." "Evan" IS a real client named in Video A (~22:41-24:53) with a real progression (first month <$10K, second month "$12" [thousand, garbled], third month higher — exact third figure is OCR-garbled as "[phone]" in the caption and unreadable), but none of the specific per-reel dollar figures or the "34 reels" count appear anywhere. This is the single most important finding of this repair pass: these figures were invented in a prior extraction pass and should not be treated as verified Gabe case studies. See the matching `Provenance flag` inserted directly into `genius.md`'s CPR pattern. |
| DFV Reel Architecture (Hook 0-5s / Social Proof 5-25s / Actionable Advice 15-45s / CTA 45-60s), "80 cents of your dollar" Ogilvy reference | UNCONFIRMED (verbatim to skill file, not to a recovered transcript) | This specific 4-part timing breakdown and the Ogilvy attribution do not appear in either recovered transcript. Video C discusses hooks and DM openers extensively but not this exact timed structure. Likely from a source video not recovered in this pass (Gabe references "an extensive training on this" at Video C ~2:54-2:57 that may be the actual source, not captured in either recovered conversation). |
| "Quantity first, then iterate" / training-split analogy, "2-3 reels/day minimum" | VERIFIED | Video A ~1:53-2:03 (training-split parallel) and ~3:51-3:55 ("I like to suggest that you start with two to three reals a day"). |
| Stories: "5-20/day," "reality TV show," 24-hour urgency | VERIFIED | Video A ~8:51-8:53 ("5 to 20 stories a day"), ~10:03-10:06 ("our reality TV show"), ~10:52-10:59 (24-hour clock / built-in urgency). |
| The Doctor Frame (diagnose, don't educate) | VERIFIED | Video C ~5:09-5:48 (doctor/prescription framing) and ~6:29-7:16 (overeducating warning — also used as an Anti-Pattern anchor, see below). |
| The 17-Second Strategic Pause | **UNCONFIRMED — not in source, traced to a prior AI's own invention** | Exhaustive check: "17.second\|17 second\|seventeen\|pause\|silen\|wait.*second\|count to" returns zero hits in the raw Video C transcript (lines 1796-3196, the actual DM/frame-control training call this pattern claims to come from). The phrase first appears in the SAME conversation's own extraction commentary, explicitly labeled "Hidden Gem" (Video A's conversation: "Hidden Gem: The '17-second pause' technique he uses (mentioned subtly) but never fully develops") and later elaborated into a full pattern with its own Execute/Success Metric by the prior extraction pass — i.e., a previous AI invented a technique, attributed it to Gabe, and it propagated into this skill's genius.md as if verified. See the matching `Provenance flag` inserted directly into `genius.md`. |
| Instagram Is a Communication App (Hidden Knowledge insight) | VERIFIED | Same basis as the DM-time-spent claim above (Video A ~0:57-1:15). |
| The Rick Principle — $6,000 client from one initiated DM after a poll vote | VERIFIED | Video C ~15:29-17:11, extensive verbatim match: "I had a client named Rick... it was like over $6,000... he goes, 'Yeah, man. If you never messaged me that day, uh, when I voted on that poll, I would never be here.'" |
| The Anti-Diary Principle | VERIFIED | Video B, same basis as the "Too Hot" Anti-Pattern anchor below; the "adult diary that makes no money" phrasing is VERIFIED verbatim in Video A ~14:00-14:06: "they turn their Instagram into a into an adult diary that makes no money." |
| The Suitcase of Gold ("carrying $1M in value") | VERIFIED (paraphrase of a real analogy) | Video C ~4:21-4:36 uses the analogy with "a suitcase with a million dollars in it," not "$1M" verbatim, but the same figure and the same rhetorical point ("you have something of value"). |
| Never Say "Free" (swap for "give"/"provide") | UNCONFIRMED (verbatim to skill file, not to a recovered transcript) | Not found in either recovered transcript. Thematically consistent with Gabe's premium-positioning stance elsewhere (the doctor frame, the suitcase-of-gold conviction requirement) but the specific "never say free" rule was not independently locatable in this pass. |
| The 90-Day Trust Window (month 1/2/3 progression, "26 days without sales is normal") | VERIFIED | "26 days" is verbatim in Video A ~17:57-18:08 (see math below); the month-1/2/3 client-progression pattern is verbatim in Video A ~22:41-24:53 (Evan's story). The specific "Days 1-30 pure value, 31-60 soft positioning, 61-90 direct invitations" staging is this skill's own structuring of the underlying pattern, not a Gabe quote — reasonable inference, not verbatim. |
| "Four deals a month = $10,000" reverse-engineering math | VERIFIED | Video A ~16:07-16:34: "$2500 so 4 * 25... equals $10,000." |
| All six Anti-Pattern bullets added in this repair pass | VERIFIED (verbatim quotes) | Exact quotes and timestamps cited inline in `genius.md`'s new "Anti-Patterns Gabe Would Reject" section and cross-indexed in `PROVENANCE.md`. |

## How to extend this ledger

If a future pass locates the source for the DFV Reel Architecture's exact
timing structure, or independently verifies the "Never Say Free" rule, or
recovers the OCR-garbled exact digits in Evan's third-month revenue figure,
re-run this table against the new material before upgrading any UNCONFIRMED
label — do not upgrade on inference alone. The two figures flagged
**UNCONFIRMED — fabricated** (CPR per-reel benchmarks, 17-Second Pause)
should not be silently removed from `genius.md` per this fleet's
additive-first boundary; they are flagged in place so a future pass with
write authority over `skills/` can make the call to correct or remove them.
