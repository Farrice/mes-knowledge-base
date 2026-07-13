---
name: "Mark Kashef — Recon Dossier"
source_prompt: born-v2
skill: mark-kashef-wargame-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running the deliberate elicitation session that reaches what prompting alone cannot. "Every unknown lives in one of four boxes. Your prompt only fills the first box. The wargame drags the other three into the light." Known knowns are already in the brief. Known unknowns you could ask about directly — better prompting only ever improves these first two. But unknown-knowns (the operator's tacit context, never written down) and unknown-unknowns (the questions nobody thought to ask) are invisible to prompting by definition — you cannot prompt for what you don't know you don't know. This session exists specifically to drag boxes three and four into the light before a single move gets written.

## Input Required

- `[MISSION AS STATED]` — the mission or brief as currently written, with its existing filled and unfilled placeholders
- `[STAKES LEVEL]` — does this mission carry the ambiguity/consequence depth that justifies a full session (multi-session, client-facing, XHIGH-tier stakes)? A five-minute task skips this and routes straight to brief-writing
- `[DOMAIN MATCH]` — if the mission matches one of the known Kashef domains (website, copy, local-AI, tax, offer, chatbot, bugs, model, competitors, automation), its standard unknown-set checklist floor
- `[PRIOR RECON STATE]` — is this the mission's first recon session, or does a wargame already exist with its own RECON NEEDED items marked (those get settled by their own settling checks downstream, not re-elicited here)

## Execution Protocol

**Pre-Flight:** confirm this is the first recon pass for the mission (don't re-elicit what a wargame's own RECON NEEDED block already correctly defers); confirm the stakes actually justify a full session; commit to eliciting and surfacing only — never forcing the operator to decide anything on the spot, and never letting elicitation pressure a rushed answer; stay strictly read-only for anything touching the filesystem or a live system.

**Steps:**
1. Run the 2×2 explicitly, one quadrant at a time, against the mission as currently stated:
   - Known knowns — what's already in the brief or filled placeholders.
   - Known unknowns — placeholders still open, or anything already flagged as uncertain. List plainly.
2. Elicit unknown-knowns: ask 3–5 targeted questions about constraints, history, and taste never written down. Starting set, adapted to the mission: "What's failed on something like this before, and why?" / "What would make you reject a version even if it technically works?" / "What's the actual deadline pressure behind this — real or self-imposed?" / "Who else has to sign off, and what would they object to?" / "Is there a version of this you've already mentally ruled out? Why?" Log answers verbatim — this is tacit context that can only be told, never inferred.
3. Elicit unknown-unknowns: generate a list of every failure mode, edge case, and hidden assumption a domain expert would spot that the brief as written doesn't address, then the questions nobody thought to ask. The model generates this list without asking the operator to pre-answer it in the same pass. If the output only restates the known-unknowns list from step 1, push once more: "go deeper, these are things I already know I don't know." Bring the resulting question list back as a batch, not one at a time — this is elicitation, not interrogation.
4. Cross-reference the domain checklist: if the mission matches a known domain, confirm its implied standard unknowns (voice samples, machine specs, transcripts, statements, competitor list) are either filled or explicitly flagged in step 1's known-unknowns list.
5. Compile the recon dossier in four sections: filled placeholders (ready to wargame); RECON NEEDED candidates, each with a proposed settling check (a read-only command, a URL, or a specific question); a Frozen-Choice list (ambiguous decisions made now so the executor never has to); and the unknown-unknown question list with answers where given.
6. Set the consequence horizon explicitly for the mission's entire downstream wargame — how many orders of consequence deep should it fight this scenario. Write the answer into the dossier as its own line; the order-writing step inherits it rather than guessing.
7. Hand off to the order-writing step: the dossier becomes that step's recon-target line and frozen-choice input directly. This session never writes moves, expected observations, or fork triggers itself.

**Why a separate session, not folded into order-writing:** order-writing's own recon is read-only fact-finding against the world (files, URLs, transcripts); this session is read-only fact-finding against the operator's own head. Conflating them means the tacit-context questions get skipped in favor of the mechanical ones, because mechanical recon is easier to remember to do.

**Probe focus by content type:**
- Code build: taste rejections (what "looks wrong" even if functional), prior build failures. Domain floor: reference site/repo access, browser/device targets.
- Copy-content: voice landmines, past copy that got rejected and why. Domain floor: voice samples, ICP state-of-mind, CTA singularity.
- Research-analysis: what's already suspected but unconfirmed, prior analyses that missed the mark. Domain floor: source list, statements/categories on hand.
- Ops-automation: tolerance for tinkering, prior automation failures, what "acceptable risk" means here. Domain floor: machine specs, process steps, tool access.

## Output Contract

One recon dossier, no narrative padding, no "in summary" wrap-up. Exactly the sections below, nothing more, nothing collapsed. Filed at `.agent/missions/<name>/recon/<NN>-<slug>-dossier.md` (or the mission root if not yet scaffolded).

## Output Skeleton

```
# Recon Dossier — [mission name]

## Known / Known-Unknown Inventory
- Known: [item]
- Known-unknown: {{PLACEHOLDER}} — [what's missing]

## Unknown-Known Elicitation (verbatim Q&A)
Q: [question]
A: [verbatim answer]

## Unknown-Unknown Candidates (model-generated)
1. [failure mode / hidden assumption / question never asked]

## Frozen Choices
- [decision made this session, by the operator]

## RECON NEEDED Candidates
- [item] — settling check: [read-only command, URL, or specific question]

## Consequence Horizon
[first-order only / second-order / third-order] — set this session
```

## Quality Gate

- [ ] Unknown-unknowns list contains at least one item the operator did not originally raise — a list that only restates known unknowns fails outright
- [ ] No tacit-context question is answered by the model on the operator's behalf — genuinely unknown-known items stay open, logged, and handed forward
- [ ] Every RECON NEEDED candidate carries a settling check, not a bare flag
- [ ] Frozen-Choice list only includes decisions actually made in this session, not defaults the model invented to look complete
- [ ] Session stayed strictly read-only — no state-mutating action taken under the guise of "just checking something"
- [ ] Dossier is handed forward as input, never treated as a wargame itself — no moves, no expected observations, no fork triggers in this file

## Creative Latitude

The unknown-unknowns pass is genuinely generative work — it requires playing devil's advocate against the mission as stated, not listing generic risks. The strongest dossiers name a failure mode specific to THIS mission's actual shape, not a boilerplate risk that would apply to any project of the type. Push past the first plausible list; a second pass that goes "deeper, things I already know I don't know" is where the real value lives.

## Deploy When

Before any wargame is written, standalone, when the mission carries real ambiguity a plain brief won't surface — never a substitute for the settling checks inside a wargame's own RECON NEEDED block.
