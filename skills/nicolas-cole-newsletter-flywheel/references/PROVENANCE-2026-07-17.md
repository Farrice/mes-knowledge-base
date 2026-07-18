# Provenance — nicolas-cole-newsletter-flywheel repair (2026-07-17)

Anchor → source file + location, for every claim touched or added in this repair. No new facts about Nicolas Cole were introduced — all additions are either (a) structural (Output Schema/Quality Gate scaffolding around content the workflow files already contained) or (b) explicit sourcing/provenance labels on claims that were already present.

| Anchor / Addition | File : Location | Source | Status |
|---|---|---|---|
| "How to Use This Skill (Model Calibration)" section | `genius.md` (new section after title) | Synthesized from this file's own existing Genius Patterns #1-8 and Anti-Topic Principle (genius.md lines 26-73 in original); modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per ENVELOPE instruction. No new Cole facts introduced — restates existing patterns as model-calibration guidance. | N/A — methodology guidance, not a factual claim |
| Recognition-test sentence ("would Cole recognize this as...") | `genius.md`, inside Model Calibration section | Same as above — built from existing Wine Club Test / Faucet Test content already in genius.md (original lines 68-72, 118-120) | N/A — methodology guidance |
| Provenance note under Content Assessment | `genius.md`, after Content Assessment code block | `extractions/nicolas-cole/transcript.txt` (18,152 bytes, read in full) and `extractions/nicolas-cole-digital-products/transcript.txt` (39,852 bytes) + `extraction-report.md` (13,760 bytes), both read in full | VERIFIED file sizes and contents — confirmed via direct read, not assumed |
| Full claim-by-claim ledger | `references/source-ledger.md` (new file) | Same two extraction folders, cross-checked against every genius.md claim | See ledger for per-row VERIFIED/LIKELY/UNCONFIRMED |
| "$400,000 a year in subscription revenue... over a million dollars as a vertical" | `references/source-ledger.md` row 1 | `extractions/nicolas-cole-digital-products/transcript.txt`, opening ~400 chars | VERIFIED — verbatim string match confirmed |
| "Ship 30 for 30... over $3 million in revenue" | `references/source-ledger.md` row 2 | `extractions/nicolas-cole-digital-products/transcript.txt`, same paragraph | VERIFIED — verbatim string match confirmed |
| $350 low-ticket ceiling, tied to 22-23 Ship 30 for 30 cohorts | `references/source-ledger.md` row 3 | `extractions/nicolas-cole-digital-products/transcript.txt`, char offset ~11,314 | VERIFIED — verbatim string match confirmed |
| "over a billion views... The Art and Business of Online Writing" | `references/source-ledger.md` row 4 | `extractions/nicolas-cole/transcript.txt`, closing lines | VERIFIED — verbatim string match confirmed |
| "A paid newsletter is a book that never ends" (internal saying) | `references/source-ledger.md` row 9 | `extractions/nicolas-cole-digital-products/extraction-report.md`, line 81 | VERIFIED — direct file read, line 81 |
| Two Rules framework (Book That Never Ends + Tangible Faucet, full pedagogy) | `references/source-ledger.md` rows 6-7 | Searched: `grep -rli "saunders\|wine club\|tangible faucet\|never want.*turn off" extractions/` — zero hits in any Nicolas Cole folder | UNCONFIRMED — genuinely absent, not a false claim (both candidate transcripts read in full first) |
| George Saunders Story Club exemplar | `references/source-ledger.md` row 8 | Same search, zero hits | UNCONFIRMED — genuinely absent |
| Wine Club Test | `references/source-ledger.md` row 8 (combined row) | Same search, zero hits | UNCONFIRMED — genuinely absent |
| "#1 paid education newsletter on Substack" ranking claim | `references/source-ledger.md` row 5 | Searched both transcripts for "#1", "Write With AI" naming context — revenue figure confirmed, ranking claim not found | UNCONFIRMED (partial — revenue portion VERIFIED, ranking portion not) |
| 16 workflow "## Output Schema" + "## Quality Gate" sections | `workflows/01, 02, 03, 04, 05, 06, 07, 09, 10, 11, 12` (new sections) + `workflows/13, 14, 15, 16, 17` ("## Output" renamed to "## Output Schema") | Each section restates that SAME workflow file's own existing Process/Output content in schema form — no external facts, no new Cole claims. Anchor = the workflow file itself (its own pre-existing "Process" and prose "Output" sections, quoted structurally). | N/A — structural scaffolding, not a factual claim |

## Search commands run (for adversarial re-verification)

```bash
ls extractions/ | grep -i cole
ls extractions/ | grep -i nicolas
grep -n -i "faucet\|book that never ends\|saunders\|wine club\|never ends" extractions/nicolas-cole/transcript.txt extractions/nicolas-cole-digital-products/transcript.txt extractions/nicolas-cole-digital-products/extraction-report.md
grep -rli "saunders\|wine club\|tangible faucet\|never want.*turn off\|never ends" extractions/nicolas-cole*
grep -n -i "400,000\|Ship 30\|350\|cohort-based course" extractions/nicolas-cole-digital-products/transcript.txt
grep -n -i "billion views" extractions/nicolas-cole/transcript.txt
```
