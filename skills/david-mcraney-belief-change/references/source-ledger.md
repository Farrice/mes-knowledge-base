# Source Ledger — David McRaney: Belief Change Architecture

Every claim added or touched during the Wave 3 Lane 4 repair pass, labeled VERIFIED / LIKELY / UNCONFIRMED. This ledger covers the repair delta only (genius.md additions + workflow Output Schema sections); it does not re-audit the skill's pre-existing content, which was already carrying its own attribution (Pattern/HK numbering, Empirical calibration note in Pattern 13).

## Primary Sources on Disk

| Source file | Size | What it is | Status |
|---|---|---|---|
| `references/spencer-greenberg-interview-notes.md` | 4,075 bytes | Extraction notes from Spencer Greenberg's "Clearer Thinking" podcast interview with David McRaney (dated 2026-03-31 in the file header — that is the extraction date, not the original air date, which is UNCONFIRMED) | VERIFIED (file exists, content read in full, quotes below are verbatim substrings) |
| `references/hidden-knowledge.md` | 9,033 bytes | 13 "Hidden Knowledge" tacit-insight items, cross-referenced into genius.md's Hidden Knowledge section | VERIFIED (file exists, content read in full) |
| `references/genius-patterns.md` | 18,215 bytes | Legacy standalone copy of Patterns 1-23 (pre-dates Patterns 24-26, which only exist in genius.md and the interview notes) | VERIFIED (file exists, content read; noted as the older/partial version — genius.md is the current merged file and the one the heartbeat auditor grades) |
| `references/prompts-v2/*.md` (14 files) | ~6-19 KB each | structure-pure-v2 execution prompts, already carrying Output Contract / Output Skeleton / Quality Gate | VERIFIED (pre-existing, unchanged by this repair) |
| `_active/harness/codex-harvest-2026-06-11/agents/david-mcraney/AGENT.md` | 89 lines | Parallel agent persona file (Codex harvest), independent corroboration of McRaney's core thesis and Voice & Style — not used as a primary source for repair content, consulted only for cross-check | VERIFIED (file exists, read in full) |

## Sources Searched and Confirmed Absent (not fabricated-absence — verified by direct search)

- `extractions/` (repo root): `ls extractions/ | grep -i mcraney` and a repo-wide `grep -ril "mcraney"` outside `skills/david-mcraney-belief-change/` returned no dedicated raw-transcript extraction folder for McRaney. The only per-expert artifact found was the codex-harvest `AGENT.md` above (a derivative persona file, not a raw transcript).
- `_active/harness/codex-harvest-2026-06-11/extractions/`: no McRaney-specific subfolder found via the same search.
- `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes): `tar -tzf ... | grep -i mcraney` against the full archive index (no extraction performed, per scratch-directory discipline) returned zero matching paths — confirmed absent, not unread.
- **Conclusion**: This skill's only primary-source artifact on disk is the Spencer Greenberg interview notes file plus the pre-existing genius-patterns.md/hidden-knowledge.md synthesis (itself derived from McRaney's book *How Minds Change* per SKILL.md's description line, which is UNCONFIRMED against a source file — no book excerpt exists in this repo).

## Claims Added in This Repair Pass (genius.md)

| Claim / addition | Label | Anchor |
|---|---|---|
| "The better your argument, the *more* the other person assimilates it into their existing framework without changing." | VERIFIED | Verbatim substring, `references/hidden-knowledge.md` #1 |
| "the hardest skill isn't what to say — it's learning when to stop talking." | VERIFIED | Verbatim substring, `references/hidden-knowledge.md` #6 |
| "how did you arrive at this?" activates metacognition vs. content questions triggering defense | VERIFIED | `references/spencer-greenberg-interview-notes.md`, item 3 ("Metacognition as Master Mechanism") |
| "Transparency fixes technique rebuttals but looks desperate on topic rebuttals. Evidence fixes topic rebuttals but confirms suspicion on technique rebuttals." | VERIFIED | Verbatim substring, `references/spencer-greenberg-interview-notes.md`, item 2 |
| "If you've hit 30% evidence and nothing's changing, STOP adding evidence. The barrier is social/identity cost, not information deficit." | VERIFIED | Verbatim substring, `references/spencer-greenberg-interview-notes.md`, "The 30% Tipping Point" item |
| "you can't remove a load-bearing belief without either replacing it with something equally strong or restructuring the entire system it supports." | VERIFIED | Verbatim substring, `references/hidden-knowledge.md` #7 |
| "Focus groups are especially bad — people perform for each other." | VERIFIED | Verbatim substring, `references/hidden-knowledge.md` #5 |
| Illustrative "Example" additions to 12 entity-floor sections (Patterns 1, 4, 12, 16, 24; Hidden Knowledge 2, 3, 5, 6, 7, 9, 10) — hypothetical scenarios, not attributed factual claims | N/A (craft illustration, not a sourced claim — same house style as existing Pattern 9's "$X in 3 months" and accommodation-audit.md's "$10-50K" examples) | Self-consistent with existing skill numbers (30%, 70-80% from Pattern 13's own Empirical Calibration note); no new external fact asserted |
| "How to Use This Skill (Model Calibration)" section — recognition-test framing, tell-class warnings | N/A (original craft-calibration prose, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per the batch envelope's instruction) | Not a factual claim requiring a source |

## Claims Added in This Repair Pass (workflow Output Schema sections)

All 10 new "## Output Schema" sections (accommodation-audit.md, belief-dissolution-copywriting.md, belief-layer-creative-brief.md, deep-canvassing-research-sprint.md, elm-content-strategy.md, metacognitive-thought-leadership.md, persuasion-engineered-copy-engine.md, resistance-matched-proof-rx.md, social-permission-campaign.md, threshold-optimized-campaign.md) are structural/process descriptions of that workflow's OWN pre-existing Output blocks and Quality Gate tables — not factual claims about the world. Label: **N/A (procedural, not factual)**. Each was written by re-reading the full file and describing only what its own Phase Output blocks already specify — no new mechanism invented.

## UNCONFIRMED Items (flagged honestly, not silently dropped)

- The original air date of the Spencer Greenberg × David McRaney "Clearer Thinking" interview — the notes file only records the 2026-03-31 extraction date, not the interview's original publish date. **UNCONFIRMED**, not asserted anywhere in the repair.
- SKILL.md's claim that the skill is "based on ... David McRaney's How Minds Change + Spencer Greenberg interview synthesis" — the book itself is not present as a source file in this repo; only the interview notes and the derived pattern/HK files exist. Book-attributed content (most of Patterns 1-23) is **LIKELY** (consistent with McRaney's publicly known thesis and cross-corroborated by the independent codex-harvest AGENT.md) rather than VERIFIED against a primary text file. This was pre-existing before the repair and is noted here for completeness, not re-labeled skill-wide (out of scope for this pass).
