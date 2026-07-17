# Tension Map Architecture

> **Expert**: Seth Godin | **Skill**: seth-godin-marketing-mind | **Tier**: Foundation
> **Produces**: Tension Map
> **Slash Command**: `/gmind-tension-map`

---

## Purpose

Familiarity doesn't sell. A plan built on "show up consistently" or "get the word out" is optimizing for the wrong mechanism entirely: *"People don't spend good money to buy from people who are familiar to them."* The actual mechanism is story → tension → relief-by-purchase. This workflow diagnoses whether a current content or marketing plan is a familiarity play, names the story actually being told, maps the tensions it creates, and designs how buying — specifically buying, not following — relieves them.

---

## Inputs Required

1. **The Current Plan** — the content/marketing approach as currently described.
2. **Audience Segments** — who's being reached, broken out if more than one.
3. **The Actual Transaction** — what buying looks like once someone is convinced.

---

## Workflow

### Step 1: Diagnose — Is This a Familiarity Play?

Scan the plan for the tell: does it describe activity (posting, showing up, getting the word out) without describing a mechanism that converts attention into a transaction? Run the trap-naming move first if the language matches: *"What a trap, Mel. What a trap. People don't spend good money to buy from people who are familiar to them."*

Cite the case that kills reach-as-strategy on contact: *"One person told me he got 40 million views to a video he did on TikTok and sold four copies of his book. No surprise. Because entertaining and performing for people on TikTok is not the same as solving their problem by selling them a $20 book. Those are totally different transactions."* If the current plan can't explain why its version of this wouldn't happen, it's a familiarity play.

### Step 2: Name the Story Being Told

State the actual story the content or plan is telling — not the topic, the narrative. A story about granola isn't about granola: *"To be in the granola business is to create a story and an item that people will happily pay more than it costs to make and tell their friends about."* Name it in one sentence.

### Step 3: Map the Tensions It Creates

Identify which of the four tensions the story is generating, per audience segment. These are the only four in the source — don't invent a fifth:

- **Being left out** — the fear of missing something others already have.
- **Falling behind** — the fear of losing ground relative to peers.
- **Maybe this will work for me** — the hope-tension of an unproven possibility.
- **All my friends are doing it** — social-proof pressure from a visible in-group.

*"This story creates tension. The tension of being left out, the tension of falling behind, the tension of maybe this will work for me, the tension of all my friends are doing it."* Map each active audience segment to the tension(s) actually in play for them — don't force all four onto every segment.

### Step 4: Design the Relief — How Buying Relieves the Tension

The relief has to be the purchase itself, not engagement, not following, not liking. *"That tension might spread cuz it's remarkable, worth talking about, but then what you want is for people to relieve the tension by buying from you."* Test every relief mechanism against the 40M/4-books case: does this design convert tension into a transaction, or does it just convert tension into more scrolling?

### Step 5: Output the Story → Tension → Relief Chain Per Segment

For each audience segment, write the full causal chain in sequence. No segment ships without all three links stated explicitly.

---

## Output Schema

```
TENSION MAP
=============

Familiarity-Play Diagnosis: [YES/NO — cite what in the plan triggered or cleared this]

The Story: [one sentence — narrative, not topic]

SEGMENT 1: [name]
  Tension(s) Active: [which of the four, and why]
  Relief Mechanism: [what the purchase specifically resolves]
  Chain: [story] → [tension] → [relief-by-purchase]

SEGMENT 2: [name]
  Tension(s) Active: [which of the four, and why]
  Relief Mechanism: [what the purchase specifically resolves]
  Chain: [story] → [tension] → [relief-by-purchase]
```

---

Execution prompt: `references/prompts-v2/tension-map.md` — honor its Output Contract.

## Quality Gate

| Dimension | Minimum Standard |
|-----------|-----------------|
| Familiarity Rejected by Name | Plan explicitly states why it isn't a reach/familiarity play, or names the trap if it is |
| Tension Sourced from the Four | No invented fifth tension category — pulled from being-left-out / falling-behind / maybe-this-will-work / friends-doing-it |
| Relief Is Purchase, Not Engagement | Relief mechanism resolves in a transaction — following/liking/commenting fails this gate |
| Chain Complete Per Segment | Every segment carries story → tension → relief explicitly, not implied |

---

## Cross-Expert Stacking

| Stack With | Compound Effect |
|-----------|----------------|
| `/kallaway-content-psychology` | Tension mechanics compound with attention-psychology hook design |
| `/gmind-premise-audit` | Run first if the plan itself needs the trap named before mapping tensions |
| `/copy-engine` | Story→tension→relief chain feeds directly into conversion copy structure |
| `/godin-brand-promise` | Relief-by-purchase design should match the brand promise's hard-mode delivery |
