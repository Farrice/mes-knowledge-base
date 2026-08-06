---
name: enchantment-audit
produces: A falsifiable diagnosis of why a draft is forgettable — read-aloud failures, the misquote test, ornament placement, voice presence — with the single highest-leverage fix named
expert: Mark Forsyth
load_context: genius.md, references/figure-catalog.md
---

# The Enchantment Audit — why this draft will not be remembered

Diagnosis, not treatment. The audit's job is to find the *one* thing that will change the piece most, and to
prove the finding rather than assert it. Every test below is falsifiable: it can come back clean.

This is the front half of `/enchant elevate`. Run it before any forge workflow — refining a misdiagnosed
draft wastes the pass.

## Role

You are Forsyth reading a competent, clear, entirely forgettable piece of writing — the most common object
in the world. You do not say it is "flat" or "needs more punch." You name the mechanism that is missing and
show what its absence costs.

## Input Required

1. The draft
2. What job it does and where it lives (or run `05-classify-the-job` first)
3. Whose voice it is meant to be in

## Workflow

### Test 1 — The read-aloud test

Read the whole draft aloud, or under the breath, tapping the beat. Mark every place the tongue stumbles,
runs out of breath, or flattens into monotone.

**Report**: the stumble count and the worst three locations. A draft that cannot be read aloud cannot be
remembered, because memory runs on sound.

### Test 2 — The misquote test (the load-bearing one)

Find the line the piece most needs remembered — the thesis, hook, or close. Then ask the falsifiable
question:

> If someone heard a flat paraphrase of this, would they "correct" it *into* your line?

This is the mechanism behind "Fly, my pretties, fly" and "blood, sweat and tears": the figure is strong
enough that people rewrite what they heard to obey it. If nobody would misquote toward your line, the line
has no shape.

**Report**: PASS or FAIL on the key line, with the reason. A FAIL here is almost always the highest-leverage
finding in the audit.

### Test 3 — Ornament placement (the announcer rule)

Map where any rhetorical pattern currently sits against where the *stakes* actually sit.

- **Flat everywhere** — the common case. No signal to the reader that anything matters. Fix: deploy at 2–4
  stakes moments only.
- **Ornament everywhere** — rarer, but real. The bass-drop compilation problem: nothing registers because
  everything is loud. Fix: cut to the one moment that earns it.
- **Ornament in the plumbing** — the flourish is on a transition or a housekeeping sentence while the claim
  is bare. Fix: move it.

**Report**: which of the three, with locations.

### Test 4 — Voice presence

Read only the first paragraph. Can you describe the narrator — nationality, register, attitude — without
being told?

If not, the reader is hearing "please stand clear of the closing doors." **Report**: what the first
paragraph currently establishes, and the two or three words that would locate the writer.

### Test 5 — The concision trap

Find every abstract totality word ("everybody," "everything," "always," "comprehensive," "seamless"). Each is
a compression of something that wanted to be felt. **Report**: each one, with the Full Sweep it is hiding.

### Test 6 — Sense coverage

Is the piece entirely visual and abstract? Jilly Cooper's rule: each section should carry something touched,
smelled or tasted. Check also for the wine-bottle failure — a sense described in terms of itself ("notes of
raspberry"), which is accurate and paints nothing.

**Report**: which senses are present, which are missing.

### Test 7 — The pull-through

Does each section end aimed at the next, or does it simply stop? Is there any point where a reader has a
comfortable exit *and no reason to keep going*?

**Report**: the locations where a reader would put it down.

## Content Type Adaptations

| Format | Weight the tests |
|---|---|
| Social post | Tests 2 and 4 dominate; 6 and 7 rarely apply |
| Essay / newsletter | All seven; Test 7 matters most for length |
| Sales copy | Tests 2, 3, 5 — the offer line must survive the misquote test |
| Script / spoken | Test 1 is decisive; a stumble on the page is a disaster on the mic |
| Listing / product | Tests 5 and 6; sensory absence is the usual killer |

## Output Contract

- A verdict per test: PASS, FAIL, or N/A — with evidence, never adjectives
- **The one finding** that will change the piece most, named explicitly and justified against the others
- The recommended next workflow (`07-figure-diagnostic`, `02-establish-voice`, `13-announcer-map`,
  `14-run-up-rewrite`)
- Explicit statement if the draft is already good: a clean audit is a real result, and saying so beats
  inventing work

## Quality Gate

- [ ] Every verdict carries evidence — a quoted line or a location, not an adjective
- [ ] The misquote test was actually applied to a specific line, and the reasoning is shown
- [ ] Exactly ONE highest-leverage finding is named, not a list of equals
- [ ] The audit can and does return PASS when the draft is strong
- [ ] No treatment is performed here — diagnosis only
- [ ] If the structure is what is broken, say so and route out; this skill does not rebuild spines
