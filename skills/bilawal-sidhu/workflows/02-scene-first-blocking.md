# Workflow 02 — Scene-First Blocking Plan

**Produces:** a **Spatial Plan** for a multi-shot piece — a persistence register (what gets built once and
what gets generated per shot), a grounding plan (which real references get retrieved for what), a per-shot
camera-control artifact, an explicit/implicit routing call per shot, and a spatial-memory ledger that
someone other than you can operate.

**Use when:** the piece has more than one shot in the same place · a location, character, product or set has
to be recognisably the same across shots · a real place has to be right · a long-form piece keeps decaying
into unrelated clips · before generating anything on a job with more than a day in it.

**Load first:** `genius.md` — Groups A, D and the reproducibility gate (Pattern 4).

> **Provenance.** This workflow assembles a planning artifact from doctrine Sidhu argues at length but never
> packages as a template. The principles are directly quoted; the document shape is this skill's. Tags:
> **[BS]** = his stated position, **[SD]** = derived, **[CG]** = craft-general. See
> `references/source-notes.md`.
>
> **This is upstream of prompting and upstream of shot design.** It does not write prompts and does not
> choose lenses. It decides what exists before anything is generated.

---

## Step 1 — Inventory what recurs

List every element that appears in more than one shot: locations, characters, vehicles, products, props,
signage, weather and time of day. For each, record **how many shots consume it**.

This count is the only input to Step 2, and it is the number people never actually take.

**Anything with a count of 1** is a candidate for pure generation. **Anything with a count of 2 or more**
enters the reproducibility gate. **[SD]**

---

## Step 2 — Run the reproducibility gate on each recurring element

The decision rule, in his words:

> *"If I need a perfectly reproducible set that I can shoot multiple takes on… [I] generate it once. And
> then I can shoot all the takes I want."* **[BS]**

| Element consumed by… | Call | Why |
|---|---|---|
| 1 shot, look matters more than identity | **Generate** | persistence isn't worth the setup |
| 2+ shots, or must match a plate | **Freeze** — build it once as an addressable asset before shot one | continuity comes from not re-deciding, not from consistent description (Pattern 18) |
| A real place that has to be *right* | **Freeze + ground** — build it *and* retrieve real reference views (Step 4) | model recall of a place is approximate; retrieved views are exact (Pattern 14) |
| Atmospheric, felt once, no coherence requirement | **Generate**, implicit lane | *"a cozy environment where I want you to feel enveloped by the vibe of the place and don't really care about the exact pixel-perfect execution"* **[BS]** |

The output of this step is the **persistence register**: element · consumed by which shots · call ·
what the frozen asset is · who owns it.

**The failure this prevents** is the single most common defect in multi-shot generative work: shot 4 does
not read as the same room as shot 3, because the room was re-invented four times.

---

## Step 3 — Route each shot: explicit or implicit

Per shot, one question — **does this shot need to be edited, matched, or repeated?** (Pattern 3.)

- **Yes → explicit lane.** Built or captured geometry, addressable, editable, re-renderable. Costs setup,
  buys the ability to change your mind and to shoot it again.
- **No → implicit lane.** Generate it. Costs nothing to try, and you are accepting that the world is a
  variable. *"Genie is very much a slot machine right now"* — that is fine when you only need one pull. **[BS]**

Refuse the tribal version of this argument. He takes neither side; the call is per shot, and a piece will
normally contain both. **[BS]**

**Also route the model by department, not by leaderboard** (Pattern 23): name which traditional craft role's
job each shot is — compositor, matte painter, DP, motion graphics, plate cleanup — and route on that. The
departments outlive the models.

---

## Step 4 — Build the grounding plan (retrieve, don't recall)

For every element where the deliverable requires the *actual* thing to be right:

> *"This system will retrieve the nearest panorama, constantly putting that into context. So the model knows
> what's physically around it, so it doesn't just make up."* **[BS]**

Per element, record:
- **What reference views exist**, and along which viewing directions — the ones the camera will actually see.
- **The gaps.** He diagnoses this exact failure by walking to the far side of a landmark and finding
  invented buildings. Whatever direction you have no reference for is where the model will invent. Either
  get the reference or keep the camera off it. **[BS]**
- **Whether the deliverable needs *anchored* or *accurate*.** He is explicit that anchored generation is
  *"close enough like most image-to-video generations"* and not a match. Anchored is enough for fiction and
  not enough for a real product, a real building or a real person. Decide per element and write it down.

**Anchored fantasy is a legitimate target and often the best one** (Pattern 16): real place as substrate,
impossible event on top. The anchor supplies scale and recognition; the generative layer supplies the event.
Name which elements are playing that role.

---

## Step 5 — Assign a camera-control artifact per shot

Every shot gets an answer to: *what will I look at, before generating, that tells me the camera is right?*
If the answer is "nothing," the shot is uncontrolled (Pattern 1).

| Artifact | When |
|---|---|
| **Greybox render** | precise move, matching, or the shot must survive a look change → hand off to workflow 01 |
| **Annotated plan / still** — line, arrowhead, numbered waypoints, POI circle | the move is a route over a place that already exists as an image (Pattern 10–11) |
| **Pose set / frustums** | recreating a real move or a real captured location |
| **Interactive framing pass** | you don't know what the shot is yet — frame it in a cheap interactive tool, then finish elsewhere (Pattern 24) |
| **None, declared** | a genuinely free shot. Allowed, but say so, so nobody is surprised |

**Note the previz/finish split explicitly per shot.** Framing and finishing are different jobs with opposite
requirements: framing wants interactive and cheap because you are making dozens of decisions; finishing
wants quality and determinism because you are making one. Record which tool class does which. **[BS]**

---

## Step 6 — Write the spatial-memory ledger

> *"These systems don't have spatial memory, and it's you as the human that's sort of managing the spatial
> context for it… but I would posit that the system should do that for you."* **[BS]**

Until they do, it is a document. One table, and it is the actual deliverable of this workflow:

| Element | Frozen asset | Reference views held | Shots consuming | Camera artifact | Lane | Anchored or accurate |
|---|---|---|---|---|---|---|

**The operator test:** hand this to someone who has not been in the conversation. If they cannot generate
shot 7 consistently with shot 2 from this table alone, the ledger is incomplete — and the missing piece is
living in your head, which is exactly where continuity goes to die. **[SD]**

---

## Step 7 — Name the abstraction level you are working at

A closing check against the failure Sidhu names most sharply (Pattern 2):

> *"What we're doing is plumbing. But let's not call it filmmaking or content creation."* **[BS]**

If the composition decisions in this plan are being made inside a node graph or a chain of tool calls,
they are being made at the wrong abstraction level. Nodes are for connecting operations. Space is decided
in a viewport; time is decided on a timeline. Move any decision that is in the wrong place.

---

## Quality gate

- [ ] Every recurring element has a consumption count, and the count drove the freeze/generate call
- [ ] The persistence register exists, and everything consumed by 2+ shots is frozen or explicitly waived
- [ ] Each shot is routed explicit or implicit, with the reason stated as edit/match/repeat
- [ ] Each grounded element declares its reference views AND its gaps, plus anchored-vs-accurate
- [ ] Every shot has a named camera-control artifact, or a declared "none"
- [ ] Previz tooling and finishing tooling are distinguished per shot
- [ ] The spatial-memory ledger passes the operator test — a stranger could shoot shot 7 from it
- [ ] No composition decision is being made inside a node graph
- [ ] Nothing in the plan depends on a specific named product

**Execution prompts:** `references/prompts-v2/scene-first-blocking-plan.md` for the plan;
`references/prompts-v2/camera-path-brief.md` for an individual shot's annotation artifact. Honor their
Output Contracts.
