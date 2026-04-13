# Context Bloat Diagnostic

> Systematic audit of context usage across any agentic system. Produces a full bloat map with compression prescriptions ranked by impact.

## Prerequisites
- Access to the target system's prompt/instruction files
- Token counting capability (or `wc -c` for byte approximation)
- List of all tool definitions loaded per invocation
- Sample of 5-10 representative task interactions

## Steps

### Step 1 — Measure Total Context Footprint
For each component in the system prompt/context:
1. **System instructions** (GEMINI.md, rules, guardrails) — count tokens
2. **Skill context** (SKILL.md, genius.md, workflows loaded) — count tokens
3. **Tool definitions** (all available tool schemas) — count tokens
4. **Conversation history** (prior turns, summaries, state) — count tokens
5. **Dynamic context** (search results, file contents, retrieval) — count tokens

Record totals and percentages. Target output:
```
Component          | Tokens | % of Total
System instructions| 3,200  | 18%
Skill context      | 4,800  | 27%
Tool definitions   | 6,400  | 36%
Conversation       | 2,100  | 12%
Dynamic context    | 1,200  | 7%
TOTAL              | 17,700 | 100%
```

### Step 2 — Map Duplication
Search for instructions or rules that appear in multiple locations:
- Same rule in system prompt AND skill files?
- Same guardrail defined in multiple agent profiles?
- Tool descriptions repeated in schemas AND in prose instructions?

Score each duplicate:
- **Exact duplicate**: Remove entirely from one location
- **Near duplicate**: Merge into single authoritative statement
- **Contextual variant**: Keep both if context genuinely differs

### Step 3 — Attention Value Scoring
For each section of loaded context, estimate its attention value:
- **High**: Directly referenced in agent outputs, critical guardrails that prevent failures
- **Medium**: Referenced sometimes, provides useful but not essential framing
- **Low**: Rarely or never influences outputs, decorative formatting, verbose examples

Score each section 1-5. Sections scoring ≤2 are compression candidates.

### Step 4 — "Lost in the Middle" Check
Take the system's current full context and place a distinctive, novel instruction in positions:
- Top (first 10% of context)
- Middle (40-60% of context)
- Bottom (last 10% of context)

Run identical tasks and check compliance with the positioned instruction. If middle placement shows significantly lower compliance than top/bottom, the system has "lost in the middle" vulnerability. This means critical instructions should be relocated to top or bottom positions.

### Step 5 — Produce Diagnostic Report
For each component, prescribe a compression action:

| Component | Current Tokens | Attention Score | Prescription | Expected Savings |
|-----------|---------------|-----------------|-------------|------------------|
| [name]    | [count]       | [1-5]           | [action]    | [tokens/pct]     |

### Step 6 — Prioritize by Impact
Rank all prescriptions by (expected token savings × ease of implementation):
1. Highest impact + lowest effort first
2. Group by compression vector (deduplication, eviction, formatting, tiering, retrieval)
3. Produce a prioritized sprint backlog

## Output Format
Deliver as a structured artifact with:
- Executive summary (total tokens, biggest offenders, overall health score 1-10)
- Component-by-component breakdown table
- Duplication map with merge prescriptions
- Attention value scores
- Lost-in-the-middle test results
- Prioritized compression sprint backlog
- Expected total reduction estimate (tokens saved, % reduction)
