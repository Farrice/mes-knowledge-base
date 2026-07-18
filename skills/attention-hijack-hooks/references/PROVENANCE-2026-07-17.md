# PROVENANCE — attention-hijack-hooks repair (Wave 3 Lane 4 Batch 2)

All anchors trace to the single existing source package
`extractions/video-context/Zc4E_K48v48/` (Diandra Escobar, "I Studied 131
Viral LinkedIn Hooks, These 5 Will Make You Go Viral," published
2026-05-28). No other extraction exists for this skill's expert — verified
via `ls extractions/ | grep -i -E "attention|hijack|hook"` (only
`extractions/luke-iha-hooks` returned, a different expert) and a direct
listing of `extractions/video-context/`.

| Anchor used in genius.md | Source file | Location |
|---|---|---|
| "3 years... clients... founders paying us thousands a month" | `transcript.txt` | 00:00:00–00:00:10 |
| "131 hooks from 21 creators... not in 2022" | `transcript.txt` | 00:00:10–00:00:19 |
| "first 40 to 50 words before it decides whether to push your post to anyone" | `transcript.txt` | 00:00:36–00:00:44 |
| "soft, vague, throat-clearing sentences" | `transcript.txt` | 00:01:03–00:01:08 |
| "Get the click, not summarize, not explain, not set up the post" | `transcript.txt` | 00:01:26–00:01:32 |
| "new LinkedIn model called 360 Brew... tracks whether people stop and read" | `transcript.txt` | 00:01:41–00:01:49 |
| "when your hook fails, two things die at the same time" | `transcript.txt` | 00:01:52–00:01:59 |
| "hooks that worked in 2023... 2024... not what's working in 2026" | `transcript.txt` | 00:02:07–00:02:16 |
| "12 months ago" / "2 years ago... actively hurting you" | `transcript.txt` | 00:02:23–00:02:30 |
| "across SaaS, agency, e-com, B2B, content, AI" | `transcript.txt` | 00:02:36–00:02:44 |
| "LinkedIn doesn't render by characters, it renders by pixels" | `transcript.txt` | 00:03:38–00:03:42 |
| "letter W takes up four times the visual space of the letter I" | `transcript.txt` | 00:03:42–00:03:52 |
| "pixel width budget, around 110 width units per line on mobile" | `transcript.txt` | 00:03:59–00:04:06 |
| "most hook advice is wrong... real answer is pixel width" | `transcript.txt` | 00:04:12–00:04:17 |
| "dense hook fits a roughly three mobile lines" | `transcript.txt` | 00:04:17–00:04:22 |
| "format we see most and the one with the highest hit rate" (Punchy + Context) | `transcript.txt` | 00:04:36–00:04:41 |
| "the punchy line tries to do everything... should provoke" | `transcript.txt` | 00:05:24–00:05:34 |
| "riskiest format... have to warn you about" (Single-Line Bomb) | `transcript.txt` | 00:06:31–00:06:36 |
| "we don't recommend this format unless you know in your gut" | `transcript.txt` | 00:06:59–00:07:03 |
| "highest variance hook" | `transcript.txt` | 00:07:56–00:08:03 |
| "each line has to be a part of a series... structure fails" (Stacked) | `transcript.txt` | 00:09:11–00:09:17 |
| "where stacked hooks die is when the lines are kind of random" | `transcript.txt` | 00:09:07–00:09:11 |
| "the format is just packaging. The gap is the engine" (core thesis) | `transcript.txt` | 00:09:25–00:09:50 |
| "master the four first, then start breaking the rules" (Hybrid) | `transcript.txt` | 00:10:11–00:10:18 |
| "won't replace your judgment... 80% of posts... stronger starting point" | `transcript.txt` | 00:10:37–00:10:51 |
| Title, uploader, publish date | `metadata.json` | title/uploader/upload_date fields |
| Zero frame/OCR evidence (used to label on-screen hook copy UNCONFIRMED) | `frame-notes.md`, `ocr-notes.md`, `uncertainty-report.md` | full files (119 / 111 / 444 bytes) |

All timestamps were located by direct `sed`/`grep` reads of
`transcript.txt` in this session, then reconstructed into full sentences
from the source's rolling-caption duplication (each caption line repeats
the tail of the prior line — reconstruction removes only that mechanical
duplication, no words added or changed). Every quote above was checked
against the raw transcript text before being placed in genius.md.

## workflows/05-content-bridge.md

The added "## Output Schema" heading and its Quality Gate bullets are not
sourced to the video — they are structural (matching the house style of
`workflows/01-signal-anchor-scan.md`, which already carries `## Output
Schema`) and reference the pre-existing "Handoff Shape" content and
genius.md Pattern 6, both already in the skill. No new factual claims were
introduced.
