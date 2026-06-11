# Phase 2: Example Backfill — Top 5 Skills

## The Situation

- **651 workflows total** across all skills
- **3** have Output Schema (Cimorelli only)  
- **478** have `Output Contract` (free-form text — upgrade target)
- **15** have any `Example Output` (12 are Connelly, 2 Cimorelli, 1 Darrel Wilson)
- **595** have Quality Gate (good shape already)

Full backfill of 651 workflows is a multi-session project. Phase 2 does the **5 highest-impact skills first** to establish the pattern and prove it works.

## Scoping Decision

> [!IMPORTANT]
> We are NOT upgrading every workflow in every skill. The rule from the `/extract` pipeline:
> - **Every workflow MUST get Output Schema** (YAML block)
> - **At least 2 workflows per skill MUST get Example Output**
> - Diagnostic/reactive workflows may skip examples

**Per skill**: Upgrade ALL workflows with Output Schema. Add Example Output to the **2-3 most-used workflows**.

## Target Selection & Order

| # | Skill | Workflows | Work Type | Why This One |
|---|-------|-----------|-----------|-------------|
| 1 | michael-connelly-vivid-writing | 12 | Schema-only (already has examples) | Lowest risk — validates schema pattern |
| 2 | donald-miller-storybrand | 8 | Schema + examples on 2-3 | Smallest full-backfill — proves the pattern |
| 3 | steven-pressfield-narrative-mastery | 15 | Schema + examples on 3 | Highest workflow count — stress tests at scale |
| 4 | luke-iha-proof-ladder | 13 | Schema + examples on 2-3 | Different domain (copywriting) |
| 5 | kallaway-word-mastery | 13 | Schema + examples on 2-3 | Different domain (content psychology) |

## Verification Protocol (Per Skill)

After upgrading each skill:

1. **Structural check**: Every workflow has `## Output Schema` with YAML block
2. **Example check**: 2-3 workflows have `## Example Output` with scenario + result + annotation  
3. **Integrity check**: Existing content (Workflow, Quality Gate) is **unchanged** — no regressions
4. **Quality check**: One example is read in full to confirm it teaches by showing

**Gate**: Each skill must pass all 4 checks before moving to the next.

## Approach

For Output Schemas — convert existing `Output Contract` text into structured YAML that defines the deliverable's components. Keep the same information, just structure it.

For Example Outputs — invent realistic scenarios that show the framework in action. Partial but representative. Annotated with "What makes this excellent."

## What This Does NOT Touch

- Workflow content (Role, Execution phases, Quality Gate) — untouched
- genius.md files — untouched  
- SKILL.md files — untouched
- Agent files — untouched
