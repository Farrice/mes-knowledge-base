# The Midjourney Port — Carter's moves on a no-Midjourney stack

Source: Luke Carter, *"Stop Posting AI Slop (Build Your Own Style Instead)"*, YouTube
`sAMArYBpDmI`, 2026-08-08 (18:27). Farrice's decision 2026-08-09: **no Midjourney — port to the
existing stack.**

This file exists because every operation Carter demonstrates is Midjourney-native, and
Midjourney has **no API** — deliberately. His own framing: the founder *"wants Midjourney to be
a crafting tool."* That makes his loop a human-in-the-browser craft session by design. Ported
here, it becomes scriptable, which is a real gain and a real loss. Both are stated below.

---

## The live stack (verified 2026-08-09 against `skills/generate/models/*.json`)

| Model | Status | Reference input | Cost | Role here |
|---|---|---|---|---|
| `nano-banana-2` | **live** | `--reference <img>`, `--edit <img>` | **$0.0062/image** | The probe workhorse. Volume exploration lives here. |
| `recraft-v3` | **live** | none (no ref param) | $0.04 / $0.08 vector | Flat, vector, text-heavy. `style` param is the dial. |
| `gpt-image-2` | live (via `fantastic-posters` `gen.sh`) | wrapper flags | see recipe | Styled/poster default per craft-map. |
| `flux-2` | ⚠️ **DEFERRED STUB — will not run.** Endpoint + price UNCONFIRMED. | — | — | Craft-map lists it as an escalation lane; it is not one yet. |

**Cost consequence, stated plainly:** a 24-candidate probe sweep at 4 images each is 96 images
≈ **$0.60** on `nano-banana-2`. A 140-image bank ≈ **$0.87**. Midjourney's equivalent is a
~$30/month subscription. Exploration is roughly free on this stack; what you give up is
described under "Honest losses."

---

## Move-by-move

### 1. `--sref random --repeat 4` → `style_vault.py probe`

**What it stands for:** roll the style space wide, let *taste* select. Carter is explicit that
this is the anti-slop mechanism — *"you're going to be using your own taste and your judgment
in this to find a style we like."*

**Why it can't port directly:** `--sref random` samples Midjourney's private latent index
(Carter says "over a billion combinations"). There is no equivalent index on fal, and no way
to address one.

**The port:** `python3 execution/style_vault.py probe --n 24 --subject "<fixed probe subject>"`
draws combinatorially from a **decomposable aesthetic lexicon** — process × era × palette
logic × light × surface × composition. Every term names a medium, a physical light condition,
a surface or a compositional rule. No quality assertions ("cinematic", "8k"), no artist names —
both bans are St. Pierre's, both because undecomposable terms cannot be swept, explained, or
banked.

**This is strictly better for banking, and that is not a consolation prize.** When a Midjourney
sref wins you have a number; you know *that* it worked, never *why*. When a lexicon draw wins
you can read the decisions straight off the descriptor and write them onto a card. Carter's
whole workflow ends in a style bank — and a bank of opaque numbers is a bank you cannot reason
about, extend, or port to the next model.

### 2. `--sref <code>` (the locked style code) → **the card is the code**

**What it stands for:** a portable pointer at a look.

**Why it can't port:** an sref is an index into Midjourney's weights. It does not exist
anywhere else, and it does not even survive Midjourney's own version changes.

**The port:** on this stack a style is **a reference image + a characterized prompt fragment**
— which is exactly what `skills/generate/styles/<slug>/` already stores. St. Pierre reached
this independently and stated it as doctrine: *"the direction session's real output is the
reference set, not the prompt string. Prompts are disposable; the bank compounds."*

The card is more durable than an sref, not less: it survives model migration, it is readable by
a human, and it can be handed to a client.

### 3. `--sw 400` (style weight, 0–1000) → **no numeric dial exists. Do not fake one.**

**What it stands for:** how hard the reference grips the output.

**The honest finding:** `nano-banana-2` takes `--reference` as a boolean-ish input with no
strength scalar. `recraft-v3` has no reference param at all. **There is no `--sw` on this
stack**, and inventing a number to put in a prompt would be theatre.

**The real port** is a prompt-authoring decision, not a parameter: *how much does the prompt
restate what the reference already carries?*

| Effect wanted | How you get it |
|---|---|
| High grip (≈ sw 700–1000) | Strip the prompt to `{medium} {subject} {environment}` and let the reference carry palette, light, texture. St. Pierre: *"I removed a lot of variables… the images fill in the rest."* |
| Medium grip (≈ sw 300–500) | Prompt states composition and subject detail; reference carries palette and finish |
| Low grip (≈ sw 100) | Prompt fully specifies the look; reference is a loose mood anchor only |

Worth knowing: St. Pierre **rejected** weighted prompting after ~50 trials — *"it feels totally
out of my control and random."* Losing the numeric dial moves you toward a control surface you
can reason about. That is the trade, and it is not a bad one.

### 4. `--stylize 1000` → prompt register, not a parameter

**What it stands for:** how loudly the engine is allowed to editorialise over your instruction.

**The port:** no equivalent. It maps onto *register* — literal physical description (low
stylize) versus aesthetic assertion (high stylize). Since aesthetic assertions are banned by
St. Pierre's rule 2 (*name the physical cause, never the quality*), the working answer on this
stack is: **always run literal, and get "loud" from the reference image instead.**

### 5. `{a, b, c}` curly-brace permutation → `style_vault.py permute`

**What it stands for:** one prompt → N variants, so a locked style becomes a bank fast. This is
Carter's volume mechanic; it is how he reaches 310 images from a handful of prompts.

**The port:** `python3 execution/style_vault.py permute "{Editorial photo, Gouache} of {a
founder, a strategist} at {dawn, dusk}"` → full cartesian expansion, with `--sample N --seed S`
for reproducible subsets.

**This one ports better than the original.** Midjourney's braces are opaque and capped; here it
is a function with a seed, so a batch is reproducible and can be diffed, scripted into the
generator, and budget-checked before it spends.

### 6. Bulk curate + download → the vault + assets board

**What it stands for:** the bank as a downstream *consumable* — Carter feeds his into a
carousel automation that builds posts in code.

**The port:** already built. `generate_media.py index` writes provenance sidecars and refreshes
`/assets-board`; `style_vault.py index` regenerates the keyed `VAULT.md`. Nothing new required.

---

## Honest losses

1. **Style-space diversity.** Midjourney's billion baked references genuinely reach corners a
   curated lexicon will not. The lexicon holds ~19 × 8 × 8 × 8 × 8 × 6 ≈ 466k combinations —
   large, but *authored*, so it inherits my blind spots. Mitigation: the lexicon is a plain
   Python dict in `execution/style_vault.py`; extend it whenever a sweep feels narrow. Treat a
   thin sweep as a lexicon bug, not a stack limitation.
2. **Midjourney's aesthetic prior is genuinely strong.** Its outputs look good on average
   because that is what it optimises for. `nano-banana-2` at $0.0062 is a draft model; it needs
   more direction to reach the same floor. The compensation is that direction is exactly what
   this pipeline produces.
3. **No `--sw` dial.** Covered above; the prompt-restatement ladder is the substitute, and it
   is coarser.

## Honest gains

1. **It automates.** Midjourney has no API by design. Every step here is scriptable, which is
   what makes a *vault* possible rather than one artist's session.
2. **Decomposability.** Winners can be explained, so cards compound instead of accumulating.
3. **Cost.** ~$0.60 per full sweep versus a monthly subscription.
4. **Reproducibility.** Seeded draws and seeded permutation mean a sweep can be re-run exactly.

---

## What Carter gets right that survives the port intact

- **Taste is the selection function, not the prompt.** *"Prompting in my opinion is completely
  dead."* Overstated, but the load-bearing half is true and matches Grace Liu's Human layer.
- **Audition before volume.** Run the candidate style across your *whole* scene inventory before
  committing to a batch. Carter does this; it is the step most people skip.
- **The bank is the deliverable.** Images are the experiment; the retrievable, named, keyed
  entry is the result. Same conclusion Rory Flynn reached from the opposite direction.
- **Delete aggressively.** *"Just delete them, move on."* A bank with weak entries is a folder.

## What does not survive contact

- **"Prompting is dead."** It is not; his own workflow is prompts end to end. What is dead is
  *adjective-hunting* as the primary control surface.
- **His output as a taste ceiling.** I pulled frames: a flat pastel-blue editorial illustration
  world. Genuinely coherent — a real brand world, not hyperreal slop — but fintech-blog
  competent, not world-class. The method buys **consistency**; the ceiling is set by the
  operator. Copy the mechanism, not the look.
