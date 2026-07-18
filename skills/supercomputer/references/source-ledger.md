# Source Ledger — `skills/supercomputer/`

Every source consulted while repairing this skill's heartbeat checks (Wave 3, Lane 4, Batch 17),
labeled VERIFIED / LIKELY / UNCONFIRMED. `supercomputer` is a system skill (the mission
orchestrator), not a named-expert extraction — ground truth is its own workflow files,
orchestration directives, and production trace log, not an `extractions/` transcript. No file
matching `supercomputer` exists under `extractions/`; that absence was confirmed by directory
listing, not assumed.

## VERIFIED — read directly, content confirmed by this repair

| Claim / anchor used | Source | Confirmation |
|---|---|---|
| Anti-pattern quotes (Seedance/Kling substitution, `/parallax` composition rule, "each deliverable gets its own finalize call") | `skills/supercomputer/SKILL.md` (11,156 bytes) | Read in full; quotes matched verbatim against the file's "Anti-Patterns (will fail the mission)" section |
| Anchor-memory pattern, cost-preview trust mechanic, Higgsfield failure mode, Open Questions (incl. "Wave 2, 2026-07-09" anchor_verify.py note) | `skills/supercomputer/genius.md` (8,586 bytes, pre-repair) | Read in full; quoted passages copied verbatim into the new Anti-Patterns and Model Calibration sections |
| "Never silently re-route. Never silently skip. Always surface the choice." | `directives/supercomputer-mode.md` (9,703 bytes) | Read in full; quote matches line 173 of the halt-gate section verbatim |
| Four-phase runbook (Phase 0-4 protocol, exact-format MISSION PLAN/MISSION COMPLETE blocks) | `.agent/workflows/supercomputer.md` (11,037 bytes) | Read in full |
| Batch-finalize failure pattern — 5 separate `chain_runner.py finalize` calls one minute apart, Anchor-004 through Anchor-010, per-deliverable adversarial scores 7.0-8.0 | `evolution_store/v2_traces/trace_20260525_232154_supercomputer.json`, `..._232212_...`, `..._232219_...`, `..._232226_...` (Resonance launch mission, dated 2026-05-25) | All 4 files read in full; anchor ids and scores pulled directly from each trace's `notes` field |
| Retry-without-root-cause-fix pattern — `intent_alignment: 4.0` unchanged across a retry, notes = "Retry after intent-alignment receipt patch" | `evolution_store/v2_traces/trace_20260701_063818_supercomputer.json`, `trace_20260701_063839_supercomputer.json` (dated 2026-07-01, both `is_failure: true`) | Both files read in full; quote and score pulled directly from JSON fields |
| Smoke-test trace exists for anchor integration (2026-05-20) | `evolution_store/v2_traces/trace_20260520_213904_supercomputer.json` | Read in full; confirms production trace history predates the 2026-05-25 mission traces |
| Four born-v2 execution prompts already exist with Output Contract / Output Skeleton / Quality Gate sections | `skills/supercomputer/references/prompts-v2/mission-plan-kickoff.md`, `anchor-propagation-verification.md`, `mission-completion-summary.md`, `mission-pivot-replan.md` | All 4 read in full; new `workflows/*.md` files wrap these engines rather than duplicating their content |
| House style for a workflow file with `## Output Schema` + `## Quality Gate` wrapping a `references/prompts-v2/` engine file | `skills/forge-os/workflows/prompt-forge.md` | Read in full; used as the structural template (Invocation/Stages/Output Schema/Quality Gate) for the 4 new `workflows/*.md` files |
| Skill build/last-touch dates (2026-05-28 creation, 2026-07-09 and 2026-07-13 modifications) | `git log --follow` on `skills/supercomputer/SKILL.md`, `genius.md`, `directives/supercomputer-mode.md`, `.agent/workflows/supercomputer.md` | Commands run directly against repo history; commit hashes/dates recorded in `PROVENANCE.md` |
| `extractions/creative-direction/higgsfield_pipeline.md` exists and is non-empty (referenced in genius.md's Reading List as the "tool surface" source) | `extractions/creative-direction/higgsfield_pipeline.md` | Confirmed present, 4,286 bytes (`wc -c`), not read line-by-line for this repair since no new claim was drawn from its body |
| Heartbeat check logic (`anti_patterns_sourced`, `recognition_test`, `source_ledger`, `named_entity_floor`, `workflow_contracts` regexes) | `execution/skill_auditor.py` | Read in full; all new content was tested against the actual regex functions (`_anti_pattern_items`, `_HB_SOURCE_ATTR_RE`, `_HB_RECOG_RE`, `_sections_zero_entity`, `_HB_OUTPUT_SCHEMA_RE`, `_HB_QUALITY_GATE_RE`) before delivery, not guessed |

## LIKELY — plausible and internally consistent, not independently re-verified this session

| Claim | Why LIKELY not VERIFIED |
|---|---|
| Higgsfield's $99/mo Ultra pricing, credit-vs-USD billing model, and multi-clip Seedance audio-drift behavior (as described in `genius.md`, pre-existing content, unchanged by this repair) | These claims predate this repair — they were already in `genius.md` before Wave 3 touched the file and were not re-verified against Higgsfield's live product this session; carried forward unchanged as pre-existing skill content, not re-asserted as newly confirmed |
| Hermes Agent being MIT-licensed | Pre-existing `genius.md` claim, carried forward unchanged; not re-checked against the Hermes Agent repository license this session |

## UNCONFIRMED — named in the skill but not independently checked

| Claim | Source cited in skill | Status |
|---|---|---|
| "The Higgsfield Supercomputer demo video (May 19, 2026)" | `genius.md` Reading List | UNCONFIRMED — no web fetch was run to confirm the video's existence, date, or content this session; carried forward as pre-existing skill content, not a new claim introduced by this repair |
| "Hermes Agent technical review (tokenmix.ai)" | `genius.md` Reading List | UNCONFIRMED — external URL not fetched this session |
| "The Bad Decisions Studio critical review" (of Higgsfield, cited for the "$200/mo plan, two chats, 4% of budget burned" figure) | `genius.md` "Why Pre-Flight Cost Preview Is the Trust Mechanic" | UNCONFIRMED — external source not fetched this session; the specific figures ("$200/mo," "4% of budget") are quoted from pre-existing `genius.md` text, not independently re-sourced |

## Explicitly absent (checked, not assumed)

- No file under `extractions/` matches `supercomputer` (`ls extractions/ | grep -i supercomputer` returns nothing) — confirmed by directory listing, not by absence-of-search.
- No `_archive/claude-export-2026-07-01.tar.gz` scan was required: this skill is a system orchestrator with its own first-party ground truth (workflow files, directives, and a live production trace log with 9 real trace files), which fully satisfies the sourcing requirement without needing the archive fallback.
