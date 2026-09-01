---
description: "Reference-first high-taste moodboard orchestrator: turns discovery briefs, creative objectives, or existing references into three materially different visual territories, actual visual boards, a blind Choose/Keep/Kill taste decision, one comparative proving-surface test, and a selected-direction handoff."
---

# /mood-board — Connected Moodboard Orchestrator

Use this front door when a brand, campaign, product, collection, content system,
event, space, or other creative objective needs a visual foundation before
production. It owns the whole path from a brief or discovery material to a
selected, reusable direction.

This workflow prevents the failure where a written strategy comparison, palette
table, or list of aesthetic adjectives is presented as a moodboard. A moodboard
must contain visual evidence and make the next set of creative decisions easier.

## Function Owner And Composition

`creative-direction` is the sole function owner and conductor. Load
`skills/creative-direction/SKILL.md`, `skills/creative-direction/genius.md`, and
`skills/creative-direction/references/prompts-v2/mood-board.md` before producing.
Load supporting components only at the phase where their judgment changes a
decision.

| Slot | Existing component | Bounded contribution |
|---|---|---|
| Reference acquisition | Refero styles when available; otherwise user-supplied references, web/image research, video frames, or `oren-slop-era-creative-strategy` Reference Edge | Finds and records real visual evidence. Does not choose the final direction. |
| Visual grammar | `creative-direction` five-layer system | Converts references into color, material, type, image, composition, and cultural rules. |
| Taste and sign-off | `oren-taste-development` Moodboard Conversation System | Architects the decision conversation, supplies elimination candidates, and runs `Choose / Keep / Kill`. |
| Proving surface | The smallest appropriate executor for the named surface | Applies each territory to the same real surface. Does not redesign the whole brand. |
| Durable handoff | `/design-md-synthesize`, `/art-direct`, `/storyboard`, or the fitting production owner | Receives only the selected direction lock. |
| Post-production characterization | `/moodboard-sweep` | Runs only after reusable style assets exist; it never replaces moodboard creation. |
| Decision documentation | Andrew Lane design-system methods, when useful | Optional after selection; records decisions and layers but never owns reference research, visual authorship, or taste approval. |

Do not load all components at once. Pass compact handoffs and exact source paths
between phases.

## Inputs

- **Objective:** what the moodboard must help create or decide
- **Audience:** who must recognize, desire, trust, or use the resulting work
- **Brand truth:** positioning, promise, category codes, existing assets, and
  non-negotiables to preserve or deliberately break
- **Desired feeling:** primary emotion, secondary tension, and the response the
  work should create
- **Constraints:** surface, format, rights, accessibility, budget, timeline,
  production capacity, privacy, and approval owner
- **References:** supplied URLs/files/boards, or `starting cold`
- **Proving surface:** the smallest real application that can falsify a weak
  direction; infer one when obvious and state the assumption

Ask at most one question, and only when the missing answer would change the
creative route. Otherwise state assumptions and continue.

## Phase 0 — Intent And Evidence Lock

Write a compact brief:

```text
Building: [brand/campaign/product/content/space]
For: [audience]
Decision the board must win: [one decision]
Make them feel: [primary emotion + secondary tension]
Preserve: [brand truths/assets]
Avoid: [category uniform, taste failure, rights risk]
Proving surface: [one shared surface]
Evidence state: [SUPPLIED / LIVE-RESEARCHED / BUNDLED / INCOMPLETE]
```

If the request contains only vague mood words, do not invent a visual identity
from those words. Use them as hypotheses to test against references.

## Phase 1 — Acquire And Ledger References

Research before direction writing.

1. Start with supplied assets and previous approved boards.
2. When Refero is available, search styles first across three to five genuinely
   different angles and retrieve strong full styles in batches of three or four.
3. For non-UI or culture-heavy work, supplement with source-appropriate image
   research, owned references, user files, archives, books, campaigns, art,
   photography, spaces, packaging, fashion, or video frames.
4. If video is a named reference, follow
   `directives/video-vision-protocol.md`; captions alone cannot establish visual
   claims.
5. Give each kept reference one role and one rights/provenance state.

Create a Reference Ledger:

| Reference | Source path/URL | Observed visual traits | Role | Use boundary |
|---|---|---|---|---|
| [name] | [inspectable source] | [specific, seen traits] | primary / type / layout / imagery / material / reject | owned / generated / licensed / reference-only / unknown |

Reject generic reference names without inspectable sources. Do not cite an
entire brand, film, or movement when the useful evidence is one specific page,
campaign, scene, collection, object, or frame.

### Reference Sufficiency Gate

- At least three credible references per territory.
- At least one reference outside the immediate category across the full set.
- Every reference has a bounded role; no source supplies an unexamined whole
  identity.
- Rights/provenance is explicit.
- If visual research is unavailable, mark the result `PARTIAL` and produce
  research-ready prompts. Do not call a text-only specification a completed
  moodboard.

## Phase 2 — Build Three Territory Hypotheses

Default to exactly three territories. Each must make a different strategic and
sensory argument—not three palettes applied to the same premium-minimal layout.

For every territory define:

- a one-sentence world;
- the audience belief or feeling it is trying to create;
- one primary reference and three to five traits that must survive;
- at most two narrowly borrowed details from secondary references;
- one signature move or `one thing` that gives the world authorship;
- one deliberate tension or convention break;
- explicit rejects and the failure reading they prevent;
- the media strategy: real, owned, generated, stock, illustration,
  product/document capture, or intentional placeholder;
- the five layers: color, texture/material, typography, image direction, and
  cultural lineage.

### Distinctness Gate

The set fails unless:

1. at least four of the five visual layers differ materially between every pair;
2. primary references do not repeat across territories;
3. hiding names and explanatory copy still leaves three visibly different
   boards;
4. no territory is a safer average of the other two;
5. every territory can make the next 20-50 assets easier to recognize and
   harder to imitate.

If the set fails, replace the weakest territory. Do not rename it.

## Phase 3 — Construct Actual Visual Boards

Build one visual artifact per territory. Use real reference images, supplied
assets, verified frames, or generated imagery whose source and role are clear.
The visual board is the primary artifact; the written five-layer specification
is its executor key.

Each board must include:

- 8-12 visual references or source crops with coherent scale and sequencing;
- dominant, supporting, and accent palette roles;
- typography shown in use, not only named;
- material/texture evidence;
- subject, light, crop, composition, and media behavior;
- one signature move shown at useful size;
- one elimination candidate that clarifies the boundary;
- source labels compact enough not to overpower the board.

Use the best available current artifact surface. In Codex Desktop, prefer a
viewable visual artifact and use image generation only when it materially
improves missing imagery. When generation is unavailable, build from verified
references; when neither is available, stop at `PARTIAL` rather than drawing
fake moodboard imagery with decorative CSS boxes.

Paid or quota-heavy generation requires the normal cost gate and explicit
approval. This workflow never authorizes publishing, purchases, external
uploads, or public deployment.

## Phase 4 — Comparative Proving Surface

Apply all three territories to the same smallest real surface. Examples:

- brand: hero, profile header, packaging face, or campaign key frame;
- content: carousel cover, video opener, thumbnail family, or newsletter hero;
- product/UI: landing-page hero or one representative product state;
- event/space: entrance moment, signage cluster, or invitation;
- collection: hero product, lookbook spread, or campaign frame.

Keep content, dimensions, and functional requirements constant. Change only
the visual direction. The test asks whether each board can govern real work,
not which mockup has better copy.

For every variant record:

- what survived from the board;
- what broke under real constraints;
- the first revision axis;
- whether the territory remains recognizable without its label.

If tools or source assets do not permit a real comparative surface, provide the
exact build specification and mark the proving surface `UNBUILT`. Do not count a
written description as proof.

## Phase 5 — Blind Taste Decision

Present the three boards as `A / B / C`. Hide the origin story, strategic
rationale, and recommendation until the decision owner records:

```text
Choose: [A / B / C]
Keep: [one element from a losing territory]
Kill: [one signal that feels borrowed, performed, or unsustainable]
Reason: [one sentence about felt truth and repeatability]
```

The decision conversation captures eliminations as standing rules. It does not
merge all three directions to protect every option. One territory becomes the
spine; at most one bounded signal is borrowed.

## Phase 6 — Lock And Hand Off The Winner

After the human choice, produce a Selected Direction Lock:

```text
Selected territory: [name]
Primary reference: [source]
Preserve: [3-5 signature traits]
Borrow only: [0-1 bounded signal]
Role rules: [what each color/type/media/component is allowed to do]
Reject: [named collapse modes]
Proving-surface result: [PASS / FAIL / UNBUILT]
Open risk: [exact limitation]
Next owner: [design-md-synthesize / art-direct / storyboard / campaign owner / other]
```

Pass only the lock, source ledger, chosen board, proving surface, and open risk
to the next owner. Do not pass every rejected direction into production context.

Use `/design-md-synthesize` when the selected direction needs durable design
tokens. Use `/art-direct` or `/storyboard` for a production brief. Use
`/moodboard-sweep` only after actual style handles or reusable image assets have
been created and need characterization.

## Output Contract

1. Intent and Evidence Lock
2. Reference Ledger
3. Three named territory hypotheses
4. Three actual visual boards, or an explicit `PARTIAL` evidence boundary
5. Five-layer executor key for each board
6. One comparative proving surface with A/B/C variants, or `UNBUILT`
7. Blind `Choose / Keep / Kill / Reason` card
8. Reveal and recommendation held until the human vote
9. Selected Direction Lock and downstream handoff after selection
10. Proof states separating structural verification, human taste, deployment,
    and market performance

## Quality Gate

- Research happened before direction writing and every kept reference is
  inspectable.
- The three territories remain unmistakably different with labels hidden.
- Each board uses actual visual evidence; a written strategy memo is not
  mislabeled as a moodboard.
- Each board argues one direction rather than collecting unrelated likes.
- Reference roles, rejects, media strategy, and rights boundaries are explicit.
- The same proving surface tests all three territories.
- The recommendation stays hidden until the blind vote is recorded.
- The selected direction makes the next 20-50 assets easier to create.
- Andrew Lane, DESIGN.md, generation, and production routes remain downstream;
  none replaces the moodboard function owner.
- Human preference, approval-speed improvement, commercial lift, and market
  performance remain `UNTESTED` until measured.

## Replay Prompt

```text
Run /mood-board on [objective or discovery brief]. Research real references first.
Build three materially different visual territories as actual boards, apply all
three to the same proving surface, and present a blind Choose / Keep / Kill vote.
Do not ship a text-only strategy memo as a moodboard. After my vote, lock one
direction and hand only that direction to the appropriate production owner.
```
