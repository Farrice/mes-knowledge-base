# Workflow 03 — The Style-Code Bank

**Deliverable:** dated *style-code entries* — named, reusable looks with the exact fragment or
reference, the conditions they need, and the conditions that break them. Plus, on request, a
**pairing table** (grade ↔ light condition) for a project or brand.

**Use when:** a sweep has just concluded · a look worked and you want it again · a brand or project
needs a repeatable visual system · you are inheriting someone's references and need them named.

**Do NOT use when:** nothing has been decided yet. A bank of untested entries is a wish list.
Sweep first (`01-aesthetic-sweep.md`), bank second.

---

## Why the bank is the real deliverable

> "The craft won't (and shouldn't) be about finding the right adjectives. It'll be a collection of
> choices that shape your preferences and refine your tastes until the tool thinks like you do."
> — St. Pierre, 2025-12-04

Prompts are disposable. The bank compounds. It is also the only artefact that survives a model
change — which is exactly why it is worth building.

## Step 1 — Harvest only what was decided

An entry earns its place if it was **chosen against alternatives**, not merely used. A look you
tried once and liked is a note; a look that won a side-by-side is a code.

For each: what was it up against, and why did it win?

## Step 2 — Name it so it can be recalled cold

Names should be short, specific and evocative of the *condition*, not the vibe.

- Good: `WET-SLATE-800T`, `DAWN-SOMBER-E100`, `MEZZOTINT-BLACKS`, `BAY-DOOR-FILL`
- Bad: `Look 3`, `Moody`, `The Good One`, `Cinematic v2`

His own private-vocabulary example: *"I use 'mezzotint' in my prompts a lot for deeper blacks."*
(2024-01-30) — a term kept because its effect was measured.

## Step 3 — Write the entry

Six fields, all required:

```
### [NAME]
- **Does:** one line — the actual visual effect, not the mood
- **Fragment / reference:** the exact prompt text, or the reference image path/URL
- **Needs:** the conditions it requires to work (light, surface, subject, frame shape, time)
- **Not for:** where it breaks or reads wrong
- **Beat:** what it won against, in one clause
- **Dated:** YYYY-MM-DD + the model/tool it was validated on
```

**The date and tool are not bookkeeping.** An undated style code is a liability the first time a
model updates. This is the whole reason `references/era-bound-mechanics.md` exists as a separate,
quarantined file.

## Step 4 — Build the pairing table

The highest-value artefact in his corpus is a **curated pairing table**: an emulsion/grade matched
to the lighting condition it was made for (2024-01-28, *"I curated some pairings you can play
with"*). Eleven of his are reproduced in `SKILL.md`.

Build the project's own. Rows are grades; columns are: paired light condition · subject type it
suits · one-line prompt shape · the frame shape it wants.

**Prompt shape for a pairing entry** (his form): *scene sentence. Mood-and-light sentence,
captured on [grade].* Two sentences. No buzzwords.

## Step 5 — Add the shorthand layer

Three kinds of dense, decomposable shorthand are allowed in the bank:

- **Design movements / registers** — *"Use specific design references like 'Scandinavian Bedroom'
  to help define the look"* (2023-02-23)
- **House styles / brand references** — *"Brand references like 'Pottery Barn' help define style"*
  (2023-02-23). Decomposable: you can name what makes them what they are.
- **Palettes** — brand colour treated as a first-class control layer, not a garnish (2024-02-14).

**Never banked:** artist names (*"I don't use artist names in my prompts. Never have"*,
2024-03-21) and quality-assertions (`8k`, `HDR`, `vray`). They cannot be swept, decomposed, or
explained to a client.

## Step 6 — Prune

Every entry that fails on a current model gets **struck through with a date**, not deleted — the
record of what stopped working is direction knowledge too. Entries older than a model generation
are marked `VERIFY` until re-run.

*Execution prompt: `references/prompts-v2/03-style-code-bank-entry.md` — honor its Output Contract.*

---

## Quality gate

- [ ] Every entry was chosen against alternatives, and names what it beat
- [ ] Names are condition-specific and recallable cold — no "Look 3," no bare mood words
- [ ] All six fields present on every entry, including **Not for** and **Dated + tool**
- [ ] No artist names, no quality-assertion buzzwords anywhere in the bank
- [ ] Pairing table (if built) states the light condition each grade was matched to
- [ ] Stale entries are marked `VERIFY` rather than silently trusted

---

## Example output (abridged)

### WET-SLATE-800T
- **Does:** tungsten-balanced night grade; halated highlights bloom on wet surfaces so they read
  cold and wet rather than dark and clean
- **Fragment:** `…captured on Cinestill 800T`
- **Needs:** a hard side or top light, a reflective/wet ground, dusk-or-later, 4:5 or 16:9
- **Not for:** warm daylight lifestyle, skin-led beauty frames, anything needing neutral whites
- **Beat:** Provia 100F (sharper, read as pharmacy) and Portra 800 (too forgiving, went warm)
- **Dated:** 2026-08-02 · validated on Nano Banana Pro

### MEZZOTINT-BLACKS
- **Does:** deepens blacks and adds an engraved tonal structure; pulls illustrative
- **Fragment:** `mezzotint photo…` (medium collision — pair with `photo` deliberately)
- **Needs:** something in the frame that wants density — night, shadow, heavy material
- **Not for:** clean e-comm, anything needing an even white ground
- **Beat:** plain "high contrast" phrasing, which flattened instead of deepening
- **Dated:** source St. Pierre 2024-01-30 · `VERIFY` on current models before campaign use

### Pairing table — supplement brand, night register
| Grade | Paired light | Suits | Prompt shape | Frame |
|---|---|---|---|---|
| Cinestill 800T | practical night / window at dusk | product on wet or reflective ground | scene · mood+light · captured on | 4:5 |
| Kodak Portra 800 | candle / low warm practical | hands, skin, warm materials | scene · mood+light · captured on | 4:5 |
| Fuji Neopan Acros 100 | single hard source + fog | B&W hero, high-contrast physique | scene · mood+light · captured on | 3:2 |
