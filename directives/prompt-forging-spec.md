# Prompt Forging Spec — Born-v2 Execution Prompts (2026-07-13, Farrice-approved wiring project)

> Every skill ships with its execution layer. An extraction that produces SKILL.md + genius.md +
> workflows but no prompts is HALF-FINISHED: the model gets the expert's thinking but must improvise
> the output shape every time — that improvisation is where run-to-run degradation lives.
> This spec makes deterministic practitioner prompts a NON-OPTIONAL phase of every extraction.

## What a forged prompt is

A **structure-pure v2 prompt, born v2** (no fabrication era, nothing to strip later), one per
distinct deliverable the skill produces. File: `skills/<skill>/references/prompts-v2/<slug>.md`.

Frontmatter (exactly, unquoted values; `forged: born-v2` distinguishes these from
renaissance-refactored files whose `source_prompt` points at a legacy original):

```yaml
---
name: "<Expert> — <Deliverable>"
source_prompt: born-v2
skill: <skill-slug>
standard: structure-pure-v2
forged: born-v2
refactored: <date>
---
```

Required body sections (same standard as the Renaissance, audit-enforced):

1. **Role & Activation** — the expert's real frame; ONLY credentials corroborated by genius.md /
   SKILL.md / reference corpus. No invented stats, no "virtuoso" padding.
2. **Input Required** — `[BRACKET]` architecture for everything the prompt needs.
3. **Execution Protocol** — the skill's ACTUAL methodology for this deliverable (steps, decision
   rules, named frameworks) lifted from SKILL.md/genius.md/workflows at full depth. Never thinned,
   never invented. Verbatim exemplars from the corpus are gold — cite, don't fabricate.
4. **## Output Contract** — exact deliverable components, format, length bounds.
5. **## Output Skeleton** — code-fenced SHAPE specimen, placeholders/one-line descriptors only.
   (Exception: generative-prose prompts may carry prose *instructions* in the skeleton — never
   sample copy presented as output.)
6. **## Quality Gate** — 3-6 checkable yes/no criteria distilled from what the expert would check.
7. **Creative Latitude** (required for creative deliverables; optional for pure diagnostics) —
   names exactly where the model should push beyond the skeleton: angles, voice, unexpected
   connections, taste calls. This section is load-bearing, not decoration.
8. **Deploy When** — trigger scenarios.

**HIGH FLOOR, UNLIMITED CEILING (Farrice 2026-07-13, binding design principle):** the Output
Contract and Skeleton are a FLOOR — they make the deliverable's shape, completeness, and honesty
deterministic so no run ever comes back malformed, padded, or fabricated. They must NEVER cap the
ceiling: no prompt may constrain word choice, argument, angle, or creative leaps beyond what the
expert's own methodology demands. Quality Gate items check for floor violations (missing
components, fabrication, genericism) — never for "followed the template exactly." A v2 prompt that
reads like a fill-in-the-blanks form has failed this spec even if it passes the audit; a v2 prompt
that produces remarkable, surprising work inside a reliable shape is the standard.

**FIDELITY RULE (unchanged):** never invent methodology to fill gaps. Thin source → forge fewer,
deeper prompts and/or mark `fidelity: low` and report it. A skill with 3 honest prompts beats one
with 12 padded ones.

## How many prompts per skill

One per **distinct deliverable** the skill actually produces — derived from its workflows and
SKILL.md "produces/outputs" sections. Typical range 4-10. A workflow whose output is itself a
process (audits, diagnostics) counts as a deliverable. Do NOT force one-per-workflow when several
workflows share one deliverable shape.

## Wiring (the part that was missing — prompts nothing loads don't exist)

After forging, ALL of:
1. `python3 execution/renaissance_audit.py` → must report 0 fail (gate; `--delete` + refix on failures).
2. `python3 execution/prompt_library.py build` → index (feeds the load-time menu hook + facade).
3. `python3 execution/wire_prompt_pointers.py --write` → refreshes the skill's
   `<!-- BEGIN:execution-prompts -->` section in SKILL.md.
4. Each skill workflow that produces a deliverable gets one line under its output step:
   `Execution prompt: references/prompts-v2/<file>.md — honor its Output Contract.`

The load-time injection (`execution/hooks/prompt_menu_hook.py`, PostToolUse on SKILL.md reads)
then surfaces the menu automatically — no manual step at use time.

## Where this fires

- **/extract** — Step 5.5 (after skill generation, before agent files).
- **/extract-forge** — Phase 5.5 (after Build, before Registration).
- **Backfill** — `execution/forge_queue.py` + the renaissance wave machinery for pre-existing
  prompt-less skills (one Sonnet effort-high agent per skill; Fable orchestrates, gates, commits).
- **Lazy safety net** — the menu hook flags any prompt-less skill at load time so gaps are visible,
  never silent.

## Provenance guard

Born-v2 prompts are forged FROM the skill's own extracted material (SKILL.md, genius.md,
workflows, reference corpus). Forging from training memory about the expert is prohibited —
that's how generic 5/10 skills happen (see docs/solutions/2026-07-07-transcript-only-extraction-
generic-output.md). If the skill's material can't support a deliverable's protocol, that prompt
is not forged.
