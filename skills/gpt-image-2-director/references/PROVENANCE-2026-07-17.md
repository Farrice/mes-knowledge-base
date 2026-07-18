# Provenance — gpt-image-2-director repair

Anchor → source file + location, for everything added in `genius.md`, `references/source-ledger.md`, and `workflows/*.md`.

| Anchor / claim | Source file | Location |
|---|---|---|
| "Avoid 'photorealistic' when faces are in frame... plasticky-skin failure mode." | `skills/gpt-image-2-director/SKILL.md` | line 119 |
| "If the concept fits multiple, pick the one best suited to the subject — don't hedge." | `skills/gpt-image-2-director/SKILL.md` | line 23 |
| "Return only the finished prompt in a code block... no format-choice justification." | `skills/gpt-image-2-director/SKILL.md` | line 156 |
| "Specific over atmospheric... GPT Image 2.0 executes specificity better than it interprets mood." | `skills/gpt-image-2-director/SKILL.md` | line 115 |
| GPT Image 2's #1 strength = prompt following on layout | `skills/gpt-image-2-director/SKILL.md` | line 14 |
| Six-section Format C structure (opening line, derivations, Overall Style, Composition Rules, Visual Quality, Typography System, Signature) | `skills/gpt-image-2-director/SKILL.md` | lines 124-150 |
| Canonical Format B prose exemplar ("A cinematic, moody photograph of a young Asian woman...") | `skills/gpt-image-2-director/SKILL.md` | line 122 |
| "GPT Image 2 is the strongest text-rendering model around... If a title runs more than ~6 words, expect typos; shorten and re-run." | `skills/fantastic-posters/README.md` | line 150 |
| Quality tiers: `low` ~$0.011 (10-15s), `medium` ~$0.04 (25-40s), `high` ~$0.17 (60-90s) | `skills/fantastic-posters/README.md` | lines 142-146 |
| Default portrait size 1024×1536; model "maxes out at 1536 on a side" | `skills/fantastic-posters/README.md` | line 148 |
| Independent confirmation of ~6-word title ceiling as "known weak spot," fixed via masked re-render | `skills/fantastic-posters/genius.md` | line 171 |
| "GPT Image 2 supports up to 3840×2160 at ≤ 3:1 aspect, multiples of 16... Invalid sizes are rejected before the API call." | `directives/fal-usage-policy.md` | line 103 |
| Edit endpoint `openai/gpt-image-2/edit`, "the strongest text-preserving image-edit model on Fal" | `directives/fal-edit-mode-guide.md` | line 6 |
| Source note: patterns harvested from `robonuggets/gpt-image-2-skill` (MIT), 2026-04-30 | `directives/fal-edit-mode-guide.md` | line 3 |
| "The model's job is to find the delta... surgical edit." | `directives/fal-edit-mode-guide.md` | line 105 |
| "Rule of thumb: edit changes content; regenerate changes design." | `directives/fal-edit-mode-guide.md` | line 22 |
| "Common gotcha: a JPEG mask compresses gray values and softens edges → use PNG." | `directives/fal-edit-mode-guide.md` | line 78 |
| Mask convention: white = edit, black = preserve | `directives/fal-edit-mode-guide.md` | line 76 |
| "GPT Image 2.0" (this skill) vs. "GPT Image 2" (real usage-policy captures) naming gap | `skills/gpt-image-2-director/SKILL.md` (title, lines 6, 17) vs. `directives/fal-usage-policy.md`, `directives/fal-edit-mode-guide.md`, `skills/fantastic-posters/README.md` | UNCONFIRMED whether ".0" is an official OpenAI suffix — flagged, not resolved (out of scope, additive-only) |
| No dedicated `extractions/` folder exists for GPT Image 2 / OpenAI as a named source capture | `extractions/` directory search | `find extractions -maxdepth 1 -iname "*gpt-image*" -o -iname "*openai*"` → zero results (run 2026-07-17, this session) |

All file sizes for presence/absence claims recorded via `wc -c` (bytes) — see `references/source-ledger.md` table for the full byte-count log.
