---
description: "/jcin-prompt-doctor — diagnose and repair a failing image/video prompt: bell-curve bloat, abstraction leak, anchor decay, position faults, lock faults, reference faults — output a rewritten prompt plus the upstream lock fix so the failure never recurs"
---

# Prompt Doctor (Joey Cinema OS)

Joey's repair move is never "add another clause." Past ~3 failed iterations the instruction is the opposite: "cut it, reset it, let the prompt breathe," then re-add only what's necessary — because prompt length is a bell curve, and a patched prompt is usually past the peak. This workflow takes a failing prompt and a symptom, diagnoses against the known failure patterns, rewrites, and — the part that makes it worth running — names the upstream lock to fix so the same drift never comes back. Drift is never fully solved; hit rate scales with prep.

## Pre-Flight Gate

> **🔒 Gate — intake before surgery.** Do not touch the prompt until you hold all four:
> 1. The failing prompt, verbatim
> 2. The symptom, named: **drift** (identity/wardrobe/lens changes across takes) / **plastic** (AI-render skin, gloss, flatness) / **ignored instruction** (a named element never renders) / **chaos** (unplanned cuts, swapped subjects, broken timing)
> 3. Iteration count — how many takes failed, and what was patched between them
> 4. The reference set actually attached (not the intended one — the actual one)
> Missing any → ask. A diagnosis without the reference list is a guess.

## Skill Acquisition

1. `skills/joey-cinema-os/genius.md` — patterns 7–14 (prompt physics), 1–4 (reference physics), 15–16 (canon discipline); Signature Move: Reset Ritual; Anti-Patterns (the anti-exemplar is the full disease in one prompt)
2. Stills prompt → `skills/banana-pro-director/SKILL.md` § **UNIVERSAL PROMPT RULES**, § **18% GRAY SEAMLESS + FLAT GRADE** ("the three things that must appear in every flat close"), § **READING REFERENCE IMAGES**, the lean-prompt rules in the reference-reading passage above § THE CINEMA STACK
3. Video prompt → `skills/cinema-worldbuilder-pro/SKILL.md` § **WRITE THE VISIBLE**, § **POSITIVE PHRASING**, § **DISTRIBUTED STYLE**, § **FOV DEGREE TABLE**, § **CUTS & TIMING PRECISION SCALE**, § **PRE-DELIVERY PASS** (its built-in repair pass is the video-side checklist — run it, don't reinvent it)

## Execution

### Step 1 — Triage by symptom
Symptoms point at pattern families; confirm against the prompt, don't assume.

| Symptom | Look first at |
|---|---|
| Drift | Lock faults, reference faults, anchor decay |
| Plastic | Reference faults (baked lighting), missing/mangled realism close, style-keyword slop |
| Ignored instruction | Bell-curve bloat, position faults, abstraction leak, negative phrasing |
| Chaos | Anchor decay (untimed beats), missing null statements, overloaded action |

### Step 2 — Diagnose against the pattern set
Walk all six families regardless of triage — failing prompts usually carry two or three at once.

**1. Bell-curve bloat.** 10+ iterations of accreted patches; sentences added to fix sentences; the prompt is longer than its first version and hits less. Confirm: word count vs the density targets (video: 280–400 single-shot, 600 multi — § density rule; stills: a 2,500-char prompt with strong refs beats 5,000). *Repair = the Reset Ritual, Step 3.*

**2. Abstraction leak.** Mood words that produce no pixel: "fast," "dangerous," "stressed," "huge," "cinematic," "moody." Confirm with the read-back test from § WRITE THE VISIBLE: is every named element actually going to render on screen? *Repair = write-the-visible rewrite:* speeds in km/h, atmosphere in % density + meter visibility, scale in stacked humans, emotion in muscle (jaw sets, knuckles blanch), environmental contact rendered physically.

**3. Anchor decay.** Continuous suggestions where discrete anchors belong: lens in mm alone (mm reads as suggestion; degrees read as instruction — re-anchor to the § FOV DEGREE TABLE ladder, never an off-ladder value), untimed beats where timing is load-bearing (timestamp them, HARD CUT at every speed change), contrast stated once (state it three ways per Capture Realism: tonal curve + specular removal + grade), bare color lists (tie every hue to a surface, a light source, and a purpose).

**4. Position faults.** Style prefix at the top of the prompt (scatters attention — redistribute per § DISTRIBUTED STYLE, each aspect to its home block); camera/FOV block anywhere but the bottom (bottom position holds the lock; at the top it fights identity data); composition buried under description in a stills prompt (Banana Pro reads the front heaviest — front-load composition, pose, light).

**5. Lock faults.** Locks that include but never exclude — no "never" clauses naming the wrong-answer drift ("warm fair skin — never pale porcelain, never tan"); character names, brand names, ages, or platform names in the prompt body (names drift, all four are banned); prose that re-describes what an attached reference already shows (double-weight — cut unless load-bearing for composition); missing lock-down line in a video Subject Lock; missing null statements ("nothing else moves" per motion layer; "the camera does not add any additional cuts").

**6. Reference faults.** The prompt may be innocent — check the assets: baked lighting or shadow in an identity plate (inherited and amplified downstream — the plate must carry zero lighting information, three flat-close clauses per § 18% GRAY SEAMLESS + FLAT GRADE); more than one face on an identity reference, or a face too small to control drift; white seamless on an asset that seeds video (high-contrast edges breed halo and edge breathing — should be 18% gray); a named subject riding only in the environment plate with no canonical reference (canonical-over-plate is a hard lock); missing reference the prompt assumes ("References First" — a missing ref reads as an ignored instruction).

One sanctioned-negation caution: do NOT "fix" the end-position suppression blocks (on-screen-text line, specular kill, no-music line, headless suppression stack) into positive phrasing, and do not scatter them upward. They are sanctioned, end-positioned, and load-bearing.

### Step 3 — Repair
- **Iteration ≥3 or bloat confirmed → Reset Ritual.** Strip to the minimum true skeleton (subject handles + composition + the mode's locked close), breathe, re-add only what earns a visible pixel. The post-reset prompt must be shorter than the bloated one.
- Otherwise → surgical: apply the specific pattern repairs above, preserving every locked block untouched (flat-grade close, Capture Realism, Mode 5 lean prompt, cinema-prose close — these get restored verbatim from their source sections, never hand-edited).
- Re-run the source skill's own silent QA before delivery: stills → § INVENTORY EXTRACTION CHECKLIST; video → § PRE-DELIVERY PASS.

### Step 4 — Name the upstream lock fix
Every diagnosis ends by moving the failure out of the prompt layer: which permanent artifact, fixed once, makes this failure structurally impossible next time?

| Root found | Upstream fix |
|---|---|
| Identity drift from weak/absent canonical | `/jcin-character-lock` or `/jcin-product-lock` — rebuild the face/hero lock, face large, one face |
| Wardrobe drift | Outfit base + sheet via `/jcin-outfit-engine`; add the missing "never" clause to the bible's visual lock |
| Voice/persona wobble | `/jcin-voice-lock` — quoted descriptors into the bible |
| World/era inconsistency | `/jcin-world-canon` — aesthetic era block + production rules |
| Lighting baked into plates | Regenerate the plate on the flat grade; audit the asset library for other lit plates |
| Cost bleed from re-rolling | `/jcin-shot-plan` before the next batch |

## Content Type Adaptations

| Prompt type | Adaptation |
|---|---|
| Banana Pro / stills | Front-load check + flat-close integrity are the top diagnostics; cinema stack on a character plate is itself a fault (flat grade only, Modes 0/1/2/4/5) |
| Seedance / video | Block order + FOV degrees + timestamped beats + null statements dominate; word-count band is hard (280–400/600) |
| Video-to-video / Omni edit | Register flip: edit prompts go SIMPLE and imperative ("keep me exactly the same, change X"), ≤10s footage — a dense generation-register prompt on an edit op is the whole diagnosis |
| Fal-wrapper prompt | @tags don't exist there — tag grammar in a Fal prompt is an ignored-instruction generator; strip to prose descriptors; seedance-1080p on Fal is HARD-BLOCKED, route to Higgsfield |
| Multi-shot sequence | Check the extreme-FOV four-lock stack (§ SPECIAL PROTOCOLS) and per-beat lens declarations; drift on beat three = a missing lock from that stack |

## Output Requirements

Deliver three parts, in order:
1. **Diagnosis** — pattern(s) found, each with the offending line quoted from the failing prompt
2. **Rewritten prompt** — single fenced code block, locked blocks restored verbatim from source sections, density inside band
3. **Upstream fix** — one line: which lock, which workflow builds it, and what "never recurs" means for this failure

Execution prompt: references/prompts-v2/prompt-repair.md — honor its Output Contract.

## Quality Gate

> **🛡️ Anchor before shipping** — `genius.md § Quality Rubric` (Prompt economy, Write-the-visible, Reference discipline) + § Anti-Patterns.
- Every diagnosis cites a quoted line — no pattern claimed without evidence in the prompt or reference set
- Post-reset prompt is shorter than the failing one AND structurally different, not the same prompt trimmed
- No locked block was paraphrased during repair; sanctioned negations stayed end-positioned and intact
- Names/brands/ages/platform names: zero in the rewrite
- The upstream fix targets an artifact, not advice ("be more careful" is not a lock)
- If the prompt was actually fine and the references were the disease, the output says so plainly — rewriting an innocent prompt is a miss

## Worked Micro-Diagnosis (the anti-exemplar, dissected)

The extraction report's anti-exemplar — "8k, masterpiece, hyperrealistic, cinematic lighting, trending on artstation" + a character name + a brand + "beautiful girl, age 22" + style header at top + 5,000 characters re-describing the attached reference — carries five families at once. The teardown reads:

```
DIAGNOSIS
  Bell-curve bloat:   5,000 chars against strong refs — target ~2,500 with refs carrying identity
  Abstraction leak:   "masterpiece," "cinematic," "beautiful" — zero visible pixels among them
  Position fault:     style header at top — scatters attention; distribute per home blocks
  Lock fault:         name + brand + age all present (three bans); reference fully re-described
  Reference fault:    unknown until the attached set is listed — demand it before rewriting

REPAIR ROUTE:  Reset Ritual (bloat confirmed) → lean rewrite on the mode's locked close
UPSTREAM FIX:  no canonical existed (identity was living in the prompt) → /jcin-character-lock
```

That last line is the signature of the whole method: the prompt was carrying identity because no asset was — and no rewrite fixes an asset gap.

## Common Pitfalls
- **Patching instead of resetting.** The instinct at take 6 is one more clause; the bell curve says the prompt is already past the peak and every patch pushes it further over. Recovery: iteration ≥3 triggers the Reset Ritual unconditionally — cut, breathe, re-add minimum.
- **"Fixing" the sanctioned negations.** A well-meaning positive-phrasing pass rewrites the on-screen-text suppression, the specular kill, or the headless suppression stack — and the failure they suppressed comes back. Recovery: sanctioned end-position negation blocks are load-bearing; restore them verbatim and leave them at the end.
- **Diagnosing the prompt when the reference is sick.** Hours of prompt surgery can't fix a lit identity plate, a two-face reference, or a missing canonical. Recovery: Step 2 family 6 runs on every case — check the assets before touching a word.
- **Rewriting into a longer prompt.** A repair that adds net words usually re-imported the bloat under new phrasing. Recovery: the post-reset prompt must be shorter than the failing one; if it isn't, the reset didn't happen.
- **Fixing the symptom, skipping Step 4.** A rewritten prompt that works today drifts again next week if the lock never moved upstream. Recovery: no delivery without the upstream fix line — the named artifact and the workflow that builds it.
- **Off-ladder anchor repairs.** Re-anchoring lens language to 23° or 55° trades one decaying suggestion for another. Recovery: FOV values come off the § FOV DEGREE TABLE ladder only.
