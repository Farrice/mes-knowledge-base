# PROVENANCE — fantastic-posters repair (Wave 3 Lane 4 Batch 5)

Anchor → source file + location. Every quote below was verified by direct file read before use; none were invented. `fantastic-posters` is a tool skill (generator + workflow docs), not a person-extraction — so all grounding is internal repo documentation and code, not an external transcript/interview corpus (none exists for this skill; `extractions/` has no fantastic-posters-adjacent source, confirmed via `ls extractions/ | grep -iE "poster|fal|fantastic"` → no match).

| # | Anchor (in genius.md Anti-Patterns) | Claim | Source | Location | Status |
|---|---|---|---|---|---|
| 1 | Item 1 — "Keyword-template brain" | "a strong pair of hands... bolted to a thin brain (`pickStyle()` keyword-matches one template; `--n` nudges 'shift colour accent')" | `skills/fantastic-posters/genius.md` (self — the file's own v1→v2 diagnosis, dated "v2 'Studio' elevation, 2026-07-04" in the file header) | Header + line 8 of the pre-repair file | VERIFIED (read verbatim, quoted verbatim) |
| 2 | Item 7 — "Verbose ref prompts" | "the shortest prompt that names ONLY what changes outperforms verbose specs... Verbose specs make the model drift." | `skills/fantastic-posters/.claude/skills/fantastic-posters/SKILL.md` | "Trust the Reference" section, ~lines 180-182 | VERIFIED (read verbatim, quoted verbatim) |
| 3 | Item 8 — "Auto-firing paid gen" | "Root cause of the 2026-05→07 fal-usage.json staleness: fal_budget_guard.py logging was AI-memory-dependent (a human/agent had to remember to run it after each call)." | `skills/fantastic-posters/generate.js` | Lines 40-41 (code comment) | VERIFIED (read verbatim, quoted verbatim) |
| 4 | Item 9 — "Title > ~6 words" | "GPT Image 2 is the strongest text-rendering model around — titles, billing blocks, masthead lockups all hold up. If a title runs more than ~6 words, expect typos; shorten and re-run." | `skills/fantastic-posters/README.md` | "Settings" section, ~line 150 | VERIFIED (read verbatim, quoted verbatim; same claim also appears independently in SKILL.md "Rules" section, cross-confirming) |

## Non-quote additions (no external claim — self-derived, no provenance risk)

| Addition | Basis | Status |
|---|---|---|
| genius.md "How to Use This Skill (Model Calibration)" section | Original synthesis calibrated to this skill's own documented mechanics (Satori/router/critique-loop language already in genius.md), modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per ENVELOPE instruction — not a factual claim about a person, so no VERIFIED/LIKELY/UNCONFIRMED label applies | N/A — original craft writing |
| Workflow `## Quality Gate` sections (01-08) | Each checklist is a direct distillation of that same workflow file's own pre-existing "Output Requirements" completeness criteria and "Execution" gates — no new external claims, only restructured into the checklist format `00-studio.md` (the already-passing sibling) established | VERIFIED (self-derived from the same file being edited) |
| Workflow `## Output Schema` + `## Quality Gate` sections (deliverable-cover.md, kling-multishot.md, mybpm-products.md, poster-to-video.md, seedance-cinematic.md) | Each schema/gate distills that file's own pre-existing "Standard Run," "Cost Envelope"/"Cost Reference," and "Anti-Patterns" sections into a named record + checklist — no new cost figures, flags, or claims invented; all dollar amounts and flags reused verbatim from the same file | VERIFIED (self-derived from the same file being edited) |

## UNCONFIRMED

None. Every quoted claim above traces to a file+line I read directly in this session. No claim in the repair carries an UNCONFIRMED label because no claim required external (non-repo) sourcing — this is a tool skill's own documentation being made internally consistent, not a person's biography or public-record claims.
