# Source Ledger — nate-b-jones-trust-architecture

Claim-by-claim audit. Every source below was opened and read (not assumed) during this repair pass — see PROVENANCE.md for exact file+location anchors and REPAIR-NOTES.md for what a full-repo search covered before any UNCONFIRMED label was assigned.

## Sources Consulted

| # | Source | Type | Size | Verdict |
|---|--------|------|------|---------|
| 1 | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/0ee5fc4c-9a58-447a-9a1e-b93f6d2c8aaf.md` | claude.ai conversation export, title "[Ai Prompt Engineer 09/24/25]-Nate B Jones: I've Built Over 100 AI Agents: Only 1% of Builders Know These 6 Principles" (created 2025-09-23), contains full pasted YouTube transcript of the underlying video (youtube.com/watch?v=kWeLc-Dda94) | 34,337 bytes | **VERIFIED** — primary source for genius.md Patterns 5-8 + Hidden Knowledge Addendum + all 7 new Anti-Patterns items |
| 2 | `extractions/nate-b-jones/karpathy-loop-mes-extraction.md` (line 149, "Metric Gaming") | Prior MES 3.0 extraction, same expert, different video ("The Karpathy Loop") | 25,368 bytes | **VERIFIED** — one direct quote reused (fraud-model example) |
| 3 | `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md` | Prior extraction, "Smoothing the Jagged Frontier" video | 16,368 bytes | Read in full; no trust-architecture-specific content found (orchestration/DPVI domain, not zero-trust) — not cited |
| 4 | `extractions/nate-b-jones/turbokvant-context-engineering-extraction.md` | Prior extraction, "TurboQuant" video | 19,104 bytes | Read in full; memory-compression domain, not trust — not cited |
| 5 | `extractions/nate-b-jones/transcript.txt` | Raw transcript | 30,609 bytes | Read in full (preview + grep); confirmed this is the Karpathy-loop video transcript, not a trust-architecture source — not cited |
| 6 | `skills/nate-b-jones-trust-architecture/references/{genius-patterns,hidden-knowledge,implementation}.md` | Skill's own pre-existing reference files | 2,480 / 1,365 / 2,211 bytes | Read in full — duplicate of genius.md Patterns 1-4 + Hidden Knowledge, carry no source anchors of their own |
| 7 | `_archive/nate-b-jones-trust-architecture.skill` (zip) | Older archived skill snapshot | 13,253 bytes | Read via `zipfile` listing; contents match current references/ exactly — no additional provenance recovered |
| 8 | `_active/claude-export/harvest/*.json` (census/plan files) | Harvest metadata | — | Grepped for "nate b jones" / "trust architecture" — 4 filename hits, all generic census/plan JSON with no conversation content — not a content source |
| 9 | Full-archive scan: `_archive/claude-export-2026-07-01.tar.gz`, `claude-export/normalized/conversations/` (3,711 files) | Python `tarfile` streaming scan (`r|gz`, single sequential pass) for exact phrases: "deterministic bridges", "probabilistic core", "Vigilance Fallacy", "Insider Personnel Threat", "Subtle-Failure", "Graduated Health State", "Capability-Based Routing", "Reality Anchor", "Safe Word" | 332,779,255 bytes compressed archive; 3,711 conversation files scanned | Only "deterministic bridges" / "probabilistic core" hit a genuine Nate B Jones source (item #1 above). "Reality Anchor" hit 5 unrelated conversations (prompt-engineering, solopreneur coaching, Lulu Cheng Meservey — none Nate B Jones). "Vigilance Fallacy", "Insider Personnel Threat", "Subtle-Failure" (as a compound), "Graduated Health State", "Capability-Based Routing", "Safe Word" returned **zero hits anywhere in the 3,711-file corpus**. |

## Claim-by-Claim Labels

### genius.md — Patterns 1-4 (Structural vs. Behavioral Trust Shift, Contextual Scaling of Trust Failure, Vigilance Fallacy Mitigation, Anti-Sycophancy Architecture)
**UNCONFIRMED.** These are pre-existing skill content (predates this repair). No matching primary-source file or transcript was located in `extractions/nate-b-jones/`, the claude-export archive (full 3,711-file scan, see row 9), or the archived `.skill` zip. The terminology ("Insider Personnel Threat," "Vigilance Fallacy," "Anti-Sycophancy Architecture") does not appear verbatim anywhere in the searched corpus. Preserved per the additive-first boundary (not deleted), but they carry no verified anchor — do not present as direct Nate B Jones quotes.

### genius.md — Hidden Knowledge (Infrastructure Delusion, Open-Source Vulnerability, Cognitive Interface)
**UNCONFIRMED** for the same reason as above, with one exception: the illustrative "fraud model scores great in tests but misses real fraud" sentence added to Infrastructure Delusion during this repair is **VERIFIED** against source #2 (line 149).

### genius.md — Hall of Fame Exemplars (Financial Agent, Research Agent, Anti-Exemplar)
**UNCONFIRMED.** Illustrative composite scenarios, not traced to a transcript. No source anchor existed before this repair and none was found; labeling here rather than silently upgrading them.

### genius.md — Patterns 5-8 (Deterministic Bridges, Subtle-Failure World, Graduated Health States, Continuous Conversation-State Validation) + Hidden Knowledge Addendum (Capability-Based Routing, Stateful Intelligence)
**VERIFIED** against source #1. Every quoted fragment ("We have to engineer deterministic bridges on top of probabilistic cores," "still functional but be completely wrong," "there was a checkpoint there and it worked," "hundreds of multiples of different computes," "maybe 50 shades of gray," "those disappear on a restart," "AI behavior depends on accumulated context") was checked verbatim against the transcript text in source #1. Two are near-verbatim compressions rather than exact substrings — noted below, not upgraded past what the text supports:
- "still functional but be completely wrong" — transcript reads "It can still be functional but be completely wrong" (4:36-4:38). Genius.md's inline use drops the leading "It can" — meaning preserved, wording compressed. Treat as VERIFIED-paraphrase, not exact quote.
- All other quotes above are exact substring matches of the transcript.

### genius.md — Anti-Patterns (new section, this repair)
All 7 items **VERIFIED**. Six cite source #1 with timestamp anchors; the seventh ("Metric-gaming an agent's proxy objective") cites source #2 line 149, quoted verbatim: "Fraud model scores great in tests but misses real fraud."

### genius.md — How to Use This Skill (Model Calibration) (new section, this repair)
Craft guidance authored for this repair, calibrated to the verified register found in source #1 (declarative, mechanism-naming sentences, no metaphor stacking). Not a claim about Nate B Jones's exact words — a stylistic instruction grounded in his verified transcript register.

### workflows/*.md — Output Contract / Quality Gate sections
Structural scaffolding authored by the skill's original builder (born-v2 era), not sourced content — no verification claim applies.

## Labeling Key
- **VERIFIED** — quote or claim checked against a primary source file opened during this repair, exact or near-exact match.
- **LIKELY** — not used in this ledger; no claim met the bar for LIKELY without also meeting VERIFIED or falling to UNCONFIRMED.
- **UNCONFIRMED** — no primary source located despite genuine search (file reads + full-archive scan); preserved as pre-existing content per additive-first boundary, flagged so it is never mistaken for a verified Nate B Jones quote.
