# Antigravity System — Workspace Rules (Antigravity IDE / Gemini surfaces)

You are operating inside the Antigravity orchestration OS. Full constitution: `GEMINI.md` (repo root). This file is the distilled, always-loaded version for the Antigravity IDE.

## What this workspace is
A 3-layer expert-orchestration system: routing (JARVIS) → 140 expert personas + 261 skills (`skills/[name]/SKILL.md` + `genius.md` + `workflows/`) → deterministic Python (`execution/`). The ~25 revenue-proven skills live in `PRODUCTION_CORE.md`. Workflows invoked as `/name` live in `.agent/workflows/`.

## The Chain (every deliverable, no exceptions)
1. **SCORE** intent 1-5 (+1 each: deliverable, audience, context, end-state, specificity)
2. **SHARPEN** if ≤3 — ask missing dimensions, one round max
3. **ROUTE** to expert skills — default to `PRODUCTION_CORE.md` entries; bindings in `directives/routing-bindings.md`
4. **LOAD** the expert before producing: `skills/[name]/SKILL.md` + at least one of genius.md / workflow. Also run `python3 execution/memory_retrieve.py "<task intent>" --top 10`
5. **PRODUCE** in the expert's thinking, not their terminology
5.5 **VERIFY** factual claims (real people/dates/stats/sources) → label VERIFIED/LIKELY/UNCONFIRMED before delivery
6. **FINALIZE** in a terminal at repo root:
   `python3 execution/chain_runner.py finalize "[what]" --expert X --skill X --workflow X --type [Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis] --intent N --expert-score N --adversarial N --sub-agents 0 --notes "... | platform: antigravity-ide | Verification: [PASS/FAIL/PARTIAL/N/A]"`

## No hooks here — manual gates
Claude Code enforces cost/finalize/routing via hooks. They DO NOT fire in this IDE. Before any paid API call run `python3 execution/cost_gate.py check --service <id>`. Always run Chain Step 6 yourself — this repo's ledger is canonical for ALL platforms.

## Tool remaps
`search_web` → GoogleSearch · `read_url_content` → URL fetch · `mcp__recall__search` → recall MCP (`.gemini/settings.json`) · sub-agent spawning → unavailable: run sequentially.

## CRITICAL (placed last deliberately — final instructions carry the most weight)
1. Chain on every deliverable; no trivial skip.
2. Load the expert skill BEFORE producing expert-domain output.
3. No AI slop: never delve/tapestry/landscape/leverage/robust/utilize/realm/multifaceted/holistic/synergy; no "Here's what/why/how" openers, no twin-sentence endings, no triple anaphora, no "It's not X. It's Y."
4. Real tools only — no phantom research, no confident hallucination. Uncertain → "I don't know."
5. Never edit `skills/`, `directives/`, `execution/` casually — they are production infrastructure shared with Claude Code.

## VERIFY: ANTIGRAVITY-IDE-9Q2M (Created 2026-06-11)
