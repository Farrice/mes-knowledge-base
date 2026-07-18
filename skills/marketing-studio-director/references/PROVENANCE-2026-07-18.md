# PROVENANCE — marketing-studio-director repair

Anchor → source file + location. All sources pre-existed in `skills/marketing-studio-director/`
before this repair; no `extractions/` source exists (confirmed via `ls extractions/ | grep -i higgsfield`
and `grep -i "marketing.studio"`, both empty).

| Anchor (genius.md section) | Source file | Location | Label |
|---|---|---|---|
| "Never restyle or 'improve' the product" | `skills/marketing-studio-director/SKILL.md` | Engine Rules block, line ~136 | VERIFIED |
| "Trigger words to avoid: boy, girl, child, kid, young, teen, little" | `skills/marketing-studio-director/SKILL.md` | Age-blind character rule, line ~40 | VERIFIED |
| "right hand rotates cap counterclockwise while left stabilizes base" (banned) vs. "twists the cap off, sets the bottle down" (approved) | `skills/marketing-studio-director/SKILL.md` | Engine Rules, line ~138 | VERIFIED |
| "The product smells fresh." (banned) vs. condensation/bottle example (approved) | `skills/marketing-studio-director/SKILL.md` | Engine Rules, line ~145 | VERIFIED |
| "No section labels (no 'Style & Mood:', 'Dynamic Description:', etc.)" | `skills/marketing-studio-director/SKILL.md` | Output Rules, line ~181 | VERIFIED |
| Antislop banned-word list (40+ terms) | `skills/marketing-studio-director/SKILL.md` | Antislop section, line ~232 | VERIFIED |
| "Avoid reflection shots (in screens, mirrors, glass, puddles)" | `skills/marketing-studio-director/SKILL.md` | Engine Rules, line ~144 | VERIFIED |
| 3 worked corpus examples (UGC/TV Spot/Hyper Motion quotes) | `skills/marketing-studio-director/SKILL.md` | Output Format section, lines ~155-177 | VERIFIED |
| 5 Genius Patterns | `skills/marketing-studio-director/references/genius-patterns.md` | Full file (1,808 bytes, 27 lines) | VERIFIED |
| Platform bias / failure mode ("reference drift") / operating rule | `skills/marketing-studio-director/references/hidden-knowledge.md` | Full file (546 bytes, 11 lines) | VERIFIED |
| 9-preset table, ≤15-second hard cap, Appendix B quick-reference | `skills/marketing-studio-director/SKILL.md` | Preset Router table (lines ~50-60) + Appendix B (lines ~246-258) | VERIFIED |
| `refactored: 2026-07-13` frontmatter date, `standard: structure-pure-v2`, Output Contract / Quality Gate headings | `skills/marketing-studio-director/references/prompts-v2/*.md` (all 9) | Frontmatter + `## Output Contract` / `## Quality Gate` headings, `grep`-confirmed in all 9 files | VERIFIED |
| Higgsfield generation link `https://higgsfield.ai/s/general-higgsfieldai-vKnfpx` | `skills/marketing-studio-director/SKILL.md` | Reproduced verbatim, not called/tested | UNCONFIRMED (URL liveness) |

No quote, statistic, or anchor in `genius.md`, `references/source-ledger.md`, or `workflows/*.md`
was invented — every one traces to a file that exists in `skills/marketing-studio-director/`
today and was read (not assumed) during this repair.
