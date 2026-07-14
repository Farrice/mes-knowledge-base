---
description: End-to-end mission conductor for the Joey pipeline — intake via the Existence Question, then CANON → STILLS → MOTION with checkpoints, a costed shot plan before any generation, and an execution-surface fork (Higgsfield MCP @tags vs Fal prose)
---

# `/jcin-pipeline` — Persistent-World Production Conductor

Runs a full mission through the strict pipeline: **CANON → STILLS → MOTION**. This workflow does not write prompts itself — it sequences the layer workflows, holds the checkpoints, and refuses layer-skipping. Kick to the right layer, always.

## Pre-Flight Gate

Answer before anything runs (genius.md — Signature Moves: the Existence Question, Cost Before Generate):

- [ ] **The Existence Question, per asset class.** For this mission: does a bible exist? Do the characters exist (canonical face + sheet)? Do the products exist (hero lock + turnaround)? Do the environment plates exist? Anything that exists gets locked and reused; anything that doesn't gets routed to a build step. Never assume — ask.
- [ ] **Mission shape known:** deliverable (single shot / 15s story / ad set / music video), runtime targets, and how many distinct subjects appear.
- [ ] **Surface known:** Higgsfield MCP or Fal wrappers (fork below). If unknown, ask — the prompt grammar differs.
- [ ] **Budget posture known:** roughly ~117 credits per 13s 1080p Seedance generation, 200-300 credits per studio piece, 5-6k per music video. If the mission is music-video scale, say the number out loud before starting.

## Skill Acquisition

Load in this order, only the layers this mission touches:

1. `skills/joey-cinema-os/genius.md` — judgment layer (already hot if routed here)
2. `skills/story-bible-builder/SKILL.md` — if CANON work is needed
3. `skills/banana-pro-director/SKILL.md` — if any STILLS work is needed
4. `skills/cinema-worldbuilder-pro/SKILL.md` — if any MOTION work is needed

The three production skills carry LOCKED verbatim grammar (flat-grade close, cinema stack, Capture Realism, FOV ladder). Never paraphrase their blocks — the layer workflows point at them by section name.

## Execution

### Step 1 — Intake (the Existence Question, expanded)

One compact block of questions:
- What are we making, for whom, at what runtime(s)?
- Which subjects recur (characters, products, vehicles, mascots)?
- Per subject: exists (reference in hand) or needs developing?
- Bible: exists / partial / none? Multi-scene world with no bible → recommend `/jcin-world-canon` first, or proceed with drift **named explicitly** (Farrice's call, on record).
- Which environment plates exist vs need Mode 3 builds?
- Surface: Higgsfield MCP or Fal?

Mirror back an **asset inventory** — EXISTS / NEEDS BUILD per item — and get a nod before proceeding.

### Step 2 — CANON checkpoint

If a bible is needed: run `/jcin-world-canon`. If a bible exists: load it and confirm which characters' Speech/Movement/Stillness descriptors and which aesthetic-era block this mission draws from.

**Checkpoint:** bible (or explicit no-bible decision) confirmed. The bible refuses cinematography — canon only.

### Step 3 — STILLS checkpoint

Per subject flagged NEEDS BUILD:
- Characters → `/jcin-character-lock` (strict Mode 0→1→2A)
- Products/garments/vehicles → `/jcin-product-lock` (Tier 2)
- Scene plates → `/jcin-scene-shot` Part A (Mode 3), mode-matched to the eventual video

**Checkpoint per asset:** user has generated and approved the still before it becomes a canonical reference. Plates that seed video stay flat (18% gray, zero lighting information — genius.md pattern 2). Unbuilt character in a video ask → kick back here. No exceptions.

### Step 4 — Costed shot plan (BEFORE any motion generation)

Build the plan as a table — beats, per-shot mode (M1-M5), duration, take budget, credit estimate:

| Shot | Beat | Mode | Duration | Takes budgeted | Est. credits |
|---|---|---|---|---|---|

Rules: duration declared per shot, never assumed. Honest take budgets — 2-3 for locked-asset shots, up to ~50 generations for the hardest garment/product composite (budgeted knowingly, not discovered). Total the credits. Present to Farrice for approval. For deeper planning use `/jcin-shot-plan` (Tier 2).

**Checkpoint:** plan approved. Generating before the plan is costed is an anti-pattern (genius.md).

### Step 5 — MOTION

Per approved shot, run `/jcin-scene-shot` Part B: block-structured Seedance prompt consuming canonical refs + bible payloads. One main idea per shot; complex sequences split into separate prompts (worldbuilder rule 19).

### Step 6 — Execution surface fork

- **Higgsfield MCP (native surface):** `@tag` element grammar works. Upload refs via `media_upload`/`show_reference_elements`, name tags exactly as the prompt uses them, paste the code block. Character slots via `show_characters`.
- **Fal wrappers** (`fal_video_seedance.py` etc.): **no @tags** — strip every `@tag` to its prose descriptor ("the woman from the attached character reference" → full visual descriptor line from the Subject Lock). **seedance-1080p is HARD-BLOCKED** by `fal_budget_guard.py`; plan around it, never around the guard.

**Cost-gate compliance:** all three production skills are prompt-only — the skill's job ends at the code block. Actual generation calls fire the existing gates (`cost_gate_hook.py`, `higgsfield_budget_guard.py`, `fal_budget_guard.py`). When a gate denies, surface it to Farrice — never retry around it.

### Step 7 — Iterate honestly

Per shot: past ~3 failed iterations, run the Reset Ritual (cut it, let it breathe, re-add minimum) — never patch a bloated prompt. Drift or bloat mid-mission → `/jcin-prompt-doctor` (Tier 2). The honest win is 8-10 takes → 2-3, never one-shot magic.

### Step 8 — Session continuity

Long missions span sessions. Before closing: write the mission state note (Step 4 of Output Requirements below) and pin the session (`/pin-session`) so `/resume` surfaces it by name. Tag names, approved canonical refs, bible path, and remaining shot-plan rows are the resume payload — a next session that re-asks the Existence Question on assets this session already locked has failed the handoff.

## Content Type Adaptations

| Mission type | CANON | STILLS | MOTION emphasis |
|---|---|---|---|
| Character world / film | Full story bible | Face lock → sheet → scene plates | M1/M3 narrative shots, bible payloads in Subject Lock/Sound Bed |
| Product (MyBPM, client goods) | Brand canon (palette + colors-to-avoid + "never" clauses) | Hero lock → turnaround → in-context plates via `/jcin-product-lock` | Product = the locked subject; M2 studio or M1 in-context |
| Client brand world | Brand bible in `_active/<client>/bible/` | Locked avatars + locked product | Ad beats; `/jcin-ad-world` for the full system |
| Music video | Full bible incl. musical voice, era palettes | Full character roster + wardrobe library | M4 performance + M1/M3 intercut; shot plan is mandatory at this scale |
| Ad / 15s story | Bible optional — premise + ICP context minimum | Only the assets in frame | 3-shot grab → payoff → unresolved questions (`/jcin-story-15s`) |

## Output Requirements

- Asset inventory (EXISTS / NEEDS BUILD) — delivered at intake
- Costed shot plan table with total credit estimate — approved before generation
- Per-shot prompts in fenced code blocks, each via its layer workflow's own delivery format
- A mission state note: which canonical refs exist, their tag names, where the bible lives — so the next session resumes without rebuilding

Execution prompt: references/prompts-v2/shot-plan.md — honor its Output Contract.

## Quality Gate

Check against genius.md rubric + anti-patterns before calling the mission done:

- [ ] No layer skipped or combined — bible did no cinematography, stills baked no lighting, motion re-described nothing a reference carries
- [ ] Existence Question asked at intake; no asset rebuilt that already existed
- [ ] Shot plan costed and approved BEFORE first paid generation; durations declared, never assumed
- [ ] Surface fork applied — @tags only on Higgsfield MCP; Fal prompts fully de-tagged; seedance-1080p never attempted on Fal
- [ ] Reference discipline (rubric): refs carry identity, prompts carry framing; plates flat; canonical-over-plate for every named subject
- [ ] Credit economy (rubric ≥7): take budgets honest, hardest asset budgeted knowingly
- [ ] Any prompt that failed 3+ iterations was reset, not patched
- [ ] No names, brands, ages, or platform names in any prompt output

If any box fails, kick back to the owning layer — never patch downstream.
