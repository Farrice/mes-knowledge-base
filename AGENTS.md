# Antigravity System — Codex Constitution

Self-contained: Codex does NOT auto-follow file pointers, so everything load-bearing is in THIS file. `CODEX.md` is the Codex-native operating authority for this workspace; read it as the expanded harness contract when repairing routing, hooks, command surfaces, or Operator Core behavior. Deep reference (read on demand, never assume loaded): `GEMINI.md`, `CLAUDE.md`, `PRODUCTION_CORE.md`, `OPERATING_MANUAL.md`.

> **⚠️ GOLDEN RULE — ONE TOOL PER WORKING TREE AT A TIME.** This repo is shared by Claude Code **and** OpenAI Codex with no lock between them. **Never run both against this directory at the same time** — concurrent edits corrupt the tree (the "apply one fix, another breaks" failure, root-caused 2026-06-30). Safe handoff: let the active tool finish to a clean `git status` or a commit, **then** open the other. Need both at once? Give one its own `git worktree` — never a second driver in this folder.

## What this workspace is
A 3-layer expert-orchestration OS owned by Farrice: JARVIS routing → <!-- COUNTS:BEGIN -->219 expert personas + 367 skills + 1,527 workflows<!-- COUNTS:END --> → deterministic Python backplane (`execution/`, ~128 scripts). The goal: world-class extracted experts producing revenue work, every deliverable feeding one learning loop (finalize → ledger → evolution) **rooted in this repo** — never fork it.

## Environment
- `.env` at root holds `NOTION_API_KEY`. Python deps: `python-dotenv`, `requests`.
- Notion: ALWAYS `execution/notion_api.py` (pins `Notion-Version: 2022-06-28`). Never the JS client.
- Skills: `skills/[name]/` → `SKILL.md` + `genius.md` + `workflows/*.md`. **This repo is the single source of truth** — the ports under `~/.codex/skills/` are stale and many fail YAML validation; prefer reading repo skills directly.
- Workflows: `/name` → read `.agent/workflows/[name].md` and execute. Index: `SLASH_COMMANDS.md`.
- **Front doors (2026-07-06)**: `/go "<messy thought>"` = anti-bottleneck staging (silent DICE compile → written assumptions, max ONE question round → run packet → routes to the right conductor). `/create` = universal content conductor (outcome contract ≥2 outcomes → context richness → live zeitgeist w/ receipts → purpose routing → proven recipe → gates). Orchestrating multi-step or quality-critical work: load `directives/peak-operation.md` (the operating doctrine — shape of the work, routing table, drift signals, invariants).
- Intermediates → `.tmp/` (never commit).

## The Chain (every deliverable request — no exceptions)
1. **SCORE** intent 1-5 (+1 each: Deliverable, Audience, Context, End-state, Specific language)
2. **SHARPEN** if ≤3 (one round of questions max). Flowing/vision language ("I want it to feel like...", raw notes, stream-of-consciousness) → run the `/raw-intent-bridge` Stage 0 Vision Translation automatically (`.agent/workflows/raw-intent-bridge.md`): build the Translation Card, compile `python3 execution/raw_intent_run_packet.py "<sharpened intent line>" --plain`, execute the route with Farrice's verbatim words as the creative payload. Never compile or route raw flow-speech directly, and never make Farrice restate his vision in system terms.
3. **ROUTE** to expert skills. Default to `PRODUCTION_CORE.md` (~25 proven entries); long-tail needs explicit `/name`. Mandatory bindings: `directives/routing-bindings.md`.
4. **LOAD** before producing: `skills/[name]/SKILL.md` + minimum one more file (genius.md or workflow). Also: `python3 execution/memory_facade.py "<task intent>" --top 10` (one call across sovereign + auto-memory + wiki + agent + episodic stores; `memory_retrieve.py` stays valid as the sovereign-only sub-path)
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

<!-- BEGIN:solution-recorder -->**Step 6.5 — Solution Recorder (binding, 2026-07-07):** cracked a non-trivial problem (any domain)? Run `python3 execution/solution_recorder.py draft --slug <slug> --problem "<signature>"`, fill the card, `save` it to `docs/solutions/` before moving on — a solved problem without a card is unfinished work. Check `docs/solutions/index.md` before re-solving anything familiar. Finalize is latched to this: open fresh learning debt makes `chain_runner.py finalize` refuse until you pass `--learning <card>` (validated card clears the debt) or `--skip-learning` (proceeds, logged to `evolution_store/learning_latch_overrides.jsonl`).<!-- END:solution-recorder -->

## No hooks on Codex — run gates manually
Claude Code enforces these physically; here YOU are the hook:
- **Cost gate** before any paid API (Fal, Seedance, Kling, deep-research): `python3 execution/cost_gate.py check --service <id>`. Denied = stop and surface.
- **Finalize debt**: produced an artifact with an expert skill loaded → Step 6 is mandatory before ending.
- **Routing bindings**: check `directives/routing-bindings.md` when a route feels ambiguous.

## Persistent Per-Exchange Steering
Every meaningful final answer should end with useful steering and an Operator
Lesson by default. This is not command-only behavior and does not require
`/steering-compass`, `/end-session`, or any slash command to be invoked.

Default closeout:
- Tiny answers: one micro Operator Lesson is enough.
- Normal answers: include a compact Operator Lesson with What I noticed, Better
  system move, and Next-time prompt.
- Builds, repairs, artifacts, strategy, audits, recommendations, source work,
  client work, or any answer with a real next decision: include 3 Next Prompts
  under the Insightful Momentum/frontier standard.

The 3 Next Prompts must be useful follow-ups, not a legacy prompt shell. Keep
Use Now / Harden / Expand, but make the visible options context-rich and
capability-revealing:
- action title tied to the actual session object
- Output/Capability Move
- Operator Insight
- Hidden Gap/Opportunity
- Capability Revealed
- Prompt
- Expected output or What it entails
- Quality bar
- Skip condition when useful
- Suggested skills/workflows

When `execution/contextual_next_prompts.py` fits the situation, use it before
finalizing:

```bash
python3 execution/contextual_next_prompts.py --objective "[current objective]"
```

If the helper output is awkward, improve the objective and rerun it; do not
compress the closeout back into generic next steps. Skip steering only when
Farrice explicitly asks for a terse/direct answer, a higher-priority instruction
requires silence, or a special tool action requires no extra text.

## Execution Bias Contract
When intent is clear enough and no risk boundary is detected, Codex defaults to **Patch + Verify** for safe workspace-local work. Do the next local action first, keep commentary to blockers or decision gates, then report what changed and what passed.

- Do not hand Farrice another prompt when the next step is a safe local inspection, patch, verifier run, or receipt.
- Ask only when the answer changes execution, taste, scope, external action, destructive action, paid/quota use, global `~/.codex`, Codex Antigravity writes, or real subagent behavior.
- For system, routing, hook, operator-core, or "explaining instead of executing" complaints, route to `/system-audit` and run `python3 execution/codex_operator_preflight.py "<raw intent>" --plain` as the manual hook-equivalent gate.
- Subagents default to read-only diagnostics/validation. The main thread owns file edits and integration unless Farrice explicitly authorizes edit-owning workers with disjoint write scopes.

## Tool remaps (system docs use Claude Code names)
- `search_web` / `WebSearch` → Codex web search
- `read_url_content` / `WebFetch` → Codex URL fetch / browser
- `mcp__recall__search` → `recall` MCP server (configured in `~/.codex/config.toml`; re-auth if bearer token expired)
- Task/Agent sub-agent spawning → when unavailable, execute sequentially and report `--sub-agents 0`; when available and explicitly authorized, use read-only diagnostic/validation subagents by default and keep the main thread responsible for edits.

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
