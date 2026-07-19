# /lynch-character-test — Qualification of People (Ron Lynch)

> Lynch's people-picking system, run on 2,600+ grocery employees and every client and friend since: the admired-three character-traits exercise, the integrity contract (both halves), and the paid-qualification ladder. The founding principle, from the four-zero-shows failure: *"Picking is one of the most important things you do in life. That's why I qualify. I have tests."* Deploys in any vertical: client vetting, hiring, partnerships, collaborations.

Source anchor: `extractions/ron-lynch/transcript-3-V8BD.txt`; ledger in `references/source-ledger.md`.

## When to Use
- Before signing a client, hire, partner, or collaborator (before contracts, not after)
- A prospect is consuming free time without committing (the coffee filter)
- Reading a person's actual value system fast (first meeting, first date-equivalent)
- Post-mortem on a relationship that went wrong — what the test would have caught

## When NOT to Use
- Product/offer qualification (→ `/lynch-product-prequalify` — the four-criteria gate)
- Audience/ICP profiling (→ Dai Media, icp-deep-canvasser)

## Inputs Required
1. Who is being qualified and for what role (client / hire / partner / inner circle)
2. What's at stake (deal size, access, time commitment)
3. If run live: their answers. If run as design: the qualification mechanism to install.

## Execution Steps

### Step 1: The Coffee Filter (commitment gate)
Price the first conversation. Verbatim: *"I have a thousand dollar cup of coffee... knocks out about 80% of the people... The ones that do sit down amazingly start to take you seriously and start to take themselves seriously."* Scale to context (Farrice's current equivalent: a paid readout/diagnostic, not a free pick-your-brain call). Deliver back a 1-2 page notes document — the paid conversation produces an artifact. Known quantities are exempt: *"Known quantities are completely different than unknown quantities."*

### Step 2: The Admired-Three Exercise
Ask for three people, living or dead, no fictional characters, whom they strongly admire. For each: extract CHARACTER TRAITS, not results ("what kind of person does that?"). Push past behaviors to traits: "said what he wanted" → conviction; "overcame failure" → resilience. The read: those 9+ traits ARE the person's own value system — *"Ladies and gentlemen, [them] right to a T."*

### Step 3: The Dark-Side Variant (optional, high-stakes only)
The antithesis person, three traits. Read: not their evil, their WOUNDS — *"the things that [they have] been hurt by in the past."* Handle with care; this is diagnostic, never ammunition.

### Step 4: The Two Definitions
Ask what integrity means, then honesty. Lynch's standards: integrity = *"I do what I say I'm going to do and I don't do what I say I'm not going to do. Most people forget the second half."* Honesty = truth with tact, including the courage to tell ugly truths. Vague answers ("follow your heart," "your truth") are data.

### Step 5: Score the Tells
- **Keeper signal**: they ask for the test back (*"the people that I really love are the people who go, 'What about yours?'"*)
- **Walk-away signals**: status-picks with no nameable character traits after 30 minutes; success/wealth/fame answers where traits should be; "their truth is the truth"
- **Contract close**: make the agreement explicit up front — who we are, the can-do list AND the won't-do list — *"I hold them to it and they hold me to it."*

## Output Format
```
## CHARACTER TEST — [Person / Mechanism]

### Commitment gate
[Passed the paid filter? Known or unknown quantity?]

### Traits read
| Admired person | Traits extracted |
|---|---|
Read-back: [their value system in one sentence]

### Definitions
Integrity: [their answer + both-halves check]
Honesty: [their answer + tact/courage check]

### Verdict
[KEEPER / PROCEED WITH AGREEMENT / WALK] — [which tells fired]
The explicit agreement: [can-do list / won't-do list]
```
Execution prompt: `references/prompts-v2/lynch-character-test.md`

## Quality Gate
- First conversation is paid or the person is a known quantity — no free unknown-quantity consulting
- Traits extracted are character words, never results/status words
- Both halves of the integrity definition checked
- Verdict cites specific tells, not vibes
- High-stakes relationships close with the explicit two-list agreement
