# Two-Question Solvent Architecture

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Foundation
> **Produces**: Positioning Card
> **Slash Command**: `/gmind-two-questions`

---

## Purpose

Two questions, asked specifically enough to hurt: who's it for, what's it for. Godin runs this reset on granola, perfectionism, employee presentations, decisions, nonprofits — everything. *"If you can't answer those two questions very specifically, go back, rewind 30 seconds, and start over."* The output isn't a positioning statement. It's a don't-come list, a sufficiency number, and a referral map — the artifacts that prove the positioning is real instead of decorative.

---

## Inputs Required

1. **The Offer** — what's being positioned (business, service, content, project).
2. **The Current Answer** — how the asker currently answers "who's it for" (usually too broad — flag this before starting).
3. **Capacity Reality** — how much of this can actually be delivered (time, seats, hours).

---

## Workflow

### Step 1: Diagnose — Is the Current Answer Specific Enough to Exclude?

Test the current positioning against the failure case: *"I don't it's for people who need a haircut. What's it for? So that they feel better?"* That answer fails — it excludes no one. If the current answer could apply to any competitor's customer, it hasn't cleared this step. *"If your motto is you can pick anyone and I'm anyone, then you're doomed."*

### Step 2: Who's It For — Specific Enough to Exclude

Rewrite the audience until it names a real, narrow group with a real, narrow desire. The model: *"There's a hairdresser near my home that only works on women who have curly hair. All she does."* Not "women," not "people who want haircuts" — curly hair, specifically, and nothing else.

### Step 3: What's It For — From the Customer's Ledger

Define value the way the customer would total it up, not the way the seller would describe the craft. *"What's it for? To give them an experience that will make them decide it was worth more than it cost. That's it."* If the answer describes the maker's process instead of the buyer's ledger, rewrite it.

### Step 4: Smallest Viable Audience + the Sufficiency Number

Attach a number to the audience, and let it be small on purpose. *"What's the smallest viable audience? How many people would be enough?"* His own answers stay small: *"I can only cut 10 people's hair a day. That's enough"* — and at bakery scale, *"there's 500 people who every couple weeks are going to buy a pound of coffee. That's enough for now."* Sufficiency, not maximization, is the target number.

### Step 5: The Don't-Come List (≥4 Exclusions)

Write the exclusions before the inclusions, curly-hair style: *"If you're bald, don't come. If you're a guy, don't come. If you don't have curly hair, don't come. If you have curly hair, but you want a cheap haircut, don't come."* Four distinct exclusion criteria minimum — demographic, desire-based, and price-based exclusions all belong on the list.

### Step 6: The Referral Map

For each excluded segment, name who they should go to instead — a real name or a real competitor, not a vague "look elsewhere." The model: *"If you're a Ferrari dealer and someone shows up and says, 'I got a carpool seven kids.' They don't try to persuade you to buy an Enzo. They say, 'My brother-in-law's got a Volvo dealership. I'll call ahead for you.'"* This is the proof-of-positioning test: *"how often are you regularly referring people to someone who might think of as your competitor? If you're never doing that, then you're really stuck in the 'I'm anyone.'"*

### Step 7: The "Sorry, It's Not for You" Script

Write the actual sentence used when the excluded show up. No hedging, no apology tacked on: *"you need to be able to regularly say, 'Sorry, it's not for you.' No apology. The These baked goods are so expensive. Sorry, they're not for you."*

---

## Output Schema

```
POSITIONING CARD
=================

Who's It For: [specific enough to exclude — not demographic alone]
What's It For: [from the customer's ledger — "worth more than it cost"]

Smallest Viable Audience: [the number]
Sufficiency Number: [what "enough" looks like — stated, not implied]

DON'T-COME LIST:
1. [exclusion]
2. [exclusion]
3. [exclusion]
4. [exclusion]

REFERRAL MAP:
[excluded segment] → [where they go instead]
[excluded segment] → [where they go instead]

The Script: "Sorry, it's not for you." [no apology appended]
```

---

Execution prompt: `references/prompts-v2/positioning-card.md` — honor its Output Contract.

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Exclusion Specificity | ≥4 don't-come items, at least one demographic, one desire-based, one price-based |
| Referral rate to competitors > 0 | At least one named referral destination per excluded segment — positioning proof, not decoration |
| Sufficiency Stated | A number is attached to "enough," not just "smallest viable audience" as a phrase |
| Ledger, Not Craft | "What's it for" is written from the buyer's value calculation, not the maker's process description |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/april-dunford` | Two-question output feeds directly into formal positioning statement construction |
| `/avatar-machine` | Don't-come list sharpens the ICP's negative space, not just its positive traits |
| `/icp-build` | Sufficiency number grounds ICP sizing in capacity reality, not TAM fantasy |
| `/godin-brand-promise` | What's-it-for answer feeds the brand promise draft in the seth-godin-brand skill |
