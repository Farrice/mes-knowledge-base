# Wave 2: Single-Source Constitutions — Design Review

## Overview
Extend `platform_compiler.py` from read-only drift detection (v1) to single-source generation (v2): extract shared blocks into `directives/constitution-core/*.md`, inject via `<!-- BEGIN:block --> ... <!-- END:block -->` markers, respect platform-specific constraints (CONSTRAINTS_LAST, CANARIES, size limits).

---

## Shared Blocks (Ready for Extraction)

These sections appear in **all three platform constitutions** (CLAUDE.md, GEMINI.md, AGENTS.md) with identical or near-identical content. Extracting them eliminates manual sync.

### Block 1: `CRITICAL-OVERRIDE-RULES` 
**Current state:** Hand-synced across 3 files with drift observed
**Content to extract:**
```
After context compaction, read `.agent/session-state.md` immediately before continuing.
Real tools only — no phantom research, no confident hallucination. Uncertain? Say "I don't know."
Weekly ritual (`/weekly-closeout`, ~20 min): drain revenue tracker, check calibration, clear evolution queue, monthly CORE DRIFT scan.
```
**Appears in:** CLAUDE.md (added Wave 1), GEMINI.md has partial, AGENTS.md has partial
**Placement rule:** Must sit in final third (CONSTRAINTS_MIN_OFFSET=0.60) for Gemini/Agents (CONSTRAINTS_LAST list). Mark with `## CRITICAL` to detect positioning.
**File:** `directives/constitution-core/critical-override.md`

### Block 2: `GOLDEN-RULE`
**Current state:** Identical in all three constitutions
**Content:**
```
⚠️ GOLDEN RULE — ONE TOOL PER WORKING TREE AT A TIME.
This repo is shared by Claude Code and OpenAI Codex with no lock between them.
Never run both against this directory at the same time — concurrent edits corrupt the tree.
Safe handoff: let the active tool finish to a clean `git status` or a commit, then open the other.
Need both at once? Give one its own `git worktree` — never a second driver in this folder.
```
**Appears in:** CLAUDE.md (line 3), GEMINI.md (implicit), AGENTS.md (line 4-5)
**Placement rule:** Early in document (before "What this workspace is" sections)
**File:** `directives/constitution-core/golden-rule.md`

### Block 3: `CHAIN-STEPS` 
**Current state:** Very similar across 3 files, differs slightly in tone/format per platform
**Content structure:** 6 steps (Score, Sharpen, Route, Load, Produce, Finalize) with 5.5 (Verify)
**Appears in:** CLAUDE.md (lines ~35-60), GEMINI.md (lines ~22-32), AGENTS.md (lines ~17-32)
**Placement rule:** In Step section, before "Skip conditions"
**Platform variance:** None in substance; CLAUDE.md slightly more detailed. Propose single canonical version.
**File:** `directives/constitution-core/the-chain.md`

### Block 4: `AI-SLOP-BAN` 
**Current state:** Pointer added to CLAUDE.md Wave 1; missing from GEMINI.md/AGENTS.md (drift risk)
**Content:**
```
No AI slop: banned phrases/structural moves catalogued in `directives/ai-slop-ban-bank.md` (64 entries), enforced via `python3 execution/prose_classifier.py check <file>` before delivery.
```
**Appears in:** CLAUDE.md (Wave 1 addition), missing from GEMINI.md/AGENTS.md
**Placement rule:** Early enforcement section or within Step 5 (Produce)
**File:** `directives/constitution-core/ai-slop-ban.md`

### Block 5: `TOOLS-OR-TEXT-RULE`
**Current state:** Present in all three constitutions, identical language
**Content:**
```
Tools OR text per response—never both. Each turn is either all tool calls (respond after tools return) or all text (no tool calls) — never mix tool use and final prose in the same turn.
```
**Appears in:** CLAUDE.md Step 5, GEMINI.md Step 5, AGENTS.md Step 5
**Placement rule:** Within Step 5 (Produce) before "Enforce quality_assurance.md"
**File:** `directives/constitution-core/tools-or-text.md`

### Block 6: `DETERMINISTIC-ENFORCEMENT-LAYER`
**Current state:** Appears in CLAUDE.md (~lines 71-95) and GEMINI.md (~lines 36-48), identical tables and substance
**Content:** Cost gate, finalize debt, routing violations, extraction freeze, sub-agent truth behaviors
**Appears in:** CLAUDE.md, GEMINI.md (nearly identical)
**Note:** AGENTS.md/CODEX.md omit this (Codex omits hooks intentionally); should NOT be injected into those files
**File:** `directives/constitution-core/enforcement-hooks.md` — but mark PLATFORM-SPECIFIC: claude|gemini

### Block 7: `CONTEXT-ENGINE-TIERS`
**Current state:** Table present in CLAUDE.md (lines ~120-133) and GEMINI.md (lines ~60-71), structured identically
**Content:** 3-layer tier system (0=invocation-cards, 1=SKILL+workflow, 2=+genius.md, 3=sub-agent, 1.5a=Recall, 1.5b=memory_facade)
**Appears in:** CLAUDE.md, GEMINI.md (identical), AGENTS.md (less detailed but same structure)
**File:** `directives/constitution-core/context-engine.md`

---

## Extraction Strategy (For Your Review)

### Marker Format
```markdown
<!-- BEGIN:constitution-core/block-name.md -->
[injected content here]
<!-- END:constitution-core/block-name.md -->
```

### Injection Workflow
1. Create `directives/constitution-core/*.md` files with block content
2. Add `cmd_compile()` to `platform_compiler.py`:
   - Read each `directives/constitution-core/*.md` file
   - Search constitutions for `<!-- BEGIN:X -->...<!-- END:X -->` markers
   - Replace inner content, preserve markers
   - Respect CONSTRAINTS_LAST (CRITICAL block must sit in final 60%) and CANARIES
3. Wire `compile --check` and `compile --apply` into evolution_orchestrator.py (~lines 310/332)

### Deployment Approach
- **Phase 1 (Review):** Create block files, present to you for approval (Block 1-7 list above)
- **Phase 2 (Implement):** Extend platform_compiler.py with `cmd_compile()`, add markers to constitutions
- **Phase 3 (Wire):** Integration with evolution_orchestrator.py daily run
- **Phase 4 (Enforce):** `compile --check` becomes part of CI/pre-commit validation

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Over-extraction loses platform nuance | Mark blocks as PLATFORM-SPECIFIC; store separate versions (e.g., enforcement-hooks-claude.md vs enforcement-hooks-gemini.md) |
| Marker corruption during manual edits | `compile --check` exits 1 if markers malformed; pre-sync validation required |
| Block order sensitivity (e.g., CRITICAL placement) | Linter already checks CONSTRAINTS_MIN_OFFSET; extend to validate block markers respect this |
| Size limit violations (GEMINI.md 15KB) | `compile` measures output size before writing; fails if over limit, reports drift |

---

## Next Steps (After Your Approval)

1. **Approve blocks 1-7** (content, placement, platform-specific notes)
2. **Approve extraction strategy** (marker format, injection workflow)
3. **Optional refinements** (additional blocks, block structure, naming conventions)
4. Then: Create block files → Extend platform_compiler.py → Wire evolution_orchestrator.py

---

## Questions for You

- **Block 6 (enforcement-hooks):** Create separate files for Claude/Gemini/Codex versions, or one file with platform guards (`<!-- PLATFORM:claude|gemini -->`)?
- **Block 5 (tools-or-text):** This is currently in Step 5; when compiling, should it replace the inline text or coexist?
- **New blocks?** Any other content that appears in 2+ constitutions and should be centralized?
- **Deployment risk:** After implementation, when should `compile` be wired as a hard gate vs. advisory report?
