# QA Automation Code Review — Multi-Agent System

> Built by Farrice Cain's Antigravity system. Demo for Ryan @ JDM.

## What This Is

A multi-agent AI code review system for Playwright test automation. Instead of one AI doing a single-pass review, **5 specialized agents** review your code simultaneously through different lenses, then their findings are synthesized into a single prioritized review.

## What's Inside

```
ryan-qa-demo/
├── CLAUDE.md                          ← THE BRAIN — orchestrates everything
├── README.md                          ← You're reading this
│
├── agents/                            ← 5 specialized reviewers
│   ├── _framework/
│   │   └── invocation-cards.md        ← Quick reference card for each agent
│   ├── playwright-specialist/         ← Selector strategy, waits, assertions
│   │   ├── AGENT.md
│   │   └── genius.md
│   ├── corporate-standards/           ← Naming, descriptions, forbidden patterns
│   │   ├── AGENT.md
│   │   └── genius.md
│   ├── flakiness-hunter/              ← Timing, race conditions, CI reliability
│   │   ├── AGENT.md
│   │   └── genius.md
│   ├── security-compliance/           ← PII, credentials, insurance regulations
│   │   ├── AGENT.md
│   │   └── genius.md
│   └── test-architecture/             ← POM, fixtures, isolation, abstractions
│       ├── AGENT.md
│       └── genius.md
│
├── workflows/
│   └── qa-code-review.md             ← Step-by-step review workflow
│
├── sample-tests/
│   └── claims-processing.spec.ts     ← Demo file with 13 planted issues
│
├── copilot-fallback/                  ← Works with GitHub Copilot (no Claude needed)
│   └── .github/
│       └── copilot-instructions.md
│
└── reference-architecture/            ← Farrice's full system (for study)
    ├── CLAUDE.md
    ├── agents/
    ├── skills/
    ├── execution/
    └── directives/
```

## Setup Options

### Option A: Claude Code (Full Multi-Agent System)

**Requirements:**
- VS Code
- Claude Code extension (install from VS Code marketplace)
- Anthropic API key (Claude Pro subscription includes this)

**Steps:**
1. Copy this entire folder into your Playwright repo root
2. Install Claude Code extension in VS Code
3. Open VS Code in your repo
4. Open a test file
5. In the Claude Code panel, type: `review this test file`
6. Watch 5 agents analyze in parallel

**To demo with the sample file:**
```
review sample-tests/claims-processing.spec.ts
```
This file has 13 intentional issues. The agents should find all of them.

### Option B: GitHub Copilot (Single-Pass, Works Today)

**Requirements:**
- VS Code
- GitHub Copilot subscription (you likely already have this)

**Steps:**
1. Copy `copilot-fallback/.github/copilot-instructions.md` to your repo's `.github/` folder
2. Open a test file
3. In Copilot Chat, type: `review this test file for QA standards`

This gives you a single-pass review covering all 5 domains. Less powerful than multi-agent, but works immediately with no new tools.

## How Multi-Agent Review Differs from Single-Pass

| | Copilot (single-pass) | Claude Code (multi-agent) |
|---|---|---|
| **Perspectives** | 1 (reads a checklist) | 5 (specialized experts) |
| **Handoffs** | None | Agent A's finding enriched by Agent B |
| **Example** | "SSN found in code" | "SSN found (Security) → violates Policy 4.2.1 (Corporate Standards)" |
| **Output** | Flat list of findings | Prioritized review with merge recommendation |
| **Deep knowledge** | Generic best practices | genius.md patterns from real-world QA at scale |

## Customizing for JDM

### Step 1: Corporate Standards
Edit `agents/corporate-standards/AGENT.md`:
- Replace example naming conventions with JDM's actual conventions
- Add JDM policy numbers to the forbidden patterns section
- Add any JDM-specific required description formats

### Step 2: Security Policies
Edit `agents/security-compliance/AGENT.md`:
- Add JDM's data classification levels
- Add specific insurance regulation references (HIPAA, GLBA, state laws)
- Update the PII patterns for data types JDM handles

### Step 3: Test Standards
Edit `agents/playwright-specialist/AGENT.md`:
- Set your team's preferred selector strategy
- Add known application-specific wait patterns
- Document any known flaky areas of the application

## The Pitch to Management

**Problem**: Manual code reviews catch ~60% of test quality issues. Reviewers can only hold one perspective at a time.

**Solution**: 5 specialized AI agents review simultaneously, each through a different lens (reliability, security, architecture, standards, Playwright best practices). Findings cross-reference each other via handoff protocols.

**Cost**: ~$0.08 per review with Claude Code. Zero with Copilot fallback.

**ROI Angle**: A single flaky test wastes ~30 min/occurrence. At 3x/week = 78 hours/year per flaky test. The Flakiness Hunter catches these patterns at review time before they enter the codebase.

**Security Angle**: The Security & Compliance agent catches PII in test code, hardcoded credentials, and insurance data handling violations that no linter detects.

## Credits

Built using the Antigravity orchestration system by Farrice Cain.
Architecture inspired by: Mark Kashef (AI Councils), Nick Saraev (Agentic Workflows), Nate B. Jones (Intent Engineering).
