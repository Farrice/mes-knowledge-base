# GEMINI.md — Gemini-Native Antigravity Instructions

> Same system intent as CLAUDE.md, optimized for Gemini's context budget.
> Modular rules are in `.gemini/rules/` — they are auto-loaded. This file contains only critical rules and environment setup.

## ⛔ CRITICAL RULES

1. **THE CHAIN RUNS ON EVERY DELIVERABLE.** "Trivial" is NOT a skip condition. See `.gemini/rules/chain.md`.
2. **NEVER produce expert output without loading the expert first.** Read SKILL.md + workflow BEFORE writing.
3. **⛔ NEVER MIX TOOL CALLS WITH TEXT OUTPUT IN THE SAME RESPONSE.** Each response is EITHER tool calls OR text — never both. This prevents crashes.
4. **After compaction:** READ `.agent/session-state.md` IMMEDIATELY to restore state.
5. **AI slop = automatic failure.** Banned: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy.

---

## Environment

- `.env` at root with `NOTION_API_KEY`
- ⛔ NEVER use JS Notion client. Always `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`)
- Scripts: run from project root. Check `execution/` before creating new ones.

## Reference

For directory conventions, file organization, knowledge sources, and budget gates: read `directives/gemini-reference.md`.

## Modular Rules (auto-loaded from `.gemini/rules/`)

| Module | What It Contains |
|--------|-----------------|
| `chain.md` | The 6-step chain — SCORE → SHARPEN → ROUTE → LOAD → PRODUCE → FINALIZE |
| `routing.md` | Expert routing table and auto-deploy signals |
| `context-engine.md` | Tiered loading (Hot → Tier 0-3) and escalation rules |
| `quality.md` | Quality gates, anti-patterns, finalize scoring rubric |
| `efficiency.md` | Token optimization, tool call discipline, checkpoint rules |
| `memory.md` | Session state anchors, compaction recovery, supporting protocols |
