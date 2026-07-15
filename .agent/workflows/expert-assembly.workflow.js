export const meta = {
  name: 'expert-assembly',
  description: 'Assemble a world-class expert panel for ANY task. Detects domain coverage gaps in the roster, seats strong matches directly, synthesizes bespoke composite personas where coverage is thin/absent, runs genuine multi-round deliberation, and emits a tiered roadmap (strategic 6–12mo / tactical 1–6mo / operational 0–30d) with observable success criteria. Hybrid panel: no fabricated credentials, no phantom research, real synthesis. The presets /assemble front this via args.mode and args.domains.',
  phases: [
    { title: 'Scope' },
    { title: 'Cast' },
    { title: 'Forge' },
    { title: 'Diverge' },
    { title: 'Deliberate' },
    { title: 'Synthesize' },
    { title: 'Learn' },
    { title: 'Close' },
  ],
}

let _A = args
if (typeof _A === 'string') { try { _A = JSON.parse(_A) } catch (e) { _A = {} } }
const TASK = (_A && _A.task) || 'Design optimal rigging configuration for racing yacht in varying sea states'
const _rawDomains = (_A && _A.domains) || []
const SUPPLIED_DOMAINS = (Array.isArray(_rawDomains) ? _rawDomains : String(_rawDomains).split(','))
  .map(d => String(d).trim()).filter(Boolean)
const MODE = (_A && _A.mode) || 'panel'
const ROOT = '/Users/farricecain/Google Antigravity'
const SLUG = TASK.toLowerCase().replace(/[^a-z0-9]+/g, '-').slice(0, 48).replace(/^-+|-+$/g, '')

const PANEL_SCHEMA = {
  type: 'object',
  required: ['task', 'mode', 'panel', 'coverage', 'seats_total', 'roster_seats', 'bespoke_seats'],
  properties: {
    task: { type: 'string' },
    mode: { type: 'string' },
    required_domains: { type: 'array', items: { type: 'string' } },
    coverage: { type: 'array' },
    seats_total: { type: 'number' },
    roster_seats: { type: 'number' },
    bespoke_seats: { type: 'number' },
    bespoke_slots: { type: 'array' },
    panel: { type: 'array' },
  },
}
const PERSONA_SCHEMA = {
  type: 'object',
  required: ['identity', 'worldview', 'voice', 'narrative'],
  properties: {
    identity: { type: 'object' },
    backstory: { type: 'string' },
    worldview: { type: 'object' },
    voice: { type: 'object' },
    messy_details: { type: 'string' },
    narrative: { type: 'string' },
    stat_lint_check: { type: 'string' },
    stat_lint_issues: { type: 'array' },
  },
}
const TAKE_SCHEMA = {
  type: 'object', required: ['take', 'the_move'],
  properties: { take: { type: 'string' }, signature_angle: { type: 'string' }, the_move: { type: 'string' } },
}
const RESP_SCHEMA = {
  type: 'object', required: ['response'],
  properties: { response: { type: 'string' }, build_on: { type: 'string' }, challenge: { type: 'string' },
    cross_pollinate: { type: 'string' }, revised_move: { type: 'string' } },
}
const CONVERGE_SCHEMA = {
  type: 'object', required: ['crux', 'net_new_principle'],
  properties: { crux: { type: 'string' }, net_new_principle: { type: 'string' },
    forks: { type: 'array', items: { type: 'string' } }, synthesis_direction: { type: 'string' } },
}
const ROADMAP_SCHEMA = {
  type: 'object',
  required: ['panel', 'crux', 'net_new_principle', 'roadmap', 'composition_ledger'],
  properties: {
    panel: { type: 'string' },
    crux: { type: 'string' },
    net_new_principle: { type: 'string' },
    forks: { type: 'array', items: { type: 'string' } },
    roadmap: { type: 'string' },
    composition_ledger: { type: 'string' },
    next_moves: { type: 'string' },
    blind_spots: { type: 'string' },
  },
}

function bash(cmd) {
  return `Run exactly this and output ONLY the raw JSON it prints (no prose, no fences):\ncd "${ROOT}" && ${cmd}`
}
function divergePrompt(m, task) {
  if (m.is_user) {
    return `You are **Farrice's own lens** (taste + alignment + Anti-Guru filter; inductive cross-domain pattern-thinker).\n\n## Task\n${task}\n\nGive the take only YOU would: where does the obvious expert move feel performative/misaligned? What cross-domain pattern (gaming, spirituality, systems) reframes this? What makes it feel REAL, not just optimized?\nReturn JSON {take, signature_angle, the_move} — the_move = your single sharpest contribution.`
  }
  const bespoke = m.bespoke ? ` [Composite Synthesis: ${m.domain_needed}]` : ''
  return `You are **${m.name}**${bespoke}.\n${m.bespoke ? `First READ your full persona document and EMBODY it completely — worldview, heuristics, voice, contradictions: ${m.persona_file}\n\n` : `Your method: ${m.core_method}\nYour lens: ${m.lens}\n\n`}## Task\n${task}\n\nGive YOUR distinctive take — the angle only you, through your method, would see. Be unmistakably yourself, not comprehensive. If you'd lean on a fact/number, ground it (\`python3 execution/research.py "<q>" --depth quick\`) or flag it as an assumption.\nReturn JSON {take, signature_angle, the_move} where the_move is your single sharpest, most STEALABLE contribution.`
}

// ── Scope (extract required domains) ──────────────────────────────────────
phase('Scope')
const domains = SUPPLIED_DOMAINS.length > 0 ? SUPPLIED_DOMAINS :
  await agent(
    `Extract 2–4 required critical domains from this task: "${TASK}". Return JSON {domains: ["domain1", "domain2", ...]} — domains are single keywords or two-word phrases, lowercase.`,
    { label: 'scope-domains', phase: 'Scope', model: 'sonnet', effort: 'low' }
  ).then(r => (r && r.domains) || [TASK])
log(`Scope: ${domains.length} required domains — ${domains.join(', ')}`)

// ── Cast (panel_cast.py: hybrid roster + bespoke) ──────────────────────────
phase('Cast')
const plan = await agent(
  bash(`python3 execution/panel_cast.py ${JSON.stringify(TASK)} --domains "${domains.join(',')}" --mode ${JSON.stringify(MODE)}`),
  { label: 'cast', phase: 'Cast', schema: PANEL_SCHEMA, model: 'sonnet', effort: 'low' }
)
const panel = (plan && plan.panel) || []
const bespokeSlots = (plan && plan.bespoke_slots) || []
const coverage = (plan && plan.coverage) || []
const requiredDomains = (plan && plan.required_domains) || domains
log(`Cast: ${plan.roster_seats} roster seats, ${plan.bespoke_seats} bespoke slots; coverage: ${coverage.map(c => `${c.domain}=${c.status}`).join(', ')}`)

// ── Forge (synthesize bespoke personas; agent writes file + runs the REAL lint) ─
// The lint verdict must come from execution/persona_stat_lint.py (deterministic),
// never from the model grading itself (AI-memory-dependent observability is banned).
phase('Forge')
const FORGE_SCHEMA = {
  type: 'object', required: ['name', 'persona_file', 'lint_verdict'],
  properties: { name: { type: 'string' }, persona_file: { type: 'string' },
    lint_verdict: { type: 'string' }, signature_methodology: { type: 'string' } },
}
const panelDir = `${ROOT}/.tmp/assemble/${SLUG}`
const bespokePersonas = {} // keyed by domain_needed so each slot gets ITS persona
const forgedList = (await parallel(
  bespokeSlots.map((slot) => () =>
    agent(
      `Synthesize a COMPOSITE PERSONA for an expert panel seat.\n\nDomain needed: ${slot.domain_needed}\nWhy the roster is thin: ${slot.why_thin}\nPanel task: ${TASK}\n\nRead ${ROOT}/skills/expert-assembly-os/references/persona-synthesis-prompt.md and follow its contract: identity foundation, backstory with contradictions/struggles, 3-5 worldview convictions with operational implications, voice DNA, 3-5 operational heuristics, NAMED signature methodology, then a 500-1000 word narrative. Constraints: NO fabricated statistics (%, $, millions, tenure-at-named-company claims, real company names, attributions). The literal words "composite persona" must appear in the opening line.\n\nSide effects (you have tools — do these yourself):\n1. mkdir -p ${panelDir}/personas\n2. Write the complete persona document to ${panelDir}/personas/<name-slug>.md\n3. Run: python3 ${ROOT}/execution/persona_stat_lint.py <that file>\n4. If FLAG: fix the flagged lines IN THE FILE and re-run the lint (max 2 retries; after that strip credentials to methodology-only until it passes).\n5. Return JSON {name, persona_file (absolute path), lint_verdict (the lint's FINAL printed verdict — relay it exactly), signature_methodology}.`,
      { label: `forge:${slot.domain_needed}`, phase: 'Forge', schema: FORGE_SCHEMA, model: 'sonnet' }
    ).then((r) => (r ? { domain_needed: slot.domain_needed, slot_reason: slot.why_thin, ...r } : null))
  )
)).filter(Boolean)
for (const f of forgedList) bespokePersonas[f.domain_needed] = f
const unlinted = forgedList.filter((f) => f.lint_verdict !== 'PASS')
if (unlinted.length) log(`⚠ ${unlinted.length} persona(s) closed without lint PASS — flagged in outcome`)
log(`Forge complete: ${forgedList.length} bespoke personas synthesized: ${forgedList.map(f => f.name).join(', ') || 'none'}`)

// ── Merge panel: each bespoke seat gets ITS OWN persona (matched by domain) ──
const fullPanel = panel.map((m) => {
  if (m.bespoke) {
    const personaData = bespokePersonas[m.domain_needed]
    if (personaData) {
      return {
        ...m,
        name: personaData.name,
        core_method: personaData.signature_methodology || m.core_method,
        lint_verdict: personaData.lint_verdict,
        persona_file: personaData.persona_file, // absolute; written at Forge time
      }
    }
  }
  return m
})
const rosterMembers = fullPanel.filter(m => !m.bespoke)
const bespokeMembers = fullPanel.filter(m => m.bespoke)
log(`Panel finalized: ${rosterMembers.length} roster + ${bespokeMembers.length} bespoke`)

// ── Diverge (parallel independent takes) ─────────────────────────────────
phase('Diverge')
const takes = await parallel(
  fullPanel.map((m) => () =>
    agent(divergePrompt(m, TASK), { label: m.name, phase: 'Diverge', schema: TAKE_SCHEMA, model: 'sonnet' })
      .then((r) => (r ? {
        name: m.name,
        bespoke: m.bespoke,
        domain: m.covers_domain || m.domain_needed || 'composite',
        genius_path: m.genius_path,
        persona_file: m.persona_file,
        ...r
      } : null))
  )
)
const valid = takes.filter(Boolean)
log(`Diverge: ${valid.length}/${fullPanel.length} takes`)

// ── Deliberate — Round A: cross-talk, Round B: converge ───────────────────
phase('Deliberate')
const otherTakes = (self) => valid.filter((t) => t.name !== self).map((t) => `**${t.name}**: ${t.take} (move: ${t.the_move})`).join('\n')
const roundA = await parallel(
  valid.map((m) => () =>
    agent(
      (m.bespoke && m.persona_file ? `First re-read your persona document and stay fully in character: ${m.persona_file}\n\n`
        : (m.genius_path ? `First read your genius file for voice + signature moves: ${ROOT}/${m.genius_path}\n\n` : '')) +
        `You are **${m.name}** in panel deliberation on: ${TASK}\n\nYour own opening move: ${m.the_move}\n\nThe OTHER panel members said:\n${otherTakes(m.name)}\n\nNow DELIBERATE — respond as yourself: where do you BUILD on someone, where do you CHALLENGE (name the real disagreement, don't smooth it over), and where do two of these ideas CROSS-POLLINATE into something none of you said alone? Then give your revised move if it changed.\nReturn JSON {response, build_on, challenge, cross_pollinate, revised_move}.`,
      { label: `deliberate:${m.name}`, phase: 'Deliberate', schema: RESP_SCHEMA, model: 'sonnet' }
    ).then((r) => (r ? { name: m.name, ...r } : null))
  )
)
const deliberation = roundA.filter(Boolean)
const converge = await agent(
  `You are the panel facilitator. The expert panel deliberated on: ${TASK}\n\nResponses:\n${deliberation.map((d) => `### ${d.name}\nbuilds: ${d.build_on}\nchallenges: ${d.challenge}\ncross-pollinates: ${d.cross_pollinate}`).join('\n\n')}\n\nConverge — but PRESERVE real disagreement (never blend to mush). Return JSON {crux (the one real tension that matters), net_new_principle (the insight that emerged ONLY from the combination — what no single member said), forks (genuine either/or choices for Farrice to decide), synthesis_direction}.`,
  { label: 'converge', phase: 'Deliberate', schema: CONVERGE_SCHEMA }
)
log(`Deliberated: net-new principle surfaced; ${(converge.forks || []).length} forks for decision`)

// ── Synthesize (roadmap per schema + outcome) ─────────────────────────────
phase('Synthesize')
const outcome = await agent(
  `Synthesize the panel's work into a DECISION-GRADE expert assembly roadmap for: ${TASK}\n\n` +
    `Crux: ${converge.crux}\nNet-new principle: ${converge.net_new_principle}\nDirection: ${converge.synthesis_direction}\n` +
    `Forks for Farrice: ${(converge.forks || []).join(' | ')}\n\nPanel moves:\n${valid.map((t) => `- ${t.name}: ${t.the_move}`).join('\n')}\n\n` +
    `Write a COMPLETE roadmap per this schema (all sections non-empty, no placeholders):\n\n` +
    `## 1. PANEL (Labeled Roster vs Bespoke)\n` +
    `List each panelist with domain and methodology. Mark all synthetic personas [Bespoke Composite]. Include Farrice as Function Owner.\n\n` +
    `## 2. CLAIMS GROUNDING TABLE\n` +
    `If the deliverable contains factual claims (statistics, market data, methodology attributions): table with | Claim | Source | Confidence |. If no claims, write "No factual claims in synthesis."\n\n` +
    `## 3. SYNTHESIS\n` +
    `**The Crux** (one real tension): [paragraph]\n` +
    `**Net-New Principle** (emerged from combination): [paragraph]\n` +
    `**Forks for Farrice** (genuine either/or): - Fork A [choice detail] — Tradeoff: [gains/sacrifices]\n\n` +
    `## 4. ROADMAP — Three Horizons\n` +
    `### OPERATIONAL (0–30 days)\n` +
    `**Move 1: [Title]** - Owner: [role] - Action: [concrete] - Success criteria: [observable, not 'improve X'] - Dependencies: [blockers]\n` +
    `[Additional moves]\n\n` +
    `### TACTICAL (1–6 months)\n` +
    `**Deliverable 1: [Title]** - Owner: [team] - Scope: [what it covers/excludes] - Success criteria: [metrics/outcomes] - Dependencies: [prereqs]\n` +
    `[Additional deliverables]\n\n` +
    `### STRATEGIC (6–12 months)\n` +
    `**Initiative: [Thesis]** - North Star: [market/org change] - Phases: [high-level sequence] - Leading indicator: [what to watch] - Owner: [who drives]\n\n` +
    `## 5. COMPOSITION LEDGER\n` +
    `Table: | Seat | Expert | Filled By | Coverage | Notes |\n` +
    `Show why each panelist was seated (domain coverage, bespoke reason, complementary lens).\n\n` +
    `## 6. NEXT MOVES TOGETHER\n` +
    `**What We Built Together**: [paragraph on outcome]\n` +
    `**What Comes Next (Our Advice)**: [3+ specific points]\n` +
    `**What We Didn't Explore**: [risks/domains panel ran out of time for]\n` +
    `**The Blind Spot We Flagged**: [meta-awareness of what panel might be missing]\n\n` +
    `Rules: Show>Tell, mechanics not narrative, every word earns keep. No fabricated numbers. If you state a fact, ground it or flag as assumption. Write to ${ROOT}/.tmp/assemble/${SLUG}/outcome.md (create dirs), then run \`python3 execution/grounding_guard.py ${ROOT}/.tmp/assemble/${SLUG}/outcome.md --task-type Strategy\` and report its verdict. Return the full roadmap text + the grounding verdict line.`,
  { label: 'synthesize', phase: 'Synthesize', schema: ROADMAP_SCHEMA }
)
log(`Synthesized: roadmap emitted with ${(converge.forks || []).length} forks`)

// ── Learn — "How the Masters Thought" digest ─────────────────────────────
phase('Learn')
const learn = await agent(
  `Produce the LEARNING ARTIFACT. Calibrate to Farrice: Show>Tell, mechanism-not-narrative, dense, no filler.\n\n` +
    `Panel on "${TASK}". Members + their moves:\n${valid.map((t) => `- **${t.name}** ${t.bespoke ? '[Composite]' : '[Roster]'}: signature_angle="${t.signature_angle}", move="${t.the_move}"`).join('\n')}\n\n` +
    `Deliberation cross-pollination:\n${deliberation.map((d) => `- ${d.name} cross-pollinated: ${d.cross_pollinate}`).join('\n')}\n\nNet-new principle: ${converge.net_new_principle}\n\n` +
    `Write a digest:\n` +
    `## How the Masters Thought — ${TASK}\n` +
    `### The Moves (one per expert: SIGNATURE MOVE shown in action + 'the move you can steal' as a reusable rule)\n` +
    `### The Collision (exact moment two domains met; name both + the spark)\n` +
    `### The Principle (transferable mental model Farrice can apply elsewhere)\n` +
    `### Your Rep (one prompt: different problem where Farrice tries this principle himself)\n\n` +
    `STEP 1: run \`date +%Y-%m-%d\` to get today's date.\n` +
    `STEP 2: write the digest to ${ROOT}/knowledge/assembly-sessions/<date>-${SLUG}.md (create dir).\n` +
    `STEP 3: APPEND one distilled line to ${ROOT}/knowledge/assembly-rubric.md in the form: "- **<principle name>** (<date>, ${SLUG}): <one-line model> — from <domain A> × <domain B>." Read-then-append; never overwrite existing lines.\n` +
    `Return the digest text + confirm both file paths written.`,
  { label: 'learn', phase: 'Learn', model: 'sonnet' }
)
log(`Learning digest written`)

// ── Close — persist panel, pin for /panel-sync ──────────────────────────────
phase('Close')
const panelJSON = {
  task: TASK,
  domains: requiredDomains,
  mode: MODE,
  slug: SLUG,
  panel: fullPanel.map(m => ({
    name: m.name,
    bespoke: m.bespoke,
    domain: m.covers_domain || m.domain_needed,
    slot: m.slot,
    core_method: m.core_method || null,
    covers_domain: m.covers_domain || null,
    genius_path: m.genius_path || null,
    is_user: m.is_user || false,
  })),
  coverage: coverage.map(c => ({ domain: c.domain, status: c.status, best_card: c.best_card })),
  seats_total: plan.seats_total,
  roster_seats: plan.roster_seats,
  bespoke_seats: plan.bespoke_seats,
  // timestamp stamped by the close-persist agent via `date` — Date.now()/new Date()
  // are unavailable in Workflow scripts (they break resume).
  synthesized_at: 'STAMP_WITH_DATE_CMD',
}

// Write panel.json (personas were already written to disk at Forge time).
await agent(
  `Persist the panel metadata.\n\n` +
    `STEP 1: Run \`date -u +%Y-%m-%dT%H:%M:%SZ\` and substitute the result for "STAMP_WITH_DATE_CMD" in the JSON below.\n` +
    `STEP 2: Write the JSON to ${panelDir}/panel.json (dir exists from Forge):\n${JSON.stringify(panelJSON, null, 2)}\n\n` +
    `STEP 3: Run \`ls ${panelDir}/personas/\` and confirm each bespoke persona file exists.\n` +
    `Return JSON {panel_json_written: true, persona_files_found: <count>}.`,
  { label: 'close-persist', phase: 'Close', model: 'sonnet', effort: 'low' }
)

// Pin session for /panel-sync
await agent(
  `Pin this panel session so /panel-sync can reload it.\n\n` +
    `Write to ${ROOT}/.agent/handoffs/assemble-${SLUG}.md:\n\n` +
    `# Panel Session — ${TASK}\n\n` +
    `**Date**: [today]\n` +
    `**Slug**: ${SLUG}\n` +
    `**Panel Size**: ${plan.seats_total} (${plan.roster_seats} roster, ${plan.bespoke_seats} bespoke)\n` +
    `**Domains**: ${requiredDomains.join(', ')}\n\n` +
    `## Panelists\n` +
    `${fullPanel.map(m => `- **${m.name}** [${m.covers_domain || m.domain_needed}] — ${m.bespoke ? 'Bespoke Composite' : 'Roster'}`).join('\n')}\n\n` +
    `## Net-New Principle\n` +
    `${converge.net_new_principle}\n\n` +
    `## Session Files\n` +
    `- Panel metadata: ${panelDir}/panel.json\n` +
    `- Personas: ${panelDir}/personas/*.md\n` +
    `- Outcome: ${panelDir}/outcome.md\n` +
    `- Learning: knowledge/assembly-sessions/*-${SLUG}.md\n\n` +
    `## Resume This Panel\n` +
    `Run \`/panel-sync ${SLUG}\` to reload and reconvene the same voices.\n\n` +
    `THEN register it in the durable handoff store so /resume can find it by thread: run \`python3 ${ROOT}/execution/handoff_store.py save ${ROOT}/.agent/handoffs/assemble-${SLUG}.md --thread assemble-${SLUG} --pin --hint "Expert Assembly panel: ${TASK.replace(/"/g, "'").slice(0, 90)}" --overwrite\` and report its output.`,
  { label: 'close-pin', phase: 'Close', model: 'sonnet', effort: 'low' }
)

log(`Panel pinned to .agent/handoffs/assemble-${SLUG}.md`)

return {
  task: TASK,
  domains: requiredDomains,
  mode: MODE,
  slug: SLUG,
  convened: fullPanel.length,
  panel_composition: {
    roster_seats: rosterMembers.length,
    bespoke_seats: bespokeMembers.length,
    names: fullPanel.map(m => m.name),
  },
  coverage_summary: coverage.map(c => `${c.domain}=${c.status}`).join('; '),
  net_new_principle: converge.net_new_principle,
  forks: converge.forks || [],
  crux: converge.crux,
  synthesis_outcome: outcome,
  learning_digest: learn,
  session_pin: `.agent/handoffs/assemble-${SLUG}.md`,
  panel_dir: panelDir,
}
