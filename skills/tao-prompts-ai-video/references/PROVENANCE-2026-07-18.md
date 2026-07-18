# Provenance — tao-prompts-ai-video repair

Anchor → source file + location, for every quote/anchor added or verified during this repair pass. All source files confirmed present and non-empty via `wc -c` (byte count, not `wc -l`).

| Source file | `wc -c` |
|---|---|
| `extractions/tao-prompts/transcript.txt` | 15,185 bytes |
| `extractions/tao-prompts/extraction-report.md` | 7,490 bytes |
| `skills/tao-prompts-ai-video/references/hidden-knowledge.md` | (pre-existing skill file, not under `extractions/`) |

## Anchors used in genius.md

| Anchor text (as it appears in genius.md) | Location in genius.md | Verbatim source |
|---|---|---|
| "the actual quality of the video itself will roughly be the same regardless of how complicated your prompt is" | Model Calibration section + Anti-Patterns bullet 1 | `extractions/tao-prompts/transcript.txt` (Level 1 discussion, "Just because these prompts are super simple..." paragraph) |
| "it's not a magic pill that's going to suddenly create amazing AI videos" | Anti-Patterns bullet 2 | `extractions/tao-prompts/transcript.txt` (Level 2, JSON prompt discussion) |
| "warped faces or melted environments" | Hidden Knowledge 1 (pre-existing) + Anti-Patterns bullet 3 | `skills/tao-prompts-ai-video/references/hidden-knowledge.md` line 5 — NOT found in `extractions/tao-prompts/`; correctly re-attributed after an initial mis-citation to `extraction-report.md` was caught and fixed during this pass |
| "Most AI video companies aren't going to tell you what it's bad at" | Pattern 3 Source Note + Anti-Patterns bullet 4 | `extractions/tao-prompts/transcript.txt` (Level 4, Leverage & Scaling section) |
| "varied, disconnected clips that don't look like they exist in the same universe" | Hidden Knowledge 2 + Anti-Patterns bullet 5 | `skills/tao-prompts-ai-video/references/hidden-knowledge.md` line 10 |
| "if you add too much action or movement into the prompts, the AI is not going to give you good results" | Anti-Patterns bullet 6 | `extractions/tao-prompts/transcript.txt` (Level 5, lip-sync prompting section) |
| "a single prompt that defines multiple sequential shots, each with its own camera angle, action, and timing" | Pattern 2 Source Note | `extractions/tao-prompts/transcript.txt` (Level 2, multi-shot prompt definition) |

## Self-caught error (recorded, not hidden)

Anti-Patterns bullet 3 was first drafted citing `extractions/tao-prompts/transcript.txt` for "warped faces or melted environments" and separately a since-removed line citing `extractions/tao-prompts/hidden-knowledge.md` (a path that does not exist — the file lives at `skills/tao-prompts-ai-video/references/hidden-knowledge.md`, outside `extractions/`). Both were caught by a `grep`/`in`-string verification pass before finalizing and corrected to the real file paths. No invented anchor shipped in the final version — see `references/source-ledger.md` for the full claim-by-claim table, including the UNCONFIRMED items (Hall of Fame Exemplars, Anti-Exemplar, and Pattern 5/Temporal Dramaturgy, none of which appear in the source material and are labeled as such rather than silently treated as sourced).
