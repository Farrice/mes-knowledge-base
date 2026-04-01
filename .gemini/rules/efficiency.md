# Token Efficiency Rules

> Prevent wasted context through redundant file reads and unnecessary ceremony.

## Steps 1-2 (SCORE + SHARPEN): Internalized

The scoring formula (+1 Deliverable, +1 Audience, +1 Context, +1 End state, +1 Specific language) is memorized. Do NOT read `directives/intent-pipeline.md` to score intent.
Only read it if running `/validate-intent` explicitly.

## Step 3 (ROUTE): Internalized for Known Domains

If the domain maps to an obvious expert, route without reading `DOMAIN_REGISTRY.md` or `invocation-cards.md`. Only read routing files for ambiguous or multi-domain requests.

## Step 4 (LOAD): Deferred Tier Escalation

Start at Tier 1. Escalate only when needed. See `context-engine.md` for Hot Context rules.

## Step 6 (FINALIZE): Required Only for Expert Output

Quick answers, system commands, file organization, and conversations do NOT require finalize.

## Tool Call Discipline

⛔ **NEVER MIX TOOL CALLS WITH TEXT OUTPUT IN THE SAME RESPONSE.**
Each response is EITHER tool calls OR text — never both. This prevents crashes.
Most common crash: tool call mixed with text in same response. Keep them separate.

## Checkpoint Discipline

- **Print checkpoints** after Steps 1, 3, 4, 6
- **Write session state** after Step 4, after major decisions, after 7+ file reads
