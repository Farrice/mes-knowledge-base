---
name: "Nate B. Jones — Context Bloat Diagnostic"
source_prompt: born-v2
skill: nate-b-jones-context-engineering
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Nate B. Jones's context bloat diagnostic: a systematic audit of context usage across an agentic system, treating the context window as a KV cache where every byte must earn its place. This is not a vibes-based "the prompt feels long" review — it is a measured audit that produces a full bloat map with compression prescriptions ranked by impact. The frame: memory efficiency is a software problem, not a hardware problem — compression moves at the speed of software (months), hardware at the speed of physics (5+ years to build a new fab line). Bias toward measuring and fixing the system today rather than waiting for larger context windows.

## Input Required

- **[TARGET SYSTEM]** — the agentic system under audit (repo path, prompt/instruction files, skill files, agent configs)
- **[TOOL DEFINITIONS]** — list of all tool/MCP schemas loaded per invocation
- **[TASK SAMPLE]** — 5-10 representative task interactions run against the system
- **[TOKEN COUNTING METHOD]** — actual tokenizer if available, else byte-count approximation (`wc -c`)
- **[ACCESS SCOPE]** — which files/directories the auditor can read (system instructions, skill context, tool schemas, conversation logs)

## Execution Protocol

Run all six steps in order. Do not skip Step 4 (lost-in-the-middle) even if time-pressured — it is the check most likely to surface silent failures.

**Step 1 — Measure Total Context Footprint.** For each of the five components below, count tokens and compute percentage of total:
1. System instructions (root rules, guardrails)
2. Skill context (SKILL.md, genius.md, workflows loaded)
3. Tool definitions (all available tool schemas)
4. Conversation history (prior turns, summaries, state)
5. Dynamic context (search results, file contents, retrieval)

**Step 2 — Map Duplication.** Search for instructions/rules appearing in multiple locations (system prompt AND skill files; same guardrail in multiple agent profiles; tool descriptions repeated in schemas AND prose). Classify each hit:
- Exact duplicate → remove entirely from one location
- Near duplicate → merge into a single authoritative statement
- Contextual variant → keep both only if context genuinely differs

**Step 3 — Attention Value Scoring.** For each loaded section, score attention value 1-5:
- High (4-5): directly referenced in agent outputs, critical guardrails that prevent failures
- Medium (3): referenced sometimes, useful but not essential framing
- Low (1-2): rarely/never influences outputs, decorative formatting, verbose examples
Sections scoring ≤2 are compression candidates.

**Step 4 — "Lost in the Middle" Check.** Place a distinctive, novel instruction at three positions in the system's current context: top (first 10%), middle (40-60%), bottom (last 10%). Run identical tasks against each and check compliance with the positioned instruction. If middle placement shows materially lower compliance than top/bottom, flag the system as having a lost-in-the-middle vulnerability and prescribe relocating critical instructions to top or bottom.

**Step 5 — Produce Diagnostic Report.** For every audited component, assign one compression action pulled from the five vectors (quantization/dedup, eviction/sparsity, architectural redesign/format, offloading/tiering, attention placement) with an expected savings estimate.

**Step 6 — Prioritize by Impact.** Rank all prescriptions by (expected token savings × ease of implementation). Highest impact + lowest effort first. Group by compression vector. Produce a prioritized sprint backlog that feeds directly into a Context Compression Sprint.

## Output Contract

Deliver a single diagnostic artifact containing, in order:
1. Executive summary — total tokens measured, biggest offenders (top 3), overall health score 1-10 with one-sentence justification
2. Component-by-component breakdown table (5 rows: system instructions, skill context, tool definitions, conversation, dynamic context — tokens + % of total)
3. Duplication map (each duplicate found, classification, merge prescription)
4. Attention value scores (per section, 1-5, with the ≤2 sections flagged)
5. Lost-in-the-middle test results (pass/fail per position, compliance rates)
6. Prioritized compression sprint backlog (ranked list, each item tagged with its compression vector)
7. Expected total reduction estimate (tokens saved, % reduction)
Length: as long as the audit requires — do not pad; do not omit a section for brevity if data exists for it.

## Output Skeleton

```
# Context Bloat Diagnostic — [TARGET SYSTEM]

## Executive Summary
Total context measured: [N] tokens
Health score: [1-10] — [one-sentence justification]
Biggest offenders: [component], [component], [component]

## Component Breakdown
| Component | Tokens | % of Total |
|---|---|---|
| System instructions | [n] | [pct] |
| Skill context | [n] | [pct] |
| Tool definitions | [n] | [pct] |
| Conversation history | [n] | [pct] |
| Dynamic context | [n] | [pct] |
| TOTAL | [n] | 100% |

## Duplication Map
| Location A | Location B | Classification | Prescription |
|---|---|---|---|
| [file:section] | [file:section] | [exact/near/contextual] | [action] |

## Attention Value Scores
| Section | Score (1-5) | Basis for score | Compression candidate? |
|---|---|---|---|

## Lost-in-the-Middle Results
| Position | Instruction | Compliance | Verdict |
|---|---|---|---|
| Top | [instruction] | [pct/pass-fail] | |
| Middle | [instruction] | [pct/pass-fail] | |
| Bottom | [instruction] | [pct/pass-fail] | |

## Prioritized Compression Sprint Backlog
1. [prescription] — Vector: [quantization/eviction/architecture/tiering/attention] — Expected savings: [tokens/pct] — Effort: [low/med/high]
2. ...

## Expected Total Reduction
[N] tokens saved ([pct]% reduction) if all prescriptions executed.
```

## Quality Gate

- [ ] All five components in Step 1 are measured with real numbers, not estimates presented as measurements
- [ ] Every duplication claim in the map cites the actual two locations, not a generic "duplication exists"
- [ ] The lost-in-the-middle check was actually run (or explicitly marked as not run and why) — never fabricated compliance rates
- [ ] Every backlog item names its compression vector (one of the five) and is not a vague "clean this up"
- [ ] Health score in the executive summary is justified by the data in the breakdown, not asserted independently

## Deploy When

- System hitting context window limits or showing "lost in the middle" failures
- Token costs scaling faster than value delivered
- Before a Context Compression Sprint (this diagnostic is its Step 0 input)
- Periodic health check on a system that's accumulated skill/agent files over time
