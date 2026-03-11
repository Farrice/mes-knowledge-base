---
description: Session kickoff protocol — declare active protocols at conversation start for complex tasks
---

# Session Kickoff Protocol

> **Purpose**: Make protocol compliance visible. At the start of any complex conversation (estimated 3+ tool calls), declare which protocols are active and why.

## When to Run

**Always run for:**
- Multi-step builds or creative projects
- Research or intelligence tasks
- Strategy, decisions, or multi-domain requests
- Any `/big-project`, `/swarm`, `/roundtable` invocation

**Skip for:**
- Quick factual questions (1-2 tool calls)
- Bug fixes or corrections
- Simple file reads or lookups
- User explicitly says "just do it"

## The Kickoff Block

Present this at the start of work (after initial planning, before execution):

```
## 🚀 Session Kickoff

**Task Type Detected**: [Creative / Research / Strategy / Build / Debug]
**Complexity**: [Light (1-5 tools) / Medium (5-20 tools) / Heavy (20+ tools)]

**Active Protocols**:
- ✅ Expert Routing — [which experts detected]
- ✅ Quality Gate — post-output check
- ✅ Intent Refiner — [sharpness score X/5]
- ⏭️ Parallel Thought — [reason for skip, e.g. "single approach sufficient"]
- ⏭️ Perplexity — [reason for skip, e.g. "no research needed"]

**Session Plan**: [1-2 sentence summary of approach]

Ready to go.
```

## Rules

1. **Only show protocols that are relevant** — don't list all 5 every time
2. **Be honest about skips** — saying "skipped because X" is more useful than silently not using it
3. **If Heavy complexity detected** — recommend `/big-project` workflow
4. **Update if scope changes** — if a "Light" task turns "Heavy" mid-session, re-declare

## Integration with Big Project Workflow

When `/big-project` is invoked, the kickoff block is mandatory and expanded to include:
- Session boundary planning (when to suggest new conversation)
- Per-batch quality gate schedule
- Checkpoint strategy

## Usage Tracking

> **Purpose**: Detect dead infrastructure. If this directive hasn't fired in 30 days, it should be reviewed for relevance or archived.

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-03-19 |

**Update Rule**: When this protocol fires, update the "Last Activated" date and increment the count. If the 30-day review date passes with 0 activations, flag for archival review.

---

*Created: 2026-02-17 | Session Kickoff Protocol v1.0*
