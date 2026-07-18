---
description: Persuasion-Engineered Copy Engine — McRaney × Luke Iha cross-stack that produces finished copy with ELM routing, rebuttal defense, accommodation design, and proof prescription baked into every line
---

# Persuasion-Engineered Copy Engine

**Produces**: Finished copy (ads, sales pages, emails, VSLs, landing pages, LinkedIn posts) with belief-change architecture built into every line.

> **Load before executing**:
> 1. `skills/david-mcraney-belief-change/genius.md`
> 2. `skills/luke-iha-proof-ladder/SKILL.md` (or relevant Luke Iha skill for copy type)
> 3. `skills/luke-iha-copy-blocks/SKILL.md` (for ad/sales copy)

> [!IMPORTANT]
> Phase 1 fires Perplexity research to ground audience diagnosis in real data. Do NOT skip this phase or substitute training data.

## When to Deploy

- Writing any conversion copy where you need people to genuinely change their mind — not just agree
- Sales pages for contrarian or innovative offers
- Ads targeting audiences with known objections or resistance
- Email sequences designed to move cold traffic to purchase
- Any copy where "they agree but don't buy" is the pattern

## Inputs Required

- **Offer/Product**: What are we selling?
- **Audience**: Who are we writing for?
- **Copy Type**: Ad / Sales page / Email sequence / VSL / LinkedIn / Landing page
- **Known Objections** (optional): Any resistance you already know about
- **Existing research** (optional): Output from `/mcraney-deep-canvass` or `/belief-creative-brief`

---

## Phase 1: Audience Belief Diagnosis 🔍

**Uses**: McRaney Patterns 1 (Resistance Hierarchy), 24 (ELM Route Selection), 25 (Rebuttal Type Detection)

> Skip this phase if you already have output from `/mcraney-deep-canvass` or `/belief-creative-brief`. Use that document directly.

### Research Step 🔬

Fire Perplexity query:

```
Search for: [audience] objections to [product/category/offer type].
Find: Reddit discussions, review complaints, forum threads, social media posts where
people explain WHY they resist/refuse/are skeptical of [product/category].
Also find: What convinced people who DID convert — testimonials, "what changed my mind" posts.
Return: 10-15 objection quotes + 5-10 conversion trigger quotes.
```

### Diagnosis

From the research, determine:

1. **Top 3 Blocking Beliefs** — The specific beliefs preventing purchase
2. **Resistance Classification** — Fact / Attitude / Value / Identity for each
3. **ELM Route** — Score motivation (1-10) + ability (1-10) for this audience on this topic:
   - Both ≥ 7 → Central route: lead with evidence, logic, novel arguments
   - Either < 7 → Peripheral route: lead with credibility, social proof, design quality
   - Mixed → Dual: peripheral hook into central depth
4. **Predicted Rebuttal Type** — Will resistance manifest as:
   - Technique rebuttal ("you're trying to sell me") → Build transparency into copy
   - Topic rebuttal ("your claims are wrong") → Front-load strongest evidence

### Output

```
## Belief Diagnosis

Top Blocking Beliefs:
1. "[belief]" — [tier] — Source: [quote]
2. "[belief]" — [tier] — Source: [quote]  
3. "[belief]" — [tier] — Source: [quote]

ELM Route: [Central / Peripheral / Dual]
Motivation: [X]/10 | Ability: [X]/10

Predicted Rebuttal: [Technique / Topic / Mixed]
```

---

## Phase 2: Accommodation Design

**Uses**: McRaney Pattern 2 (Accommodation Detection), HK 12 (Accommodation Requires Surprise)

### Execute

For this specific audience × offer, design the three accommodation triggers:

1. **Surprise Element** — What would this audience genuinely NOT expect? What can't their current model explain? This becomes the hook concept.
   - ❌ NOT shock, controversy, or clickbait
   - ✅ A genuine gap in their mental model: "Wait, that doesn't fit what I thought..."

2. **Relevance Anchor** — Why does this matter to THEM specifically? Not "this is important" but "this affects YOUR [specific thing they care about]"

3. **Safety Mechanism** — The face-saving narrative that lets them update without feeling stupid, naive, or disloyal. Pre-build this BEFORE the challenge.
   - Template: "You were right to think [old way] given [old information]. Here's what changed..."

### Output

```
## Accommodation Design

Surprise: [specific gap in their model you'll exploit]
Relevance: [specific personal stake for THIS audience]
Safety: "[Face-saving narrative]"
```

---

## Phase 3: Copy Architecture

**Uses**: McRaney Pattern 16 (Staged Delivery), Pattern 26 (Metacognitive Unlock), Pattern 11 (Face-Saving)

### Execute

Design the copy structure as a **belief sequence** — each section shifts exactly ONE belief:

| Section | Belief to Shift | Technique | Copy Element |
|---------|----------------|-----------|-------------|
| Hook | Break default processing → activate attention | Surprise element from Phase 2 | Headline / opening line |
| Problem | Activate metacognition — reader examines their own assumption | Process question (Pattern 26) | Problem section / story setup |
| Bridge | Provide the face-saving narrative | Safety mechanism from Phase 2 | Transition / "here's what changed" |
| Solution | Deliver the new framework | Staged revelation (Pattern 16) | Mechanism / offer explanation |
| Proof | Match proof type to predicted rebuttal | See Phase 4 | Proof section / testimonials |
| CTA | Remove final barrier | Permission architecture (Pattern 21) | Call to action |

**Route-Specific Adjustments**:
- **Central route** → Longer proof section, more evidence, logical argument chain
- **Peripheral route** → Authority signals early, social proof heavy, design/visual quality emphasis, shorter logical chain
- **Dual** → Peripheral hook (first screen), central depth (for scrollers/readers)

---

## Phase 4: Proof Prescription

**Uses**: McRaney Pattern 25 (Rebuttal Type Detection) × Luke Iha proof ladder

### Execute

Match proof types to the predicted rebuttal:

**If Technique Rebuttal Predicted** ("you're trying to sell me"):
- Deploy: Transparency proof ("Here's exactly why I'm showing you this")
- Deploy: Permission proof ("You don't have to decide now, but...")
- Deploy: Anti-selling proof (acknowledge the pitch, then transcend it)
- Deploy: Process proof (show your method, not just your results)
- ❌ Avoid: Heavy testimonial stacking (confirms "sales tactic" suspicion)

**If Topic Rebuttal Predicted** ("your claims are wrong"):
- Deploy: Empirical proof (data, studies, specific numbers)
- Deploy: Third-party proof (independent verification, press mentions)
- Deploy: Demonstration proof (show it working, not just claim it works)
- Deploy: Concession proof (acknowledge where they're RIGHT, then redirect)
- ❌ Avoid: Transparency about method (looks defensive on topic rebuttals)

**If Mixed**:
- Lead with transparency to defuse technique suspicion
- Follow with empirical/demonstration to handle topic objections

### Output

```
## Proof Prescription

Predicted rebuttal: [type]
Proof stack (in order):
1. [Proof type] — [specific example for this offer]
2. [Proof type] — [specific example]
3. [Proof type] — [specific example]
Proof to AVOID: [type] — [why it backfires here]
```

---

## Phase 5: Draft Production

### Execute

Write the full copy using the architecture from Phases 1-4:

1. **Hook** → Surprise element, route-matched format
2. **Problem/Story** → Metacognitive activation, relevance anchor
3. **Bridge** → Face-saving narrative
4. **Solution/Mechanism** → Staged revelation, one belief per section
5. **Proof Section** → Prescribed proof types in prescribed order
6. **CTA** → Permission architecture, barrier-matched

### Copy Calibration Check (during drafting)

For every section, verify:
- [ ] ICP on phone, 2 seconds — do they know it's for them?
- [ ] Could this be comfortably assimilated without changing anything? If yes → add surprise
- [ ] Is the proof type matched to the predicted rebuttal? If mismatched → swap
- [ ] Does the face-saving narrative appear BEFORE the challenge? If after → restructure

---

## Output Schema

**Deliverable**: One finished copy piece assembled per the Phase 5 architecture (Hook → Problem/Story → Bridge → Solution/Mechanism → Proof Section → CTA), ready to run through the Phase 6 accommodation test below.

- **Structure**: Six labeled beats in order, each carrying the pattern it executes (surprise, metacognitive activation, face-saving narrative, staged revelation, prescribed proof types, permission-matched CTA) — but the labels themselves never appear in the delivered copy.
- **Proof fidelity**: Every proof element in the Proof Section must match the Phase 4 prescription exactly (type AND sequence) — substituted or reordered proof fails Phase 6's Rebuttal Defense test.
- **Format**: Matches the format requested in Inputs (ad, email, page, script) — the six-beat structure adapts length and beat-weight to that format, never forces a sales-page length onto a 150-word ad.

---

## Phase 6: Accommodation Audit (Quality Gate)

**Uses**: Pattern 2 (Accommodation Detection), HK 12

Run the finished copy through the accommodation test:

| Test | Question | Pass? |
|------|----------|-------|
| **Surprise** | Does the hook contain genuine cognitive surprise — something the audience's model can't explain? | |
| **Relevance** | Is the personal stake specific to THIS audience, not generic "this matters"? | |
| **Safety** | Does the face-saving narrative appear before the challenging claim? | |
| **Route Match** | Is the messaging style (evidence vs cues) matched to the diagnosed processing route? | |
| **Rebuttal Defense** | Is the proof type matched to the predicted rebuttal type? | |
| **Staged Delivery** | Does each section shift exactly one belief, in sequence? | |
| **Accommodation vs Assimilation** | Would a reader say "I never thought of it that way" or "yeah I already knew that"? | |

If any test fails → rewrite the failing section using the specific prescribed fix.

---

## Integration

- **Upstream**: Accepts research from `/mcraney-deep-canvass` or `/belief-creative-brief`
- **Downstream**: Output can be refined by `/slop-check`, `/word-sprint`, `/accommodation-audit`
- **Cross-stack**: Works with any Luke Iha skill for proof production, any content engine for platform adaptation
