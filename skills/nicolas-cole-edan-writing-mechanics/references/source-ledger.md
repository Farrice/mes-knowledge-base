# Source Ledger — nicolas-cole-edan-writing-mechanics

## Primary Source

- **Video**: "The EDAN Writing Framework: Explanation, Narration, Action, Description"
- **Channel/Expert**: Nicolas Cole
- **Video ID**: `gAVbSZHwzNU`
- **Published**: 2026-05-01 · **Duration**: 33:38 (2018s per `metadata.json`)
- **Actual on-disk location** (VERIFIED, wc -c confirmed 2026-07-18): `_active/codex-harvest-2026-06-11/extractions/video-context/gAVbSZHwzNU/`
  - `transcript.txt` — 124,718 bytes, timestamped spoken transcript, full 33:38 read for this repair.
  - `metadata.json` — 3,749 bytes, YouTube metadata (title, uploader, upload_date, duration).
  - `video-context-ledger.md` / `.json` — 223,211 / 441,301 bytes, frame + evidence rows (not read for this repair; not needed — all anchors below are transcript-verified).
  - `analysis.md` — 2,275 bytes. `frame-notes.md` — 2,452 bytes. `uncertainty-report.md` — 422 bytes.
- **Note on path drift**: `references/source-map.md` (existing, passing file, not modified in this repair) points to `extractions/video-context/gAVbSZHwzNU/`, which does **not exist** at that path in the live repo — the package only exists under the `_active/codex-harvest-2026-06-11/` legacy-harvest mirror. This is a stale pointer, not an absent source: the transcript is real, large (124KB), and was read in full for this repair. Flagged in REPAIR-NOTES.md; not fixed here because `source_ledger` was already a PASSING check and source-map.md is outside this batch's failing-check scope.

## Claim-by-Claim Verification

| Claim / Quote Used | Status | Location |
|---|---|---|
| "write what you feel, write what you love, be honest on the page... bundled instructions" | VERIFIED | transcript.txt lines 336-344, timestamp 00:06:26-00:06:41 |
| "it's not just, oh, I do a paragraph of explanation... extremely beginner way of thinking about it" | VERIFIED | transcript.txt lines 400-412, timestamp 00:07:42-00:07:55 |
| Nikolai Gogol / Anton Chekhov, Russian literature, description over explanation | VERIFIED | transcript.txt lines 620-632, timestamp 00:11:54-00:12:22 (transcript auto-caption renders "Nikolai Gole" — corrected to the real author Nikolai Gogol; "Anton Czechov" corrected to standard spelling Anton Chekhov) |
| "two pages describing a doorknob... tends to go awry" | VERIFIED | transcript.txt lines 748-760, timestamp 00:14:33-00:14:57 (auto-caption "doorork knob" is a caption artifact; quoted as "doorknob") |
| "I took a step forward and then I took another step... every action is consequential" | VERIFIED | transcript.txt lines 819-834, timestamp 00:16:09-00:16:23 |
| "let me just have something happen for the sake of happening" | VERIFIED | transcript.txt lines 836-844, timestamp 00:16:33-00:16:41 |
| Narration as king/queen chess piece, "last resort," "two most valuable pieces" | VERIFIED | transcript.txt lines 1094-1131, timestamp 00:21:34-00:22:19 |
| "We hadn't talked all summer... it hurts the people getting divorced" (divorce narration passage) | VERIFIED | transcript.txt lines 1014-1068, timestamp 00:19:57-00:20:12 |
| "abusive alcoholic father... moment of growth... moment of redemption" | VERIFIED | transcript.txt lines 508-524, timestamp 00:09:49-00:10:05 |
| *Tomorrow, and Tomorrow, and Tomorrow* by Gabrielle Zevin | VERIFIED (title/author correction) | transcript.txt lines 154-158, timestamp 00:02:59-00:03:02. Auto-caption spells the author "Gabrielle Zeban" — this is a transcription error; the real book/author (well-established public fact) is *Tomorrow, and Tomorrow, and Tomorrow* by Gabrielle Zevin, which the on-screen title in the video's own frame corroborates per the source's stated context. Corrected spelling used in genius.md/genius-patterns.md. |
| Book *Peak*, recreational golfer plateau example, "upgrade your mental model" | VERIFIED | transcript.txt lines 1244-1364, timestamp 00:24:38-00:26:48 (Cole names the book "Peak" on-camera but does not state the author; author is commonly known as Anders Ericsson — NOT stated here to avoid attributing an unstated claim to Cole) |
| "a bunch of chess books... nothing but openers" | VERIFIED | transcript.txt lines 382-394, timestamp 00:07:22-00:07:34 |
| "opener number one... opener number two... opener number three" / running doc of combinations | VERIFIED | transcript.txt lines 1646-1670, timestamp 00:31:57-00:32:24 |
| "explanation and action are the two pieces that get used the most... narration [is] the most advanced piece" | VERIFIED | transcript.txt lines 1156-1174, timestamp 00:22:54-00:23:15 |
| Pulitzer/Nobel-tier literature distinguished by narration density | VERIFIED | transcript.txt lines 1180-1216, timestamp 00:23:25-00:24:08 |
| Action genre spectrum, Mission: Impossible / Academy Award film example | VERIFIED | transcript.txt lines 862-946, timestamp 00:17:04-00:18:33 |
| Bishop-10-moves-later chess/explanation-timing analogy | VERIFIED | transcript.txt lines 576-598, timestamp 00:11:06-00:11:30 |
| "start to realize why certain pieces of writing elicit the feelings" | VERIFIED | transcript.txt lines 254-262, timestamp 00:04:53-00:05:04 |

## Unresolved / Not Used

- No claims in this repair required an UNCONFIRMED label — every quote and entity added to genius.md and genius-patterns.md traces to a verbatim line in the transcript above. Two auto-caption misspellings ("Gole" -> Gogol, "Zeban" -> Zevin) were corrected using well-established public facts about real, named authors, not invented.
- Video description metadata (Ship 30 for 30, Premium Ghostwriting Academy, billion+ views, 10+ books, 15 years writing online) was read in `metadata.json` but **not used** in genius.md/genius-patterns.md pattern content — held back because these are channel-bio facts, not craft claims from inside the EDAN teaching itself, and using them would have been padding rather than grounding.

## Existing Ledger Entries (unchanged, still passing)

- `source-map.md` — video source identification, evidence-note summary, build boundary vs. sibling Cole skills.
- `source-study-deconstruction.md` (workflow prompt) — reverse-engineering methodology, not modified this pass.
