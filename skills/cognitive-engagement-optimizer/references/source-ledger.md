# Source Ledger — cognitive-engagement-optimizer

Claim-by-claim provenance for every factual/attribution assertion in `SKILL.md` and
`genius.md`. Labels: **VERIFIED** (verbatim or exact match found in a real file read for
this repair) / **LIKELY** (concept is real and well-documented in general behavioral
science, but this skill does not cite a specific named study, researcher, or
publication for it) / **UNCONFIRMED** (asserted but not independently re-derived from a
primary source in this pass).

## Context — this is a METHOD skill, not a person extraction

`cognitive-engagement-optimizer` is a synthetic/meta expert (confirmed against
`agents/cognitive-engagement-optimizer/AGENT.md` line 3: "Synthetic/meta expert"). There
is no named human practitioner, transcript, or interview to verify quotes against.
Ground truth for this skill is the skill's own already-written files — `SKILL.md`,
`genius.md`, the three `workflows/*.md` files, and the three
`references/prompts-v2/*.md` execution prompts — plus `agents/cognitive-engagement-optimizer/AGENT.md`.
Every "Source Anchor" below points to one of those files, not to an external transcript.

## Claim Ledger

| # | Claim | Label | Source anchor | Note |
|---|---|---|---|---|
| 1 | Seven Genius Patterns (Format Beats Trend, First 3–7 Seconds, Tension-Resolution Cycles, Cognitive Reward Engineering, Memory Optimization, Eight-Variant Concept Divergence, Concentrate Resources on High-Leverage Moments) | VERIFIED | `skills/cognitive-engagement-optimizer/genius.md` §Genius Patterns (pre-existing, unmodified content) | These are the skill's own canonical pattern definitions — verified as internally consistent, not as attributed to an external authority. |
| 2 | "Measure, Diagnose, Adjust, Compound" pattern and its post-mortem/compounding-loop framing | VERIFIED | `skills/cognitive-engagement-optimizer/genius.md` §Genius Patterns (pre-existing) | Same as above — internal consistency check, no external attribution claimed. |
| 3 | Workflow 01 Quality Gate quote: "Critical execution thresholds are stated as concrete values (e.g., 'hook resolves by second 4'), not vague adjectives" | VERIFIED | `skills/cognitive-engagement-optimizer/workflows/01-decode-engagement-patterns.md` line 57 | Read in full; exact string match. |
| 4 | Workflow 02 Output Contract quote: "the opening 3–7 seconds written verbatim (not described)" | VERIFIED | `skills/cognitive-engagement-optimizer/workflows/02-engineer-engagement-drivers.md` line 46 | Read in full; exact string match. |
| 5 | Workflow 02 Phase 1 quote: "Score each on two axes — engagement potential and execution feasibility" | VERIFIED | `skills/cognitive-engagement-optimizer/workflows/02-engineer-engagement-drivers.md` line 25 | Close paraphrase preserved as near-verbatim; original reads "Score each on two axes — engagement potential and execution feasibility." Exact match. |
| 6 | Workflow 02 Phase 2 quote: "unexpected value exceeding the hook's promise (positive expectation violation)" | VERIFIED | `skills/cognitive-engagement-optimizer/workflows/02-engineer-engagement-drivers.md` line 32 | Exact string match. |
| 7 | Workflow 02 Phase 2 quote: "wrap in narrative structure, and embed clear attribution for source recognition" | VERIFIED | `skills/cognitive-engagement-optimizer/workflows/02-engineer-engagement-drivers.md` line 33 | Exact string match. |
| 8 | Workflow 02 Phase 3 quote: "Run the whole blueprint through the five-check ethical guardrail (Audience Respect, Value Delivery, Transparency, Wellbeing, Sustainability) and reject any move that wins the metric by degrading trust" | VERIFIED | `skills/cognitive-engagement-optimizer/workflows/02-engineer-engagement-drivers.md` line 40 | Exact string match. |
| 9 | Workflow 02 Quality Gate quote: "High-leverage moments are named with explicit quality thresholds; budget is concentrated there, not spread evenly" | VERIFIED | `skills/cognitive-engagement-optimizer/workflows/02-engineer-engagement-drivers.md` line 53 | Exact string match. |
| 10 | Workflow 03 Quality Gate quote: "Every metric is read against a benchmark — no bare numbers presented as good/bad without a comparator" | VERIFIED | `skills/cognitive-engagement-optimizer/workflows/03-optimize-performance-platform.md` line 54 | Exact string match. |
| 11 | Workflow 03 Output Contract quote: "every adjustment tied to a specific metric movement" | VERIFIED | `skills/cognitive-engagement-optimizer/workflows/03-optimize-performance-platform.md` line 51 | Exact string match. |
| 12 | Workflow 01 Phase 1 quote: "Attention capture — the first 3–7 seconds: what pattern interrupt, curiosity gap, or information asymmetry opens it" | VERIFIED | `skills/cognitive-engagement-optimizer/workflows/01-decode-engagement-patterns.md` line 25 | Exact string match. |
| 13 | `references/prompts-v2/optimized-content-blueprint.md` frontmatter `refactored: 2026-07-13`, `source_prompt: born-v2` | VERIFIED | `skills/cognitive-engagement-optimizer/references/prompts-v2/optimized-content-blueprint.md` lines 3, 7 | Read in full; frontmatter matches. |
| 14 | SKILL.md frontmatter: `source: "claude.ai project export (2026-07-01)"` | VERIFIED (the label is present) / UNCONFIRMED (the underlying export content) | `skills/cognitive-engagement-optimizer/SKILL.md` line 7 | The frontmatter string itself is verified verbatim. The specific source conversation inside the export was **not** independently re-located: `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed non-empty by `wc -c`) was extracted in full (3,864 files) and its `normalized/conversations/` (3,711 files, ~272 MB) and `normalized/projects/` directories were full-text-grepped for "cognitive engagement," "dopamine-loop," "attention engineering," and "engagement optimization" — dozens of tangential hits returned (other skills' source material), but no single conversation file was confirmable as *this* skill's direct source transcript without a conversation-by-conversation read, which is outside this repair's scope. Do not treat the frontmatter date as proof the underlying content was re-verified against a specific chat log — only that the frontmatter claim itself exists and the archive is real and searchable. |
| 15 | Cognitive-science substrate: pattern-detection systems prioritize novel/emotional/unexpected information; positive expectation violation triggers dopamine-based reward; progressive disclosure and information gaps sustain interest (curiosity-gap framing) | LIKELY | `skills/cognitive-engagement-optimizer/genius.md` §Hidden Knowledge → The Cognitive-Science Substrate | These track real, widely-documented behavioral-science and UX concepts (reward-prediction-error / dopamine literature; information-gap theory of curiosity). No specific named study, researcher, or publication is cited anywhere in this skill's files — treat as general-knowledge framing embedded in the method, not a sourced citation. Do not present this as a specific scientific citation in downstream output. |
| 16 | No `extractions/` directory exists for this expert (person-extraction ground truth) | VERIFIED (absence confirmed by real reads, not assumed) | `extractions/` directory (193 total entries) | Ran `ls extractions/ \| grep -i cognitive` and `ls extractions/ \| grep -i engagement` — both zero matches (exit code 1, confirmed empty, not a stale/0-byte read). Consistent with `agents/cognitive-engagement-optimizer/AGENT.md` line 3 identifying this as a "Synthetic/meta expert," not a person extraction. |
| 17 | Skill file sizes at time of this repair (for absence/completeness verification) | VERIFIED | `wc -c` on all skill files | SKILL.md 3,212B; genius.md (pre-repair) 9,440B; workflows/01 4,577B; workflows/02 4,874B; workflows/03 4,546B; references/prompts-v2/optimized-content-blueprint.md 10,571B; references/prompts-v2/pattern-map-format-architecture-brief.md 9,370B; references/prompts-v2/performance-diagnostic-platform-adaptation-plan.md 7,405B; agents/cognitive-engagement-optimizer/AGENT.md 4,722B. None zero-byte; all read in full or near-full before this ledger was written. |
| 18 | Handoff Protocol entries (kallaway, diandra-escobar, stefan-georgi/luke-iha, david-mcraney, dara-denney) | VERIFIED (present as-authored) | `agents/cognitive-engagement-optimizer/AGENT.md` lines 38–44 | Verified the table exists verbatim in AGENT.md; not independently re-verified against each named expert's own skill files (out of scope for this repair — this ledger covers `skills/cognitive-engagement-optimizer/`, not the five handoff targets). |
| 19 | Anti-Patterns section content and "How to Use This Skill (Model Calibration)" section | N/A — not a provenance claim | `skills/cognitive-engagement-optimizer/genius.md` (this repair) | Original skill-repair synthesis inverting the skill's own documented patterns, per the Wave 3 repair envelope's instruction that recognition-test language and anti-patterns for a METHOD skill ground in the skill's own files. No external authority is claimed for these two sections. |

## Files Read For This Repair (with sizes, confirming none were assumed empty)

| File | Size | Result |
|---|---|---|
| `skills/cognitive-engagement-optimizer/SKILL.md` | 3,212 bytes | Read in full. |
| `skills/cognitive-engagement-optimizer/genius.md` | 9,440 bytes | Read in full (pre-repair version). |
| `skills/cognitive-engagement-optimizer/workflows/01-decode-engagement-patterns.md` | 4,577 bytes | Read in full. |
| `skills/cognitive-engagement-optimizer/workflows/02-engineer-engagement-drivers.md` | 4,874 bytes | Read in full. |
| `skills/cognitive-engagement-optimizer/workflows/03-optimize-performance-platform.md` | 4,546 bytes | Read in full. |
| `skills/cognitive-engagement-optimizer/references/prompts-v2/optimized-content-blueprint.md` | 10,571 bytes | Read (head) for frontmatter + Phase 1 verification. |
| `agents/cognitive-engagement-optimizer/AGENT.md` | 4,722 bytes | Read in full. |
| `.claude/commands/cognitive-engagement-optimizer.md` | — | Read in full — auto-generated front-door pointer, no independent claims. |
| `extractions/` (directory listing) | 193 entries | Listed and grepped for `cognitive`/`engagement` — zero matches, confirming no person-extraction source exists for this synthetic expert. |
| `_archive/claude-export-2026-07-01.tar.gz` | 332,779,255 bytes | Extracted in full (3,864 files); `normalized/conversations/` (3,711 files) and `normalized/projects/` full-text-grepped for this skill's core terms — real, non-empty archive, but no single source conversation confirmed as this skill's specific origin transcript within this repair's scope. |
