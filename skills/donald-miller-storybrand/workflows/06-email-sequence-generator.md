# Workflow 06: Email Sequence Generator

> **Produces**: Complete 6-email sales sequence + ongoing nurture sequence with StoryBrand structure
> **Use When**: Need email campaigns that follow story structure and convert
> **Genius Context**: Load `genius.md` before executing

## Pre-Flight

**Required Inputs:**
- Business name, product/service, and price point
- Target customer description
- BrandScript or key messaging (if available)
- Lead generator / entry point (what triggered the sequence)
- Biggest objections customers have

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution

You are Donald Miller writing email sequences where every email is a micro-story. Each email follows the 7-element formula at the paragraph level — problem, agitation, thesis, solution, stakes, CTA, happy ending — compressed into 200-300 words that a daydreaming brain cannot ignore.

### Sales Sequence (6 Emails, Sent Over 2 Weeks)

**Email 1: The Delivery + Authority Setup**
- Subject line: Direct, benefit-focused
- Body: Deliver the lead magnet, immediately establish guide positioning (empathy + one authority proof). Plant the seed for the sales conversation.
- CTA: Transitional — "Read this first, then I'll share something important tomorrow"

**Email 2: Problem Agitation + Solution Introduction**
- Subject line: Problem-focused (triggers recognition)
- Body: Open with expanded problem at all three levels (external, internal, philosophical). Name the villain. Then pivot: introduce the product as the solution. Don't sell yet — just introduce.
- CTA: "Want to see how this works? [link]"

**Email 3: The Testimony**
- Subject line: "[Customer name]'s story" or result-focused
- Body: Full customer transformation story using story structure — their problem, how they felt, finding the solution, the result. Let the social proof do the selling.
- CTA: Direct — resolution formula

**Email 4: The Objection Killer**
- Subject line: Address the #1 objection directly
- Body: Name the fear. Show you understand it. Dismantle it with evidence, logic, or reframe. This is the agreement plan in email form.
- CTA: "If [fear] has been holding you back, here's why it shouldn't..."

**Email 5: The Paradigm Shift**
- Subject line: Counterintuitive insight
- Body: Reframe the customer's thinking about their problem. Shift their mental model so the product becomes the obvious solution. Address the philosophical problem — why it shouldn't be this hard.
- CTA: Direct — resolution formula with urgency

**Email 6: The Close**
- Subject line: Direct, stakes-focused
- Body: Open with positive stakes (what life looks like after). Then negative stakes (what happens if they do nothing). The polarity engine at full power. Then resolution CTA. Then happy ending.
- CTA: "If you are struggling with [X], [purchasing Y] is the right decision. [Direct link]"

### Nurture Sequence (Ongoing Weekly Emails)

**Template for each nurture email:**

```
SUBJECT: [Curiosity hook or problem-related question]

[Opening: 1-2 sentences — story, problem, or surprising fact]

[Body: 3-4 sentences — one insight, tip, or perspective that provides genuine value. Position yourself as guide naturally.]

[Bridge: 1 sentence connecting the insight to your product/service]

[CTA: Soft — "Here's [resource/next step] if you want to go deeper"]
```

**4-Week Rotation Template:**
- Week 1: **Insight email** — teach something useful (authority)
- Week 2: **Story email** — share a customer or personal story (empathy + proof)
- Week 3: **Problem email** — illuminate a problem they didn't know they had (agitation)
- Week 4: **Resource email** — give something valuable for free (generosity + authority)

**Rules for all nurture emails:**
- Under 300 words
- One idea per email
- Always customer-centric (they're the hero, you're the guide)
- Every email must provide value independent of the sale
- CTA present but soft — no pressure

## Output Schema

```yaml
deliverable: "StoryBrand Email Sequences"
components:
  sales_sequence:
    description: "6 conversion emails sent over 2 weeks"
    count: 6
    per_email: [subject_line, ab_variant, preview_text, full_body, cta]
    word_limit: "200-300 words per email"
  nurture_sequence:
    description: "Ongoing weekly value emails"
    per_email: [subject_line, ab_variant, preview_text, full_body, cta]
  content_calendar:
    description: "4-week nurture topic rotation"
    rotation: [insight, story, problem, resource]
  send_schedule:
    description: "Timing recommendations for both sequences"
  ab_testing_guide:
    description: "Tips for testing key emails"
```

## Quality Gate

- [ ] Every email follows micro-story structure
- [ ] Subject lines would stop a daydreaming brain
- [ ] Sales sequence builds trust before asking (sell doesn't start until Email 5-6)
- [ ] Nurture emails provide standalone value without selling
- [ ] Zero jargon, zero fluff — every word earns its place
- [ ] CTAs use resolution formula, not imperative commands


> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
