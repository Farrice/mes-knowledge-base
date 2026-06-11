# Antigravity System — Codex Constitution

Self-contained: Codex does NOT auto-follow file pointers, so everything load-bearing is in THIS file. Deep reference (read on demand, never assume loaded): `GEMINI.md`, `CLAUDE.md`, `PRODUCTION_CORE.md`, `OPERATING_MANUAL.md`.

## What this workspace is
A 3-layer expert-orchestration OS owned by Farrice: JARVIS routing → 140 expert personas + 261 skills + 1,049 workflows → deterministic Python backplane (`execution/`, ~128 scripts). The goal: world-class extracted experts producing revenue work, every deliverable feeding one learning loop (finalize → ledger → evolution) **rooted in this repo** — never fork it.

## Environment
- `.env` at root holds `NOTION_API_KEY`. Python deps: `python-dotenv`, `requests`.
- Notion: ALWAYS `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`). Never the JS client.
- Skills: `skills/[name]/` → `SKILL.md` + `genius.md` + `workflows/*.md`. **This repo is the single source of truth** — the ports under `~/.codex/skills/` are stale and many fail YAML validation; prefer reading repo skills directly.
- Workflows: `/name` → read `.agent/workflows/[name].md` and execute. Index: `SLASH_COMMANDS.md`.
- Intermediates → `.tmp/` (never commit).

## The Chain (every deliverable request — no exceptions)
1. **SCORE** intent 1-5 (+1 each: Deliverable, Audience, Context, End-state, Specific language)
2. **SHARPEN** if ≤3 (one round of questions max)
3. **ROUTE** to expert skills. Default to `PRODUCTION_CORE.md` (~25 proven entries); long-tail needs explicit `/name`. Mandatory bindings: `directives/routing-bindings.md`.
4. **LOAD** before producing: `skills/[name]/SKILL.md` + minimum one more file (genius.md or workflow). Also: `python3 execution/memory_retrieve.py "<task intent>" --top 10`
5. **PRODUCE** — the expert's thinking, not their terminology
5.5 **VERIFY** — factual claims about real people/events/dates/stats/sources get labeled VERIFIED/LIKELY/UNCONFIRMED before delivery
6. **FINALIZE** (run in terminal at repo root):
   ```
   python3 execution/chain_runner.py finalize "[what you produced]" \
       --expert [name] --skill [dir] --workflow [name] \
       --type [Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis] \
       --intent N --expert-score N --adversarial N --sub-agents 0 \
       --notes "[what worked] | platform: codex | Verification: [PASS/FAIL/PARTIAL/N/A]"
   ```
   Composite <7 or any dimension <6 → retry weakest section once, re-finalize. Factual Grounding <6 = delivery blocked.

## No hooks on Codex — run gates manually
Claude Code enforces these physically; here YOU are the hook:
- **Cost gate** before any paid API (Fal, Seedance, Kling, deep-research): `python3 execution/cost_gate.py check --service <id>`. Denied = stop and surface.
- **Finalize debt**: produced an artifact with an expert skill loaded → Step 6 is mandatory before ending.
- **Routing bindings**: check `directives/routing-bindings.md` when a route feels ambiguous.

## Tool remaps (system docs use Claude Code names)
- `search_web` / `WebSearch` → Codex web search
- `read_url_content` / `WebFetch` → Codex URL fetch / browser
- `mcp__recall__search` → `recall` MCP server (configured in `~/.codex/config.toml`; re-auth if bearer token expired)
- Task/Agent sub-agent spawning → unavailable: execute sequentially, report `--sub-agents 0`

## Known routes (internalized)
LinkedIn → Lara Acosta (`skills/lara-acosta-*`) · copywriting → Luke Iha / Stefan Georgi · ghostwriting → Nicolas Cole · brand → Oren/Grace · content psychology → Kallaway · SEO → Nathan Gotch · ambiguous/multi-domain → read `DOMAIN_REGISTRY.md`.

## CRITICAL — placed last deliberately
1. **CHAIN ON EVERY DELIVERABLE.** Trivial is not a skip condition for content/copy/strategy/research.
2. **LOAD BEFORE PRODUCING.** Never ship expert-domain output from general training when an extracted skill exists.
3. **NO AI SLOP.** Banned words: delve, tapestry, landscape, leverage, robust, utilize, realm, multifaceted, holistic, synergy. Banned moves: "Here's what/why/how" openers, twin-sentence endings, triple anaphora, "It's not X. It's Y."
4. **REAL TOOLS ONLY.** No phantom research, no confident hallucination. Uncertain → say "I don't know."
5. **NEVER FORK THE SYSTEM.** Do not copy this workspace elsewhere; do not maintain parallel skill trees. All finalize/ledger/evolution data lands HERE.
6. **Do not edit `skills/`, `directives/`, `execution/`, hooks, or indexes casually** — production infrastructure shared with Claude Code.

## VERIFY: ANTIGRAVITY-CODEX-3J8R (Created 2026-06-11)
