# PROVENANCE — alex-copper-creative-strategy repair (Wave 3 Lane 4 Batch 1)

Anchor → source file + location. Full claim-by-claim confidence labels live in `references/source-ledger.md`.

| Anchor (as written in repaired genius.md) | Source file | Location | Confidence |
|---|---|---|---|
| "the algorithm isn't broken, your creative sucks" | `references/agent_system_prompt.md` | line 12 | LIKELY (verbatim in-repo, unverified vs. primary transcript) |
| "meta ads is a creative game, not a media buying game" | `references/agent_system_prompt.md` | line 9 | LIKELY |
| "Do X. Stop doing Y." | `references/agent_system_prompt.md` | line 15 | LIKELY |
| "Become an absolute hoarder of top performing ads." | `genius.md` | line 202 (§16-27, dated 2026-07-01) | LIKELY |
| "The only people making good ads with AI are people who make good ads without AI" | `genius.md` | line 240 (Hidden Knowledge cont'd, item 9) | LIKELY |
| "I don't think creative shops as they currently work will be around in 2-3 years." | `genius.md` | line 245 (Hidden Knowledge cont'd, item 10) | LIKELY |
| "Problem: Full AI ads lack trust. Solution: AI for hooks only, humans for testimony." | `references/_legacy-prompts/ai-visual-generation-protocol.md` | Pitfall 3, "AI as Primary Content" (~line 273-275) | UNCONFIRMED as literal Cooper words; VERIFIED as existing skill text |
| "Problem: AI attempting photorealism often hits uncanny valley. Solution: Lean into stylized/surreal" | `references/_legacy-prompts/ai-visual-generation-protocol.md` | Pitfall 1, "Trying for 'Too Real'" (~line 265-267) | UNCONFIRMED as literal Cooper words; VERIFIED as existing skill text |
| "Feature-First, Who Cares?" Anti-Exemplar | `genius.md` | § Hall of Fame Exemplars, Anti-Exemplar (~line 142-144) | VERIFIED as pre-existing skill content; UNCONFIRMED as a real ad |
| "Do NOT use collision as a gimmick..." | `workflows/02-performance-creative-production.md` | line 48 | VERIFIED (skill-authored constraint, not attributed to Cooper) |

## Absence verification (for the anti_patterns_sourced / source_ledger gaps)

Commands run and results, 2026-07-17:
- `ls extractions/ | grep -iE 'cooper|copper'` → 0 results
- `find . -iname "*cooper*"` (excluding `skills/alex-copper-creative-strategy/`) → 0 results
- `find extractions -iname "*adcrate*" -o -iname "*ad-crate*" -o -iname "*ad_crate*"` → 0 results
- `wc -c` recorded for every skill file read (table in `references/source-ledger.md`) — all non-zero, real content, no "0-byte/unrecoverable" claims made.

Conclusion: no primary transcript or `extractions/` folder exists for Alex Cooper anywhere in this repo. This is a verified absence, not an unread gap.
