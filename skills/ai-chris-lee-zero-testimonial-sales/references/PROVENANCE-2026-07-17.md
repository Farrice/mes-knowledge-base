# PROVENANCE — ai-chris-lee-zero-testimonial-sales repair

Anchor → source file+location table. Full claim-by-claim detail lives in
`references/source-ledger.md`; this is the compact index.

| Anchor (new/changed content) | Points to | Status |
|---|---|---|
| "How to Use This Skill (Model Calibration)" section, `genius.md` | Structural model: `skills/ben-watkins-storytelling/genius.md` lines 7-16 (read in full). Content (numbers, texture) drawn from this skill's own pre-existing Patterns 9/10 and Exemplars. | Structure borrowed per envelope instruction; content UNCONFIRMED at the external level (see below). |
| Recognition-test sentence ("would AI Chris Lee recognize this as theirs... or using zero-testimonial-sales vocabulary") | Same section, house-authored this repair | Craft-guidance language, not a factual claim — no label required. |
| Anti-Patterns (Sourced) — 6 bullets, `genius.md` | Each bullet anchors to a pre-existing Genius Pattern / Signature Move / Quality Rubric row already in `genius.md` (Patterns 4, 5, 7, 9, 10, 13 and the Anti-Exemplar) | Internal anchor VERIFIED (text is present in the file); external anchor to a real AI Chris Lee recording UNCONFIRMED — no transcript exists in this repo. |
| `references/source-ledger.md` (new file) | `extractions/` repo-wide search (empty), `skills/ai-chris-lee-zero-testimonial-sales/genius.md` (12,679 bytes), `references/genius-patterns.md` (3,211 bytes), `SKILL.md.old` (3,318 bytes), `agents/ai-chris-lee/AGENT.md` (2,807 bytes), codex-harvest duplicate (3,522 bytes), unrelated research file `ai_chris_lee.md` (4,744 bytes) — all sizes via `wc -c` this session | All sizes independently verified this session, not carried forward from memory. |

## Absence Verification (the check that matters most)

Claim: "No `extractions/` source exists for this expert." Verified by:

```bash
ls extractions/ | grep -i "chris.lee\|chris-lee\|chrislee\|zero-test\|testimonial"
# → empty, exit 1
grep -rli "chris lee" --include="*.md" . | grep -v "^./skills/ai-chris-lee-zero-testimonial-sales"
# → 20+ hits, all downstream references (routing indexes, the codex-harvest
#   duplicate skill, one unrelated research file) — none are a primary
#   transcript/interview/video source
```

No file was assumed absent without being searched for and, where found,
opened and read (not just listed).

## What Was NOT Touched

`SKILL.md`, `SKILL.md.old`, all `references/prompts*/` files, all
`references/_legacy-prompts/` files, and all 4 `workflows/*.md` files were
already passing their respective checks (`verbatim_exemplars`,
`named_entity_floor`, `workflow_contracts`) and were left byte-for-byte
unchanged. Only `genius.md` (additive edit) and the new
`references/source-ledger.md` were produced.
