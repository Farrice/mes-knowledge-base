---
description: "/depth-social — deepen a social post (LinkedIn / X / IG / short newsletter) by fixing only its 1–2 weakest depth deficits without breaking the hook, brevity, or scroll-stopping shape. The lightest dose on the dial: most often the deepest move is a cut."
---

# Depth — Social

A social post is the hardest room to deepen, because the function it serves — stop the scroll, hold for fifteen seconds, earn the save — is destroyed by the exact thing most people call "depth": more words. The full stack that saves a novel chapter drowns a 150-word post in essay. This workflow exists to apply real depth at the lightest dose on the dial: diagnose the post on the 8 deficits, fix the one or two weakest links *inside the existing shape*, and leave the hook, the white space, and the brevity untouched. The deepest move here is almost never an addition. It is a single cut, or one abstraction swapped for one image.

This workflow is a **full-stack orchestrator dosed for social** — it conducts architecture/scene/line owners as needed, then calls `/really-real-social` as its truth slot. It does **not** re-implement `/really-real-social`, and it does **not** re-teach craft any owner already owns. Its job is the conductor's job: which deficit, which owner, which order, which dose — then a deepened post and a Depth Receipt. A post that comes back longer than it went in has failed this workflow regardless of how good the sentences read.

## Pre-Flight
Read these files before executing:
1. `skills/writing-depth-layer/genius.md` (the composition brain — § The Deepen Loop, § The Ordering Law, § Per-Vertical Dosing [Social row], § Anti-Duplication Contract)
2. `skills/writing-depth-layer/references/depth-deficit-taxonomy.md` (the 8 deficits + the 0/1/2 severity rubric — score Deficits #2 Hollow, #6 Weak rhythm, #5 Over-explained first; these matter most for social)
3. `skills/writing-depth-layer/references/vertical-dosing.md` (the Social row — dose, deficits that matter most, PRESERVE column, failure mode) and `skills/writing-depth-layer/references/routing-map.md` (the deficit → owner table + the Ordering Law) as needed
4. Load ONLY the owner `genius.md` files for the confirmed deficits, using the real paths from the routing map. Do not pre-load the whole roster.

> **🔒 Pre-Flight Gate**: Before treating, run the **Decision Framework** in `genius.md § Decision Framework`. Confirm you have a *named* set of 1–2 confirmed deficits from an actual diagnosis (not a hunch), that the user asked for a rewrite (not diagnosis-only — that is `/depth-audit`), and that you have named the post's PRESERVE function (the hook, the platform shape). STOP condition: if no diagnosis has run, you cannot load owners — refining slop on a misdiagnosed post is the one unrecoverable error. STOP also if the fix you are reaching for would lengthen the post or change its shape; on social, that is the failure mode the dose exists to prevent.

## Input Required
- **The draft post** — the actual text, with its line breaks and white space intact (the shape is part of the function).
- **The platform / channel** — LinkedIn, X, IG caption, or short newsletter. The platform narrows the PRESERVE list (X wants brevity and punch; LinkedIn wants the first-50 hook and scannable line breaks; IG wants the caption's opening + save-worthy payoff; newsletter-short wants the open and the one-idea spine).
- **The function to protect** — the one thing this post must keep doing: stop the scroll, earn the save, drive the one click. This is the PRESERVE column made concrete.
- *(Optional)* The hook, if the user wants it locked exactly as written (default: preserve it; deepen *below* it).
- *(Optional)* Word/character ceiling — if the platform or user imposes one, the deepened post must come in at or under the original length.

---

## Workflow

Run the DEEPEN LOOP (`genius.md § The Deepen Loop`) dosed LIGHT + FAST for social: **diagnose → select+order → apply → receipt.** Fix 1–2 deficits *max*. Default to subtraction.

### Step 1: DIAGNOSE — score the post, name 1–2 weakest links
Score the post on the 8 deficits using the 0/1/2 rubric in `references/depth-deficit-taxonomy.md`. For social you look hardest at the deficits the Social row flags first — do not manufacture the ones that rarely apply to a post.

| Deficit | Where it hides in a social post | Social-specific note |
|---|---|---|
| #2 Hollow / generic | Could-be-anyone claim; swap the @handle and nothing breaks | **Most common social deficit.** Fix = one telling detail, not three paragraphs. |
| #6 Weak rhythm | Every line the same length; no short line snaps it shut; flat read-aloud | Cadence and white space ARE the format on social — high-value fix, low word cost. |
| #5 Over-explained / bloated | Point made twice; a caveat the scroll didn't ask for; throat-clearing under the hook | On social this fix is a **cut** — usually the single deepest move available. |
| #1 No architecture | Rare on social — the hook usually carries the implicit spine | **Do NOT manufacture architecture a 150-word post doesn't need.** A post is not an essay missing a thesis. |
| #3 Emotionally unearned | Stacked feeling-labels ("this was huge / devastating") with no scene under them | Earn it with one concrete beat, never a confession the post hasn't earned. |
| #4 No signature voice | Default AI cadence; "Here's the thing," "It's not X, it's Y" | Light touch — set the fingerprint without rewriting the post into someone else. |
| #7 Missing telling detail | Adjective where an image belonged ("it was a hard week") | Swap one conclusion for one rendered image; do not stack images. |
| #8 No reader trust | Slow defended open before the hook earns the read; fake-closure bow | A trust wobble on social = a lost scroll; cheap-question signoffs count here. |

Name the **1–2 highest-scoring** deficits as the treatment target. If the post scores clean (no 2s, at most one 1), say so and stop — over-deepening a healthy post is the social failure mode. If only diagnosis was requested, route to `/depth-audit` and do not apply any owner.

### Step 2: SELECT + ORDER — pick only the confirmed owners, sequence by the Ordering Law
Pull the owner(s) for the confirmed deficit(s) from `references/routing-map.md`. Load **only** those rows' `genius.md` (Tier 2) plus the single named command — never bulk-load a skill. Even with just one or two fixes, sequence them by the Ordering Law (`genius.md § The Ordering Law`): architecture → scene/detail → line/rhythm → truth/voice. The deficit numbers are an index, not an apply order.

| Confirmed deficit | Owner to load (real path) | Command to reach for |
|---|---|---|
| #2 Hollow / generic | `skills/michael-connelly-vivid-writing/genius.md` | `/telling-detail-engine` |
| #5 Over-explained | `skills/nicolas-cole-sentence-craft/genius.md` (or `skills/eric-roth-writing-mastery/genius.md`) | `/atomic-compression-density-audit` (or `/content-erosion-protocol`) |
| #6 Weak rhythm | `skills/nicolas-cole-sentence-craft/genius.md` | `/terminal-power-rhythm-engineering` |
| #7 Missing telling detail | `skills/eric-roth-writing-mastery/genius.md` | `/visual-prose-for-copy` |
| #4 No signature voice | `skills/ghostwriting-voice-engine/genius.md` (line-level: `skills/nicolas-cole-sentence-craft/genius.md`) | `/voice-capture` (01) |
| #1 No architecture (rare) | `skills/noah-hawley-storytelling-mastery/genius.md` | `/hawley-theme-engine` |
| #3 Emotionally unearned | handled in the truth slot (Step 4) + optional `skills/eric-roth-writing-mastery/genius.md` `/content-erosion-protocol` | `/really-real-social` |

**Platform-fit pull (mandatory, light):** consult ONE platform owner to confirm the deepened post still wins on its native channel — load only the `genius.md` and the single command:
- LinkedIn shape / first-50 hook → `skills/lara-acosta-linkedin-mastery/genius.md` → `/high-performance-content-engine`, or `skills/diandra-escobar-linkedin-growth/genius.md` → `/first-50-hook-rewriter` (17) / `/save-worthy-content-architect` (18)
- Grip / opening tension (any platform) → `skills/kallaway-word-mastery/genius.md` → `/opening-sentence-forge`, `/grip-and-tension-engine`

This is a *fit check*, not a rewrite engine — it protects the hook and shape, it does not re-architect the post.

### Step 3: APPLY — fix inside the existing shape, default to the cut
Apply each owner's move **into the post**, in Ordering-Law sequence, at the lightest dose that fixes the deficit. Rules specific to social:

- **Try subtraction first.** If #5 is confirmed, cut before you consider adding anything — the cut is usually the deepest move and the lowest word cost. Re-check length after every move.
- **Preserve the hook exactly** unless the user opened it for editing. Deepen *below* the hook; never bury it under throat-clearing.
- **Hold the shape.** Keep the line breaks, the white space, the scannability, the platform-native format. Deepen inside the shape; do not change the shape.
- **One image, not a stack.** For #2/#7, swap one abstraction for one concrete telling detail. Do not turn a post into a scene.
- **Integrate invisibly.** No expert names, no technique labels, no manufactured vulnerability or sentiment the post hasn't earned (`genius.md § Anti-Patterns`).
- **Length ceiling is a hard constraint.** The deepened post comes back at or under the original word/character count. A longer post is a failed dose.

### Step 4: TRUTH SLOT — CALL `/really-real-social` (do not re-implement)
Run the post through **`/really-real-social`** as the final pass to earn the emotion and land the human truth at social dose. This workflow **calls** that command; it never re-teaches its craft (`genius.md § Anti-Duplication Contract`). If #3 Emotionally unearned was confirmed, this is where it lands — let `/really-real-social` carry it, optionally pre-eroded by `/content-erosion-protocol` if the original overclaimed.

### Step 5: RECEIPT — emit the Depth Receipt
End with the Depth Receipt block (verbatim format below). Experts are named **only here** — never inside the deepened post.

---

## Content-Type Adaptations

| Vertical | How this workflow adapts (dose / order / truth slot) |
|---|---|
| **Social** | THIS workflow. LIGHT + FAST, fix 1–2 deficits max, default to the cut, preserve hook + brevity + scannability + platform shape, deepen inside the existing shape. Truth slot = **`/really-real-social`** (called, never reimplemented). Platform fit pulled from Lara Acosta / Diandra / Kallaway. Never balloon a short post into an essay. |
| **Copy** | Out of scope — route to `/depth-copy`. MEDIUM dose, depth without losing conversion; preserve offer logic, CTA, proof, clarity-to-action. Truth slot = `/really-real-marketing`. |
| **Marketing** | Out of scope — route to `/depth-marketing`. Humanity + specificity + belief via Rory Sutherland reframe + Roth; preserve the position. Truth slot = `/really-real-marketing`. |
| **Book / long-form** | Out of scope — route to `/depth-book`. FULL stack, architecture (Hawley) first; the only vertical where the whole ladder runs by default. Truth slot = `/really-real-book`. |
| **Client / personal** | Out of scope — route to `/depth-client`. MEASURED, trusted-advisory; argument architecture (Fareed) + restraint + credibility; never manufacture vulnerability. Truth slot = `/really-real-client`. |

If a "social" piece is really long-form wearing a post's clothing (a 1,500-word LinkedIn essay, a full newsletter), re-confirm the vertical before dosing — the wrong dose breaks the function. When in doubt, ask which vertical; the dose is wrong if the vertical is wrong.

## Output Format

```
DEEPENED POST
[the rewritten post — same shape, same-or-shorter length, hook preserved,
 1–2 confirmed deficits fixed, moves integrated invisibly. No expert names,
 no technique labels in the prose.]

---

DEPTH RECEIPT
- Weakest link found: [deficit name + severity 1/2 — e.g. "#2 Hollow/generic (2)"]
- Moves applied:
    [deficit fixed] -> [move in plain craft terms] -> [expected reader effect] -> [source principle]
    (one line per move; 1–2 lines total for social)
- Truth slot: /really-real-social — [what it earned / confirmed]
- Platform fit: [which owner checked — Lara/Diandra/Kallaway] -> [hook + shape held: yes]
- Dose / vertical fit: SOCIAL — light/fast, [N] deficit(s) fixed, [original length] -> [final length, same-or-shorter]
- Remaining risk: [what still could fail — e.g. "hook strong but payoff line may read soft on X"]
```

The DEEPENED POST and the DEPTH RECEIPT are both mandatory. A `/depth-social` run that returns prose without the Receipt is incomplete.

## Quality Gate

> **🛡️ Anti-Pattern Check**: Before delivering, run the post against `genius.md § Anti-Patterns` and `genius.md § Per-Vertical Dosing` (Social row). Any hit = rebuild that pass and re-check.

- **Not lengthened.** The deepened post is at or under the original length. *If longer:* you confused deepen with lengthen — re-run Step 3 starting from the cut, return only when it fits.
- **Hook + shape intact.** The first line still earns the scroll-stop; line breaks, white space, scannability, and platform-native format are preserved. *If broken:* restore the shape and deepen inside it; do not change the shape.
- **Only confirmed deficits treated.** No owner was applied to a deficit that scored 0; no architecture manufactured for a post that didn't need it. *If a 0 was touched:* revert that move — over-deepening is the social failure mode.
- **Ordering Law respected.** Even with 1–2 fixes, owners were sequenced architecture → scene/detail → line/rhythm → truth/voice. *If inverted:* re-sequence; line-craft before spine yields polished nothing.
- **Truth slot called, not copied.** `/really-real-social` was invoked as the truth pass, not re-implemented locally. *If duplicated:* delete the local craft and route to the command (`genius.md § Anti-Duplication Contract`).
- **Machinery invisible.** No expert names or technique labels in the post; experts live only in the Receipt. Nothing manufactured — no sentiment, vulnerability, or stakes the post hadn't earned. *If the technique stack is felt:* integrate harder, then re-check.

## Common Pitfalls

- **Deepen read as lengthen.** Added paragraphs to "deepen" a 150-word post and killed its scroll-stopping shape. *Recovery:* for social, try the cut first — re-run DIAGNOSE for #5 Over-explained before adding a single word; the deepest social move is usually subtraction.
- **Hook buried under the fix.** Inserted setup or a telling detail *above* the hook and lost the first-50. *Recovery:* deepen below the hook; if the hook was opened for editing, run the platform owner's hook command (`/first-50-hook-rewriter` or `/opening-sentence-forge`) to keep the scroll-stop.
- **Manufactured architecture.** Treated #1 No architecture on a post whose hook already carried the spine, turning a sharp post into a mini-essay with a thesis. *Recovery:* a post is not an essay missing a thesis; revert and confirm #1 actually scored — on social it rarely does.
- **Manufactured vulnerability.** Injected confession or stacked feeling-labels chasing "heart" the post hadn't earned. *Recovery:* depth is earned, never faked — find the one real concrete beat that earns the feeling, or leave the restraint and let `/really-real-social` do the truth pass.
- **Truth slot re-implemented.** Re-taught really-real craft inline instead of calling `/really-real-social`. *Recovery:* enforce the Anti-Duplication Contract — the depth layer composes the truth owner, never duplicates it; route to the command.
- **Wrong vertical, right moves.** Dosed a full newsletter or a 1,500-word LinkedIn essay as a light social post, or vice versa. *Recovery:* re-confirm the vertical and the function to protect before selecting moves; if it's long-form, route to `/depth-book`; the dose is set by the vertical, not the channel's label.
