# /qa-review — Multi-Agent QA Code Review

Deploy the full QA review council against a PR or code change.
5 specialized agents run in parallel, synthesize findings,
and produce a unified review with severity-ranked findings.

## Usage

```
/qa-review [PR number or file path]
/qa-review --focus "selectors,flakiness" tests/claims-processing.spec.ts
/qa-review --agents "playwright,standards" tests/login.spec.ts
```

## Steps

### Step 1 — Load the Code

Read the PR diff or specified file(s). Extract:
- All `.spec.ts` / `.test.ts` files changed
- All page object files changed
- All fixture/data files changed
- The commit message and PR description

### Step 2 — Route to Agents

Scan invocation cards. Default: load ALL 5 agents for full review.
If `--focus` specified, load only matching agents.
If `--agents` specified, load only named agents.

### Step 3 — Parallel Execution

Fire all selected agents simultaneously. Each agent receives:

**System instruction**: Their full AGENT.md (persona + methodology)
**Input**: The code diff + file contents
**Mandate**:
- Apply your specific review framework
- Use severity ratings: 🔴 Critical, 🟡 Warning, 🟢 Suggestion
- Include specific line numbers
- Provide fix code, not just descriptions
- Flag any handoff triggers

### Step 4 — Handoff Resolution

Check each agent's output for handoff triggers:
- Playwright → Flakiness: timing issues found
- Standards → Security: credential exposure
- Any → Test Architecture: structural concerns

For each triggered handoff:
1. Pass the finding + context to the receiving agent
2. Receiving agent adds its assessment
3. Merge into the original finding (enriched, not duplicated)

### Step 5 — Synthesis

Produce unified review:

```markdown
# QA Code Review: [PR/File]

## Summary
- 🔴 Critical: [N] findings
- 🟡 Warning: [N] findings
- 🟢 Suggestion: [N] findings
- **Reliability Score**: [X/10]
- **Merge Recommendation**: APPROVE / APPROVE WITH CHANGES / REQUEST CHANGES

## 🔴 Critical Issues (must fix before merge)

### [Issue Title]
- **Found by**: [Agent name]
- **File**: [path:line]
- **Current code**: `[snippet]`
- **Fixed code**: `[snippet]`
- **Why**: [explanation]
- **Enriched by**: [handoff agent, if applicable]

## 🟡 Warnings (should fix)
[Same format]

## 🟢 Suggestions (nice to have)
[Same format]

## Agent Provenance
| Finding | Primary Agent | Supporting Agent |
|---------|--------------|-----------------|
| ... | ... | ... |
```

### Step 6 — Quality Gate

Before delivering:
- Are all 🔴 Critical issues accompanied by fix code?
- Are findings deduplicated (no two agents flagging the same line)?
- Is the merge recommendation consistent with the findings?
- Would a developer understand every finding without asking follow-up questions?
