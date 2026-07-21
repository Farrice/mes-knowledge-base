---
name: "Satori Graphics — Three-Flow Spine Spec"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
---

## Role & Activation

You are committing a layout spine using Satori's **Three-Flow Rule**: every layout is ONE primary journey with THREE committed anchors — Hook (entry), Secondary Detail (middle stop), Finisher (where the eye rests and absorbs the essential info). The spine is committed in writing before grid or style exist, and verified at thumbnail size.

> "It provides a clear, streamlined path that helps most viewers absorb the message quickly." — Satori
> "Look at your design from a distance or shrink it down to a thumbnail size. If the visual path still feels balanced and easy to follow, you've done something right." — Satori

## Input Required

- **[SURFACE]** — poster / landing hero / carousel frame / listing frame / slide / email / other
- **[COMMUNICATION PROBLEM]** — the one-line message this layout must transmit
- **[ESSENTIAL INFO]** — what the viewer must absorb before leaving (CTA, date/location, price, logo, handle)
- **[AVAILABLE ELEMENTS]** — the content on the table: imagery, headline, copy blocks, marks
- **[AUDIENCE + FEELING]** — who views it and the target feeling (GP-14)

## Execution Protocol

### Step 1 — Finisher First
Commit the essential info as the Finisher before choosing a hook: "If they remember nothing else, they leave with ___." The finisher is the anchor amateurs lose.

### Step 2 — Commit the Three Anchors
Hook = largest visual (product brief → the product IS the hook; non-product → art or dominant type may hook while essential info still rides the finisher — the events-poster exception: largest ≠ most important; largest = entry). Secondary = slightly smaller middle stop. Exactly three anchors — a fourth = a second journey = chaos. Micro-routes may loop inside the path, never replace it.

### Step 3 — Draw the Flow Line
Describe the physical path between anchors (e.g., "bottom-right mass → upper-left heading → bottom-left logo" — a curve over a triangle of anchors, not a straight scan). Rent-test every non-anchor element sitting on the line: quiet or evict.

### Step 4 — Thumbnail Test
Shrink to ~120px / step 3m back; trace the path. Eye bounces → fix in strict order: contrast → spacing → alignment; re-test after each single fix.

### Step 5 — Handoff Notes
Name what runs next: grid selection around the anchors, directional wiring, contrast assignment, temporal beats.

## Output Contract

A Three-Flow Spine Spec: the essential-info line, the committed spine (element + position + size level per anchor), the flow-line description, rent-test verdicts, thumbnail verdict with fixes, and handoff notes — executable by a second designer or generation tool without re-asking.

## Output Skeleton

```markdown
# Three-Flow Spine — [layout name]

## Essential Info
If they remember nothing else: [...]

## The Spine
- HOOK: [element] @ [position] — [size level / what makes it win first]
- SECONDARY: [element] @ [position]
- FINISHER: [element] @ [position]

## Flow Line
[path description]

## Rent Test (non-anchor elements on the path)
- [element]: QUIET / EVICT — [reason]

## Thumbnail Verdict
PASS / FAIL → fix applied: [contrast|spacing|alignment change]

## Handoff
- Grid: [...] · Gaze path: [...] · Contrast: [...] · Beats: [...]
```

## Quality Gate

- Finisher committed before the hook
- Exactly three anchors; no competing journey
- Hook = largest visual OR the exception explicitly justified
- Flow line free of hijackers (quieted/evicted, with reasons)
- Thumbnail test logged with ordered fixes

## Creative Latitude

The anchors are the discipline; their placement is the taste. The Buck exemplar launches from the bottom-right — reading-culture defaults are a starting bias, not a law. The creative act is an unexpected entry point that still resolves into a calm three-beat path.

## Deploy When

Starting any layout from scratch; rescuing a draft where "everything is on it" but nothing wins; briefing generation tools that would otherwise produce evenly-weighted composition. Not for logos (one beat), not before the communication problem exists.
