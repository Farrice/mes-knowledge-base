# GEMINI.md — Antigravity System

## Environment
- `.env` at root = `NOTION_API_KEY`
- NO JS Notion client. Use `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`)
- Scripts from project root. Check `execution/` before creating new ones.
- Directory/file details: `directives/gemini-reference.md`

## The Chain — Every Deliverable, No Exceptions

**Step 1 SCORE:** +1 Deliverable +1 Audience +1 Context +1 End-state +1 Specificity. Print score.
**Step 2 SHARPEN:** If ≤3, ask missing dimensions (one round). Skip if ≥4.
**Step 3 ROUTE:** LinkedIn→Lara Acosta | Copy→Luke Iha | SEO→Gotch | Brand→Oren/Grace | Ghost→Cole | Psychology→Kallaway | Consumer→Dai Media | Agentic→Saraev. Ambiguous? Read `DOMAIN_REGISTRY.md`. Print expert name.
**Step 4 LOAD:** Read `skills/[name]/SKILL.md` + workflow BEFORE writing. Add `genius.md` for creative/complex. Hot expert? Skip reads. Print files loaded.
**Step 5 PRODUCE:** Tool calls in one response, text in the next. NEVER mix. Use real tools — no phantom research.
**Step 6 FINALIZE:** Score Intent/Expert/Adversarial 1-10 each. Run: `python3 execution/chain_runner.py finalize "[summary]" --expert X --skill X --workflow X --type X --intent X --expert-score X --adversarial X --notes "X"`. Composite <7 or any <6 → retry.

**Narrowing:** Score 4-5 skip Step 2. "Just do it" route silently. Follow-up reuse Step 3. System commands skip chain.
**Workflows:** `/command` → read `.agent/workflows/[command].md` and execute.

## CRITICAL — These Override Everything

1. **CHAIN RUNS ON EVERY DELIVERABLE.** No skip for "trivial."
2. **LOAD EXPERT BEFORE PRODUCING.** No expert output without reading SKILL.md first.
3. **NEVER MIX TOOL CALLS WITH TEXT.** Response = 100% tools OR 100% text. Mixing crashes the session.
4. **AFTER COMPACTION:** Read `.agent/session-state.md` IMMEDIATELY.
5. **NO AI SLOP.** Banned: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy.
6. **USE REAL TOOLS.** No training-data substitution. Phantom research = automatic failure.

## VERIFY: ANTIGRAVITY-GEMINI-7X4K
