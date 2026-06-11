# Token Efficiency Overhaul — Three Moves

Reduce token waste by 30-50% on routine tasks without losing any system capability. Three targeted modifications to session ceremony, Chain execution, and context loading.

## Proposed Changes

### Move 1: Tiered Kickoff — Sport Mode / Race Mode

Replace the monolithic `/session-kickoff` (always 10+ tool calls) with two modes that auto-select based on complexity.

---

#### [MODIFY] [session-kickoff.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/session-kickoff.md)

**Sport Mode** (default — 3 tool calls max):
1. Generate conversation label (in-head, no file read)
2. Create workspace folder via `session_workspace.py create` — but **deferred**: only runs when the first asset is actually produced
3. Begin work immediately — no protocol declarations, no system health check, no intent pipeline file read

**Race Mode** (explicit `@session-kickoff --deep` or auto-triggered for Heavy complexity):
- Full current ceremony: label → workspace → detect complexity → declare protocols → score intent → begin work
- Auto-trigger conditions: extraction workflows, parallel swarms, client deliverables, `/big-project`

**What changes in the file**:
- Add `## Mode Detection` section at the top that checks for `--deep` flag or Heavy-trigger keywords
- Wrap Steps 2-4 in a conditional that only fires for Race Mode
- Add deferred workspace creation: workspace folder is created on first `log-asset` call, not at kickoff
- Streamline the Sport Mode output to a single compact line: `🏎️ Sport Mode | [Label] | Ready.`

---

#### [MODIFY] [end-session.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/end-session.md)

Replace the 7-step ceremony with **ambient logging** — session state accumulates naturally during work, so there's nothing to "clean up" at the end.

**What changes**:
- Steps 1-3 (Artifact Triage, Workspace Finalize, File Organization) → become **optional**, triggered only by `@end-session --deep`
- Step 4 (System Health Pulse) → removed from end-session (it belongs in a dedicated `/health-check`)
- Step 5 (Git Checkpoint) → kept, since it's already optional
- Step 6 (Handoff Summary) → **always runs** — this is the one piece that's always worth the tokens (3-4 lines of output)
- Step 7 (Execution Offer) → removed (the triage plan description burns tokens describing cleanup before doing cleanup)

**New default end-session**: Just produce the handoff summary. 1-2 tool calls. The workspace is already organized because assets are logged when they're created, not retroactively.

---

#### [MODIFY] [session_workspace.py](file:///Users/farricecain/Google%20Antigravity/execution/session_workspace.py)

Add a `create-if-needed` command that combines workspace creation + asset logging in a single call. This supports deferred workspace creation — the folder only materializes when there's actually something to put in it.

```python
def cmd_create_if_needed(domain, label, file_path, asset_type, description, conv_id=None):
    """Create workspace on first asset, then log the asset."""
    session = find_latest_session()
    # If no session exists today for this domain, create one
    if not session or not _matches_current_session(session, domain):
        session = cmd_create(domain, label, conv_id)
    cmd_log_asset(file_path, asset_type, description, str(session))
```

---

### Move 2: Internalize the Chain's Lightweight Steps

Steps 1-2 (SCORE + SHARPEN) should not require file reads. The scoring logic is simple pattern matching that the AI should do in-head.

---

#### [MODIFY] [GEMINI.md](file:///Users/farricecain/Google%20Antigravity/GEMINI.md) + [CLAUDE.md](file:///Users/farricecain/Google%20Antigravity/CLAUDE.md) + [AGENTS.md](file:///Users/farricecain/Google%20Antigravity/AGENTS.md)

Add a new section after "The Chain" called **"Chain Efficiency Rules"**:

```markdown
### Chain Efficiency Rules (Token Optimization)

**Steps 1-2 (SCORE + SHARPEN): Internalized — no file reads required.**
The scoring formula (+1 Deliverable, +1 Audience, +1 Context, +1 End state, +1 Specific language) 
is memorized. Do NOT read `directives/intent-pipeline.md` to score intent. 
Only read it if running `/validate-intent` explicitly.

**Step 3 (ROUTE): Internalized for known domains.**
If the domain maps to an obvious expert (LinkedIn → Lara Acosta, copywriting → Luke Iha, 
SEO → Nathan Gotch, brand → Oren/Grace), route without reading `DOMAIN_REGISTRY.md` or 
`invocation-cards.md`. Only read routing files for ambiguous or multi-domain requests.

**Step 4 (LOAD): Deferred Tier escalation.**
Start at Tier 1 (SKILL.md only). Load genius.md ONLY if:
- The first-pass output doesn't meet quality expectations
- The task is explicitly creative/complex (screenwriting, brand strategy, deep extraction)
- The user asks for "the best" or "world-class" output

**Step 6 (FINALIZE): Required only for expert-domain output.**
Quick answers, system commands, file organization, and conversations do NOT require finalize.
```

This changes behavior, not files (mostly). The key file change is adding the section above to prevent future drift.

---

#### [MODIFY] [token-efficiency-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/token-efficiency-protocol.md)

Add a new **Rule 5: Chain Step Internalization**:

```markdown
## Rule 5: Chain Step Internalization

**Steps 1-3 of The Chain should be executed in-head, not via file reads.**

| Step | Old Behavior | New Behavior | Savings |
|------|-------------|--------------|---------|
| 1. SCORE | Read intent-pipeline.md | Internalized formula | ~500 tokens |
| 2. SHARPEN | Read intent-pipeline.md Stage 2 | Ask directly if needed | ~500 tokens |
| 3. ROUTE | Read DOMAIN_REGISTRY.md + invocation-cards.md | Internalized for known domains | ~1,200 tokens |

Total per-request savings: ~2,200 tokens for routine tasks.
```

---

### Move 3: Hot Context Cache

Prevent redundant expert file reads within a single conversation.

---

#### [MODIFY] [session-state-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/session-state-protocol.md)

Add a new section: **"Hot Context Stack"**

```markdown
## Hot Context Stack

When an expert is loaded during a conversation (Tier 1+ file read), add them to the 
Hot Context Stack. This is maintained in-memory (no file write needed).

**Format** (tracked mentally by the AI):
- Expert loaded: [name]
- Files read: [SKILL.md, genius.md, workflow X]
- Tier level: [1, 2, or 3]
- Key patterns retained: [list 2-3 core patterns]

**Rules**:
1. Before loading any expert, check if they're already hot
2. If hot at Tier 1 and Tier 2 is needed, only read genius.md (incremental load)
3. If hot at Tier 2, skip all file reads — the expert is fully loaded
4. Hot status persists for the entire conversation (cleared on new conversation)
5. Write hot experts to session-state.md so they survive compaction

**Anti-pattern**: Re-reading SKILL.md for the same expert twice in one conversation.
This wastes ~1,350 tokens per redundant load.
```

---

#### [MODIFY] [GEMINI.md](file:///Users/farricecain/Google%20Antigravity/GEMINI.md) + [CLAUDE.md](file:///Users/farricecain/Google%20Antigravity/CLAUDE.md) + [AGENTS.md](file:///Users/farricecain/Google%20Antigravity/AGENTS.md)

Update the Context Engine table to include Hot Context:

```markdown
| Tier | What to Read | Token Cost | When |
|------|-------------|-----------|------|
| **Hot** | Nothing (already loaded) | 0 | Expert was loaded earlier this conversation |
| **0 — Card** | invocation-cards.md | ~80 | Routing, ensemble selection |
| **1 — Standard** | SKILL.md + workflow | ~1,350 | Single expert, clear task |
| **2 — Deep** | SKILL.md + genius.md + workflow | ~2,550 | Creative/complex work |
| **3 — Sub-Agent** | Spawn sub-agent | ~300 main | Multi-expert, 10+ files loaded |
```

---

## Summary of Token Impact

| Move | Where Savings Come From | Est. Savings |
|------|------------------------|-------------|
| **Tiered Kickoff** | Sport Mode skips 7+ tool calls, end-session skips 5+ | 15-20% of daily burn |
| **Internalized Chain** | Steps 1-3 skip file reads on known domains | 30-50% per routine request |
| **Hot Context Cache** | No redundant expert loads within a conversation | 20-40% on multi-workflow sessions |

**Combined effect**: 30-50% reduction in token consumption for typical daily usage, with zero capability loss. Every workflow, expert, and quality gate remains fully available — they're just loaded smarter.

---

## Verification Plan

> [!IMPORTANT]
> This system is an AI orchestration layer, not a traditional app. There are no automated tests. Verification is behavioral — confirming the AI follows the new protocols correctly.

### Manual Verification (Next Session)

1. **Sport Mode Test**: Start a new conversation with a simple request (e.g., "write me a LinkedIn hook"). Confirm:
   - No protocol declarations appear
   - No `intent-pipeline.md` is read
   - No system health check runs
   - Work begins within 1-2 tool calls
   - Workspace folder is NOT created until an asset is produced

2. **Race Mode Test**: Start a new conversation with `/session-kickoff --deep` or an extraction request. Confirm:
   - Full ceremony runs (label → workspace → protocols → intent scoring)
   - This should feel identical to the current behavior

3. **Internalized Chain Test**: In a Sport Mode session, ask for a LinkedIn post. Confirm:
   - Intent is scored in-head (no file read for `intent-pipeline.md`)
   - Routing goes directly to Lara Acosta (no read of `DOMAIN_REGISTRY.md`)
   - SKILL.md is loaded, genius.md is NOT loaded on first pass

4. **Hot Context Test**: In the same session, ask for a second LinkedIn post. Confirm:
   - Lara Acosta's SKILL.md is NOT re-read
   - The expert is recognized as "hot" and context is reused
