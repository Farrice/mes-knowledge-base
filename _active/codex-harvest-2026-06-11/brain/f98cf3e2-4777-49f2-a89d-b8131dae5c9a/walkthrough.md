# Claude Code Harness → Antigravity Evolution — Walkthrough

## Summary

Adopted 6 high-ROI patterns from the Claude Code harness leak and built them into Antigravity across 3 phases.

---

## Phase 1: Foundation

### Prompt Modularization
Decomposed 128-line monolith `GEMINI.md` into 6 auto-loaded modules in `.gemini/rules/`:

| Module | Lines | Purpose |
|--------|-------|---------|
| `chain.md` | 69 | The 6-step chain |
| `routing.md` | 35 | Expert routing table |
| `context-engine.md` | 30 | Tiered loading |
| `quality.md` | 42 | Quality gates + anti-patterns |
| `efficiency.md` | 36 | Token optimization |
| `memory.md` | 69 | Session state + compaction + frustration |

`GEMINI.md` slimmed to 35 lines as a thin loader.

### Verification Agent
Created [verification-agent-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/verification-agent-protocol.md) — adversarial verification that fires after Step 5 with PASS/FAIL/PARTIAL verdicts. Integrated into chain and memory protocols table.

---

## Phase 2: Intelligence

### Semantic Memory Selection
[memory_selector.py](file:///Users/farricecain/Google%20Antigravity/execution/memory_selector.py) — 248-item manifest, Gemini Flash Lite ranking, ~$0.003/call.

```
"Write vicious hooks for SaaS" → Luke Iha Vicious Hooks (#1), Kallaway (#2), CASH Method (#3)
```

### Coordinator Mode
[parallel_swarm.py](file:///Users/farricecain/Google%20Antigravity/execution/parallel_swarm.py) `--coordinator` — 4-phase pipeline replacing keyword routing with semantic selection + LLM work order decomposition.

```
"LinkedIn strategy for AI founder" → Diandra (#1), Lara Acosta (#2), Tommy Clark (#3)
```

Total coordinator overhead: ~$0.005/swarm invocation.

---

## Phase 3: Polish

### 3-Mode Compaction

Extended [session-state-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/session-state-protocol.md) and [checkpoint_manager.py](file:///Users/farricecain/Google%20Antigravity/execution/checkpoint_manager.py) with graded compaction:

| Mode | When | What Survives |
|------|------|---------------|
| **Full** | Sub-agent spawn, total topic change | Everything → 9-section anchor |
| **Partial Older** | Same task, early context stale | Old summarized, recent 8 turns verbatim |
| **Partial Recent** | User pivoted directions | Old kept, new direction summarized |

Key features:
- Analysis-then-summary pattern (scan facts, then compress)
- Preservation rules (decisions, file paths, expert outputs always survive)
- Recent user messages always preserved verbatim (all modes)
- `detect_compaction_mode()` for automatic selection

**Test results**: 4/4 mode detection correct, write/read verified.

### Frustration Detection

Created [user-state-awareness.md](file:///Users/farricecain/Google%20Antigravity/directives/user-state-awareness.md) with 3-tier signal detection and automatic behavior shifts:

| Tier | Signals | Behavior Shift |
|------|---------|---------------|
| **1** | "this isn't working", "just do it" | Stop proposing, start executing |
| **2** | Single-word responses, repeated requests | Reduce output 50%, lead with answer |
| **3** | "forget it", "I'll do it myself" | Emergency mode, zero chain overhead |

Programmatic support via `detect_frustration(message)` in `checkpoint_manager.py`.

**Test results**: 9/9 detection cases correct.

---

## All Files Changed

| File | Phase | Change |
|------|-------|--------|
| `.gemini/rules/chain.md` | 1 | **[NEW]** Chain rules module |
| `.gemini/rules/routing.md` | 1 | **[NEW]** Expert routing module |
| `.gemini/rules/context-engine.md` | 1 | **[NEW]** Context engine module |
| `.gemini/rules/quality.md` | 1 | **[NEW]** Quality gates module |
| `.gemini/rules/efficiency.md` | 1 | **[NEW]** Token efficiency module |
| `.gemini/rules/memory.md` | 1,3 | **[NEW]** Memory + compaction + frustration rules |
| `GEMINI.md` | 1 | **[MODIFIED]** 128→35 lines (thin loader) |
| `directives/verification-agent-protocol.md` | 1 | **[NEW]** Adversarial verification |
| `execution/memory_selector.py` | 2 | **[NEW]** ~300 lines, semantic selection |
| `execution/parallel_swarm.py` | 2 | **[MODIFIED]** +290 lines, coordinator mode |
| `directives/session-state-protocol.md` | 3 | **[MODIFIED]** +80 lines, 3-mode compaction |
| `directives/user-state-awareness.md` | 3 | **[NEW]** Frustration detection |
| `execution/checkpoint_manager.py` | 3 | **[MODIFIED]** +240 lines, compaction + frustration |
