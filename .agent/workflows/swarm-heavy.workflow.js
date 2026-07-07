export const meta = {
  name: 'swarm-heavy',
  description: 'Grok-Heavy/Kimi killer: N independent expert trajectories on ONE problem, reflective aggregation that PRESERVES dissent (never blend to mush), then adversarial claim verification. $0 incremental — Claude subagents only.',
  phases: [
    { title: 'Diverge', detail: 'fanOut independent expert takes on the brief, each through its own skill/genius + lens, written to file' },
    { title: 'Aggregate', detail: 'reflective aggregation of all takes (files Read in full, not just summaries) preserving real dissent as explicit Forks' },
    { title: 'Verify', detail: 'adversarial refuters try to REFUTE each top claim; default to refuted/unconfirmed if uncertain' },
    { title: 'Assemble', detail: 'final deliverable: Answer / Forks / Claim ledger / Task trace — refuted claims corrected or removed from the Answer' },
  ],
}

// Accept args as an object OR a JSON string (defensive — binding varies by
// harness; matches collective-genius-council.workflow.js idiom).
let _A = args
if (typeof _A === 'string') { try { _A = JSON.parse(_A) } catch (e) { _A = {} } }
const SLUG = (_A && _A.slug) || 'swarm-heavy-run'
const BRIEF = (_A && _A.brief) || ''
const _fanOutRaw = Number((_A && _A.fanOut) || 8)
const FAN_OUT = Math.min(Number.isFinite(_fanOutRaw) ? _fanOutRaw : 8, 12)
const ROSTER = ((_A && _A.roster) || []).slice(0, 12)
const MISSION_PATH = (_A && _A.missionPath) || `.tmp/swarm/${SLUG}/mission.md`
const OUT_DIR = (_A && _A.outDir) || `.tmp/swarm/${SLUG}`
const ROOT = '/Users/farricecain/Google Antigravity'

// The shared contract doesn't say whether missionPath/outDir arrive absolute
// or repo-relative — normalize defensively so both forms work.
const abs = (p) => (p && p.startsWith('/') ? p : `${ROOT}/${p}`)
const missionAbs = abs(MISSION_PATH)
const outDirAbs = abs(OUT_DIR)
const slugify = (s) => ((s || 'expert').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'expert')

const DIVERGE_SCHEMA = {
  type: 'object',
  required: ['expert', 'position', 'keyClaims', 'confidence', 'filePath'],
  properties: {
    expert: { type: 'string' },
    position: { type: 'string', description: '≤80 words' },
    keyClaims: {
      type: 'array',
      items: {
        type: 'object',
        required: ['claim', 'tag'],
        properties: {
          claim: { type: 'string' },
          tag: { type: 'string', enum: ['GROUNDED', 'SUPPLEMENTED', 'PROJECTED'] },
          source: { type: 'string' },
        },
      },
    },
    confidence: { type: 'number', description: '1-10' },
    dissentRisk: { type: 'string', description: 'what the OTHER experts will get wrong' },
    filePath: { type: 'string' },
  },
}

const AGGREGATE_SCHEMA = {
  type: 'object',
  required: ['finalPosition', 'filePath'],
  properties: {
    finalPosition: { type: 'string' },
    forks: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          question: { type: 'string' },
          positions: { type: 'string' },
          resolver: { type: 'string' },
        },
      },
    },
    topClaims: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          claim: { type: 'string' },
          tag: { type: 'string' },
          source: { type: 'string' },
        },
      },
    },
    filePath: { type: 'string' },
  },
}

const VERIFY_SCHEMA = {
  type: 'object',
  required: ['claim', 'verdict'],
  properties: {
    claim: { type: 'string' },
    verdict: { type: 'string', enum: ['VERIFIED', 'LIKELY', 'UNCONFIRMED', 'REFUTED'] },
    evidence: { type: 'string' },
    source: { type: 'string' },
  },
}

const ASSEMBLE_SCHEMA = {
  type: 'object',
  required: ['deliverablePath', 'refutedCount', 'unconfirmedCount'],
  properties: {
    deliverablePath: { type: 'string' },
    refutedCount: { type: 'number' },
    unconfirmedCount: { type: 'number' },
  },
}

// 4-field envelope per directives/sub_agent_protocol.md (box-separator form).
function envelope({ objective, outputFormat, allow, deny, scope, antiScope, halt, skillAcquisition }) {
  return (
    `═══ OBJECTIVE ═══\n${objective}\n\n` +
    `═══ OUTPUT FORMAT ═══\n${outputFormat}\n\n` +
    `═══ TOOLS ALLOWED ═══\nALLOW: ${allow}\nDENY: ${deny || 'no further sub-agent spawns (no nesting)'}\n\n` +
    `═══ BOUNDARIES ═══\nSCOPE: ${scope}\nANTI-SCOPE: ${antiScope}\nHALT: ${halt}` +
    (skillAcquisition ? `\n\n═══ SKILL ACQUISITION ═══\n${skillAcquisition}` : '')
  )
}

const taskTrace = []
let deadWorkers = 0

// ── Diverge ──────────────────────────────────────────────────────────────
phase('Diverge')
const workers = ROSTER.slice(0, FAN_OUT)
const takeResults = await parallel(
  workers.map((m) => () => {
    const fname = `${outDirAbs}/takes/${slugify(m.name)}.md`
    return agent(
      envelope({
        objective:
          `STEP 1 — Read the mission file at ${missionAbs} first (it carries the objective, constraints, and plan checklist — recite the constraints to yourself before proceeding). ` +
          `STEP 2 — SKILL ACQUISITION (Tier 3 loading per directives/agent-loading-protocol.md): read the skill (and genius file, if any) and embody the expert's THINKING, not vocabulary. ` +
          `STEP 3 — Attack this brief through YOUR assigned lens: "${m.lens || 'no lens specified'}". Give the distinctive take only ${m.name} would give — not a comprehensive survey.\n\nBRIEF:\n${BRIEF}`,
        outputFormat:
          `Write your FULL take to ${fname} (create dirs as needed). Return JSON: {expert, position (≤80 words), keyClaims:[{claim, tag, source}], confidence (1-10), dissentRisk (what the OTHER experts will get wrong), filePath}. ` +
          `Every claim in keyClaims MUST carry a grounding tag — GROUNDED (cite the source), SUPPLEMENTED (label as training knowledge), or PROJECTED (label as inference). ` +
          `In the FILE you write, tag claims with the repo convention 🟢 GROUNDED / 🟡 SUPPLEMENTED / 🔴 PROJECTED. In the schema \`tag\` field, return exactly GROUNDED | SUPPLEMENTED | PROJECTED — plain word, NO emoji. ` +
          `filePath must equal ${fname}. Return a summary ≤500 tokens including the file path.`,
        allow: 'Read, Write, Grep, Glob, WebSearch, WebFetch',
        scope: `Your assigned lens ("${m.lens || 'n/a'}") on the brief only`,
        antiScope: "Do not attempt comprehensive coverage of the brief — that is the Aggregate phase's job",
        halt: 'After your take file is written and the JSON is returned',
        skillAcquisition:
          `Read: ${abs(m.skill)}${m.genius ? ` → ${abs(m.genius)}` : ' (no genius file for this expert — skip)'}. ` +
          `Before writing, confirm internally: what would this expert say is WRONG with the obvious/generic take here?`,
      }),
      { label: m.name, phase: 'Diverge', schema: DIVERGE_SCHEMA, model: 'sonnet' }
    ).then((r) => (r ? { ...r, _expertMeta: m } : null))
  })
)
const takes = takeResults.filter(Boolean)
deadWorkers += workers.length - takes.length
// Zero-survivor guard: no takes = nothing downstream can honestly aggregate.
if (workers.length > 0 && takes.length === 0) {
  log('FAILED: Diverge produced zero survivors — aborting before Aggregate.')
  return {
    deliverablePath: null,
    failed: true,
    failureReason: 'Diverge produced zero survivors',
    taskTrace,
    forks: [],
    tokensSpent: budget.spent(),
    agentCount: workers.length,
  }
}
takes.forEach((t) =>
  taskTrace.push({ phase: 'Diverge', label: t.expert || (t._expertMeta && t._expertMeta.name), filePath: t.filePath, summary1line: (t.position || '').slice(0, 160) })
)
log(`Diverge: ${takes.length}/${workers.length} takes written (budget spent ${budget.spent()})`)

// ── Aggregate ────────────────────────────────────────────────────────────
phase('Aggregate')
const takesManifest = takes
  .map((t) => `- **${t.expert}** [confidence ${t.confidence}] file: ${t.filePath}\n  position: ${t.position}\n  dissentRisk: ${t.dissentRisk || 'n/a'}`)
  .join('\n')
const aggregate = await agent(
  `You are the reflective aggregator (Kimi-heavy style) for the brief:\n${BRIEF}\n\n` +
    `Read the mission file first: ${missionAbs}.\n\n` +
    `${takes.length} independent expert takes were produced. You MUST Read each take file IN FULL before aggregating — the summaries below are not sufficient on their own:\n${takesManifest}\n\n` +
    `Produce a reflective aggregation across all takes — BUT preserve real disagreement (never blend to mush, per the convene doctrine). ` +
    `Write the full aggregation to ${outDirAbs}/aggregate.md, containing: the final answer, an explicit "Forks" section (positions that genuinely disagree — who holds them, what evidence would resolve each), and the top claims worth adversarial verification.\n\n` +
    `Return JSON {finalPosition, forks:[{question, positions, resolver}], topClaims:[{claim, tag, source}], filePath}.`,
  { label: 'aggregate', phase: 'Aggregate', schema: AGGREGATE_SCHEMA }
)
// Zero-survivor guard: an aggregate that died never wrote aggregate.md —
// never fall back to a fabricated path.
if (!aggregate) {
  log('FAILED: Aggregate produced zero survivors — aborting before Verify.')
  return {
    deliverablePath: null,
    failed: true,
    failureReason: 'Aggregate produced zero survivors',
    taskTrace,
    forks: [],
    tokensSpent: budget.spent(),
    agentCount: workers.length + 1,
  }
}
if (aggregate.filePath) {
  taskTrace.push({ phase: 'Aggregate', label: 'aggregate', filePath: aggregate.filePath, summary1line: (aggregate.finalPosition || '').slice(0, 160) })
}
log(`Aggregate: ${(aggregate.forks || []).length} forks preserved, ${(aggregate.topClaims || []).length} claims flagged for verification`)

// ── Verify ───────────────────────────────────────────────────────────────
phase('Verify')
const claimsToCheck = (aggregate.topClaims || []).slice(0, 6)
const verdicts = claimsToCheck.length
  ? await parallel(
      claimsToCheck.map((c, i) => () =>
        agent(
          `Adversarially try to REFUTE this claim — do not confirm it by default. Claim: "${c.claim}" (cited source: ${c.source || 'none cited'}, original tag: ${c.tag || 'unknown'}).\n` +
            `Use WebSearch to look for independent corroboration or contradiction. If you cannot independently corroborate it, default the verdict to UNCONFIRMED or REFUTED — never VERIFIED on silence.\n` +
            `Return JSON {claim, verdict: VERIFIED|LIKELY|UNCONFIRMED|REFUTED, evidence, source}.`,
          { label: `verify-${i + 1}`, phase: 'Verify', schema: VERIFY_SCHEMA, model: 'sonnet', effort: 'low' }
        )
      )
    )
  : []
const validVerdicts = verdicts.filter(Boolean)
deadWorkers += claimsToCheck.length - validVerdicts.length
validVerdicts.forEach((v) =>
  taskTrace.push({ phase: 'Verify', label: `verify:${(v.claim || '').slice(0, 40)}`, filePath: '', summary1line: `${v.verdict}: ${(v.evidence || '').slice(0, 120)}` })
)
const refutedCount0 = validVerdicts.filter((v) => v.verdict === 'REFUTED').length
log(`Verify: ${validVerdicts.length}/${claimsToCheck.length} claims checked, ${refutedCount0} refuted (budget spent ${budget.spent()})`)

// ── Assemble ─────────────────────────────────────────────────────────────
phase('Assemble')
const verdictsManifest =
  validVerdicts.map((v) => `- "${v.claim}" -> ${v.verdict} (${v.evidence || 'no evidence given'}${v.source ? `, source: ${v.source}` : ''})`).join('\n') ||
  'none checked'
const traceManifest = takes.map((t) => `- [Diverge] ${t.expert}: ${t.filePath}`).join('\n')
const aggregateFilePath = aggregate.filePath
const deliverablePath = `${outDirAbs}/heavy-report.md`
const assemble = await agent(
  `Read the aggregate file at ${aggregateFilePath} in full, then assemble the FINAL deliverable at ${deliverablePath}.\n\n` +
    `Verdicts from adversarial verification:\n${verdictsManifest}\n\n` +
    `Task trace so far (every Diverge agent + file):\n${traceManifest}\n- [Aggregate] aggregate: ${aggregateFilePath}\n- [Verify] ${validVerdicts.length} claims checked\n\n` +
    `Write these sections to ${deliverablePath}:\n` +
    `1. Answer — the aggregated final position. Any claim verdicted REFUTED must be corrected or removed from this section entirely.\n` +
    `2. Forks — the preserved dissent from Aggregate, verbatim (question / positions / resolver).\n` +
    `3. Claim ledger — every checked claim with its verdict and source; note which were corrected/removed from the Answer.\n` +
    `4. Task trace — every agent that ran (each Diverge expert, Aggregate, each Verify check), its file (if any), and a one-line summary.\n\n` +
    `Return JSON {deliverablePath, refutedCount, unconfirmedCount}.`,
  { label: 'assemble', phase: 'Assemble', schema: ASSEMBLE_SCHEMA }
)
const agentCount = workers.length + 1 /* aggregate */ + claimsToCheck.length + 1 /* assemble */

// Zero-survivor guard: an assembler that died never wrote heavy-report.md —
// never return a guessed deliverablePath.
if (!assemble) {
  log('FAILED: Assemble produced zero survivors — no deliverable was written.')
  return {
    deliverablePath: null,
    failed: true,
    failureReason: 'Assemble produced zero survivors',
    taskTrace,
    forks: aggregate.forks || [],
    tokensSpent: budget.spent(),
    agentCount,
  }
}
taskTrace.push({
  phase: 'Assemble',
  label: 'assemble',
  filePath: assemble.deliverablePath,
  summary1line: `${assemble.refutedCount || 0} refuted, ${assemble.unconfirmedCount || 0} unconfirmed`,
})
log(`Assemble: deliverable written to ${assemble.deliverablePath}${deadWorkers ? ` (degraded: ${deadWorkers} dead workers)` : ''}`)

return {
  deliverablePath: assemble.deliverablePath,
  taskTrace,
  forks: aggregate.forks || [],
  tokensSpent: budget.spent(),
  agentCount,
  ...(deadWorkers > 0 ? { degraded: true, deadWorkers } : {}),
}
