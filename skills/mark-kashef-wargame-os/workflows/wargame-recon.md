---
description: Fire BEFORE any wargame is written, standalone, when the mission carries real ambiguity a plain brief won't surface — run this to drag tacit context (unknown-knowns) and the questions nobody thought to ask (unknown-unknowns) into the light. Feeds wargame-order; never a substitute for the settling checks inside a wargame's own RECON NEEDED block.
---

# /wargame-recon — The Unknowns-Elicitation Session

"Every unknown lives in one of four boxes. Your prompt only fills the first box. The wargame drags the other three into the light." A prompt only ever states known knowns. Known unknowns you could ask about directly. Unknown-knowns — Farrice's tacit context, never written down — and unknown-unknowns — what nobody thought to ask — are invisible to prompting by definition. This workflow is the deliberate session that reaches boxes 3 and 4 before a single move gets written.

## Pre-Flight Gate

- **First-pass check**: is this the mission's first recon session? If a wargame already exists with RECON NEEDED items marked, those get settled by their own settling check at `/wargame-run` time — don't re-elicit what's already correctly deferred.
- **Stakes check**: does the mission actually carry the ambiguity or consequence depth that justifies a full 2×2 — multi-session, client-facing, an XHIGH effort tag (website/tax/offer/bugs-grade stakes)? Heuristic 7: the human sets the consequence horizon. A five-minute task doesn't need this session; route it straight to `/wargame-brief`.
- **No premature freezing**: this session elicits and surfaces, it does not force Farrice to decide anything on the spot. Anything left genuinely unsettled becomes a RECON NEEDED candidate for the wargame, not a rushed answer here — genius.md Anti-Pattern 7 (recon that mutates state) extends in spirit to: don't let elicitation pressure a decision that belongs at wargame-write time.
- **Read-only in fact, not just in spirit**: if this session touches the filesystem or a live system at all (checking a repo's current state, opening a reference URL), it stays strictly read-only — `/goal` contract point 2, generalized: "recon is read-only. Read anything you need, run nothing that changes state."

## Skill Acquisition

- `genius.md` — the Epistemics section (2×2 unknowns, "the map is not the territory"), Decision Heuristic 3 (RECON NEEDED with the exact settling check)
- `extractions/wargame-source/mes-extraction.md` — Hidden Knowledge section, "The 2×2's real claim" paragraph, for the deeper epistemic justification if Farrice pushes back on why this session matters
- `references/mission-brief-library.md` — if the mission matches one of the 10 Kashef domains, its standard unknown set (voice samples for copy, machine specs for local-AI, statements for tax) is the checklist floor — confirm those specific unknowns are addressed, not just generic ones

## Execution

1. **Run the 2×2 explicitly**, one quadrant at a time, against the mission as currently stated:
   - Known knowns — what's already in the brief or filled placeholders.
   - Known unknowns — placeholders still `{{ }}`, or anything Farrice has flagged as uncertain. List them plainly.
2. **Elicit unknown-knowns.** Ask 3–5 targeted questions about constraints, history, and taste that Farrice has never written down. Starting set, adapt to the mission:
   - "What's failed on something like this before, and why?"
   - "What would make you reject a version even if it technically works?"
   - "What's the actual deadline pressure behind this — is it real or self-imposed?"
   - "Who else has to sign off on this, and what would THEY object to?"
   - "Is there a version of this you've already mentally ruled out? Why?"
   Log answers verbatim — this is tacit context the model can't infer, only be told.
3. **Elicit unknown-unknowns.** Dispatch an agent (or reason in-context) whose sole job is to enumerate failure modes and questions the operator never thought to ask, playing devil's advocate against the mission as stated.
   - The model generates the question list — it does not ask Farrice to pre-answer it in the same pass. This is the "guide you in areas where you would have never thought to go before" move.
   - Prompt shape: "You are not executing or wargaming this mission. List every failure mode, edge case, and hidden assumption a domain expert would spot that the brief as written doesn't address. Then list the questions I never thought to ask."
   - If the output only restates the known-unknowns list from step 1, the pass hasn't done its job — push it once more with "go deeper, these are things I already know I don't know."
   - Bring the resulting question list back to Farrice as a batch, not one at a time — this session is elicitation, not an interrogation.
4. **Cross-reference the domain checklist.** If the mission matches a `mission-brief-library.md` entry, confirm its implied standard unknowns (voice samples, machine specs, transcripts, statements, competitor list) are either filled or explicitly flagged in step 1's known-unknowns list.
5. **Compile the recon dossier**, four sections: filled placeholders (ready to wargame), RECON NEEDED candidates (each with a proposed settling check — a read-only command, a URL, or a specific question, per Heuristic 3), Frozen-Choice list (ambiguous decisions Farrice makes now so the executor never has to, per Heuristic 2), and the unknown-unknowns question list from step 3 with Farrice's answers where given.
6. **Hand off to `/wargame-order`.** The dossier becomes that workflow's recon-target line and frozen-choice input directly — this workflow never writes moves, expected observations, or fork triggers itself; that's Tier 1's job.

## Why This Session Exists (And When It Doesn't)

Better prompting only ever improves the first two boxes of the 2×2 — you can sharpen a known unknown into a specific question, but you cannot prompt your way into a box you don't know exists. That's the entire justification for running this as a SEPARATE session rather than folding elicitation into `/wargame-order`'s own recon step: `/wargame-order` recon is read-only fact-finding against the world (files, URLs, transcripts); this session is read-only fact-finding against Farrice's own head. Conflating them means the tacit-context questions get skipped in favor of the mechanical ones, because mechanical recon is easier to remember to do. Skip this workflow only when the Pre-Flight stakes check genuinely comes back low — running a full 2×2 against a trivial ask is its own anti-pattern (over-simulating a scenario that never fires, per Heuristic 7's consequence-horizon discipline).

## Setting The Depth Dial

Heuristic 7 hands the consequence horizon to the human, not the tool — this session is where that dial gets set for the mission's ENTIRE downstream wargame, not just for itself. Before closing the dossier, name explicitly: how many orders of consequence deep should the wargame fight this scenario (first-order failures only, or second/third-order knock-on effects too)? Write the answer into the dossier as its own line — `/wargame-order` inherits it rather than guessing.

## Content Type Adaptations

| Type | Unknown-known probe focus | Domain-checklist floor |
|---|---|---|
| **Code build** | Taste rejections (what "looks wrong" even if functional), prior build failures | Reference site/repo access, browser/device targets |
| **Copy/content** | Voice landmines, past copy that got rejected and why | Voice samples, ICP state-of-mind, CTA singularity |
| **Research/analysis** | What Farrice already suspects but hasn't confirmed, prior analyses that missed the mark | Source list, statements/categories on hand |
| **Ops/automation** | Tolerance for tinkering, prior automation failures, what "acceptable risk" means here | Machine specs, process steps, tool access |

## Output Requirements

Recon dossier at `.agent/missions/<name>/recon/<NN>-<slug>-dossier.md` (or the mission root if the folder isn't yet scaffolded), containing exactly these sections, no narrative padding, no "in summary" wrap-up:

```markdown
# Recon Dossier — <mission name>

## Known / Known-Unknown Inventory
- Known: ...
- Known-unknown: {{PLACEHOLDER}} — ...

## Unknown-Known Elicitation (verbatim Q&A)
Q: ...
A: ...

## Unknown-Unknown Candidates (model-generated)
1. ...

## Frozen Choices
- ...

## RECON NEEDED Candidates
- [item] — settling check: ...

## Consequence Horizon
[first-order only / second-order / third-order] — set by Farrice this session
```

## Quality Gate

- [ ] Unknown-unknowns list contains at least one item Farrice did not originally raise — a list that only restates known unknowns fails this gate outright
- [ ] No tacit-context question is answered by the model on Farrice's behalf — genuinely unknown-known items stay open, logged, and handed forward, never guessed
- [ ] Every RECON NEEDED candidate carries a settling check, not a bare flag — a flag with no check is half the work
- [ ] Frozen-Choice list only includes decisions Farrice actually made in this session, not defaults the model invented to look complete
- [ ] Session stayed strictly read-only — no state-mutating action taken under the guise of "just checking something"
- [ ] Dossier handed to `/wargame-order` as input, not treated as a wargame itself — this workflow produces no moves, no expected observations, no fork triggers
