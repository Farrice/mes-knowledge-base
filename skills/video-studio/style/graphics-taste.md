# Graphics Taste — the Edit Bay's taste skill (approach, not preset)

Motion graphics are front-end design: every HyperFrames/Remotion comp is HTML/TSX, so
graphic quality IS front-end craft. Left alone, models produce default-styled slop.
This file is the design APPROACH a working designer would hold — it improves graphics
in ANY style (a preset produces one). Load it, plus the named stack below, before
building ANY comp. REVIEW.md blockers cite these rules as `graphics-taste#<n>`.

## The named load (MANDATORY before the first comp of a session)
1. This file.
2. `frontend-design` skill (Skill tool) — the general front-end craft layer.
3. The style-file merge (default → `_active/farrice-brand/voice/video-style.md` → project) — palette, faces, named graphic types.
4. On taste-fog or "is this slop?": `skills/grace-liu/SKILL.md` (three layers, five tests) — the judgment layer above craft.
5. Full art-direction ambition (title sequences, campaign-grade cards): `/satori-design-think` brief first.

## The rules (cite by number)

1. **Every element authored or deliberately open.** Font, weight, color, spacing, motion curve — anything you didn't decide, the engine's defaults decided. Count your silent delegations before rendering; more than zero unnamed = not ready.
2. **One idea per graphic; one focal point per frame.** If the eye doesn't know where to land in 200ms, the graphic failed. A card needing a paragraph is a diagram beat.
3. **Hierarchy is size + weight + position — never decoration.** No gradients, shadows, glows, or borders doing work that type scale should do. Premium Minimal earns richness through restraint.
4. **Motion is motivated.** A graphic enters because something in the VO/gesture called it (the `[gesture:]` cue), moves with intent (one entrance, one settle, one exit), and never animates just to prove it can. Easing: fast-in, gentle-settle; no bounces unless the brand file says play.
5. **Name what is in tension.** A frame where every element agrees with every other is the definition of slop (St. Pierre check). One contrast axis minimum: scale against calm, ink against space, a serif statement against grid coldness.
6. **The squint test at platform size.** Shrink to a phone: text still readable, focal point still first, margins still breathing. Anything that dies at 400px wide dies in the edit.
7. **Brand type law**: display face for statements, text face for data, NEVER a third; wordlist spellings exact; palette only from the brand file — a hex the brand file doesn't contain is a defect, not a choice.
8. **Real data, real alignment.** Charts use true numbers with sources (factual floor applies to graphics); grids align to an actual grid — 2px drift reads as cheap at every size.
9. **Would this have looked the same without you?** (grace-liu travel test) If the comp could have come from any prompt by any operator, it's mass-produced. Name the three invisible decisions that make it THIS video's graphic.
10. **Slop tells, auto-blockers**: default system fonts where brand faces exist · centered-everything layouts · rainbow/random hues · drop-shadow-on-everything · filler icons (rocket, lightbulb, gears) · lorem-adjacent labels · emoji as design elements. Any one = blocker with this citation.

## Deterministic pre-render check (run before every comp render)
Grep your comp source for: font-family declarations not in the brand file · hex values not in the brand palette · `text-shadow`/`box-shadow` stacks · more than 2 font families. Hits = fix before rendering — don't spend a render learning what grep already knew.
