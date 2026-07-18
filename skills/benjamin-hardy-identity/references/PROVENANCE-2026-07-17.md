# Provenance — skills/benjamin-hardy-identity repair (Wave 3 Lane 4 Batch 2)

## Ground-truth search performed (2026-07-17)

- `ls extractions/` (full listing) + `find extractions -iname "*hardy*"` → no Hardy source
  directory exists in `extractions/`.
- `_archive/claude-export-2026-07-01.tar.gz` — 332,779,255 bytes (`ls -la`). Full listing
  via `tar -tzf` → 3,864 entries (`wc -l` on the listing file). Grep `-i hardy` across the
  full listing → 0 matches.
- `agents/benjamin-hardy/memory/context.md` — read in full (409 bytes); session notes
  only, no transcript.
- `agents/benjamin-hardy/AGENT.md`, `skills/benjamin-hardy-identity/{SKILL.md,genius.md}`,
  all 3 `workflows/*.md`, all 3 `references/prompts-v2/*.md` — read in full; these are the
  only ground truth this repair could draw on.
- WebSearch (2026-07-17) — one query to verify Hardy's published-author claims
  independently of the skill files (see `references/source-ledger.md` VERIFIED rows).

**Conclusion**: no primary interview/podcast/article transcript for Benjamin Hardy exists
anywhere in this repository. Every quote in this repair traces to text already shipped in
the skill's own files, never to an invented external source.

## Anchor table (genius.md additions → source)

| Anchor location | Content | Source |
|---|---|---|
| Anti-Patterns bullet 1 | "You really just want to use it as a tool for filtering..." | `skills/benjamin-hardy-identity/genius.md`, Insight: The Goal Is a Filter, Not a Verdict (pre-existing, unmodified) |
| Anti-Patterns bullet 2 | "the most common mistake of a smart entrepreneur is to optimize something that should not exist" | `skills/benjamin-hardy-identity/genius.md`, Pattern: Question Requirements First |
| Anti-Patterns bullet 3 | "the decisions the young entrepreneur is making are the exact opposite decisions..." | `skills/benjamin-hardy-identity/genius.md`, Pattern: 10x Is Easier Than 2x |
| Anti-Patterns bullet 4 | "you're never going to hit that goal, because you've put it 10 years away..." | `skills/benjamin-hardy-identity/genius.md`, Pattern: If a Timeline Is Long, It's Wrong |
| Anti-Patterns bullet 5 | "the tangible step is never addition — it's always subtraction" | `skills/benjamin-hardy-identity/genius.md`, Insight: The First Tangible Step of Change Is Always Subtraction |
| Anti-Patterns bullet 6 | Daniel Gilbert — "human beings are works in progress that think they're finished" | `skills/benjamin-hardy-identity/genius.md`, Pattern: Works in Progress, Not Finished Products |
| Anti-Patterns bullet 7 | "they remain the bottleneck in what they're building... king or queen of their project" | `skills/benjamin-hardy-identity/genius.md`, Pattern: Stop Being the Bottleneck (Who Not How) |
| How-to-Use quote | "Keeping this while claiming that goal is lying to myself." | `skills/benjamin-hardy-identity/workflows/02-raise-the-floor.md:34` (pre-existing, unmodified) |
| How-to-Use quote | Gilbert works-in-progress quote | Same as Anti-Patterns bullet 6 above |
| source-ledger.md VERIFIED rows | Author bio + 4 book titles/co-authorship | WebSearch 2026-07-17 (URLs: blinkist.com author page, blinkist.com summaries ×2, amazon.com listing) — external, independent of skill files |
| source-ledger.md absence verification | extractions/ + claude-export archive have no Hardy source | Direct `ls`/`find`/`tar -tzf`/`wc` this session, recorded with byte/entry counts above |

No pre-existing content in `genius.md`, `SKILL.md`, or any workflow/prompts-v2 file was
altered, deleted, or reworded — all 7 checked/failing-item repairs are additive.
