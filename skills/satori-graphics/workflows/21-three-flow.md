---
description: Commit the layout spine before any grid or style exists — three anchors (Hook / Secondary Detail / Finisher), the traced flow line, and the thumbnail test that verifies the journey reads
---

# 21 — Three-Flow Spine

> **/satori-three-flow** — Every layout is ONE primary journey with THREE committed anchors. Commit them in writing before the canvas opens; verify them at thumbnail size before anything ships.

LIFT audits hierarchy after the fact. Three-flow *originates* it. This is the layout's one-sentence brief applied to space: if you can't name the three anchors, you don't have a layout — you have a field of competing elements.

> *"It provides a clear, streamlined path that helps most viewers absorb the message quickly."* — Satori (Buck Design "Universe '24" walkthrough)

## Pre-Flight Gate

**Use this when**:
- Starting any layout from scratch — poster, cover, landing hero, carousel frame, listing frame, slide
- A draft "has everything on it" but no one can say where the eye is supposed to go
- Prepping a brief for a generation tool (fantastic-posters, product-build) that will otherwise produce evenly-weighted AI-default composition
- Reworking a layout where the essential info (CTA, date, price) keeps getting missed

**Do NOT use this when**:
- The communication problem itself is undefined — run `/satori-comms-brief` first; anchors serve a message, not vice versa
- The failure is comprehension of an *existing* hierarchy — that's `/satori-perception-gap`
- Pure logo work — a logo has one beat, not three (route `/satori-logo-concept`)
- You need the movement *mechanics* (levels 1–6) — that's `/satori-movement-ladder`, which runs after the spine is committed

## Skill Acquisition

```
Load: skills/satori-graphics/genius.md
  ├─ GP-18 (Three-Flow Rule — the spine this workflow commits)
  ├─ GP-19 (Directional Hierarchy — how the anchors get wired next)
  ├─ GP-13 (Communication-Problem-First — what the anchors must serve)
  └─ HK-10 (Subtraction creates hierarchy — quiet the non-anchors)
Load: skills/satori-graphics/references/layout-flow-hierarchy.md
```

## Execution

### Step 1 — Name the Essential Info First (work backwards)

Before choosing a hook, answer: **what must the viewer absorb before leaving?** That is the **Finisher** — logo, CTA, date/location, price, handle. The finisher is committed *first* because it's the anchor amateurs lose.

**Decision forced**: one line — "If they remember nothing else, they leave with ___."

### Step 2 — Commit the Three Anchors

| Anchor | Commit | Size discipline (3-Key Levels) |
|---|---|---|
| **Hook** | The entry point — what stops them | Largest visual. Product brief → the product IS the hook (Yakult: bottle front-and-center, red circle behind it for extra emphasis). Non-product brief → artwork or dominant type can hook (ATTISM: typography hooks; the date is still the finisher) |
| **Secondary Detail** | The middle stop that carries the eye deeper | Slightly smaller — heading, claim, supporting image |
| **Finisher** | From Step 1 | Smallest, positioned where the journey *rests* |

Rules: exactly three. A fourth anchor = a second journey = chaos. Micro-routes (movement L3) may loop *inside* the path later, never replace it. **Largest ≠ most important; largest = entry.**

**Decision forced**: write the spine as `HOOK (element, position) → SECONDARY (element, position) → FINISHER (element, position)`.

### Step 3 — Draw the Flow Line

Trace the physical path between the three anchors (on paper, overlay, or in words: "bottom-right mass → upper-left heading → bottom-left logo"). The Buck exemplar traces a smooth curve across a *triangle* of anchors — not a straight scan. Check:
- The line moves through the design's zones without doubling back
- No non-anchor element sits on the line loud enough to hijack it (rent test those elements: quiet or evict — HK-10)
- Reading-culture default honored or deliberately subverted (top-left entry for LTR unless the hook overrides)

### Step 4 — The Thumbnail Test (verification, not vibes)

> *"Literally take a step back… or shrink it down to a thumbnail size. If the visual path still feels balanced and easy to follow, you've done something right."*

Shrink the comp to ~120px (or stand 3m back). Trace the path with a finger. Verdict per anchor: still wins its beat / lost. If the eye bounces, fix **in this order**: contrast → spacing → alignment. Re-test after each single fix.

**Decision forced**: verdict line — `Thumbnail: PASS / FAIL(fix applied: ___)`.

### Step 5 — Hand Off the Spine

The committed spine feeds forward: grid selection (`/satori-grid-select`) shapes cells around the anchors; directional wiring (`/satori-gaze-path`) builds the path; contrast assignment (`/satori-contrast-stack`) makes each anchor win its beat; temporal beats (movement L6) set punch → linger → release timing.

Execution prompt: `references/prompts-v2/three-flow-spine-spec.md`

## Content-Type Adaptations

| Surface | Hook | Secondary | Finisher | Note |
|---|---|---|---|---|
| **Poster / print** | Product or dominant art | Headline/claim | Logo + date/venue | The ATTISM exception: type hooks, date finishes |
| **Landing page hero** | Hero visual or headline | Subhead/proof line | Primary CTA | Finisher = the click; CTA-blind gap starts here |
| **Social / carousel frame 1** | The scroll-stopper | Hook text payoff | Handle / swipe cue | Only ~1s exists; secondary may collapse into hook |
| **Listing frame (Jen)** | The property beauty shot | Objection-flip line | Price/address/handle | Hook = the frame's thumb-stop |
| **Slide / deck** | The one takeaway visual | Supporting stat | Source/next-step | One journey per slide, never two |
| **Email** | Subject-echo headline | Body promise | Single CTA button | Everything else quiets |

## Output Requirements

A **Three-Flow Spine Spec**: (1) essential-info line, (2) the committed spine `HOOK → SECONDARY → FINISHER` with element + position + size level each, (3) the flow-line description, (4) rent-test verdicts for non-anchor elements on the path (quiet/evict), (5) thumbnail-test verdict with fixes applied, (6) handoff notes (grid/gaze/contrast). Executable by a second designer or generation tool without re-asking.

## Quality Gate

Guards anti-patterns **#17 Uncommitted journey**, **#6 more-equals-better**, **#8 aesthetic-first**.

- [ ] Finisher committed FIRST (essential info named before the hook)
- [ ] Exactly three anchors — no fourth journey
- [ ] Hook is the largest visual OR the exception is explicitly justified
- [ ] Flow line traced and free of hijackers (non-anchors quieted/evicted, not just left)
- [ ] Thumbnail test run with verdict logged; fixes followed contrast → spacing → alignment order
- [ ] Spine written so it's executable downstream without narration

## Related Workflows

- **`/satori-comms-brief`** (15) — upstream: the message the anchors serve
- **`/satori-gaze-path`** (24) — next: wire the directional cues along the spine
- **`/satori-contrast-stack`** (22) — next: assign contrast forms so each anchor wins its beat
- **`/satori-grid-select`** (03) — the grid shapes around the committed anchors
- **`/satori-movement-ladder`** (02) — pick the movement level that choreographs the spine
- **`/satori-perception-gap`** (18) — post-draft: prove the spine actually transmits
