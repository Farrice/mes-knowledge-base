---
description: Sweep the style space against a fixed probe, pick with taste, then audition the winner across the whole scene inventory before any volume spend — ending in a verified card
---

# 02 — Mine and Audition

**Deliverable:** one decided style, **proven to replicate across the entire scene inventory**,
written to `skills/generate/styles/<slug>/card.md` with `verified` set.

**Run this when:** you have a scene inventory from `01` and no banked style that fits.

**Why the audition step exists.** It is the step everyone skips and the one that decides whether
you own a style or a lucky frame. Carter is explicit: *"we want to run this against all of our
other prompts to see if we can replicate this across a range of different scenes before we
actually go out and create 100 to 200 different variants."* A style that only works on the
image that discovered it is a coincidence with good PR.

---

## Pre-flight

- **Load the craft.** `grace-liu` first if the ask is at all foggy (which layer is failing?),
  then `nick-st-pierre` for frame construction and `rory-flynn` for sweep discipline. Do not
  restate their rules here — load them.
- **Check the vault before sweeping.** `python3 execution/style_vault.py list --brand <slug>`.
  An existing `broad` or `micro` entry may already cover this; a sweep that duplicates a banked
  look is spend with no asset at the end.
- **Read** `references/midjourney-port.md` if you are about to reach for a Midjourney parameter.
  Two of them do not port, and faking them is worse than not having them.

---

## Step 1 — Freeze the constants

Write these at the top of the sweep log. **If any of them changes, the sweep restarts.**

- The fixed probe subject (from `01` — never edited mid-sweep)
- Aspect ratio
- Model and images-per-run
- Seed policy

## Step 2 — Mine

```bash
python3 execution/style_vault.py probe --n 24 --seed 0 --subject "<fixed probe subject>"
```

This is the port of Carter's `--sref random` roulette. Each candidate is a **decomposable**
descriptor — process × era × palette logic × light × surface × composition — so a winner can be
explained rather than merely recorded.

Generate the full set on `nano-banana-2` (≈$0.60 for 24 × 4). Then **three rules**:

1. **Generate everything before judging anything.** You are reading a response curve, not hunting
   a keeper. Judging as you go selects for whatever you saw first.
2. **Taste is the selection function.** This is the anti-slop mechanism and the only step that
   cannot be automated — Carter's actual thesis, and it agrees with Grace Liu's Human layer.
3. **Delete hard.** *"Just delete them, move on."* Everything not in the emerging world goes now,
   while the comparison is live.

**If the sweep feels narrow, that is a lexicon bug, not a stack limit.** Extend `LEXICON` in
`execution/style_vault.py` and re-run with a new seed.

## Step 3 — Characterize (Flynn's null run)

Before the winner earns a card, run it **twice**:

| Run | Prompt | What it tells you |
|---|---|---|
| **Null** | nothing meaningful — a period, a slash | the asset's own prior, uncontaminated by your language |
| **Probe** | the fixed probe subject | how much of the asset survives contact with direction |

**The delta between them is the asset's strength**, and it sets the tier: `tight` (overrides
almost everything) · `broad` (range coexists) · `micro` (one isolated effect — the most valuable
kind, because it composes).

Record, in plain language: **palette · light behaviour · texture/grain · subject bias · era ·
what it refuses to do.**

## Step 4 — AUDITION (the gate)

Run the candidate style against **every scene in the inventory** — pain and desire, not a
favourite subset.

Score each: **holds · drifts · breaks.**

| Result | Verdict |
|---|---|
| Holds on all scenes | Bank it. |
| Holds on pain, breaks on desire (or vice versa) | **Two entries, not one.** Bank the strong half keyed narrowly; sweep again for the other. This is common and is not a failure. |
| Breaks on the majority | Discard. Do not "fix it with better prompts" — that is the adjective-hunting the whole method replaces. |

Carter's own named failure mode, worth watching for: *"the prompt is clashing with the
reference"* — outputs snapping to hyperrealism and away from the found style. When you see it,
the diagnosis is a **channel** conflict (prompt restating what the reference should carry), not
a wording problem. Reach for the grip ladder in `references/midjourney-port.md` §3.

## Step 5 — Bank it

```bash
python3 execution/style_vault.py init <slug> --tier <tight|broad|micro> --family <...> \
    --brands <brand> --icps <icp> --platforms <p1> <p2> \
    --provenance "swept <date>, seed <n>, probe: <subject>"
```

Fill `card.md` from Steps 3–4. Add the winning reference image(s) as `reference-1.png`. Write
`prompt.md` if absent (para 1 = description, rest = prompt — the assets board depends on this
shape).

**Then set `verified: YYYY-MM-DD`.** Only after the audition actually ran. The card stays GAP
until you do, by design — `validate` treats a characterized-but-unrun card as unproven, because
characterization can be written from a description and that is inference, not evidence.

```bash
python3 execution/style_vault.py validate
python3 execution/style_vault.py index
```

---

## Output requirements

- Sweep log: frozen constants, candidate set, what was deleted and why
- Null-run and probe-run reads, and the tier the delta implies
- Audition table: every scene × holds/drifts/breaks
- A `card.md` with `verified` set, or an explicit "discarded, here's why"

## Quality gate

1. Was one variable responsible for each difference, or did the probe move mid-sweep?
2. Was the whole set generated before any of it was judged?
3. Did the audition cover **every** scene, including the ones you expected to fail?
4. Is the tier claim supported by the null/probe delta, or asserted from how the prompt reads?
5. Run St. Pierre's closer on the winner: **would this have looked the same without me?**

**Next:** `03-bank-and-batch.md`.
