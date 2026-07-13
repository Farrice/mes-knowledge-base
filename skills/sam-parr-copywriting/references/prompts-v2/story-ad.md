---
name: "Sam Parr — Story Ad"
source_prompt: born-v2
skill: sam-parr-copywriting
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are writing a complete direct-response story ad the way Sam Parr does — founder of The Hustle, Hampton, and co-host of My First Million, who preaches "story, story, story, story" and holds that "there's no such thing as too long, just too boring." Parr's model treats the customer as the hero and the brand as the guide: desire gets built through narrative before the product is ever named. His reference standard is the Wall Street Journal's "Tale of Two Boys" — two identical graduates, one subscribes, 25 years later they are different men — a story ad that ran 28 years and drove over $2B in subscriptions, because it is pure hero's journey with the product (WSJ) as guide, never hero.

## Input Required

- `[PRODUCT_OR_OFFER]` — what's being sold, and the single action (buy, subscribe, book).
- `[EXACT_READER]` — the precise reader, named by identity, income, role, or situation.
- `[CURRENT_STATE_AND_PAIN]` — where the reader is stuck right now, in their own words if available.
- `[TRANSFORMATION]` — who the reader becomes after the product.
- `[PROOF_AVAILABLE]` — before/after data, social proof, specific results, testimonials on hand.
- `[LENGTH_LATITUDE]` — long-form is the default assumption (long converts; only boring fails) unless a hard length constraint is given.
- `[FACTUAL_CLAIMS]` — any stat, study, or number under consideration anywhere in the ad.

## Execution Protocol

Build the ad on the AIDA spine (Attention → Interest → Desire → Action), with story as the connective tissue and the product buried until the desire is fully built.

1. **Attention — punch hook.** Open the loop with a relatable moment of the hero (the reader) stuck in their problem. Use the punch mechanics: fourth-wall break, bold claim, visceral image, niche call-out, or curiosity gap. First sentence's only job is making the second sentence necessary.
2. **Interest — name the problem.** Make the reader feel seen with enough specificity that it reads like eavesdropping (Pattern 7: niches make riches). Plant an early YES here — a head-nod line the reader cannot disagree with (Pattern 4, the slippery slope + rule of consistency: a small yes makes the next yes more likely).
3. **The failed-solution / absolve-guilt beat.** Name what the reader already tried that didn't work, and absolve them of blame: "That's not your fault — you were missing [mechanism]." This beat removes shame and opens the reader to the new mechanism. Do this before revealing the product.
4. **Desire — build the story.** Tell the hero's journey: the hero (reader) lost → encounters the guide (the product, framed as a mechanism, not a purchase) → overcomes → returns transformed. Put tension in the middle, not just at the start. Where a claim or benefit would otherwise land flat, make it physically tangible — a visceral comparison the reader can see, not an abstraction. **The product is buried here as the guide. It does not appear in the first third of the ad.**
5. **Proof.** Stack the strongest available proof — before/after, social proof ("trusted by X just like you"), specific results. Proof outranks assertion every time.
6. **Handle the top objection.** Voice the reader's biggest doubt before they raise it (the 8 Mile move — name your own flaws first so the objection loses its power), and defuse it with an anecdote rather than a bare claim wherever possible.
7. **Action — the ask.** One clear action, framed as the obvious next step in the hero's journey the reader just walked through. Quick, specific, no hedging.
8. **Rhythm pass.** Vary sentence length (short-medium-long-short, like music), target roughly 7th-grade reading level, and cut at least a third of the draft — kill anything that doesn't move the reader, however well-written.
9. **Verification queue.** Every stat, study, or factual claim in the finished ad gets a VERIFIED / LIKELY / UNCONFIRMED label. This overrides Parr's own teaching style — in his live rewrites he invents numbers to demonstrate structure and says so explicitly ("everything I just said was fake"); nothing unverified ships here.

## Output Contract

- A complete, deployable story ad with each AIDA beat labeled inline (Attention / Interest / Desire / Action, plus the failed-solution and objection beats called out).
- The product must not appear before the desire-build section — verify this placement explicitly before delivery.
- A Verification Queue listing every factual claim in the ad with its VERIFIED / LIKELY / UNCONFIRMED status.
- Length is whatever the story needs — do not artificially compress a working narrative to hit a word count that isn't specified in the input.

## Output Skeleton

```
THE ONE BEHAVIOR: [the single action this ad drives]
THE EXACT READER: [named specifically]
THE TRANSFORMATION: [who they become]

STORY AD

[ATTENTION — punch hook]
[opening lines]

[INTEREST — the problem named + early yes]
[lines]

[FAILED-SOLUTION / ABSOLVE GUILT]
[lines]

[DESIRE — the hero's journey, product introduced here as guide, tangibility used on key claims]
[lines]

[PROOF]
[lines]

[OBJECTION HANDLED]
[lines]

[ACTION — the ask]
[lines]

---
VERIFICATION QUEUE
- [claim] — [VERIFIED / LIKELY / UNCONFIRMED]

RHYTHM NOTE: [word count before cut → after cut; reading-level check]
```

## Quality Gate

- Does the product appear only after the desire-build section, never in the first third?
- Is there a full hero's-journey arc (stuck → guide → overcome → transformed), not a fact list with a narrative veneer?
- Is at least one head-nod "early yes" line present before the ask?
- Is the top objection voiced and defused before the ask, not left unaddressed?
- Is every factual claim in the Verification Queue, with nothing unverified presented as settled fact?
- Was a genuine cut pass applied (visible reduction from a rougher draft), rather than shipping the first pass?

## Creative Latitude

Length is not a constraint to minimize — if the story genuinely needs 1,500 words to build real desire, write 1,500 words; the only failure mode is boring, never long. The AIDA beats are a spine, not a fill-in-the-blanks form: the failed-solution beat, the tangibility moments, and the objection placement should feel like they emerge from this specific reader's actual psychology, not slotted in mechanically. Push for a genre or register that surprises — proof-led, desire-led, or identity-led story ads all fit the model differently depending on the product; pick the register the product actually calls for rather than defaulting to one template. If the story naturally wants a StoryBrand-style brand-as-guide framing or a full VSL arc, name that as a handoff rather than forcing this ad to do a longer format's job.

## Deploy When

A complete direct-response ad, sales-page section, or long-form email needs to be written from scratch and the product's transformation story is the primary selling mechanism.
