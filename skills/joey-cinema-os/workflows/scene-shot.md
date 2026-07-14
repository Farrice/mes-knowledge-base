---
description: Scene plate + video shot pair — Mode 3 cinema-prose plate mode-matched to the eventual video, then a block-structured Seedance prompt with Frame Map, Subject Locks from canonical refs, FOV degrees, timestamped beats, Capture Realism, and asked-never-assumed runtime
---

# `/jcin-scene-shot` — Scene Plate + Video Shot

Produces the two artifacts of a single shot: **Part A** — the still scene plate (Banana Pro Mode 3, cinema-prose), and **Part B** — the block-structured Seedance video prompt that consumes it. Run both for a new shot; run Part B alone when an approved plate already exists. Grammar is mode-matched across both — the plate is shot on the same camera package the video will use.

## Pre-Flight Gate

- [ ] **Every named subject is built.** Character/product without a canonical reference → kick back to `/jcin-character-lock` / `/jcin-product-lock`. The worldbuilder refuses unbuilt characters — so does this workflow.
- [ ] **Character gate + tags** (worldbuilder — SESSION OPENER): first shot of a session, ask once — recurring characters? built or needs developing? what tag names? Tags are user-named, never invented, carried for the whole session.
- [ ] **Bible payloads pulled** if a bible exists: Movement/Stillness → Subject Lock, Speech → Sound Bed, aesthetic era → grade, production rules → rule layer (worldbuilder — OPTIONAL HANDOFFS: Story bible pairing).
- [ ] **This shot is on a costed plan** (or Farrice explicitly waived planning for a one-off). Duration declared; genie math: ~117 credits per 13s 1080p Seedance generation.
- [ ] **Surface known:** Higgsfield MCP (@tags live) or Fal wrapper (de-tag to prose; seedance-1080p HARD-BLOCKED).

## Skill Acquisition

1. `skills/joey-cinema-os/genius.md` — patterns 7-14 (prompt physics)
2. `skills/banana-pro-director/SKILL.md` — Part A grammar. Sections by name: MODE 3 — CINEMATIC SCENE PLATE, THE SILENT 6-BLOCK MENTAL CHECKLIST, RESOLUTION-AWARE DETAIL RULE, THE CINEMA-PROSE REGISTER, THE FIVE-PARAGRAPH PROSE STRUCTURE, KEY WRITING RULES FOR THE PROSE REGISTER, CANONICAL MODE 3 PROMPT — REFERENCE EXAMPLE.
3. `skills/cinema-worldbuilder-pro/SKILL.md` — Part B grammar. Sections by name: WRITE THE VISIBLE, POSITIVE PHRASING, ELEMENT TAGS, PRE-PROMPT CONFIRMATION, TWO-PART DELIVERY FORMAT (block order), DISTRIBUTED STYLE, FOV DEGREE TABLE, CUTS & TIMING PRECISION SCALE, MODE-SELECT TABLE, MODE CAMERA CAPTURE LINES, CANONICAL BLOCKS — REFERENCE (Capture Realism especially), PRE-DELIVERY PASS.

Both skills' blocks are LOCKED verbatim — slot scene specifics into them; never rewrite them.

## Execution

### Step 1 — Pick the cinema mode ONCE, for the video

Select from the worldbuilder MODE-SELECT TABLE (M1 Narrative / M2 Studio / M3 Action / M4 Performance / M5 Atmospheric) based on what the eventual VIDEO is. The plate inherits this mode — Banana Pro's Mode 3 camera-grammar table maps the same five modes. A plate shot in the wrong register fights every video generated on top of it.

### Part A — Scene plate (Banana Pro Mode 3)

**Step 2 — Compose silently.** Run the SILENT 6-BLOCK MENTAL CHECKLIST (Shot DNA / subject + placement / visible detail / world / light / camera + finish) and the RESOLUTION-AWARE DETAIL RULE — describe only what this camera at this distance, motion level, and light can physically resolve. X/Y planning stays internal; positions become positional prose. Silent structure, prose surface.

**Step 3 — Pre-prompt check** (references first, per Banana Pro's universal rule). References do the geometry and identity work: character sheet attached → "carrying identically from the attached character reference," world plate attached → the reference IS the geometry. Re-describing what a reference shows is a double-weight prompt — cut it.

**Step 4 — Write the five-paragraph cinema prose** (locked structure): opening shot sentence → character block → world/environment block → subject anchor block → camera spec + finish. Confident DP prose, no labeled blocks, no coordinates, no CRITICAL/MUST rules, negations only in the mandatory closing realism clause ("Real photographic frame... no CGI, no plastic, no AI" — the one sanctioned end-position suppression; never "fix" it into positive phrasing or scatter it upward). The M-mode register is described as the actual look in plain language in paragraph 5. Voice-check against the CANONICAL MODE 3 PROMPT reference example.

If this plate seeds identity (rare — plates carry world, canonical refs carry identity), it stays flat-graded; a normal scene plate carries the scene's real light because it IS the final render register.

User generates and approves the plate → it becomes `@<scene>_plate`.

### Part B — Seedance shot prompt (worldbuilder)

**Step 5 — Pre-prompt confirmation, worldbuilder format:** tags FIRST, runtime LAST. **Runtime is asked, never assumed** — complexity guidance: 4-8s one action, 8-12s action + reveal, 12-15s two-three beats with hard cuts, more than that splits into separate prompts. Canonical-over-plate is a hard lock: every named subject gets its canonical `@tag` even when visible in the plate.

**Step 6 — Write the block-structured prompt** in the locked block order (TWO-PART DELIVERY FORMAT):

`Scene & Mood → Frame Map → Subject Lock (one per @tag) → Cross-Frame Rules → Movement → Last Frame → World Plate → Sound Bed → Capture Realism → Camera Capture`

Per block, the discipline that carries the shot:
- **Frame Map** — every subject pinned to thirds/depth/occupancy; x/y% only when the composition is asymmetric enough to earn it
- **Subject Lock** — identity from the canonical @tag; wardrobe trusted to the reference, only state-changes written (damp, torn, dirt); bible Movement/Stillness pasted verbatim; lock-down line closes each block
- **Movement** — four layers named in order (character / micro / environmental / camera), **write the visible**: km/h not "fast," % haze + meter visibility, scale by stacked humans, emotion in muscle ("knuckles blanch"). Multi-beat shots get **timestamped beats** per the CUTS & TIMING PRECISION SCALE — timecoded format, HARD CUT written explicitly, one speed per beat with a cut at every speed change, and the close-the-door line ("the camera does not add any additional cuts"). Absence stated per layer — "nothing else moves" is a directive; silence is not
- **Last Frame** — exact closing composition + the on-screen text suppression line
- **Sound Bed** — diegetic only; Speech descriptors from the bible if dialogue lands here
- **Capture Realism** — the locked anti-plastic block, scene-tuned (drop the IF WET sentence when dry, drop the skin sentence when no humans), never omitted otherwise
- **Camera Capture** — the mode's locked line, bottom position (the FOV lock holds there): **FOV in degrees from the ladder** — `47° (50mm)`, never mm alone, never an off-ladder degree — plus stock/grade/24fps 180° shutter/runtime. Title runtime = Camera Capture runtime
- Style distributed to home blocks — a style prefix scatters attention; nothing style-related opens the prompt

**Named looks and edge protocols** — reach for these by name when the shot calls for one (worldbuilder — OPTICAL TECHNIQUES, SPECIAL PROTOCOLS):
- **Voyeur / long-lens observation** — all three ingredients simultaneously: out-of-focus foreground obstruction covering 20-30% of frame, suspended atmosphere in % between camera and subject, 8° or 12° lens far from subject; vantage anchored, never zoomed
- **Broadcast press-box** — 8° (300mm) with the small 1-2cm hunting tremor
- **Foreground-loaded wide** — 84° (24mm) inches from a hero object; **wide portrait** — 63°-84° on a centered face, room stays legible
- **Extreme-FOV multishot** (8° / 107° across beats) — all four locks, no substitutes: anchor reference every beat, opening FOV declaration, closing FOV declaration, every hue tied to a surface + light source + purpose. Drop one and it drifts on beat three
- **Pressure fracture** — breaks without an impact point: edge stress, fracture moving edge-inward, asymmetric crack timing

**Step 7 — Silent QA:** run the worldbuilder's PRE-DELIVERY PASS checklist and repair pass before delivery. Word budget 280-400 single-shot, up to 600 multi — a lean prompt with strong refs beats a long one.

**Step 8 — Surface adaptation:** Higgsfield MCP → deliver as-is, tags match uploaded reference names. Fal wrapper → replace every `@tag` with its full prose descriptor from the Subject Lock spec, everything else unchanged; seedance-1080p stays off the table.

## Content Type Adaptations

| Shot type | Mode default | What changes |
|---|---|---|
| Character narrative beat | M1 | Bible payloads mandatory in Subject Lock/Sound Bed |
| Product hero / studio | M2 | Product is the Subject Lock; controlled specular intentional — Capture Realism gloss rules relax per its M2 tuning note |
| Client ad beat | M1/M2 | Runtime fits placement (6s/15s); Last Frame composed for end-card space (text still suppressed — cards land in post) |
| Music-video performance | M4 | Stage color cast in Camera Capture; crowd diegetic in Sound Bed; hard cuts between pit/orbital angles |
| Action / chase | M3 | Speeds in km/h everywhere; impact slow-mo via the 96fps append; hard cut at every speed change |
| Atmosphere / world plate in motion | M5 | No humans — skin sentence dropped from Capture Realism; hex palette in the grade |

## Output Requirements

- Part A: pre-prompt check → one fenced code block of five-paragraph cinema prose (no labels, no coordinates, closing realism clause present)
- Part B: bolded title line with runtime (`**Seedance prompt — 12s**`) → one fenced code block in the locked block order, every pre-prompt tag appearing inline
- No character names, ages, brands, or platform names in either prompt; no aspect ratios in the body; English only in code blocks
- Take note for the shot plan: mode, duration, take budget, credit estimate

Execution prompt: references/prompts-v2/scene-plate.md — honor its Output Contract.
Execution prompt: references/prompts-v2/seedance-shot.md — honor its Output Contract.

## Quality Gate

- [ ] Mode matched across plate and video — one cinema mode dominant, never blended
- [ ] References carry identity, prompt carries framing; zero re-description of what an attached reference shows (rubric: reference discipline ≥7)
- [ ] Write-the-visible: every word produces a visible pixel — no mood words, no "8k/masterpiece/cinematic" keyword slop (anti-pattern)
- [ ] FOV in degrees from the ladder; Camera Capture single and bottom-positioned; title runtime = Camera Capture runtime; runtime was ASKED
- [ ] Multi-beat: timestamps at named marks, HARD CUT at every speed change, additional-cuts door closed
- [ ] Positive phrasing throughout; negations only in the sanctioned end-position blocks (Last Frame suppression line, Capture Realism speculars, Sound Bed no-music)
- [ ] Capture Realism present and scene-tuned; contrast curve stated three ways; flattering ceiling intact
- [ ] Prompt economy: within word budget; if this is iteration ≥3 on a failing shot, reset — don't patch (rubric: prompt economy ≥7)

Identity drift at this layer is an asset problem — kick to `/jcin-character-lock` or `/jcin-prompt-doctor`, never re-describe the face here.
