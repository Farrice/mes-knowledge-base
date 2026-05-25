# Agent Loading Protocol

> How expert agents/skills are loaded into context. Balances depth with context efficiency.
> Referenced from: GEMINI.md Context Engine, content_creation_gate.md

---

## The Loading Chain

### Tier 0: Card Check (ALWAYS FIRST)
Read `agents/_framework/invocation-cards.md`. ~50-80 tokens/expert. Sufficient for: routing, recommendations, ensemble selection. Stop here if deciding WHICH expert, not executing methodology.

### Tier 1.5: Sovereign Memory Retrieval (NEW — Sprint 4, 2026-05-25)
Before Tier 1 file loads, invoke the memory cascade for retrieval grounding:

```bash
python3 execution/memory_retrieve.py "<task intent in 10-20 words>" --top 10
```

What it returns (in priority order):
- **Pinned semantic rules** — voice rules, banned moves, identity-layer feedback (always included, cosine-ranked)
- **Vec-semantic** — workspace-filtered semantic memories by similarity
- **Vec-procedural** — workspace-filtered operational configs by similarity
- **BM25 episodic** — recent decision-class memories by keyword match

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
