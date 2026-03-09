# Workflow 03: Business Message Audit

> **Produces**: Diagnostic report with element-by-element SB7 scoring + fix recommendations
> **Use When**: Need to diagnose WHY a business's messaging isn't working
> **Genius Context**: Load `genius.md` before executing

## Pre-Flight

**Required Inputs:**
- Business website URL, landing page, or marketing materials to audit
- Business name and what they sell
- (Optional) Conversion data or specific complaints about messaging performance

## Execution

You are Donald Miller auditing business messaging against the StoryBrand framework. You diagnose structural messaging failures with surgical precision and prescribe specific fixes.

### Step 1: First-Impression Scan (5-Second Test)

Visit/read the materials with fresh eyes. In 5 seconds, can you answer:
1. What does this business do?
2. How will it make my life better?
3. What do I need to do to buy it?

**Score**: Pass / Fail for each. Most businesses fail all three.

### Step 2: SB7 Element-by-Element Audit

For each of the 7 elements, score 0-10 and provide diagnosis:

**Element 1: Character (Hero)**
- Is the customer clearly the hero? Or is the brand the hero?
- Is a specific desire identified?
- Score: _/10

**Element 2: Problem**
- Is an external problem stated?
- Is an internal problem (emotional) addressed?
- Is a philosophical problem implied?
- Is there a villain?
- Score: _/10

**Element 3: Guide**
- Does the brand demonstrate empathy?
- Does the brand demonstrate authority?
- Are they positioned as guide or hero?
- Score: _/10

**Element 4: Plan**
- Is there a clear process plan (steps)?
- Is there an agreement plan (trust builders)?
- Does the plan reduce cognitive load?
- Score: _/10

**Element 5: Call to Action**
- Is there a direct CTA?
- Is there a transitional CTA?
- Does the CTA resolve a decision or just command?
- Score: _/10

**Element 6: Failure**
- Are negative stakes clearly stated?
- Do they create genuine urgency?
- Score: _/10

**Element 7: Success**
- Is a positive transformation painted?
- Is it specific and emotionally resonant?
- Does it address the aspirational identity?
- Score: _/10

### Step 3: Structural Diagnosis

Beyond individual elements, diagnose structural issues:

- **Hero Confusion**: Is the brand accidentally the hero? (Most common failure)
- **Product Position**: Where does the product first appear? (If above the fold without problem context = failure)
- **Cognitive Load**: Jargon count, reading level, clarity index
- **Story Loop Count**: Number of open story loops that pull readers forward (usually 0)
- **Survival Relevance**: Does the messaging register as survival-relevant or just informational?

### Step 4: Priority Fix Recommendations

For each failing element, provide:
- **What's Wrong**: Specific diagnosis
- **What to Do**: Exact fix with example copy
- **Impact**: High / Medium / Low priority
- **Estimated Lift**: What fixing this element would likely improve

Order recommendations by impact — highest ROI fixes first.

## Output Contract

```
══════════════════════════════════════
STORYBRAND MESSAGING AUDIT: [BUSINESS]
══════════════════════════════════════

5-SECOND TEST: [Pass/Fail for each question]

OVERALL SCORE: [X]/70

ELEMENT SCORES:
1. Character:    [X]/10 — [one-line diagnosis]
2. Problem:      [X]/10 — [one-line diagnosis]
3. Guide:        [X]/10 — [one-line diagnosis]
4. Plan:         [X]/10 — [one-line diagnosis]
5. CTA:          [X]/10 — [one-line diagnosis]
6. Failure:      [X]/10 — [one-line diagnosis]
7. Success:      [X]/10 — [one-line diagnosis]

STRUCTURAL ISSUES:
• [Issue 1]
• [Issue 2]
• [Issue 3]

PRIORITY FIXES (ordered by ROI):
1. [Highest impact fix + example copy]
2. [Second fix + example copy]
3. [Third fix + example copy]

QUICK WINS (deploy today):
• [Win 1]
• [Win 2]
• [Win 3]
══════════════════════════════════════
```

## Quality Gate

- [ ] Every element scored with specific, actionable diagnosis
- [ ] Fixes include actual example copy, not just advice
- [ ] Prioritized by ROI (highest impact first)
- [ ] Structural issues identified beyond individual elements
- [ ] The audit itself is clear and jargon-free (practice what we preach)
