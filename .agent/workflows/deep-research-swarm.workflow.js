export const meta = {
  name: 'deep-research-swarm',
  description: 'Native expert-swarm deep research: decompose → cast world-class personas → parallel fan-out → gap-fill loop → adversarial verify → synthesize collective insight. $0 incremental (Claude subagents + Tavily + free tools); Gemini Deep Research merges in parallel. Kimi-style, honest receipt.',
  phases: [
    { title: 'Cast' },
    { title: 'Fan-out' },
    { title: 'Gap-fill' },
    { title: 'Verify' },
    { title: 'Synthesize' },
  ],
}

// Accept args as an object OR a JSON string (defensive — binding varies by harness).
let _A = args
if (typeof _A === 'string') { try { _A = JSON.parse(_A) } catch (e) { _A = {} } }
const QUERY = (_A && _A.query) || 'online strength & conditioning coaching buyer psychology 2026'
const DEPTH = (_A && _A.depth) || 'standard'
const ROOT = '/Users/farricecain/Google Antigravity'
const SLUG = QUERY.toLowerCase().replace(/[^a-z0-9]+/g, '-').slice(0, 50).replace(/^-+|-+$/g, '')

const FINDINGS_SCHEMA = {
  type: 'object',
  required: ['findings', 'angle_insight'],
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['claim', 'source_url'],
        properties: {
          claim: { type: 'string' },
          source_url: { type: 'string' },
          excerpt: { type: 'string' },
          confidence: { type: 'string' },
          finding_type: { type: 'string' },
        },
      },
    },
    angle_insight: { type: 'string' },
  },
}

const PLAN_SCHEMA = {
  type: 'object',
  required: ['agents'],
  properties: {
    agent_count: { type: 'number' },
    intent: { type: 'string' },
    agents: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          role: { type: 'string' },
          expert: { type: 'string' },
          angle: { type: 'string' },
          lens: { type: 'string' },
          question: { type: 'string' },
          search_queries: { type: 'array', items: { type: 'string' } },
        },
      },
    },
  },
}

// Build the per-agent research brief locally (keeps the plan round-trip light).
function buildPrompt(a, query) {
  const qs = (a.search_queries || []).map((q) => `   - ${q}`).join('\n')
  return (
    `You are a **${a.role}** — research this through the lens of **${a.expert}**.\n\n` +
    `## Overall research question\n${query}\n\n` +
    `## Your assigned angle: ${a.angle}\n${a.question}\n\n` +
    `## Your expert lens (use it — this is why YOU are on this)\n${a.lens}\n\n` +
    `## How to research ($0 tools you already have)\n` +
    `1. \`tvly search\` / \`tvly research\` for cited multi-source grounding on your angle.\n` +
    `2. \`WebSearch\` across these queries, then \`WebFetch\` (or \`tvly extract\`) the 2-3 strongest sources for FULL-page reads (not snippets):\n${qs}\n` +
    `3. Mine real human language where your lens calls for it (Reddit, reviews, forums).\n` +
    `4. Adversarially check each claim: would a skeptic find a contradicting source? Drop what you cannot stand behind.\n\n` +
    `## Output (STRICT)\n` +
    `Return 5-12 findings. EVERY finding MUST have a real source_url — a claim with no URL is not a finding, omit it. ` +
    `Plus a 2-3 sentence angle_insight: the non-obvious thing your expert lens surfaced.`
  )
}

function bash(cmd) {
  return `Run exactly this and output ONLY the raw JSON it prints (no prose, no code fences):\ncd "${ROOT}" && ${cmd}`
}

// ── Phase: Cast ──────────────────────────────────────────────────────────
phase('Cast')
const plan = await agent(
  bash(`python3 execution/research.py plan --query ${JSON.stringify(QUERY)} --depth ${JSON.stringify(DEPTH)}`),
  { label: 'cast-plan', phase: 'Cast', schema: PLAN_SCHEMA }
)
const agentsSpec = (plan && plan.agents) || []
// Fire Gemini Deep Research in the BACKGROUND (parallel, $0 to start).
let gemId = ''
const gem = await agent(
  bash(`python3 execution/research.py gemini-start --query ${JSON.stringify(QUERY)} --mode standard`),
  { label: 'cast-gemini-start', phase: 'Cast', schema: { type: 'object', properties: { ok: { type: 'boolean' }, interaction_id: { type: 'string' } } } }
)
if (gem && gem.ok && gem.interaction_id) gemId = gem.interaction_id
log(`Cast ${agentsSpec.length} expert agents (intent=${plan ? plan.intent : '?'}); gemini bg=${gemId ? 'firing' : 'skipped'}`)

// ── Phase: Fan-out ───────────────────────────────────────────────────────
phase('Fan-out')
const waveResults = await parallel(
  agentsSpec.map((a) => () =>
    agent(buildPrompt(a, QUERY), { label: `${a.id}:${a.role}`, phase: 'Fan-out', schema: FINDINGS_SCHEMA })
  )
)
let findings = []
const insights = []
waveResults.forEach((r, i) => {
  if (!r) return
  ;(r.findings || []).forEach((f) => { if (f && f.source_url) findings.push(f) })
  if (r.angle_insight) insights.push(`- [${agentsSpec[i] ? agentsSpec[i].role : 'agent'}] ${r.angle_insight}`)
})
log(`Fan-out: ${findings.length} sourced findings from ${waveResults.filter(Boolean).length}/${agentsSpec.length} experts`)

// ── Phase: Gap-fill (the "deep" loop) ────────────────────────────────────
phase('Gap-fill')
const maxExtraWaves = DEPTH === 'max' ? 2 : DEPTH === 'deep' ? 1 : 0
let wave = 0
while (wave < maxExtraWaves) {
  const critic = await agent(
    `You are a research completeness critic for: ${QUERY}\n\nAngle insights gathered so far:\n${insights.join('\n')}\n\nFindings count: ${findings.length}.\n\n` +
      `Name up to 4 IMPORTANT gaps still unanswered (missing angle, unverified key claim, missing data). ` +
      `Return JSON {gaps:[{role, lens, question, search_query}]}. If coverage is genuinely solid, return {gaps:[]}.`,
    { label: `gap-critic-w${wave + 1}`, phase: 'Gap-fill', schema: { type: 'object', required: ['gaps'], properties: { gaps: { type: 'array', items: { type: 'object', properties: { role: { type: 'string' }, lens: { type: 'string' }, question: { type: 'string' }, search_query: { type: 'string' } } } } } } }
  )
  const gaps = (critic && critic.gaps) || []
  if (!gaps.length) { log(`Gap-fill wave ${wave + 1}: no material gaps — coverage solid.`); break }
  const fill = await parallel(
    gaps.map((g, i) => () =>
      agent(
        `You are a ${g.role || 'research specialist'}. Lens: ${g.lens || 'evidence-first'}.\n` +
          `Fill this gap for "${QUERY}": ${g.question}\n` +
          `Use tvly search/research + WebSearch + WebFetch. Suggested query: ${g.search_query || g.question}\n` +
          `Return JSON {findings:[...], angle_insight} — EVERY finding needs a real source_url.`,
        { label: `gapfill-w${wave + 1}-${i + 1}`, phase: 'Gap-fill', schema: FINDINGS_SCHEMA }
      )
    )
  )
  let added = 0
  fill.forEach((r) => {
    if (!r) return
    ;(r.findings || []).forEach((f) => { if (f && f.source_url) { findings.push(f); added++ } })
    if (r.angle_insight) insights.push(`- [gap] ${r.angle_insight}`)
  })
  log(`Gap-fill wave ${wave + 1}: +${added} findings from ${gaps.length} gap agents`)
  wave++
}

// ── Phase: Verify (adversarial) ──────────────────────────────────────────
phase('Verify')
const checkN = DEPTH === 'quick' ? 0 : DEPTH === 'standard' ? 4 : 8
const claims = findings.filter((f) => ['statistic', 'data'].includes(f.finding_type)).slice(0, checkN)
if (claims.length) {
  const verdicts = await parallel(
    claims.map((f, i) => () =>
      agent(
        `Adversarially verify this claim — try to REFUTE it. Claim: "${f.claim}" (cited: ${f.source_url}).\n` +
          `Check INDEPENDENT sources via WebSearch/tvly. Return JSON {holds: true|false, note}. ` +
          `Default holds=false if you cannot independently corroborate.`,
        { label: `verify-${i + 1}`, phase: 'Verify', schema: { type: 'object', required: ['holds'], properties: { holds: { type: 'boolean' }, note: { type: 'string' } } } }
      )
    )
  )
  let dropped = 0
  verdicts.forEach((v, i) => { if (v && v.holds === false) { claims[i]._refuted = true; dropped++ } })
  findings = findings.filter((f) => !f._refuted)
  log(`Verify: checked ${claims.length} claims, dropped ${dropped} that couldn't be independently corroborated`)
} else {
  log('Verify: skipped (quick depth)')
}

// ── Phase: Synthesize (+ merge background Gemini, ingest → receipt) ───────
phase('Synthesize')
let gemText = ''
if (gemId) {
  const col = await agent(
    bash(`python3 execution/research.py gemini-collect --id ${JSON.stringify(gemId)} --query ${JSON.stringify(QUERY)}`),
    { label: 'gemini-collect', phase: 'Synthesize', schema: { type: 'object', properties: { status: { type: 'string' }, text: { type: 'string' } } } }
  )
  if (col && col.status === 'completed' && col.text) { gemText = col.text; log('Gemini background result MERGED ✓') }
  else { log(`Gemini background: ${col ? col.status : 'unknown'} — not merged (swarm stands alone)`) }
}

// Write findings to JSONL + ingest → typed ResearchResult + honest Receipt.
const jsonl = findings
  .map((f) => JSON.stringify({ claim: f.claim, source_url: f.source_url, excerpt: f.excerpt || '', confidence: f.confidence || 'medium', finding_type: f.finding_type || 'data' }))
  .join('\n')
const receipt = await agent(
  `Create the directory .tmp/research/${SLUG}/ under ${ROOT} if needed, then write this EXACT content to .tmp/research/${SLUG}/native-findings.jsonl (one JSON object per line, verbatim):\n` +
    '```\n' + jsonl + '\n```\n' +
    `Then run and output ONLY the receipt it prints:\ncd "${ROOT}" && python3 execution/research.py ingest --findings .tmp/research/${SLUG}/native-findings.jsonl --query ${JSON.stringify(QUERY)} --depth ${JSON.stringify(DEPTH)} --swarm`,
  { label: 'ingest-receipt', phase: 'Synthesize' }
)

const synthesis = await agent(
  `Synthesize a dense, cited intelligence brief for: ${QUERY}\n\n` +
    `You have ${findings.length} sourced findings from an expert swarm and these angle insights:\n${insights.join('\n')}\n\n` +
    (gemText ? `Gemini Deep Research independently produced this — fold in its UNIQUE points:\n${gemText.slice(0, 4000)}\n\n` : '') +
    `Write three sections, citing source URLs inline, no filler:\n` +
    `1. EXECUTIVE TRUTH — the 3-5 most important, decision-grade findings.\n` +
    `2. COLLECTIVE INSIGHT BY ANGLE — what each expert lens surfaced that the others didn't.\n` +
    `3. CONTRARIAN / RISK — the 3 strongest counter-points or risks.`,
  { label: 'synthesize', phase: 'Synthesize' }
)

return {
  query: QUERY,
  depth: DEPTH,
  experts_fired: agentsSpec.length,
  findings: findings.length,
  gemini_merged: !!gemText,
  receipt,
  synthesis,
  angle_insights: insights,
}
