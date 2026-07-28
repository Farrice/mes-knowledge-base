---
description: Build the Taste Profile — the canonical three-layer context asset (emotional customer understanding + brand narrative canon + quality bar) that instantly raises the floor of all AI and human work for a brand/operator
---

# hg-taste-profile — The Moat Asset

The single document that ends the slop cycle for a brand: everything the ICP leaves out (what the customer believes, feels, what pushes them too far), the stories the brand is telling (product narrative, emotional brand story), and the quality bar (what good looks like, per artifact). "If everybody on your team has access to that same taste profile, the quality of work automatically goes up. The consistency automatically goes up." And the Gridley test that makes it real: it must improve a team that has NO AI.

Spec is canonical: `references/taste-profile-spec.md`. This workflow assembles a profile to that spec.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md` + `references/taste-profile-spec.md` + `references/loop-frameworks.md` §1 (attribution: concept = Bodnar/Flanagan; depth architecture = Gridley; assembly = this system).
- **Grounding gate (non-optional)**: Layer 1 requires real customer language (reviews, calls, comments, DMs); Layer 2 requires founder input or existing canon; Layer 3 requires edit pairs/verdicts or a bar-setting session. Missing sources → the workflow's first output is the grounding plan, not a profile. **An invented Taste Profile is itself slop — the asset's authority comes entirely from its provenance.**
- For Farrice's own profile: FARRICE-MASTER-CONTEXT.md + VOICE-CARD.md are canonical inputs — load before writing; never interview about what's on disk.

## Skill Acquisition

- `references/taste-profile-spec.md` (the template + assembly rules)
- `genius.md` §Context Doctrine, §Codify-Before-AI Dividend
- Stacking loads as needed: `avatar-machine` Phase-0 GROUND discipline for Layer 1; `context-profile-architect` for machine-native export

## Execution

1. **Scope + source inventory.** Brand/operator, primary audience, artifact classes in scope. Map evidence per layer; mark gaps `UNGROUNDED — needs [source]`.
2. **Layer 1 — Emotional Customer Understanding.** Mine real language → beliefs, feeling-states with triggers, thresholds (each with a concrete violating example), identity stakes, language map (verbatim in/out lists). Depth test per field: would the customer say "finally, someone gets it"?
3. **Layer 2 — Brand Narrative Canon.** Core product narrative (one mechanism-story), the emotional brand story (the single feeling, named), origin/why, enemy & stakes, ranked proof spine. One author's voice throughout.
4. **Layer 3 — Quality Bar.** Per artifact class: plain-English pass/fail criteria (mined via `hg-judgment-encode` where edit pairs exist; bar-setting ritual where they don't), hall-of-fame examples with why, the brand's personal anti-pattern list, voice threshold dials.
5. **Apply the two cuts.** Calibration cut: any field that changes no downstream decision — out. Codify-before-AI cut: any section that only helps prompting — rewrite as real context or out.
6. **Canonize.** One versioned copy, one named owner, a re-mine cadence (Layer 3 after every 10 verdicts; Layer 1 thresholds after any campaign that tripped one). State where it lives and the load rule: top of every content/copy/brand/strategy task, human or agent.
7. **Optional export**: hand to `context-profile-architect` 01 for the machine-native JSON twin when agents will consume it programmatically. The prose profile stays canonical; the JSON is a build artifact.

## Content Type Adaptations

| Subject | Adaptation |
|---|---|
| Farrice/Parallax | Layers 1-2 largely exist on disk (master context, voice card) — this workflow's value is Layer 3 + canonization into ONE asset |
| Client brand | Full three-layer build; the flagship deliverable of the productized offer (`hg-taste-profile-offer`) |
| Product launch | Scoped mini-profile: L1 for the launch audience, L2 for the launch narrative, L3 for launch assets only |
| Agent harness | Profile becomes the standing context load; L3 criteria become gates |

## Output Requirements

- Deliverable: the Taste Profile per spec (≤4 pages — calibrated, not maximal) + provenance appendix (which evidence grounds which field) + canonization block (owner, version, cadence, load rule).
- Zero ungrounded fields silently filled; gaps named honestly.
- Execution prompt: `references/prompts-v2/taste-profile.md`

## Quality Gate

genius.md rubric: standard provenance (every field evidence-cited), pass/fail legibility (L3), purpose specificity. Spec's own tests: finally-someone-gets-it (L1), single-feeling-named (L2), day-one self-grade (L3), codify-before-AI. Anti-patterns: ICP-with-a-new-name (demographics smuggled back in), invented customer language, maximal data-dump profiles, multiple conflicting copies.
