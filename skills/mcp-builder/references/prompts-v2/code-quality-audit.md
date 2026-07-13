---
name: "MCP Builder — Code Quality & Build Audit"
source_prompt: born-v2
skill: mcp-builder
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are reviewing a completed (or near-complete) MCP server implementation against the framework's own quality bar before it ships. This is Phase 3 of the build process: review and test, not first-pass authorship. You check for duplicated code, inconsistent error handling, missing type coverage, and unclear tool descriptions, then verify the server actually builds and runs — you do not take "looks right" as a substitute for a real build/test attempt.

## Input Required

- `[SERVER_SOURCE]` — the server's source file(s) or repository path
- `[LANGUAGE]` — Python or TypeScript (selects which checklist applies)
- `[TOOL_INVENTORY]` — the intended tool list, to check actual coverage against plan

## Execution Protocol

**3.1 — Code Quality.** Review for: no duplicated code (DRY — a pattern repeated across two or more tools should be a shared function); consistent error handling (every external call goes through the same error-mapping helper, same message style); full type coverage (Python: type hints everywhere; TypeScript: `strict` mode, zero `any`); clear tool descriptions (every tool's docstring/description tells an agent what it does, does NOT do, and when to use an alternate tool instead).

**3.2 — Build and Test.** For TypeScript: run `npm run build` and confirm it completes without errors; confirm `dist/index.js` exists and is executable; test with `npx @modelcontextprotocol/inspector`. For Python: run `python -m py_compile [file]` to verify syntax; confirm all imports resolve; test with the MCP Inspector. Do not report a build/test step as passed without having actually attempted it — "should work" is not a pass.

**Apply the full language-specific Quality Checklist as the audit rubric** (source: the language's implementation guide). Every item below is a checkable criterion, grouped exactly as the guide groups them:

*Strategic Design* — tools enable complete workflows (not bare endpoint wrappers); tool names reflect natural task subdivisions; response formats optimize for agent context efficiency; human-readable identifiers used where appropriate; error messages guide agents toward correct usage.

*Implementation Quality* — the most important/valuable tools are implemented (not a token subset); all tools have descriptive names and documentation; return types are consistent across similar operations; error handling covers all external calls; server name follows the language's naming convention; all network operations are async; common functionality is extracted into reusable functions; error messages are actionable and educational; outputs are validated and formatted.

*Tool Configuration* — Python: all tools implement `name` and `annotations` in the decorator; annotations correctly set; all tools use Pydantic `BaseModel` with `Field()`; all fields have explicit types, descriptions, and constraints; docstrings are comprehensive with explicit input/output types and full schema for dict/JSON returns. TypeScript: all tools registered via `registerTool` with complete configuration; `title`/`description`/`inputSchema`/`annotations` all present; Zod schemas use `.strict()` with descriptive messages; descriptions include return-value examples and complete schema documentation.

*Advanced Features (where applicable)* — Context injection / resources / lifespan management / structured output types used where they genuinely fit the tool's need (Python); resources registered for appropriate data endpoints, notifications used sparingly for genuine capability changes (TypeScript).

*Code Quality* — pagination properly implemented where applicable; filtering options provided for potentially large result sets; constants defined at module level in `UPPER_CASE`; (TypeScript only) `CHARACTER_LIMIT` truncation implemented with clear messages.

*Testing* — server runs/builds successfully; all imports resolve; sample tool calls behave as expected; error scenarios are handled gracefully (not just the happy path).

## Output Contract

An Audit Report: one row per checklist item (PASS / FAIL / N/A), each FAIL paired with a concrete fix (file/function named, not a vague restatement of the rule), plus a top-line Build & Test verification log showing the actual commands run and their actual output.

## Output Skeleton

```markdown
# [SERVICE_NAME] MCP Server — Code Quality Audit

## Build & Test Verification
- Command run: [exact command]
- Result: [pass/fail + relevant output excerpt]
- Command run: [exact command]
- Result: [pass/fail + relevant output excerpt]

## Strategic Design
| Item | Status | Evidence / Fix |
|---|---|---|
| [checklist item] | [PASS/FAIL/N-A] | [file:line or fix] |

## Implementation Quality
| Item | Status | Evidence / Fix |
|---|---|---|

## Tool Configuration
| Item | Status | Evidence / Fix |
|---|---|---|

## Advanced Features
| Item | Status | Evidence / Fix |
|---|---|---|

## Code Quality
| Item | Status | Evidence / Fix |
|---|---|---|

## Testing
| Item | Status | Evidence / Fix |
|---|---|---|

## Priority Fix List
1. [highest-impact FAIL first]
```

## Quality Gate

- Was the build/test step actually executed (real command, real output shown), not assumed?
- Does every checklist category from the applicable language guide appear in the report, with no category silently dropped?
- Does every FAIL name the specific file/function and a concrete fix, not a restatement of the checklist wording?
- Was the tool inventory cross-checked against what's actually implemented (missing tools flagged, not just quality of existing ones)?

## Deploy When

After a Python or TypeScript MCP server implementation is drafted and before it's considered ready for evaluation (Phase 4) or handoff — the gate between "written" and "verified."
