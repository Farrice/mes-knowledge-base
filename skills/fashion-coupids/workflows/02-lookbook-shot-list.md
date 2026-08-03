# Workflow 02 — Lookbook / Campaign Shot List

**Produces:** a **directed shot list** — one camera-report card per frame, plus the set-level
consistency architecture and the real-life visualisation audit.

**Use when:** a drop, lookbook, editorial or campaign has a concept and a board, and now needs the
frame-by-frame plan. Also the correct entry point when someone says "just generate a few looks" —
this is what should exist first.

**Prerequisite:** Stages 1–5 of `workflows/01-fashion-campaign-chain.md` are done. **You cannot write
a shot list without a one-sentence concept.** If there isn't one, stop and go get one.

---

## Step 1 — Set the set-level constants

Decided once, they bind every card. This is what makes six frames read as one campaign.

| Constant | Decide |
|---|---|
| **World** | One place and one time. "Urban, late afternoon, autumn" — not "various". |
| **Light logic** | One named source from the closed list — *soft diffused · hard direct · studio · golden hour · blue hour* — with a **position** ("hard direct, high and camera-left"). Frames may vary within one logic; they may not switch logics. |
| **Palette** | Brand-anchored, tied to real surfaces (asphalt, wet wool, brushed brass), not adjectives. |
| **Subject** | Who is in this campaign — one person unless the concept demands otherwise. |
| **Consistency architecture** | What locks the subject and the look across frames: the reference that holds identity, the anchor language repeated verbatim in every frame, the seed/style handle if the tool supports one. Name it; do not hope for it. |
| **Hero product** | What must be recognisably accurate, and in which frames it must be readable at thumbnail size. |

## Step 2 — Assign a narrative role to every frame

Before compositions, decide what each frame *does*. A lookbook is a sequence, not a grid.

Common roles: **opener** (establishes the world) · **hero** (the product, unmistakable) ·
**movement** (proves the garment behaves) · **detail** (texture, hardware, fabric hand) ·
**environment** (the world without the pitch) · **closer** (the feeling you want them to leave with).

**Rule:** no two adjacent frames share a role. Two details in a row is a slideshow.
**Rule:** at least one frame is a *detail* — a set with no close texture reads as CGI regardless of
the rest.

## Step 3 — Write one card per shot

```
SHOT 03 — role: hero
Concept beat      what this frame carries from the one-sentence concept
Framing           full body / three-quarter / medium / close / macro
Angle             eye level / low / high / over-shoulder — and why
Subject action    a verb the body is actually doing (not "posing elegantly")
Wardrobe/styling  the specific look, including what is NOT worn
Hero product      where in frame, at what scale, readable at thumbnail? Y/N
Location + hour   a place a crew could stand in, and a clock time
Light             the set-level source, placed for this frame; where the shadow falls
Depth / lens      wide-and-close vs long-and-compressed — and what that does to the story
Motion            what is moving; what is frozen
Must deliver      the one thing this frame fails without
Post note         what will be fixed downstream instead of prompted (product accuracy, background)
```

**Writing standard:** every field must render as a pixel or be cut. "Beautiful lighting", "elegant
mood", "editorial feel" are non-fields. If you are unsure how to specify a field at frame level,
that is the handoff signal — go to `skills/nick-st-pierre/` (construction, reference-over-adjective)
or `skills/dave-clark/` (light, black point, why it reads flat). **Do not fill the gap with adjectives.**

## Step 4 — The real-life visualisation audit

Run every card:

1. **Could a crew shoot this?** Name the location, the hour, the lens. If any is unnameable, the
   frame is not directed yet.
2. **Does the light in the card match the light in the world?** A "golden hour" card with an
   overhead studio shadow is the commonest tell.
3. **Does the body fit the space?** Scale, reach, headroom, where the feet are.
4. **Does the fabric behave?** Weight, drape and motion consistent with the named material.
5. **Is anything in frame physically impossible?** Straps, hardware, hands, reflections, seams.

Any card failing 1–5 is rewritten or cut. This audit is the cheapest anti-slop pass available in
fashion AI — most of what people call "looks AI" is a physics failure, not an aesthetic one.

## Step 5 — Coverage and cut-down

- **Coverage:** for every hero frame, plan one alternative angle and one alternative distance. You
  will need them at layout, and re-generating later breaks consistency.
- **Cut-down:** name the channel crops now (9:16 story, 4:5 feed, 1:1 grid, 16:9 site hero) and
  which frames survive each crop with the product still readable. A hero shot that dies at 9:16 is
  not a hero shot for an Instagram campaign.

## Step 6 — Hand off to execution

State the iteration axes (**lighting · environment · pose · styling**, one at a time), the variant
count per shot, the Keep/Kill/Push evaluation, and the post plan (**product → subject → background**,
then one series grade). Details: `workflows/01-fashion-campaign-chain.md` Stage 7.

---

## Output

The shot list: set-level constants block, one card per frame, the audit result per card, the coverage
and cut-down plan.

**Execution prompt:** `references/prompts-v2/lookbook-shot-list.md` — honor its Output Contract.

---

## Quality gate

- [ ] Every card traces to the one-sentence concept — name the beat it carries.
- [ ] One world, one light logic, one palette, one subject across the set.
- [ ] Consistency architecture is named (reference / anchor / seed), not hoped for.
- [ ] No two adjacent frames share a narrative role; at least one detail frame exists.
- [ ] Every card passes all five real-life visualisation checks.
- [ ] Hero product is readable at thumbnail in at least one frame, and its post-correction is noted.
- [ ] Channel crops named, with the frames that survive each.
- [ ] No field on any card is an adjective standing in for a decision.
