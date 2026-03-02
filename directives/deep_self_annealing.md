# Deep Self-Annealing Protocol

> **Purpose**: Replaces the basic "retry once" self-annealing loop with a tiered recovery system that makes the system permanently stronger after every failure.
> **Supersedes**: The 5-step self-annealing loop in GEMINI.md Operating Principles (which remains as a summary; this directive is the full protocol).
> **Reference**: `skills/nick-saraev-agentic-workflows/references/prompts/crown_jewel_02_self_annealing_architect.md`

---

## Core Principle

> Every error is diagnostic data. The system doesn't just recover — it evolves. A failure that happens twice is a system design failure, not a runtime error.

---

## Tiered Recovery System

### Tier 1: Auto-Fix (Silent)
**Scope**: Predictable, low-risk errors that have known solutions.

| Error Type | Auto-Fix Action |
|-----------|----------------|
| Missing import | Add the import, re-run |
| Syntax error | Fix syntax, re-run |
| File not found (expected path) | Check alternative paths, retry |
| Simple API error (400 with clear message) | Fix the request per error message, retry |
| Rate limit (429) | Wait, backoff, retry |

**Rules**:
- Fix silently — user sees nothing
- Maximum 2 auto-fix attempts per error
- If the same error recurs after fix → escalate to Tier 2

---

### Tier 2: Diagnose & Document
**Scope**: Errors requiring root cause analysis. The fix may not be obvious.

| Step | Action |
|------|--------|
| 1. **Capture** | Full error message, stack trace, input that caused it |
| 2. **Ingest Context** | Load the entire source code file, related `SKILL.md`/`AGENT.md`, and full conversation context into Gemini 3.1 Pro High. |
| 3. **Deep Diagnosis** | Prompt Gemini 3.1 Pro High to perform root cause analysis across the full ingested context. |
| 4. **Fix** | Apply the targeted structural fix recommended by the model. |
| 5. **Verify** | Re-run to confirm the fix works |
| 6. **Document** | Add a "Lesson Learned" entry to the relevant directive |

**Lesson Learned Format** (append to the relevant directive):
```markdown
### Lesson: [Error Title] — [Date]
- **Trigger**: [What caused the error]
- **Root Cause**: [Why it happened]
- **Fix**: [What resolved it]
- **Prevention**: [How to avoid it in the future]
```

**Rules**:
- User sees nothing unless the fix changes the output meaningfully
- Maximum 1 diagnosis cycle — if the fix doesn't work, escalate to Tier 3
- Always document, even if the fix was simple in hindsight

---

### Tier 3: Escalate to User
**Scope**: Errors that require human judgment, credentials, or external action.

| Error Type | Escalation Template |
|-----------|-------------------|
| Authentication failure | "🔐 Auth failed for [service]. Need: [specific credential or token refresh]" |
| Missing credentials | "🔑 Missing [KEY_NAME] in .env. I need this to proceed." |
| Breaking API change | "⚠️ [API] changed their response format. Here's what changed: [diff]. Proposed fix: [approach]" |
| Persistent failure (2+ retries) | "🔴 [Task] failed after 2 attempts. Root cause: [diagnosis]. Options: [A/B/C]" |
| Paid API call needed | "💰 This fix requires calling [API] which costs [estimate]. Proceed?" |

**Rules**:
- Always include your diagnosis and proposed fix — never just say "it broke"
- Present options when multiple fixes exist
- Halt the workflow; do not continue past the failure point

---

## Permanent Learning Protocol

The difference between "retry" and "self-anneal" is that self-annealing makes the system *permanently stronger*. Every Tier 2+ failure must produce a lasting artifact:

| Artifact | Where | What |
|---------|-------|------|
| **Lesson Learned** | Relevant `directives/*.md` | Error details + prevention steps |
| **Error Handler** | Relevant `execution/*.py` | Try/except block for the specific failure mode |
| **Edge Case** | `directives/*.md` edge cases section | Documented boundary condition |

**The Standard**: If the same error can happen twice without the system catching it earlier, the self-annealing protocol failed.

---

## Checkpoint Pattern (Multi-Step Workflows)

For workflows with 3+ sequential steps, implement checkpointing so recovery doesn't restart from scratch:

```
Step 1: Fetch data → checkpoint ✓
Step 2: Process data → checkpoint ✓
Step 3: Upload results → FAIL
Recovery: Resume from Step 3 checkpoint, not Step 1
```

**Implementation**: Use `execution/checkpoint_manager.py` for file-based checkpoints. Key functions:
- `save_checkpoint(workflow_name, step, data)` — persist state after each step
- `load_checkpoint(workflow_name)` — resume from last successful step
- `clear_checkpoint(workflow_name)` — clean up after successful completion

---

## Integration Points

- **Replaces**: The "Self-annealing loop" summary in Operating Principles (summary remains, this is the full protocol)
- **Works with**: `directives/quality_gate.md` (quality failures follow this recovery protocol)
- **Works with**: `directives/workflow-chains.md` (chain failures follow tiered recovery)
- **Referenced from**: GEMINI.md/CLAUDE.md/AGENTS.md Operating Principles
- **Checkpoint tool**: `execution/checkpoint_manager.py`

---

## Quick Reference: Which Tier?

```
Error occurred
  ├── Known fix exists? → Tier 1 (Auto-Fix)
  ├── Root cause diagnosable? → Tier 2 (Diagnose & Document)
  └── Needs human judgment/credentials? → Tier 3 (Escalate)
```

---

## Usage Tracking

> **Purpose**: Detect dead infrastructure. If this directive hasn't fired in 30 days, it should be reviewed for relevance or archived.

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-03-19 |

**Update Rule**: When this protocol fires (any Tier), update the "Last Activated" date, increment the count, and note which Tier was triggered.

---

*Created: 2026-02-17 | Deep Self-Annealing Protocol v1.0*
