# Source Ledger — kallaway-ai-content-engine

Claim-by-claim verification for every factual assertion in `SKILL.md` and `genius.md`.
Labels: **VERIFIED** (verbatim or numerically exact match found in primary source) /
**LIKELY** (concept/number confirmed, a supporting detail — name, attribution, or
framing — is either paraphrased beyond what the source states or drawn from general
knowledge, not the transcript itself) / **UNCONFIRMED** (no matching text found in any
source file this repair pass could read; treat as extractor synthesis, not a Kallaway
quote).

## Critical Finding (read first)

`genius.md`'s original citation named the source as *"Three Biggest Social Media
Shifts" (YouTube, 2026)*. That phrase is not a video title — it is Kallaway's own
in-video description of the video's content ("I'm going to walk through the three
biggest social media shifts happening right now," transcript @ 00:00:54). The material
was **not** found anywhere under `extractions/kallaway/` or
`extractions/kallaway-content-system/`. Both directories were read in full and grepped
(`AI\b`, `sandcastle`, `transactional`, `goldilocks`, `trust equation`, `grandfather`,
`AI-skeptic`) — zero matches relevant to this skill's Patterns 1-6. File sizes,
confirming these are real, non-empty, off-topic files, not silently-assumed-absent:

| File | Size | Actual topic |
|---|---|---|
| `extractions/kallaway/extraction-report.md` | 6,971 bytes | Desire-based hook / relatability-constraint copywriting |
| `extractions/kallaway/internet-money-machine-extraction.md` | 12,864 bytes | Revenue-model breakdown ("Internet Money Machine") |
| `extractions/kallaway/internet-money-machine-transcript.txt` | 24,657 bytes | Same — full transcript |
| `extractions/kallaway/transcript.txt` | 34,072 bytes | "Illusion of Novelty" storytelling framework |
| `extractions/kallaway/word-mastery-extraction.md` | 16,292 bytes | Articulation / voice-pocket editing craft |
| `extractions/kallaway-content-system/transcript.txt` | 43,221 bytes | "I Hated Social Media... Until I Learned THIS System" (video B9l9TRhu5Vw) — content-systems workflow, different video, no AI-Enabled Creativity or Goldilocks material |
| `extractions/kallaway-content-system/B9l9TRhu5Vw.en-orig.vtt` | 398,725 bytes | Raw VTT of the same B9l9TRhu5Vw video |
| `extractions/kallaway-content-system/extraction-report.md` | 4,963 bytes | Extraction summary for B9l9TRhu5Vw |
| `extractions/kallaway-content-system/integrity-patch.md` | 5,108 bytes | Trend-hook-engine build-shape notes, not source transcript |

The real primary source for Patterns 1-6 was located at
`_active/codex-harvest-2026-06-11/extractions/video-context/ImzoNTrgvFg/` (a prior Codex
harvest import, not indexed under `extractions/kallaway*` — this same mismatch was
independently caught and documented by the sibling `kallaway-social-commerce` repair,
which draws from the identical source video):
- `transcript.txt` — 107,458 bytes, 17,043 words, full line-timestamped transcript, read in full for this repair.
- `metadata.json` — 3,343 bytes; confirms title **"The NEW Way to WIN on Social Media in 2026,"** uploader/channel **Kallaway**, `upload_date`/`publish_date` **20260429**, URL `https://www.youtube.com/watch?v=ImzoNTrgvFg`, duration 24:14, and a description timestamp block confirming `0:59 Trend 1: AI-Enabled Creativity` — matching this skill's domain exactly.

Every VERIFIED/LIKELY label below is anchored against that `transcript.txt`, cross-checked with `metadata.json`.

### Pattern 7 — source search record

Pattern 7 ("AI Trust Goldilocks Window") cites *"What Happens When AI Takes Over Social
Media?" (claude.ai export tranche 2, 2026-07-10)*. Searched for this pass:
`grep -rli "goldilocks\|grandfather" --include="*.md" .` (repo-wide, excluding
node_modules) — zero hits outside the two `kallaway-ai-content-engine/genius.md` copies
(this skill's own file and its untouched worktree mirror). Searched
`_active/claude-export/` (INDEX.md, canonical-systems.json, index.json, state.json,
routed-decisions.json, harvest/, reports/, triage/) by filename and grep — no
Goldilocks/trust-grandfathering content found. Searched `_archive/claude-export-2026-07-01.tar.gz`
by listing (`tar -tzf`) filtered for `kallaway` — zero matching entries. No file
anywhere in the readable repo matches this citation. **Pattern 7 is UNCONFIRMED in
its entirety** — every sub-claim inside it (the ~1-2% AI-content-density figure, the
~20-25% threshold, the Trust Equation decomposition, the owned-channel economics)
inherits that UNCONFIRMED status. This does not mean the claims are false — only that
this repair pass could not locate the source file to verify them.

---

## Claim Ledger

| # | Claim (as stated in genius.md / SKILL.md) | Label | Source anchor | Note |
|---|---|---|---|---|
| 1 | Real source is Kallaway, "The NEW Way to WIN on Social Media in 2026," published 2026-04-29, YouTube ID ImzoNTrgvFg | VERIFIED | `ImzoNTrgvFg/metadata.json` | Title, uploader, upload_date, webpage_url all present verbatim in metadata.json. |
| 2 | "I'm going to walk through the three biggest social media shifts happening right now" | VERIFIED | transcript.txt @ 00:00:54–00:00:59 | Verbatim. This is the origin of the original (inaccurate) citation phrase. |
| 3 | AI-Enabled Creativity: "using AI to eliminate the boring task and free up more of your time for creativity" / "I call this AI-enabled creativity. The AI is clearing space so you can be more creative." | VERIFIED | transcript.txt @ 00:01:06–00:01:15, 00:01:55–00:02:00 | Verbatim, both clauses. |
| 4 | "Most people assume using AI means fully replacing creative thinking... robotic, sanitized, soulless content... but that's kind of a lazy way of thinking about it" | VERIFIED | transcript.txt @ 00:01:17–00:01:30 | Verbatim. |
| 5 | "requires creative thinking and then also a bunch of redundant transactional task that most of us don't want to spend time doing. Things like research and scripting and editing and captions." | VERIFIED | transcript.txt @ 00:01:36–00:01:44 | Verbatim; this is the direct source of Pattern 1's Transactional column framing. |
| 6 | Pattern 1 Transactional-Creative Split table (research, outlier ID, hook clustering, data analysis, scripting structure, captions, analytics vs. take, perspective, hook angle, reaction, voice, emotional calibration, strategic interpretation) | LIKELY | transcript.txt @ 00:01:36–00:02:31 (general area) | The categories of "research/scripting/editing/captions" as transactional and "your unique take... that's where your authenticity comes from" as creative are both verbatim-grounded (see #5, #7). The specific 7-item/7-item table format is extractor synthesis organizing verified concepts, not a table Kallaway states on camera — treat the table shape as LIKELY, the underlying claims as VERIFIED. |
| 7 | "If you're letting AI do the thinking and the ideating, that's where your content gets stale and robotic. But if you use the data from AI and then creatively think, that's the winning formula." | VERIFIED | transcript.txt @ 00:05:31–00:05:42 | Verbatim, both sentences. |
| 8 | "Your unique take, that is the creative part. That's where your authenticity comes from. You don't want to outsource that to AI." | VERIFIED | transcript.txt @ 00:02:25–00:02:31 | Verbatim. |
| 9 | Channel list "10-30 top creators... hand-curated by taste, not algorithm" / "I curated this list by hand cuz I know who I like" | VERIFIED (curation claim) / LIKELY (range) | transcript.txt @ 00:03:15–00:03:19 (quote), 00:03:26–00:03:28 (range) | Quote is verbatim. Transcript states "10, 20, 30 channels" as a channel-list-size example, not a stated "10-30" range — genius.md's phrasing is a reasonable paraphrase but label the specific "10-30" framing LIKELY, not VERIFIED. |
| 10 | Sandcastles pipeline: sort by outlier score, filter last 3 months, deep analyze (transcript, topic, seed, hook format, storytelling format, visual format, stats), export to CSV, upload to Claude Co-work | VERIFIED | transcript.txt @ 00:03:28–00:04:19 | Verbatim sequence match, including the specific field list ("the transcript, the topic, the idea, the seed, the exact hook, the hook format, the storytelling format, the visual format, plus all the stats"). |
| 11 | The exact bucketing prompt ("bucket them as topic categories and rank them based on which ones have the most views... within each topic bucket, break out each separate topic as a one-liner... include the original link") | VERIFIED | transcript.txt @ 00:04:27–00:05:00 | Near-verbatim (genius.md paraphrases lightly but preserves every instruction clause). |
| 12 | "Now I have a hit list of all the best topics validated by data in just 2 minutes" | VERIFIED | transcript.txt @ 00:05:12–00:05:17 | Verbatim ("2 minutes" figure confirmed). |
| 13 | "In a niche, certain topics always outperform other topics. That's not me saying that. That's just the data showing it." | VERIFIED | transcript.txt @ 00:02:33–00:02:39, 00:02:44–00:02:47 (second clause) | Verbatim, near-adjacent lines combined. |
| 14 | "Topics like hooks, psychology, and storytelling outperform ideation, strategy, and editing in the social media marketing niche" | VERIFIED | transcript.txt @ 00:02:39–00:02:44 | Verbatim: "for example, hooks, psychology, and storytelling typically outperform things like ideation, strategy, and editing." |
| 15 | Hook clustering: "broadly bucket the hooks into types and then again cluster by the actual hook format and rank them... make a list of the top 10 performing hooks... write new hooks for me... 10 fresh hooks in the formats validated by the data" | VERIFIED | transcript.txt @ 00:06:05–00:06:30 | Verbatim sequence. |
| 16 | "It will cluster them, it will give you the top hooks, and then it will save that as a skill for you to just run over and over" | VERIFIED | transcript.txt @ 00:06:32–00:06:40 | Verbatim; source of Hidden Knowledge #3 and Signature Move "The Compound Dataset." |
| 17 | "There's nothing in the world that can do content research like this this fast" | VERIFIED | transcript.txt @ 00:06:44–00:06:49 | Verbatim; source of Hidden Knowledge #4 "The Speed Moat." |
| 18 | "I purposely left in the human in the loop step of me seeing the topic and [reacting]" / distancing from "AI gurus" claiming workflows "just print content automatically" | VERIFIED | transcript.txt @ 00:06:51–00:07:03 | Verbatim, both clauses (the "AI gurus" line precedes the "human in the loop" line in the same breath). |
| 19 | Compound workflow: "I also use the same data for deep dive research... for scripting, for hook writing... for captions, for analytics, for strategy. I've all these different Claude workflows built out using this data." | VERIFIED | transcript.txt @ 00:07:38–00:07:52 | Verbatim; the 7-row Pattern 5 table (Topic Mining/Hook Writing/Deep Dive/Scripting/Captions/Analytics/Strategy) is a faithful reorganization of this exact list into a table — VERIFIED content, LIKELY table format. |
| 20 | "The Creativity Paradox," "The Data Confidence Effect" (Hidden Knowledge #1-2) | UNCONFIRMED | — | Not stated on camera in these terms. Both are reasonable inferences from VERIFIED claims #3-4 and #12 but are extractor-authored interpretive labels, not Kallaway statements. Do not present as direct quotes. |
| 21 | Pattern 7 (AI Trust Goldilocks Window) — all sub-claims: ~1-2% AI-content density, ~20-25% threshold, Trust Grandfathering mechanic, 5-lever Trust-Building Playbook, Off-Ramp Imperative, 2026-2030 window | UNCONFIRMED | — | See "Pattern 7 — source search record" above. No source file located anywhere in the repo. Retained per additive-first repair rules but must not be cited as verified Kallaway content until the original claude.ai export tranche 2 (2026-07-10) is recovered. |
| 22 | Anti-Exemplar: "Prompting ChatGPT with 'write me a social media post about marketing' and posting whatever it generates" | N/A — not a provenance claim | — | Original skill-authoring synthesis, generalized from the VERIFIED anti-patterns (#4, #7, #18). No Kallaway quote implied; flagged in `genius.md` itself. |
| 23 | Signature Moves list, Expert-Specific Quality Rubric table, workflow tier structure | N/A — not a provenance claim | — | Standard skill-authoring synthesis (same practice as every skill in the roster), grounded in the VERIFIED patterns above but not itself a factual assertion about Kallaway requiring a label. |

---

## Files Read For This Verification Pass (with sizes)

| File | Size | Purpose |
|---|---|---|
| `skills/kallaway-ai-content-engine/SKILL.md` | 6,903 bytes | Pre-repair state |
| `skills/kallaway-ai-content-engine/genius.md` | 17,437 bytes | Pre-repair state |
| `extractions/kallaway/extraction-report.md` | 6,971 bytes | Ruled out as source |
| `extractions/kallaway/internet-money-machine-extraction.md` | 12,864 bytes | Ruled out as source |
| `extractions/kallaway/internet-money-machine-transcript.txt` | 24,657 bytes | Ruled out as source |
| `extractions/kallaway/transcript.txt` | 34,072 bytes | Ruled out as source |
| `extractions/kallaway/word-mastery-extraction.md` | 16,292 bytes | Ruled out as source |
| `extractions/kallaway-content-system/transcript.txt` | 43,221 bytes | Ruled out as source (different video) |
| `extractions/kallaway-content-system/extraction-report.md` | 4,963 bytes | Ruled out as source |
| `extractions/kallaway-content-system/integrity-patch.md` | 5,108 bytes | Ruled out as source |
| `extractions/kallaway-content-system/B9l9TRhu5Vw.en-orig.vtt` | 398,725 bytes | Ruled out as source (raw VTT, same different video) |
| `_active/codex-harvest-2026-06-11/extractions/video-context/ImzoNTrgvFg/transcript.txt` | 107,458 bytes | **Primary source — read in full** |
| `_active/codex-harvest-2026-06-11/extractions/video-context/ImzoNTrgvFg/metadata.json` | 3,343 bytes | Title/date/URL verification |
| `_active/codex-harvest-2026-06-11/extractions/video-context/ImzoNTrgvFg/video-context-ledger.md` | (spot-checked, opening rows) | Corroborating caption-level evidence |
| `_active/codex-harvest-2026-06-11/brain/.../kallaway-expansion-vision.md` | 10,158 bytes | Confirms this skill's own genesis document cites the same ImzoNTrgvFg source and video-date |
| `skills/kallaway-social-commerce/genius.md` | 20,006 bytes | Sibling skill — same source video, format/anchor-style reference only, not copied verbatim |
| `skills/kallaway-social-commerce/references/source-ledger.md` | (read in full) | Confirmed independent discovery of the same ImzoNTrgvFg mismatch by a different repair pass — cross-validates this finding |
| `_active/claude-export/` (INDEX.md, state.json, index.json, routed-decisions.json, harvest/, reports/, triage/) | directory scan + grep | Searched for Pattern 7's "claude.ai export tranche 2" — not found |
| `_archive/claude-export-2026-07-01.tar.gz` | tarball listing only | Searched (filtered `kallaway`) for Pattern 7 source — no matching entries |
