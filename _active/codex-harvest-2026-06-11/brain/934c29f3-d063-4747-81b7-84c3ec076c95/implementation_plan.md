# Context Engineering Sprint 4-5-6: Memory Scaling, Auto-Hooks, Directive Modernization

## Background

Sprints 2-3 shipped the core infrastructure: sovereign memory store, chain integration, and 63% directive compression. This plan covers the three next-horizon items identified in the walkthrough.

---

## Sprint 4: Memory Scaling

Enhance `memory_store.py` with two capabilities the current MVP lacks:

### What Changes

#### [MODIFY] [memory_store.py](file:///Users/farricecain/Google%20Antigravity/execution/memory_store.py)

1. **FTS5 Full-Text Search**: Replace keyword-based search with SQLite FTS5 (built-in, zero dependencies). This gives us ranked BM25 scoring instead of naive word overlap — the same algorithm powering production search engines.

2. **Deduplication Engine**: Add a `deduplicate` command that detects near-duplicate memories (Jaccard similarity > 0.7) and merges them, keeping the highest-freshness version. As the store grows, duplicates will accumulate from repeated sessions.

3. **Prune Cold**: Add a `prune` command that permanently deletes memories below `FRESHNESS_COLD` threshold (with confirmation). Keeps the store lean.

4. **Batch Store**: Add a `batch-store` CLI command accepting a JSON file of memories — enables bulk seeding from session summaries.

> [!NOTE]
> PostgreSQL + pgvector remains the long-term path. FTS5 is the right move now because it's zero-dependency, ships with SQLite, and handles our current scale (4-1000 memories) efficiently.

---

## Sprint 5: Auto-Memory Hooks

Wire `memory_store.py` into `chain_runner.py` so every chain finalization auto-stores a memory. This closes the critical gap: currently memories only exist if someone manually stores them.

### What Changes

#### [MODIFY] [chain_runner.py](file:///Users/farricecain/Google%20Antigravity/execution/chain_runner.py)

Add a new Step 9 (after the evolution trace) that:
1. Imports `memory_store.store_memory` 
2. Auto-stores an **episodic/milestone** memory with: output description, expert, skill, composite score, status, and notes
3. On quality gate FAIL, also stores an **episodic/error** memory capturing the failure dimensions
4. On regression detection, stores a **semantic/error_pattern** memory capturing the regression data
5. All auto-stored memories include metadata: `{"source": "chain_runner", "session": "<id>", "composite": <score>}`

#### [MODIFY] [memory_store.py](file:///Users/farricecain/Google%20Antigravity/execution/memory_store.py)

Add a Python-importable `store_memory_silent()` function that stores without printing — for programmatic use from chain_runner.

---

## Sprint 6: Directive Modernization

Compress the next tier of large directives. The first sprint hit the 6 core directives (56K → 21K). This sprint targets the next 5 largest that are actively loaded:

| Directive | Current Size | Target |
|---|---|---|
| `feedback-ratchet.md` | 9,320 bytes | ~4,500 bytes |
| `token-efficiency-protocol.md` | 8,649 bytes | ~3,500 bytes |
| `perplexity-usage-policy.md` | 8,314 bytes | ~4,000 bytes |
| `sub_agent_protocol.md` | 12,965 bytes | ~6,000 bytes |
| `expert_auto_routing.md` | 4,739 bytes | ~2,500 bytes |
| **Total** | **43,987 bytes** | **~20,500 bytes** |

> [!IMPORTANT]
> `evolution-direction.md` (54K) is excluded — it's a data file (evolution history), not a directive. Compressing it would destroy historical records. Same for `mes-3.0-extract.md` and `ghostwriting-delivery.md` which are SOPs, not system prompts.

### Compression Vectors (same methodology as Sprint 3)
1. Remove duplicate cross-references to rules already in GEMINI.md
2. Collapse verbose examples into single-line rules
3. Inline templates instead of multi-line code blocks
4. Remove "why" narratives — keep "what" rules
5. Update stale references (e.g., `token-efficiency-protocol.md` references outdated CLAUDE.md and pre-routing internalized routes)

> [!WARNING]
> `token-efficiency-protocol.md` partially overlaps with what's now built into GEMINI.md (Context Engine, Execution Tools). Rules 3-6 are essentially superseded by the new architecture. We'll preserve the non-redundant rules and mark the rest as handled by the new tooling.

---

## Execution Order

1. **Sprint 4** first (Memory Scaling) — foundational for Sprint 5
2. **Sprint 5** second (Auto-Hooks) — depends on Sprint 4's batch/silent store
3. **Sprint 6** third (Directive Modernization) — independent, cleanup pass

## Verification Plan

### Automated Tests
- `python3 execution/memory_store.py search "chain runner"` — verify FTS5 returns ranked results
- `python3 execution/memory_store.py deduplicate --dry-run` — verify dedup detection
- `python3 execution/chain_runner.py finalize "test" --expert test --skill test --workflow test --type System --intent 8 --expert-score 8 --adversarial 8 --skip-notion` — verify auto-memory storage
- `python3 execution/memory_store.py stats` — verify memory count increased after finalize
- `wc -c` on all compressed directives — verify size reduction targets met
