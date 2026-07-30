---
status: superseded
superseded_by: CLAUDE.md
superseded_date: 2026-07-29
amnesty_note: >
  Rule amnesty 2026-07-29 (Farrice-ratified). Activation count 0; review date 3.5 months overdue; its sub-agent VERIFICATION-block template contradicts the ratified dialect law (C4). Live homes: CLAUDE.md Context Engine (tiers) + memory_facade.py (Tier 1.5 loading).
---

# Agent Loading Protocol

> How expert agents/skills are loaded into context. Balances depth with context efficiency.
> Referenced from: GEMINI.md Context Engine, content_creation_gate.md

---

## The Loading Chain

### Tier 0: Card Check (ALWAYS FIRST)
Read `agents/_framework/invocation-cards.md`. ~50-80 tokens/expert. Sufficient for: routing, recommendations, ensemble selection. Stop here if deciding WHICH expert, not executing methodology.

### Tier 1.5: Unified Memory Facade (Sprint 4, 2026-05-25 · facade shipped 2026-06-12, audit Fix 7)
Before Tier 1 file loads, invoke the unified facade for retrieval grounding. It makes ONE call across every memory store instead of querying each silo separately:

```bash
python3 execution/memory_facade.py "<task intent in 10-20 words>" --top 10
```

What it returns (sovereign pinned rules first, then everything else by score, deduped):
- **sovereign** — `.memory/sovereign.db` vector retrieval (pinned voice rules / banned moves always surface first; deterministic FTS5 fallback when embeddings are unavailable)
- **automem** — Claude Code user auto-memory (`~/.claude/.../memory/`), frontmatter-description keyword match
- **wiki** — `knowledge/` manifest pointers (filename / domain / expert match) — pointers, not full docs
- **agents** — `agents/*/memory/context.md`, matched when the query names an agent

Every store that returns nothing or errors is REPORTED in the `degraded` field — silent-skip is the banned pattern this facade exists to kill. The facade is read-only and wraps the single-store entry points; `python3 execution/memory_retrieve.py "<intent>"` remains valid as the sovereign-only sub-path. Use `--sources sovereign,automem` to subset, `--json` for structured output.

Inject the top 5-10 results into your working context BEFORE producing output. This is the primary mechanism for cross-session compounding — past voice rules, prior routing decisions, and distilled patterns all surface here.

**When to invoke:** Always, when producing expert-domain output (content, strategy, copy, brand, voice, etc.). Skip for trivial system commands (file reads, git status).

**Token budget:** ~500-1500 tokens for top 10 results (each row ≤300 chars). Add `--top 5` if context-constrained.

**Workspace scoping:** Auto-detects from CWD (looks for `projects/<slug>/state.yaml`). Override with `--workspace <slug>` or env `ANTIGRAVITY_WORKSPACE`.

### Tier 1: Standard Load
Read `skills/[skill]/SKILL.md` + specific prompt. Skip genius.md. ~1,350 tokens. For: straightforward tasks where prompt gives everything needed.

### Tier 2: Deep Load
Read SKILL.md + genius.md + workflow. ~2,550 tokens. For: taste, creative judgment, novel application. Optionally add AGENT.md + memory/context.md.

### Tier 3: Sub-Agent Load
Spawn sub-agent with fresh context. ~300 tokens main. For: 2+ experts needed, or 10+ files already loaded.

**Semantic-first alternative:** `python3 execution/context_retriever.py search "query"` → ranked chunks before full-file loading.

## Decision Matrix

| Task | Expert Count | Tier |
|---|---|---|
| Quick recommendation / routing | 1-5 | T0 |
| Single expert, clear task | 1 | T1 |
| Single expert, creative/complex | 1 | T2 |
| Multi-expert, any complexity | 2+ | T3 |
| Council / Roundtable | 3-5 | T0 + sub-agents |

---

## Sub-Agent Prompt Template (Tier 3)

Never describe frameworks — require direct file reading:
1. SKILL ACQUISITION: Read SKILL.md → genius.md → specific prompt. Confirm 3 patterns, output structure, what expert says is WRONG.
2. EXPERT-DRIVEN EXECUTION: Apply methodology to task.
3. OUTPUT: Embody principles (not templates). Reference patterns by name.
4. VERIFICATION: `SKILL FILES READ: [list] | PATTERNS APPLIED: [list] | QUALITY CHECK: [test, pass/fail]`

**Creative Latitude:** Skills transfer principles/taste/intuition — NOT templates. Absorb, create original.

---

## Missing Card Protocol
No invocation card? → Fall back to T1 (read SKILL.md directly). After session, add card.

## Agent-to-Agent Handoffs
Summarize → identify receiving agent → ask approval → load receiving agent from T0.

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-11 |

*Created: 2026-02-27 | Compressed: 2026-04-13*
