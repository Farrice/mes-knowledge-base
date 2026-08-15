export const meta = {
  name: 'panel-sync',
  description: 'Reload a pinned expert panel and reconvene for follow-up deliberation. Same roster + bespoke personas, new task or refinement question.',
  phases: [
    { title: 'Discover' },
    { title: 'Load' },
    { title: 'Diverge' },
    { title: 'Deliberate' },
    { title: 'Synthesize' },
    { title: 'Learn' },
    { title: 'Close' },
  ],
}

let _A = args
if (typeof _A === 'string') { try { _A = JSON.parse(_A) } catch (e) { _A = {} } }
const REFINEMENT_TASK = (_A && _A.task) || (_A && _A.refinement) || 'Refine and stress-test the deliberation against objections'
const SUPPLIED_SLUG = (_A && _A.slug) || (_A && _A.session) || null
const ROOT = '/Users/farricecain/Google Antigravity'

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

function bash(cmd) {
  return `Run exactly this and output ONLY the raw JSON it prints (no prose, no fences):\ncd "${ROOT}" && ${cmd}`
}

function divergePrompt(m, task) {
  if (m.is_user) {
    return `You are **Farrice's own lens** (taste + alignment + Anti-Guru filter; inductive cross-domain pattern-thinker).\n\n## Refinement Task\n${task}\n\nGive the take only YOU would: where does the panel's synthesis hold up, where does it crack? What cross-domain pattern (gaming, spirituality, systems) strengthens it? What feels like the right next move?\nReturn JSON {take, signature_angle, the_move} — the_move = your single sharpest contribution to this refinement.`
  }
  const bespoke = m.bespoke ? ` [Composite Synthesis: ${m.domain_needed}]` : ''
  return `You are **${m.name}**${bespoke}.\n${m.bespoke ? `First READ your full persona document and EMBODY it completely — worldview, heuristics, voice, contradictions: ${m.persona_file}\n\n` : `Your method: ${m.core_method}\n\n`}## Refinement Task\n${task}\n\nGive YOUR distinctive take on this refinement. Does your original move still hold? Where would you deepen it, or pivot? Be unmistakably yourself.\nReturn JSON {take, signature_angle, the_move} where the_move is your sharpest contribution to this refinement.`
}

// ── Discover (find the pinned session) ────────────────────────────────────
phase('Discover')
let slug = SUPPLIED_SLUG
if (!slug) {
  // Auto-discover most recent pinned session from .agent/handoffs/
  const discover = await agent(
    bash(`ls -t .agent/handoffs/assemble-*.md 2>/dev/null | head -1 | xargs -I {} basename {} .md | sed 's/^assemble-//'`),
    { label: 'discover-session', phase: 'Discover', model: 'sonnet', effort: 'low' }
  )
  slug = (discover && String(discover).trim()) || null
}
if (!slug) {
  throw new Error('No pinned panel session found. Run /assemble first to create a panel, then /panel-sync to reload it.')
}
log(`Discovered session: ${slug}`)

// ── Load (read panel.json + reload personas) ──────────────────────────────
phase('Load')
const panelDir = `${ROOT}/.tmp/assemble/${slug}`
const panelJSON = await agent(
  bash(`cat "${panelDir}/panel.json"`),
  { label: 'load-panel', phase: 'Load', model: 'sonnet', effort: 'low' }
)
if (!panelJSON || !panelJSON.panel) {
  throw new Error(`Failed to load panel.json from ${panelDir}`)
}
const panel = panelJSON.panel || []
const originalTask = panelJSON.task || 'Unknown task'
log(`Loaded panel: ${panel.length} members on "${originalTask}"`)

// ── Diverge (new takes on refinement task) ────────────────────────────────
phase('Diverge')
const takes = await parallel(
  panel.map((m) => () =>
    agent(divergePrompt(m, REFINEMENT_TASK), { label: m.name, phase: 'Diverge', schema: TAKE_SCHEMA, model: 'sonnet' })
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
log(`Diverge: ${valid.length}/${panel.length} takes on refinement`)

// ── Deliberate — Round A: cross-talk, Round B: converge ───────────────────
phase('Deliberate')
const otherTakes = (self) => valid.filter((t) => t.name !== self).map((t) => `**${t.name}**: ${t.take} (move: ${t.the_move})`).join('\n')
const roundA = await parallel(
  valid.map((m) => () =>
    agent(
      (m.bespoke && m.persona_file ? `First re-read your persona document and stay fully in character: ${m.persona_file}\n\n`
        : (m.genius_path ? `First read your genius file for voice + signature moves: ${ROOT}/${m.genius_path}\n\n` : '')) +
        `You are **${m.name}** in panel refinement on: ${REFINEMENT_TASK}\n\nYour own opening move: ${m.the_move}\n\nThe OTHER panel members said:\n${otherTakes(m.name)}\n\nNow DELIBERATE — respond as yourself: where do you BUILD on someone, where do you CHALLENGE, and where do two of these ideas CROSS-POLLINATE into a refinement? Then give your revised move if it changed.\nReturn JSON {response, build_on, challenge, cross_pollinate, revised_move}.`,
      { label: `deliberate:${m.name}`, phase: 'Deliberate', schema: RESP_SCHEMA, model: 'sonnet' }
    ).then((r) => (r ? { name: m.name, ...r } : null))
  )
)
const deliberation = roundA.filter(Boolean)
const converge = await agent(
  `You are the panel facilitator. The expert panel is REFINING on: ${REFINEMENT_TASK}\n\nOriginal task: ${originalTask}\n\nRefinement Responses:\n${deliberation.map((d) => `### ${d.name}\nbuilds: ${d.build_on}\nchallenges: ${d.challenge}\ncross-pollinates: ${d.cross_pollinate}`).join('\n\n')}\n\nConverge — PRESERVE real disagreement. Return JSON {crux (the one real tension in this refinement), net_new_principle (the insight that emerged ONLY from this round), forks (genuine either/or choices for Farrice), synthesis_direction}.`,
  { label: 'converge-refine', phase: 'Deliberate', schema: CONVERGE_SCHEMA }
)
log(`Deliberated refinement: net-new principle surfaced; ${(converge.forks || []).length} forks for decision`)

// ── Synthesize (refinement outcome) ──────────────────────────────────────────
phase('Synthesize')
const refinementOutcome = await agent(
  `Synthesize the panel's REFINEMENT work.\n\n` +
    `Original task: ${originalTask}\n` +
    `Refinement task: ${REFINEMENT_TASK}\n\n` +
    `Crux: ${converge.crux}\n` +
    `Net-new principle: ${converge.net_new_principle}\n` +
    `Direction: ${converge.synthesis_direction}\n\n` +
    `Refinement moves:\n${valid.map((t) => `- ${t.name}: ${t.the_move}`).join('\n')}\n\n` +
    `Write a concise REFINEMENT SYNTHESIS (under 800 words):\n` +
    `## REFINEMENT SYNTHESIS\n` +
    `**Original Crux**: [one-liner from original panel]\n` +
    `**Refinement Crux**: ${converge.crux}\n` +
    `**How We Deepened It**: [what shifted, what held]\n` +
    `**Net-New Principle**: ${converge.net_new_principle}\n` +
    `**Forks for Next Move**: ${(converge.forks || []).join(' | ')}\n\n` +
    `Return the full refinement synthesis text.`,
  { label: 'synthesize-refine', phase: 'Synthesize', schema: { type: 'object', properties: { synthesis: { type: 'string' } } } }
)
log(`Synthesized refinement`)

// ── Learn (brief refinement digest) ────────────────────────────────────────
phase('Learn')
const learnRefine = await agent(
  `Produce a brief REFINEMENT LEARNING ARTIFACT.\n\n` +
    `Panel on "${originalTask}". Refinement: "${REFINEMENT_TASK}"\n\n` +
    `Members + their refinement moves:\n${valid.map((t) => `- **${t.name}**: ${t.the_move}`).join('\n')}\n\n` +
    `Net-new principle: ${converge.net_new_principle}\n\n` +
    `Write a digest:\n` +
    `## Refinement Digest — ${originalTask}\n` +
    `### How the Panel Deepened It\n` +
    `[What was questioned, what held, what shifted]\n\n` +
    `### The Principle Refined\n` +
    `[Updated mental model after refinement]\n\n` +
    `Write to ${ROOT}/knowledge/assembly-sessions/${slug}-refinement.md.\n` +
    `Return digest text + confirm file path written.`,
  { label: 'learn-refine', phase: 'Learn', model: 'sonnet' }
)
log(`Refinement digest written`)

// ── Close — append to pinned session handoff ────────────────────────────────
phase('Close')
const handoffFile = `${ROOT}/.agent/handoffs/assemble-${slug}.md`
await agent(
  `Append the refinement run to the pinned session handoff.\n\n` +
    `Read ${handoffFile}. Find the line "## Resume This Panel". BEFORE that line, add:\n\n` +
    `## Refinement Run (${originalTask})\n` +
    `**Refinement Task**: ${REFINEMENT_TASK}\n` +
    `**Crux**: ${converge.crux}\n` +
    `**Net-New Principle**: ${converge.net_new_principle}\n` +
    `**Forks**: ${(converge.forks || []).join(' | ')}\n\n` +
    `(Append the full refinement synthesis + digest, THEN the "Resume" line)\n\n` +
    `Rewrite ${handoffFile} with the refinement section inserted. Report success.`,
  { label: 'close-append', phase: 'Close', model: 'sonnet', effort: 'low' }
)

log(`Refinement appended to ${handoffFile}`)

return {
  original_task: originalTask,
  refinement_task: REFINEMENT_TASK,
  slug: slug,
  panel_size: panel.length,
  takes_gathered: valid.length,
  net_new_principle: converge.net_new_principle,
  forks: converge.forks || [],
  crux: converge.crux,
  refinement_synthesis: refinementOutcome,
  learning_digest: learnRefine,
  session_handoff: handoffFile,
}
