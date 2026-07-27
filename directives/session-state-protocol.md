# Session State Anchor Protocol

> Prevent context drift after compaction. Write checkpoints to `.agent/session-state.md` at key moments. Re-read anchor after compaction to recover precision.

---

## Anchor Format

```markdown
# Session State Anchor
> Last updated: [ISO timestamp]

## Active Task / ## Intent (Validated) / ## Decisions Made / ## Experts Deployed
## Hot Context Stack / ## Key Findings / ## Files Created/Modified / ## Current Phase / ## Next Steps
```

---

## Hot Context Stack Rules
1. Before loading expert → check Hot Context Stack
2. Hot at T1, need T2 → only read `genius.md` (incremental)
3. Hot at T2 → skip all reads, fully loaded
4. Hot status persists entire conversation
5. Write hot experts to anchor so they survive compaction
Anti-pattern: Re-reading SKILL.md for same expert = ~1,350 wasted tokens.

---

## When to Write

| Trigger | What to Anchor |
|---------|---------------|
| After intent validation | Validated intent |
| After major analysis | Key findings + methodology |
| After expert deployment | Experts, patterns, outputs |
| After user decision | Decision + rationale |
| Before sub-agents | Current state |
| 10+ file reads in session | Preemptive anchor |

## When to Read
After compaction | After sub-agent return | Session resume | Decision uncertainty

---

## 3-Mode Compaction

| Situation | Mode |
|-----------|------|
| Sub-agent spawn / topic change | **Full** — All 9 sections, replaces all context. Keep last 3-5 user messages verbatim. |
| Same task, early context stale | **Partial Older** — Summarize turns 1 to N-8, keep last 8 verbatim. Most common. |
| User pivoted directions | **Partial Recent** — Keep old context, summarize new direction with pivot trigger. |

### Preservation Rules (All Modes)
Always survive: user decisions + rationale, file paths + line numbers, expert names + outputs, code <20 lines, error messages + resolutions, current chain step.
Safely compressed: reasoning chains, tool metadata, intermediate research, greetings.

### Anti-Pattern
Paraphrasing flow ("We discussed X, then Y") loses specifics. Instead: "Decided: X over Y because Z. Files: `path/file.py` modified lines 45-80."

---

## Execution Integration
`execution/checkpoint_manager.py`: `save_session_state(state)` / `load_session_state()`. Graceful failure: if no file, fall back to compacted summary.

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-07-27 (chain_runner session checkpoint) |
| **Activation Count** | 745 |
| **30-Day Review Date** | 2026-08-26 |

*Created: 2026-02-27 | Compressed: 2026-04-13*
