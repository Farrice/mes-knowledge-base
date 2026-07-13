export const meta = {
  name: 'forge-wave',
  description: 'Forge born-v2 execution prompts for one wave of prompt-less skills (scout reads forge-input.json, one Sonnet agent per skill)',
  phases: [
    { title: 'Scout', detail: 'read forge-input.json skill list' },
    { title: 'Forge', detail: 'one Sonnet effort-high agent per skill', model: 'sonnet' },
  ],
}

const REPO = '/Users/farricecain/Google Antigravity'
const INPUT = REPO + '/_active/prompt-wiring-os-2026-07-13/forge-input.json'
const DATE = '2026-07-13'

const SCOUT_SCHEMA = {
  type: 'object',
  properties: {
    total_skills: { type: 'integer' },
    remaining_after_wave: { type: 'integer' },
    skills: { type: 'array', items: { type: 'string' } },
  },
  required: ['total_skills', 'remaining_after_wave', 'skills'],
}

const REPORT_SCHEMA = {
  type: 'object',
  properties: {
    skill: { type: 'string' },
    forged: { type: 'integer', description: 'count of born-v2 prompt files written' },
    deliverables: { type: 'array', items: { type: 'string' }, description: 'deliverable each prompt covers' },
    fidelity_low: { type: 'array', items: { type: 'string' }, description: 'v2 paths flagged fidelity: low' },
    summary: { type: 'string', description: '1-3 sentences: what the prompts cover, what was too thin to forge' },
  },
  required: ['skill', 'forged', 'deliverables', 'fidelity_low', 'summary'],
}

function forgePrompt(skill) {
  return `You are forging BORN-V2 execution prompts for a skill that has none. Repo root: ${REPO}
Spec (binding): ${REPO}/directives/prompt-forging-spec.md — read it FIRST, follow it exactly.

YOUR SKILL: "${skill}"

Steps:
1. Read ${INPUT}, find your skill's entry in "skills" (matching "skill" == "${skill}"): it lists skill_md, genius_md (may be null), workflows, and existing_v2_failing (delete-and-replace any listed there).
2. Read the skill's SKILL.md fully, genius.md fully if present, and every workflow file listed. This extracted material is your ONLY source — forging from training memory about the expert is prohibited (that is how generic 5/10 output happens).
3. Derive the skill's DISTINCT DELIVERABLES (typically 4-10) from its workflows and SKILL.md. Several workflows sharing one deliverable shape = one prompt.
4. For each deliverable, Write one born-v2 prompt to ${REPO}/skills/${skill}/references/prompts-v2/<deliverable-slug>.md with EXACTLY this frontmatter (unquoted values):
---
name: "<Expert> — <Deliverable>"
source_prompt: born-v2
skill: ${skill}
standard: structure-pure-v2
forged: born-v2
refactored: ${DATE}
---
Body sections (all required unless noted): Role & Activation (expert's real frame, ONLY credentials corroborated by the skill's own material) · Input Required ([BRACKET] architecture) · Execution Protocol (the skill's ACTUAL methodology for this deliverable at full depth — steps, decision rules, named frameworks, verbatim exemplar fragments where the material has them) · "## Output Contract" (exact components, format, length bounds) · "## Output Skeleton" (code-fenced pure-placeholder shape; generative-prose deliverables may carry prose INSTRUCTIONS, never sample copy) · "## Quality Gate" (3-6 checkable yes/no criteria) · Creative Latitude (REQUIRED for creative deliverables: name exactly where to push beyond the skeleton — angles, voice, unexpected connections, taste calls) · Deploy When.

HIGH FLOOR, UNLIMITED CEILING (binding): the contract makes shape/completeness/honesty deterministic; it must NEVER constrain word choice, argument, angle, or creative leaps beyond what the expert's methodology demands. Quality Gate items check floor violations only — never "followed the template." A prompt that reads like a fill-in-the-blanks form has FAILED even if structurally compliant.

FIDELITY RULE: never invent methodology to fill gaps. Thin material → forge FEWER, deeper prompts; if a forged prompt is still thin, add "fidelity: low" to its frontmatter and list it in your report. A skill with 3 honest prompts beats 12 padded ones. Zero fabricated statistics, invented clients, or unverifiable credibility claims anywhere.

HARD RULES: write ONLY into skills/${skill}/references/prompts-v2/ (create the dir). NEVER edit SKILL.md, genius.md, workflows, originals, or registries — central wiring happens after your wave. Return the structured report; keep summary to 1-3 sentences.`
}

phase('Scout')
const scout = await agent(
  `Read the file ${INPUT} (JSON). Return exactly: total_skills (its "total_skills" field), remaining_after_wave (its "remaining_after_wave" field), and skills — the "skill" string of each element in its "skills" array, in order. No other work.`,
  { label: 'scout:forge-input', phase: 'Scout', schema: SCOUT_SCHEMA }
)
if (!scout || !scout.skills || !scout.skills.length) throw new Error('scout failed to read forge-input.json')

phase('Forge')
log(`Forge wave: ${scout.skills.length} skills, ${scout.remaining_after_wave} remaining after`)

const reports = await parallel(scout.skills.map(s => () =>
  agent(forgePrompt(s), {
    label: `forge:${s}`,
    phase: 'Forge',
    model: 'sonnet',
    effort: 'high',
    schema: REPORT_SCHEMA,
  })
))

const ok = reports.filter(Boolean)
const totals = {
  skills_reported: ok.length,
  skills_expected: scout.skills.length,
  forged: ok.reduce((s, r) => s + r.forged, 0),
  fidelity_low: ok.flatMap(r => r.fidelity_low),
  reports: ok,
}
log(`Forge wave done: ${totals.forged} prompts forged across ${totals.skills_reported} skills, ${totals.fidelity_low.length} fidelity-low`)
return totals
