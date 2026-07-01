# skill-creator — genius layer

Advanced patterns that sharpen the base skill-creator process. The base SKILL.md tells you the mechanics of building a skill; this layer adds the rigor gates that separate a merely-functional skill from a top-1% one. Load when you want measured quality, not just a structurally-valid package.

---

### Patterns from claude.ai export — Skill Architect project

Net-new against the base skill-creator process (which covers progressive disclosure, references vs assets vs scripts, and the anti-bloat "does Claude need this?" heuristic — do NOT re-import those). These add the two rigor gates the base process leaves informal: evaluation-first development and a deterministic optimization pass. See `workflows/01-evaluation-driven-token-optimization.md` for the runnable sequence.

**Evaluation-first, not example-first**
- Execute: Before writing any SKILL.md body, author 3-5 `input -> expected output` evaluation scenarios (not usage examples) including one robustness edge case; then walk a skill-less Claude through each to establish the baseline gap. Build ONLY what closes a measured gap. Re-run the same scenarios against the finished skill and iterate on real misses.
- Success Metric: Every SKILL.md paragraph maps to a specific evaluation scenario or measured gap; scenarios with no baseline gap were deleted, not documented; the finished skill passes all retained scenarios.

**Ruthless token-optimization sweep (pre-package gate)**
- Execute: Just before packaging, run a concrete checklist — cut concepts Claude already knows, tighten filler ("in order to" -> "to"), enforce one term per concept (no synonym-drift), keep body under ~500 lines by pushing advanced detail to `references/`.
- Success Metric: No paragraph survives that fails "does Claude really need this?"; terminology is consistent skill-wide; body is under the line ceiling without loss of meaning.

**Description = the highest-leverage field**
- Execute: Verify the `description` states both WHAT the skill does AND WHEN to use it with concrete trigger terms a user would actually type, written in third person ("Analyzes..." not "I analyze..."). Treat a missed invocation (should have triggered, did not) as a description trigger-term gap, not a body gap.
- Success Metric: A fresh Claude invokes the skill on the intended prompts without an explicit "use skill X" instruction.

**Security audit before ship**
- Execute: Sweep for hardcoded credentials/keys/secrets (none allowed), forward-slash-only file paths, and scripts that validate their input and fail loudly.
- Success Metric: Zero secrets in the package, no backslash paths, every bundled script rejects malformed input rather than producing silent garbage.

**Deliberately NOT imported from the source** (already covered or explicitly banned by base skill-creator): README.md / CHANGELOG.md / QUICK_REFERENCE templates (base skill-creator explicitly forbids these as clutter — never add them), progressive-disclosure architecture, the references/assets/scripts taxonomy, and the core "concise is key" heuristic.
