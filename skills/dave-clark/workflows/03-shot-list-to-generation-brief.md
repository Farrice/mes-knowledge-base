# Workflow 03 — Shot List to Generation Brief

**Produces:** a directed shot list where every shot is specified as a camera report, with coverage pairs, a
named look reference decomposed to mechanism, a cadence plan, and a generation/selection protocol — the
document you generate *from*, rather than improvising at the prompt bar.

**Use when:** starting anything longer than a single image; converting a script, idea or dump into something
generatable; or when previous attempts came out as a slideshow of unrelated postcards.

**Load first:** `genius.md` Part II (direction discipline).

> **Model-independent by design.** This brief specifies shots, not prompts. It hands off to whatever image and
> motion tooling is current — including a camera. The house's prompt-syntax lane
> (`skills/cinema-worldbuilder-pro/`, `/art-direct`, Nick St. Pierre's style layer) executes *from* this brief;
> it does not replace it.

---

## Step 0 — The chain, in order

> *"I still approach it like I would any other short film… I started with the script, I have an outline, I kind
> of had a shot list — which my shot list is what I use to prompt my stuff."* — [FWAI 2023 @ 08:20]

**Script → outline → shot list → prompts.** The prompt is the *last* artifact, never the first. Every taste
decision happens before a tool opens.

The honest alternative mode, which he also uses: the 4am exploratory session, *"crack open a beer… and see what
I get"* [FWAI 2023 @ 08:42]. That mode produces **material**. This workflow produces **films**. Know which one
you're in, and don't confuse the output of one for the other.

## Step 1 — The one-sentence idea, and the genre container

- **Idea in one sentence.** If it can't be said, the shot list will be decoration. [FWAI 2023 @ 06:45]
- **Genre container.** Choose the grammar whose conventions absorb the medium's current constraints — POV,
  found footage, dream, memory, surveillance, archival, animation. (Pattern 15) Name what the container
  *forgives*, so you stop paying to fix it later.

## Step 2 — The look reference, decomposed to mechanism

Not adjectives. A named work **plus the operations underneath it.** The model is his *Seven* read:

> film → *Seven* · DP instruction → "watch a bunch of perfume ads" · mechanism → "very high contrast, almost
> felt black and white, but there's always a splash, a wash of color… whites are really white and blacks are
> really black." [EVERY 2024 @ 27:29–28:05]

Produce a **look card** with five lines, each a mechanism, not a mood:

1. **Light** — source, direction, whether it's behind/beside/in front, what's motivating it.
2. **Contrast & black point** — where the shadows land, what's allowed to clip.
3. **Palette** — the base family, and the **one** accent family. (Observed discipline: never two competing
   warms. [REEL-obs 2025])
4. **Atmosphere** — what's physically in the air between camera and subject.
5. **Capture register** — grain, gate, handheld, format artifact. The one layer applied globally.

If any line reads as an adjective, it isn't done.

## Step 3 — Write the shot list as camera reports

> *"Think of generators as your film cameras… it's my Arri Alexa, it's my Sony Venice, it's my 35 millimeter
> film camera."* — [FWAI 2023 @ 05:26]

Each shot gets: **size · camera position and height · movement · light source and direction · subject action ·
duration intent.** The thing you'd hand a DP. Not a mood.

**Two mandatory disciplines:**

- **Coverage pairs.** Every hero beat gets its medium close-up *and* its wide, from the same setup, so the cut
  reads as one place. *"When I'm cutting it together it feels like it's just this consistent narrative. It's
  really just the same shot."* [FWAI 2023 @ 15:57]
- **The physics budget.** The camera isn't bound by physics [FWAI 2023 @ 06:00] — but spend that on *one* shot
  per piece. Mark which one. A film where every shot is impossible reads as a screensaver.

**Aspect and frame spec are set here, not later.** Decide the ratio before generation; plan to extend the plate
outward rather than crop it. (Pattern 14)

## Step 4 — Plan the cadence before you cut

Duration is an editorial variable, not a tool constraint. Assign an intended screen duration per shot and make
the sequence **deliberately uneven** — long beats against quick cuts.

> *"Sometimes you'll get an 8 second clip because I slowed it down, then you'll get a one second clip — and I
> use that cadence to help tell it."* — [EVERY 2024 @ 19:23]

Name the cadence reference the way he does: *Man on Fire*, *300*, *Dawn of the Dead*, *Oppenheimer*
[EVERY 2024 @ 17:44–18:12]. Then note which shots you'll generate **to be retimed** rather than used as-is.

## Step 5 — Set the generation and selection protocol

The part everybody skips, and cause #1 of flat work.

- **Takes per shot: five minimum.** Twenty for hero shots. *"How many generations you do? Well, just one"* is
  the diagnosis, every time. [EVERY 2024 @ 59:42, 52:13, 55:49]
- **Selection rule: composite, don't pick.** For each shot, ask what's best *in each* take and whether it can be
  masked into one plate — smoke from take 2, performance from take 4, light from take 1. [EVERY 2024 @ 54:08]
- **Fidelity rule: mask the source back in** where identity or resolution matters — the motion plate carries
  movement, the still carries fidelity. [EVERY 2024 @ 55:56]
- **Phrasing rule: phenomenon over category.** "Red liquid running down plaster," not "blood." More specific,
  renders better, and clears filters as a side effect. [FWAI 2023 @ 15:23]
- **Log as you go** — prompt, settings, which take, what got composited. (Pattern 3; scale to stakes.)

## Step 6 — Performance, if there is any

Direct it; don't generate it. Perform the read yourself and convert the timbre, and keep the raw human read
wherever it's better — *"I just thought it sounded better and more natural to have the natural pauses."*
[EVERY 2024 @ 20:20] Note per line which of the two you're doing.

**Execution prompt:** `references/prompts-v2/shot-list-generation-brief.md` — honor its Output Contract.

---

## Output shape

1. **Idea** — one sentence. **Container** — genre grammar + what it forgives.
2. **Look card** — five mechanism lines (light / contrast & black point / palette / atmosphere / capture register).
3. **Frame spec** — aspect, resolution, frame rate; extend-not-crop noted.
4. **Shot list** — numbered; each a camera report; coverage pairs marked; the one physics-budget shot marked.
5. **Cadence plan** — intended duration per shot, the uneven rhythm, the named cadence reference, which shots
   are generated to be retimed.
6. **Generation protocol** — takes per shot, selection/compositing rule, fidelity rule, phrasing rule, what's logged.
7. **Performance notes** — per line: directed-and-converted, or raw human.

## Quality gate

- [ ] The one-sentence idea exists and is specific
- [ ] Every look-card line is a mechanism, not an adjective
- [ ] Every shot reads as a camera report — size, position, movement, light source, action, duration
- [ ] Coverage pairs exist for every hero beat
- [ ] The physics budget is spent on exactly one shot, and it's marked
- [ ] The cadence plan is deliberately uneven, with a named reference
- [ ] Takes-per-shot is ≥5 and the selection rule is composite-not-pick
- [ ] Aspect and frame spec are set here, not deferred
- [ ] **No prompt syntax, model name or parameter appears anywhere** — this brief hands off to the syntax layer,
      it does not become it
