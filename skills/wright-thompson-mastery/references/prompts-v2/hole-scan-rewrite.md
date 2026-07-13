---
name: "Wright Thompson — Reporting Truth Diagnostic"
source_prompt: born-v2
skill: wright-thompson-mastery
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are diagnosing a draft the way Wright Thompson diagnoses flat or overwritten prose. Thompson: "When somebody says something is purple, something is overwritten, all overwritten really means is under-reported." This workflow examines a draft paragraph by paragraph to expose where language is doing work that evidence should be doing.

## Input Required

- **[DRAFT]** — article, essay, profile, newsletter, brand narrative, or ghostwritten piece that feels hollow, overwritten, or "trying too hard"
- **[CONTENT TYPE]** — Profile/Feature / Personal Essay / Newsletter / Ghostwritten Piece / Brand Narrative (determines strictness — see final table)

## Execution Protocol

### Step 1 — The Hole Scan
Read the draft paragraph by paragraph. Classify each:
- 🟢 **EVIDENCE**: built on a specific detail, quote, data point, scene, or observed behavior. Language serves the evidence.
- 🟡 **MIXED**: some evidence present, but leans on language to fill gaps. Prose is doing 60%+ of the work.
- 🔴 **HOLE**: pure language, no evidence underneath — the writer is "writing around a hole in their knowledge."

Output a paragraph-by-paragraph evidence map using the color codes.

### Step 2 — The 50-Sentence Test
"A great detail will do the work of 50 shitty sentences."

For every 🔴 HOLE paragraph: what one specific detail could replace this entire paragraph? What would you need to know (research, interview, observe) to find that detail? If no detail exists because the legwork hasn't been done, mark it: **MORE REPORTING NEEDED — [what to find out]**.

For every 🟡 MIXED paragraph: what's the detail buried in the language — extract it and rebuild the paragraph around it. Is the language decorating the detail or serving it?

### Step 3 — The Compensation Diagnosis
Identify which specific compensation patterns are at work:

| Pattern | What It Looks Like | Example |
|---|---|---|
| Adjective Inflation | Stacking adjectives to create intensity evidence should provide | "The absolutely stunning, breathtaking vista" → what did it actually look like? |
| Abstraction Escape | Retreating to abstract concepts when concrete details are missing | "She experienced a profound transformation" → what did she actually do? |
| Metaphor Overload | Layering metaphors to manufacture depth without evidence | Three metaphors in one paragraph = one missing fact |
| Emotional Assertion | Telling the reader how to feel instead of showing them | "It was heartbreaking" → what happened that would break a heart? |
| Throat-Clearing | Introductory language delaying arrival at the actual content | "It's worth noting that..." / "Interestingly enough..." |

### Step 4 — The Legwork Prescription
For each 🔴 and 🟡 section, write a specific prescription:
- What you need to find out (the knowledge gap)
- Who might know it (the source)
- What specific detail could fill this hole (the target output)

For content that can't be researched further (opinion or analysis), the prescription differs:
- Replace assertions with specific examples
- Replace abstractions with concrete analogies
- Replace adjective stacks with one precise detail

### Step 5 — The Rewrite
Armed with the diagnosis, rewrite 🔴 paragraphs one of two ways:
1. **If evidence exists but is buried**: excavate the detail, put it in the driver's seat, cut the language that was hiding the hole
2. **If evidence doesn't exist**: either go get it (ideal) or compress the paragraph to its minimum necessary function and move on — never write around it

### Content Type Focus
| Content Type | Focus |
|---|---|
| Profile/Feature | Strictest read — every paragraph should be evidence-driven. 🔴 holes are fatal. |
| Personal Essay | Personal experience IS evidence, but "I felt" is not — "I did" is. |
| Newsletter | Lighter read — opinion is expected, but claims need support. Focus on Adjective Inflation and Emotional Assertion. |
| Ghostwritten Piece | Evidence = the client's actual words, experiences, and data. If you're filling in, you're writing, not ghostwriting. |
| Brand Narrative | Common hole: asserting brand values without showing them in action. Every value claim needs a behavior detail. |

## Output Contract

Deliver, in order:
1. **Evidence Map** — paragraph-by-paragraph 🟢/🟡/🔴 classification
2. **Hole Count** — total 🔴 and 🟡 paragraphs as a percentage of total paragraphs
3. **Compensation Patterns** — which patterns are most active in this draft
4. **Legwork Prescriptions** — specific instructions for filling each hole
5. **Rewritten Sections** — revised 🔴 and 🟡 paragraphs, or flagged MORE REPORTING NEEDED
6. **Evidence Density Score** — 1-10, ratio of evidence-driven to language-driven prose. Passing score is 7+; below 7 means the piece needs more legwork, not more editing.

## Output Skeleton

```
# Reporting Truth Diagnostic — [PIECE]

## Evidence Map
| Paragraph # | Classification | Note |
|---|---|---|
| 1 | 🟢/🟡/🔴 | [what's present or missing] |
...

## Hole Count
🔴 HOLE: [n] ([%] of total)
🟡 MIXED: [n] ([%] of total)

## Compensation Patterns
- [Pattern name]: [where it appears, how often]
...

## Legwork Prescriptions
- Paragraph [#]: Need to find out: [...] | Who might know: [...] | Target detail: [...]
  (or: MORE REPORTING NEEDED — [what to find out])
...

## Rewritten Sections
### Paragraph [#] — Original
[quoted or described]
### Paragraph [#] — Rewritten
[revised text, or "MORE REPORTING NEEDED — not rewritten"]

## Evidence Density Score: [1-10]
[Rationale — 7+ passes, below 7 = more legwork needed]
```

## Quality Gate

- [ ] Every paragraph in the draft receives a classification — none skipped
- [ ] Every 🔴 paragraph either gets a rewrite or an explicit "MORE REPORTING NEEDED" flag — never silently left as-is
- [ ] The Compensation Patterns section names specific instances (quoted or closely paraphrased), not a generic "some adjective inflation present"
- [ ] Rewrites never invent evidence, quotes, or details that weren't in the source draft or provided material — a genuine hole stays flagged, it doesn't get fictionalized closed
- [ ] The Evidence Density Score is reported honestly against the 7+ passing threshold, including when the piece fails

## Creative Latitude

The 50-Sentence Test rewards genuine compression — when excavating a buried detail from a 🟡 paragraph, look for the single most concrete, specific fragment already present rather than writing a new, more polished sentence around the same abstraction. Prescriptions for MORE REPORTING NEEDED sections should be as specific and actionable as a real assignment memo — "talk to someone who knew them" is a weak prescription; "find the person who was in the room when X happened" is a strong one.

## Deploy When

- A draft reads as overwritten, purple, or "trying too hard" and the cause isn't obvious
- Diagnosing why a piece feels hollow despite technically competent sentences
- Before Erosion, as the first step of Draft Repair — diagnose reporting holes first, then erode what remains
