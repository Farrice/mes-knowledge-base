export const meta = {
  name: 'swarm-research',
  description: 'Perplexity Deep Research killer: query decomposition → parallel search workers → gap-driven second round → adversarial claim verification → cited synthesis with a visible task trace. $0 incremental — WebSearch/WebFetch only, no paid Perplexity MCP calls.',
  phases: [
    { title: 'Decompose', detail: 'break the question into 6 (standard) or 10 (deep) subtopics, each with search queries + a settles-criterion' },
    { title: 'Sweep', detail: 'per-subtopic search workers write grounded findings files with per-claim tags + source URLs + unknowns' },
    { title: 'Gap check', detail: 'identify contradictions + material unknowns; deep runs may trigger one followup sweep round' },
    { title: 'Verify', detail: 'adversarial verification of the most load-bearing claims; default to unconfirmed/refuted on silence' },
    { title: 'Synthesize', detail: 'Single Truth + labeled narrative + contradictions/unknowns + source inventory + task trace' },
  ],
}

// Accept args as an object OR a JSON string (defensive — binding varies by
// harness; matches collective-genius-council.workflow.js idiom).
let _A = args
if (typeof _A === 'string') { try { _A = JSON.parse(_A) } catch (e) { _A = {} } }
const SLUG = (_A && _A.slug) || 'swarm-research-run'
const QUESTION = (_A && _A.question) || ''
const DEPTH = (_A && _A.depth) === 'deep' ? 'deep' : 'standard'
const MISSION_PATH = (_A && _A.missionPath) || `.tmp/swarm/${SLUG}/mission.md`
const OUT_DIR = (_A && _A.outDir) || `.tmp/swarm/${SLUG}`
const ROOT = '/Users/farricecain/Google Antigravity'

// The shared contract doesn't say whether missionPath/outDir arrive absolute
// or repo-relative — normalize defensively so both forms work.
const abs = (p) => (p && p.startsWith('/') ? p : `${ROOT}/${p}`)
const missionAbs = abs(MISSION_PATH)
const outDirAbs = abs(OUT_DIR)
const slugify = (s) => ((s || 'subtopic').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'subtopic')

const NUM_SUBTOPICS = DEPTH === 'deep' ? 10 : 6
// "standard"→1 round total (no gap-fill), "deep"→up to 2 rounds total
// (initial sweep + at most one gap-driven followup sweep).
const ALLOW_FOLLOWUP = DEPTH === 'deep'

const DECOMPOSE_SCHEMA = {
  type: 'object',
  required: ['subtopics'],
  properties: {
    subtopics: {
      type: 'array',
      items: {
        type: 'object',
        required: ['name', 'queries'],
        properties: {
          name: { type: 'string' },
          queries: { type: 'array', items: { type: 'string' } },
          settles: { type: 'string', description: 'what would settle this' },
        },
      },
    },
  },
}

const SWEEP_SCHEMA = {
  type: 'object',
  required: ['subtopic', 'filePath'],
  properties: {
    subtopic: { type: 'string' },
    keyFindings: { type: 'array', items: { type: 'string' }, description: '≤5 bullets' },
    claims: {
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
    unknowns: { type: 'string' },
    filePath: { type: 'string' },
  },
}

const GAP_SCHEMA = {
  type: 'object',
  required: ['contradictions'],
  properties: {
    contradictions: { type: 'array', items: { type: 'object', additionalProperties: true } },
    followups: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' },
          queries: { type: 'array', items: { type: 'string' } },
        },
      },
    },
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

const SYNTH_SCHEMA = {
  type: 'object',
  required: ['deliverablePath', 'singleTruth'],
  properties: {
    deliverablePath: { type: 'string' },
    verifiedCount: { type: 'number' },
    unconfirmedCount: { type: 'number' },
    singleTruth: { type: 'string', description: '≤50 words' },
  },
}

// 4-field envelope per directives/sub_agent_protocol.md (box-separator form).
function envelope({ objective, outputFormat, allow, deny, scope, antiScope, halt }) {
  return (
    `═══ OBJECTIVE ═══\n${objective}\n\n` +
    `═══ OUTPUT FORMAT ═══\n${outputFormat}\n\n` +
    `═══ TOOLS ALLOWED ═══\nALLOW: ${allow}\nDENY: ${deny || 'no further sub-agent spawns (no nesting); no paid Perplexity MCP calls'}\n\n` +
    `═══ BOUNDARIES ═══\nSCOPE: ${scope}\nANTI-SCOPE: ${antiScope}\nHALT: ${halt}`
  )
}

function sweepPrompt(st) {
  const fname = `${outDirAbs}/findings/${slugify(st.name)}.md`
  return envelope({
    objective:
      `STEP 1 — Read the mission file at ${missionAbs} first (objective, constraints, plan checklist). ` +
      `STEP 2 — Research this subtopic: "${st.name}" (part of the overall question: ${QUESTION}). What would settle this: ${st.settles || 'n/a'}. ` +
      `Run these search queries (or close variants): ${(st.queries || []).join(' | ')}`,
    outputFormat:
      `Read the top sources you find (WebFetch the full page, not just the snippet), then write findings to ${fname} (create dirs as needed): findings + per-claim grounding tags + source URLs + what remains unknown. ` +
      `In the FILE you write, tag claims with the repo convention 🟢 GROUNDED / 🟡 SUPPLEMENTED / 🔴 PROJECTED. In the schema \`tag\` field, return exactly GROUNDED | SUPPLEMENTED | PROJECTED — plain word, NO emoji. ` +
      `Return JSON {subtopic, keyFindings (≤5 bullets), claims:[{claim, tag, source}], unknowns, filePath}. filePath must equal ${fname}. Return a summary ≤500 tokens including the file path.`,
    allow: 'WebSearch, WebFetch, Read, Write, Grep, Glob',
    deny: 'no mcp__perplexity-ask__* calls (no paid Perplexity); no further sub-agent spawns',
    scope: `This subtopic only: ${st.name}`,
    antiScope: 'Do not attempt the whole question — Synthesize handles cross-subtopic integration',
    halt: 'After the findings file is written and JSON returned',
  })
}

const taskTrace = []
let deadWorkers = 0

// ── Decompose ────────────────────────────────────────────────────────────
phase('Decompose')
const decomposed = await agent(
  `Read the mission file first: ${missionAbs} (objective, constraints, plan checklist).\n\n` +
    `Decompose this research question into ${NUM_SUBTOPICS} subtopics, each with 2-3 concrete search queries and a "what would settle this" criterion.\n\n` +
    `QUESTION: ${QUESTION}\n\nReturn JSON {subtopics:[{name, queries:[...], settles}]}.`,
  { label: 'decompose', phase: 'Decompose', schema: DECOMPOSE_SCHEMA }
)
const subtopics = ((decomposed && decomposed.subtopics) || []).slice(0, NUM_SUBTOPICS)
// Zero-survivor guard: no subtopics = the Sweep guard below could never fire
// (its attempted count would be 0) and the run would limp to a hollow report.
if (subtopics.length === 0) {
  log('FAILED: Decompose produced zero survivors — aborting before Sweep.')
  return {
    deliverablePath: null,
    failed: true,
    failureReason: 'Decompose produced zero survivors',
    taskTrace,
    gaps: [],
    tokensSpent: budget.spent(),
    agentCount: 1,
  }
}
log(`Decompose: ${subtopics.length} subtopics planned (depth=${DEPTH})`)

// ── Sweep ────────────────────────────────────────────────────────────────
phase('Sweep')
const sweepResults = await pipeline(
  subtopics,
  (st) =>
    agent(sweepPrompt(st), { label: `sweep:${st.name}`, phase: 'Sweep', schema: SWEEP_SCHEMA, model: 'sonnet' }).then((r) => (r ? { ...r, _st: st } : null))
)
let findings = sweepResults.filter(Boolean)
deadWorkers += subtopics.length - findings.length
// Zero-survivor guard: no findings = nothing downstream can honestly synthesize.
if (subtopics.length > 0 && findings.length === 0) {
  log('FAILED: Sweep produced zero survivors — aborting before Gap check.')
  return {
    deliverablePath: null,
    failed: true,
    failureReason: 'Sweep produced zero survivors',
    taskTrace,
    gaps: [],
    tokensSpent: budget.spent(),
    agentCount: 1 + subtopics.length,
  }
}
findings.forEach((f) =>
  taskTrace.push({
    phase: 'Sweep',
    label: f.subtopic || (f._st && f._st.name),
    filePath: f.filePath,
    summary1line: (f.keyFindings || []).slice(0, 2).join(' | ').slice(0, 160),
  })
)
log(`Sweep: ${findings.length}/${subtopics.length} subtopics researched (budget spent ${budget.spent()})`)

// ── Gap check ────────────────────────────────────────────────────────────
phase('Gap check')
const findingsManifest = findings
  .map((f) => `- **${f.subtopic}**: ${(f.keyFindings || []).join('; ')} (unknowns: ${f.unknowns || 'none noted'}) file: ${f.filePath}`)
  .join('\n')
const gapCheck = await agent(
  `Identify contradictions between subtopic findings and material unknowns for the question: ${QUESTION}\n\nFindings so far:\n${findingsManifest}\n\n` +
    (ALLOW_FOLLOWUP
      ? `This is a "deep" run — if there are material gaps (missing angle, unverified key claim, missing data), propose up to 4 followupQueries as {name, queries}. If coverage is genuinely solid, return followups: [].`
      : `This is a "standard" run — report contradictions/unknowns for the record only; no followup sweep round will run regardless of what you return here.`) +
    `\n\nReturn JSON {contradictions:[...], followups:[{name, queries}]}.`,
  { label: 'gap-check', phase: 'Gap check', schema: GAP_SCHEMA }
)
const contradictions = (gapCheck && gapCheck.contradictions) || []
const followups = (ALLOW_FOLLOWUP ? (gapCheck && gapCheck.followups) || [] : []).slice(0, 4)
log(`Gap check: ${contradictions.length} contradictions noted; ${followups.length} followups queued`)

if (followups.length) {
  const followupResults = await parallel(
    followups.map((fu) => () =>
      agent(sweepPrompt(fu), { label: `sweep-followup:${fu.name}`, phase: 'Gap check', schema: SWEEP_SCHEMA, model: 'sonnet' }).then((r) => (r ? { ...r, _st: fu } : null))
    )
  )
  const followupFindings = followupResults.filter(Boolean)
  deadWorkers += followups.length - followupFindings.length
  followupFindings.forEach((f) =>
    taskTrace.push({
      phase: 'Gap check (followup sweep)',
      label: f.subtopic || (f._st && f._st.name),
      filePath: f.filePath,
      summary1line: (f.keyFindings || []).slice(0, 2).join(' | ').slice(0, 160),
    })
  )
  findings = findings.concat(followupFindings)
  log(`Gap check: +${followupFindings.length} findings from followup sweep round`)
}

// ── Verify ───────────────────────────────────────────────────────────────
phase('Verify')
const allClaims = []
findings.forEach((f) => (f.claims || []).forEach((c) => allClaims.push(c)))
// Prioritize GROUNDED (highest-stakes: already source-cited) claims, then
// fill from the rest, cap the candidate pool at 8, then verify the top 6
// in parallel (reconciling the spec's "5-8 most load-bearing" against its
// own "parallel, cap 6" — see deviations note in the final report).
const grounded = allClaims.filter((c) => c.tag === 'GROUNDED')
const others = allClaims.filter((c) => c.tag !== 'GROUNDED')
const candidates = grounded.concat(others).slice(0, 8)
const claimsToVerify = candidates.slice(0, 6)
const verdicts = claimsToVerify.length
  ? await parallel(
      claimsToVerify.map((c, i) =>
        () =>
          agent(
            `Adversarially try to REFUTE this claim — do not confirm it by default. Claim: "${c.claim}" (cited source: ${c.source || 'none cited'}, original tag: ${c.tag || 'unknown'}).\n` +
              `Use WebSearch for independent corroboration or contradiction. Default to UNCONFIRMED or REFUTED if you cannot independently corroborate — never VERIFIED on silence.\n` +
              `Return JSON {claim, verdict: VERIFIED|LIKELY|UNCONFIRMED|REFUTED, evidence, source}.`,
            { label: `verify-${i + 1}`, phase: 'Verify', schema: VERIFY_SCHEMA, model: 'sonnet' }
          )
      )
    )
  : []
const validVerdicts = verdicts.filter(Boolean)
deadWorkers += claimsToVerify.length - validVerdicts.length
validVerdicts.forEach((v) =>
  taskTrace.push({ phase: 'Verify', label: `verify:${(v.claim || '').slice(0, 40)}`, filePath: '', summary1line: `${v.verdict}: ${(v.evidence || '').slice(0, 120)}` })
)
const verifiedCount0 = validVerdicts.filter((v) => v.verdict === 'VERIFIED').length
log(`Verify: ${validVerdicts.length}/${claimsToVerify.length} load-bearing claims checked (${verifiedCount0} verified, budget spent ${budget.spent()})`)

// ── Synthesize ───────────────────────────────────────────────────────────
phase('Synthesize')
const allFindingsManifest = findings.map((f) => `- **${f.subtopic}** file: ${f.filePath}`).join('\n')
const verdictsManifest =
  validVerdicts.map((v) => `- "${v.claim}" -> ${v.verdict} (${v.evidence || 'n/a'}${v.source ? `, source: ${v.source}` : ''})`).join('\n') || 'none checked'
const deliverablePath = `${outDirAbs}/research-report.md`
const synth = await agent(
  `Read the mission file first: ${missionAbs}.\n\n` +
    `Read ALL findings files listed below IN FULL before writing (do not rely on the manifest alone):\n${allFindingsManifest}\n\n` +
    `QUESTION: ${QUESTION}\n\nVerification verdicts:\n${verdictsManifest}\n\n` +
    `Contradictions/unknowns noted at Gap check:\n${contradictions.length ? contradictions.map((c) => `- ${JSON.stringify(c)}`).join('\n') : 'none'}\n\n` +
    `Write the report to ${deliverablePath} with these sections:\n` +
    `1. Single Truth — up top, the one decision-grade answer.\n` +
    `2. Narrative — inline [VERIFIED]/[LIKELY]/[UNCONFIRMED] labels on every load-bearing claim; REFUTED claims corrected or removed.\n` +
    `3. Contradictions & Unknowns — honesty over completeness (can degrade, cannot lie — per execution/research.py doctrine).\n` +
    `4. Source Inventory — every source URL used, grouped by subtopic.\n` +
    `5. Task Trace — every worker: subtopic, queries run, file.\n\n` +
    `Return JSON {deliverablePath, verifiedCount, unconfirmedCount, singleTruth (≤50 words)}.`,
  { label: 'synthesize', phase: 'Synthesize', schema: SYNTH_SCHEMA }
)
const agentCount = 1 /* decompose */ + subtopics.length /* sweep */ + 1 /* gap-check */ + followups.length /* followup sweep */ + claimsToVerify.length /* verify */ + 1 /* synthesize */

// Zero-survivor guard: a synthesizer that died never wrote research-report.md —
// never return a guessed deliverablePath.
if (!synth) {
  log('FAILED: Synthesize produced zero survivors — no deliverable was written.')
  return {
    deliverablePath: null,
    failed: true,
    failureReason: 'Synthesize produced zero survivors',
    taskTrace,
    gaps: contradictions,
    tokensSpent: budget.spent(),
    agentCount,
  }
}
taskTrace.push({ phase: 'Synthesize', label: 'synthesize', filePath: synth.deliverablePath, summary1line: (synth.singleTruth || '').slice(0, 160) })
log(`Synthesize: deliverable written to ${synth.deliverablePath}${deadWorkers ? ` (degraded: ${deadWorkers} dead workers)` : ''}`)

return {
  deliverablePath: synth.deliverablePath,
  taskTrace,
  gaps: contradictions,
  tokensSpent: budget.spent(),
  agentCount,
  ...(deadWorkers > 0 ? { degraded: true, deadWorkers } : {}),
}
