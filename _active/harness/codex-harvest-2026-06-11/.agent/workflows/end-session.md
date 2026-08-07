---
description: End the session with handoff, automatic evidence capture, routing feedback, and local-first intelligence logging
---

# /end-session - Session Handoff And Intelligence Closeout

> **Purpose**: Generate a clean handoff for the next session and automatically capture the evidence the system needs to improve. Deep cleanup is optional; intelligence capture is the default.

## Operator Core Alignment

This workflow is the canonical source of truth for End-session behavior. Global
and local End-session wrappers must stay thin compatibility wrappers that point
back here, not competing behavior contracts.

Preserve these invariants:

- `/end-session` owns whole-session closeout, retrieval handoff, and closeout intelligence capture.
- It is not `/handoff` for a focused transfer packet and not `/steering-compass` for standalone next-prompt coaching.
- Meaningful closeouts include session naming metadata, a concise handoff, `3 Next Prompts`, and an `Operator Lesson`.
- Closeout intelligence runs through `python3 execution/session_closeout_intelligence.py run --source end-session`.
- Conversation indexing uses the safe `python3 execution/conversation_index.py stats` check before any rebuild.
- Optional cleanup must be reviewed; never publish, push, broadly delete, or perform destructive cleanup without explicit approval.
- Real Codex subagents require explicit authorization.

## Usage

```
/end-session              # Quick handoff (default)
/end-session --deep       # Full cleanup + handoff
```

## Quick Handoff (Default)

### 1. Generate Handoff Summary
// turbo
Output the handoff block:

```markdown
## Session Name
**Recommended title:** [Domain]: [Specific Object] - [Outcome]
**Slug:** yyyy-mm-dd-[domain]-[object]-[outcome]
**Keywords:** [5-8 searchable terms]

## Session Handoff
**Completed:** [2-3 bullet points of what was built]
**Remaining priority:** [Next immediate task]
**Core context to load:** [Paths to the 2-3 essential deliverable files]
**Hot experts this session:** [List of experts loaded — so next session can warm-start]

## 3 Next Prompts
1. **[Path Name]**
   - **When to use:** [condition that makes this the right continuation]
   - **Why this is recommended:** [leverage, risk, or learning]
   - **Prompt:** [copy-paste continuation prompt]
   - **Expected output:** [what gets produced]
   - **Quality bar:** [what makes it worth shipping]
   - **Skip if:** [when this would be overkill or wrong]
   - **Suggested skills/workflows:** [exact routes]

## Operator Lesson
- **What I noticed:** [missed leverage, bottleneck, or useful pattern]
- **Better system move:** [route, workflow, reuse, or delegation move]
- **Next-time prompt:** [paste-ready wording for the next similar request]
- **Agent/Workflow I'd use:** [/route or skill for the next meaningful step]
- **Subagent worth it?:** [yes/no and why; real Codex subagents still need explicit authorization]
- **Reuse hook:** [where this should become an asset, memory, workflow, offer, or next artifact]
```

Use `semantic_libraries/antigravity/primitives/collaborative-steering-compass.md` and `semantic_libraries/antigravity/references/no-lazy-path-gate.md` to keep the three prompts dense, practical, and non-generic. Skip the three-prompt block only for Light sessions with no artifact, decision, or system change. When helpful, ground the prompts with `python3 execution/contextual_next_prompts.py --objective "[current objective]"`.

### 2. Run Closeout Intelligence
// turbo
Run the end-session intelligence loop so meaningful work, routing evidence, route feedback, health snapshots, and review inboxes update without manual retyping:
```bash
python3 execution/session_closeout_intelligence.py run --source end-session
```

High-confidence performance entries commit to `.agent/performance-log.jsonl`; uncertain performance entries go to `.agent/performance-log-inbox.jsonl`. Explicit route feedback commits to `.agent/routing-intelligence.json`; ambiguous route/failure signals go to `.agent/routing-feedback-inbox.jsonl`.

### 3. Update Conversation Index
// turbo
Use a safe index check that does not require guessing the hidden current conversation id:
```bash
python3 execution/conversation_index.py stats
```

If the stats look stale or the user asks for a rebuild, run:
```bash
python3 execution/conversation_index.py build
```

### 3.5 Artifact Organization Check
// turbo
For any new or changed substantial artifact paths from the session, run:

```bash
python3 execution/artifact_router.py enforce "[artifact path]"
python3 execution/artifact_frontmatter_guard.py "[artifact path]"
```

If multiple paths were produced, pass them in one command. If enforcement fails, include the proposed destination or inbox status in the handoff instead of pretending the workspace is clean.

### 4. Git Checkpoint (Optional)
// turbo
If the workspace is a Git repo, offer to commit:
> "Want me to commit? `git add . && git commit -m 'Session: [Label]'`"

Do not push without explicit confirmation.

---

## Deep Cleanup (`--deep`)

Run all steps above, plus:

### 3. Artifact Triage
Identify files in the current session's `brain/` directory:
- **Delete**: Temp extractions, raw data dumps, rough drafts
- **Keep**: Final offer docs, finished skills, deliverables

### 4. Finalize Session Workspace
// turbo
If a session workspace exists:

```bash
python3 execution/session_workspace.py finalize
```

### 5. File Organization
// turbo
- Run `python3 execution/artifact_router.py inventory`
- Run `python3 execution/artifact_router.py plan`
- Apply only reviewed safe moves with `python3 execution/artifact_router.py apply --plan "[plan path]"`
- Move intermediates to `.tmp/`
- Ensure deliverables are properly named
- Consolidate fragmented notes into canonical files

### 6. State Check
- Read `task.md`, mark completed items, roll over uncompleted items

---

## When to Use
- **Quick Handoff**: End of any session — costs almost nothing
- **Deep Cleanup** (`--deep`): After heavy sessions (extractions, multi-expert work, client deliverables)
- Skip entirely if the session was conversational with no artifacts produced

## Verification

After changing this workflow, run:

```bash
python3 execution/sync_operator_core_end_session.py --check
python3 execution/verify_operator_core_end_session.py
python3 execution/verify_end_session_intelligence.py
python3 execution/validate_skill.py source-command-end-session
```
