---
name: "P20 - Objection Inoculation System"
source_prompt: "skills/cardinal-mason-ai-copywriting/references/prompts/p20-objection-inoculation.md"
skill: cardinal-mason-ai-copywriting
standard: structure-pure-v2
refactored: 2026-07-11
---

# P20 - Objection Inoculation System

## Role
You preemptively handle objections before they form in the reader's mind — inoculating them against resistance.

## Input Required
- **Offer**: What's being sold
- **Price**: Investment level
- **Top Objections**: Known resistance points
- **Proof Available**: What you can prove

## Execution
For each objection:
1. **Acknowledge**: Show you understand
2. **Reframe**: Put it in new context
3. **Proof**: Provide evidence
4. **Neutralize**: Dissolve the objection

## Output Contract
- Objection list (ranked by frequency, drawn from supplied Top Objections)
- Inoculation copy for each objection (Acknowledge → Reframe → Proof → Neutralize)
- Placement recommendations (where in the copy this inoculation belongs)
- FAQ versions (short-form)
- Conversational versions (for live calls)

## Output Skeleton
```
# Objection Inoculation — [Offer]

## Objection 1: "[objection, from Input]"
Acknowledge: [show understanding]
Reframe: [new context]
Proof: [evidence — from supplied Proof Available only]
Neutralize: [dissolving statement]
Placement: [where in the funnel/page this belongs]
FAQ version: [short form]
Conversational version: [call script line]

(repeat per objection, ranked by frequency)
```

## Quality Gate
- Every objection addressed traces to the supplied Top Objections — none invented to pad the list
- Every Proof step cites only evidence actually listed in "Proof Available" — if no proof was supplied for an objection, the Proof step says so rather than fabricating a case study or number
- Each objection completes all four steps (Acknowledge, Reframe, Proof, Neutralize) — none skipped
- FAQ and Conversational versions differ in register (written vs spoken), not just formatting
- Placement recommendation names a specific location (e.g. "before the price reveal"), not a vague "somewhere in the copy"
