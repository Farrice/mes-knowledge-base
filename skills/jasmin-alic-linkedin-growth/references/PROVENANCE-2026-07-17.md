# PROVENANCE — jasmin-alic-linkedin-growth repair

Anchor → source file + location, for every new claim/quote added this pass.
All entries are cross-referenced in `references/source-ledger.md` (claim-by-
claim table with VERIFIED/LIKELY/UNCONFIRMED labels).

| Anchor (in repaired genius.md) | Source file | Location |
|---|---|---|
| "Great post! So much value here. Really resonated with me. Keep up the good work!" | `skills/jasmin-alic-linkedin-growth/genius.md` (pre-existing, unmodified) | § Hall of Fame Exemplars → Anti-Exemplar, line 91 |
| "Marketers default to isolating pitches into standalone 'sales posts'..." | `extractions/Jasmin_Alic_Extraction.md` | Hidden Knowledge — "The 'Un-Salesy' Mid-Post Tag", line 51 |
| "People treat comments as chores or forced engagement..." | `extractions/Jasmin_Alic_Extraction.md` | Hidden Knowledge — "The Comment Laboratory", line 50 |
| "Never DM-pitch a stranger and never post a 'sales post'..." | `skills/jasmin-alic-linkedin-growth/genius.md` (pre-existing, unmodified) | § Patterns from claude.ai export, pattern 1, line 131 |
| "anchor... in real, named specificity and quantified stakes, never generic transformation" | `skills/jasmin-alic-linkedin-growth/genius.md` (pre-existing, unmodified) | § Patterns from claude.ai export, pattern 4, line 143 |
| "Must stop before line 4 so it naturally truncates on all devices" | `extractions/Jasmin_Alic_Extraction.md` | Methodology → Level 2: Hook Architecture, line 38 (also mirrored at `genius.md` line 34 pre-existing) |
| "DM me to learn more" | `skills/jasmin-alic-linkedin-growth/genius.md` (pre-existing, unmodified) | § Expert-Specific Quality Rubric, "Engagement Intent (Post)" row, line 115 |
| "Hear me out," "See how different these two are?," "Boom." | `extractions/Jasmin_Alic_Extraction.md` | Agent Configuration → Voice & Style, line 104 |

## Verification method
Every quote above was located via direct `Read` of the cited file at the
cited line before being reused. No quote was paraphrased into quotation
marks; where markdown nesting required a single-quote substitution for an
inner term (e.g. "sales post" → 'sales post'), the substitution is
typographic only — wording is unchanged and traceable to the same line.

## Absence checks performed
- `grep -rl "c10c06cd" --include="*.md" .` (repo-wide) → no hits outside
  `skills/jasmin-alic-linkedin-growth/genius.md` itself. The claude.ai export
  referenced by that section's own heading is not present as a separate file
  anywhere in the repo. This is a confirmed absence (searched, not assumed)
  — labeled LIKELY rather than UNCONFIRMED in the ledger because the content
  is pre-existing shipped skill material, not newly authored this pass.
- `find . -iname "*jasmin*"` → no raw/dated transcript file beyond
  `extractions/Jasmin_Alic_Extraction.md` (8,268 bytes, confirmed non-empty
  via `ls -la`).
