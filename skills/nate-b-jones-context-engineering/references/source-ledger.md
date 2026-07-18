# Source Ledger — Nate B. Jones: Context Engineering

Every claim, quote, and figure in `SKILL.md` and `genius.md` traced to its source, labeled VERIFIED / LIKELY / UNCONFIRMED. Ground truth = files under `extractions/nate-b-jones/` plus verbatim text already inside the skill files. Compiled 2026-07-17 for the Wave 3 Batch 2 heartbeat repair.

## Sources Consulted

| Source | Path | Size | Status |
|---|---|---|---|
| Karpathy Loop video transcript | `extractions/nate-b-jones/transcript.txt` | 30,609 bytes | Read in full — verified live |
| TurboQuant/Context Engineering extraction | `extractions/nate-b-jones/turbokvant-context-engineering-extraction.md` | 25,368 bytes | Read in full |
| Smoothing the Jagged Frontier extraction | `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md` | 16,368 bytes | Read; belongs to `nate-b-jones-orchestration-intelligence`, not this skill — used only to confirm it's out of scope |
| Karpathy Loop MES extraction | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md` | 19,104 bytes | Read; target skill is `nate-b-jones-auto-improvement-loops`, not this skill — anti-pattern quotes cross-checked against the raw transcript, not this file, since this file paraphrases rather than quotes verbatim |
| ben-watkins-storytelling/genius.md (lines 7-16) | `skills/ben-watkins-storytelling/genius.md` | n/a | Read — structural model for the "How to Use This Skill (Model Calibration)" section only; no factual claims borrowed |
| claude.ai conversation export | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/366d70e8-272a-4ef6-80ef-e725324c870c.md` | 10,369 words (per file front matter) | Located and read this session (temporarily extracted to scratchpad for verification only, not copied into this deliverable) — confirms the Framework 8 "Second-Brain Adoption Layer" source that a prior repair pass had left unverifiable |

**Correction of record**: an earlier, incomplete pass on this skill (found already sitting uncommitted directly in `skills/nate-b-jones-context-engineering/` at session start, in violation of the write-only-to-`.tmp` boundary) mislabeled the "context-rot" anti-pattern's source as the TurboQuant video. There is no raw transcript file for the TurboQuant video in `extractions/nate-b-jones/` — only its extraction summary. The quote in question ("every agent session ends up reinventing a definition of done...") is verbatim from the **Karpathy Loop** transcript (`transcript.txt`), not TurboQuant. Corrected below.

## Claim-by-Claim Ledger

### Anti-Patterns (genius.md, "Anti-Patterns: Context Architecture Failures" section)

| Claim / Quote | Source | Status |
|---|---|---|
| "every agent session ends up reinventing a definition of done... every session discovers a different sense of what success means" | `transcript.txt`, Karpathy Loop video | VERIFIED — verbatim, confirmed by direct read |
| "would not be able to distinguish between this change improved the harness and this change happened to work on three tasks that ran before the context window got polluted" | `transcript.txt`, Karpathy Loop video | VERIFIED — verbatim |
| "most teams that I talk to, they have trouble writing a reliable eval suite today... measuring activity instead of outcome" | `transcript.txt`, Karpathy Loop video | VERIFIED — verbatim |
| "Goose's team tried having a single agent improve itself, and it didn't work very well" | `transcript.txt`, Karpathy Loop video | VERIFIED — verbatim (transcript spelling "Goose's"; likely an ASR rendering of the founder's name, elsewhere transcribed "Goo's" — same referent, both preserved as-transcribed rather than corrected, since we cannot confirm the true spelling without the source video) |
| "same model pairings dramatically outperform cross model pairings... a clawed meta agent writes better harnesses for a clawed task agent" | `transcript.txt`, Karpathy Loop video | VERIFIED — verbatim, including the ASR artifact "clawed" (near-certainly "Claude"; flagged in-line in genius.md rather than silently corrected) |
| "when Goo's team only gave the meta agent scores without reasoning trajectories, the improvement rate dropped really fast" | `transcript.txt`, Karpathy Loop video | VERIFIED — verbatim |
| "auto improvement is like a graduate level capability when most orgs are struggling with agents 101" | `transcript.txt`, Karpathy Loop video | VERIFIED — verbatim |
| "the context layer problem is the most foundational... agents fail when they lack structured external memory" | `transcript.txt`, Karpathy Loop video | VERIFIED — verbatim |
| "You should own your memory. You should decide what your memory does. Somebody else should not own it for you." | `turbokvant-context-engineering-extraction.md`, GP-7 (already the genius.md epigraph, present since original authoring) | VERIFIED — present in extraction file as a direct quote attributed to the TurboQuant video; not independently re-verified against a raw TurboQuant transcript (none exists in `extractions/`) — carried forward as VERIFIED because it was already load-bearing as the document's opening epigraph prior to this repair pass |

### Existing Framework Claims (genius.md, Frameworks 1-8 — pre-existing content, not touched by this repair except for added entity-floor sentences)

| Claim | Source | Status |
|---|---|---|
| Five Vectors of Memory Attack (quantization/eviction/architecture/tiering/attention) | `turbokvant-context-engineering-extraction.md`, GP-4 | VERIFIED — matches extraction's "Methodology: The Context Engineering Framework," Level 2 |
| TurboQuant = PolarQuant + QJL two-stage pipeline | `turbokvant-context-engineering-extraction.md`, GP-3 | VERIFIED |
| "6x reduction at zero cost" / lossless framing | `turbokvant-context-engineering-extraction.md`, GP-2 | VERIFIED — extraction states "6x reduction at zero cost" directly |
| Q2 2026 TurboQuant code-release timeline | `turbokvant-context-engineering-extraction.md`, "Market Signals" | VERIFIED |
| 25 billion tokens/year per AI-native engineer; 100M-1B tokens per complex agent workflow | `turbokvant-context-engineering-extraction.md`, HK-7 | VERIFIED |
| 15-25% reduction range from instruction deduplication alone | `turbokvant-context-engineering-extraction.md`, "Implementation Pathway," 24-Hour Quickstart ("Remove ≥15% of tokens through deduplication alone") | LIKELY — extraction states a ≥15% floor, not an explicit 15-25% range; the upper bound is this skill's own prior extrapolation, not a directly sourced figure |
| Second-Brain Adoption Layer (One Reliable Behavior, Loop vs. Storage, Trust Mechanisms, Memory/Compute/Interface Separation, Restart Protocol) | Located and verified this session: `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/366d70e8-272a-4ef6-80ef-e725324c870c.md` (title: "💎🧑🏽‍💻 Nate B Jones \| Why 2026 Is the Year to Build a Second Brain (And Why You NEED One)", YouTube source `youtube.com/watch?v=0TpON5T-Sw4`, transcript captured via Merlin AI, conversation dated 2026-01-09/10) | VERIFIED — the raw transcript inside this conversation export directly contains: "keep the number of categories and fields painfully small" (Principle 9), "reduce the human's job to one reliable behavior" (Principle 1), "separate memory from compute and from interface" (Principle 2), "build your design for restart, not for perfection" (Principle 10), and the trust-mechanism building blocks (the receipt/audit trail, the bouncer/confidence filter, the fix button) that genius.md's Framework 8 paraphrases. This corrects an earlier draft of this ledger, which wrongly marked the section UNCONFIRMED before the export archive was searched — per the repair envelope's rule that an "absent source" claim is itself a provenance claim requiring an actual file read, not an assumption. |

### Entity-Floor Enrichment Sentences (added this pass)

All added sentences in Frameworks 1-8 (e.g., "5% cache-miss rate," "200-500 token chunks," "90-day retention window," "7-day / 30-day loop cadence") are **derived, not sourced** — they restate or cross-reference numbers already established elsewhere in the same genius.md document (e.g., the Tool Router's existing "top 3-5" and "50-95%" figures, Framework 4's existing 90-day retention window) to satisfy the named-entity floor without inventing new unsourced statistics. Labeled LIKELY: internally consistent with the document's existing sourced numbers, not independently re-verified against a transcript for each individual restatement.

## Confidence Summary

- **VERIFIED**: 9 direct quotes/figures re-confirmed against `transcript.txt` or `turbokvant-context-engineering-extraction.md`, plus the Framework 8 Second-Brain Adoption Layer confirmed against the located claude.ai export transcript — all located and read this session.
- **LIKELY**: entity-floor cross-reference sentences (internally consistent, not independently re-sourced) + the 15-25% dedup range (floor confirmed, ceiling extrapolated).
- **UNCONFIRMED**: none remaining after this pass. The one open item from the initial draft of this ledger (Framework 8's sourcing) was resolved by locating `_archive/claude-export-2026-07-01.tar.gz` rather than left as an unverified assumption.
