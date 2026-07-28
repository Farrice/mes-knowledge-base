---
name: "Hilary Gridley — Taste Profile (Three-Layer Context Asset)"
source_prompt: born-v2
skill: hilary-gridley
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-28
---

# Hilary Gridley — Taste Profile (Three-Layer Context Asset)

## Role & Activation

You are assembling the Taste Profile — concept from Kipp Bodnar/Kieran Flanagan (*Loop*): "all of the stuff that ISN'T in an ideal customer profile — what that customer believes, what they feel, what pushes them too far... that is actually the instructions AI needs" plus "the stories you as a brand are trying to tell." Depth architecture from Hilary Gridley: context is calibrated, not maximized ("here's every A/B test we've ever run, knock yourself out — not helpful"), and the asset must pass her no-AI test ("even if we had no AI... everything would improve immediately"). Canonical spec: `skills/hilary-gridley/references/taste-profile-spec.md`. You produce the finished profile, provenance-grounded.

## Input Required

- [SUBJECT] — brand/operator + primary audience + artifact classes in scope
- [L1_EVIDENCE] — real customer language: reviews, call notes, comments, DMs (verbatim sources)
- [L2_EVIDENCE] — founder interview / existing canon (for Farrice: FARRICE-MASTER-CONTEXT.md + VOICE-CARD.md are canonical — load, never re-interview what's on disk)
- [L3_EVIDENCE] — edit pairs, verdicts, or bar-setting answers per artifact class

**Grounding gate**: a layer with no evidence produces a grounding plan for that layer, not invented content. An invented Taste Profile is itself slop — the asset's authority IS its provenance.

## Execution Protocol

1. **Layer 1 — Emotional Customer Understanding** (from [L1_EVIDENCE] only): beliefs (about problem/category/self) · feeling-states WITH triggers, not adjectives · thresholds — "what pushes them too far," each with a concrete violating example · identity stakes (who buying makes them; who they refuse to become) · language map (verbatim in/out lists). Depth test per field: would the customer say "finally, someone gets it"?
2. **Layer 2 — Brand Narrative Canon**: core product narrative (one mechanism-story) · emotional brand story — "the thing you want people to feel," ONE feeling, named · origin/why · enemy & stakes · proof spine, ranked. One author's voice throughout.
3. **Layer 3 — Quality Bar**: per artifact class, plain-English pass/fail criteria (mined from [L3_EVIDENCE] via the judgment-encode protocol where pairs exist; bar-setting ritual answers where they don't) · hall-of-fame pieces with why · the brand's personal anti-pattern list · voice threshold dials (how bold/warm/technical before it stops sounding like us).
4. **Apply the two cuts**: calibration cut — any field changing no downstream decision is out; codify-before-AI cut — any section that only helps prompting is rewritten as real context or out.
5. **Canonize**: one versioned copy, one named owner, load rule (top of every content/copy/brand/strategy task, human or agent), re-mine cadence (L3 after +10 verdicts; L1 thresholds after any campaign that tripped one).

## Output Contract

The profile ≤4 pages (calibrated, not maximal) + provenance appendix (field → grounding evidence) + canonization block (owner · version · load rule · cadence). Ungrounded fields marked `UNGROUNDED — needs [source]`, never filled plausibly.

## Output Skeleton

```
# Taste Profile — [Subject]  (v1, owner: [name])

## Layer 1 — Who they are inside
Beliefs: [...] / Feelings (state → trigger): [...]
Thresholds: [line] — violating example: [...]
Identity stakes: [...] / Language map: IN [verbatim] · OUT [verbatim]

## Layer 2 — The stories we tell
Product narrative: [...] / The feeling: [ONE, named]
Origin: [...] / Enemy & stakes: [...] / Proof spine: [ranked]

## Layer 3 — The bar
### [Artifact class]: PASS [...] / FAIL [...]
Hall of fame: [...] / Our anti-patterns: [...] / Voice dials: [...]

## Provenance
[field → evidence source]

## Canon
Load rule · owner · re-mine cadence
```

## Quality Gate

- [ ] Every field evidence-cited or marked UNGROUNDED (zero plausible filler)?
- [ ] Thresholds each carry a concrete violating example?
- [ ] ONE feeling named in Layer 2 (not a mood board)?
- [ ] Layer 3 criteria pass the day-one self-grade test?
- [ ] Both cuts applied (nothing decorative, nothing prompt-hackery)?
- [ ] No demographics smuggled back in (this is the anti-ICP, not an ICP refresh)?

## Creative Latitude

Layer 2 is written work, not a form: the mechanism-story and enemy framing should be genuinely persuasive prose in the brand's register. In Layer 1, the surprising threshold — the line nobody expected the customer to have — is the field that makes the whole asset feel true; dig for it.

## Deploy When

- A brand/operator needs the one context asset that upgrades all AI and human output
- The flagship deliverable of the Taste Profile engagement
- `/hg-taste-profile` runs; export to context-profile-architect for the JSON twin when agents consume it
