---
description: Orchestrate high-taste writing, content, and copy when drafts are structurally sound but not compelling, generic, flat, AI slop, poor-flowing, or low-taste
---

# /high-taste-writing-os - High-Taste Writing OS

## Purpose

Make writing and copy outputs feel inevitable, elegant, specific, and worth consuming. This is the companion OS layer for moments when a draft is structurally sound but still reads as flat, generic, low-taste, poorly flowing, or obviously AI-shaped.

This is not another scorecard. It is an ordered craft system: one writing owner, multiple narrow specialist passes, explicit handoffs, and a final evidence ledger showing what changed.

## Trigger

Use this before finalizing substantial written work when any of these are true:

- The user says the work is generic, flat, low-taste, "AI slop," poorly flowing, not interwoven, or only 3-6/10.
- The output is public, revenue-critical, client-facing, or meant to build authority.
- The work needs a perspective shift, original language, reader pull, narrative flow, or high craft.
- The draft is elegant or structurally sound but the message still makes the reader decode the offer, problem, or point.
- A copy gate, excellence gate, or prose classifier passed but the user still rejects the writing.
- Multiple experts were "used" but the final draft feels patched together rather than composed.

Allowed skips:

- Tiny factual answers.
- Pure code or machine-readable output.
- User explicitly asks for raw notes, strategy only, or no polish.

## Operating Principle

One composer, many scalpels.

Do not let every expert rewrite the piece independently. The orchestrator owns the final voice and flow. Specialists diagnose one layer at a time, then the composer integrates only the changes that improve the piece.

## Required Component Stack

| Layer | Primary Asset | Job |
|---|---|---|
| Taste calibration | Brandon Jacoby `System Taste Elevation`, Nate B Jones `AI Quality Gatekeeping Protocol` | Find average-producing defaults, hollowness, and good-enough failure. |
| Reader pull | Kallaway `Flat-to-Addictive Rewrite` and Lara Acosta for LinkedIn when relevant | Create prediction, rehook, stakes, and scan behavior without gimmicks. |
| Writing mechanics | Nicolas Cole EDAN | Fix over-explanation, missing action, weak narration, and paragraph function. |
| Prose craft | Eric Roth Content Erosion / Visual Prose | Add residue, theme, scene cuts, and sensory/visual specificity where appropriate. |
| Direct-response mechanics | Sam Parr Copywriting Mechanics | Improve headline gravity, curiosity gaps, proof-first angle, copywork benchmark, rhythm, story desire, and objection-by-detail when those are the weak links. |
| Conversion | Copywriting Agent, Cardinal Mason, Luke Iha, Publishable Copy Gate | Use only when the piece must sell, convert, or create a concrete next action. |
| Message clarity | `/low-cognitive-load-message-gate`, Donald Miller cognitive-load skill | Use only when a brand, product, service, or offer message is cognitively heavy before craft polish. |
| Calibration | `prose_classifier.py`, `publishable_copy_guard.py`, user-calibrated baseline | Support evidence, not proof by itself. |

Use at most three primary craft lenses per pass. Load more only when a specific failure requires it.

Run `/low-cognitive-load-message-gate` as a bounded scalpel pass, not as another scorecard. It should produce a stop/continue handoff for one-problem clarity, phrase load, hero/guide fit, and repeatability; this workflow still owns the final composition quality.

## Skill System Contract

| Field | Contract |
|---|---|
| Source evidence | Existing draft, user critique, intent ledger, voice/source material, and relevant artifact path. |
| Objective | Produce a final written piece that has reader pull, high taste, clear flow, and concrete purpose. |
| Components | Writing Agent, Copywriting Agent, Jacoby, Nate, Kallaway, Cole EDAN, Roth, platform/copy gates as needed. |
| Step order | Intent lock -> quality baseline -> material ledger -> architecture map -> composed draft -> craft passes -> evidence ledger -> final render. |
| Inputs | Audience, desired reader effect, draft or raw material, constraints, examples, proof, CTA if any. |
| Outputs | Reader contract, failure diagnosis, architecture map, final draft, taste evidence ledger, remaining risk. |
| Handoff summary | Each pass reports only diagnosis, top 1-3 changes, and exact lines affected. |
| Human checkpoint | Before publishing, outreach, client delivery, or when taste direction changes the core message. |
| Validation | Prose classifier, relevant guards, routing checks, side-by-side read, and user-calibrated scoring. |
| Result surface | Rendered Conversation Document first; Local Markdown Source only for persistence. |
| Context policy | Keep workflow hot, load expert files cold and only for the active pass. |
| Reuse hook | Writing Agent, Copywriting Agent, Publishable Copy Gate, Autopilot, Orchestrate, revenue/content artifacts. |

Local Markdown Source rule: if a polished written piece is saved locally, it must open with readable content, not visible metadata. Put metadata in a sidecar `.metadata.json` file and run `python3 execution/artifact_frontmatter_guard.py [artifact path]` before finalizing.

## Phase 1: Reader Contract

Before writing, lock the reader experience.

| Question | Required Answer |
|---|---|
| Who is this for? | Name the specific reader and their current mental state. |
| What should they feel first? | Curiosity, recognition, threat, relief, desire, or intellectual surprise. |
| What should they keep reading to find out? | One live question, not a vague theme. |
| What belief should move? | From old belief to new belief. |
| What should they do next? | One action, or no action if the piece is pure thought leadership. |

If this table is weak, do not draft yet.

## Phase 2: Quality Baseline

Score the current draft honestly before revision.

| Dimension | Failure To Diagnose |
|---|---|
| Reader pull | No open loop, predictable setup, no stakes. |
| Flow | Paragraphs are ordered logically but not emotionally. |
| Taste | Sounds correct but not selective, surprising, or inevitable. |
| Specificity | Uses category language instead of concrete scenes, phrases, examples, or buyer reality. |
| Sentence craft | Uniform rhythm, list symmetry, weak verbs, generic abstractions. |
| Perspective shift | Says a known idea in a known way. |
| Voice | Could be written by any competent AI or consultant. |
| Purpose | CTA, proof, or reader payoff is vague. |

If the user gave a score, start there. Do not preserve internal scores that conflict with the user's read.

## Phase 3: Material Ledger

Collect better raw material before trying to sound better.

Required material:

- one private sentence from the reader,
- one concrete image, scene, or artifact,
- one proof or demonstration moment,
- one thing the piece refuses to say,
- one sentence that could only come from Farrice's taste/worldview,
- one tension pair: what the market says versus what the reader privately experiences.

Writing improves when the material improves. If the material ledger is thin, stop and gather more.

## Phase 4: Architecture Map

Build the piece before polishing it.

| Layer | Decision |
|---|---|
| Hook | The first sentence creates a real question or private recognition. |
| Rehook | Every 6-8 lines renews the reason to continue. |
| EDAN mix | Explanation, Description, Action, and Narration are deliberately balanced. |
| Proof path | Claims are followed by artifact, example, consequence, or mechanism. |
| Emotional order | The reader feels seen before being taught. |
| Turn | The piece contains one sharp "I thought X, but actually Y" shift. |
| Residue | The final line or CTA leaves a phrase, image, or action behind. |

## Phase 5: Composed Draft

Write the draft once, in one voice. Do not paste together expert outputs.

Use this order:

1. Open with the reader's live question or private alarm.
2. Create stakes before teaching.
3. Move through one controlled turn.
4. Demonstrate instead of describing the mechanism.
5. Compress the lesson.
6. End with residue or one concrete action.

## Phase 6: Scalpel Passes

Run only the passes that match the failure.

| Failure | Pass |
|---|---|
| Clear but lifeless | EDAN block map, then Roth erosion. |
| Logical but boring | Kallaway loop/re-hook pass. |
| Correct but hollow | Nate hollowness forensics and material infusion. |
| Average or too safe | Jacoby pattern/invention and good-enough breakthrough. |
| Pretty but unclear | Cole EDAN explanation/action rebalance. |
| Compelling but not converting | Copywriting Agent and Publishable Copy Gate. |
| Weak hook/proof/rhythm despite clear idea | Sam Parr Copywriting Mechanics with before/after behavior delta, then composer integration. |
| Over-scored | Copy Gate Score Calibration solution and score cap. |

Each pass must produce:

- top 1-3 issues,
- exact changed lines,
- what was preserved,
- what was cut,
- remaining risk.

## Phase 7: Taste Evidence Ledger

The final answer or artifact must include this compact ledger for high-stakes writing:

```markdown
## Taste Evidence Ledger
| Layer | Before | After | Why It Improved |
|---|---|---|---|
| Reader pull | [old issue] | [new move] | [mechanism] |
| Flow | [old issue] | [new move] | [mechanism] |
| Specificity | [old issue] | [new move] | [mechanism] |
| Sentence craft | [old issue] | [new move] | [mechanism] |
| Perspective shift | [old issue] | [new move] | [mechanism] |

**Verdict:** PASS / REVISE / REWORK
**User-calibrated baseline:** [score or critique]
**Score discipline:** [why scores are capped or proof-backed]
**Remaining risk:** [specific]
```

No 9+ score without live market/user proof, a validated benchmark comparison, or explicit user approval.

## Fail Conditions

Revise before final if:

- the draft still sounds like a framework explaining itself,
- the opening is clever but not legible,
- the piece teaches before creating reader recognition,
- experts appear as named decorations instead of changed lines,
- the flow is only outline-logical, not reader-emotional,
- the prose has list symmetry, perfect parallelism, or generic consultant texture,
- the CTA is bolted on,
- the final piece has no memorable residue.

## Agent Integration

Writing Agent uses this OS for essays, narrative, long-form, voice, and thought leadership when quality/taste matters.

Copywriting Agent uses this OS before `/publishable-copy-gate` when public or revenue copy is structurally correct but lacks flow, taste, reader pull, or perspective shift.

Autopilot and Orchestrate should surface this route for "generic," "flat," "AI slop," "poor flow," "high taste," "irresistible content," "perspective-shifting writing," and "make our agents write better."
