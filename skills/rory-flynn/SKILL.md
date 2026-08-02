---
name: rory-flynn
description: "Production image OPERATIONS — the machine that runs image craft at volume without degrading it. Founder of Systematiq AI; Figma Config 2026 Maker Stage. Covers moodboard sweeps as a repeatable operation (null-run characterization, solo-to-stack ladder, weight sweeps, named recipes), style-code and style-handle libraries, the nine Image Elements and the photography-language doctrine for photorealism control, the frozen-backbone/variable-head brand consistency system, Keep/Change edit grammar, six-slot system prompts, feeder images and scale refs, and the handoff test for whether a workflow is actually a system. Use when the ask is many on-brand images rather than one good one: campaign asset systems, style libraries, brand-consistent generation at volume, characterizing or auditing style assets, making a generation workflow handoff-ready, or diagnosing why output looks like a render instead of a photograph."
---

# Rory Flynn — Production Image Operations

Founder, Systematiq AI — self-described "operational AI agency": *"we look into people's businesses, find
holes, and then we plug those holes with conventional AI tools"* [Config 2026 @ 02:04]. Came up running a
90-client email-and-paid-media agency shipping ~900 emails a month. **He is not an artist who learned
operations. He is an operator who learned images because the throughput problem would not go away.**

Client work shown on the Figma Config 2026 stage: **BarkBox**, **SharkNinja** (hundreds of products,
25 categories, 35 global markets, 25 new products a year).

**Where he sits in the creative floor program.** St. Pierre and Clark supply craft and taste. Flynn
supplies the machine that runs them at volume. Load him *after* the craft is decided — his own framing:
*"you already have experience… you've already built design systems. We're just doing it in a little bit of
a different function now"* [Config 2026 @ 08:12].

---

## SOURCE-WEIGHTING RULE (binding)

**The 2026 Config talk is the spine of this skill.** The 2025 moodboard session is current-adjacent. The
2024 Midjourney masterclass and the 2023 LinkedIn cheat sheet are **historical**: their doctrine is
carried forward, their parameter mechanics are not.

**Nothing in this SKILL, its workflows, or its execution prompts names a model, a parameter or a menu
path as current.** Every era-bound mechanic — slash commands, weight ranges, permutation syntax, named
upscalers, version-specific failure lists — is quarantined in **`genius.md` Appendix A**, tabulated by
era with dates, each paired with the durable principle it implemented. Verify anything there against the
live tool before executing it.

This is his own rule applied to his own corpus:

> "Screw the models. Every model I've mentioned here, they're all going to change, but if you build
> structured systems, you can just swap tools in." — [Config 2026 @ 20:30]

---

## THE THESIS

Everyone can now make one beautiful image. Almost nobody can make the nine-hundredth on-brand image this
month without the quality falling apart.

> "The truth is everyone can do this now. They can create cool things, but they do it in a vacuum. The
> real question is **can they do it at scale?**" — [Config 2026 @ 04:06]

The disease has a name: **creative inflation** — *"this never-ending need for new creative… multiple
channels and multiple formats, all the variants"* [Config 2026 @ 04:21]. The target is four dials with
none sacrificed: **more creative, faster, at higher quality, with more control** [Config 2026 @ 04:42].

---

## THE INVARIANT — AI is only three things

> "You don't need to know every tool. You just need to know that AI is only like three things and you can
> figure this stuff out. It's **context**, what you provide it, it's **direction**, it's how you brief it,
> and then it's **iteration**, what you do and iterate once you get something back." — [Config 2026 @ 05:22]

Every technique in this skill is one of the three wearing a different hat. References, feeder images and
scale refs are *context*. Formulas, system prompts and Keep/Change are *direction*. Weight sweeps and the
solo-to-stack ladder are *iteration*. **When a new tool lands, don't learn it — ask which of the three it
moves.**

---

## THE NINE IMAGE ELEMENTS (the non-negotiables)

Verbatim from the Config 2026 stage:

| Element | His gloss |
|---|---|
| **Shot / Photo Type** | How it's captured |
| **Subject + Action** | Who and what |
| **Environment** | Where it is |
| **Color Scheme** | The colors |
| **Technical Details** | The aesthetic |
| **Composition** | How it's constructed |
| **Lighting** | The tone |
| **Textures** | Surface. Depth. Feel. |
| **Details / Modifiers** | The subtle details |

> "I call these like the non-negotiables. They'll be represented just about every photo ever taken…
> **if you don't add something like lighting, the model will provide it for you.** So if we can control
> these, we can really control everything." — [Config 2026 @ 09:48–09:58]

**Silence is not neutrality. Silence is delegation.** Every unspecified element is a slot filled from the
model's priors — which is exactly where run-to-run drift and off-brand output come from.
**Unspecified = model-chosen = drift.**

**Simple Prompt Formula** (same slide):

```
[Photo type], [Subject + Action], [Environment], [Color Scheme], [Camera/Lens/Film],
[Lighting], [Composition], [Additional Details], [--parameters]
```

---

## THE FOUR OPERATIONS

### 1. Freeze the backbone, vary the head

The brand-consistency system, and the most transferable move in the corpus. Split the nine elements:
**freeze** color scheme, technical details, lighting, composition, textures, modifiers (the aesthetic);
**vary** shot type, subject + action, environment (the content).

> "Everything that's in white over here, that's what I'm just going to keep for every single prompt…
> the difference between close-up of a surfer with frost on his face versus close-up of a penguin on the
> beach — **that's all that I changed.** Everything else on the back end stayed the same."
> — [Masterclass 2024 @ 20:25]

Consistency stops being vigilance and becomes string concatenation — which means it's automatable and
delegable. → `workflows/style-code-library.md`

### 2. Sweep the style assets, then name them

You do not know what a style handle does until you have run it against nothing. The operation:
**null run → probe run → tier it → solo-to-stack ladder → sweep the weight → name it with a
"use for ___" clause.**

> "Type in an empty character like a period or a slash and just run it. And just dig into what that
> default is going to be." — [Moodboards 2025 @ 35:02]

The deliverable is never images. It is named recipes — his own stated failure otherwise:
*"am I going to remember to run this combination, and when am I going to use it?"* [Moodboards 2025 @ 23:33]
→ `workflows/moodboard-sweep.md`

### 3. Photography language, not realism adjectives

> "The best way to trigger [the model] into a photorealistic mindset is to use photography terminology."
> — [Masterclass 2024 @ 12:31]

The model has no realism dial. Photographic vocabulary relocates the generation into the region of the
space where photographs live. Words *from* photography (35mm, shallow depth of field, Portra 400, extreme
tonal balance, street photography) — never words *about* realism (photorealistic, 8k, ultra-detailed).

Two supporting rules: **2–3 words per slot, no fluff** [Masterclass 2024 @ 18:38]; and **the left anchor
dominates** — before adding a word to a failing prompt, rotate the leading term, because *"sometimes you
don't necessarily have a bad prompt. Sometimes you just structured it wrong"* [Masterclass 2024 @ 16:11].

And the finish: **the last step adds damage, never cleanup.** AI fails realism from the smooth side.
→ `workflows/photorealism-language.md`

### 4. Build the machine, then leave it

- **Keep / Change** — the whole edit grammar. *"Editing is keep this, change that. It doesn't have to be
  any more complicated than that"* [Config 2026 @ 10:52]. Name the invariant first, explicitly, or the
  model drifts on exactly the thing you needed preserved.
- **The six-slot system prompt** — Act As · Input/Output · Core Focus · Rules · Format · Limits.
  *"The system prompt is basically just a brief for the LLM"* [Config 2026 @ 12:07]. Full verbatim
  production example in `genius.md` Pattern 29.
- **Change the input, not the system** — *"when these workflows are built scalable and structured
  appropriately, **95% of the time they don't have to change**"* [Config 2026 @ 08:04].
- **Scale is a parameter, not an architecture** — ask the LLM for N instead of 1, terminate each item with
  a parse character, split, fan out. The slide calls the splitter *"the only addition."*
- **The feeder image** — build one canonical composite carefully; every downstream asset inherits from it
  rather than re-describing it. *"That one image feeds everything else"* [Config 2026 @ 16:34].
- **The scale ref** — when the model cannot *know* something (proportion, seam logic, material), generate
  a spec-sheet-style reference diagram that encodes it and make that the reference. His plate was titled
  `REFERENCE DIAGRAM: PROPORTION STUDY`. Highest-leverage single trick in the talk.
- **Manual where manual is better** — he composites by hand and gives the model only the lighting/depth
  pass. Layout is a decision; rendering is a task.

---

## THE TEST — is it actually a system?

> "Build this stuff not just for yourself, but for everyone else. **If only you can operate it, then it's
> not really a system.**" — [Config 2026 @ 20:41]

The pass condition is a type signature, not a feeling:

> "Now I can hand this off to someone else. **Any 2D vector image can go in and studio shots can come out.
> I've replaced myself.** We can go work on the next problem." — [Config 2026 @ 18:38]

Checklist: can someone else run it · does 1→400 need a different graph or one number · does it survive a
model swap · does 95% stay fixed when the input changes · is there an inspection point after every
transformation · **did it measurably save hours** (*"if it doesn't save time and it doesn't save money,
what the hell is the point?"* [Masterclass 2024 @ 41:02]).

---

## RAILS (his own, stated unprompted)

- **Asset-hack your own brands only.** *"Please do not go and do this for every other brand, please."*
- **Never "in the style of [living person]"** — litigation exposure via the prompt log. Decompose the
  style into components instead: *"you can create in his style, but **you learned**."*
- **Reverse-image-search anything commercial.** He reproduced a famous magazine cover from text alone.
- **Disclose AI use to clients.** *"It has to be an open discussion."*
- **Fidelity is a budget line, not an absolute.** *"Is it 100% accurate? No. A detailed eye will find
  something wrong with this every single time"* — and he ships anyway when the economics justify it.

---

## WORKFLOWS

| Workflow | Deliverable |
|---|---|
| `workflows/moodboard-sweep.md` | Board Cards + Stack Matrix + named production recipes for a style library |
| `workflows/photorealism-language.md` | A built prompt with all nine elements accounted for, a left-anchor swap ladder, and a finishing note |
| `workflows/style-code-library.md` | A Style Library Spec: frozen backbone, handle inventory, variable-head grammar, handoff signature, dated tool binding |

Deep pattern set (35 patterns, 15 signature moves, quality rubric, voice profile, and the dated
era-bound appendix): `genius.md`. Fidelity ledger and source dates: `references/source-notes.md`.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

4 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Rory Flynn — Asset Production System Blueprint** — `skills/rory-flynn/references/prompts-v2/asset-system-blueprint.md`
- **Rory Flynn — Brand Style Library Spec** — `skills/rory-flynn/references/prompts-v2/brand-style-library-spec.md`
- **Rory Flynn — Moodboard Sweep Report** — `skills/rory-flynn/references/prompts-v2/moodboard-sweep-report.md`
- **Rory Flynn — Photorealism Prompt Build** — `skills/rory-flynn/references/prompts-v2/photoreal-prompt-build.md`

<!-- END:execution-prompts -->
---

## VOICE (when writing or speaking as him)

Practitioner, fast, unpretentious. "Right?" as a beat between clauses. Deliberately non-expert about
craft — *"I am not a designer. I am not a media buyer. I'm none of those things really. I just try to
solve common problems."* Earns authority by describing operations, never by claiming taste. Names things
plainly (creative inflation, non-negotiables, asset hacking, feeder image, scale ref). Undercuts his own
demos when they fail on camera. Volunteers the disclosure nobody asked for. Deflates the magic:
*"not a lot of things have to change," "the only addition," "four clicks and we're here."*

Never claims an output is perfect. Never says a tool is the answer. Never teaches a prompt to copy —
teaches the formula that generates prompts.
