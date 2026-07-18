# PROVENANCE — kieran-flanagan-content-engine repair

| Anchor (as written in genius.md) | Source file | Location | Verified how |
|---|---|---|---|
| "the content enrichment tools need a first draft to enrich..." | `extractions/kieran-flanagan/transcript.txt` | mid-transcript, post-enricher demo segment | `grep -o` exact-string match against raw file |
| "obviously I would never ship this" | `extractions/kieran-flanagan/transcript.txt` | near end, marketer-job-split post review | `grep -o` exact-string match |
| "this is a draft an idea and then you make much better" | `extractions/kieran-flanagan/transcript.txt` | mid-transcript, post-enricher demo segment | `grep -o` exact-string match |
| "I was never a big fan of the kind of vibe marketing..." | `extractions/kieran-flanagan/transcript.txt` | early transcript, "this is not software" segment | `grep -o` exact-string match (full sentence) |
| "Traditional personas are built from demographics and surveys — they're fiction" | `extractions/kieran-flanagan/extraction-report.md` | Hidden Knowledge, bullet 1 | `grep -o` exact-string match |
| "Never let LinkedIn style infect newsletter style..." | `extractions/kieran-flanagan/extraction-report.md` | Hidden Knowledge, bullet 5 (Platform Isolation Rule) | `grep -n` exact-string match |
| "the analytical models are 'too good' at following instructions..." | `extractions/kieran-flanagan/extraction-report.md` | Hidden Knowledge, bullet 4 (Model Routing Strategy) | `grep -n` exact-string match |
| "genuinely good" / "no single skill carries the full burden" (Model Calibration section — the latter phrase is NOT quoted as Kieran's verbatim speech, only paraphrased as the report's framing) | `extractions/kieran-flanagan/extraction-report.md` | Executive Summary, "What Makes Them Different" | `grep -n` exact-string match for "carries the full burden"; only "genuinely good" is inside quotation marks in genius.md, matching the report's own quoted fragment |

## Self-correction logged
First draft of the Anti-Patterns section attributed the persona/platform-isolation/model-routing lines directly to "Kieran" as spoken quotes. On review, these three do not appear in `transcript.txt` verbatim — they are `extraction-report.md`'s own Hidden Knowledge analysis/synthesis prose. Re-labeled in both `genius.md` (phrasing: "per the extraction's ... framing/synthesis") and `references/source-ledger.md` (explicit VERIFIED-as-report-prose-not-transcript-speech label) to avoid overstating provenance. No item was left with an invented-verbatim attribution.

## Absence check
- `ls extractions/ | grep -i flanagan` run 2026-07-17 → `kieran-flanagan`, `kieran-flanagan-second-brain`. Both opened; second-brain folder confirmed out of scope (different video, personal-knowledge-base domain), not silently skipped.
- No prior `references/source-ledger.md` (or any ledger/source file) existed for this skill before this repair — confirmed via `ls skills/kieran-flanagan-content-engine/references/`.
