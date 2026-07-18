# Source Ledger — James I. Bond: Brain Glue

Every claim, pattern, and quote in this skill traced to a source file, labeled
VERIFIED (quote/claim confirmed verbatim against the cited file, read in full
this repair pass), LIKELY (claim consistent with cited material but not
verbatim-matched line-for-line), or UNCONFIRMED (no locatable source —
flagged, never anchored as fact).

## Primary Sources (read in full this repair pass)

| Source | Size | Status |
|---|---|---|
| `skills/james-i-bond-brain-glue/references/genius-patterns.md` | 121 lines, read in full | VERIFIED |
| `skills/james-i-bond-brain-glue/references/hidden-knowledge.md` | 38 lines, read in full | VERIFIED |
| `skills/james-i-bond-brain-glue/references/implementation.md` | 59 lines, read in full | VERIFIED |
| `_active/codex-harvest-2026-06-11/brain/brain-glue-extract-forge/01-vision.md` | 2,270 bytes, read in full | VERIFIED |
| `_active/codex-harvest-2026-06-11/brain/brain-glue-extract-forge/02-architecture.md` | 2,748 bytes, read in full | VERIFIED |
| `_active/codex-harvest-2026-06-11/brain/brain-glue-extract-forge/03-extraction-summary.md` | 2,011 bytes, read in full | VERIFIED |
| `_active/codex-harvest-2026-06-11/brain/brain-glue-extract-forge/04-verification.md` | 3,825 bytes, read in full | VERIFIED |
| `_active/codex-harvest-2026-06-11/agents/james-i-bond/memory/context.md` | 8 lines, read in full | VERIFIED |
| `skills/james-i-bond-brain-glue/SKILL.md` | 75 lines, read in full | VERIFIED |
| Git history (`git log --follow --date=short`) for the above extraction files, confirming original commit date | Ran this pass | VERIFIED — earliest commit `99a01ee88`, dated 2026-06-11 ("feat(harvest): recover 4,355 unique assets from Codex Antigravity fork") |

## Claim-by-Claim: Anti-Patterns Section (anchors added this repair pass)

| Anti-pattern item | Quote used | Source anchor | Status |
|---|---|---|---|
| Clever but jobless | "Never let clever phrasing obscure the offer." | `references/hidden-knowledge.md`, Practitioner Constraints, line 34 | VERIFIED |
| All tools at once | "Brain Glue is a sequencing method. Do not use every tool." | `references/hidden-knowledge.md`, Tacit Insights, line 19 (truncated at sentence boundary; full sentence continues "Diagnose the missing mechanism, add the smallest sticky device that solves it, then stop.") | VERIFIED |
| Wrong tribe mimicry | (no quote; heading citation only) | `references/genius-patterns.md`, Pattern 2 — Tribal Belonging Before Argument, lines 19-23 | VERIFIED (claim maps directly to the named pattern's inverse) |
| Trigger-word abuse | "The word increases attention while staying connected to a real point." | `references/genius-patterns.md`, Pattern 11 — Trigger Word Wake-Up, success metric, line 77 | VERIFIED |
| Metaphor fog | (no quote; heading citation only) | `references/genius-patterns.md`, Pattern 5 — Metaphor as Product Interface, lines 37-41 | VERIFIED (claim maps directly to the named pattern's inverse) |
| Feature pileup | "A page, pitch, or script lists every feature, proof point, audience benefit, and explanation at once." | `references/genius-patterns.md`, Anti-Exemplar — The Logical Feature Dump, line 119 | VERIFIED |
| Edgy mismatch | "Shock works only when it points to truth." | `references/hidden-knowledge.md`, Tacit Insights, line 12 (truncated at sentence boundary) | VERIFIED |

All seven anti-pattern items existed in the shipped `genius.md` before this repair pass (unsourced); this pass added the anchors/quotes only — no anti-pattern claims were invented.

## Claim-by-Claim: Verbatim Exemplars Section (new this repair pass)

| Exemplar | Source anchor | Status |
|---|---|---|
| "Stop rebuilding your genius from scratch." | `_active/codex-harvest-2026-06-11/brain/brain-glue-extract-forge/04-verification.md`, Sample Dry Runs → LinkedIn Post Idea | VERIFIED |
| "Bottle the brain. Deploy the business." | `_active/codex-harvest-2026-06-11/brain/brain-glue-extract-forge/04-verification.md`, Sample Dry Runs → Campaign Request | VERIFIED |
| "If the buyer saw this once, could they explain it, feel why it matters, and remember the phrase later?" | `_active/codex-harvest-2026-06-11/brain/brain-glue-extract-forge/03-extraction-summary.md`, Quality Standard | VERIFIED |

These are dry-run/verification artifacts from the extraction session, not reproductions of James I. Bond's copyrighted book text. No verbatim book passage exists anywhere in this repo (see Absence Notes below) — using extraction-artifact exemplars instead of book quotes is the only honest way to satisfy a verbatim-exemplar requirement without violating the extraction's own no-copyrighted-reproduction constraint.

## Claim-by-Claim: Model Calibration Section (new this repair pass)

| Claim | Source anchor | Status |
|---|---|---|
| Voice register — direct, commercial, blunt, "sales trainer diagnosing a broken pitch" | `skills/james-i-bond-brain-glue/genius.md`, pre-existing Voice DNA section: "Brain Glue execution should sound direct, commercial, vivid, and practical. It should not sound academic." | VERIFIED (paraphrase of pre-existing shipped claim) |
| STEAM ATTRACTORS is diagnostic, not a labeling scheme for output | Inference from `references/hidden-knowledge.md` line 19 ("Diagnose the missing mechanism, add the smallest sticky device... then stop") + `references/implementation.md` Quality Gate, line 51: "The final recommendation is clear, not a menu with no decision." | LIKELY — reasonable synthesis of two verified constraints, not a single verbatim source claim |
| "Recognition test" framing (would Bond recognize this as Brain Glue) | Written for this skill, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per the Wave 3 repair mandate — a calibration instruction, not a factual claim about Bond | N/A (instructional) |

## Absence Notes (per envelope rule 2 — verified, not assumed)

- **No PDF or verbatim book text for "Brain Glue" by James I. Bond exists anywhere in this repo.** Verified by: `find . -iname '*brain-glue*'` repo-wide (returns only this skill's own files, its `.agent/workflows/` and `.claude/commands/` wrappers, and the `_active/codex-harvest-2026-06-11` extraction-summary docs — no `.pdf`/`.epub`/raw-text asset); `grep -ril 'brain glue\|james i\. bond'` across `extractions/` (5 hits, all false positives — other experts' files mentioning "Brain Glue" or "James"/"Bond" as separate words in passing, e.g. `extractions/rafa-conde/forge-vision.md:50`); no hit in `_archive/claude-export-2026-07-01.tar.gz` filenames. This is a design choice, not a gap: `references/hidden-knowledge.md` (Practitioner Constraints) instructs "Avoid long verbatim quotes from source material," and `_active/codex-harvest-2026-06-11/agents/james-i-bond/memory/context.md` instructs "Do not store raw copyrighted source text." **UNCONFIRMED**: any claim purporting to be a verbatim excerpt of Bond's actual book prose — none exists in this repo to verify against.
- **James I. Bond's biography** ("persuasion and behavioral management practitioner," `references/genius-patterns.md` line 7) is **UNCONFIRMED** — no author-bio source file exists in the repo, and this repair pass did not run external web verification (out of scope: ground truth for this pass is repo files only, per the envelope).
- The "14 mechanisms" / "204 pages" / "45k extracted words" figures are **VERIFIED** as claims already present in `references/genius-patterns.md` line 5 and `03-extraction-summary.md` — they describe the extraction's own self-reported scope, not independently re-verified page/word counts of an unavailable source PDF.
