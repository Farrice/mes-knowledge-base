# Source Ledger — mark-kashef-banana-squad

Claim-by-claim provenance. Ground truth checked against `extractions/mark-kashef-banana-squad/`
(read in full: `extraction-report.md` + `prompts/` + `prompts-v2/`) and `extractions/mark-kashef/`
(the only other Kashef extraction on disk). File sizes below are `wc -c` on 2026-07-18.

## Source Inventory (VERIFIED — files read directly, sizes confirmed)

| File | Bytes | Contains |
|---|---|---|
| `extractions/mark-kashef-banana-squad/extraction-report.md` | 4,212 | Expert Profile, Genius Patterns 1-6, Hidden Knowledge 1-4, Crown Jewel Prompts 1-4 |
| `extractions/mark-kashef-banana-squad/prompts/banana-squad-spawn.md` | 1,828 | v1 spawn prompt |
| `extractions/mark-kashef-banana-squad/prompts/critique-loop-optimizer.md` | 2,178 | v1 critic config prompt |
| `extractions/mark-kashef-banana-squad/prompts/reference-reverse-engineer.md` | 2,426 | v1 DNA-extraction prompt |
| `extractions/mark-kashef-banana-squad/prompts/visual-capitalist-infographic.md` | 1,961 | v1 infographic prompt |
| `extractions/mark-kashef-banana-squad/prompts-v2/banana-squad-spawn.md` | 3,308 | structure-pure v2, dated 2026-07-11 in frontmatter |
| `extractions/mark-kashef-banana-squad/prompts-v2/critique-loop-optimizer.md` | 3,148 | v2, 3 presets (6/10, 7.5/10, 8.5/10 thresholds) |
| `extractions/mark-kashef-banana-squad/prompts-v2/reference-reverse-engineer.md` | 4,193 | v2 DNA-extraction prompt |
| `extractions/mark-kashef-banana-squad/prompts-v2/visual-capitalist-infographic.md` | 3,498 | v2 infographic prompt |

**No raw video transcript, no YouTube URL, and no timestamped source exists anywhere in
`extractions/mark-kashef-banana-squad/`** — confirmed by directory listing and full-text grep for
`youtube|url|http|transcript` across every file in the folder (zero hits). The `extraction-report.md`
`Source:` line claims "YouTube transcript + companion files," but the transcript itself is absent
from the repo. This claim of absence is itself verified by direct file reads, per the envelope's
rule 2 — not asserted without checking.

## Distinct Extraction — Not Conflated

`extractions/mark-kashef/` (no `-banana-squad` suffix) is a **separate** extraction: "7 Agent Team
Use Cases," ~20-min YouTube video, domain = general multi-agent orchestration (pitch decks, RFPs,
advisory boards) — not image generation. Same named person, LIKELY the same real-world Mark Kashef
(consistent domain: multi-agent AI orchestration), but the banana-squad content is NOT drawn from
that transcript. No claim in this skill borrows from `extractions/mark-kashef/transcript.txt`.

## Claim Labels

| Claim | Label | Basis |
|---|---|---|
| Genius Patterns 1-6 (Agent Pipeline, Narrative Prompting, DNA Extraction, 5 Prompts, Critic KPIs, Conversational Iteration) | VERIFIED | Verbatim match against `extraction-report.md` — read directly, text confirmed identical to `genius.md` |
| Hidden Knowledge 1-4 (14-image ceiling, Resolution Stacking, Brand Folder Architecture, Google Search Grounding) | VERIFIED (pattern) / UNCONFIRMED (implementation detail on #4) | Text matches `extraction-report.md`; the exact Gemini API grounding parameter name is not documented in any file on disk |
| Quote: "A macro photograph of morning dew on a spider web, shot on a Canon EOS R5 with a 100mm macro lens..." | VERIFIED | Present verbatim in `extraction-report.md` Genius Pattern 2 |
| Quotes: "make the background darker" / "add more texture to the fabric" | VERIFIED | Present verbatim in `extraction-report.md` Genius Pattern 6 |
| Critic preset thresholds (6/10, 7.5/10, 8.5/10) and MAX_ITERATIONS (1/2/3) | VERIFIED | Present verbatim in `references/prompts-v2/critique-loop-optimizer.md` |
| Crown Jewel Prompts 1-4 (names + descriptions) | VERIFIED | Matches `extraction-report.md` and the actual files in `prompts-v2/` |
| **Hall of Fame Exemplars 1-3** (Neo-Noir Cityscape / Obsidian Rain, Heritage Brand Wallet, Generic Sci-Fi anti-exemplar) | **UNCONFIRMED** | Does NOT appear in `extraction-report.md` or any file in `extractions/mark-kashef-banana-squad/` — grepped for "Neo-Noir," "Obsidian Rain," "Heritage Brand," "Artisan Leather," zero hits. These were added to `genius.md` (lines 60-93 of the pre-repair file) by a process not traceable to this skill's source files. Treated as illustrative composites consistent with the verified methodology, not verified transcript moments. Left in place (additive-only boundary) with an inline provenance note added to each exemplar. |
| **Signature Moves** section | LIKELY | Restates Genius Patterns 1-6 in a different format (1:1 mapping confirmed) — no new unsourced claims, but also not present verbatim in `extraction-report.md` as a standalone section |
| **Expert-Specific Quality Rubric** | UNCONFIRMED (framework) / VERIFIED (embedded numbers) | The 4/7/10 rubric table format is a house template, not a Kashef artifact; the numeric anchors filled into it (5 dimensions, 14-image ceiling, 3-5 recommended, 6/10-8.5/10 thresholds) are individually VERIFIED against source files as cited above. The pre-repair file's table was truncated mid-header (cut off after "Score 7 (Good)" with no rows) — completed here rather than left broken. |
| Anti-Patterns (6 items added in this repair) | Each item's underlying pattern is VERIFIED against the source file cited inline; the two exemplar-derived items inherit the exemplar's UNCONFIRMED provenance note as stated | See `genius.md` Anti-Patterns (Sourced) section |

## Repair Notes on This Ledger

This file was created 2026-07-18 as part of Wave 3 Lane 4 Batch 10 heartbeat repair. It did not
exist before this repair — `source_ledger` was a hard FAIL prior to this pass.
