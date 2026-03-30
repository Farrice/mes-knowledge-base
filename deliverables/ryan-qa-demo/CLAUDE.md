# CLAUDE.md — QA Automation Code Review System

> Drop this file in the root of your Playwright test repository.
> Claude Code reads it automatically and knows how to orchestrate your agents.

---

## What This System Does

When you ask for a code review, this system deploys 5 specialized QA agents in parallel, each reviewing your test code through a different lens. Their findings are synthesized into a single prioritized review with merge recommendations.

## How to Trigger a Review

```
/qa-review tests/claims.spec.ts
/qa-review tests/              ← review all test files
"review this test file"        ← natural language works too
```

## Agent Roster

| Agent | Directory | Lens | Loads |
|-------|-----------|------|-------|
| **Playwright Specialist** | `agents/playwright-specialist/` | Selector strategy, wait patterns, assertions, Playwright API usage | AGENT.md + genius.md |
| **Corporate Standards** | `agents/corporate-standards/` | Naming conventions, description tags, forbidden patterns, PR compliance | AGENT.md + genius.md |
| **Flakiness Hunter** | `agents/flakiness-hunter/` | Timing bombs, race conditions, shared state, CI/CD reliability | AGENT.md + genius.md |
| **Security & Compliance** | `agents/security-compliance/` | PII detection, credential scanning, data classification, insurance regulations | AGENT.md + genius.md |
| **Test Architecture** | `agents/test-architecture/` | Page Object Model, fixtures, test isolation, abstraction quality | AGENT.md + genius.md |

## Review Workflow

When a review is requested:

### Step 1 — Load All Agents
Read each agent's `AGENT.md` + `genius.md` files. These contain:
- **AGENT.md**: Identity, detection patterns, severity ratings, decision framework
- **genius.md**: Deep knowledge patterns that make the agent a specialist, not a checklist

### Step 2 — Parallel Review
Deploy all 5 agents simultaneously against the target test file(s). Each agent:
1. Reads the test code
2. Applies its specific detection patterns
3. Cross-references its genius patterns for deeper findings
4. Produces findings in its defined output format

### Step 3 — Handoff Resolution
Check each agent's findings for handoff triggers:
- If Security finds PII → check Corporate Standards for specific policy numbers
- If Playwright finds bad selectors → check Test Architecture for POM recommendations
- If Flakiness finds timing issues → check Playwright Specialist for correct wait patterns

Handoffs ENRICH findings — the receiving agent adds context the originating agent doesn't have.

### Step 4 — Synthesis
Merge all findings into a single review:

```markdown
# QA Code Review: [filename]

## Merge Recommendation: 🟢 APPROVE / 🟡 APPROVE WITH COMMENTS / 🔴 REQUEST CHANGES

## Summary
- Critical: X | High: X | Medium: X | Low: X
- Reliability Score: X/10
- Compliance Score: X/10
- Architecture Score: X/10

## Critical Findings (Merge Blockers)
[From all agents, sorted by severity]

## High Priority
[From all agents]

## Medium Priority
[From all agents]

## Suggestions
[Low priority improvements]

## Agent Attribution
| Finding | Primary Agent | Enriched By |
|---------|--------------|-------------|
| ...     | ...          | ...         |
```

### Step 5 — Write Review File
Save the review to `reviews/[filename]-review-[date].md` so it can be attached to the MR/PR.

---

## Customizing for Your Organization

### Corporate Standards
Edit `agents/corporate-standards/AGENT.md` to add your company's specific:
- Naming conventions
- Forbidden patterns
- Required description formats
- Policy numbers for data handling violations

### Security Policies
Edit `agents/security-compliance/AGENT.md` to add:
- Your data classification levels (Category 1-4 or equivalent)
- Specific policy numbers and document references
- Industry-specific regulations (HIPAA, GLBA, SOC 2, state laws)
- Approved test data generators or fixture patterns

### Playwright Patterns
Edit `agents/playwright-specialist/AGENT.md` to add:
- Your team's selector strategy (getByRole vs. getByTestId)
- Custom wait patterns for your application
- Known application-specific timing issues

---

## Quick Start

1. Copy this entire folder structure into your Playwright repo root
2. Install Claude Code VSCode extension
3. Open a test file
4. Type: `/qa-review` or "review this test"
5. Watch 5 agents analyze your code in parallel
6. Get a synthesized review with merge recommendation

---

## File Structure Required

```
your-playwright-repo/
├── CLAUDE.md                          ← This file (orchestrator)
├── agents/
│   ├── _framework/
│   │   └── invocation-cards.md        ← Quick reference for all agents
│   ├── playwright-specialist/
│   │   ├── AGENT.md
│   │   └── genius.md
│   ├── corporate-standards/
│   │   ├── AGENT.md
│   │   └── genius.md
│   ├── flakiness-hunter/
│   │   ├── AGENT.md
│   │   └── genius.md
│   ├── security-compliance/
│   │   ├── AGENT.md
│   │   └── genius.md
│   └── test-architecture/
│       ├── AGENT.md
│       └── genius.md
├── workflows/
│   └── qa-code-review.md             ← Detailed review workflow
├── tests/
│   └── (your test files)
└── reviews/
    └── (generated review files)
```
