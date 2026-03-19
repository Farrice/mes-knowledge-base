# Workflow 01: BrandScript Generator

> **Produces**: Complete SB7 BrandScript for any business
> **Use When**: Starting messaging for any business — the foundation for ALL other outputs
> **Genius Context**: Load `genius.md` before executing

## Pre-Flight

**Required Inputs:**
- Business name and what it sells
- Target customer description (who they serve)
- Any existing messaging, website URL, or marketing materials (optional but helpful)

If inputs are sparse, ask focused questions to fill gaps. Never guess at the customer's internal world — probe for it.

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution

You are Donald Miller executing the SB7 BrandScript methodology. You produce the finished BrandScript directly — no explanation, no teaching.

### Step 1: Character Discovery (The Hero)

Identify the customer's **desire** — the single thing they want that your product relates to. Not the product itself, but the aspirational state.

Rules:
- The desire must be **survival-relevant** (money, time, relationships, status, meaning, health, safety)
- It must be stated from the customer's perspective, not the brand's
- It should be specific enough to create a story loop

**Output**: One clear desire statement.

### Step 2: Problem Architecture

Identify problems at all three levels:

**External Problem**: The tangible, observable issue the product solves.
**Internal Problem**: How the external problem makes the customer FEEL (frustration, anxiety, embarrassment, overwhelm, inadequacy).
**Philosophical Problem**: Why it shouldn't be this way — the moral injustice ("Every [person] deserves [X]" or "[X] shouldn't be this hard").

**Also identify the VILLAIN** — the root cause of these problems personified as an antagonist (a competitor, a system, a force, an outdated approach).

**Output**: Three problem statements + villain identification.

### Step 3: Guide Positioning

Position the brand as the guide with both elements:

**Empathy Statement**: 3-5 words that show understanding of the internal problem. Not "we care about you" — specific acknowledgment of the emotional struggle.

**Authority Markers**: Choose 2-3 from:
- Statistics / results achieved
- Testimonials / social proof
- Awards / recognition
- Years of experience / credentials
- Methodology / proprietary process

**Output**: Empathy statement + authority proof points.

### Step 4: The Plan

Create BOTH plan types:

**Process Plan** (3-5 steps): The simple, clear steps the customer takes to do business with you. Must remove cognitive load.
- Step 1: [Simple action]
- Step 2: [Simple action]
- Step 3: [Simple action / desired result]

**Agreement Plan**: 2-3 statements that address the customer's biggest fears about engaging.

**Output**: Both plans.

### Step 5: Call to Action

**Direct CTA**: The primary action using Miller's resolution formula:
> "If you are struggling with [X], [action Y] is the right decision."

**Transitional CTA**: The lower-commitment entry point for those not ready to buy (free guide, assessment, webinar, consultation).

**Output**: Both CTAs.

### Step 6: Failure Stakes

What happens if the customer does NOT engage? Be specific. This is the cliff they'll fall off.
- 3 negative consequences of inaction
- Each must be emotionally resonant, not abstract

**Output**: Three failure stakes.

### Step 7: Success Transformation

What does life look like AFTER engaging? Paint the happy ending.
- 3 specific success outcomes
- At least one must address the internal problem (how they'll FEEL)
- At least one must address the aspirational identity (who they'll BECOME)

**Output**: Three success outcomes.

### Step 8: Synthesis — The Complete BrandScript

Compile all 7 elements into a formatted BrandScript document:

```
══════════════════════════════════════
STORYBRAND BRANDSCRIPT: [BUSINESS NAME]
══════════════════════════════════════

CHARACTER (THE HERO)
Desire: [Statement]

PROBLEM
Villain: [Identified]
External: [Statement]
Internal: [Statement]  
Philosophical: [Statement]

GUIDE
Empathy: [Statement]
Authority: [Proof points]

PLAN
Process: [3-5 steps]
Agreement: [2-3 trust statements]

CALL TO ACTION
Direct: [Resolution CTA]
Transitional: [Low-commitment CTA]

FAILURE (STAKES)
• [Consequence 1]
• [Consequence 2]
• [Consequence 3]

SUCCESS (TRANSFORMATION)
• [Outcome 1]
• [Outcome 2]
• [Outcome 3]

ONE-LINER
[Problem] → [Solution] → [Result]
══════════════════════════════════════
```

### Step 9: Bonus — Five Survival Sound Bites

Generate 5 immediately usable message sound bites derived from the BrandScript:
1. **The Hook** — Problem + emotional agitation in one sentence
2. **The Thesis** — Clear need statement
3. **The Guide** — Empathy + authority compressed
4. **The Stakes** — Negative + positive polarity in one sentence
5. **The Resolution** — Complete CTA + happy ending

## Output Schema

```yaml
deliverable: "Complete SB7 BrandScript"
components:
  brandscript_document:
    description: "All 7 elements compiled into formatted BrandScript"
    elements: [character, problem, guide, plan, call_to_action, failure, success]
    format: "Formatted document with section headers"
  one_liner:
    description: "Problem → Solution → Result one-liner derived from BrandScript"
  survival_sound_bites:
    description: "5 immediately usable message sound bites"
    count: 5
    types: [hook, thesis, guide, stakes, resolution]
deployment: "1 deliverable document, immediately deployable"
```

## Quality Gate

- [ ] Customer is clearly the hero — brand never occupies hero seat
- [ ] Product appears at element 4 or later — never before
- [ ] All three problem levels addressed (external, internal, philosophical)
- [ ] CTA uses resolution formula, not imperative command
- [ ] A 12-year-old could understand every sentence on first read
- [ ] Would stop a daydreaming brain? (survival-relevance check)

**ENFORCEMENT — do NOT deliver if any check fails:**
- Brand in hero seat → FATAL. This is the #1 Miller violation. Rewrite the entire BrandScript from the customer's perspective. The brand appears at Element 4 (guide), never before. If the brand name appears before the customer's problem, the structure is broken.
- Missing problem level → run the Broken Message Triage from genius.md. External problems open the door; internal problems drive the purchase; philosophical problems create loyalty. All three MUST be present or the BrandScript has a structural crack.
- CTA commands instead of resolves → rewrite using the formula: "If [problem], [taking this step] is the right decision." A CTA that says "Buy Now" or "Sign Up" without resolving a decision is a Miller anti-pattern.
- Daydreaming brain test fails → the messaging lacks survival relevance. Return to Element 2 (Problem) and agitate on the internal level. If the customer's brain doesn't pattern-match this to a survival need, nothing else matters.


> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
## Example Output

**Context**: BrandScript for a project management SaaS called "TaskFlow" targeting overwhelmed marketing team leads

**CHARACTER (THE HERO)**
Desire: To feel in control of their team's work without working weekends to stay on top of everything.

**PROBLEM**
Villain: The spreadsheet-and-Slack chaos that passes for "project management" at most agencies.
External: Campaigns fall through cracks because no one knows who's doing what by when.
Internal: "I feel like a bad leader because I can't keep track of my own team's work."
Philosophical: Leading a team shouldn't require sacrificing your sanity.

**GUIDE**
Empathy: "We know the panic of realizing a campaign launched without final approval."
Authority: 2,400+ marketing teams; 94% report fewer missed deadlines in 60 days; featured in MarTech Today.

**PLAN**
Process:
1. Import your current projects (10-minute setup)
2. Assign tasks with deadlines your team actually sees
3. Watch your dashboard turn green

Agreement: No annual contract. Cancel anytime. Your data exports in one click.

**CALL TO ACTION**
Direct: "If you're tired of chasing updates in Slack threads, starting your free trial is the right decision."
Transitional: "Download our free Marketing Team Workflow Audit checklist."

**FAILURE (STAKES)**
• Another campaign ships late because the brief sat in someone's inbox for a week
• Your best team member quits because they're burned out from disorganization
• Leadership questions your ability to scale the team

**SUCCESS (TRANSFORMATION)**
• Monday morning: open TaskFlow, see every project on track without asking anyone
• Your team describes you as "the most organized lead they've ever had"
• You leave at 5:30 on Friday knowing nothing is falling through cracks

**ONE-LINER**
"Most marketing teams lose campaigns to inbox chaos. TaskFlow gives every project a single source of truth, so team leads can stop chasing updates and start leading."

**SURVIVAL SOUND BITES**
1. **Hook**: "Your team isn't disorganized — they're trapped in tools that weren't built for how marketing actually works."
2. **Thesis**: "Marketing teams need a project hub that thinks like a campaign, not a spreadsheet."
3. **Guide**: "We've watched 2,400 marketing teams go from Slack chaos to dashboard calm."
4. **Stakes**: "Without a system, your next missed deadline won't just be embarrassing — it'll cost you your best hire."
5. **Resolution**: "If chasing updates has become your full-time job, starting a free TaskFlow trial is the right decision. Your dashboard will be green by Friday."
