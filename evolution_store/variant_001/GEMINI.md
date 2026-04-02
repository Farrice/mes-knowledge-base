# GEMINI.md — Gemini-Native Antigravity Instructions

> CLAUDE.md intent, optimized for Gemini's budget.
> Auto-loaded modular rules in `.gemini/rules/`. This file holds only core rules and environment setup.

## ⛔ CRITICAL

1. **THE CHAIN RUNS ON EVERY DELIVERABLE.** "Trivial" is not a skip condition. See `.gemini/rules/chain.md`.
2. **NEVER produce expert output without loading the expert first.** Read SKILL.md + workflow BEFORE writing.
3. **⛔ NEVER MIX TOOL CALLS WITH TEXT OUTPUT.** Each response is EITHER tool calls OR text. This prevents crashes.
4. **After compaction:** READ `.agent/session-state.md` IMMEDIATELY to restore state.
5. **AI slop = automatic failure.** Banned: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy.

---

## Environment

- `.env` at root with `NOTION_API_KEY`
- ⛔ NO JS Notion client. Always use `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`)
- Scripts: run from project root. Check `execution/` before creating.

## Reference

See `directives/gemini-reference.md` for directory conventions, file org, knowledge sources, and budget gates.

## Modular Rules (`.gemini/rules/`)

- `chain.md`: The 6-step chain (SCORE → SHARPEN → ROUTE → LOAD → PRODUCE → FINALIZE)
- `routing.md`: Expert routing table and auto-deploy signals
- `context-engine.md`: Tiered loading (Hot → Tier 0-3) and escalation rules
- `quality.md`: Quality gates, anti-patterns, finalize scoring rubric
- `efficiency.md`: Token optimization, tool call discipline, checkpoint rules
- `memory.md`: Session state anchors, compaction recovery, supporting protocols
