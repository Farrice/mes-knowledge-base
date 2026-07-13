# Design Skill Enshrine

> Convert a perfected design workflow into a permanent, one-command reusable SKILL — Jack Roberts' Step 5 that turns discovery into infrastructure.

## Context Required
- **Load First**: `genius.md` — Step 5 (Enshrine) and Codify-Once-Replicate-Infinitely pattern

## Inputs
- **Required**: A completed, refined design that the user is satisfied with
- **Required**: The DESIGN.md used to create it
- **Required**: The iteration log showing what feedback was given
- **Required**: The format type (website, presentation, graphic, report, etc.)

## Workflow

### Step 1: Design Decision Archaeology

Before enshrining, extract every decision that produced the final quality:

1. **Explicit rules** (from the DESIGN.md):
   - Color palette and assignments
   - Typography scale and families
   - Spacing system and grid
   - Component specifications

2. **Implicit rules** (from the iteration log):
   - What feedback was given during refinement?
   - What patterns were rejected? ("I don't like X. Let's never have that.")
   - What structural conventions emerged? (logo placement, slide count, section order)
   - What content density rules applied? (max 6 lines per slide, etc.)

3. **Research rules** (from the generation process):
   - What research was done before creation?
   - What sub-agent verification was used?
   - What sources were required?

4. **Integration rules** (from the tools used):
   - Which MCP tools/connectors were essential?
   - What brand extraction was done?
   - What image generation settings produced the best results?

### Step 2: Skill Architecture

Structure the enshrined skill:

```markdown
# [Format] Design Skill: [Name]

## Quick Deploy
> [One-sentence description of what this produces]
> Usage: "Create a [format] about [topic] for [audience]"

## Required Inputs
- [Input 1]: [What and why]
- [Input 2]: [What and why]

## Design System (Frozen)
[Embed the complete DESIGN.md inline — this is the immutable design law]

## Production Rules
### Content Rules
- [Rule 1 from iteration log]
- [Rule 2 from iteration log]
- [Rule N]

### Structural Rules  
- [Layout conventions]
- [Section/slide ordering]
- [Required elements: logo placement, navigation, footer, etc.]

### Quality Rules
- [Anti-Slop requirements]
- [Minimum quality thresholds]
- [The specific things that must NEVER appear]

### Tool Requirements
- [Required integrations: Firecrawl, Kia API, etc.]
- [Research requirements: sub-agent fact-checking, etc.]
- [Image generation: model, style, parameters]

## Execution Process
1. [Step-by-step production process]
2. [In the exact order that produces the best results]
3. [Including the refinement loop]

## Anti-Slop Checklist (Mandatory Pre-Delivery)
□ [Check 1]
□ [Check 2]
□ [Check N]

## Example Output
[Reference to the original perfected design as the quality benchmark]
```

### Step 3: Skill Validation

Test the enshrined skill by generating a NEW design using it:

1. Give the skill a different topic/content than the original
2. Generate the output using ONLY the enshrined skill instructions
3. Compare the new output against the original quality benchmark

**Validation criteria:**
- Does the new output match the quality of the original?
- Does it still look brand-consistent?
- Did the production rules prevent any slop from appearing?
- Is the process truly one-command, or does it need manual intervention?

If the new output is ≥90% as good as the original → the skill is ready.
If not → identify what's missing from the skill and add it.

### Step 4: Skill Registration

Save the enshrined skill:

1. Create a new skill directory: `skills/[format]-[brand-or-style]/`
2. Write the `SKILL.md` with the complete enshrined instructions
3. Copy the DESIGN.md into the skill's `references/` directory
4. Store the original exemplar output as a benchmark
5. Register the skill in the system's workflow index

### Step 5: Usage Documentation

Create a quick-start guide:

```markdown
## How to Use This Skill

### One-Command Deploy
"Create a [format] about [topic] using the [skill-name] design skill"

### With Customization
"Create a [format] about [topic] using the [skill-name] design skill, 
but adjust [specific element] to [change]"

### With Brand Override
"Create a [format] in [client-brand] style, using [skill-name] as the
structural template but extracting brand colors from [client-url]"
```

## Output
- Enshrined SKILL.md (complete, self-contained)
- DESIGN.md frozen in skill's references directory
- Quality benchmark (original exemplar output)
- Quick-start usage guide
- Validation test results

---

## Prompt Forging Gate (MANDATORY since 2026-07-13 — spec: `directives/prompt-forging-spec.md`)

Any skill this workflow creates, converts, or enriches ships with its execution layer — no exceptions:
1. **Born-v2 prompts**: one structure-pure v2 prompt per distinct deliverable (typically 4-10) in `skills/<skill>/references/prompts-v2/` — Role & Activation (real credentials only), Input Required, Execution Protocol at full depth FROM THE EXTRACTED MATERIAL (never training memory), Output Contract, Output Skeleton (placeholders only), Quality Gate, Creative Latitude where creative, Deploy When. Fidelity rule: thin source → fewer/deeper prompts, flag `fidelity: low`, never invent.
2. **Wire (all four)**: `python3 execution/renaissance_audit.py` (0 fail) → `python3 execution/prompt_library.py build` → `python3 execution/wire_prompt_pointers.py --write` → `Execution prompt:` cross-ref line under each workflow's output step.

A skill without prompts is half-finished work — do not register or close out without this gate passing. The load-time menu hook (`execution/hooks/prompt_menu_hook.py`) flags violations at every future load.
