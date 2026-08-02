# Workflow — The Moodboard Sweep

**Deliverable:** a **Board Card** for every style asset swept, plus a **Stack Matrix** and a set of
**named production recipes**. Not images. The images are the experiment; the card is the result.

**Run this when:** you have built (or bought, or inherited) style assets — moodboards, style references,
profile codes, LoRAs, any reusable style handle — and you do not yet know, in words, what each one does,
what it does to *other* assets, or which combinations are worth keeping.

**Why it exists.** Flynn's own scaling failure, stated against himself: *"I've got 40 or 50 of these
things — how are you even going to keep track of what we're running here"* [MOOD @ 29:36, 2025], and
*"am I going to remember to run this combination, and when am I going to use it?"* [MOOD @ 23:33, 2025].
A sweep whose output is images is entertainment. A sweep whose output is **named, retrievable recipes** is
infrastructure. The name "moodboard sweep" is a label on his demonstrated operation — he never uses the
term; see `references/source-notes.md`.

**Tool-neutral by construction.** Nothing below names a model, a parameter or a menu item. Every step is
stated as an operation any generator with a reusable style handle supports. Era-bound implementations of
these operations are in `genius.md` Appendix A and must be verified against the live tool before use.

---

## Step 0 — Declare the constant

Pick **one probe prompt** and do not change it for the entire sweep. Everything you learn is a *difference*,
and a difference requires a fixed baseline. Change the probe mid-sweep and the whole run is void.

The probe should be neutral and typical of what you actually produce. Flynn's stated method:

> "I try to think of the things that I'm going to create most often, which could be maybe photorealism-based,
> so maybe I'll throw in something very simple like 'editorial photo,' 'editorial photography,' 'lifestyle
> photography,' and just kind of see where it takes me." — [MOOD @ 35:29, 2025]

Also fix: aspect ratio, any stylization dial, and the number of images per run. Write them at the top of
the sweep log. If any of them changes, the sweep restarts.

## Step 1 — The null run (characterize the asset alone)

Run each asset with **nothing meaningful in the prompt** — a period, a slash, a single neutral character.

> "Whether you're doing this yourself or you're using [someone else's] — type in an empty character like a
> period or a slash and just run it. And just dig into what that default is going to be. And then that
> might give you a better sense of what to expect." — [MOOD @ 35:02, 2025]

**Why this and not a real prompt:** with real words attached you cannot tell what came from the asset and
what came from your language. The two signals are confounded. A null prompt isolates the asset's own prior.
This is the step that separates a library from a folder of vibes, and it is the step everyone skips.

Record, per asset, in plain language: **palette · light behaviour · texture/grain · subject bias ·
era/register · what it refuses to do.**

## Step 2 — The probe run (asset against your actual work)

Same asset, now with the Step 0 probe. This tells you how much of the asset survives contact with
direction — the difference between Step 1 and Step 2 *is* the asset's strength.

Classify each asset into a tier [MOOD @ 01:35–02:38, 37:20, 2025]:

| Tier | Signature | Job |
|---|---|---|
| **Tight** | overrides the probe almost entirely; one exact aesthetic | reproduce a look |
| **Broad** | wide range, several aesthetics coexisting | a house style with room |
| **Micro** | one isolated effect, barely changes subject or composition | **stack fuel** |

> "Not every moodboard needs to carry the same amount of burden… one could be a little bit more of a
> 'hey this is a nice little seasoning to put on your bland chicken.'" — [MOOD @ 02:20, 2025]

A micro asset is the *most* valuable kind, because it composes. If your library has no micro tier, that is
the finding.

## Step 3 — The solo → stack ladder

The sweep proper. One prompt, held constant, up the rungs:

1. **Baseline alone** — your global/personalization layer only, no boards.
2. **Each asset solo** (already done in Step 2 — carry it forward).
3. **Baseline + one asset**, for each asset.
4. **Pairs**, added one at a time, so every addition is attributable.
5. Stop when you can no longer name what the last addition contributed.

> "So this I just ran global. Then we ran a different moodboard. Then we ran these together. So this is
> just kind of showing you what happens to stacking versus running a moodboard solo — then I just kind of
> went and stacked one at a time." — [MOOD @ 23:13, 2025]

**Prioritise opposition pairs.** They are where the non-obvious results live:

> "Cenote and this ethereal one together — very very well. So it's like more of a super gritty dark
> high-contrasty with a very ethereal sort of soft. It's like blending two opposites together — that's how
> I like the opposites. Like putting my black and white one with my super colorful one. I like doing the
> juxtaposition there because you get some really cool stuff." — [MOOD @ 20:39, 2025]

**And test at least one asset as a brake.** A deliberately flat, unstylised asset used to *pull back*
over-cooked output is the highest-utility item in a library and nobody builds one on purpose:

> "I was getting these really crazy images that I wanted, but they were so overdone in terms of texture.
> And then I applied like my little iPhone moodboard to it and it brought it right back down to reality,
> exactly where I wanted it to be." — [MOOD @ 03:44, 2025]

## Step 4 — Sweep the weight, don't guess it

For every combination worth keeping, sweep the reference coefficient rather than picking one.
Every reference mechanism in every generator has a weight, because every one of them is a blend, and
blends have coefficients. Batch the range in a single submission using whatever the current tool's
permutation facility is.

> "Do you know what [the style reference] is, how comfortable are you with it, **do you know how to weight
> it?** … If it's 'I'm super comfortable' and then I get to 'I don't know how to weight it' — okay, sure,
> then you don't really know, because you're not able to control it." — [MOOD @ 07:21, 2025]

Also sweep the **second-order** weight where the tool allows it — your baseline/personalization layer
against the assets, not just the assets against the prompt [MOOD @ 16:38, 2025].

Record the winning coefficient. A recipe without its weights is not a recipe.

## Step 5 — Name it, or it didn't happen

Every asset gets a **name** and a **one-line behaviour note** in his register — concrete, sensory,
no adjective without a referent:

> "This is the Cenote, where it's going to be way more dark and mysterious and gritty textured…
> deep blacks, deep blues, deep greens." — [MOOD @ 34:02, 2025]

Every kept combination gets a **recipe line**: assets, order, weights, and *what kind of asset it is for*.
That last clause is the one that makes it retrievable under deadline, and it is the answer to his own
complaint at [MOOD @ 23:33].

## Step 6 — Go deep on the one

The sweep produces candidates, not deliverables. Name the transition out loud.

> "Don't get lost in going too far in too many directions that you forget to go deep enough in one…
> dig into things that you really like, push it, because that's how you go from the good to the great."
> — [MOOD @ 33:19, 2025]

Pick the single best frame from the sweep and branch **from that frame**, at high deviation, repeatedly —
not from the prompt. *"Now I have to go and run these actually individually instead of just bashing
everything together"* [MOOD @ 26:44, 2025].

---

## Output schema

```
# Moodboard Sweep — <library or project name> — <date>

## Sweep constants
Probe prompt: <verbatim>
Aspect: <> · Stylization dial: <> · Images per run: <> · Tool + version: <>

## Board Cards
### <ASSET NAME>
Tier: tight | broad | micro
Null-run behaviour: <palette · light · texture · subject bias · era · refusals>
Under probe: <how much survives direction>
Best weight: <coefficient + range tested>
Stacks well with: <names> · Fights with: <names>
Use for: <asset types>

## Stack Matrix
| Combination | Weights | What the stack adds | Verdict |

## Named production recipes
R1 · <name> — <assets, order, weights> — for <asset type>

## Library gaps
<what the library cannot currently do — esp. missing micro/brake assets>

## Deep-dive candidate
<the one frame worth pushing, and why>
```

**Length:** 1–2 pages plus one card per asset. If it runs longer, the sweep was too wide — cut assets,
not depth.

## Quality gate

- [ ] One probe prompt, unchanged across every run, recorded verbatim.
- [ ] Every asset has a **null run** — not just a probe run.
- [ ] Every asset has a tier and a behaviour note written in concrete sensory language, no bare adjectives.
- [ ] At least one opposition pair tested, and at least one asset evaluated as a **brake**.
- [ ] Weights were swept, not guessed, and the winning coefficient is recorded on every kept recipe.
- [ ] Every kept combination has a name and an "use for ___" clause.
- [ ] Library gaps named — including "we have no micro tier" if that's true.
- [ ] No model name, parameter syntax or menu path is taught as current anywhere in the deliverable.

## Example output (abridged)

```
# Moodboard Sweep — My.BPM streetwear library — 2026-08-02
Probe: "editorial photography, full body, streetwear" · 3:4 · 6 per run

### GRAIN-05  (micro)
Null run: near-monochrome warm grey, no subject bias, heavy 400-speed grain,
  soft halation on highlights. Refuses saturated colour.
Under probe: composition and subject fully survive; only surface changes.
Best weight: 0.4 (swept 0.2–1.0; above 0.6 it eats the palette)
Stacks with: CONCRETE-01, NIGHTMARKET-02 · Fights with: CHROME-03
Use for: unifying a mixed-source lookbook

### NIGHTMARKET-02  (broad)
Null run: sodium and neon, wet asphalt, deep blacks with coloured lift in the
  shadows, crowd bias — puts people in frame unasked. Refuses daylight.
...

## Named recipes
R1 · "House Night" — NIGHTMARKET-02 (0.7) + GRAIN-05 (0.4) — for campaign hero frames
R2 · "Flatten" — baseline (1.0) + PHONE-FLAT-06 (0.8) — brake, for pulling back over-cooked R1 output

## Library gaps
No daylight asset at all — every board is night-biased. No brake other than
PHONE-FLAT-06. Build two micro boards: overcast-daylight, and a clean-studio white.
```

**Execution prompt:** `references/prompts-v2/moodboard-sweep-report.md` — honor its Output Contract.
