# Expert Assembly OS — Genius Context

> Load this before running `/assemble` or `/panel-sync`. This is not an extraction of an
> external human expert — there is no `extractions/` folder for this skill (verified via
> `ls extractions/ | grep -i assembl`, zero matches). The "genius" here is Farrice's own
> claude.ai creation: the hybrid-panel system he calls the Virtuoso / "GENIUS-LEVEL EXPERT
> ASSEMBLY SYSTEM," rebuilt production-grade in two commits — `26adc893f` (2026-07-15,
> "Expert Assembly OS Phase 0–3: hybrid casting + bespoke personas + roadmap synthesis +
> routing integration") and `9c8c4d098` (2026-07-15, "Grounded Forge + Mastery Floor").
> Every pattern below traces to `references/lineage.md`, `references/persona-synthesis-
> prompt.md`, `references/roadmap-schema.md`, `docs/solutions/2026-07-15-expert-assembly-
> os-hybrid-casting.md`, or the user's own memory note `project_expert-assembly-os.md`.

---

## How to Use This Skill (Model Calibration)

These are casting and synthesis primitives, not a checklist to narrate. If the output
reads "Phase 1: Scope. Phase 2: Cast. Phase 3: Forge..." spelled out to Farrice, the
machinery has leaked — run the phases, never announce them by name in the deliverable.

The test: would Farrice recognize this as *his own Virtuoso panel* — the one that ran
~29 conversations across domains as different as maritime rigging and spiritual
retreats and never once needed a real human expert to already exist for the topic — or
would it read as a generic multi-agent council wearing "expert panel" vocabulary? If
it's the second, the fix is never a prose polish; it's regenerating the Composition
Ledger and the Forks until the disagreement is real.

Specifically:
- Do NOT let `[Bespoke Composite]` be a badge slapped on a thin paragraph. It only
  earns the label with full McClain depth — backstory, worldview, contradictions,
  messy detail — per `SKILL.md`: "Composite label explicit; authority from
  specificity, not numbers."
- Do NOT let a Mastery Floor failure disappear quietly into a normal-looking seat.
  See the Step G4 rule quoted below — it exists because silence is the failure mode,
  not the stat itself.
- Do NOT write a roadmap move as "improve engagement." The whole point of the
  Requirement 3 fix (`lineage.md`) was killing that exact sentence shape.
- Polish is the tell in a very specific way on this skill: personas that read too
  smooth, too resume-perfect, are the precise failure the Mastery Floor was built to
  catch. `"Led initiatives that generated $47M"` is banned not because it's false
  but because it *feels* like credibility — real composite authority comes from a
  named, slightly awkward, specific methodology (e.g. "the Preference Paradox
  Protocol"), never from a clean number.
- Do NOT skip the Grounding pass (Phase 4) on the theory that the panel "already
  knows" the domain. The 2026-07-15 Grounded Forge commit exists precisely because
  latent-only synthesis was ruled insufficient for bespoke seats.

---

## The Core Engine: Coverage-Aware Casting, Not Roster-Only

The system never returns an empty panel and never fakes credentials to fill a gap.
`execution/panel_cast.py` scores each required domain against the 227-card roster and
classifies it **STRONG** (≥2 keyword hits + ≥50% ratio), **THIN** (≥1 hit, lower ratio),
or **ABSENT** (no matches). Strong domains seat an extracted roster expert directly.
Thin and absent domains get a bespoke composite — never an empty seat, never a forced
mismatch.

Five governor slots structure every panel regardless of domain: **Spine, Mechanism,
Differentiator, Craft, Risk Gate** — plus Farrice, always seated as **Function Owner**,
never an afterthought bolted onto the end. This is the mechanism that let the sailing-
rigging test case (zero roster coverage — 3 bespoke composites: mechanical engineer,
aerodynamicist, materials scientist) and the LinkedIn test case (full roster coverage —
Tommy Clark, Ross McKay + one thin-domain composite) run through the *same* casting
logic and both produce a coherent 5-seat panel.

The 8-phase workflow (`Scope → Cast → Forge → Ground → Diverge → Deliberate →
Synthesize → Close`) is not decorative sequencing — Forge is gated by
`persona_stat_lint.py` (blocks $/%/real-company fabrication, 2-retry regenerate then
strip-to-methodology-only fallback), and as of the 2026-07-15 Grounded Forge upgrade,
Forge additionally runs 4 hybrid research queries per bespoke slot *before* synthesis
and writes a receipt sidecar (≥3 source URLs) that a separate adversarial verifier
checks for CURRENT vs. STALE before the persona is allowed to speak in Diverge.

---

## Anti-Patterns (Sourced)

- **Fabricated persona credentials** — synthesizing "Led the growth team at McKinsey" or "$47M generated" to sound authoritative; locked 2026-07-15 in `persona-synthesis-prompt.md` ("NO Fabricated Statistics," "NO Real Company Names in Credentials") and `docs/solutions/2026-07-15-expert-assembly-os-hybrid-casting.md` Key Decision #2, "No fake stats... authority from specificity not numbers."
- **Latent-only bespoke personas** — synthesizing a composite from model intuition alone, no live research pass; closed by commit `9c8c4d098` (2026-07-15, "Grounded Forge + Mastery Floor"), per `project_expert-assembly-os.md`: "Latent-only personas are no longer acceptable for bespoke seats."
- **Silent Mastery Floor failure** — seating a STALE or UNSUPPORTED persona without flagging it; `persona-synthesis-prompt.md` Step G4 (2026-07-15, binding): "Floor fails after retry → seat with `[MASTERY FLAG: <reason>]` beside the panelist in every output, so confidence is never silently borrowed."
- **Unlabeled panel composition** — presenting roster and bespoke seats without distinguishing them; `roadmap-schema.md` Labeling Rule: "All synthetic panelists explicitly marked `[Bespoke Composite]`. Real extracted experts marked `[Roster]`. No ambiguity."
- **Vague roadmap moves** — writing "improve X" instead of an observable target; `lineage.md` Requirement 3, fix landed in the 2026-07-15 rebuild (commit `26adc893f`): "'Improve X' became 'X reaches Y by DATE.'"
- **Pinning Opus as a hard-coded conductor** — locking the panel to one model tier instead of routing per `orchestration-doctrine.md`; `docs/solutions/2026-07-15-expert-assembly-os-hybrid-casting.md` Key Decision #5: "Never pin Opus: Conductor = strongest available model; Sonnet executes."
- **Treating `/assemble` as a rebuild target** — respinning `panel_cast.py` or the workflow engine from scratch instead of extending it; `project_expert-assembly-os.md` (2026-07-15 memory note): "Extend, never rebuild. Known open edges: keyword coverage scoring is crude; /panel-sync reload not yet E2E-tested."

---

## Verbatim Exemplars (Source-Grounded)

> "Floor fails after retry → seat with `[MASTERY FLAG: <reason>]` beside the
> panelist in every output, so confidence is never silently borrowed."
— `references/persona-synthesis-prompt.md`, GROUNDED FORGE Step G4

> "All synthetic panelists explicitly marked `[Bespoke Composite]`. Real extracted
> experts marked `[Roster]`. No ambiguity."
— `references/roadmap-schema.md`, Labeling Rule

> "Composite label explicit; authority from specificity, not numbers."
— `SKILL.md`, Composite Personas

> "Latent-only personas are no longer acceptable for bespoke seats."
— `project_expert-assembly-os.md` (user memory note, 2026-07-15; LIKELY — a
memory observation, not a primary source file, see source-ledger.md)

---

## Recognition Test

Would Farrice recognize this as his own claude.ai Virtuoso panel — the one that
survived ~29 conversations across wildly different domains without ever needing a
pre-existing human expert on the roster — or would it read as a generic AI "here are
some perspectives" council wearing expert-panel vocabulary? The honest tell: does
every bespoke seat carry a receipt (`<persona>.receipt.md`, ≥3 URLs) it could survive
`persona_stat_lint.py` and an adversarial mastery-verify pass on first try, does every
roadmap move carry an owner and a date instead of "improve X," and does Farrice sit as
Function Owner rather than a closing footnote? If any of those three are missing, it
is not this system's output — rebuild the Cast and Forge phases, not the prose.
