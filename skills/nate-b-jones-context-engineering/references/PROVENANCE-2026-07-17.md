# PROVENANCE — nate-b-jones-context-engineering (Wave 3 Batch 2 Repair)

Anchor → source file + location, for every claim added or corrected in this repair pass. Compiled 2026-07-17. Full per-claim confidence detail lives in `references/source-ledger.md`; this file maps specifically to what changed in `genius.md` and the six `workflows/*.md` files.

## genius.md — Anti-Patterns section (new)

| Anchor in genius.md | Source file | Location | Confidence |
|---|---|---|---|
| "Context-rot compounds under auto-optimization" | `extractions/nate-b-jones/transcript.txt` | Karpathy Loop video, "context layer problem" passage (search: "reinventing a definition of done") | VERIFIED |
| "Activity metrics substitute for outcome metrics" | `extractions/nate-b-jones/transcript.txt` | Karpathy Loop video, "measuring activity instead of outcome" passage | VERIFIED |
| "Single-agent self-improvement underperforms specialized pairs" | `extractions/nate-b-jones/transcript.txt` | Karpathy Loop video, "Goose's team tried having a single agent improve itself" passage | VERIFIED |
| "Cross-model meta/task pairing degrades harness quality" | `extractions/nate-b-jones/transcript.txt` | Karpathy Loop video, "same model pairings dramatically outperform cross model pairings" passage | VERIFIED (includes the transcript's own ASR artifact "clawed" for "Claude," flagged in-line rather than silently corrected) |
| "Stripping reasoning traces collapses the improvement rate" | `extractions/nate-b-jones/transcript.txt` | Karpathy Loop video, "Goo's team only gave the meta agent scores without reasoning trajectories" passage | VERIFIED |
| "Skipping the deployment prerequisites cascades into failure" | `extractions/nate-b-jones/transcript.txt` | Karpathy Loop video, "graduate level capability" + "context layer problem is the most foundational" passages | VERIFIED |
| "Renting memory instead of owning it forfeits sovereignty" | `extractions/nate-b-jones/turbokvant-context-engineering-extraction.md` | GP-7 ("The Sovereign Memory Imperative") — quote already served as this document's own epigraph prior to this repair | VERIFIED (as inherited; not independently re-checked against a raw TurboQuant transcript, because none exists in `extractions/`) |

**Correction of record**: a stray, uncommitted draft found sitting directly in `skills/nate-b-jones-context-engineering/genius.md` at session start (written outside this envelope's `.tmp`-only boundary by an earlier, interrupted attempt at this same repair) had mislabeled the first anti-pattern's source as the TurboQuant video. No raw transcript exists for TurboQuant under `extractions/` — only its extraction summary. The quote is verbatim Karpathy Loop content. Fixed in this deliverable; the stray draft in `skills/` was left untouched (git-read-only boundary — see REPAIR-NOTES.md).

## genius.md — entity-floor enrichment sentences (18 sections touched)

Every sentence added to clear a zero-entity section restates or cross-references a number already established elsewhere in this same genius.md (pre-existing, sourced content): the 6x TurboQuant compression figure (GP-2, `turbokvant-context-engineering-extraction.md`), the 40% low-value-token diagnostic threshold, the 15% dedup floor (`turbokvant-context-engineering-extraction.md`, "24-Hour Quickstart"), the Tool Router's existing 3-5/95%/100+ figures (Framework 3, pre-existing), and Framework 4's existing 90-day episodic retention window. No new unsourced statistics were introduced — see `references/source-ledger.md` for the full claim-by-claim table, including the one figure (15-25% range) flagged LIKELY rather than VERIFIED because only the floor (≥15%) is directly sourced.

## genius.md — Model Calibration section (new)

Structural model only, no factual claims: `skills/ben-watkins-storytelling/genius.md`, lines 7-16 (read per envelope instruction). Content (Nate's quantified, cascading texture; "no output without a number attached") is drawn from the already-VERIFIED Framework 1-7 content in this same genius.md, not a new source.

## workflows/*.md — Quality Gate sections (5 files: all except tool-router-agent-blueprint.md, which already carried a passing "Quality Gates" bold-label section pre-repair)

Each Quality Gate checklist is derived from that workflow's own existing Steps/Output Format content (self-referential — e.g., context-bloat-diagnostic.md's gate cites its own Step 1/2/4/6; sovereign-memory-architecture-blueprint.md's gate cites its own Step 6 sovereignty checklist and the decay-mechanism thresholds already specified in genius.md Framework 4). No external claims introduced. One genius.md-sourced figure reused: the 40% low-value-token threshold and the ≥15% dedup floor (both VERIFIED per the table above).

## references/source-ledger.md

New file this pass. See the file itself for the full claim inventory, including the correction of an initial UNCONFIRMED label on the Framework 8 "Second-Brain Adoption Layer" — resolved to VERIFIED by locating `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/366d70e8-272a-4ef6-80ef-e725324c870c.md` (Nate B. Jones, "Why 2026 Is the Year to Build a Second Brain," YouTube transcript captured via Merlin AI, conversation dated 2026-01-09). This is the one place in this repair where the envelope's rule 2 ("a claim that sources are ABSENT is itself a provenance claim") was directly tested: the first draft of the ledger nearly shipped an UNCONFIRMED label before the archive was actually searched.
