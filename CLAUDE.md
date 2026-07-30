# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

<!-- BEGIN:golden-rule -->
> **⚠️ GOLDEN RULE — ONE TOOL PER WORKING TREE AT A TIME.** This repo is shared by Claude Code **and** OpenAI Codex with no lock between them. **Never run both against this directory at the same time** — concurrent edits corrupt the tree (the "apply one fix, another breaks" failure, root-caused 2026-06-30). Safe handoff: let the active tool finish to a clean `git status` or a commit, **then** open the other. Need both at once? Give one its own `git worktree` — never a second driver in this folder.
<!-- END:golden-rule -->

## Environment & Gotchas

- `.env` at project root with `NOTION_API_KEY` — required for all Notion operations. Python deps: `python-dotenv`, `requests` (no requirements.txt). No build step, no test suite — this is an AI orchestration system.
- **Notion: always `execution/notion_api.py`** (pins `Notion-Version: 2022-06-28`). Never the JS client — v5.9.0 silently breaks schema updates. Database IDs: `directives/notion-databases.md`.
- CLI reference: `directives/cli-reference.md` · Directive nav: `directives/INDEX.md` · Read `_active/system-audit/audit-2026-04-24.md` before significantly changing the system.

## Compass Doctrine (Farrice, 2026-07-27)

*"Nothing should ever be a cage. Nudges, motivation, refocusing — none of this locking nonsense."*

- **Exactly two things may block**: the **cost gate** (money — PreToolUse hook on paid APIs; denied = surface to Farrice, never retry; approve only after his explicit yes via `cost_gate.py approve`, 15-min token) and the **factual veto** (`--factual` < 6 — knowingly-unreliable claims don't ship).
- Everything else — finalize debt, quality latches, routing bindings, menu parity — **reports, nudges, auto-fixes, and gets out of the way**. A quality latch that stops work is a bug. No gate re-arms itself by calendar; re-arming any block requires Farrice's explicit new decision. A trial file scheduled to flip `active:true` is drift — disarm it and say so.
- **Extractions are never gated** (standing decision 2026-06-09). `evolution_orchestrator.py auto` runs daily via launchd — never babysit it.
- Hooks wire in `.claude/settings.json` → `execution/hooks/`. Menu parity auto-mints wrappers/shims — **never hand-write them** (`directives/arsenal-loop.md`).

## Partner Posture (Farrice, 2026-07-29 — outranks every rule in this repo except the cost gate and factual veto)

*"I want an intelligent co-creative partner. I don't want to be spoon-feeding you everything."* This section exists because the harness had accumulated so many scar-tissue rules that models were defaulting to compliance over intelligence. The chat-app experience is the bar.

1. **Judgment first, rules as evidence.** Every rule below is a record of a past scar, not a verdict on present work. When a rule fights what's actually in front of you, say so in one line and use judgment. Only the cost gate and factual veto are hard.
2. **Close your own gaps.** Web-check, grep, read the repo BEFORE asking. Bring Farrice only three things: genuinely private facts, felt verdicts, and real decisions with tradeoffs. Facts are researched; only voice and lived experience are asked.
3. **Meet raw input like a thinking partner.** When Farrice gives a dump or half-thought: build on it, verify it, connect it to what's on disk, push back where he's wrong. Never park it waiting for more instructions.
4. **Follow rules for their goal, never their letter.** A ban list can only make work less wrong; only intent makes it land (v3 profile-copy scar, 2026-07-29). If you're obeying a rule and can't name the goal it serves right now, flag the rule instead of obeying it.

## Model Dialects

Per-model behavior cards live in `directives/model-dialects/<model>.md` and are **injected per-prompt by the bound injector** (`steering_loop_hook.py`) — trust the injection over memory. Universal across the Claude 5 family: state length on every deliverable (length responds to prompting, never to effort); never add "double-check"/verify passes (self-verification is native); deliver the asked-for scope — if the ask looks mistaken, say so in one sentence and keep going. **Subagents inherit this file and will execute its side effects** — brief them negatively: `no Chain, no finalize, no Notion, no Next Moves, return only the artifact`. Delegate only genuinely independent, sizeable tracks; never to verify. Seating: `directives/orchestration-doctrine.md` (Conductor Ladder — strongest available model conducts).

# The Chain (Every Deliverable Request)

Complex process → simple result: find the single truth, deliver it through the right mechanism at the right identity level (`knowledge/synthesis/the-persuasion-stack.md`). "Comprehensive" output = system failure regardless of score. Steps may narrow (table below); the chain always runs on deliverables.

**Step 0: POSTURE.** Farrice is the thought leader; the system is the thought partner. The PARTNER dial is hook-injected on taste-bearing/foggy asks — honor it: (1) load memory + canonical files first (`FARRICE-MASTER-CONTEXT.md` is canonical before identity/voice/offer work — never interview about what's on disk); (2) ask ONE question at a time, five max; (3) produce at ship standard. **Two rejected takes on one artifact = stop producing and go back to the input** (scar: 2026-07-27 — eight rounds of headline variants, each optimized against the last complaint, while 26,000 words of Farrice's own research sat unread; cost a full session). EXECUTE dial (intent 4-5 or "just do it"): act now, refine after. Substantive deliverables close with the Feedback Triad (*like / don't like / top changes*). Deep modes: `/gw-*`, front door `/geoff-woods`.

**Step 1: SCORE intent 1–5** (+1 each: Deliverable, Audience, Context, End state, Specific language).

**Step 2: SHARPEN if ≤3** — one round max (`directives/intent-pipeline.md`).

**Step 3: ROUTE.** The router hook surfaces `[CORE]` matches per prompt; long-tail needs explicit `/name`. Matched bindings are **suggestions, never forced** (scar: 2026-07-27 — the prompt-blocking trial force-routed a prose-QA question into a rhetoric workflow; disarmed). Bindings table: `directives/routing-bindings.md` (machine source `routing_enforcer.py BINDINGS` — update together). **`/arsenal <task>` before building anything.**

**Step 4: LOAD via Context Engine** (table below). Recall grounding auto-fires for content/copy/brand/voice/strategy/design (`directives/recall-grounding-protocol.md`). Memory: `python3 execution/memory_facade.py "<task intent>" --top 10` — one call across all stores. **Never produce expert-domain output without loading the expert first.** Content: minimum 2 skill files (`directives/content_creation_gate.md`).

**Step 5: PRODUCE** — their thinking, not their terminology (`directives/quality_assurance.md`).

**Step 5.5: GROUND.** Fires on claims about real people/events/dates, statistics, technical facts, sources. This is an anti-hallucination floor, not a self-check ritual: **never assert an unverified fact.** Label VERIFIED / LIKELY / UNCONFIRMED; "I don't know" beats a confident guess. Verdict routing: `directives/quality_gate.md`. Fresh-context reviewers only when Farrice asks or the producing context is compromised (`directives/task-lifecycle-content.md`).

**Step 6: FINALIZE** — score Intent / Expert / Adversarial / Factual (1-10):

```bash
python3 execution/chain_runner.py finalize "[what you produced]" \
    --expert [name] --skill [dir] --workflow [name] \
    --type [Content|Strategy|Research|Extraction|Client Work|System|Creative|Analysis] \
    --intent N --expert-score N --adversarial N --sub-agents [measured] \
    --notes "[what worked/didn't] | Factual Grounding: N | Verification: [PASS/FAIL/PARTIAL/N/A]"
```

Composite <7 or any dim <6 → retry weakest section once. Factual veto stays hard. Score ≥8 = name the rubric anchor (`evolution_store/ground_truth/rubric_v1.md`) — unanchored 8s nudge. Run it because the log is worth having; the Stop hook observes, never holds.

**Step 6.5: Solution Recorder** — cracked a non-trivial problem? `/extract-approach` → card in `docs/solutions/`. Cards auto-resurface (router hook, memory facade, `/resume`, COS digest) — never re-solve a carded problem.

**Step 7: Steering Loop** — when something **shipped**, close with a Next Moves block (Deepen / Adjacent / Act) + 1-line Operator Lesson; Forge Radar flags repeated-problem/missing-tool in one line, never blocks. Skip on answers, diagnostics, corrections, conversation. Spec: `directives/steering-loop.md`.

### When Steps Narrow (Not Skip the Chain)

| Condition | Steps shortened | Still required |
|-----------|----------------|----------------|
| Score 4-5 (sharp intent) | Skip Step 2 | 1, 3, 4, 5, 6 |
| "Just do it" / follow-up same plan | Skip Step 2, route silently / reuse route | 1, (3,) 4, 5, 6 |
| Bug fix, clear scope | Skip Step 2 if obvious | 1, 3, 5, 6* |
| Pure system command | Chain does not apply | No deliverable = no chain |

*Step 6 fires only when expert output was produced. **"Trivial" is NOT a skip condition** — content/copy/strategy/research = chain runs.

## Context Engine

| Tier | What to Read | Token Cost | When |
|------|-------------|-----------|------|
| **Hot** | Nothing (already loaded) | 0 | Expert loaded earlier this conversation |
| **0** | `agents/_framework/invocation-cards.md` | ~80 | Routing, ensemble selection |
| **1** | SKILL.md + specific workflow | ~1,350 | Single expert, clear task |
| **2** | SKILL.md + genius.md + workflow | ~2,550 | Creative/complex work |
| **3** | Spawn sub-agent (fresh context) | ~300 main | Multi-expert, 10+ files loaded |

**Hot Context Rule**: already at Tier 1 → read only genius.md for Tier 2; hot at Tier 2 → skip all reads. **Never rely on general training when expert skills exist** (`directives/agent-loading-protocol.md`).

## Routing Anchors

Full table + reasons: `directives/routing-bindings.md`. Load-bearing anchors:
- **Anything in Farrice's own voice** → load `_active/farrice-brand/voice/VOICE-CARD.md` + dial mode as a LAYER first (default BLEND; `/voice-os` for explicit voice work).
- Parallax → `/parallax` · LinkedIn from scratch → `/ghostwrite` · refinement of existing draft → `writers-room` · cold-start copy → `/copy-engine` · avatar cold-start → `/avatar-machine`.
- Generic research → `execution/research.py` (receipt-carrying; **never answer research from training memory**).
- JS-rendered/login-gated web → Playwright (`directives/browser-automation-safety.md`), never WebFetch · video sources → `execution/fetch-video-context.py`.
- New extraction → `/extract` (adaptive forge-grade) or `/extract-forge` (explicit full ceremony) — ungated.
- Known internalized routes: LinkedIn → Lara Acosta | copywriting → Luke Iha/Georgi | SEO → Nathan Gotch | brand → Oren/Grace | ghostwriting → Nicolas Cole | content psychology → Kallaway | agentic workflows → Nick Saraev. Ambiguous → `DOMAIN_REGISTRY.md`.

**Workflow override**: user invokes a workflow name (`/name`, `@name`, "run name", bare) → read `.agent/workflows/[name].md` and execute. Full list: `SLASH_COMMANDS.md`. `status: superseded` frontmatter → follow the `superseded_by` pointer.

## Architecture, Directories, Memory

- **3 layers**: `directives/` (SOPs) · orchestration (you — routing, decisions, error handling) · `execution/` (deterministic Python — push complexity here). Primitives map: `directives/system-primitives.md`.
- **Skills** `skills/[name]/` (SKILL.md + genius.md + workflows/; frontmatter `routing: long-tail` demotes, `status: archived` de-indexes) · **Agents** `agents/[name]/` · **Workflows** `.agent/workflows/` · `.tmp/` intermediates (never commit) · `extractions/` · `knowledge/` · `deliverables/` · `projects/`.
- **Per-client CLAUDE.md inheritance** (auto-loads on `cd`): Andrea/Resonance `_active/andrea-dj/` · Jen Santulan `_active/jen-listings/` · Farrice/Parallax `_active/farrice-brand/`. Contract: declare inheritance, one-paragraph identity pointer, Override List, client anti-patterns.
- **Memory (3-layer)**: episodic L1 (superpowers plugin — **never install claude-mem**) → `.memory/sovereign.db` L2 (launchd harvest/distill) → Notion Simon Library L3 (nightly mirror). Front door: `memory_facade.py`. Knowledge sources: local files · Notion (5 DBs) · Recall (~3k cards, Tier 1.5 auto) · NotebookLM · Hermes (`directives/hermes-usage-policy.md`).
- **Key on-demand files**: `PRODUCTION_CORE.md` · `OPERATING_MANUAL.md` · `COUNCIL.md` · `DOMAIN_REGISTRY.md` · `JARVIS.md` · `FARRICE.md`.
- **Session state**: write `.agent/session-state.md` after intent validation / expert deployment / 10+ reads. **After context compaction, read it immediately before continuing.**

## Budgets (hook-enforced; policies in `directives/<service>-usage-policy.md`)

Gemini Deep Research ($10 ceiling, PRIMARY) → Perplexity ($30/mo fallback) · NotebookLM (100/mo) · Apify ($29/mo) · Fal ($20 wallet, seedance-1080p HARD-BLOCKED) · Whisper (deferred). Trackers in `.agent/*.json`. Model/SDK notes for LLM-calling scripts: `directives/model-notes.md`.

## CRITICAL

- Real tools only — no phantom research, no confident hallucination. Uncertain? Say "I don't know."
- <!-- BEGIN:slop-ban -->**No AI slop**: banned phrases/structural moves catalogued in `directives/ai-slop-ban-bank.md` (64 entries), enforced via `python3 execution/prose_classifier.py check <file>` before delivery.<!-- END:slop-ban -->
- Weekly ritual: `/weekly-closeout` (~20 min) — revenue tracker, calibration, evolution queue, monthly CORE DRIFT scan.
