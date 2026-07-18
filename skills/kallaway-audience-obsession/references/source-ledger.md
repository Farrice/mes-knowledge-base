# Source Ledger — kallaway-audience-obsession

Compiled by Wave 3 Lane 4 Batch 8 repair worker, 2026-07-18. Every source consulted
while repairing `anti_patterns_sourced`, `recognition_test`, and `source_ledger` for
this skill, with VERIFIED / LIKELY / UNCONFIRMED labels applied claim-by-claim.

## Files Consulted (with sizes, `wc -c`)

| File | Size (bytes) | What it is | Relevance to this skill |
|---|---|---|---|
| `extractions/kallaway/transcript.txt` | 34,072 | "Illusion of Novelty" video transcript | Different Kallaway framework (relevant/novel/interesting, not Bankshot/Levels). No overlap with this skill's claimed quotes. |
| `extractions/kallaway/extraction-report.md` | 6,971 | Mastery Extraction — "Desire-Based Hook System" (Constraint-Free Bridge, Latent Desire Mirroring, Subject-Switching Matrix) | Different framework entirely. No "bankshot," "obsession level," or "signal-to-noise" language. |
| `extractions/kallaway/internet-money-machine-transcript.txt` | 24,657 | "Internet Money Machine" video transcript | 4-step revenue playbook (avatar/offer → competitor research → production → funnels). No overlap. |
| `extractions/kallaway/internet-money-machine-extraction.md` | 12,864 | Extraction of the above | Same scope, no overlap. |
| `extractions/kallaway/word-mastery-extraction.md` | 16,292 | Word Mastery patterns (sentence length, specificity, proof) | Thematically adjacent (specificity/proof are related concepts) but zero verbatim overlap with this skill's genius.md quotes. |
| `extractions/kallaway-content-system/transcript.txt` | 43,221 | "I Hated Social Media... Until I Learned THIS System" transcript | Contains one genuine mention of "dopamine ladders" (line 836) — corroborates that term only, nothing else in this skill. |
| `extractions/kallaway-content-system/extraction-report.md` | 4,963 | Extraction report for the above | Same scope, no overlap with this skill's claims. |
| `extractions/kallaway-content-system/integrity-patch.md` | 5,108 | Integrity patch note for the above extraction | No overlap. |
| `extractions/kallaway-content-system/B9l9TRhu5Vw.en-orig.vtt` | 398,725 | Raw YouTube captions for the content-system video | Same video as transcript.txt above; not the "Power of Suggestion" source. |
| `.agents/skills/source-command-kallaway-audience/SKILL.md` | 1,336 | Routing shim that points at this skill | Not a source — a command-alias wrapper, confirmed by read. |
| `skills/kallaway-audience-obsession/references/obsession-framework.md` | (in-skill, pre-existing) | Contains 8 "Source Quotes (Verbatim)" attributed to "The Power of Suggestion" | No transcript, timestamp, URL, or filename backs these quotes anywhere in the repo. |

## Searches Run (2026-07-18)

- `grep -ril "bankshot" extractions/` → 0 hits
- `grep -ril "power of suggestion" extractions/` → 0 hits
- `grep -in "suggestion\|obsess" extractions/kallaway/transcript.txt` → 0 hits
- `find . -iname "*kallaway*"` (repo-wide, excluding skills/) → no additional transcript or raw-source file for this skill's specific claims
- `find . -iname "*suggestion*"` (repo-wide) → no raw source file

**Conclusion**: The skill's stated source — "The Power of Suggestion" (YouTube, 2026), 5,075
words — is not present anywhere in this workspace as a transcript, caption file, or
extraction-report. This does not mean the framework is false (Kallaway may well teach
this material); it means it is **currently unauditable** from files available to this
repair worker.

## Claim-by-Claim Labels

| Claim | Label | Basis |
|---|---|---|
| Genius.md source line: "The Power of Suggestion (YouTube, 2026) — 5,075 words" | UNCONFIRMED | No matching file, title, or word count found anywhere in `extractions/` |
| Genius Patterns 1–10 (Bankshot Principle, Signal-to-Noise, Invisible Suggestion, Belief Change, Contrasting Frame, Relatable Character, Small Cost/Large Reward, Proof-Driven Action, Atomic Tactical Steps, Inception Model) | UNCONFIRMED | Not traceable to any file under `extractions/kallaway*` |
| Hall of Fame Exemplars 1–3 (Dopamine Ladders video, 0-to-100K video, YouTube Scripting video) + Anti-Exemplar | UNCONFIRMED | No corroborating transcript found for the specific claims made (viewer comment quotes, video content) |
| `references/obsession-framework.md` — 8 "Source Quotes (Verbatim)" | UNCONFIRMED | Quotes exist in-skill but carry no file/timestamp/URL anchor anywhere in the repo; cannot be cross-checked |
| "Dopamine Ladders" as a genuine Kallaway framework name | LIKELY | Verbatim match at `extractions/kallaway-content-system/transcript.txt:836` — "dopamine ladders or all the stuff I do in the videos" — confirms the *term* is real; does not confirm the Level-1-obsession content built around it in this skill |
| General Kallaway voice (proof-first, avoids hard-sell phrasing, leads with results/numbers) | LIKELY | Consistent pattern across `extractions/kallaway/transcript.txt` and `internet-money-machine-transcript.txt`, both of which lead with concrete numbers ("million followers," "billions of views," "seven figures") rather than direct claims of superiority |
| Anti-Patterns 1–8 in genius.md (this repair) | UNCONFIRMED | No verbatim anchor exists for any of the 8; each now carries an explicit UNCONFIRMED tag pointing here instead of an invented citation |

## Recommendation

If the "Power of Suggestion" source video is re-sourced (title, URL, or transcript
recovered), re-run this extraction against the real transcript and replace the
UNCONFIRMED labels above with VERIFIED + line anchors. Until then, treat this skill's
core framework as internally coherent but externally unverified.
