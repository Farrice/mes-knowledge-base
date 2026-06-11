# Kieran Flanagan AI Content Team — Full Extraction Pipeline

> **Architecture**: 3-skill hybrid (approved) — audience-intelligence / content-engine / content-ops
> **Future**: Note to audit other agents for skill-splitting when context bloat causes performance issues (separate session)

## Phase 1: Planning
- [x] Fetch transcript via `fetch-transcript.py`
- [x] Run Perplexity deep research on content teams, bundling, audience profiling
- [x] Read existing workflows for overlap analysis
- [x] Read extraction protocol (MES 3.0, `/extract`, `/create-agent`)
- [x] Write implementation plan
- [x] Architecture analysis — single vs multi-skill → 3-skill hybrid approved
- [x] User reviews and approves implementation plan

## Phase 2: Extraction Report
- [x] Produce MES 3.0 extraction report (Deep tier)
- [x] 8 Genius patterns + 6 Hidden knowledge items + Applied Intelligence
- [x] Save to `extractions/kieran-flanagan/extraction-report.md`

## Phase 3: Skill 1 — `kieran-flanagan-audience-intelligence`
- [x] SKILL.md + genius.md
- [x] `/content-audience-profile` workflow
- [x] `/content-style-card` workflow
- [x] `/style-from-creator` workflow
- [x] `/content-cluster` workflow

## Phase 4: Skill 2 — `kieran-flanagan-content-engine`
- [x] SKILL.md + genius.md
- [x] `/talking-points` workflow
- [x] `/lookalike-content` workflow
- [x] `/content-enrich` workflow
- [x] `/content-bundle` workflow
- [x] `/platform-adapt` workflow
- [x] `/content-series-plan` workflow
- [x] `/hook-formula-extract` workflow
- [x] `/competitor-content-spy` workflow

## Phase 5: Skill 3 — `kieran-flanagan-content-ops`
- [x] SKILL.md + genius.md
- [x] `/content-orchestrate` workflow
- [x] `/content-feedback` workflow
- [x] `/content-review-cycle` workflow

## Phase 6: Agent + Registry
- [x] Create `agents/kieran-flanagan/AGENT.md`
- [x] Create `agents/kieran-flanagan/memory/context.md`
- [x] Register in `AGENT_INDEX.md` and `SKILL_INDEX.md` (via sync_registries.py)
- [x] Add invocation cards
- [x] Create 15 workflow command files in `.agent/workflows/`

## Phase 7: Verification
- [x] Verify all files created and properly linked
- [x] Confirm no overlap/conflict with existing workflows
- [x] Write walkthrough
