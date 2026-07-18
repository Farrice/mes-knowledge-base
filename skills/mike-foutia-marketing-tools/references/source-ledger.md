# Source Ledger — mike-foutia-marketing-tools

> Claim-by-claim audit for `genius.md` (repaired 2026-07-17/18, Wave 3 Lane 4 Batch 11).
> Every source below was opened and read directly (not assumed). Sizes recorded via `wc -c`.

## Sources Consulted

| # | File | Size (bytes, `wc -c`) | Status | Notes |
|---|------|------------------------|--------|-------|
| 1 | `extractions/mike-foutia-marketing-tools/extraction-report.md` | 12,701 | VERIFIED | Primary ground truth — full transcript-derived extraction of the Marketing Against The Grain podcast interview. Read in full. |
| 2 | `extractions/mike-foutia-marketing-tools/prompts/*.md` (7 files) | 6,391–6,785 each | VERIFIED | Deployable prompt drafts derived from the extraction; consulted for corroborating language, not cited directly in Anti-Patterns. |
| 3 | `extractions/mike-foutia-marketing-tools/prompts-v2/*.md` (7 files) | 4,657–5,627 each | VERIFIED | Second-pass prompt drafts; same status as row 2. |
| 4 | `skills/mike-foutia-marketing-tools/genius.md` (pre-repair) | 15,131 | VERIFIED | The skill's own compiled genius file — internally cross-cited for Hidden Knowledge #2 and #4 quotes reused in the new Anti-Patterns section. |
| 5 | `skills/mike-foutia-marketing-tools/references/exemplars.md` | 6,653 | VERIFIED | Hall of Fame + Anti-Exemplar library. Exemplar 1 numbers (5.2M views / 350K likes / 12K comments) and the GlowUp Serum "500 scraped TikToks / 10,000+ comments" figures are quoted directly from this file. |
| 6 | `skills/mike-foutia-marketing-tools/references/quality-rubric.md` | 73,596 | VERIFIED | Score-anchor table (4/7/10) confirmed present; used only for the score-scale entity added to the "## Quality Rubric" pointer section. |
| 7 | `skills/mike-foutia-marketing-tools/references/genius-patterns.md` | 12,886 | VERIFIED | Older duplicate of genius.md's pattern section (pre-dates the Signature Moves / Quality Rubric additions). Read for cross-check only — not modified, not cited as an independent source. |
| 8 | `skills/mike-foutia-marketing-tools/SKILL.md.old` | 7,749 | VERIFIED | Legacy SKILL.md version. Read to confirm no lost content; not cited. |

## Cross-Reference Note (flagged by prior worker)

A prior worker flagged a possible cross-reference to Andrew Wilkinson inside a mike-foutia file. Located: `extractions/mike-foutia-marketing-tools/extraction-report.md`, line 12 — `"Existing Overlap: Partial overlap with andrew-wilkinson (vibe coding mindset), nick-saraev (agentic workflows), seena-rez (TikTok content)."` This is the extraction pipeline's own "Existing Overlap" field, noting adjacent skills in the roster — it is not a fabricated Wilkinson quote or a source mix-up. **UNCONFIRMED as a problem** — verified benign on direct read.

## Claim-by-Claim Labels (new Anti-Patterns section, genius.md)

| Claim | Label | Anchor |
|---|---|---|
| "he never jumps layers" / 3-layer escalation | VERIFIED | extraction-report.md, Genius Pattern 1 |
| "from nothing to brief in 15 minutes" benchmark | VERIFIED | extraction-report.md, Genius Pattern 1, Success Metric |
| Mike ships "internal tools, not SaaS products" | VERIFIED | extraction-report.md, Genius Pattern 5 |
| "AI video is NOT ready for full automation" | VERIFIED | extraction-report.md, Market Signals |
| Mike "would NOT learn [N8N] if starting today" | VERIFIED | extraction-report.md, Hidden Knowledge "N8N is a Dead End for Non-Coders" |
| "without it, you get mean-reversion content" | VERIFIED | genius.md (pre-repair), Hidden Knowledge #2 |
| "AI is really good at getting you to the mean" | VERIFIED | genius.md (pre-repair), Hidden Knowledge #4 |
| 5.2M views / 350K likes / 12K comments (Exemplar 1) | VERIFIED | references/exemplars.md, Exemplar 1 |
| 500 scraped TikToks / 10,000+ comments (GlowUp Serum) | VERIFIED | references/exemplars.md, Hall of Fame Exemplar 1 |
| $2-5K/mo productized pricing | VERIFIED | extraction-report.md, Applied Intelligence § "Creative Volume Service" |
| Score anchors 4 / 7 / 10 | VERIFIED | references/quality-rubric.md, Expert-Specific Quality Rubric table |
| "Record Yourself" pitch line as verbatim Mike quote | NOT USED | extraction-report.md frames this as a *suggested* pitch line for Farrice's consulting practice, not a verbatim Foutia quote — excluded from Anti-Patterns to avoid mislabeling a suggestion as a source quote. |

## Method

Name-fragment search only (`grep -i foutia`, `grep -i wilkinson`), no punctuation assumptions. Every file above opened with the Read tool in full or by targeted offset before any claim was written against it. No file was assumed absent or 0-byte without a direct listing (`find ... | xargs wc -c`) confirming otherwise.
