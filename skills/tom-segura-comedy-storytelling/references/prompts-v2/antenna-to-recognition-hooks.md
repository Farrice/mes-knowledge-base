---
name: "Tom Segura — Antenna to Recognition Hooks"
source_prompt: born-v2
skill: tom-segura-comedy-storytelling
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are translating a scored observation bank into scroll-stopping first lines by stacking Tom Segura's recognition antenna onto a LinkedIn/social hook container — Segura is a working A-list observational/storytelling comedian whose material is built on the "That's a Thing" antenna and the Universal-but-Unarticulated: "we've all experienced this, but that person was the first to actually say it." That "of course" charge — the reader thinking "why didn't *I* say it?" — is the entire payload this workflow converts into a hook. Segura supplies the recognition payload and the swerve; the hook format itself is a structural container borrowed from a social-copy hook engine (e.g. Lara Acosta's), not native Segura material — do not attribute hook mechanics to Segura beyond what genius.md supports.

Governing material: Pattern 1 (The "That's a Thing" Antenna), Pattern 3 (Universal-but-Unarticulated), Pattern 6 (Surprise is the Core Mechanism), Move: The "That's a Thing" Flag, Move: The Word Swap. Load `skills/tom-segura-comedy-storytelling/genius.md` before executing. Stack: load the social hook-engine partner (e.g. `.agent/workflows/ghostwrite.md` or the relevant LinkedIn-hook skill) for the structural container.

## Input Required

- **[OBSERVATION BANK]** — a ranked observation bank, ideally the output of the Observation Bank deliverable (5-10 top candidates). If no bank exists yet, generate one first — this workflow does not originate raw material, it converts an existing bank.
- **[PLATFORM]** (optional) — LinkedIn / X / other feed — affects hook length/format conventions from the stacking partner. Default: LinkedIn.

## Execution Protocol

1. **Pull the top-ranked observations from the bank (5-10 candidates).** For each, isolate the precise unarticulated-universal underneath it — the thing noticed "60, 70 times" but never voiced. State it in one plain sentence.
2. **Test each for the "of course" charge:** does it trigger "why didn't *I* say it?" If it only reads as "yeah, relatable," cut it.
3. **Translate each survivor into the hook container.** Open on the recognition, then swerve before the line resolves — build anticipation in one direction, turn somewhere else. Where possible, engineer the against-judgment beat (the line they laugh at reluctantly).
4. **Swap the pivotal word on every hook** for the funniest-sounding specific. Strip flat verbs and abstractions. Test the sound, not just the sense.
5. **Cut any winking or "this is a joke" signaling** — play the recognition straight so the swerve hits harder.
6. **Rank all hooks 1-N by scroll-stop potential,** scoring each on Recognition + Surprise (the two rubric rows this workflow owns). Tag each with the source observation and the format used.
7. **Render the ranked list** and mark the single strongest hook as the recommended open.

## Output Contract

- A numbered, ranked list of 5-10 hooks.
- Each entry: the hook line + source observation + hook format used + Recognition/Surprise scores.
- At least one against-judgment (reluctant-laugh) hook.
- The word-swapped final phrasing on every line.
- Ends with the single recommended open flagged, with one line on why it tops the ranking.

## Output Skeleton

```
## Ranked Hooks

1. [hook line, final word-swapped form]
   Source observation: [which bank entry this came from]
   Format: [hook container/format used]
   Recognition: [1-10] | Surprise: [1-10]

2. [hook line]
   Source observation: [...]
   Format: [...]
   Recognition: [n] | Surprise: [n]

... (continue for all 5-10)

## Recommended Open
[#1 hook, repeated] — why it tops the ranking: [one line]
```

## Quality Gate

- Does every hook trace to a specific bank observation (no hook invented from scratch outside the bank)?
- Did any observation that only reads as generically relatable ("yeah, that happens") get cut rather than converted?
- Is at least one hook an explicit against-judgment / reluctant-laugh construction?
- Does every hook's pivotal word pass the deflation test (swapping back to the flat word measurably weakens it)?
- Is the ranking justified by the stated Recognition/Surprise scores, not just ordered by gut with no visible reasoning?

## Creative Latitude

The hook container supplies structure, not content — resist letting the borrowed format flatten the specificity of the underlying observation into a generic template opener. The swerve is where the ceiling lives: two hooks built off the same observation can turn on completely different axes (register vs. target vs. scale), so if the first swerve that comes to mind feels safe, generate a second, sharper option before locking the ranking. Recognition and Surprise should genuinely diverge in scoring across the list — a set of hooks that all score 8/8 signals the differentiation pass wasn't rigorous.

## Deploy When

- You have a flagged observation bank and need first-line hooks for LinkedIn, X, or any feed.
- A post draft dies on the first line and needs a recognition swerve installed.
- Converting "that's a thing" fragments into scroll-stops without losing the raw charge.
