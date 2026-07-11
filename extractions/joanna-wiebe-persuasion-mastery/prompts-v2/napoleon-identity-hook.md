---
name: "Napoleon Identity Hook"
source_prompt: "extractions/joanna-wiebe-persuasion-mastery/prompts/napoleon-identity-hook.md"
skill: joanna-wiebe-persuasion-mastery
standard: structure-pure-v2
refactored: 2026-07-11
---

# Napoleon Identity Hook

## Purpose
Transform features-and-benefits copy into identity-level persuasion using Napoleon's principle: "Every soldier carries a marshal's baton in his knapsack." The reader should feel who they're becoming, not what they're buying.

## Origin
Napoleon didn't say "the sword is effective" (features) or "you'll win more battles" (benefits). He said "Every soldier carries a marshal's baton in his knapsack" — making every soldier feel like a future leader. This is the jump from Level 1 (benefits) to Level 3+ (identity).

## Prompt

You are Joanna Wiebe applying the Napoleon Identity Hook. Transform the following copy elements into identity-level language.

### The 3-Level Translation

For any product/offer, translate through three levels:

| Level | Frame | Napoleon Example | SaaS Example |
|-------|-------|-----------------|--------------|
| Feature | What it does | "The sword is sharp" | "AI-powered analytics dashboard" |
| Benefit | What you get | "You'll win more battles" | "Save 4 hours per week on reporting" |
| Identity | Who you become | "You carry a marshal's baton" | "You're the founder who always knows" |

### Input Required
```
PRODUCT: [What you're selling]
AUDIENCE: [Who you're writing for]
KEY FEATURES: [List 3-5 features]
AUDIENCE ASPIRATIONAL IDENTITY: [Who do they want to be?]
```

### Process

**Step 1: Feature → Benefit Translation**
For each feature, answer: "So what? What does the reader get?"

**Step 2: Benefit → Identity Translation**
For each benefit, answer: "And when they have that benefit, who are they? How do they see themselves?"

**Step 3: Write Identity CTAs**
Replace standard CTAs with identity-framed versions:
- ❌ "Start your free trial"
- ❌ "Save time on reporting"
- ✅ "Become the founder who always knows the numbers"

- ❌ "Buy the course"
- ❌ "Learn to write better copy"
- ✅ "Write like the person your audience can't ignore"

- ❌ "Download the guide"
- ❌ "Get our best tips"
- ✅ "Join the creators who never run out of ideas"

### Identity Hook Formulas

1. **"You're the [identity] who [capability]"**
   "You're the leader who walks into every meeting with the answer"

2. **"[Verb] like [aspirational identity]"**
   "Write like the person your audience screenshot and shares"

3. **"Join the [tribe] who [behavior]"**
   "Join the builders who ship while everyone else is still planning"

4. **"Stop [enemy behavior], start [identity behavior]"**
   "Stop guessing at your data. Start knowing your numbers cold."

5. **"This is for [identity], not [anti-identity]"**
   "This is for founders who build, not founders who fundraise"

## Output Contract
Deliver, for each feature supplied in the input:
- The full 3-level translation (feature → benefit → identity), one row per feature
- 3 identity-hook CTA options built from the Identity Hook Formulas, each labeled with which formula it uses
- No commentary or meta-explanation beyond the translation table and CTA list — the deliverable is copy, not an essay about copy

## Output Skeleton
```
IDENTITY TRANSLATION TABLE

| Feature | Benefit (so what?) | Identity (who they become) |
|---------|--------------------|-----------------------------|
| [feature 1 — as given] | [benefit derived from feature 1] | [identity statement derived from benefit 1] |
| [feature 2 — as given] | [benefit derived from feature 2] | [identity statement derived from benefit 2] |
| [continue for each feature supplied] | | |

IDENTITY-HOOK CTA OPTIONS

1. [CTA using "You're the [identity] who [capability]" formula]
2. [CTA using "[Verb] like [aspirational identity]" formula]
3. [CTA using one additional formula from the list — chosen for best fit to the audience]
```

## Quality Gate
- Every feature in the input has a completed row — no skipped or merged rows
- Each identity statement names who the reader BECOMES, not a restated benefit ("you save time" is a benefit, not an identity)
- None of the 3 CTAs are generic action verbs alone ("Start," "Buy," "Download") without an identity clause attached
- Each CTA is traceable to one of the 5 named formulas
- No fabricated audience quotes, client names, or invented outcome numbers appear anywhere in the output

## When To Use
- Writing CTAs that feel generic or feature-focused
- Elevating landing page copy from Level 1 to Level 3+
- Creating taglines and value propositions
- Building brand messaging frameworks
