---
description: "/deepen — the flagship one-tool conductor: diagnose the 8 depth deficits, fix the 1–3 weakest links in Ordering-Law sequence at the right vertical dose, and return a deepened draft + Depth Receipt. If you only had one command, this is it."
---

# Deepen

Most drafts don't need more — they need the *right less, in the right order*. A piece reads thin because something specific is missing: a spine, a concrete image, a sentence that earns the next one, a feeling the draft asserted instead of built. The mistake is to "improve" everything at once and hand back something longer that still doesn't land. This workflow is the conductor that refuses that move. It diagnoses what depth is actually absent, picks only the owners who fix *those* deficits, sequences them so architecture is set before any sentence is polished, doses by the room the piece plays in, and returns a draft that reads more honest, clearer, warmer, more specific, less defended — with the machinery invisible.

This is the flagship. It owns the full DEEPEN LOOP end to end: it can borrow `/depth-audit`'s diagnostic logic and a per-vertical `/depth-*` orchestrator's dosing, but it stands alone — give it a draft and a vertical and it returns the deepened prose plus the change-map by itself. It re-teaches no craft. Every move loads its owner skill and applies *their* technique into the prose. The only thing this file owns is the order, the dose, and the composition.

## Pre-Flight
Read these files before executing:
1. `skills/writing-depth-layer/genius.md` (the composition brain — § The 8 Depth Deficits, § The Ordering Law, § The Deepen Loop, § Per-Vertical Dosing, § Anti-Patterns)
2. `skills/writing-depth-layer/references/depth-deficit-taxonomy.md` (the 0/1/2 severity rubric + detection signals for all eight deficits — score against this)
3. `skills/writing-depth-layer/references/routing-map.md` (the deficit → owner table; the REAL skill paths and commands — never reference a path not in this map)
4. `skills/writing-depth-layer/references/vertical-dosing.md` (the dose, the truth slot, and the PRESERVE column for the confirmed vertical)
5. Then, and ONLY for the confirmed deficits, each owner's `genius.md` + the single named command from the routing map. Do not pre-load the whole roster — loading an owner you don't need taxes the prose and tempts a fix for a deficit the draft doesn't have.

> **🔒 Pre-Flight Gate**: Before touching the prose, run the **Decision Framework** in `genius.md § Decision Framework` — all five questions. STOP condition: if you cannot name 1–3 confirmed deficits from an actual score (not a hunch), or you do not know the vertical and therefore the dose, you are about to refine slop on a misdiagnosed draft. Diagnose first; that is the one unrecoverable error. If the user asked for diagnosis ONLY, do not run this workflow — route to `/depth-audit`.

## Input Required
- **The draft** — the prose to deepen, pasted in full. Deepen works on what's on the page, never on a description of what the piece is "supposed" to do.
- **The vertical** — social / copy / marketing / book-long-form / client-personal. This sets the dose, the truth slot, and the PRESERVE list *before* any owner is chosen. If ambiguous, ask which one; the dose is wrong if the vertical is wrong.
- **The function to protect** *(infer if unstated, confirm if risky)* — the one thing this draft must keep doing: stop the scroll, convert, hold authority, carry the spine. This is the PRESERVE column made concrete. A deepening move that breaks this function is wrong no matter how good the sentence sounds.
- **The goal / stakes** *(Optional)* — what the piece is for and what's riding on it (a launch, a pitch, a chapter's turn). Sharpens the diagnosis toward the deficits that matter most for the outcome.
- **The scope** *(Optional, defaults to full rewrite)* — surgical inject (one or two confirmed deficits, prose mostly intact) vs. full rewrite. Never full-rewrite when an inject would do.

---

## Workflow

The DEEPEN LOOP, run end to end: **DIAGNOSE → SELECT + ORDER → APPLY → RECEIPT.**

### Step 1: DIAGNOSE (score the 8, name the weakest links)
Diagnose before treating — always. Read the draft once for what it's *about*, then score all eight deficits on the 0/1/2 rubric in `references/depth-deficit-taxonomy.md`. Score against the detection signals, not against a vibe.

| Deficit | The one question that scores it | Severity anchors (0 / 1 / 2) |
|---|---|---|
| 1 — No architecture | Can I name what this is *about*, underneath the topic, in one sentence? | 0: spine nameable, ending pays off opening · 1: theme reachable but buried · 2: paragraphs freely reorderable, no center |
| 2 — Hollow / generic | If I swap the proper noun for a competitor's, does anything break? | 0: concrete & particular · 1: hollow patches · 2: could-be-anyone throughout |
| 3 — Emotionally unearned | Is the feeling *built*, or just *labeled* (melodrama or flatness)? | 0: earned through scene/cost · 1: one over/under-claimed beat · 2: pervasive melodrama or flatness |
| 4 — No signature voice | Strip the byline — would anyone who knows the writer recognize it? | 0: unmistakable fingerprint · 1: thin/intermittent, a tell or two · 2: AI/anyone, default explainer cadence |
| 5 — Over-explained / bloated | Can I lift ~25–30% with no loss of meaning? | 0: lean, each point made once · 1: 10–25% cuttable · 2: ≥25–30% cuttable, ideas re-made |
| 6 — Weak rhythm | Read aloud — does it ride the mouth or fight it? | 0: varied length, terminal punch · 1: flattens in stretches · 2: monotone throughout, fails read-aloud |
| 7 — Missing telling detail | Am I handed the conclusion, or shown the image that produces it? | 0: shows, reader concludes · 1: mixed, key moments told · 2: tells throughout, nothing rendered |
| 8 — No reader trust | Am I held — or rushed, judged, confused, handed fake closure? | 0: held start to finish · 1: one trust wobble · 2: lost/judged/managed, reader bails |

Output one integer per deficit in Ordering-Law order (1→8). Then name the **1–3 weakest links** — the highest-scoring deficits — as the treatment target. A draft scored clean (no 2, at most one or two 1s) needs little or nothing; say so rather than manufacturing work. *(This is the same instrument as `/depth-audit`; the difference is `/deepen` continues past the score into the prose.)*

### Step 2: SELECT + ORDER (pick only the owners, sequence by the law, set the dose)
Three sub-decisions, in this order:

1. **Set the dose first — from the vertical, not the draft's ambition.** Open `references/vertical-dosing.md` to the confirmed vertical's row. Lock the **dose** (light/medium/heavy), the **truth slot** (`/really-real-social` / `-marketing` / `-book` / `-client`), and the **PRESERVE list** (the function forbidden to break). Social = LIGHT + FAST, 1–2 deficits max, often a cut. Book/long-form = FULL STACK. The dose caps how much you may touch.
2. **Select only the owners for confirmed deficits.** From `references/routing-map.md`, load exactly the rows for the named weakest links — nothing more. A deficit scored 0 gets no owner; routing one risks over-deepening (a 150-word post becoming an essay).
3. **Order by the Ordering Law, not by deficit number.** Sequence the selected owners:

| Order | Layer | Owners (load `genius.md` + named command) | Treats deficits |
|---|---|---|---|
| 1st | **Architecture (spine first)** | Noah Hawley — `skills/noah-hawley-storytelling-mastery` → `/hawley-theme-engine`, `/hawley-ending-first` | 1 |
| 2nd | **Scene + telling detail** | Eric Roth — `skills/eric-roth-writing-mastery` → `/visual-prose-for-copy`; Michael Connelly — `skills/michael-connelly-vivid-writing` → `/telling-detail-engine` | 2, 7 |
| 3rd | **Line / rhythm** | Nicolas Cole — `skills/nicolas-cole-sentence-craft` → `/atomic-compression-density-audit`, `/terminal-power-rhythm-engineering`; Lamott-Allen technical-craft — `skills/lamott-allen-really-real-writing` → `/really-real-silence`, `/really-real-attention` | 5, 6 |
| 4th | **Truth + voice (LAST)** | Lamott-Allen really-real → the vertical's `/really-real-*` truth slot; voice owners (`skills/ghostwriting-voice-engine` → `/voice-capture`; `skills/nicolas-cole-sentence-craft` → `/terminal-power-rhythm-engineering`; `skills/lara-acosta-linkedin-mastery` → `/ghostwriting-voice-scaling-system`) | 3, 4 |

If the confirmed set is, say, Deficits 4 and 1, you still run architecture (1st) before voice (4th). Inverting the order yields well-crafted sentences with no spine.

### Step 3: APPLY (run each owner's move INTO the prose, in sequence)
Work down the ordered layers from Step 2. For each confirmed deficit: load that owner's `genius.md` + the single named command, and apply *their* move into the draft — never re-implement it here. Preserve the user's core meaning and voice throughout; you are deepening their piece, not replacing it with yours.

- **Hold the PRESERVE list as a hard constraint** at every move. If a change touches the hook, the CTA, the offer, the proof, the position, or the spine, it must *strengthen* that function or it doesn't go in.
- **Call the truth slot — never duplicate it.** When Order Step 4 fires, run the vertical's `/really-real-*` pass; do not re-teach really-real craft inside this workflow. (Marketing belief layer: `skills/rory-sutherland-marketing` → `/conspiratorial-reframe-engine`. Client argument spine: `skills/fareed-zakaria-writing-mastery` → `/high-stakes-argument-architecture`.)
- **Deepen ≠ lengthen.** On a Deficit 5 finding, and on social especially, the move is the cut. Try subtraction before addition.
- **Integrate invisibly.** No expert names, no technique labels, no "now applying the telling-detail move" inside the prose. The reader feels the effect, never the machinery. Experts are named only in the Receipt.

### Step 4: RECEIPT (hand back the change-map)
End with the Depth Receipt (verbatim block in Output Format). This is where — and the *only* where — experts and moves are named. The receipt is what makes the deepening auditable: weakest link found, each move in plain craft terms with its expected reader effect and source principle, the dose rationale, and the remaining risk.

## Content-Type Adaptations
| Vertical | How `/deepen` adapts (dose / order / truth slot) |
|---|---|
| **Social** (LinkedIn / X / IG / newsletter short) | LIGHT + FAST. Fix 1–2 deficits *max* — usually #2 hollow, #6 rhythm, or a #5 cut. Don't manufacture architecture (#1) a 150-word post doesn't need; the spine is usually already implicit in the hook. PRESERVE the hook, brevity, scannability, platform-native shape. Truth slot: `/really-real-social`. The deepest move is often subtraction — deepen *inside* the existing shape, never change the shape. |
| **Copy** (ads / VSL / landing / email / offers) | MEDIUM — depth WITHOUT losing conversion. Suspect #2 (vague benefit → telling detail), #4 (sounds like every ad), #3 (sentiment without proof). Add conviction, specificity, voice into the existing conversion skeleton; never re-architect the funnel. PRESERVE offer logic, CTA, proof, clarity-to-action. Truth slot: `/really-real-marketing`. Literary flourish never beats clarity-to-action. |
| **Marketing / Brand** | MEDIUM-HEAVY on humanity + belief. Suspect #2 (could-be-any-brand), #3 (manufactured warmth), #4 (no voice). Run the Rory Sutherland reframe + Roth specificity until the brand sounds like a human who believes something. PRESERVE the belief/position and the strategic frame. Truth slot: `/really-real-marketing`; belief layer via `/conspiratorial-reframe-engine`. Specificity serves belief, not decoration. |
| **Book / long-form / novel** | FULL STACK — the only vertical where the whole Ordering Law runs by default. Architecture (#1, Hawley) matters MOST — set the spine before any line work; then #7 detail, #3 earned emotion, #8 reader trust. PRESERVE the spine/theme once set, narrative continuity, the reader's earned trust across the arc. Truth slot: `/really-real-book`. Deep ≠ long — a deepened chapter often cuts a scene. |
| **Client / personal-brand** | MEASURED — trusted-advisory prose with restraint. Suspect #1 (argument has no spine, via Fareed `/high-stakes-argument-architecture`), #8 (throat-clearing, fake closure), #5 (proving what's already trusted). Depth shows as authority and clarity, not ornament. PRESERVE the claim→evidence→so-what architecture, credibility (no overreach), and the restraint of a trusted advisor. Truth slot: `/really-real-client`. Never manufacture vulnerability for "relatability." |

## Output Format
```
## DEPTH DIAGNOSIS
Vertical: [social / copy / marketing / book-long-form / client-personal] · Dose: [light / medium / heavy]
Function to protect (PRESERVE): [the one thing this draft must keep doing]
Deficit scores (Ordering-Law order, 0/1/2):
  1 No architecture: [n]   2 Hollow/generic: [n]   3 Emotionally unearned: [n]   4 No signature voice: [n]
  5 Over-explained: [n]    6 Weak rhythm: [n]      7 Missing telling detail: [n]   8 No reader trust: [n]
Weakest link(s) — treatment target: [the 1–3 highest-scoring deficits]
Apply order (Ordering Law): [e.g. #1 architecture → #7 detail → #3 truth]

## DEEPENED DRAFT
[The rewritten prose. Same meaning, same voice — more honest, clearer, warmer, more specific, less defended.
 No expert names, no technique labels on the page. The machinery is invisible.]

DEPTH RECEIPT
- Weakest link found: [deficit(s)]
- Moves applied:
    [deficit fixed] -> [move in plain craft terms] -> [expected reader effect] -> [source principle]
    (one line per move, in apply order)
- Dose / vertical fit: [why this dose for this vertical; what was deliberately left untouched]
- Remaining risk: [what still could fail]
```

## Quality Gate
> **🛡️ Anti-Pattern Check**: review the output against `genius.md § Anti-Patterns` and `genius.md § Anti-Duplication Contract` before delivering. Flag and fix any violation.
- **Diagnosis ran before the rewrite.** All eight scored, 1–3 weakest links named — not a hunch. No diagnosis, no rewrite. If you treated a deficit you never scored, rebuild from Step 1.
- **Ordering Law respected.** Architecture → scene/detail → line/rhythm → truth/voice. If any line-craft move ran before the spine was set on a draft that needed a spine, re-sequence — well-crafted sentences with no center is the signature failure.
- **Only confirmed deficits treated.** Every move maps to a deficit scored 1 or 2. A deficit scored 0 got no owner. If you "improved" a clean dimension, you over-deepened — return it.
- **Deepen, not lengthen.** Did the draft get longer by default? On social and any #5 finding the move should have been a cut. If length grew without a deficit demanding it, rebuild leaner.
- **Function preserved.** The PRESERVE item (hook / CTA / offer / proof / position / spine) is intact or stronger. If a "literary" move blurred the next action or dissolved the position, it doesn't ship.
- **No machinery on the page.** No expert names, no technique labels, no manufactured trauma or false vulnerability in the prose. Experts appear ONLY in the Depth Receipt. If a reader can feel the technique stack, integrate harder.
- **Composed, never duplicated.** Every move ran through its owner's real command; the truth slot was *called* (`/really-real-*`), not re-implemented. If craft got re-taught inside this file's run, route to the owner instead.

## Common Pitfalls
- **Refine-before-diagnose.** Jumped straight to rewriting because the weak spot "looked obvious," fixed the wrong deficit, and made the prose worse. Recovery: stop, run Step 1's full eight-deficit score, and treat only what scores 1 or 2.
- **Inverted order.** Polished sentences and earned the emotion before establishing the spine, ending with beautiful prose that means nothing. Recovery: obey the Ordering Law — return to architecture (Hawley) first, set the center, then re-run the line and truth passes on top of it.
- **Over-deepened social.** Turned a 150-word scroll-stopper into a 600-word essay chasing "depth." Recovery: re-confirm the dose from the vertical, fix 1–2 deficits max, try the cut (#5) first, and deepen inside the existing shape.
- **Function sacrificed for feel.** Produced a gorgeous sentence that buried the CTA, dissolved the position, or drifted the spine. Recovery: hold the PRESERVE column as a hard constraint — any move touching the protected function must strengthen it or be reverted.
- **Truth slot re-implemented.** Re-taught really-real craft inside this workflow instead of calling the matching `/really-real-*` pass. Recovery: enforce the Anti-Duplication Contract — compose the truth-slot owner, never duplicate it; route to `/really-real-social` / `-marketing` / `-book` / `-client`.
- **Over-scoped the ask.** Full-rewrote when a surgical inject would do, or rewrote when the user asked for diagnosis only. Recovery: match scope to the ask — diagnosis-only routes to `/depth-audit`; a one-deficit fix is an inject, not a teardown.
- **Manufactured sentiment.** Injected confession or false intimacy a client/marketing draft hadn't earned, chasing "heart." Recovery: depth is earned, never faked — find the real specific detail that earns the feeling, or leave the restraint intact.
