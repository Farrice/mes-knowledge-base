---
name: "Mark Kashef — Mission Brief"
source_prompt: born-v2
skill: mark-kashef-wargame-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are writing the executor's contract, not a description of the work. "A mission brief is not a description of the work, it's the executor's contract. Every line in it either constrains the executor physically or it's decoration." This is the discipline underneath every one of the domain briefs — written before any wargaming happens, so it passes the same "executable blind" bar the wargame itself gets graded on. If a brief is vague enough that the executor would have to ask a question to proceed, it hasn't cleared the bar yet.

## Input Required

- `[RAW ASK]` — the mission as originally stated, however loose
- `[DOMAIN MATCH]` — whether the ask matches one of the known Kashef domains (website, copy, local-AI, tax, offer, chatbot, bugs, model, competitors, automation); if yes, adapt that domain's starting brief and placeholder map rather than writing cold
- `[DOWNSTREAM STATE]` — will this brief actually get wargamed before an executor sees it, or is it going straight to execution? (if no downstream wargame, the "no judgment calls left" discipline here matters MORE, not less)
- `[KNOWN SPECIFICS]` — ICP/audience, CTA, constraints, and evidence standard already decided, versus what's genuinely still open

## Execution Protocol

**Pre-Flight:**
- Domain-match check: does the ask match a known domain? If yes, adapt that starting brief and its placeholder map rather than writing cold.
- Scope-creep check: is "and also..." already showing up in the ask? Apply the scope clamp now, at brief-writing time, not at execution time when it's too late.
- Placeholder-honesty check: for every value not yet known, does it stay literal `{{PLACEHOLDER}}` rather than getting plausible-sounding filler? A brief with invented specifics reads as complete and isn't — the BLOCKED signal has to survive into the brief itself.

**Steps:**
1. State the definition of done in ONE sentence — not a feature list, a single observable state that means the mission is complete. Register example: "the executor can open index.html and it matches the reference site's tone/palette." If it takes two sentences, the mission is actually two missions.
2. Name the audience/ICP AND their state of mind arriving at this deliverable. Verbatim pattern: "`[ICP]`... arrive `[STATE OF MIND, e.g. skeptical, burned by two agencies]`." This is not throat-clearing — every later line gets checked against it.
3. Name the ONE CTA/outcome. Not several. A brief with multiple outcomes is multiple missions — split it now rather than let the executor guess which matters most.
4. Write constraints as physical rules, not preferences. Verbatim register: "No horizontal scroll at 375px," "Mobile first," "Semantic landmarks, labeled form inputs, alt text on every image." A constraint the executor can't mechanically check against reality isn't a constraint yet — it's a suggestion.
5. Write the evidence rule matching the domain — pick the register that fits: "If you cannot quote it, it does not exist" / "If you cannot point to evidence, it does not go in the report" / "Anything you cannot verify gets marked unverified rather than smoothed over." Any mission touching real-world claims needs one of these, verbatim in spirit.
6. Spell out the executor's own verification path — what it checks before it reports done, distinct from the wargamer's later 8-point grade. Verbatim register: "Open each page, exercise every link, every form validation path, and every interactive element... Audit each claim in your final summary against something you actually ran or read in this session."
7. Close with the scope clamp — the last line, not optional flavor text: "Do the simplest thing that works well. No features, no abstractions, nothing beyond this list."
8. Map every placeholder to a real resource where one exists — an ICP profile, a client identity doc, a voice-calibration file, a research agent's output. Anything with no matching resource stays literal `{{PLACEHOLDER}}`, explicitly unfilled, never quietly invented.

**Two failure modes this discipline prevents:**
- **Too vague to wargame** — "build a good landing page" gives the wargaming step nothing to fight on paper; every move it drafts is a guess about what "good" means. If wargaming keeps hitting RECON NEEDED marks that trace back to the brief being underspecified rather than the world being unknown, the fix is here.
- **Too specific too early** — pre-deciding implementation details that haven't actually been settled (a specific font, a specific automation tool) freezes a choice that belongs in the wargame's own Frozen-Choice list, decided deliberately — not smuggled into the brief as if it were a given. Distinguish "constraint" (physical, checkable, non-negotiable) from "assumption dressed as constraint" (a confident-sounding guess).

**When the ask doesn't match any known domain:** the 8 steps above still apply in full — domain matching is a shortcut for the placeholder map (step 8), not a requirement for the discipline (steps 1–7). Even an unmatched ask (a database migration, say) needs a one-sentence DoD, a named audience (even if the audience is "future-me resuming this project"), one CTA, physical constraints, and a scope clamp.

**DoD pattern and evidence-rule register by content type:**
- Code build: "Opens/runs and matches [reference] with zero [named failure]." Verification = exercised end to end, claims audited against what was actually run.
- Copy-content: "Moves [ICP] from [state of mind] to [CTA]." Skeptic-reread rule: cut every line that doesn't move the reader toward the CTA.
- Research-analysis: "Every claim traceable to a cited source." Unverified-label rule — conflicting sources named, never averaged.
- Ops-automation: "Each phase has a runnable acceptance check." Guardrail named for whatever breaks first in the pipeline.

## Output Contract

One mission brief at `.agent/missions/<name>/tasks/<NN>-<slug>.md`, using the exact `=== THE MISSION BRIEF (the executor's orders, not yours) ===` framing to separate the writer's voice from the executor's orders even inside the same file.

## Output Skeleton

```
=== THE MISSION BRIEF (the executor's orders, not yours) ===

Definition of done: [one sentence, one observable end state]

Audience: [ICP], arriving [state of mind]

CTA / outcome: [exactly one]

Constraints (physical, checkable):
- [constraint 1]
- [constraint 2]

Evidence rule: [domain-matched register, or n/a if no real-world claims]

Verification path: [what the executor checks before reporting done]

Scope clamp: Do the simplest thing that works well. No features, no
abstractions, nothing beyond this list.

[{{PLACEHOLDER}} for any value with no real resource to map to]
```

## Quality Gate

- [ ] One-sentence definition of done present, not a list
- [ ] Single CTA/outcome named — no multi-outcome briefs
- [ ] Every constraint is physically checkable — a human or model could verify pass/fail without judgment
- [ ] Evidence rule present if the mission touches any real-world claim
- [ ] Scope-clamp closing line present, verbatim in spirit
- [ ] Every placeholder either mapped to a real resource or explicitly left `{{PLACEHOLDER}}` — never invented
- [ ] No implementation detail that hasn't actually been decided is smuggled in as if it were a given constraint

## Deploy When

Writing a NEW mission brief from scratch — the executor's definition of done — before any wargaming happens; whenever a brief is vague enough that the executor would have to ask a question to proceed.
