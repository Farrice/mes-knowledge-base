# Provenance — andrew-lane-design-systems repair (Wave 3 Lane 4 Batch 1)

Anchor → source file + location, for every quote/claim added or newly labeled by this
repair. Full claim table lives in `references/source-ledger.md`; this file is the
anchor-to-location index the adversarial verifier should open first.

| Anchor (in repaired genius.md) | Source file : line | Verbatim? |
|---|---|---|
| "Do NOT discuss fonts, colors, or logos" | `skills/andrew-lane-design-systems/workflows/01-build-vibe-foundation.md:23` | Yes — exact string match, confirmed via `grep -n` this session |
| "it just doesn't come out right and I want to have more control" | `skills/andrew-lane-design-systems/genius.md:51` (pre-existing line, unedited) | Yes — exact string match |
| "Now go in a completely different direction — show me the opposite style of brand for this." | `skills/andrew-lane-design-systems/genius.md:22` AND `skills/andrew-lane-design-systems/references/prompts-v2/brand-vibe-foundation.md:53` | Yes — exact match at both locations |
| "Assume they cannot see this or any other visual — the description must be clear and easy to follow with no visual inspiration available." | `skills/andrew-lane-design-systems/references/prompts-v2/brand-vibe-foundation.md:60` | Yes — exact string match |
| "branding cannot fix an undecided offer" | `skills/andrew-lane-design-systems/workflows/03-split-brand-decisions.md:25` | Yes — exact string match |
| "No fabricated hex codes, font names, or imagery claims not grounded in [EXISTING BRAND MATERIAL] or the generated mood board" | `skills/andrew-lane-design-systems/references/prompts-v2/brand-vibe-foundation.md:79` | Yes — exact string match |
| SKILL.md frontmatter source claim ("claude.ai export 2026-07-01") used as the date anchor throughout | `skills/andrew-lane-design-systems/SKILL.md:7` | Yes — frontmatter field, pre-existing |
| `forged: born-v2` / `refactored: 2026-07-13` date anchor for the three v2 prompts | `skills/andrew-lane-design-systems/references/prompts-v2/brand-vibe-foundation.md:6-7` (and matching frontmatter in `brand-layer-library.md`, `business-branding-decision-split.md`) | Yes — frontmatter field, pre-existing |

## Absence anchors (what was checked to confirm no deeper source exists)

| Check | Command run | Result |
|---|---|---|
| Expert-specific extraction directory | `find extractions -iname "*lane*"` | 0 results |
| Archived claude.ai export tarball | `tar -tzf _archive/claude-export-2026-07-01.tar.gz \| wc -l` = 3,864; then grep for `lane\|mood.?board\|dude.?woof` | 0 matches |
| Harvest manifest | `_active/claude-export/harvest/lanes-build-input.json`, 18,471 bytes, parsed fully as JSON | No entry for andrew-lane |
| Raw conversation directory | `.tmp/claude-export/normalized/conversations/` | Does not exist |

All six skill files' sizes were recorded with `wc -c` (not `wc -l`) before any edit, per
the envelope's rule on verifying absence honestly — see `references/source-ledger.md`
for the full table.
