# QA Code Review — Invocation Cards

> **Purpose**: Fast routing for the QA review council. ~50 tokens per card.
> Scan these FIRST before loading full agent files.

---

```
AGENT: Playwright Specialist
DOMAIN: Playwright patterns, selectors, waits, assertions, test API
CORE METHOD: Selector hierarchy + auto-retrying assertion enforcement
BEST FOR: Playwright-specific code quality, reliability patterns
PAIRS WITH: Flakiness Hunter (stability), Test Architecture (structure)
```

```
AGENT: Corporate Standards
DOMAIN: JDM naming conventions, file organization, documentation, PR compliance
CORE METHOD: Convention checklist against internal style guide
BEST FOR: Naming, structure, documentation, forbidden patterns
PAIRS WITH: Test Architecture (structural alignment), Security (credentials)
```

```
AGENT: Test Architecture
DOMAIN: Page Object Model, fixtures, test isolation, data management
CORE METHOD: Isolation-first design — every test independent, no shared state
BEST FOR: Structural design decisions, maintainability, scalability
PAIRS WITH: Corporate Standards (naming), Playwright Specialist (implementation)
```

```
AGENT: Flakiness Hunter
DOMAIN: Race conditions, timing, environment sensitivity, parallel safety
CORE METHOD: "1,000 runs at 3am" smell test — if it can fail, it will
BEST FOR: CI reliability, intermittent failure prevention, timing issues
PAIRS WITH: Playwright Specialist (fix patterns), Test Architecture (state isolation)
```

```
AGENT: Security & Compliance
DOMAIN: PII in test data, credential handling, auth patterns, insurance regulations
CORE METHOD: Data classification scan + compliance checklist
BEST FOR: Insurance industry compliance, data handling, credential management
PAIRS WITH: Corporate Standards (policy), Test Architecture (fixture design)
```
