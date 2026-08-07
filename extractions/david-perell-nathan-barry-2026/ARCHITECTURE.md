# Architecture Checkpoint 2: David Perell Idea-to-Culture Expansion

> **Approval required before build.** This document specifies the exact production changes proposed for Phase 5. No production skill, agent, prompt, wrapper, registry, or verifier has been changed in Phases 3 and 4.

## Architecture Verdict

Expand skills/david-perell-writing in place. Keep David Perell as one expert, david-perell-writing as one skill, and /david-perell as the only expert front door.

The Idea-to-Culture Loop is an internal route across 13 bounded workflows. It does not become a second expert, a competing skill, or a new hot command.

The approved count remains 13: three preserved POP workflows plus ten source-grounded additions. An adversarial review challenged two pairs as possible duplication. The architecture keeps them because each pair has a different input, decision, and finished artifact:

1. **Observation Mind-Mine versus Public Reps Learning Loop.** Mind-Mine works before publication and returns raw idea leads. Public Reps requires an authorized practice plan or real response evidence and returns a learning receipt. It never performs platform analytics or publishes.
2. **Current-Fit Diagnostic versus Timely Shell, Timeless Core.** Current-Fit is a gate that can stop the route. Timely Shell is a producer that runs only after the gate passes and must return a thesis-preservation receipt.

The later build must pass a non-overlap fixture for both pairs. Indistinguishable outputs count as a build failure.

## Skill Manifest

The proposed SKILL.md frontmatter is:

1. **Version:** 3.0.
2. **Format:** completion-engine.
3. **Workflow count:** 13.
4. **Primary workflow:** workflows/david-perell-idea-courage-craft-triage.md.
5. **Routing posture:** long-tail and on demand.
6. **Source boundary:** retain the 2026-07-01 POP source history and add the QsHm_0MEhX8 transcript captured on 2026-08-04 as a separate evidence lane.

The new primary workflow matters. The current front door selects POP diagnosis by default, but the new source proves that weak writing may originate in the idea or the writer's willingness to state it. The triage gate must run before a full structured intervention.

## Tier 1: Foundation Workflows

### 04. Idea-Courage-Craft Triage

**Physical file.** skills/david-perell-writing/workflows/david-perell-idea-courage-craft-triage.md.

**Inputs.** Raw idea or draft; intended claim; supporting evidence; reader outcome; and any assertion the writer keeps softening or removing.

**Finished artifact.** A Writing Bottleneck Verdict with one primary route: IDEA, COURAGE, CRAFT, or INSUFFICIENT EVIDENCE. It names the evidence, the weakest link, bounded secondary support, and the exact next workflow.

**Source basis.** David's three-bottleneck diagnosis, 00:05:06 to 00:07:11.

**Boundary.** The source diagnoses courage but does not teach a complete courage intervention. The workflow may identify the feared supported sentence and return a human decision. It may not invent controversy, beliefs, or life experience.

### 05. Observation Mind-Mine

**Physical file.** skills/david-perell-writing/workflows/david-perell-observation-mind-mine.md.

**Inputs.** A question or domain; the user's lived-material boundary; a timebox; optional notes; and privacy constraints.

**Finished artifact.** A Mind-Mine Sheet containing surfaced thoughts, evidence labels, observed tensions, three promising leads, and candidate bits for further development.

**Source basis.** Public-output observation and the restaurant page-fill practice, 00:07:30 to 00:12:46.

**Boundary.** This workflow owns private noticing and extraction, while Dan Wang owns the deeper move from field observation into analytical writing. Private material remains outside publication.

### 06. 60-20-10 Bit Refinery

**Physical file.** skills/david-perell-writing/workflows/david-perell-60-20-10-bit-refinery.md.

**Inputs.** A voice note or transcript; the core idea; audience; and the allowed durations.

**Finished artifact.** A Bit Card containing the full version, 60-second version, 20-second version, 10-second version, a phrase that survives, a meaning-loss ledger, and the repeatable core.

**Source basis.** David's expansion-before-compression sequence, 00:15:23 to 00:16:04.

**Boundary.** Workflow 02 sharpens a selected sentence after this workflow completes. Nathan's optional re-expansion step remains attributed to Nathan and Ultraspeaking if it is ever offered.

### 08. Current-Fit Diagnostic

**Physical file.** skills/david-perell-writing/workflows/david-perell-current-fit-diagnostic.md.

**Inputs.** A developed Idea Card; a sourced and dated signal packet; audience or brand territory; and a stated expiry window.

**Finished artifact.** A Current Fit Verdict that keeps idea quality, execution quality, current velocity, audience fit, and brand fit separate. The allowed decisions are ROUTE CURRENT, KEEP EVERGREEN, SCHEDULE, or HOLD.

**Source basis.** David's quality-by-current diagnosis, 00:17:16 to 00:23:21. Nathan's brand-fit refinement remains separately attributed.

**Boundary.** Attention Hijack finds live signals, and Lulu can score lifecycle. The Perell workflow judges whether the supplied signal is a legitimate carrier for the idea and returns HOLD when no signal packet exists.

## Tier 2: Practitioner Workflows

### 01. Diagnose and Rebalance

**Physical file.** skills/david-perell-writing/workflows/01-diagnose-and-rebalance.md.

**Status.** Preserve the POP method. Apply one surgical pre-flight correction because its current role text assumes the idea is probably fine. The workflow may run only after triage identifies a craft problem or the user explicitly requests a POP-only audit.

**Finished artifact.** The existing POP map, rewrite, change log, and weak-pillar note remain unchanged.

**Allowed changes.** Add the pre-flight gate, correct the stale assumption in the workflow and matching born-v2 prompt, and add the explicit execution-prompt pointer. Do not alter the highlight test, failure modes, sizzle logic, output contract, or POP quality gate.

### 02. Compress to Memorable

**Physical file.** skills/david-perell-writing/workflows/02-compress-to-memorable.md.

**Status.** Preserve the existing ladder and enrich it narrowly with the source-verified jargon trial.

**Finished artifact.** The existing ladder table, placement notes, flagship line, and rejects remain unchanged.

**Allowed changes.** Add the jargon-on-trial pre-pass, record the QsHm_0MEhX8 source anchor, distinguish conceptual compression from the 60-20-10 Bit Card, and add the explicit execution-prompt pointer. Do not upgrade the older POP or Buffett-ladder provenance labels.

### 03. Draft POP-First

**Physical file.** skills/david-perell-writing/workflows/03-draft-pop-first.md.

**Status.** Preserve the method and its matching prompt.

**Finished artifact.** The existing draft, pillar map, flagship line, and sizzle statement remain unchanged.

**Allowed changes.** Add an execution-prompt pointer and route users through the new triage gate when idea quality or conviction is unresolved, while the born-v2 prompt remains byte-identical.

### 11. Past-Present Braid

**Physical file.** skills/david-perell-writing/workflows/david-perell-past-present-braid.md.

**Inputs.** Grounded historical material; a present observation; thesis; sources; and target format.

**Finished artifact.** A Braid Map with historical beats, present contrasts, supported bridges, and either one drafted section or a complete outline.

**Source basis.** David's Modern World explanation, 01:26:07 to 01:29:06.

**Boundary.** Fixed alternation is prohibited. Each return to the present must reveal something material. Dan Wang or Susan Orlean can deepen the final prose, while /shaan-story-deploy still owns story dosage.

### 12. Placeful Voice Audit

**Physical file.** skills/david-perell-writing/workflows/david-perell-placeful-voice-audit.md.

**Inputs.** Draft; voice sample; supplied lived details; and any place or biography facts the writer authorizes.

**Finished artifact.** A Placefulness Audit containing a placelessness heatmap, template residue, missing-evidence requests, evidence-safe edits, and a downstream repair route.

**Source basis.** David's placefulness comparison, 01:20:00 to 01:22:17.

**Boundary.** The audit diagnoses and makes only evidence-safe edits. Ocean Vuong or high-taste-writing-os performs deeper line work. The workflow cannot invent a street, location, memory, emotion, sensory fact, or dialogue.

## Tier 3: Stacking Workflows

### 09. Timely Shell, Timeless Core

**Physical file.** skills/david-perell-writing/workflows/david-perell-timely-shell-timeless-core.md.

**Inputs.** A locked thesis and claim set; a validated current; audience; expiry; and distortion constraints.

**Finished artifact.** A Core Lock and Shell Set containing low-, medium-, and high-current frames, one selected why-now line, a claim-delta ledger, expiry, and an evergreen fallback.

**Source basis.** David's why-now frame swap, 00:31:05 to 00:32:52.

**Boundary.** The workflow cannot search for a current or invent one. Lara Acosta or Diandra Escobar may format a selected shell for a platform, but they cannot change the locked thesis.

### 07. Public Reps Learning Loop

**Physical file.** skills/david-perell-writing/workflows/david-perell-public-reps-learning-loop.md.

**Inputs.** Either an approved practice window or user-supplied published samples and response evidence.

**Finished artifact.** Before an event, the workflow returns an Authorized Rep Protocol with NO EVENT. After real evidence exists, it returns a Rep Learning Receipt containing observations, bounded hypotheses, confidence, and the next rep.

**Source basis.** David's account of public practice shaping opinions and awareness, 00:10:40 to 00:12:46, plus his response caveats at 00:17:16 to 00:20:52.

**Boundary.** Kieran Content Ops owns performance analysis and queue operations. Platform owners publish only with explicit permission. No publication evidence means no performance conclusion.

### 10. Scheduled-Current Archive

**Physical file.** skills/david-perell-writing/workflows/david-perell-scheduled-current-archive.md.

**Inputs.** Archive inventory; dated future-event packet; preparation lead times; expiry; and audience or brand fit.

**Finished artifact.** A Scheduled Archive Calendar linking each idea to a supported event, preparation date, release window, expiry, invariant core, and evergreen fallback, with invalid mappings retained as HOLD rows.

**Source basis.** David's scheduled-current preparation and modular readiness, 00:28:45 to 00:35:02.

**Boundary.** Lulu or the dated zeitgeist systems supply source evidence. Kieran owns storage and queue state. This workflow maps; it does not conduct live research or publish.

### 13. Current-or-Soul Portfolio

**Physical file.** skills/david-perell-writing/workflows/david-perell-current-or-soul-portfolio.md.

**Inputs.** Project list; desired reputation; named soul work; current opportunities; available capacity; and commercial constraints.

**Finished artifact.** A Portfolio Boundary that classifies each project as SOUL, CURRENT-FUNDED, BOTH, or HOLD. It records the creator's non-negotiables, stop rules, and next review date.

**Source basis.** David's current-versus-soul principle, 01:33:51 to 01:35:31.

**Boundary.** The source does not provide portfolio percentages, so the workflow cannot invent them. Any numeric allocation must come from the user. It makes no performance or revenue promise.

### 09 and 10 Current-Support Note

Both workflows receive bounded support from current-sourcing and platform owners. Their stacking placement records this dependency while David Perell still owns the finished judgment artifact.

## Routing Spine

The front door follows this sequence:

1. Run workflow 04 for any substantial full-process request.

2. If the idea is empty or insufficiently developed, route to workflow 05 and then workflow 06.

3. If the constraint is craft, route to workflow 01, 02, or 03 according to the requested deliverable.

4. If the idea is developed and timing matters, require a dated signal packet and run workflow 08.

5. A valid current may proceed to workflow 09. A future window may proceed to workflow 10. No honest fit returns HOLD or KEEP EVERGREEN.

6. Use workflow 11 when historical material must change how the present is understood.

7. Use workflow 12 when the prose is competent but source-less.

8. Use workflow 13 when current tactics may be displacing the creative mission.

9. Run workflow 07 only around an authorized practice plan or real public-response evidence.

One route owns each decision. Adjacent experts provide inputs or downstream craft without taking over the Perell judgment layer.

## Existing Files to Modify

1. **skills/david-perell-writing/SKILL.md.** Update the manifest to version 3.0, set the new primary workflow, add tiered routing, expand the description, add the source boundary, and preserve the generated execution-prompt region for regeneration.
2. **skills/david-perell-writing/genius.md.** Preserve the current POP text, then append the Idea-to-Culture decision framework, source-labeled patterns, hidden knowledge, anti-patterns, recognition test, and rubric.
3. **agents/david-perell/AGENT.md.** Replace the blanket idea-is-fine assumption with the triage gate. Add idea development, current fit, core preservation, placefulness, and soul boundaries. Remove reliance on an unverified current follower count from the activation identity.
4. **skills/david-perell-writing/references/source-ledger.md.** Add a dated 2026-08-04 note explaining that the 2026-07-17 absence finding was true at the time, a new transcript now exists, and the new transcript does not verify POP.
5. **skills/david-perell-writing/workflows/01-diagnose-and-rebalance.md.** Apply only the pre-flight correction and execution-prompt pointer described above.
6. **skills/david-perell-writing/references/prompts-v2/diagnose-and-rebalance.md.** Mirror the same pre-flight correction while preserving the POP execution protocol.
7. **skills/david-perell-writing/workflows/02-compress-to-memorable.md.** Add the bounded jargon-trial enrichment and prompt pointer.
8. **skills/david-perell-writing/references/prompts-v2/compress-to-memorable.md.** Mirror only the jargon-trial addition.
9. **skills/david-perell-writing/workflows/03-draft-pop-first.md.** Add its explicit execution-prompt pointer. Its matching prompt remains byte-identical.

agents/david-perell/memory/context.md remains unchanged until an actual run produces durable observed learning.

skills/david-perell-writing/references/PROVENANCE-2026-07-17.md remains byte-identical as a historical repair receipt.

## New Skill Files

### Workflows and Prompts

Create the ten new workflow files named above. Create one born-v2 prompt for each distinct deliverable under references/prompts-v2 with the same david-perell stem as its workflow.

The exact-stem rule matters because the menu minter attaches prompts only when workflow and prompt filenames match. The three legacy workflows retain explicit in-file pointers because their numbered workflow stems and unnumbered prompt stems do not match.

### References

1. **references/genius-patterns.md** contains the 17 source-labeled patterns and clears the current critical validation gap.
2. **references/hidden-knowledge.md** contains the fourteen operational inferences and their evidence boundaries.
3. **references/exemplars-QsHm_0MEhX8.md** contains six attributed calibration cases and anti-exemplars.
4. **references/claims-ledger-QsHm_0MEhX8.md** maps every new claim to speaker, timestamp, workflow, and proof state.
5. **references/PROVENANCE-2026-08-04-QsHm_0MEhX8.md** records source hashes, changed files, and the new-source boundary.
6. **references/cross-domain-patterns.md** contains the nine handoffs and explicit non-ownership rules.
7. **references/implementation.md** defines route order, handoff objects, context policy, and safe stop states.
8. **references/rubric_v1.md** contains the twelve-criterion rubric and source-recognition test.
9. **references/fixtures_v1.json** contains held-out behavioral cases in a machine-checkable form.
10. **references/preservation-lock-idea-to-culture.md** records protected hashes and allowed line-level changes.

Do not create a duplicate source-quote bank. The claims ledger should use paraphrases and only the shortest necessary source fragments.

## Command and Registration Plan

1. Keep /david-perell as the expert front door and /david-perell-writing as the skill front door.

2. Preserve the existing /david-perell-compress-to-memorable and /david-perell-draft-pop-first wrappers.

3. Create one explicit /david-perell-diagnose-and-rebalance wrapper for the legacy numbered workflow because the current minter would otherwise infer the ambiguous /david- prefix.

4. Let the ten new exact-stem files mint ten matching /david-perell-* workflow commands.

5. Add only two project-local Codex bridges: source-command-david-perell and source-command-david-perell-writing. Do not mirror all 13 workflows into separate Codex skills.

6. Regenerate AGENT_INDEX.md, SKILL_INDEX.md, SLASH_COMMANDS.md, command indexes, prompt indexes, arsenal indexes, and Codex semantic indexes through their owners. Do not hand-edit generated registries.

7. Do not create an /idea-to-culture-loop hot command, a global ~/.codex mirror, or a plugin.

This route keeps the new capability reachable without adding 13 more top-level skill packages.

## Adjacent-Owner Boundaries

1. **attention-hijack-hooks** owns live signal discovery and source capture.
2. **lulu-cheng-meservey-communications** owns current lifecycle and dated trajectory support.
3. **kieran-flanagan-content-engine and content-ops** own storage, queue state, publication operations, and performance analysis.
4. **dan-koe-multipassionate-mastery** owns cross-domain recombination.
5. **oren-taste-development** owns formal taste training and critique vocabulary.
6. **tim-danilov-niche-bending and sky-tan-format-engine** own format transfer and testing.
7. **dan-wang-literary-analysis and Susan Orlean** can deepen analytical or braided prose.
8. **ocean-vuong-perceptual-writing or high-taste-writing-os** owns deep placeful line repair.
9. **Lara Acosta and Diandra Escobar** own platform-native structure and distribution format.
10. **how-i-write-os and /shaan-story-deploy** remain the conductors for multi-expert composition and story dosage.

No adjacent-owner file changes in this build.

## Preservation Lock

The current content hashes are:

1. Workflow 01: f463ef256342190636c596978fd2fa46167e0ffef1857e3a75bbef7191596096.

2. Workflow 02: 7effa159c024b88affc6996e7ec1639d9dec324a8092c113e1e0ce97053fa281.

3. Workflow 03: 9df79ae52579549db78e307e5e04325ef1651a00c993693b75fb0e63c174de85.

4. Prompt 01: 2b9f0d8eab5aa523b3174960b1517b20fad8ff6287fa3addba82a86d368033e5.

5. Prompt 02: 22a0b6af89e5ca92e4b562f4ee433abc65d0ebb53048872d8eaaafd1113f9ca8.

6. Prompt 03: ae44225c0877c5b06c1f890f700677b8b1605bfe16d2517233399f9ca21f0c5a.

Allowed differences are narrow:

1. Workflow and prompt 01 may change only the stale assumption, add the triage pre-flight, and wire the prompt.

2. Workflow and prompt 02 may add only the source-cited jargon trial, the 60-20-10 boundary, and prompt wiring.

3. Workflow 03 may add prompt wiring and a route note. Prompt 03 remains byte-identical.

4. The existing POP evidence labels cannot be upgraded.

5. New mechanics must cite QsHm_0MEhX8 and preserve Nathan or third-party attribution.

6. Media operations, guest acquisition, taste curricula, signal research, format testing, and platform production cannot enter the skill.

Any broader difference fails the preservation verifier.

## Held-Out Behavioral Fixtures

1. **Empty viral ambition.** A user wants reach without supplying a real idea. Required result: IDEA route or HOLD, never a manufactured hot take.

2. **Strong but safe.** A supported thesis is repeatedly softened. Required result: COURAGE route and a human decision, never invented controversy.

3. **Strong idea, poor draft.** Thesis and conviction are clear, but prose is stiff. Required result: CRAFT route into the preserved POP system.

4. **Mixed deficits.** Several problems appear at once. Required result: one primary bottleneck with evidence and sequenced secondary support.

5. **Genuine current.** A dated event fits an evergreen idea. Required result: current-fit pass, core lock, expiry, shell set, and evergreen fallback.

6. **Fake current.** An unsupported celebrity or news claim is supplied. Required result: HOLD and a request for evidence.

7. **Brand mismatch.** A real current has no payload or reputation fit. Required result: reject the frame despite attention potential.

8. **Expired current.** A previously useful event has passed. Required result: EXPIRED CURRENT and evergreen fallback.

9. **Placeful with evidence.** Exact place and lived details are supplied. Required result: use only those details.

10. **Placefulness cosplay.** One biographical fact is supplied. Required result: sparse truth or evidence request, with no invented texture.

11. **POP provenance trap.** The evaluator asks what this interview taught about POP. Required result: it did not teach POP; route to the older evidence lane.

12. **Speaker attribution trap.** Nathan supplies an example and David agrees. Required result: separate authorship.

13. **Mechanical braid.** Past and present alternate but reveal nothing. Required result: reject the structure and require a meaningful contrast.

14. **Viral but wrong audience.** Reach is high without target-reader or business effect. Required result: separate reach, audience fit, conversion, and revenue.

15. **Soul conflict.** A real current contradicts the creator's stated mission. Required result: preserve the mission and decline or reframe the current.

16. **Visual deictic claim.** The transcript references an object that was not captured visually. Required result: mark visual properties unavailable.

17. **Observation versus reps.** Private notes exist but nothing was published. Mind-Mine may run; Public Reps must return NO EVENT.

18. **Current-fit versus shell.** A bad current must stop at workflow 08. A valid current may proceed to workflow 09, whose output must be a materially different frame artifact.

## Verification Plan

### Structural and Content Checks

1. Run validate_skill.py for david-perell-writing and clear the current missing genius-patterns critical finding.

2. Run skill_auditor.py and preserve the current 7-of-7 baseline.

3. Run the workflow contract validator across all 13 workflows.

4. Run the prompt renaissance audit with zero failures.

5. Build the prompt library and wire the SKILL.md prompt section.

6. Generate wrappers, registries, and indexes, then run strict menu and Codex surface audits.

7. Run export-format, JSON, diff, and prose checks on the new artifacts.

### Behavioral Checks

1. Create a standard-library verifier under extractions/david-perell-nathan-barry-2026/verify_idea_to_culture_build.py.

2. Execute all eighteen held-out fixtures from references/fixtures_v1.json.

3. Verify preservation hashes and allowed differences for the three existing workflows and prompts.

4. Verify no adjacent-owner file changed.

5. Verify that no current-dependent output can run without a source date and expiry.

6. Verify that NO EVENT, NO PERMISSION, HOLD, EXPIRED CURRENT, and UNTESTED EFFECT remain distinct.

### Recognition and Blind-Pass Debt

The skill has no two-piece David Perell reference corpus suitable for the forge blind-pass requirement. Before Checkpoint 3, collect at least two real published Perell writing pieces with provenance and freeze them before generating test outputs.

Until a side-by-side recognition judgment is recorded, the expanded system cannot receive A-tier promotion even if every structural and behavioral check passes.

## Build Sequence After Approval

1. Freeze the six protected files and write the preservation lock.
2. Add the source references, claims ledger, rubric, fixtures, and implementation schemas.
3. Patch the three existing workflows only within the allowed differences.
4. Write the ten new workflows and ten matching born-v2 prompts.
5. Update SKILL.md, genius.md, AGENT.md, and the dated source ledger.
6. Run prompt audits before any registration.
7. Generate wrappers and registries through their owners.
8. Run the eighteen fixtures, structural checks, and preservation verifier.
9. Acquire and freeze the two-piece reference corpus.
10. Return at Checkpoint 3 with sample outputs, structural proof, fixture results, and the unresolved recognition judgment.

## Proof State at This Checkpoint

**Source verified.** Transcript identity, speaker labels, timestamps, hashes, and the source mechanics behind all ten additions.

**Architecture specified.** Exact workflows, files, routes, handoffs, safeguards, fixtures, and generators.

**Build untested.** No new workflow or prompt exists in the production skill.

**Runtime unobserved.** No fixture or cold-start execution has run against the proposed system.

**Market unobserved.** No content was published and no audience, buyer, conversion, sales, or revenue event occurred.

**No permission used.** No external write, registry mutation, global skill promotion, outreach, or publishing occurred.

## Checkpoint Decision

**Recommended approval:** Approve Architecture.

That authorizes the local Phase 5 build, prompt forging, project-local registration, and deterministic verification inside this isolated worktree. It does not authorize global mirrors, external publishing, outreach, or market claims.

To change the plan before any build, respond with: Adjust Architecture: followed by the specific change.
