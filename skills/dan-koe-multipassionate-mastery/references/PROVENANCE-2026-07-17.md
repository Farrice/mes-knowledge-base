# Provenance — dan-koe-multipassionate-mastery repair (2026-07-17)

Anchor → source file + location. Full claim-by-claim detail lives in
`references/source-ledger.md`; this table covers the new/changed anchors added
by this repair (Anti-Patterns section + Pattern 1-14 entity fixes + Model
Calibration section).

| Anchor (in modified genius.md) | Source | Location | Status |
|---|---|---|---|
| "we're not just going to have an agent do this all for us... the human aspect of it" | `extractions/dan-koe/transcript.txt` | ~paragraph 1 (context/personal-brand-AI framing) | VERIFIED — read in full, matched verbatim |
| "You're gambling at that point." | `extractions/dan-koe/transcript.txt` | Context (4C framework) paragraph, mid-file | VERIFIED |
| "you're not treating it like an employee that you have to train" | `extractions/dan-koe/transcript.txt` | Clarification (4C) paragraph | VERIFIED |
| "You're waiting for someone like me in this video to give you a step-by-step framework rather than going in tinkering, experimenting..." | `extractions/dan-koe/transcript.txt` | Clarification (4C) paragraph, same block as above | VERIFIED |
| "Stop treating AI as an oracle. Treat it as a capable but untrained new hire." | `extractions/dan-koe/extraction-report-ai-leverage.md` | Genius Pattern 6, "AI as Employee" Mental Model | VERIFIED |
| "Get out of the mindset of 'I need to provide something super valuable'..." | genius.md, Hidden Knowledge — 2026 additions, #1 (pre-existing) | same file | LIKELY (see ledger — 2026-07-01 export, not re-derived this session) |
| "The worst thing you can do is follow one specific person's advice law..." | genius.md, Hidden Knowledge — 2026 additions, #6 (pre-existing) | same file | LIKELY |
| "Never build the product first" | genius.md, Pattern: Validation Cascade + The 4-Hour Productization Trigger (pre-existing) | same file | LIKELY |
| `prompt_2_past_self_avatar_generator.md` | `references/prompts-v2/prompt_2_past_self_avatar_generator.md` | file exists on disk | VERIFIED (file-existence check, `ls`/`find` this session) |
| `advanced_prompt_4_high_density_insight_compressor.md` | `references/prompts-v2/advanced_prompt_4_high_density_insight_compressor.md` | file exists on disk | VERIFIED |
| `prompt_4_idea_museum_architect.md` | `references/prompts-v2/prompt_4_idea_museum_architect.md` | file exists on disk | VERIFIED |
| `advanced_prompt_17_philosophical_grounding_system.md` | `references/prompts-v2/advanced_prompt_17_philosophical_grounding_system.md` | file exists on disk | VERIFIED |
| `advanced_prompt_7_permission_based_conversion_engine.md` | `references/prompts-v2/advanced_prompt_7_permission_based_conversion_engine.md` | file exists on disk | VERIFIED |
| `prompt_6_content_to_system_productizer.md` | `references/prompts-v2/prompt_6_content_to_system_productizer.md` | file exists on disk | VERIFIED |
| "Energy reveals truth: Pay attention to what energizes you..." | genius.md, Tacit Expertise Made Explicit, item 2 (pre-existing) | same file | UNCONFIRMED as verbatim Dan Koe quote — synthesized behavioral description, no dated source file (see ledger) |
| Eugene Schwartz sophistication-stage reference | genius.md, Pattern: Market Sophistication Endgame (pre-existing) | same file | LIKELY (2026-07-01 export) |
| claude-export tarball check | `_archive/claude-export-2026-07-01.tar.gz` | archive root | CHECKED (332,779,255 bytes; `tar tzf` filename search for "koe" = 0 hits; not extracted) |

## Rule-2 compliance note
Before treating any source as absent, this repair verified: `extractions/`
contains a real `dan-koe/` directory with two non-trivial files (26,836 +
14,529 bytes, both read in full — not 0-byte, not unrecoverable). The
`_active/codex-harvest-2026-06-11/` tree was checked and contains only a
duplicate `SKILL.md` (already reflected in `SKILL.md.old`), no new source
material. The claude-export tarball was confirmed to exist and sized (332MB)
rather than assumed absent or fabricated as read.
