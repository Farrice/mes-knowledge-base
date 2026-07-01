# Workflow 01 — Evaluation-Driven Development + Token-Optimization Pass

> Net-new capability folded in from the claude.ai "Skill Architect" export. The base skill-creator process (Steps 1-6 in SKILL.md) tells you *how* to build a skill; this workflow adds two rigor gates the base process leaves informal: (a) measure the skill against explicit evaluations BEFORE and AFTER writing it, and (b) run a deterministic optimization pass before packaging. Run this AROUND the base process — evals in Step 1, optimization pass just before Step 5 (Packaging).

## Role

You are building a skill the way Anthropic's own skill authors do: evals first, measured baseline, minimal instructions to close the gap, then a ruthless token/QA sweep. You do not guess whether a skill is good — you measure it against cases you wrote before you started, then cut every token that did not earn its place.

## Input

- The skill being created or edited (its intended domain and 3-5 concrete usage examples from base Step 1).
- Access to run the base skill-creator scripts (`scripts/init_skill.py`, `scripts/package_skill.py`, `scripts/quick_validate.py`).

## Workflow Phases

### Phase A — Author evaluations BEFORE writing docs (pairs with base Step 1)

Do this *before* drafting SKILL.md body, not after.

1. Write 3-5 **evaluation scenarios**, each a concrete `input -> expected output/behavior` pair, not a vague usage example. Include at least one edge case that reveals robustness (ambiguous trigger, missing input, wrong file type).
2. Establish the **baseline gap**: mentally (or in a scratch run) walk a skill-less Claude through each scenario. Note specifically what it would get wrong, re-derive every time, or ask for repeatedly. That delta is the only thing the skill must fix — everything else is bloat.
3. Convert each gap into a success criterion. If a scenario has no gap (Claude already handles it fine unaided), delete it — it is not justification for skill content.

### Phase B — Write minimal instructions to pass (during base Step 4)

1. Draft ONLY the instructions/resources needed to close the measured gaps from Phase A. Resist adding "nice to know" context.
2. For each paragraph you write, name which eval scenario it makes pass. A paragraph that maps to no scenario is a candidate for deletion or a reference file.
3. Prefer a `scripts/` file over prose whenever a gap is "Claude rewrites the same code / makes the same inconsistent choice" — deterministic gaps get deterministic fixes.

### Phase C — Optimization + QA pass (run just before base Step 5 Packaging)

Run this sweep as a checklist; each item is a concrete edit, not a vibe:

**Token optimization**
1. Delete any explanation of a concept Claude already knows (question every paragraph: "Does Claude really need this?" — default no).
2. Tighten filler phrasing ("in order to" -> "to", "make use of" -> "use", "at this point in time" -> "now").
3. Enforce ONE term per concept throughout — never alternate synonyms (e.g. pick "reference file" and never also say "doc"/"guide" for the same thing).
4. Confirm SKILL.md body is under ~500 lines; if not, push variant/advanced detail into `references/` (progressive disclosure) rather than trimming meaning.

**Description quality (the highest-leverage field)**
5. Verify the `description` states both WHAT the skill does and WHEN to use it (concrete trigger terms a user would actually say).
6. Third-person, no first-person voice ("Analyzes..." not "I analyze...").

**Security**
7. No hardcoded credentials, API keys, or secrets anywhere in the skill.
8. All file paths use forward slashes.
9. Bundled scripts validate their input and fail loudly.

### Phase D — Re-measure and iterate (pairs with base Step 6)

1. Re-run the Phase A evaluation scenarios against the finished skill. Each expected output should now be reached.
2. Any scenario that still fails: identify the single missing instruction or resource, add only that, re-run. Iterate on measured misses, never on speculation.
3. Watch for **missed invocations** (skill should have triggered but did not) — that is almost always a `description` trigger-term gap, not a body gap.

## Output Contract

Deliver, alongside the packaged skill:

- The 3-5 evaluation scenarios (input -> expected) used to gate the build, with each mapped to the gap it closes.
- A one-line note per skipped/deleted candidate scenario (why it was cut — usually "no baseline gap").
- Confirmation the Phase C checklist ran (token sweep done, description WHAT+WHEN present, security clean).

## Quality Gate

Do not package if any of these are true:

- A SKILL.md paragraph exists that maps to no evaluation scenario or measured gap (bloat — cut or move to `references/`).
- The `description` lacks concrete trigger terms, or is written in first person.
- Any hardcoded secret, backslash path, or unvalidated-input script remains.
- A Phase A scenario still fails against the finished skill and no follow-up iteration was run.

If all four are clean and `scripts/package_skill.py` validates, the skill is deployment-ready.
