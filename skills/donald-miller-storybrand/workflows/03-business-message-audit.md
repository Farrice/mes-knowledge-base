# Workflow 03: Business Message Audit

> **Produces**: Diagnostic report with element-by-element SB7 scoring + fix recommendations
> **Use When**: Need to diagnose WHY a business's messaging isn't working
> **Genius Context**: Load `genius.md` before executing

## Pre-Flight

**Required Inputs:**
- Business website URL, landing page, or marketing materials to audit
- Business name and what they sell
- (Optional) Conversion data or specific complaints about messaging performance

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


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

## Output Schema

```yaml
deliverable: "StoryBrand Messaging Audit"
components:
  five_second_test:
    description: "Pass/Fail for 3 questions: what, how, action"
  overall_score:
    description: "Aggregate score out of 70"
  element_scores:
    description: "0-10 score per SB7 element with one-line diagnosis"
    elements: [character, problem, guide, plan, cta, failure, success]
    format: "[X]/10 — [one-line diagnosis]"
  structural_issues:
    description: "Identified issues beyond individual elements"
  priority_fixes:
    description: "Top 3 fixes ordered by ROI with example copy"
    count: 3
  quick_wins:
    description: "3 changes deployable today"
    count: 3
```

## Quality Gate

- [ ] Every element scored with specific, actionable diagnosis
- [ ] Fixes include actual example copy, not just advice
- [ ] Prioritized by ROI (highest impact first)
- [ ] Structural issues identified beyond individual elements
- [ ] The audit itself is clear and jargon-free (practice what we preach)


> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
## Example Output

**Context**: Messaging audit for "Peak Performance Coaching" — an executive coaching firm whose website isn't converting despite high traffic

**5-SECOND TEST:** ❌ Fail | ❌ Fail | ❌ Fail
1. What do you do? — Unclear. Homepage opens with "Unlock Your Potential" over a mountain photo.
2. How will it make my life better? — No specific outcome stated anywhere above the fold.
3. What do I need to do? — CTA says "Learn More" — learn more about what?

**OVERALL SCORE: 24/70**

| Element | Score | Diagnosis |
|---------|-------|-----------|
| Character | 2/10 | Hero is the coach, not the client — "Dr. Sarah's 20-year journey" is the first section |
| Problem | 4/10 | External problem vaguely mentioned ("challenges"), internal and philosophical absent |
| Guide | 5/10 | Strong credentials buried on About page, zero empathy statements |
| Plan | 1/10 | No process plan at all — visitor has no idea how to engage |
| CTA | 3/10 | "Learn More" and "Contact Us" — neither resolves a decision |
| Failure | 2/10 | No stakes mentioned — why would anyone act today? |
| Success | 7/10 | Best element — testimonials show genuine transformation but buried at bottom |

**STRUCTURAL ISSUES:**
• Brand-as-hero problem: 73% of homepage copy is about the coach, not the client
• Product appears in paragraph 1 ("our coaching methodology") — before any problem context
• Zero open story loops — no reason for a scanning brain to keep reading

**PRIORITY FIXES (by ROI):**
1. **Swap hero seats** (HIGH): Rewrite header from "Unlock Your Potential with Dr. Sarah" → "Stop Dreading Monday Mornings. Lead with confidence, not anxiety." Move coach bio below the fold.
2. **Add a 3-step plan** (HIGH): "1. Book a free clarity call → 2. Get your personalized leadership map → 3. Show up Monday as the leader your team deserves."
3. **Replace CTA copy** (MEDIUM): "Learn More" → "If leading your team feels harder than it should, booking a clarity call is the right decision."

**QUICK WINS (deploy today):**
• Move testimonials from bottom to Section 4 (guide authority positioning)
• Change "Contact Us" button to "Book Your Free Clarity Call"
• Add one failure stake above the CTA: "Every month without a leadership system is another month your best people consider leaving."
