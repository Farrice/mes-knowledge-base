---
description: Audit any newsletter concept against Cole's Two Rules — pass/fail with fix prescriptions
---

# Book Never Ends — Two Rules Audit

Binary pass/fail validation for any newsletter concept. If it fails, prescribes the specific redesign needed.

## Prerequisites
- Load `nicolas-cole-newsletter-flywheel` skill (SKILL.md + genius.md)

## Process

### Step 1: Capture the Concept
Get the newsletter description from the user. Accept any format — a sentence, a paragraph, a pitch deck slide. Normalize it into:
- **Topic**: What area does it cover?
- **Audience**: Who is it for?
- **Claimed value**: What does the creator say the reader gets?

### Step 2: Rule 1 — Book That Never Ends
**Question**: "If this were a book, would the reader reach the last page and think 'Damn, I wish this kept going'?"

Run the assessment:
1. What is the "book" equivalent of this newsletter? Name it.
2. Does this book have a natural endpoint? (If yes → Rule 1 fails. Newsletters with endpoints = courses, not newsletters.)
3. Would the reader re-read this book? (If no → the content isn't sticky enough for a subscription.)

**Verdict**: PASS / FAIL
**If FAIL**: Prescribe what would make it a book-that-never-ends. Usually: narrow the scope, increase specificity, add a repeating structure.

### Step 3: Rule 2 — Tangible Faucet
**Question**: "What tangible, repeatable asset does the subscriber receive every issue?"

Run the triple test:
1. **Noun Test**: Can the reader name the thing they get? (Not a topic, a THING.)
2. **Save Test**: Can they save, bookmark, copy-paste, or screenshot it?
3. **Wine Club Test**: "It's like a _____ club but for _____." Does the analog work?

**Verdict**: PASS / FAIL
**If FAIL**: Prescribe the specific tangible asset that would fix it. Pull from the 7-type taxonomy in `/tangible-faucet`.

### Step 4: Output Report

```
NEWSLETTER TWO RULES AUDIT
═══════════════════════════

Concept: [their description]
Book Equivalent: [named]

RULE 1 — BOOK THAT NEVER ENDS: [PASS ✅ / FAIL ❌]
[1-2 sentence reasoning]
[If fail: specific fix prescription]

RULE 2 — TANGIBLE FAUCET: [PASS ✅ / FAIL ❌]  
Asset identified: [noun or "NONE"]
Noun Test: [pass/fail]
Save Test: [pass/fail]
Wine Club Test: [pass/fail]
[If fail: specific fix prescription]

OVERALL: [PASS — in the 1% / FAIL — needs redesign]

[If pass: "Ready to proceed to /newsletter-flywheel or /substack-launch"]
[If fail: Recommended next step — /tangible-faucet to redesign the asset]
```

## Output Schema

The audit report above (Step 4) IS this workflow's output contract — every field must be filled, no field left as a bracketed placeholder in the delivered version.

## Quality Gate

- [ ] Both rules given an explicit PASS/FAIL, never "sort of" or "mostly"?
- [ ] Rule 2's three sub-tests (Noun, Save, Wine Club) each individually scored, not collapsed into one verdict?
- [ ] Every FAIL carries a specific fix prescription (name the redesign), not a generic "needs work"?
- [ ] The OVERALL verdict routes to the correct next workflow (`/tangible-faucet` on fail, `/newsletter-flywheel` or `/substack-launch` on pass)?
