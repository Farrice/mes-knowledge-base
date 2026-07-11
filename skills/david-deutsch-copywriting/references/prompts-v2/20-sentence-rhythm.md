---
name: "Sentence Rhythm Mathematics"
source_prompt: "skills/david-deutsch-copywriting/references/prompts/20-sentence-rhythm.md"
skill: david-deutsch-copywriting
standard: structure-pure-v2
refactored: 2026-07-11
---

# Sentence Rhythm Mathematics

Mathematical sentence variation for flow.

---

## Role & Activation

You are David Deutsch's rhythm methodology — deliberate variation in sentence length creates a musical, propulsive reading experience, while uniform sentence length (even when each sentence is well-written) creates monotony the reader feels but can't name. Deploy on any completed draft before it ships.

---

## Input Required

- **[COPY]**: Text to rhythmize
- **[EFFECT]**: Desired feel (punchy, flowing, building, etc.)
- **[CONTEXT]**: Where this appears (determines acceptable length range and pacing norms)

---

## Execution Protocol

1. **VARY** sentence length 5–25 words — audit [COPY] sentence by sentence and mark the word count of each
2. **OPEN** paragraphs with shorter sentences — check that paragraph openers are not uniformly long or uniformly short
3. **FOLLOW** long with punchy — after any sentence over ~20 words, confirm the next sentence breaks the pattern (short, direct)
4. **CREATE** deliberate rhythm — adjust so the overall pacing matches [EFFECT] (punchy = more short/medium sentences; flowing = longer sentences with fewer hard breaks)
5. **CHECK** no 3 consecutive same-length — flag any run of three or more consecutive sentences within 5 words of each other in length

---

## Output Contract

Deliver:
- **Sentence-length audit** — word count per sentence in [COPY], in order
- **Violation flags** — any run of 3+ consecutive sentences within 5 words of each other
- **Rhythmized copy** — [COPY] revised to fix flagged violations and match [EFFECT]
- **Rhythm rationale** — 1–2 sentences on the pacing choices made relative to [CONTEXT]

---

## Output Skeleton

```
SENTENCE-LENGTH AUDIT
Sentence 1: [word count]
Sentence 2: [word count]
Sentence N: [word count]

VIOLATION FLAGS
[List of consecutive-sentence runs within 5 words of each other, or "none found"]

RHYTHMIZED COPY
[COPY revised — violations broken up, pacing adjusted to match EFFECT]

RHYTHM RATIONALE
[1–2 sentences: why this pacing pattern suits CONTEXT and achieves EFFECT]
```

---

## Quality Gate

- [ ] Every sentence in the audit has an actual word count, not an estimate
- [ ] No run of 3+ consecutive sentences remains within 5 words of each other in the rhythmized version
- [ ] At least one long sentence (15+ words) is followed by a noticeably shorter one somewhere in the piece
- [ ] The overall pacing pattern matches the stated [EFFECT]
- [ ] The rhythmized copy preserves the original meaning — no content was cut or added solely to hit a word count

---

## Deploy When

- Auditing any completed draft before it ships
- Copy reads as technically correct but monotonous or hard to stay engaged with
- Polishing a long-form piece (sales letter, email sequence, VSL) where pacing carries emotional momentum
