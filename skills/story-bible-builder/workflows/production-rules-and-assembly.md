---
name: "Production Rules and Bible Assembly"
slug: "production-rules-and-assembly"
produces: "Bible sections 11–12 plus the final assembled, installable SKILL.md file"
skill: "story-bible-builder"
load_context: "genius.md"
---

# Story Bible Builder — Production Rules and Bible Assembly

## Role
You are running Build-Flow Steps 6–7 of Story Bible Builder — the final workflow in the build sequence, run only after the spine/world, all characters, and ensemble/engines are locked. This workflow closes the interview and compiles every prior section into one installable canon file.

## Input Required
1. All prior locked sections (1–10) from the Spine and World Build, Character Deep-Dive, and Ensemble and Engines workflows.
2. The user's hard-earned prompt/canon/naming rules from their own prior work (Step 6 question).
3. Which production-companion skills the user runs alongside this bible (e.g. `cinema-worldbuilder-pro`), so the closing section names them explicitly (`SKILL.md`, line 164).

## Workflow

### Step 1 — Production rules (section 11)
Ask: "What are the rules you've hard-earned about your own work? The stuff that only works in a specific way. Prompt rules, naming rules, canon lock rules, aesthetic rules that can't be broken." (`SKILL.md`, line 138). Bake in four defaults unless the user overrides them: no character names in image/video/music prompts, every prompt standalone, code-block output with no aspect ratio in the prompt body, locked physical traits restated verbatim in every prompt (`SKILL.md`, lines 141–144). Copy the user's own phrasing verbatim where they've already articulated a rule (`SKILL.md`, line 146).

### Step 2 — Assembly and "when this skill is active" (section 12)
Compile sections 1–11 into the final structure. Write the closing section to instruct future Claude for **both** usage modes (`SKILL.md`, lines 152–164):
- Standalone mode: pull relevant context per request, stay inside canon, never invent conflicting detail, use quoted descriptors verbatim.
- Paired-with-director-skill mode: name the companion skill(s) explicitly; map character voice → Sound Bed, movement/stillness → Subject Lock, aesthetic era → World Plate/grade, production rules → cross-frame rules and locked traits.

### Step 3 — Ship
Assemble the full file with YAML frontmatter (`name:` + a pushy `description:`) and the complete canon body, staying under 500 lines (`SKILL.md`, line 20). Save to `projects/<project>/bible/[working-title-slug].md` (or `_active/<client>/bible/` for client worlds) — never to a sandbox path (`SKILL.md`, line 166; historical install defect corrected, see `genius.md` anti-patterns). Offer to zip it as an installable `.skill` file (`SKILL.md`, line 168).

## Output Schema

The delivered turn contains, in order:
1. **Section 11 — Production rules**, bulleted, with the four baked defaults present unless explicitly overridden, and any user-specific rules quoted in their own words.
2. **Section 12 — "When this skill is active,"** split into the two named subsections (Standalone mode / Paired-with-director-skill mode) with any named companion skills called out.
3. **The full assembled bible** as one fenced markdown block with YAML frontmatter, ready to save at the specified path.
4. **A one-line save-path confirmation and zip offer.**

## Quality Gate

1. **All four baked production-rule defaults present** unless the user explicitly overrode one — and any override is stated, not silently dropped.
2. **Both usage modes are named in section 12**, not just the standalone case.
3. **Any active companion skill is named explicitly** in the paired-mode subsection — never left as a generic "a director skill."
4. **Save path is a repo path**, never `/mnt/user-data/outputs/` or any other sandbox path.
5. **Final file stays under 500 lines** and is one dense file, never split into modular sub-files (`SKILL.md`, line 20).
6. **Stranger test applied to the whole assembled bible**, not just individual sections — could a stranger write any scene in this world using only this file? (`references/example-bible-excerpts.md`, line 113).
