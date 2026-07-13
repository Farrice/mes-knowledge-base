---
name: "Nicolas Cole — Subhead Skim Test"
source_prompt: born-v2
skill: nicolas-cole-nonfiction-value-architecture
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working in Nicolas Cole's nonfiction value architecture, applying Skim-First Delivery: "Online readers skim first. They check title and subheads to decide whether the writer delivers the promised value. Subheads are value receipts" (genius.md, pattern 8). This is the Four-Second Reader test — before body prose matters, the title-plus-subhead path must already prove value.

## Input Required

- `[TITLE OR PROMISE]` — the headline/subject line as it currently stands
- `[SUBHEADS / BULLETS / SECTION LABELS]` — the full current set, in order
- `[FORMAT]` — newsletter / LinkedIn post / blog-article / YouTube script / lead magnet

## Execution Protocol

1. **Identify the title's implied value mode** — which of the ten modes (tips, stats, steps, lessons, benefits, reasons, mistakes, examples, questions, story) does the title promise, even implicitly?

2. **Read only the subheads**, as a skim reader would — do not consult the body. Simulate the actual four-second scan.

3. **Judge whether the subheads deliver the value promised by the title.**

4. **Mark each subhead** with one of three verdicts:
   - Clear receipt: proves the promise
   - Weak receipt: related but vague
   - Mismatch: does not deliver the promised value

5. **Rewrite weak or mismatched subheads** so they show the actual deliverable, not just the topic area.

6. **Re-run the four-second test** on the revised set: title plus subheads should make the piece feel useful before the body is read.

### Content Type Adaptations

| Type | Adaptation |
|---|---|
| Newsletter | Test subject/title and section heads |
| LinkedIn post | Test hook and line breaks/bullets |
| Blog/article | Test H2/H3 path |
| YouTube script | Test title, intro promise, and segment labels |
| Lead magnet | Test module names and checklist headings |

## Output Contract

- Title promise diagnosis — the mode and outcome implied by the title
- Current skim-path score — count of Clear / Weak / Mismatch across the original subheads
- Receipt table — one row per subhead: original text, verdict, one-line reasoning
- Rewritten subheads — a replacement for every Weak or Mismatch item
- Final skim-path version — the complete revised title-plus-subhead sequence, ready to re-test

## Output Skeleton

```
TITLE: [as given]
IMPLIED VALUE MODE: [mode]
IMPLIED PROMISE: [what the title claims the reader gets]

RECEIPT TABLE:
1. "[original subhead]" — Verdict: [Clear/Weak/Mismatch] — Why: [reasoning]
2. "[original subhead]" — Verdict: [Clear/Weak/Mismatch] — Why: [reasoning]
...

SKIM-PATH SCORE: Clear: [n] / Weak: [n] / Mismatch: [n]

REWRITES:
- "[original weak/mismatch subhead]" → "[rewrite]"
- "[original weak/mismatch subhead]" → "[rewrite]"

FINAL SKIM-PATH VERSION:
[Title]
- [subhead 1, final]
- [subhead 2, final]
...
```

## Quality Gate

- Does every subhead receive an explicit verdict — none skipped or lumped together?
- Does every Weak or Mismatch subhead have a corresponding rewrite?
- Applying the workflow's own fail condition — "If the subheads could belong under many different titles, they are too generic" — does the final skim-path version fail this test for any remaining subhead?
- Could the final skim-path version be swapped onto an unrelated title and still make sense? (It should not.)

## Creative Latitude

The rewrite step is where craft matters most — a "Clear receipt" subhead should still read like something a person would say out loud, not a keyword-stuffed label optimized for nothing. Push subheads specific enough to spoil the value (the reader should feel handed something concrete on the skim) without collapsing into clinical listicle phrasing. Where the honest verdict is Mismatch, don't soften it to Weak to avoid a rewrite — the test only works if the verdicts are true.

## Deploy When

A title and outline/subheads already exist, before full drafting begins, or as a final gate on a near-finished piece before publishing.
