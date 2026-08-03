# Workflow 01 — Fashion Campaign Chain

**Produces:** a **Campaign Direction Document** — the complete pre-generation and post-generation
plan for a fashion/apparel/accessory campaign, from intent through channel-placed deliverables.

**Use when:** a brand, a drop, a collection or a product needs a *campaign* (a coherent set), not a
picture. Also use when previous AI attempts produced six nice images that do not read as one thing.

**Do not use when:** you need one hero frame → `nick-st-pierre` workflow 02. You need many on-brand
assets from an already-decided look → `rory-flynn` `style-code-library.md`. You need moving image →
`dave-clark`.

**Load first:** `genius.md` (the chain, the 18 patterns, the rubric). Then this file.

---

## Before you start — the honesty check

This workflow carries the **spine**. It does not carry prompt craft. At Stage 6 you will be told to
hand off to `nick-st-pierre` / `rory-flynn` for the actual frame construction. Do not simulate that
craft from inside this workflow — that is precisely the failure this skill is documented to avoid
(`references/source-notes.md`).

---

## Stage 1 — INTENT (four axes, before any input is gathered)

Fill all four. An unfilled axis is a revision round you have already scheduled.

- **Purpose** — what this campaign has to *do*. Launch, reposition, sell a specific SKU, reactivate.
- **Audience** — who, specifically. Not a demographic; a person with a life.
- **Emotion** — the one feeling the viewer should leave with. This axis decides lighting and pose.
- **Constraints** — budget, channels, dates, brand-safety limits, what must appear in frame, what
  cannot.

**Gate:** if *emotion* is a list, pick one. If *constraints* is empty, you did not ask.

## Stage 2 — CULTURE READ

What moment is this campaign standing in? Two or three specific reads — a silhouette that is
current, a colour that is everywhere, a mood the category is tired of. Name the thing you are
**deliberately not** doing, too; that is usually the sharper decision.

**Output:** 3–5 bullets. Cite where each read comes from. Do not assert a trend you have not seen.

## Stage 3 — BRAND READ

Research the brand's aesthetic identity *and* its positioning. Extract:
- **2–3 non-negotiable signatures** — the things that are theirs and nobody else's. (Onalaja:
  bold patterns, sculptural silhouettes. Versace: the Greca.)
- **Palette**, with hex where obtainable, anchored to real surfaces not adjectives.
- **Materials** the brand actually uses.
- **Register** — where they sit between austere and maximal, cold and warm, quiet and loud.

**Gate:** if this campaign's boards could be swapped onto a competitor without anyone noticing, go
back. This is the stage that stops AI campaign work being interchangeable.

## Stage 4 — CONCEPT (the hinge)

Write **one sentence** containing **one metaphor**, plus a claim about the buyer.

> Specimen (hers, Onalaja): *"a woman running through the city, a metaphor for the fast-paced rhythm
> of modern life"* — with the claim that stylish women stay stylish however busy their schedule.

Then stress-test it:
1. Does the metaphor **dictate** at least three of {environment, pose, light, time of day, wardrobe}?
   If it dictates nothing, it is a mood.
2. Does the claim about the buyer flatter *them*, not the brand?
3. Could a stylist, a colourist and a caption writer each act on it without asking a question?

**Gate:** one sentence. If it takes two, you have two campaigns — pick one and bank the other.

## Stage 5 — BOARD (moodboard + **loose** storyboard)

Lock exactly four things: **tone · colour · material · theme.** Leave composition open on purpose.

- Build it somewhere cheap and fast. The board is a decision artifact, not a deliverable.
- 6–12 references maximum. A board that argues one direction beats a collage of maybes.
- Beside each reference, write the **one word** you are taking from it. If you cannot, cut it.
- Storyboard the *beats* of the campaign (3–6 frames as a narrative), not the compositions.

**Gate:** the board should be approvable — or killable — in one look.

## Stage 6 — DIRECTION (art direction & styling → shot list → camera → real-life check)

Produce the shot list. **For the frame-level craft, hand off:**
- Frame construction, layered build, reference-over-adjective →
  `skills/nick-st-pierre/workflows/02-*` and its ten-check critique.
- Lighting/flatness diagnosis at DP grade → `skills/dave-clark/` look card.
- If the set is large or must be brand-repeatable → `skills/rory-flynn/` frozen-backbone split.

Per shot, minimum fields: **shot number · role in the narrative · framing/shot type · camera angle ·
subject action · styling · location + time of day · light (one named source, placed) · where the
hero product sits in frame · the one thing this frame must deliver.**

Then the **real-life visualisation check** on every shot: could a crew shoot this? Name the location,
the hour, the lens, and a body that physically fits in that space. Any shot that fails gets rewritten
or cut — impossible geometry, light and fabric physics are what "looks AI" actually means.

**Full shot-list mechanics:** → `workflows/02-lookbook-shot-list.md`.

## Stage 7 — EXECUTION PLAN (generate → composite → unify → place)

You are writing the *plan* here, not doing the work.

**7a. Generation protocol.** Declare the iteration axes before generating — default
**lighting · environment · pose · styling.** Move one axis at a time. Declare the consistency
architecture (which reference locks the face/subject, what anchors the look) rather than hoping prose
delivers it. Declare how many variants per shot and the stop condition.

**7b. Evaluation — Keep / Kill / Push.** *Keep* = serves the concept as-is. *Kill* = good but
off-concept, delete now. *Push* = nearly right on one axis, re-run that axis only.
**Marked INFERRED mechanics — see genius.md Pattern 17.** If nothing was killed, nothing was
evaluated.

**7c. Composite plan — the hero-object fidelity pass.** State up front that the product will render
wrong and budget the pass. Fixed order: **product → subject → background.** Per campaign, name what
specifically must be corrected on the product (hardware, weave, Pantone, logo geometry, proportion).

**7d. Unify.** One grade, decided at set level, applied once across the whole set, **matched to the
brand palette** — not to what flatters each frame. This is what turns a folder into a campaign.

**7e. Place it.** Every deliverable gets a channel: crop, aspect, type, cover lines, carousel order,
layout. Loose images are one stage short of finished.

---

## Output

Deliver the Campaign Direction Document with all seven stages present. A stage you skipped is
written down as skipped, with the reason.

**Execution prompt:** `references/prompts-v2/campaign-direction-document.md` — honor its Output Contract.

---

## Quality gate (from `genius.md`)

- [ ] Concept is **one sentence** with a metaphor and a buyer claim.
- [ ] 2–3 named brand signatures appear, and at least one is visible in the shot list.
- [ ] Every shot passes the real-life visualisation check (location, hour, lens named).
- [ ] Iteration axes declared *before* generation; consistency architecture named.
- [ ] Hero-object fidelity pass is budgeted as a line item, not left to prompting.
- [ ] One series-level grade, matched to brand palette, applied once.
- [ ] Every deliverable is placed in a channel with a crop and format.
- [ ] Frame-level craft is handed off to `nick-st-pierre` / `dave-clark`, not simulated here.

**Grade the eventual output against `https://maisonmeta.io/work`, not against this document.**
