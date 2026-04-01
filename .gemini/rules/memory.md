# Memory, Session State & Recovery

> Survive compaction. Recover gracefully. Never lose thread.

## Session State Anchors

Write `.agent/session-state.md` at these trigger points:
- After intent validation (DICE protocol completes)
- After expert deployment (skill loaded and applied)
- After any user decision (chose direction, confirmed approach)
- When 7+ file reads have occurred in the session

## 3-Mode Compaction

When compaction is needed, **match the mode** — don't default to full:

| Situation | Mode | Effect |
|-----------|------|--------|
| Sub-agent spawn or total topic change | **Full** | All context → 9-section anchor |
| Same task, early context stale | **Partial Older** | Old summarized, recent 8 turns verbatim |
| User pivoted directions | **Partial Recent** | Old context kept, new direction summarized |

**Key rules:**
- Recent user messages (last 3-5) always survive verbatim, even in Full mode
- Decisions, file paths, and expert outputs always survive, regardless of mode
- Analysis-then-summary: internally list all facts before compressing (scan, don't paraphrase)

Script: `execution/checkpoint_manager.py` → `compact_session_state(mode, ...)` and `detect_compaction_mode()`

## Compaction Recovery

When compaction occurs (context feels thin, prior details vague):
1. Read `.agent/session-state.md` IMMEDIATELY
2. Restore hot experts, task, decisions
3. Don't reload hot experts (check Hot Context Stack)
4. Resume Chain from where you left off

## Frustration Detection

Detect and adapt to frustrated user states. Protocol: `directives/user-state-awareness.md`.

**Tier 1** (explicit: "this isn't working", "just do it", "that's wrong"):
→ Stop proposing, start executing. Skip SHARPEN + ROUTE display. Produce immediately.

**Tier 2** (implicit: very short response, repeated same request):
→ Reduce output 50%. Lead with the answer. One question max.

**Tier 3** (escalation: "forget it", "I'll do it myself"):
→ Emergency mode. Zero chain overhead. Most literal interpretation.

Script: `execution/checkpoint_manager.py` → `detect_frustration(user_message)`

## Error Recovery

- **Most common crash:** Tool call mixed with text in same response. Keep them separate — one response for tools, next response for text.
- **Script failure:** Read error → diagnose → adjust → retry once → ask user if still failing.

## Architecture Reference

**Layer 1** Directives (`directives/`) | **Layer 2** You (routing, decisions) | **Layer 3** Scripts (`execution/`)
Push complexity to scripts. You decide.

## Supporting Protocols

These fire at their trigger point within the chain:

| Protocol | Fires During | Directive |
|----------|-------------|-----------|
| Quality Assurance | Step 5 (production) | `directives/quality_assurance.md` |
| **Verification Agent** | **Step 5.5 (implementation tasks)** | **`directives/verification-agent-protocol.md`** |
| Token Efficiency | Every workflow | `directives/token-efficiency-protocol.md` |
| Session State | After Step 2, after Step 4, after 10+ reads | `directives/session-state-protocol.md` |
| **User State** | **Every turn (lightweight)** | **`directives/user-state-awareness.md`** |
| Self-Annealing | On any error | `directives/deep_self_annealing.md` |
| Collaboration | Always | `directives/collaboration-protocol.md` |
| Sub-Agent | 2+ experts loaded, or 10+ files in context | `directives/sub_agent_protocol.md` |
| Content Gate | Step 4, for content tasks | `directives/content_creation_gate.md` |

### Budget-Gated (check before calling)

| Protocol | Directive | Gate |
|----------|-----------|------|
| Perplexity | `directives/perplexity-usage-policy.md` | $30/mo, track in `.agent/perplexity-usage.json` |
| NotebookLM | `directives/notebooklm-usage-policy.md` | 100/mo, track in `.agent/notebooklm-usage.json` |
