# Provenance — `skills/supercomputer/` repair (Wave 3, Lane 4, Batch 17)

Anchor → source file + location table. Every quote/date/figure used in the repaired
`genius.md` and the new `workflows/*.md` files traces to one of these.

| Anchor used in repair | Source file | Location / commit |
|---|---|---|
| "If the user approved Seedance and you'd prefer Kling, ASK — don't substitute." | `skills/supercomputer/SKILL.md` | "Anti-Patterns (will fail the mission)" section, item 5 |
| "If `/parallax` exists, you compose it; you don't rewrite its logic inside the supercomputer workflow." | `skills/supercomputer/SKILL.md` | "Anti-Patterns (will fail the mission)" section, item 3 |
| "Each deliverable gets its own `chain_runner.py finalize` call. No exceptions." | `skills/supercomputer/SKILL.md` | "Anti-Patterns (will fail the mission)" section, item 4 |
| SKILL.md build/last-touch dates: created 2026-05-28, modified 2026-07-09, 2026-07-13 | git history | `git log --follow -- skills/supercomputer/SKILL.md`: commits `49141b746` (2026-05-28), `e2fe22d4b` (2026-07-09), `de9bac803` (2026-07-13) |
| "Our cost gate shows USD. That alone is a moat." | `skills/supercomputer/genius.md` (pre-repair) | "Why 'Pre-Flight Cost Preview' Is the Trust Mechanic" section |
| "grep-detects anchor key-term coverage in dependent deliverables and scores propagation 1-10" + "Wave 2, 2026-07-09" | `skills/supercomputer/genius.md` (pre-repair) | "The Open Questions" section, item 2 |
| genius.md build/last-touch dates: created 2026-05-28, modified 2026-07-09 | git history | `git log --follow -- skills/supercomputer/genius.md`: commits `49141b746` (2026-05-28), `e2fe22d4b` (2026-07-09) |
| "Never silently re-route. Never silently skip. Always surface the choice." | `directives/supercomputer-mode.md` | "Halt gate (cost_gate.py exit 1)" section, single line (line 173 as read) |
| directive build date: 2026-05-28 | git history | `git log --follow -- directives/supercomputer-mode.md`: commit `49141b746` |
| Batch-finalize evidence — Anchor-004 through Anchor-010, 5 separate `chain_runner.py finalize` calls, adversarial scores 7.0-8.0, dated 2026-05-25 23:21:54–23:22:26 | `evolution_store/v2_traces/trace_20260525_232154_supercomputer.json`, `trace_20260525_232212_supercomputer.json`, `trace_20260525_232219_supercomputer.json`, `trace_20260525_232226_supercomputer.json` | `notes` field of each JSON file (Resonance launch mission); `timestamp` field for the exact minute-apart cadence |
| Retry-without-fix evidence — `intent_alignment: 4.0` unchanged, notes "Retry after intent-alignment receipt patch", both `is_failure: true` | `evolution_store/v2_traces/trace_20260701_063818_supercomputer.json`, `trace_20260701_063839_supercomputer.json` | `quality.intent_alignment` and `notes` fields of each JSON file, dated 2026-07-01 |
| Earliest supercomputer production trace, confirms trace history predates the Resonance mission | `evolution_store/v2_traces/trace_20260520_213904_supercomputer.json` | `timestamp` field: 2026-05-20T21:39:04 |
| 4 born-v2 execution prompts already exist and carry Output Contract / Output Skeleton / Quality Gate | `skills/supercomputer/references/prompts-v2/mission-plan-kickoff.md`, `anchor-propagation-verification.md`, `mission-completion-summary.md`, `mission-pivot-replan.md` | Full file reads; used as the content engine each new `workflows/*.md` wraps (per each workflow's own "Dispatches..." line) |
| House style for a workflow file wrapping a `references/prompts-v2/` engine (Invocation / Stages / Output Schema / Quality Gate headings) | `skills/forge-os/workflows/prompt-forge.md` | Full file read; structural template for the 4 new workflow files |
| `extractions/creative-direction/higgsfield_pipeline.md` exists, 4,286 bytes | `extractions/creative-direction/higgsfield_pipeline.md` | `wc -c` output: 4286; confirms genius.md's pre-existing Reading List reference is not a dead pointer |
| No `extractions/` directory matches "supercomputer" | `extractions/` directory listing | `ls extractions/ | grep -i supercomputer` → empty; confirms this is a system skill with no named-expert transcript, per the Envelope's own framing |
| Heartbeat check regex behavior (anti_patterns_sourced, recognition_test, source_ledger, named_entity_floor, workflow_contracts) | `execution/skill_auditor.py` | Functions `_anti_pattern_items`, `_HB_SOURCE_ATTR_RE`, `_HB_RECOG_RE`, `_sections_zero_entity`, `_HB_OUTPUT_SCHEMA_RE`, `_HB_QUALITY_GATE_RE`; all new content was run against these functions directly (see repair verification below) before delivery |

## Repair verification (self-check, run against the actual auditor code)

Ran `execution/skill_auditor.py`'s own `heartbeat_checks()` function against a staged copy of the
repaired skill (`genius.md` + new `workflows/*.md` + new `references/source-ledger.md` layered
onto the existing `skills/supercomputer/` tree). Result: 6/6 PASS —
`anti_patterns_sourced` (6 sourced items, need ≥5), `verbatim_exemplars` (13, need ≥3, was
already passing), `recognition_test` (found "recognize this as"), `source_ledger` (found
`source-ledger.md`), `named_entity_floor` (11 sections, 0.00 zero-entity ratio, was already
passing), `workflow_contracts` (all 4 new workflow files carry Output Schema + Quality Gate).
