---
description: "/meg-trust-email-engine — produce the three trust emails that carry Heckman's Layer 5: the give-before-ask welcome, the customer-life story email, and the co-creation 'need your help' ask. 'The first email someone gets from you is a handshake. And most brands open that handshake with an invoice.'"
---

# The Trust Email Engine

The existing Factory Loop treats email as pre-paid traffic — cadence and campaign types. This workflow owns what goes IN those emails: the three artifacts that turned Sloth Hiking Club's list from a discount channel into the R&D department and retention engine behind a claimed $1.7M/18 months (UNCONFIRMED). Welcome emails open at ~84% vs ~40% for everything else (GetResponse, per Meg — LIKELY); "the one email everyone actually opens and most brands typically waste it."

## Pre-Flight

1. `skills/meg-heckman-buyer-trigger-os/genius.md` — Trust Mechanics (Layer 5, moments 3-5), Exemplars 5-6, Voice DNA
2. Voice source: the named human's actual words (founder emails/texts/replies). No source → capture 3 voice decisions before writing.

> **Pre-Flight Gate**: a named human must sign (the "Eric, Founder" role). Anonymous brand voice fails this layer — "brand voice = a person's voice, not a persona doc."

## Input Required

- Brand, niche, sub-identity (behavioral-moment person)
- Named human signer + voice source
- The promise made at opt-in (discount/lead magnet) — email 1 must deliver it instantly
- 3+ lived moments of the sub-identity (or approve mining them from the niche in Step 2)

## Workflow

### Step 1: THE WELCOME — Give Before You Ask
Three lines, nothing else: (1) deliver the promise instantly, no games; (2) say hi like the named human actually talks — why this brand exists, one breath; (3) ask ONE niche-specific question they'll *want* to answer. No logo block, no product grid, no "shop now button the size of a house." Subject reads like a person. Works identically at subscriber #1 and #10,000.

Execution prompt: `references/prompts-v2/trust-welcome-email.md`

### Step 2: THE STORY — Their Life, Not Your Shelf
Pick the sub-identity's most recognizable unspoken moment (SHC's: "the drive home after a hike"). Write it second person, sensory beats, the lies they tell themselves — affection, never mockery. Product enters in the last line or not at all. Then build the **moment bank**: 5 further titles ranked by recognition strength ("ranked everything that ruins a hike" is a system, not a one-off).

Execution prompt: `references/prompts-v2/customer-life-email.md`

### Step 3: THE ASK — Let Customers Write the Products
The six-beat co-creation email (the "Need your help" template that produced the claimed #3 bestseller): backstory beat → open question about a product that doesn't exist yet → 3 example lanes → "doesn't need to be a finished idea" → free-product promise if it ships → "hit reply" + signature. Plus the operator's build rule: when a reply makes you laugh out loud, build it, send them one free — "you just turned a customer into a co-founder."

Execution prompt: `references/prompts-v2/cocreation-ask-email.md`

### Step 4: SEQUENCE WIRE
Slot the three into the existing cadence (Factory Loop Step 4 if installed): welcome = automation day 0; story emails = the weekly default ("week after week, it is about their world, not our shelf"); the ask = closes any story email with one question, full template monthly.

## Content Type Adaptations

**POD/merch**: as written. **Coaching/services**: promise = the lead magnet; story email = the client's Tuesday, not your framework; co-creation = "what should the next workshop cover — dumb questions welcome." **Newsletter**: welcome = deliver archive + one question; the ask feeds content, not products. **Local/real estate**: story = the neighborhood moment (the Sunday open-house drive-by); feature co-creation = "what would make you actually open these emails."

## Output Schema

```
TRUST EMAIL ENGINE — [brand] — [date]
1 WELCOME (3 lines, signed): [full sendable text]
2 STORY EMAIL: [full sendable text, product last-line-only]
  MOMENT BANK: [5 titles, ranked, one-line recognition rationale each]
3 CO-CREATION ASK (6 beats, signed): [full sendable text]
SEQUENCE WIRE: [where each slots into the live cadence]
CLAIMS NOTE: SHC figures UNCONFIRMED; stat citations LIKELY (her citations)
```

## Example Output

**Context**: Jen Santulan (SFV realtor, FTHB engine), signer Jen, opt-in promise = FTHB checklist.

**WELCOME (excerpt)**:
> **Subject: your checklist (+ a question I ask everyone)**
>
> Checklist's attached — no drip campaign hostage situation, it's just yours.
>
> I'm Jen. I sell homes in the Valley, and I started this list because first-time buyers get talked AT by everyone and listened to by almost no one.
>
> So: what's the one thing about buying that keeps you up at 2am? Hit reply. I answer every email myself.

**MOMENT BANK (top 2)**: "Can we talk about the Zillow scroll at midnight?" · "The open house where you pretended you weren't in love."

**What makes this excellent**: line 1 delivers with a no-games flag in Jen's dry register; the 2am question targets the buyer's real behavioral moment, so replying feels like confession, not survey; nothing else competes for the click.

## Quality Gate

- Welcome survives the invoice test: three moves, zero catalog furniture, one human ask
- Story email: specific moment (not a theme), affection not mockery, product absent until last line
- Co-creation ask carries all six beats; reward + "hit reply" present
- Every artifact signed by the named human in captured voice
- Claims labeled per `references/source-quotes.md` ledger
