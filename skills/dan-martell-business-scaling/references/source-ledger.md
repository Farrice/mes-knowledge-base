# Dan Martell — Source Ledger

Claim-by-claim provenance for `skills/dan-martell-business-scaling/`. Every source consulted is listed, including negative searches (files checked, not found).

## Sources Consulted

| Source | Type | Size | Status |
|---|---|---|---|
| `extractions/dan-martell/transcript.txt` | Primary — full transcript, YouTube "Give Me 20 Minutes and I'll Make You Insanely Rich" (~25 min) | 24,265 bytes (`wc -c`) | READ IN FULL |
| `extractions/dan-martell/extraction-report.md` | Secondary — MES extraction summary derived from the transcript | 9,577 bytes (`wc -c`) | READ IN FULL |
| `_active/harness/codex-harvest-2026-06-11/extractions/` | Searched for `*martell*` (`find ... -iname "*martell*"`) | n/a | NO MATCHES — directory exists, glob returned zero files |
| `_archive/claude-export-2026-07-01.tar.gz` | Searched via `tar -tzf ... \| grep -i martell` | 332,779,255 bytes (`ls -la`) | NO MATCHES — archive listed successfully, zero entries contain "martell" |

No other Dan Martell source material exists in this repo as of this repair pass. All genius.md / SKILL.md claims trace to the two files above unless labeled otherwise.

## Claim-by-Claim Labels

### Biographical claims
- "3x SaaS exit CEO," "$100M+ enterprise value," "29 years in business" — **VERIFIED**. Verbatim in transcript.txt opening: *"took me from broke to $100 million plus CEO... spent the last 29 years... I've exited three software companies."*
- "Author of *Buy Back Your Time*" — **LIKELY**. Not stated in transcript.txt itself; asserted in extraction-report.md line 7 ("author of 'Buy Back Your Time'"). This is a real, publicly known book by Dan Martell (2023) but is not verifiable against a primary source held in this repo, so it is not VERIFIED — it is a well-known claim carried from the extraction step.

### Genius Patterns 1-8 (genius.md)
All eight — Constraint Telescope, Subtraction Before Addition, Bonus Bank Architecture, Flywheel Over Motivation, Price Anchor Engineering, Partner-at-Point-of-Sale, Output-Only Measurement, The Vacation Test — **VERIFIED**. Each traces to a specific numbered "Cheat code" in transcript.txt (Cheat Codes 4, 5, 6, 9, 10, 11, 12, 14, 15, 18 map directly; see SKILL.md's Cheat Code Coverage Map for the full crosswalk). Direct quotes added during this repair pass (e.g., "My feelings don't matter. I follow it. I get results. I create momentum.") were checked verbatim against transcript.txt before insertion.

### Hidden Knowledge (genius.md)
Echo Marketing, Competition = Validation, Standards ≠ Aspirations, The Bank Statement Test, Moat = Uncopyable Compound Asset, Irresistible Offer = 4 Components — **VERIFIED**. All quotes verbatim-checked against transcript.txt (Cheat Codes 1, 4, 7, 8, 13).

### Anti-Patterns (new section, this repair pass)
All six anti-pattern bullets — **VERIFIED**. Each quote confirmed as an exact substring of transcript.txt via direct string search before being written into genius.md (never paraphrased into a quoted form).

### Hall of Fame Exemplars + Anti-Exemplar (genius.md)
"The SaaS Company's Churn Cure," "The Coaching Program's Revenue Jump," "The Perpetual Discount Trap" — **UNCONFIRMED**. These are illustrative composites applying Martell's verified frameworks (correctly labeled with a provenance note added in this repair pass) — no company names, dollar figures, or outcomes ("20% conversion increase," "$15,000 VIP tier") appear in transcript.txt or extraction-report.md. They should be read as worked examples, not real case studies Martell described.

### Signature Moves (genius.md)
All five moves — **VERIFIED**. Each is a direct rephrasing of a transcript.txt Cheat Code with the underlying quote traceable (see genius.md Genius Patterns / Hidden Knowledge sections for the matching verbatim quote).

### Expert-Specific Quality Rubric (genius.md)
**LIKELY**. Synthesized scoring criteria extrapolated from the verified genius patterns — not a Martell quote or framework named in the source, but a direct, defensible operationalization of his stated principles (e.g., "Constraint Focus Clarity" operationalizes the verified Constraint Telescope pattern).

### Workflow 03 (`03-buyback-audit.md`) — "Delegation Timing Calculus (Phase 0)"
**UNCONFIRMED as a Martell framework** — this is a system-added elaboration (dated 2026-04-09 in the file's own header, pre-existing this repair pass, not modified here) that extends the verified Buyback/Vacation Test patterns with a break-even formula. It is a deployable extension built on top of verified source material, not something Martell states in transcript.txt.

### Workflow Output Schema/Quality Gate content (all 10 workflows)
The deliverable structures (tables, dashboards, scripts) are **LIKELY** — direct operationalizations of VERIFIED patterns (e.g., the 3-tier pricing table operationalizes the VERIFIED Price Anchor Engineering pattern), not verbatim Martell material. No claim of Martell having produced these exact templates is made or implied.

## Labeling Key
- **VERIFIED** — quote or fact confirmed as an exact match against a primary source file in this repo.
- **LIKELY** — reasonable extrapolation from verified material, or a well-known fact not present in the primary source held here.
- **UNCONFIRMED** — no source in this repo supports the specific claim (names, figures, outcomes); flagged so it is never mistaken for a real case study.
