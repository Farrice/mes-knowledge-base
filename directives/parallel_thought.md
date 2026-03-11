# Parallel Thought Protocol (Rimuru Protocol)

> **Trigger**: Activates automatically when the Router Agent classifies a task as **complex** or **swarm-worthy**, OR when a build/design task has >1 viable approach.
> **Reference**: `skills/nick-saraev-agentic-workflows/references/prompts/crown_jewel_04_parallel_build_orchestrator.md`
>
> **Execution Modes**:
> - **Single-Agent** → Structured Exploration (one agent thinks through 3 approaches sequentially, picks the winner)
> - **Multi-Agent** → True Parallelism (via `parallel_swarm.py` — 3 agents explore simultaneously)

---

## When to Parallelize

Run this check on every build, design, or creative task:

| Signal | Action |
|--------|--------|
| Only one obvious approach exists | **Skip** — execute directly |
| 2+ viable approaches with different trade-offs | **Parallelize** — run the Three-Track Pattern |
| Task spans multiple domains (research + build + launch) | **Swarm** — escalate to `/swarm` or `/parallel-swarm` |
| Simple refactor, bug fix, or factual question | **Never parallelize** — overhead isn't worth it |

**Anti-Bloat Rule**: Parallelization has cognitive overhead. Only invoke when the cost of picking wrong > cost of exploring multiple paths.

### Disambiguation Trigger

When it's **unclear** whether a task warrants parallelization:

```
IF uncertainty about whether to parallelize:
  Present to user:
  "I see 2-3 viable approaches with different trade-offs.
   Want me to explore them in parallel, or should I pick
   my best guess and go?"
```

**Don't guess. Don't silently skip. Ask once, then execute.**
This fires when complexity signals are mixed — e.g., a task that *looks* simple but has hidden trade-offs, or a build request where the "right" approach depends on user priorities (speed vs. reliability).

---

## The Three-Track Pattern

When parallelization triggers, design three distinct approaches:

### Track 1: Conservative (Proven Patterns)
- Battle-tested libraries and methods
- Maximum reliability, minimum risk
- Trade-off: may be slower or less elegant

### Track 2: Moderate (Balanced)
- Best-practice approach with some optimization
- Good balance of reliability and performance
- Trade-off: requires more careful testing

### Track 3: Aggressive (Maximum Performance)
- Cutting-edge techniques, maximum optimization
- Highest ceiling but also highest risk
- Trade-off: may require more debugging

---

## Winner Selection Protocol

After all tracks produce results, evaluate using a weighted matrix:

| Criterion | Weight | Measure |
|-----------|--------|---------|
| **Correctness** | 30% | Does it solve the problem completely? |
| **Reliability** | 25% | Will it work consistently in production? |
| **Performance** | 20% | Speed, efficiency, resource usage |
| **Readability** | 15% | Can it be maintained and extended? |
| **Elegance** | 10% | Is the solution clean and well-designed? |

**Tiebreaker Rules** (in order):
1. Higher correctness score wins
2. Higher reliability score wins
3. Fewer dependencies wins
4. Fewer lines of code wins

**Merge Protocol**: If Track 1 wins on reliability but Track 3 has a clever optimization, merge the optimization into Track 1's architecture. Best parts of each.

---

## Integration Points

- **Triggered by**: `directives/intent-pipeline.md` Stage 3 (complexity = complex/swarm-worthy)
- **Execution tools**: `execution/parallel_swarm.py`, `/parallel-swarm` workflow
- **Quality gate**: Each track's output runs through `directives/quality_gate.md` before winner selection
- **Referenced from**: GEMINI.md/CLAUDE.md/AGENTS.md Operating Principles

---

## Example: When This Fires Automatically

User says: "Build me an email enrichment script that finds business emails from company names."

**Router classifies**: Complex (build task, multiple API options, trade-offs exist)
**Parallel Thought activates**:
- Track 1: Hunter.io single-API approach (proven, simple)
- Track 2: Multi-API cascade with fallbacks (balanced)
- Track 3: Async batch processing with intelligent caching (maximum throughput)

**I present**: "I see 3 viable approaches with different trade-offs. Here's my recommendation..." and let user pick or trust the winner selection matrix.

---

## Usage Tracking

> **Purpose**: Detect dead infrastructure. If this directive hasn't fired in 30 days, it should be reviewed for relevance or archived.

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-03-19 |

**Update Rule**: When this protocol fires (either mode), update the "Last Activated" date and increment the count. If the 30-day review date passes with 0 activations, flag for archival review.

---

*Created: 2026-02-17 | Rimuru Protocol v1.1 — Post-Roundtable*
