export const meta = {
  name: 'strike-native',
  description: 'Wave-4 pilot: the /strike mission pattern (2-4 expert sub-agents on one multi-faceted task) as a NATIVE Workflow-engine script, run head-to-head against the prose-orchestrated JCC strike (swarm-orchestrator agent / /strike -> collective-genius-council.workflow.js mode=strike). Brief -> parallel Strike -> Synthesize-with-dissent. See .tmp/wave4-strike-pilot/COMPARISON-PLAN.md for the judging protocol.',
  phases: [
    { title: 'Brief', detail: 'one cheap agent turns mission+focus into per-expert task briefs (schema-forced)', model: 'sonnet' },
    { title: 'Strike', detail: 'parallel — one agent per expert, loads its OWN SKILL.md+genius.md, returns take + labeled claims + gaps', model: 'sonnet' },
    { title: 'Synthesize', detail: 'merge takes into the named deliverable, PRESERVE dissent, carry claim labels through unchanged, write to disk' },
  ],
}

// ── args ─────────────────────────────────────────────────────────────────
// { mission: str, experts: [{name, skillPath, focus}], synthesis: str (what the final deliverable is) }
let _A = args
if (typeof _A === 'string') { try { _A = JSON.parse(_A) } catch (e) { _A = {} } }
const MISSION = (_A && _A.mission) || ''
const EXPERTS = (_A && _A.experts) || []
const SYNTHESIS = (_A && _A.synthesis) || 'a single decision-grade deliverable that compounds every expert take'
const ROOT = '/Users/farricecain/Google Antigravity'

if (!MISSION) throw new Error('strike-native requires args.mission')
if (!EXPERTS.length || EXPERTS.some((e) => !e.name || !e.skillPath || !e.focus)) {
  throw new Error('strike-native requires args.experts: [{name, skillPath, focus}, ...] (2-4 entries)')
}
if (EXPERTS.length < 2 || EXPERTS.length > 4) {
  // Strike is defined as 2-4 experts (directives/orchestration-doctrine.md Pattern Table).
  // Outside that band the right tool is /convene (wide) or a fleet, not this script — fail
  // loud rather than silently degrade into a different pattern.
  throw new Error(`strike-native is for 2-4 experts (got ${EXPERTS.length}) — use /convene --mode wide for more voices`)
}

const SLUG = MISSION.toLowerCase().replace(/[^a-z0-9]+/g, '-').slice(0, 48).replace(/^-+|-+$/g, '')
const OUT_DIR = `${ROOT}/.tmp/strike-native/${SLUG}`

// ── Schemas ──────────────────────────────────────────────────────────────
// NOTE — mission_validator.py integration point (built in parallel, may not exist yet on this
// branch): that validator consumes a stage-payload schema keyed roughly on
// {quarantine_root, protected_tree_clean, gaps}. This script does not import or call it — but
// every stage below is shaped to be payload-compatible on first contact:
//   - quarantine_root: every artifact this run writes lives under OUT_DIR (nothing touches the
//     protected tree outside .tmp/strike-native/<slug>/), so protected_tree_clean is true by
//     construction, not by self-report.
//   - gaps: each Strike agent surfaces its own `gaps[]`; Synthesize carries them up unresolved
//     rather than papering over them, so the validator (once wired) has a real gaps[] to check
//     instead of an empty placeholder.
const CLAIM_SCHEMA = {
  type: 'object',
  required: ['text', 'label'],
  properties: {
    text: { type: 'string' },
    label: { type: 'string', enum: ['VERIFIED', 'LIKELY', 'UNCONFIRMED'] },
    source: { type: ['string', 'null'], description: 'primary source if VERIFIED/LIKELY, else null' },
  },
}
const BRIEF_SCHEMA = {
  type: 'object',
  required: ['briefs'],
  properties: {
    briefs: {
      type: 'array',
      items: {
        type: 'object',
        required: ['name', 'task_brief'],
        properties: {
          name: { type: 'string' },
          task_brief: { type: 'string', description: 'what THIS expert, working only their focus, must produce' },
          key_questions: { type: 'array', items: { type: 'string' } },
        },
      },
    },
  },
}
const STRIKE_SCHEMA = {
  type: 'object',
  required: ['name', 'take', 'claims', 'gaps', 'take_path'],
  properties: {
    name: { type: 'string' },
    take: { type: 'string' },
    claims: { type: 'array', items: CLAIM_SCHEMA },
    gaps: { type: 'array', items: { type: 'string' }, description: 'what this expert could NOT answer from their focus alone' },
    take_path: { type: 'string', description: 'file this agent actually wrote {name,take,claims,gaps} to — the real path, not a self-report' },
  },
}
const SYNTH_SCHEMA = {
  type: 'object',
  required: ['deliverable_path', 'dissents', 'claims'],
  properties: {
    deliverable_path: { type: 'string', description: 'the real path the deliverable was written to' },
    dissents: {
      type: 'array',
      description: 'genuine load-bearing disagreements between experts — NEVER averaged away',
      items: {
        type: 'object',
        required: ['tension', 'positions'],
        properties: {
          tension: { type: 'string' },
          positions: {
            type: 'array',
            items: { type: 'object', properties: { expert: { type: 'string' }, position: { type: 'string' } } },
          },
        },
      },
    },
    claims: { type: 'array', items: CLAIM_SCHEMA, description: 'merged claim list — labels carried through UNCHANGED, never upgraded' },
    gaps: { type: 'array', items: { type: 'string' }, description: 'unresolved gaps carried up from the experts' },
  },
}

// ── Brief ────────────────────────────────────────────────────────────────
phase('Brief')
const briefPlan = await agent(
  `Mission: ${MISSION}\n\nExperts on this strike (name — their assigned focus):\n${EXPERTS.map((e) => `- ${e.name}: ${e.focus}`).join('\n')}\n\n` +
    `For EACH expert, write a tight task brief: what THIS expert, working ONLY their assigned focus, must produce to serve the mission — plus 1-3 key_questions their take must answer. You are briefing, not doing the work; do not write any expert's take yourself.\n` +
    `Return JSON {briefs:[{name, task_brief, key_questions}]} — one entry per expert, names must match exactly.`,
  { label: 'brief', phase: 'Brief', schema: BRIEF_SCHEMA, model: 'sonnet', effort: 'low' }
)
const briefs = (briefPlan && briefPlan.briefs) || []
const briefFor = (name) => (briefs.find((b) => (b.name || '').toLowerCase() === name.toLowerCase()) || {}).task_brief || `Serve the mission from your focus: ${name}`
log(`Briefed ${briefs.length}/${EXPERTS.length} experts`)

// ── Strike (parallel, one agent per expert) ─────────────────────────────
phase('Strike')
function strikePrompt(e) {
  const slug = e.name.toLowerCase().replace(/[^a-z0-9]+/g, '-')
  const takePath = `${OUT_DIR}/experts/${slug}.json`
  return (
    `You are **${e.name}**, striking on: ${MISSION}\nYour focus: ${e.focus}\nYour brief: ${briefFor(e.name)}\n\n` +
    `STEP 1 — LOAD YOUR OWN EXPERTISE (non-negotiable — never answer generically from training memory when the skill exists): read ${ROOT}/${e.skillPath}/SKILL.md fully, and ${ROOT}/${e.skillPath}/genius.md if it exists. Think and write as this expert's actual methodology, not a generic take.\n` +
    `STEP 2 — produce YOUR take on the mission, from your focus only. Do not try to cover the whole mission; that is the synthesizer's job.\n` +
    `STEP 3 — CLAIM DISCIPLINE: every factual claim (real people/events/dates, statistics, technical facts, market claims, source attributions) gets a label — VERIFIED (you checked a primary source), LIKELY (plausible, unverified), or UNCONFIRMED (asserted, no grounding). Never state a claim with no label. List genuine gaps — what you could not answer from your focus alone; do not fabricate to fill them.\n` +
    `STEP 4 — write your take to ${takePath} (create dirs) as JSON {name, take, claims, gaps}.\n` +
    `Return JSON {name, take, claims, gaps, take_path} where take_path is the exact path you just wrote (${takePath}).`
  )
}
const strikes = await parallel(
  EXPERTS.map((e) => () => agent(strikePrompt(e), { label: `strike:${e.name}`, phase: 'Strike', schema: STRIKE_SCHEMA, model: 'sonnet', effort: 'high' }))
)
const takes = strikes.filter(Boolean)
log(`Strike: ${takes.length}/${EXPERTS.length} experts returned takes`)
if (takes.length < 2) throw new Error(`Strike phase yielded ${takes.length} valid take(s) — need >=2 for a synthesis worth preserving dissent over`)
const perExpertPaths = takes.map((t) => ({ name: t.name, path: t.take_path }))
const allGaps = takes.flatMap((t) => (t.gaps || []).map((g) => `${t.name}: ${g}`))

// ── Synthesize (single agent, compound not average, preserve dissent) ────
phase('Synthesize')
const deliverablePath = `${OUT_DIR}/deliverable.md`
const synth = await agent(
  `Synthesize this strike into ${SYNTHESIS} for mission: ${MISSION}\n\n` +
    `Expert takes (read each fully — do not skim):\n${takes
      .map((t) => `### ${t.name}\nTake: ${t.take}\nClaims: ${JSON.stringify(t.claims)}\nGaps: ${(t.gaps || []).join('; ') || 'none'}`)
      .join('\n\n')}\n\n` +
    `HARD RULES:\n` +
    `1. COMPOUND, don't average — identify each expert's load-bearing contribution and combine those; a synthesis that reads as a comparison grid or that blunts every expert's sharpest point has failed.\n` +
    `2. PRESERVE DISSENT — where two experts genuinely disagree at a load-bearing point, surface it as a named tension with both positions stated. Never silently pick a winner or smooth it into consensus language.\n` +
    `3. CARRY CLAIM LABELS THROUGH UNCHANGED — VERIFIED/LIKELY/UNCONFIRMED per claim, exactly as each expert labeled it. Never upgrade a claim's confidence during synthesis; that is where fabrication creeps in.\n` +
    `4. Write the full deliverable to ${deliverablePath} (create dirs).\n\n` +
    `Return JSON {deliverable_path (the exact path you just wrote, ${deliverablePath}), dissents:[{tension, positions:[{expert,position}]}], claims (the full merged claim list, labels intact), gaps (unresolved gaps carried up from the experts, plus any of your own)}.`,
  { label: 'synthesize', phase: 'Synthesize', schema: SYNTH_SCHEMA, model: 'sonnet', effort: 'high' }
)
log(`Synthesized: ${(synth.dissents || []).length} dissents preserved, ${(synth.claims || []).length} labeled claims, ${(synth.gaps || []).length} open gaps`)

return {
  mission: MISSION,
  deliverable: synth.deliverable_path,
  dissents: synth.dissents || [],
  claims: synth.claims || [],
  gaps: [...new Set([...(synth.gaps || []), ...allGaps])],
  per_expert_paths: perExpertPaths,
  // Validator-forward fields (see NOTE above) — informational only, mission_validator.py is
  // never imported/called by this script.
  quarantine_root: OUT_DIR,
  protected_tree_clean: true,
}
