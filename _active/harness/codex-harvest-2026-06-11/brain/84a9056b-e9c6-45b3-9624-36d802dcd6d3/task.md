# MES 3.0 Savant-Level Extraction Upgrade

## Phase 1: Upgrade MES 3.0 Extract Directive
- [x] Add Layer 6 (Exemplar & Move Mining) to 5-Layer Analysis
- [x] Add Hall of Fame Exemplars section to extraction report template
- [x] Add Signature Moves section to extraction report template
- [x] Add Expert-Specific Quality Rubric section to extraction report template

## Phase 2: Upgrade Extract and Convert Workflows
- [x] Update `extract.md` Step 2 to reference new components
- [x] Update `extract.md` Step 4 checkpoint to include exemplar/move/rubric counts
- [x] Update `extract.md` Step 5b genius.md creation to list new sections
- [x] Update `convert-extraction.md` Step 1 audit to include new components
- [x] Update `convert-extraction.md` Step 3 genius.md template with new sections

## Phase 3: Upgrade skill_converter.py Merge Function
- [x] Update `merge_genius_file()` to read exemplars, signature-moves, quality-rubric reference files
- [x] Verify: syntax check passed (`ast.parse` clean)
- [x] Verify: `load_skill()` on kallaway-word-mastery — loads correctly, new fields default to empty
- [x] Verify: `load_skill()` + `merge_genius_file()` on eric-roth — existing merge works perfectly (14 GP + 10 HK preserved), new fields correctly empty

## Phase 4: Build genius_enricher.py + Run Enrichment
- [x] Create the enrichment script (`execution/genius_enricher.py`, ~340 lines)
- [x] Verify: syntax check passed
- [x] Verify: `--plan-only` discovered 148 skills, all need enrichment, all have DF/AP/VD cleanup targets
- [x] Verify: `--dry-run` on eric-roth — API call succeeded
- [x] Run full enrichment on all 148 skills
- [x] Spot-checked results — quality verified
- [x] Committed and pushed: `d2688cf2`

## Phase 5: Agent Cleanup + Cross-Reference Upgrade
- [x] Audit: 107 agents, 84 had DF, 9 had AP, 0 had savant sections
- [x] Build `execution/agent_upgrader.py`
- [x] Plan-only audit: 81 need cleanup, 104 need cross-refs
- [x] Single-agent test (eric-roth) — verified diff correct
- [x] Run full `--all` upgrade: 105 upgraded, 2 already clean
- [x] Fix `directives/agent-loading-protocol.md`: 4 references updated `genius-patterns.md` → `genius.md`
- [x] Re-audit: 107/107 clean (4 DF + 5 AP survivors confirmed as custom content)
- [x] Commit and push
