# /verticalize — Genius Context

Load this before running the skill. SKILL.md is the phase map; this is the reasoning underneath it — why the sequence is sequence, why Phase 2.5 cannot bend, and what a rushed vertical bootstrap actually looks like when it's failing quietly. Everything below is grounded in the skill's own workflow contract (`.agent/workflows/verticalize.md`), the resolver code that routes into it (`execution/intent_to_package.py:_resolve_vertical_bootstrap`, class 10, shipped 2026-05-25), `execution/ground_truth.py:init_domain`, and two named-failure feedback cards this skill was built to prevent from recurring.

---

## How to Use This Skill (Model Calibration)

The 8 phases are sequencing logic, not a script to narrate. Internalize *why* Phase 2.5 sits where it sits, then run the bootstrap — never recite "Phase 0 complete, advancing to Phase 1" into anything the founder actually reads. If a delivered ICP master or voice document contains a sentence explaining its own phase number, the compression discipline already failed: the founder should read `02-icp-master.md` and feel like it was always true, not like they're reading minutes from an orchestration meeting.

Specifically:

- **Do NOT let phase mechanics leak into the delivered artifacts.** "Generated in Phase 1 per the vertical bootstrap protocol" belongs in `_working/phase-0-capture.md`, never in `projects/<slug>/00-foundation/02-icp-master.md`. The five deliverables listed under "Critical outputs" are read by five different future consumers (a copywriter, a designer, the founder's own memory six months out) — none of them should be able to tell the doc came out of an orchestrated pass rather than a bespoke two-week build.
- **Do NOT treat Phase 2.5 as a checkpoint you narrate past.** It is a HALT, not a status update — the workflow file is explicit: `"Do not auto-advance. Wait for explicit user signal."` If you find yourself writing "the user would likely approve this" instead of actually stopping, you have converted a gate into a rubber stamp, which `directives/workflow-gate-convention.md` (2026-05-12) names directly as worse than no gate at all, because it trains the click-through habit.
- **The recognition test**: would someone who has personally run a vertical bootstrap by hand — ICP interviews, a voice document drafted against real samples, five ground-truth pieces argued over one at a time, a week of back-and-forth — recognize this as that same rigor compressed into one sequential session, or as a fast, confident package that skipped the parts that require someone's actual judgment? If a run produces zero PROPOSED-but-unconfirmed items, zero founder pushback, and a same-session PASS on all 5 ground-truth samples, that is not evidence of a clean vertical — per the 2026-04-11 naming failure below, it is usually evidence the rigor didn't fire.
- **Polish in the wrong place is the tell.** A vertical package that reads too smoothly — an ICP with no flagged cultural-connotation risk, a voice doc where every worked example landed on the first draft, a Phase 2.5 gate answered "yes" in one line with no follow-up question — is more likely rubber-stamped than actually calibrated. The naming sprint that produced "Lake Effect" and "Thaw" for a Chicago brand carried a 9.3/10 confidence score and zero internal doubt; the failure wasn't visible in the process, only in the output a lived Chicagoan actually read.
- **This skill's texture is orchestration discipline, not creative authorship.** /verticalize doesn't write the ICP, the voice doc, or the samples — it composes `/icp-deep-dive`, `/voice-document`, `/extract`, and `ground_truth.py init-domain` in the right order with the right gate between them. If a run "produces" a voice document without actually invoking `/voice-document`, or "seeds" ground truth without a real user PASS on each of the 5 samples, the composition has been faked, not executed.

---

## Why Phase 2.5 is structurally non-skippable

`skills/verticalize/SKILL.md` states the reasoning directly: skipping the gate means "the new vertical's calibration anchor IS the auto-seed — and from day one, the quality gate has nothing to push back against." This is not a verticalize-specific worry; it's the general finding behind `feedback_auto-evolution-cant-substitute-for-ground-truth.md`, dated 2026-05-03:

> "In subjective-domain AI systems (content, brand, voice, copy, taste), auto-improvement loops cannot self-validate... if Farrice's taste isn't captured as ground truth, the system averages toward the model's own preferences and calls that 9/10."

The 2026-04-24 audit that produced that card found 94-99% of finalize traces scoring 8+ before the rubric was calibrated — a system fully capable of grading itself as excellent while actually drifting. A new vertical bootstrapped through `/verticalize` inherits that exact risk at the moment of creation: five auto-generated "PASS" samples with no human eyes on them isn't a calibrated domain, it's a domain calibrated to its own model's taste. The gate exists to put a real human judgment between "the system produced this" and "this is now the standard the domain gets graded against forever."

**The one legitimate exit**: `--skip-2.5` is reserved for domains the user is "already deeply expert in (lived experience)." Per `directives/workflow-gate-convention.md`'s skip-syntax rule, this flag "must be passed explicitly — not inferred" — a fast-moving, impatient tone in the conversation is not consent to skip the gate. Only the literal flag is.

---

## Why the gate asks about cultural connotation specifically

Phase 2.5's third question — "Are there cultural / lived-experience claims that need validation by someone with that experience BEFORE we generate ground-truth?" — is not a generic diversity checkbox. It is a direct response to a named, dated failure:

> "A naming sprint for Andrea's Chicago event brand produced 'Lake Effect' (8.6 score) and 'Thaw' (8.8 score) — both associated with winter misery by every Chicagoan... Farrice (30-year Chicago resident) rated them 2/10. The gap between system confidence and actual quality was the most damaging part — worse than a bad name is a bad name presented as a great one."

That 2026-04-11 incident produced a durable rule that Phase 2.5 operationalizes for every future vertical: "If the user has lived in the target geography, ASK THEM before presenting." A vertical whose ICP or voice document rests on a geographically- or culturally-specific claim (a neighborhood's connotation, a subculture's in-group language, a regional idiom) cannot pass Phase 2.5 on process-adherence alone — the specific question about lived-experience validation has to get a real answer, not a skip.

---

## Why the skip flag for Phase 4 (routing) is different from the skip flag for Phase 2.5

Phase 4 (routing bindings) is proposal-only by design — the workflow file is explicit that the skill must "Surface the diff to the user for approval. Do NOT auto-edit `routing_enforcer.py` — this is a system-config file." This is a *harder* rule than Phase 2.5's: there is no skip flag for it at all, because `routing_enforcer.py` is shared infrastructure every other vertical routes through. A bad ICP only damages the new vertical; a bad auto-edit to `BINDINGS` can silently misroute an unrelated, already-calibrated domain. Composing atoms is the whole point of this skill (per its own "Why this skill exists" framing: 234 skills + 134 agents outgrew manual orchestration) — but composing them into a shared config file without a human diff-review inverts the benefit into a system-wide risk.

---

## Why the 5-sample floor and the sequential-only rule aren't arbitrary

`execution/ground_truth.py:init_domain` validates the slug (`^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$`, lowercase alphanumeric + hyphens, no leading/trailing dash) and registers the domain with zero pre-loaded samples — "verticalize fills this," per the function's own docstring. Nothing about the registration itself enforces quality; the enforcement lives entirely in Phase 3's stop condition: "If fewer than 5 samples reach user-approved PASS, halt." Four approved samples is not "almost there" — it's an under-seeded domain whose quality gate, per the same 2026-05-03 finding above, will calibrate against noise instead of taste.

The sequential-only constraint (no bootstrapping 5+ verticals in parallel) follows from the same logic, not from a throughput limit: "Each vertical bootstrap is sequential because Phase 2.5 user-validation is per-vertical." A gate that exists to force one human's real attention cannot be batched without becoming exactly the rubber stamp it was built to prevent — five simultaneous Phase 2.5 halts competing for one person's judgment produces skimmed answers, not five calibrated verticals.

---

## Why the child CLAUDE.md is an inheritance contract, not a brand archive

Phase 5 produces `projects/<slug>/CLAUDE.md` against a fixed 6-section template (inheritance declaration, one-paragraph brand identity, voice test, when-to-load-context table, override list, anti-patterns) — the same shape already proven across `_active/clients/andrea-dj/CLAUDE.md`, `_active/clients/jen-listings/CLAUDE.md`, and `_active/farrice-brand/CLAUDE.md`. SKILL.md's own anti-pattern warning is specific: "Don't duplicate brand bibles in the per-project CLAUDE.md. Point to the brand context files." A child CLAUDE.md that pastes the full ICP and voice doc into itself instead of pointing at `00-foundation/02-icp-master.md` and `03-voice-document.md` breaks the moment either source file amends — now there are two copies to keep in sync, and inheritance contracts that require manual double-maintenance stop getting maintained.

---

## Anti-Patterns — Sourced (SKILL.md's own rules + the failures that produced them)

- **Skipping Phase 2.5 because the founder is moving fast** — SKILL.md's Anti-pattern #1 states plainly: "Even when the user is fast-moving and impatient, the calibration cost of un-validated ground truth is permanent," a rule written directly against the 2026-05-03 finding that ungrounded auto-improvement "drifts toward grade inflation without human calibration."
- **Auto-editing `execution/routing_enforcer.py` instead of surfacing the diff** — SKILL.md's Anti-pattern #2: "Don't auto-edit `routing_enforcer.py`. Phase 4 proposes; the user applies. System-config files require manual gating," restated in `.agent/workflows/verticalize.md` Phase 4 as "Do NOT auto-edit `routing_enforcer.py` — this is a system-config file."
- **Shipping a vertical with fewer than 5 PASS-marked ground-truth samples** — SKILL.md's Anti-pattern #3, enforced mechanically at Phase 3's stop condition: "If fewer than 5 samples reach user-approved PASS, halt. Don't ship a vertical with under-calibrated ground-truth."
- **Duplicating the brand bible's content inside the per-project CLAUDE.md instead of pointing to it** — SKILL.md's Anti-pattern #4, which names the failure mode directly: a child CLAUDE.md that becomes "the brand archive" instead of "the inheritance contract."
- **Running `/verticalize` in parallel across 5+ verticals** — SKILL.md's Anti-pattern #5, restated in the workflow file's "What This Workflow Does NOT Do" section: "Does NOT support 'verticalize at scale' (5+ verticals in parallel) in v1. Each vertical bootstrap is sequential because Phase 2.5 user-validation is per-vertical."
- **Answering the Phase 2.5 halt question with a rubber-stamp "looks good, proceed"** — named directly in `directives/workflow-gate-convention.md` (2026-05-12): "Anti-pattern: rubber-stamp gates ('Looks good, proceed?') with no structured halt path. These train Claude and the user to auto-click yes, defeating the gate."
- **Inferring `--skip-2.5` from conversational urgency instead of requiring the literal flag** — per the workflow-gate-convention's skip-syntax rule cited in `.agent/workflows/verticalize.md` Phase 2.5: "the skip flag must be passed explicitly — not inferred."
- **Presenting a vertical package with high confidence and zero flagged uncertainty as evidence of a clean build** — the exact inversion the 2026-04-11 naming failure documented: a "9.3/10 quality gate pass" on names later rated "2/10" by someone with lived experience of the geography, because "confidence must track output quality, not process adherence."
- **Skipping the lived-experience validation question when the vertical touches a specific geography or subculture** — the same 2026-04-11 card's core rule: "NEVER present names for a geographically-rooted brand without validating cultural connotation with someone who has lived experience in the target geography," which is the literal wording behind Phase 2.5's third gate question.

---

## Recognition Test

A run of this skill should feel like the compressed version of a real week-long bootstrap, not a faster version of skipping it. Would a builder who has actually done vertical setup the slow way — sat through ICP interviews, argued over five ground-truth pieces one at a time, waited for a founder to actually read a voice doc before shipping anything downstream — recognize this as the same discipline run in one session, or as a fast package wearing the vocabulary of ICP/voice/ground-truth without any of the judgment calls that make those words mean something? If every phase auto-advanced, if the Phase 2.5 gate got a one-word yes with no follow-up, if all 5 samples reached PASS on the first draft — that reads as the second thing, not the first.

---

## v1 Status and Open Gaps (Named, Not Hidden)

Per SKILL.md's own "v1 status" note, this skill shipped 2026-05-25 as part of Phase C of the Universal Autopilot plan, and "the first real end-to-end run against a fake 'AI-for-construction consulting' vertical happens in a follow-on session." As of this repair pass, `knowledge/expert-benchmarks/_registered_domains.json` is an empty object (`{}`) — no vertical has ever actually been bootstrapped through this skill in production. Every phase description in this file and in SKILL.md is grounded in the workflow contract as *written*, not in a completed real-world run. The plan file the SKILL.md cites as its origin (`i-think-the-biggest-virtual-emerson.md`) is not present on disk at the referenced path — treat that specific citation as UNCONFIRMED (see `references/source-ledger.md`), not as a live pointer.
