# PROVENANCE — pj-accetturo-ai-video repair

Anchor → source file+location for every added claim/quote in `genius.md`. Full detail and confidence labels: `references/source-ledger.md`.

| Anchor text (as it appears in genius.md) | Source file | Location |
|---|---|---|
| "233M views in 3 days" / David Beckham IM8 credit | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/6bf72208-81f6-47e9-a5a1-aa7a34b2a2d3.md` | line 77 (Content Assessment) — UNCONFIRMED, self-reported, no independent corroboration found |
| "the viral Kalshi NBA Finals ad (seen during primetime)" | same archive file as above | line 77 — UNCONFIRMED, same caveat |
| "23 Virtuoso Genius Patterns detected" | same archive file | line 80 |
| 5-role model (Writer → Director → Cinematographer → Animator → Editor) | same archive file | lines 204, 213, 241, 440, 560 — LIKELY (secondhand extraction summary, raw transcript text not recoverable) |
| 2x2 Grid Consistency technique | same archive file | line 244 — LIKELY |
| Motion Control / "Avatar technique" | same archive file | line 245 — LIKELY |
| "cutting corners" / "scrappy innovation" | `skills/pj-accetturo-ai-video/workflows/strategic-creative-direction.md` | line 31 — verified verbatim present via `grep -c` before use |
| "uncanny valley risk" | same workflow file | line 45 |
| "without looking at the script" | same workflow file | line 66 |
| "Audio Anchor" | same workflow file | line 46 |
| "No invented statistic, dollar figure, or percentage appears anywhere the underlying number wasn't supplied in the input" | `skills/pj-accetturo-ai-video/references/prompts-v2/prompt_05_brand_strategy.md` | line 152 |
| Refactor date 2026-07-11 | same prompt file | frontmatter, line 6 (`refactored: 2026-07-11`) |
| "Top 5 AI Video Tools You NEED to Try!" / "Generic AI Video Tool Listicle" / "could be produced by any AI without expert insight" | `skills/pj-accetturo-ai-video/genius.md` (pre-existing, this file) | lines 23-25, Hall of Fame Exemplars → Anti-Exemplar |
| "clunky, requiring significant manual intervention where AI could assist" | `skills/pj-accetturo-ai-video/genius.md` (pre-existing, this file) | line 43, Expert-Specific Quality Rubric table |
| Archive file size 332,779,255 bytes | `_archive/claude-export-2026-07-01.tar.gz` | confirmed via `wc -c` (not `wc -l` — file is a binary tarball, line-count would misreport) |
| Normalized conversation file size 119,243 bytes | `claude-export/normalized/conversations/6bf72208-81f6-47e9-a5a1-aa7a34b2a2d3.md` (extracted from the tarball) | confirmed via `wc -c` after extraction |

## Search discipline log

1. `ls extractions/ | grep -i accetturo` → no matches.
2. `grep -rli accetturo extractions/ knowledge/` → no matches (only `extractions/tao-prompts/extraction-report.md`, a different expert who references PJ Accetturo tangentially — not used as a primary source).
3. Per SOURCE-SEARCH DISCIPLINE, before claiming absence: ran a Python `tarfile` per-member **content** scan (not filename scan) of `_archive/claude-export-2026-07-01.tar.gz` across all 7,720 members for the byte string `accetturo` (case-folded). Found 2 hits, both logged above. The normalized `.md` hit (119,243 bytes) was extracted and read in full — it is the MES 3.0 extraction conversation that originally built this skill (dated 2026-01-23), not the raw source transcript itself (the transcript's own text blocks are collapsed to "This block is not supported on your current device yet." in the export — only the extraction assistant's narration/summary survived). This is why several claims are labeled LIKELY/UNCONFIRMED rather than VERIFIED: the chain of custody stops at a secondhand summary, not PJ's own words.
