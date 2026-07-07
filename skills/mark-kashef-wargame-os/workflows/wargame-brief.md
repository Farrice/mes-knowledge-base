---
description: Fire when writing a NEW mission brief from scratch — the executor's definition of done — before any wargaming happens. This produces wargame-order's INPUT, not the wargame itself. Fire whenever a brief is vague enough that the executor would have to ask a question to proceed.
---

# /wargame-brief — The Executable-Blind Bar, At The Source

The discipline in all 10 Kashef task files, made explicit: a mission brief is not a description of the work, it's the executor's contract. Every line in it either constrains the executor physically or it's decoration. This workflow writes briefs that pass the same "executable blind" bar the wargame itself is graded on — the difference is this happens before a single move gets fought on paper.

## Pre-Flight Gate

- **Downstream-wargame check**: will this brief actually get wargamed before an executor sees it? If it's going straight to execution with no wargame pass, the "no judgment calls left" discipline here matters MORE, not less — there's no downstream pre-fight to catch what this step misses.
- **Domain-match check**: does the ask match one of the 10 Kashef domains in `references/mission-brief-library.md`? If yes, adapt that starting brief and its placeholder map rather than writing cold — reuse the frozen frame, change only the specifics.
- **Scope-creep check**: is "and also..." already showing up in the ask? Apply the scope clamp now, at brief-writing time — "Do the simplest thing that works well. No features, no abstractions, nothing beyond this list" (01-website.md, verbatim) — waiting until execution to enforce this is too late.

- **Placeholder-honesty check**: for every value that isn't known yet, is it staying `{{PLACEHOLDER}}` rather than getting a plausible-sounding filler written in its place? A brief with invented specifics reads as complete and isn't — the BLOCKED signal has to survive into the brief itself, not just the ledger.

## Skill Acquisition

- `assets/wargame-folder-template/tasks/*.md` — the 10 mission briefs; read the domain-matched one(s) verbatim for structural discipline before writing anything
- `references/mission-brief-library.md` — placeholder-mapping notes that point `{{ICP}}`, `{{BUSINESS}}`, research placeholders, etc. at real Antigravity resources
- `genius.md` — Anti-Pattern 4 (leave no judgment calls to the executor), Anti-Pattern 8 (claims without evidence)

## Execution

1. **State the definition of done in one sentence.** Not a feature list — a single observable state that means the mission is complete. Example register (01-website.md): "the executor can open index.html and it matches the reference site's tone/palette." If it takes two sentences, the mission is actually two missions.
2. **Name the audience/ICP AND their state of mind arriving at this deliverable.** Verbatim pattern (02-copy.md): "{{ICP}}... arrive {{STATE OF MIND, e.g. skeptical, burned by two agencies}}." This is not throat-clearing — every later line gets checked against it.
3. **Name the ONE CTA/outcome.** Not several. A brief with multiple outcomes is multiple missions; split it now rather than let the executor guess which one matters most.
4. **Write constraints as physical rules, not preferences.** Verbatim (01-website.md): "No horizontal scroll at 375px," "Mobile first," "Semantic landmarks, labeled form inputs, alt text on every image." A constraint the executor can't mechanically check against reality isn't a constraint yet — it's a suggestion.
5. **Write the evidence rule matching the domain.** Pick the register that fits: "If you cannot quote it, it does not exist" (06-chatbot.md), "If you cannot point to evidence, it does not go in the report" (07-bugs.md), "Anything you cannot verify gets marked unverified rather than smoothed over" (09-competitors.md). Any mission touching real-world claims needs one of these, verbatim in spirit.
6. **Spell out the executor's own verification path** — what it checks before it reports done, distinct from the wargamer's later 8-point grade. Verbatim (01-website.md): "Open each page, exercise every link, every form validation path, and every interactive element... Audit each claim in your final summary against something you actually ran or read in this session."
7. **Close with the scope clamp.** "Do the simplest thing that works well. No features, no abstractions, nothing beyond this list." This is the last line, not optional flavor text.
8. **Map every `{{PLACEHOLDER}}` to a real Antigravity resource** per `references/mission-brief-library.md` — `{{ICP}}` → deep-ICP profile path or `icp-deep-canvasser` output, `{{BUSINESS}}` → client CLAUDE.md, research placeholders → `execution/research.py` or the `competitive-intel` agent. Anything with no matching resource stays `{{PLACEHOLDER}}`, explicitly unfilled — never quietly invented.

## Worked Micro-Example

Compare a flat ask against its `/wargame-brief` version:

- **Flat**: "Write the copy for the new homepage."
- **Brief'd**: DoD — "the page reads as the natural next thing a skeptical [ICP] would want after landing." ICP + state of mind — "solo consultants who've been burned by two agencies already, arriving defensive." CTA — "book the intro call, nothing else." Constraint — "no hype adjectives, sentences a 7th grader can read." Evidence rule — n/a (no real-world claims here, this domain skips that line). Verification path — "reread as that skeptical reader, cut every line that doesn't move them to the CTA." Scope clamp — "two headline/CTA alternates only, nothing else gets variants."

The second version is wargameable. The first isn't — every move `/wargame-order` would draft against it is a guess about what "the copy" even means.

## Content Type Adaptations

| Type | DoD sentence pattern | Evidence-rule register |
|---|---|---|
| **Code build** | "Opens/runs and matches [reference] with zero [named failure]" | Verification = exercised end to end, claims audited against what was actually run |
| **Copy/content** | "Moves [ICP] from [state of mind] to [CTA]" | Skeptic-reread rule: cut every line that doesn't move the reader toward the CTA |
| **Research/analysis** | "Every claim traceable to a cited source" | "Unverified" label rule — conflicting sources named, never averaged |
| **Ops/automation** | "Each phase has a runnable acceptance check" | Guardrail named for whatever breaks first in the pipeline |

## Two Failure Modes This Workflow Exists To Prevent

**Too vague to wargame**: a brief that says "build a good landing page" gives `/wargame-order` nothing to fight on paper — every move it drafts is a guess about what "good" means. If `/wargame-run` keeps hitting RECON NEEDED marks that trace back to the BRIEF being underspecified rather than the world being unknown, the fix is here, not there — rewrite the brief.

**Too specific too early**: a brief that pre-decides implementation details Farrice hasn't actually settled (a specific font, a specific automation tool) freezes a choice that belongs in the wargame's Frozen-Choice list, decided deliberately, not smuggled into the brief as if it were a given. Distinguish "constraint" (physical, checkable, non-negotiable) from "assumption dressed as constraint" (a guess that happens to be phrased confidently).

## When The Ask Doesn't Match Any Of The 10 Domains

Most Antigravity work won't map cleanly onto website/copy/local-ai/tax/offer/chatbot/bugs/model/competitors/automation. When it doesn't, the 8 execution steps above still apply in full — the mission-brief-library.md domain match is a shortcut for the placeholder map (step 8), not a requirement for the discipline (steps 1–7). A brief for, say, a Notion database migration still needs a one-sentence DoD, a named audience (even if the audience is "future-me resuming this project"), one CTA, physical constraints, and a scope clamp.

## Output Requirements

`.agent/missions/<name>/tasks/<NN>-<slug>.md`, using the exact `=== THE MISSION BRIEF (the executor's orders, not yours) ===` framing from the source template — this separates the wargamer's voice from the executor's orders even inside the same file.

## Quality Gate

- [ ] One-sentence definition of done present, not a list
- [ ] Single CTA/outcome named — no multi-outcome briefs
- [ ] Every constraint is physically checkable (a human or model could verify pass/fail without judgment)
- [ ] Evidence rule present if the mission touches any real-world claim
- [ ] Scope-clamp closing line present, verbatim in spirit
- [ ] Every placeholder either mapped to a real resource or explicitly left `{{PLACEHOLDER}}` — never invented
- [ ] No implementation detail Farrice hasn't actually decided is smuggled in as if it were a given constraint
- [ ] The brief reads as orders TO the executor, not notes ABOUT the mission — "the executor's orders, not yours" framing intact
