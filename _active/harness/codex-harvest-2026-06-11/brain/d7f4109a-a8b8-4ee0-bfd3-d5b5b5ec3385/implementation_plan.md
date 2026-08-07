# Claude Code 1M Context & Loop Caching Mitigations

This implementation plan addresses systemic high-velocity token burn and context-hoarding loops experienced in the Antigravity system caused by known bugs in Claude Code's prompt caching.

## Problem Description
Deep research via Perplexity indicates several distinct bugs in Claude Code's caching architecture, particularly regarding the 1M token context window:
1. **Tool-Use Session Resume Bug:** When resuming a session, Claude Code invalidates prompt caching for previously read files (cache ratio drops from 99% to 26%), forcing an expensive re-read of all context.
2. **Subagent / Loop Corruption:** Long-running operations or subagent loops (~24 mins+) corrupt the internal caching structure, causing responses from unrelated contexts and breaking prefix reuse.
3. **The `/clear` Persistence Bloat:** Running `/clear` fails to completely wipe file and branch state, maintaining a hidden bloat that contributes to 0-cache hits on loops.
4. **Model Pinning Failures:** Caching regularly breaks entirely on Claude 4 models but is more stable on pinned Claude 3.7 Sonnet versions.

## Proposed Changes

To armor Antigravity against these upstream bugs, we will modify the system's core orchestration and state directives.

---

### Directives

#### [MODIFY] [token-efficiency-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/token-efficiency-protocol.md)
Add a new **Rule 7: Upstream Claude Code Mitigations** that dictates:
- **Never use `/clear`:** Require hard restarts (`^C` then relaunch `claude`) instead of `/clear` to truly wipe token bloat.
- **Model Pinning:** Explicitly advise pinning `ANTHROPIC_MODEL='claude-3-7-sonnet-20250219'` if cache hit ratios fall to zero.
- **Pre-emptive Compaction:** Provide guidelines around running `/compact` *before* the 80% mark of the 1M context limit.

#### [MODIFY] [session-state-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/session-state-protocol.md)
Update the execution protocol to account for the **Session Resume Bug**:
- Under **When to Read**, add rules specifying that resuming a session should rely *exclusively* on `.agent/session-state.md` and Hot Context caches.
- **Anti-Pattern Addition:** Explicitly state that executing batch tool reads (`view_file` etc.) immediately upon session resume will shatter existing cache alignment. Files should be loaded in early continuous blocks, and session restoration should be heavily bottlenecked through `session-state.md` text rather than triggering direct file queries.

---

## User Review Required

> [!WARNING]
> These changes are workarounds for **upstream bugs in Anthropic's CLI**. Once Anthropic ships patches (e.g., in GitHub issues #27048, #2538), these mitigations can be relaxed.

**User Decisions Needed:**
1. Do you want me to automatically implement the proposed changes to `token-efficiency-protocol.md` and `session-state-protocol.md`?
2. Are you concurrently using a `.env` configured `export CLAUDE_CODE_USE_BEDROCK=1` or another API wrapper that we should account for?

## Verification Plan

### Manual Verification
- After updates, review `token-efficiency-protocol.md` and `session-state-protocol.md` to ensure the Claude Code mitigations align with the Antigravity system logic.
- Run a typical Antigravity task chain. Monitor token consumption logs inside Claude Code (`/cost` or terminal output) to ensure caching stays >80% after manual `/compact` and that session resumption doesn't trigger 1M-token baseline re-reads.
