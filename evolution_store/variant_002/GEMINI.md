# GEMINI.md — Gemini-Native Antigravity

> CLAUDE.md intent, optimized for Gemini budget.
> Rules auto-load from `.gemini/rules/`. This file holds core rules + env.

## ⛔ CRITICAL
1. **CHAIN RUNS ON EVERY DELIVERABLE.** No skips. See `chain.md`.
2. **LOAD EXPERTS FIRST.** Read SKILL.md + workflow BEFORE writing.
3. **⛔ NEVER MIX TOOL CALLS & TEXT.** Response = EITHER tool OR text. Prevents crashes.
4. **COMPACTION RECOVERY:** READ `.agent/session-state.md` IMMEDIATELY.
5. **NO AI SLOP.** Banned: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy.

---

## Environment
- `.env` at root = `NOTION_API_KEY`
- ⛔ NO JS Notion client. Use `execution/notion_api.py` (`Notion-Version: 2022-06-28`)
- Scripts: run from project root. Check `execution/` first.

## Reference
See `directives/gemini-reference.md` for directory, file org, knowledge sources, and budget gates.

## Modular Rules (`.gemini/rules/`)
- `chain.md`: 6-step loop (SCORE → SHARPEN → ROUTE → LOAD → PRODUCE → FINALIZE)
- `routing.md`: Expert routing & auto-deploy signals
- `context-engine.md`: Tiered loading & escalation
- `quality.md`: Quality gates, anti-patterns, scoring
- `efficiency.md`: Token optimization, tools, checkpoints
- `memory.md`: Session anchors, compaction, protocols
