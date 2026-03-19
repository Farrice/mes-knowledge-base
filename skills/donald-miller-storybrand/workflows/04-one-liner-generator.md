# Workflow 04: One-Liner Generator

> **Produces**: StoryBrand one-liner + deployment variants
> **Use When**: Need the single sentence that captures entire value proposition
> **Genius Context**: Load `genius.md` before executing

## Pre-Flight

**Required Inputs:**
- Business name and what it sells
- Target customer
- Primary problem solved
- (Optional) Existing BrandScript — if available, extract from it

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution

You are Donald Miller crafting the one-liner — the single most important marketing sentence a business will ever write. It must be repeatable in casual conversation, social media bios, email signatures, and elevator pitches.

### Step 1: Problem Identification

Identify the single most emotionally resonant problem the business solves. Rules:
- Must be stated from the customer's perspective
- Must be specific (not "grow your business" — too vague)
- Must trigger recognition ("that's me") in the target customer
- Prefer the internal problem over the external

### Step 2: Solution Mechanism

State what the business does to solve this problem. Rules:
- Must be the mechanism, not the product name
- Must imply competence without bragging
- Must be simple enough to say in conversation

### Step 3: Result Painting

State the positive outcome. Rules:
- Must be aspirational — the life AFTER
- Must address either the emotional state, the identity, or the tangible result
- Must be specific enough to create desire

### Step 4: Assemble the One-Liner

**Formula**: [Problem] + [Solution] + [Result]

Structure: "Most [customers] struggle with [problem]. We [solution mechanism] so they can [desired outcome]."

Generate 5 variations:
1. **Standard** — "Most... We... So they can..."
2. **Conversation** — Natural spoken version for networking
3. **Social Bio** — Compressed for LinkedIn/Instagram bio (under 150 characters)
4. **Email Signature** — Professional format
5. **Pitch** — Extended version with one supporting detail

### Step 5: Stress Test

Run each variation through:
- **The Taxi Test**: If you told this to a taxi driver, would they understand and be interested?
- **The Repeat Test**: Is it simple enough to repeat from memory after hearing once?
- **The "Tell Me More" Test**: Does it make people lean in and ask a follow-up question?
- **The Survival Test**: Does it register as survival-relevant to the listener's brain?

## Output Schema

```yaml
deliverable: "StoryBrand One-Liner"
components:
  core_one_liner:
    description: "Full Problem → Solution → Result one-liner"
  variants:
    description: "Platform-adapted versions"
    includes: [conversation, social_bio, email_signature, pitch]
  stress_test_results:
    description: "Pass/fail on 4 tests"
    tests: [taxi_test, repeat_test, tell_me_more_test, survival_test]
  deployment_guide:
    description: "Channel-specific versions ready to copy/paste"
    channels: [linkedin_headline, email_signature, website_header, networking, social_bio]
```

## Quality Gate

- [ ] Problem triggers customer recognition ("that's me")
- [ ] Solution implies competence without jargon
- [ ] Result creates genuine desire
- [ ] Passes all 4 stress tests
- [ ] Deployable today across 5+ channels


> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
## Example Output

**Context**: One-liner for "GreenLeaf Financial" — a financial planning firm for millennial couples

**CORE ONE-LINER:**
"Most couples fight about money because they've never had a plan that accounts for both of their dreams. GreenLeaf builds financial roadmaps for two, so you can stop arguing about spending and start building the life you actually want together."

**VARIANTS:**
• Conversation: "You know how couples fight about money? We fix that — we build financial plans that work for both partners, so the money conversations stop being fights."
• Social Bio: "Financial plans for couples who want to stop fighting about money and start building together."
• Email Signature: "GreenLeaf Financial — Financial roadmaps for two."
• Pitch: "Most couples argue about money because they've never aligned their individual dreams into one shared plan. We sit down with both partners, build a roadmap that honors what each person wants, and give you a system so money becomes the thing that brings you together — not the thing that pulls you apart."

**STRESS TEST RESULTS:**
✓ **Taxi Test** — Could repeat it from memory after hearing once
✓ **Repeat Test** — "Oh you should talk to GreenLeaf — they do financial plans for couples who fight about money"
✓ **Tell Me More Test** — "How does it work for both partners?" (they lean in)
✓ **Survival Test** — Money + relationships = survival-relevant on two dimensions

**DEPLOYMENT GUIDE:**
• LinkedIn headline: "Helping couples stop fighting about money | Financial Roadmaps for Two"
• Email signature: "GreenLeaf Financial — Stop arguing about spending. Start building together."
• Website header: "Financial Plans That Work for Both of You"
• Networking: "We help couples stop fighting about money by building financial plans that honor both partners' dreams."
• Social bio: "Financial roadmaps for couples who want to build together, not fight about money 💚"
