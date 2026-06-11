# Gemini Truncation Fix — Execution

## Phase 0: Safety
- [x] Snapshot AGENTS.md, GEMINI.md, token-efficiency-protocol.md → `.tmp/gemini-fix-backup/`

## Phase 1: Workflow Description Trim
- [x] Ran inline Python to trim 122 workflow descriptions to ≤8 words
- [x] Verified: 0 descriptions over 8 words

## Phase 2: AGENTS.md Diet
- [x] Removed "When Steps Narrow" table → replaced with 8 bullet points
- [x] Removed "Chain Efficiency Rules" section → merged into Chain Narrowing Rules  
- [x] Removed full Directive Index (7 sub-tables, 30+ entries) → 3-line compact reference
- [x] Result: 15,490 → 10,187 chars (-34%)

## Phase 3: GEMINI.md Consolidation
- [x] Stripped Architecture, Chain steps 1-6, Environment, Artifact-First (all in AGENTS.md)
- [x] Kept: Zero-Crash Law + AI Slop list + Deep Alignment Protocol
- [x] Result: 5,350 → 1,121 chars (-79%)

## Phase 4: Token Efficiency Protocol Update
- [x] Added Rule 7: System Prompt Hygiene (limits, audit command, rationale)

## Phase 5: Verification
- [x] AGENTS.md: 15,490 → 10,187 chars
- [x] GEMINI.md: 5,350 → 1,121 chars
- [x] Total saved: 7,817 chars (~1,954 tokens)
- [x] All workflow descriptions ≤ 8 words ✅
- [x] Backups at `.tmp/gemini-fix-backup/`
