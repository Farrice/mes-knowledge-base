# PROVENANCE — luke-iha-copy-blocks repair (Frontier Wave 3 PoC, 2026-07-17)

Every anchor added or entity added during this repair pass, with exact file + section it cites. Cross-reference `references/source-ledger.md` for the VERIFIED/LIKELY/UNCONFIRMED classification of each source file.

## `genius.md` — Anti-Pattern anchors (target: `anti_patterns_sourced`)

1. **"Sequential blocks" anti-pattern** → `extractions/luke-iha/video-4-copy-blocks/extraction-report.md`, section "## 4. Hidden Knowledge", item "### HK4: Copy Blocks Aren't Sequential". Verbatim: "Beginners use blocks in order: Pain → Promise → Proof → CTA. Experts interleave them: Pain → Curiosity → Promise → Pain (new angle) → Proof → Curiosity → Constraint → Promise (new angle) → Proof → CTA."

2. **"Challenging identity/values head-on" anti-pattern** → `extractions/luke-iha/video-8-proof-ladder/extraction-report.md`, section "## Genius Patterns", item "### 3. Belief Hardening & Backward Dissolution". Verbatim: "Once something becomes part of identity (e.g., 'I'm not the kind of person who…'), it's nearly impervious to data... Dissolution must work backward — start by attacking observations with counterexamples, then experiences."

3. **"Claim bigger than proof" anti-pattern** → `extractions/luke-iha/video-8-proof-ladder/extraction-report.md`, section "## Genius Patterns", item "### 4. The Proof Balance Scale", "Executable Behavior" line. Verbatim: "Never let the claim side outweigh the proof side."

4. **"Over-proofing" anti-pattern** → `extractions/luke-iha/extraction-report.md` (root), section "## Hidden Knowledge", item "**Proof is About Safety, Not Convincing**". Verbatim: "The core purpose of proof isn't to bludgeon the prospect into agreement. It's to make them feel *safe* taking the leap."

## `genius.md` — Named-entity floor fixes (target: `named_entity_floor`)

5. **Canyon / Helicopter Metaphor section** — added provenance-note flagging the metaphor itself as UNCONFIRMED (no transcript on file for the Director's Cut source), while anchoring the adjacent dollar figure to `extractions/luke-iha/video-8-proof-ladder/extraction-report.md`, "## Content Assessment" line: "Expert: Luke Iha — Direct Response Copywriter ($100M+ generated)."

6. **Decision Framework section** — cross-referenced the skill's own already-stated `$10–20k/mo` identity-ceiling figure (genius.md, "## Promise — the Promise Ladder..." section, "Identity Runway" bullet) rather than introducing a new unsourced number. Internal self-consistency, not a new external claim.

7. **Quality Rubric section** — anchored to `skills/luke-iha-copy-blocks/references/quality-rubric.md`, table header row confirming a 1–10 scale with named anchors at Score 4 / Score 7 / Score 10.

8. **"Patterns from claude.ai export — Collaborative Copywriting & Marketing Maestro" intro** — cross-referenced the file's own Evolution Log entry dated 2026-07-01 ("Extract-Amplify Add-To"), and explicitly flagged the claude.ai-export source itself as outside this pass's ground-truth scope (UNCONFIRMED, see source-ledger.md).

9. **Evolution Log section intro** — added a factual count/date-span ("4 entries below span 2026-04-09 to 2026-07-01") verifiable by reading the four `###` subsections immediately below it in the same file.

10. **"2026-04-09 — Belief-State Sequencing" subsection** — added "(on the skill's 1–10 rubric scale, see Quality Rubric above)" — internal cross-reference to fix #7, not a new claim.

## `workflows/cash-method-generator.md` — Output Schema (target: `workflow_contracts`)

11. Renamed `## PHASE 7: MATRIX OUTPUT` → `## PHASE 7: OUTPUT FORMAT (CASH Matrix)`. Content of the phase (the matrix skeleton, multiplication summary, priority testing order) is unchanged — only the heading text was touched, to match house style (`## OUTPUT FORMAT` appears in all other 13 workflow files in this skill) and satisfy the auditor's Output Schema/Format/Requirements pattern.

## `genius.md` — Model Calibration section (task item, not a failing check)

12. Renamed `## How to Use This Skill (Opus Calibration)` → `## How to Use This Skill (Model Calibration)`, added two new paragraphs ("This expert's texture," "Polish is the tell") modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16. Texture claims anchored to:
    - "Jargon Flurry" mechanic → `extractions/luke-iha/video-1-proof-mechanisms/extraction-report.md`, "## Genius Patterns" → "### The Jargon Flurry (existing — enhanced)" (cross-refs the fuller definition in the root `extraction-report.md`, "### The Jargon Flurry (Strategic Complexity)").
    - "This is the number one thing" delivery-style quote → `extractions/luke-iha-creative-strategist/transcript.txt`, opening lines (read directly; this transcript is the raw source behind video-8-proof-ladder's extraction-report.md).

## `SKILL.md`

13. Added one line to the "References (load on-demand)" list pointing to the new `references/source-ledger.md`. No other change.

---

**Judgment call flagged for review**: item #12 renames the existing calibration section rather than adding a second, near-duplicate "How to Use This Skill" header, since the worker envelope's instruction ("ADD... a section modeled on ben-watkins") would otherwise produce two H2 headers with nearly identical content under different names in the same file — worse for the skill than one upgraded section. See `REPAIR-NOTES.md`.
