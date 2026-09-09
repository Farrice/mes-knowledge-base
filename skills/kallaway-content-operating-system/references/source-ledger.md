# Kallaway Content Operating System — Source Ledger

Claim-by-claim provenance for the anti-patterns, verbatim exemplars, and operating-pattern grounding added in `genius.md` during the Wave 3 Lane 4 Batch 8 repair pass. `references/source-evidence-map.md` already existed and passes the `source_ledger` heartbeat check on its own; this file is the additive, claim-level companion the repair envelope requires.

## VERIFIED (quote or figure confirmed present verbatim in the cited file)

| Claim | Source | Verification |
|---|---|---|
| "the first step in this playbook is actually not to make content. The first step is avatar selection and offer framing" | `extractions/kallaway/internet-money-machine-transcript.txt` | Read in full (24,657 bytes); phrase present verbatim. |
| "Every video has 11 core attributes. I call these Lego bricks." | `extractions/kallaway/internet-money-machine-transcript.txt` | Read in full; phrase present verbatim, including the spoken/visual/text hook breakdown that follows it. |
| "$1,000 deals, $5,000 deals, or even $20,000 deals" / "batches of 10 videos" / "average views are 500" / "at least 5,000 views" / "five to 10 batches" | `extractions/kallaway/internet-money-machine-transcript.txt` | Read in full; all figures present verbatim in the monetization-math and batch-system passages. |
| "content, audience, product fit" / "If you make content that attracts a viewer that doesn't need to buy your product, then you could have billions of views with literally zero dollars in sales" | `extractions/kallaway/internet-money-machine-transcript.txt` | Read in full; phrase present verbatim. |
| "the reason we want to avoid really big, large, and mega accounts... some portion of that can be attributed to their fame" / "between 10 and about a million followers" / "the 10 to 250K range" | `extractions/kallaway/internet-money-machine-transcript.txt` | Read in full; phrase present verbatim in the competitor-research section. |
| "The most addictive content is relevant, novel, and interesting." | `extractions/kallaway/transcript.txt` (Illusion of Novelty video) | Read in full (34,072 bytes); phrase present verbatim near the top of the transcript. |
| "you don't have to worry about like scrambling and copying what I'm saying word for word" (line 168) | `extractions/kallaway-content-system/transcript.txt` | Read in full (43,221 bytes, line-numbered); confirmed at line 168. |
| "I don't recommend combining multiple creators here because oftentimes, you know, speaking patterns are like fingerprints" (line 688) | `extractions/kallaway-content-system/transcript.txt` | Confirmed at line 688. |
| "if you're a business owner or you're trying to build an actual revenue engine from content, you should not be editing" (line 802) | `extractions/kallaway-content-system/transcript.txt` | Confirmed at line 802. |
| "My creativity in this workflow comes a little bit later in substance, hook, and scripting and sometimes the edit, but I don't need to reinvent the wheel on the topic front" (line 58) | `extractions/kallaway-content-system/transcript.txt` | Confirmed at line 58. |
| "topic, format, substance, hook, script, and edit" / "nothing else really matters if you pick a losing topic" | `extractions/kallaway-content-system/transcript.txt` | Confirmed near lines 34–47. |
| Video title "I Hated Social Media... Until I Learned THIS System," acquired 2026-05-07 | `extractions/kallaway-content-system/transcript.txt`, header lines 1–5 | Confirmed: `Source: https://www.youtube.com/watch?v=B9l9TRhu5Vw`, `Acquired: 2026-05-07`. |
| "Source: YouTube video, ~25 min (4,935 words)... Genius Patterns: 14 identified across 3 buckets" | `extractions/kallaway/word-mastery-extraction.md` | Confirmed at file header, lines 1–9. |
| "1886 spoken rows, 20 visual rows, 0 OCR rows, 1 unavailable row" for `oRYfJ_yxz6M` | `skills/kallaway-content-operating-system/references/source-evidence-map.md` | Confirmed verbatim in the Source Packages table (this is a claim *about* an evidence package, not a claim that the package itself was re-verified — see UNCONFIRMED row below). |
| OCR unavailable project-wide | `skills/kallaway-content-operating-system/references/hidden-knowledge.md`, item 5 | Confirmed verbatim: "OCR rows are unavailable because the local OCR dependency is not configured." |
| Micro-fame means category authority and authority density rather than follower volume alone | `extractions/video-context/1ilMGCxJBQY/video-context-ledger.json`, rows S01–S02 | Directly grounded in the cleaned caption package; creator outcome claims are separately labeled. |
| Seven positioning lenses: topic, substance depth, stories/scenarios, avatar specificity, delivery style, storytelling format, visual format | `extractions/video-context/1ilMGCxJBQY/video-context-ledger.json`, row S04 | Directly grounded in the timestamped transcript. Farrice's taste verdict changes these from output checklist to backstage search lenses. |
| 3-2-1 means three topic buckets, two posts per bucket per week, and one chaos slot; one broad and two narrow buckets have different jobs | `extractions/video-context/1ilMGCxJBQY/video-context-ledger.json`, rows S08–S09 and V04 | Spoken and visual evidence agree. |
| Four executions over two weeks precede a bucket decision | `extractions/video-context/1ilMGCxJBQY/video-context-ledger.json`, row S12 | Directly grounded in the source recipe. Farrice's verdict makes four reps the minimum evidence floor, not an automatic kill timer. |

## LIKELY (adjacent/secondary source, not a direct line-cited quote)

| Claim | Source | Why LIKELY not VERIFIED |
|---|---|---|
| Pattern 5 (Retention Is Prediction Management: stakes, big question, head fake, rehook, loop density) | `skills/kallaway-content-operating-system/references/genius-patterns.md`, Pattern 5 | Carried forward from the skill's existing compact genius-patterns file. The named source video (`SDHKQbKC7gA`, "Storytelling Is Easier Than You Think") is not present under `extractions/video-context/` — see UNCONFIRMED row. |
| Pattern 6 (Obsession Is Indirect Suggestion) | `extractions/kallaway/word-mastery-extraction.md` (adjacent trust/delivery material) | The named source video (`cuVyTmbOZjk`) is not present under `extractions/video-context/`. Word-mastery extraction covers adjacent delivery/trust craft but not this video's specific suggestion mechanics. |

## UNCONFIRMED (claimed in an existing skill file but not independently verifiable this pass)

| Claim | Where claimed | What was checked |
|---|---|---|
| 9 of the 11 packages listed in `source-evidence-map.md` do not resolve at the stated `extractions/video-context/<id>/` path | `skills/kallaway-content-operating-system/references/source-evidence-map.md`, Source Packages table | Two full packages resolve in this branch: `a7VjpIqq8Xk` and `1ilMGCxJBQY`. `B9l9TRhu5Vw` is recoverable under a different real path. The remaining eight older IDs have no located transcript in this branch. Their quoted evidence counts remain unconfirmed until the packages are restored or the map is corrected. |

## Files Actually Read This Pass (with sizes)

- `extractions/kallaway/extraction-report.md` — 6,971 bytes
- `extractions/kallaway/internet-money-machine-extraction.md` — 12,864 bytes
- `extractions/kallaway/internet-money-machine-transcript.txt` — 24,657 bytes
- `extractions/kallaway/transcript.txt` — 34,072 bytes
- `extractions/kallaway/word-mastery-extraction.md` — 16,292 bytes
- `extractions/kallaway-content-system/extraction-report.md` — 4,963 bytes
- `extractions/kallaway-content-system/integrity-patch.md` — 5,108 bytes
- `extractions/kallaway-content-system/transcript.txt` — 43,221 bytes
- `extractions/kallaway-content-system/B9l9TRhu5Vw.en-orig.vtt` — 398,725 bytes (header sampled; raw VTT, not fully re-transcribed for this pass)
- `extractions/video-context/a7VjpIqq8Xk/metadata.json`, `analysis.md` — sampled (full package present and intact)
