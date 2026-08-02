# Workflow 01 — The Aesthetic Sweep

**Deliverable:** a *Sweep Record* — one control prompt, one variable ladder, a generation grid
ready to run, and (after generation) a decided winner with the reason, banked as a style code.

**Use when:** the look is not decided yet. "I don't know what this should feel like," "try some
options," "which lighting?", "find the vibe," any brief where the honest answer is that nobody has
chosen the aesthetic yet.

**Do NOT use when:** the look is already decided and you need the frame built — use
`02-additive-prompt-build.md`. Or when you want wide random exploration rather than a decision —
that is a separate act (see Step 6).

---

## Step 1 — Name the decision, not the image

Write one sentence: **"By the end of this sweep I will have decided ___."** If you cannot fill the
blank with a single variable, the sweep is not scoped yet.

Bad: "explore some looks for the campaign."
Good: "By the end of this sweep I will have decided the emulsion/grade for the whole campaign."

## Step 2 — Write the control prompt and freeze it

The control is the fixed string that will appear in every generation with exactly one slot
swapped. It must be:

- **Simple.** *"It also helps to have simple prompts where you only change a single, specific
  variable."* (St. Pierre, 2023-02-08)
- **Representative.** Whatever you decide here gets inherited by the whole set, so the control
  subject should be a real subject from the job, not a generic stand-in.
- **Complete above the swept layer.** Every layer higher on the ladder is already decided and
  present.

Write it out and mark the swap slot explicitly with `[BRACKETS]`.

His canonical example (2023-02-04): `[street style] photo of [a woman], shot on [Film Type]` —
where only `[Film Type]` moves.

## Step 3 — Fix the random state

Set a seed, or use the same reference image, so a difference between two cells is caused by the
variable and not by the dice. If the tool has no seed, generate each cell as a batch and compare
batch-to-batch central tendency, not cherry-picked bests — and say so in the record.

## Step 4 — Build the variable ladder

Choose **4–8 values** for the one variable. Values must be:
- **Nameable** — a term you could put in a style bank
- **Genuinely distinct** — not three shades of the same choice
- **Real vocabulary where possible** — actual film stocks, actual lighting setups, actual design
  movements. Real-world terms carry real-world behaviour into the model.

**Banned as sweep values:** artist names, `8k` / `HDR` / `ultra-detailed` / `cinematic` and other
quality-assertions, and "vibey" adjectives. They are undecomposable and cannot be banked.

**Ladder position matters.** Sweep in the layer order — medium & subject → emulsion/grade → light →
shot & camera → wardrobe/colour/material → atmosphere → setting & time → mood. Sweeping a lower
layer before an upper one is decided means re-doing it.

## Step 5 — Add the contrast probe

Include **one deliberately colliding value** in every ladder — a value in tension with the fixed
control (a night stock against a daylight scene, an illustrative medium against a photographic
subject, a genre that does not belong). *"Lean into the contrast, see where it takes you."*
(2024-01-30)

The probe is not padding. It is the cell most likely to produce the thing you did not know you
wanted.

## Step 6 — Generate the whole grid before judging any of it

Generate every cell. Do not stop early on a keeper. You are reading a response curve, not hunting.

*If what you actually want is exploration rather than a decision* — cast wide, random style
references, big batches — do that as a **separate, labelled pass** and feed its survivors back in
as ladder values. Never let random exploration masquerade as a sweep.

## Step 7 — Judge in pairs, then decide

- Lay out **side-by-side pairs** for the finalists. He called the two-up his favourite view
  (2023-02-05).
- Judge against the **brief's felt standard**, not against each other's prettiness.
- Run the critique pass (SKILL.md) on the finalists — especially: did the framing arrive, is the
  light named and placed, what is in tension.
- **Decide.** A sweep that ends in "they're all nice" has failed. Name the winner and the reason
  in one sentence.

## Step 8 — Lock, bank, and climb

- **Lock** the winner into the control prompt.
- **Bank** it as a style-code entry (`03-style-code-bank.md`): name, what it does, exact fragment,
  conditions, anti-conditions, date.
- **Climb** to the next layer with the new control prompt, and repeat.

*Execution prompt: `references/prompts-v2/01-aesthetic-sweep-plan.md` — honor its Output Contract.*

---

## Quality gate

- [ ] The decision sentence names exactly one variable
- [ ] The control prompt is written out with the swap slot bracketed, and everything above it on
      the ladder is already decided
- [ ] Random state is fixed (seed / same reference), or its absence is explicitly noted
- [ ] 4–8 nameable, genuinely distinct values — no artist names, no quality-assertions, no vibe words
- [ ] At least one contrast probe in the ladder
- [ ] The verdict names a winner **and** the reason, in one sentence
- [ ] The winner is written into the style bank with a date, not left in a chat log

---

## Example output (abridged)

**Decision:** By the end of this sweep I will have decided the **emulsion/grade** for the
supplement-brand product set.

**Control prompt (frozen):**
`Editorial product photo of a matte-black supplement tin on a wet slate surface, side light from
camera-left, shot on [EMULSION] --ar 4:5`
Seed fixed. Layers above (medium, subject, light) already decided.

**Ladder (6 + probe):**
1. Kodak Portra 800 — warm, forgiving, open shadow
2. Fuji Provia 100F — vivid colour, fine grain, clinical
3. Cinestill 800T — tungsten-balanced, halated highlights
4. Ilford Pan F Plus 50 — B&W, fine grain, hard detail
5. Kodak Ektachrome E100 — slide, cool-neutral, crisp
6. Polaroid Originals Color — soft, vintage, low fidelity
7. **Contrast probe:** Fuji Neopan Acros 100 at high contrast against a wet, reflective surface —
   B&W physique against a colour-led product category

**Verdict:** Cinestill 800T. The halation on the wet slate is the only cell where the surface
reads as *cold and wet* rather than *dark and clean* — which is the felt standard the brief asked
for. Provia was sharper and read as pharmacy.

**Banked:** `WET-SLATE-800T` → tungsten-balanced night grade for product-on-wet-surface; needs a
hard side light and a reflective ground; not for warm/daylight lifestyle frames. (2026-08-02)

**Next layer:** shot & camera position, with `Cinestill 800T` now locked into the control.
