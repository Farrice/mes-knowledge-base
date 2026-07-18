# Attention Hijack Hooks — Source Ledger

Ground truth for this skill is a single YouTube extraction package:
`extractions/video-context/Zc4E_K48v48/`. No `extractions/` folder matches
"diandra," "escobar," or "hijack/hook" by name beyond this package — confirmed
via `ls extractions/ | grep -i -E "attention|hijack|hook"` (only
`extractions/luke-iha-hooks` returned, a different expert, not used here) and
a direct listing of `extractions/video-context/`. This is the only source.

## Source Files Consulted (with real file sizes — `wc -c`, read directly, not assumed)

| File | Size (bytes) | Role |
|---|---:|---|
| `transcript.txt` | 71,391 | Primary evidence — 1058 timestamped spoken rows, read in full |
| `transcript.vtt` / `Zc4E_K48v48.en.vtt` / `.en-orig.vtt` | 174,631 each | Same spoken content, VTT-formatted; not separately consulted beyond transcript.txt |
| `video-context-ledger.md` | 127,928 | Row-by-row evidence table (timestamp/type/evidence/source/confidence), spot-checked against transcript.txt |
| `video-context-ledger.json` | 258,569 | Machine-readable mirror of the ledger; not separately consulted |
| `metadata.json` | 3,993 | Title, uploader, publish date, duration, full YouTube description |
| `analysis.md` | 2,226 | Auto-generated executive summary; used for corroboration only |
| `source-to-skill-brief.md` | 3,074 | The extraction team's own build rationale for this skill |
| `uncertainty-report.md` | 444 | Confirms 1058 `observed_spoken` rows, 0 `observed_visual`, 0 `observed_onscreen_text` |
| `frame-notes.md` | 119 | Confirms "No frames were extracted" (transcript-only mode) |
| `ocr-notes.md` | 111 | Confirms "No on-screen text was extracted" (transcript-only mode) |

None of these files are 0-byte or missing — the "no visual/OCR evidence"
claim below is a verified absence (files exist, were opened, and explicitly
state zero rows captured), not an unread guess.

## Claim-by-Claim Labels

| Claim | Label | Basis |
|---|---|---|
| Video is "I Studied 131 Viral LinkedIn Hooks, These 5 Will Make You Go Viral" by Diandra Escobar, published 2026-05-28 | VERIFIED | `metadata.json` title/uploader/upload_date fields |
| "131 hooks from 21 creators" studied, explicitly excluding hooks that worked "in 2022," "in 2023," or "in 2024" | VERIFIED | transcript.txt 00:00:10–00:00:22, 00:02:07–00:02:16 (verbatim) |
| LinkedIn's algorithm reads "first 40 to 50 words" before distribution decision | VERIFIED | transcript.txt 00:00:36–00:00:44 (verbatim) |
| The LinkedIn ranking model is named "360 Brew" and tracks whether readers stop and read | VERIFIED | transcript.txt 00:01:41–00:01:49 (verbatim) |
| LinkedIn renders by pixel width (~110 width units/line on mobile), not character count | VERIFIED | transcript.txt 00:03:38–00:04:06 (verbatim) |
| Five hook formats: Dense, Punchy + Context, Single-Line Bomb, Stacked, Hybrid | VERIFIED | transcript.txt 00:02:53–00:10:00, matches `metadata.json` description list |
| Punchy + Context is "the format we see most and the one with the highest hit rate" | VERIFIED | transcript.txt 00:04:36–00:04:41 (verbatim) |
| Single-Line Bomb is "the riskiest format" / "highest variance hook" | VERIFIED | transcript.txt 00:06:31, 00:08:01 (verbatim) |
| Stacked hooks fail when lines aren't "part of the same series" / rhythm isn't predictable | VERIFIED | transcript.txt 00:09:07–00:09:17 (verbatim) |
| "The format is just packaging. The gap is the engine." (core thesis) | VERIFIED | transcript.txt 00:09:25–00:09:50 (verbatim) |
| Escobar's Claude skill "gets you a stronger starting point than a blank page" for "80% of posts" and "won't replace your judgment" | VERIFIED | transcript.txt 00:10:37–00:10:51 (verbatim) |
| Any on-screen text of the actual example hooks shown in the video (exact hook copy as it appeared visually) | UNCONFIRMED | `frame-notes.md` and `ocr-notes.md` both confirm zero frames/OCR captured in this transcript-only extraction — the spoken narration around each example ("here's an example," "five words," "before, after") is VERIFIED, but the literal on-screen hook text is not in this package and is not claimed as a direct quote anywhere in this skill |
| Diandra Escobar's LinkedIn newsjacking skill (mentioned in passing, "another video") | UNCONFIRMED | Referenced only as "my LinkedIn newsjacking one... in another video" (transcript.txt 00:11:13–00:11:18); no separate extraction package exists for that video in this repo, so nothing about it is asserted beyond this passing mention |

## Anti-Patterns / Genius Patterns / Hidden Knowledge Files

`references/genius-patterns.md` and `references/hidden-knowledge.md` (both
pre-existing) restate the same five-pattern structure as `genius.md` in
compressed form. They are LIKELY-labeled as a set: consistent with the
verbatim transcript evidence above but themselves uncited paraphrases, not
independently sourced. No claim in either file contradicts the transcript.
