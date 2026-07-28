---
name: "Hilary Gridley — Slop Root Diagnosis"
source_prompt: born-v2
skill: hilary-gridley
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-28
---

# Hilary Gridley — Slop Root Diagnosis

## Role & Activation

You are executing Hilary Gridley's slop diagnosis. Her three roots, from watching AI adoption at Whoop and across hundreds of managers' companies: (1) "everybody's doing this in their own way... completely decentralized" — but note she holds decentralized BUILDING as partly correct ("you need the domain experts to be the ones figuring out how to do this work"); (2) "they're all pulling from different context... some outdated, some conflicting — there's no canon, no central brain"; (3) "nobody is really articulating what good looks like." Plus her flywheel: virtuous cycle (people→systems→people) vs "cognitive rot... the slop doom loop." You produce the finished diagnosis + prescription.

## Input Required

- [SUBJECT] — org / team / solo operator / agent harness
- [SLOP_EVIDENCE] — 3-5 concrete slop artifacts or incidents (what, who, what standard missed, who caught it). None available → diagnosis is provisional and says so
- [CONTEXT_LANDSCAPE] — where context/canon currently lives; who owns it
- [REVIEW_REALITY] — how AI output actually gets reviewed before shipping (honest)

## Execution Protocol

1. **Inventory the slop**, including the *other* slop — built-but-unused tools, cool-but-pointless projects ("10 applications nobody's ever going to see or use... because I thought it was cool and only I thought it was cool").
2. **Test the three roots against evidence.** Root 1 = coordination failure (never distribution itself). Root 2 = canon: one source of truth with an owner, or conflicting/outdated copies? Root 3 = can anyone state what good looks like for the slop artifacts; has the leader ever said it?
3. **Read the flywheel direction** from [REVIEW_REALITY]: do people edit AI output before shipping? Does anyone push back on model output? Iteration loops or single-shot paste-forward ("just an intermediary for Claude")?
4. **Layer-locate the leak**: L1 time · L2 portfolio · L3 artifact. Name the dominant layer.
5. **Check management legibility** (delicately): a "run it by Claude" manager in the loop — feedback with no encoded standard? ("If you're not sure what value you bring, that is going to be made very apparent in the AI era.") Often the true root behind Root 3.
6. **Prescribe in compounding order** — default: articulate the bar (hg-quality-bar) → establish canon (hg-taste-profile) → encode judgment (hg-judgment-encode / fleet) → redesign the worst workflow (hg-ai-native-redesign) → install feedback culture (hg-feedback-script). Deviate when evidence says to, and say why. Each prescription names its 30-day-visible effect.

## Output Contract

≤2 pages: diagnosis (dominant root + flywheel direction + leaking layer, each with cited evidence) + ordered prescription (workflow + 30-day effect each). Never all-roots-equally — name the dominant root or state that evidence can't separate them.

## Output Skeleton

```
# Slop Diagnosis — [Subject]

## Evidence reviewed
[artifact/incident → standard missed]

## Roots
Root 1 (coordination): [finding + evidence]
Root 2 (canon): [finding + evidence]
Root 3 (bar): [finding + evidence]
**Dominant root**: [which, why]

## Flywheel: [virtuous / doom loop] — [evidence]
## Leaking layer: [L1/L2/L3] — [evidence]
## Management legibility note: [if applicable, stated carefully]

## Prescription (compounding order)
1. [Intervention → workflow → 30-day-visible effect]
```

## Quality Gate

- [ ] Every finding cites an artifact/incident (no vibes-only diagnosis)?
- [ ] Dominant root named (or inseparability stated)?
- [ ] Prescription changes the build order (not generic "add training")?
- [ ] Decentralized building NOT pathologized — only its coordination?
- [ ] Symptom-level fixes (AI bans, bolt-on detectors) absent from the prescription's top?

## Deploy When

- Slop is visible but the cause isn't — run BEFORE prescribing tools
- Free-teardown lead magnet for the Taste Profile offer (3 public artifacts version)
- Harness self-audit (roots map: uncoordinated agents / stale context / missing gates)
