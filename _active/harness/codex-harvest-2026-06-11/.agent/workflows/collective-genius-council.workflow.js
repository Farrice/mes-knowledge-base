export const meta = {
  name: 'collective-genius-council',
  description: 'A reliable multi-expert orchestrator for ANY creative/intelligence work. Convene a deliberately diverse cross-domain council (+ Farrice) → divergent takes → select the most complementary inner council → 2 rounds of genuine DELIBERATION (cross-talk, genius-loaded) → synthesize an outcome none could reach alone → emit a "How the Masters Thought" learning digest + append to the growing rubric. Holds the grounding floor; $0 incremental. The presets /council /roundtable /strike /campaign /deploy front this via args.mode.',
  phases: [
    { title: 'Convene' },
    { title: 'Diverge' },
    { title: 'Inner-Council' },
    { title: 'Deliberate' },
    { title: 'Synthesize' },
    { title: 'Learn' },
  ],
}

let _A = args
if (typeof _A === 'string') { try { _A = JSON.parse(_A) } catch (e) { _A = {} } }
const TASK = (_A && _A.task) || 'Design a premium offer + launch narrative for an invisible-expert coaching brand'
const MODE = (_A && _A.mode) || 'tight'
const ROOT = '/Users/farricecain/Codex Antigravity'
const SLUG = TASK.toLowerCase().replace(/[^a-z0-9]+/g, '-').slice(0, 48).replace(/^-+|-+$/g, '')

const ROSTER_SCHEMA = {
  type: 'object',
  required: ['roster', 'inner_council_size'],
  properties: {
    inner_council_size: { type: 'number' },
    wildcards: { type: 'array', items: { type: 'string' } },
    roster: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' }, domain_group: { type: 'string' },
          core_method: { type: 'string' }, lens: { type: 'string' },
          genius_path: { type: ['string', 'null'] }, wildcard: { type: 'boolean' }, is_user: { type: 'boolean' },
        },
      },
    },
  },
}
const TAKE_SCHEMA = {
  type: 'object', required: ['take', 'the_move'],
  properties: { take: { type: 'string' }, signature_angle: { type: 'string' }, the_move: { type: 'string' } },
}
const INNER_SCHEMA = {
  type: 'object', required: ['inner'],
  properties: { inner: { type: 'array', items: { type: 'object', required: ['name', 'why_seated'],
    properties: { name: { type: 'string' }, why_seated: { type: 'string' } } } } },
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
    return `You are **Farrice's own lens** (taste + alignment + Anti-Guru filter; inductive cross-domain pattern-thinker).\n\n## Task\n${task}\n\nGive the take only YOU would: where does the obvious expert move feel performative/misaligned? What cross-domain pattern (gaming, spirituality, systems) reframes this? What makes it feel REAL, not just optimized?\nReturn JSON {take, signature_angle, the_move} — the_move = your single sharpest contribution.`
  }
  const wild = m.wildcard ? ' (you are the WILDCARD — bring your outsider lens precisely BECAUSE it does not obviously fit this problem)' : ''
  return `You are **${m.name}** — ${m.domain_group}${wild}.\nYour method: ${m.core_method}\nYour lens: ${m.lens}\n\n## Task\n${task}\n\nGive YOUR distinctive take — the angle only you, through your method, would see. Be unmistakably yourself, not comprehensive. If you'd lean on a fact/number, ground it (\`python3 execution/research.py "<q>" --depth quick\`) or flag it as an assumption.\nReturn JSON {take, signature_angle, the_move} where the_move is your single sharpest, most STEALABLE contribution.`
}

// ── Convene ──────────────────────────────────────────────────────────────
phase('Convene')
const plan = await agent(
  bash(`python3 execution/council_cast.py ${JSON.stringify(TASK)} --mode ${JSON.stringify(MODE)}`),
  { label: 'convene', phase: 'Convene', schema: ROSTER_SCHEMA }
)
const roster = (plan && plan.roster) || []
const innerSize = (plan && plan.inner_council_size) || 4
log(`Convened ${roster.length} voices across ${new Set(roster.map(r => r.domain_group)).size} domains; wildcards: ${(plan.wildcards || []).join(', ') || 'none'}`)

// ── Diverge (parallel independent takes) ─────────────────────────────────
phase('Diverge')
const takes = await parallel(
  roster.map((m) => () =>
    agent(divergePrompt(m, TASK), { label: m.name, phase: 'Diverge', schema: TAKE_SCHEMA })
      .then((r) => (r ? { name: m.name, domain: m.domain_group, wildcard: m.wildcard, genius_path: m.genius_path, ...r } : null))
  )
)
const valid = takes.filter(Boolean)
log(`Diverge: ${valid.length}/${roster.length} takes`)
const takesDigest = valid.map((t) => `- **${t.name}** [${t.domain}]: ${t.the_move}`).join('\n')

// ── Inner-Council select (most complementary, max cross-pollination) ─────
phase('Inner-Council')
const sel = await agent(
  `From these ${valid.length} expert takes on the task "${TASK}", select the ${innerSize} most COMPLEMENTARY voices for a deliberating inner council — maximize cross-pollination and productive tension, not just the "best" takes. Favor seating at least one wildcard/outsider if it sharpens the collision.\n\nTakes:\n${valid.map((t) => `### ${t.name} [${t.domain}]\nangle: ${t.signature_angle}\nmove: ${t.the_move}`).join('\n\n')}\n\nReturn JSON {inner:[{name, why_seated}]} — why_seated = the specific tension/complement each brings.`,
  { label: 'select-inner', phase: 'Inner-Council', schema: INNER_SCHEMA }
)
// Robust name match (case-insensitive, strip "(you)"/punctuation, substring either way) —
// the selector's strings rarely match take names byte-for-byte.
const norm = (s) => (s || '').toLowerCase().replace(/\(you\)/g, '').replace(/[^a-z0-9 ]/g, '').trim()
const innerNorm = ((sel && sel.inner) || []).map((i) => norm(i.name)).filter(Boolean)
let inner = valid.filter((t) => {
  const tn = norm(t.name)
  return innerNorm.some((n) => n === tn || (n && (tn.includes(n) || n.includes(tn))))
})
// Fallback: if matching produced too few, take the top valid takes so DELIBERATION
// always fires (its absence was the whole bug). Prefer including a wildcard.
if (inner.length < Math.min(3, valid.length)) {
  const picked = new Set(inner.map((t) => t.name))
  for (const t of valid) {
    if (inner.length >= innerSize) break
    if (!picked.has(t.name)) { inner.push(t); picked.add(t.name) }
  }
}
inner = inner.slice(0, innerSize)
const seatReasons = {}
;((sel && sel.inner) || []).forEach((i) => { seatReasons[i.name] = i.why_seated })
log(`Inner council (${inner.length}): ${inner.map((i) => i.name).join(', ')}`)

// ── Deliberate — Round A: cross-talk (genius-loaded), Round B: converge ──
phase('Deliberate')
const otherTakes = (self) => inner.filter((t) => t.name !== self).map((t) => `**${t.name}**: ${t.take} (move: ${t.the_move})`).join('\n')
const roundA = await parallel(
  inner.map((m) => () =>
    agent(
      (m.genius_path ? `First read your genius file for voice + signature moves: ${ROOT}/${m.genius_path}\n\n` : '') +
        `You are **${m.name}** in council deliberation on: ${TASK}\n\nYour own opening move: ${m.the_move}\n\nThe OTHER council members said:\n${otherTakes(m.name)}\n\nNow DELIBERATE — respond as yourself: where do you BUILD on someone, where do you CHALLENGE (name the real disagreement, don't smooth it over), and where do two of these ideas CROSS-POLLINATE into something none of you said alone? Then give your revised move if it changed.\nReturn JSON {response, build_on, challenge, cross_pollinate, revised_move}.`,
      { label: `deliberate:${m.name}`, phase: 'Deliberate', schema: RESP_SCHEMA }
    ).then((r) => (r ? { name: m.name, ...r } : null))
  )
)
const deliberation = roundA.filter(Boolean)
const converge = await agent(
  `You are the council facilitator. The inner council deliberated on: ${TASK}\n\nResponses:\n${deliberation.map((d) => `### ${d.name}\nbuilds: ${d.build_on}\nchallenges: ${d.challenge}\ncross-pollinates: ${d.cross_pollinate}`).join('\n\n')}\n\nConverge — but PRESERVE real disagreement (never blend to mush). Return JSON {crux (the one real tension that matters), net_new_principle (the insight that emerged ONLY from the combination — what no single member said), forks (genuine either/or choices for Farrice to decide), synthesis_direction}.`,
  { label: 'converge', phase: 'Deliberate', schema: CONVERGE_SCHEMA }
)
log(`Deliberated: net-new principle surfaced; ${(converge.forks || []).length} forks for your decision`)

// ── Synthesize (creative-partner outcome + floor check) ──────────────────
phase('Synthesize')
const synthesis = await agent(
  `Synthesize the council's work into a DECISION-GRADE outcome for: ${TASK}\n\n` +
    `Crux: ${converge.crux}\nNet-new principle: ${converge.net_new_principle}\nDirection: ${converge.synthesis_direction}\n` +
    `Forks for Farrice: ${(converge.forks || []).join(' | ')}\n\nInner-council moves:\n${inner.map((t) => `- ${t.name}: ${t.the_move}`).join('\n')}\n\n` +
    `Write, dense and concrete (Farrice's calibration: Show>Tell, mechanics-not-narrative, every word earns its keep):\n` +
    `1. THE OUTCOME — the actual recommendation/deliverable that exceeds any single voice, built on the net-new principle.\n` +
    `2. WHY IT'S MORE THAN THE PARTS — name the cross-pollination that produced it.\n` +
    `3. FORKS FOR YOU — the genuine choices only Farrice should make, each with the tradeoff.\n` +
    `4. NEXT MOVES WE MAKE TOGETHER — concrete, so this is a partner moving forward, not a one-shot report.\n` +
    `If you state any fact/number, it must be grounded or flagged as an assumption — do not fabricate.\n` +
    `Then write the full text to ${ROOT}/.tmp/council/${SLUG}-outcome.md (create dirs), and run ` +
    `\`python3 execution/grounding_guard.py ${ROOT}/.tmp/council/${SLUG}-outcome.md --task-type Strategy\` and report its verdict line. Return the outcome text + the grounding verdict.`,
  { label: 'synthesize', phase: 'Synthesize' }
)

// ── Learn — "How the Masters Thought" digest + growing rubric ────────────
phase('Learn')
const learn = await agent(
  `Produce the LEARNING ARTIFACT — this is how Farrice levels up by watching the masters work. Calibrate to him: Show>Tell, mechanism-not-narrative, dense, no filler.\n\n` +
    `Council on "${TASK}". Members + their moves:\n${inner.map((t) => `- **${t.name}** [${t.domain}]: signature_angle="${t.signature_angle}", move="${t.the_move}"`).join('\n')}\n\n` +
    `Deliberation cross-pollination:\n${deliberation.map((d) => `- ${d.name} cross-pollinated: ${d.cross_pollinate}`).join('\n')}\n\nNet-new principle: ${converge.net_new_principle}\n\n` +
    `Write a digest with these sections:\n` +
    `## How the Masters Thought — ${TASK}\n` +
    `### The Moves (one per expert: the SIGNATURE MOVE shown in action + 'the move you can steal' as a reusable rule)\n` +
    `### The Collision (the exact moment two domains met and produced the net-new principle — name both domains + the spark)\n` +
    `### The Principle (the transferable mental model, stated so Farrice can apply it to unrelated problems)\n` +
    `### Your Rep (one prompt: a different problem where Farrice should try this principle himself)\n\n` +
    `STEP 1: run \`date +%Y-%m-%d\` to get today's date.\n` +
    `STEP 2: write the digest to ${ROOT}/knowledge/council-sessions/<date>-${SLUG}.md (create dir).\n` +
    `STEP 3: APPEND one distilled line to ${ROOT}/knowledge/council-rubric.md (create it with an "# Council Rubric — Farrice's Growing Mental Models" header if absent) in the form: "- **<principle name>** (<date>, ${SLUG}): <one-line mental model> — from <domain A> × <domain B>." Read-then-append; never overwrite existing lines.\n` +
    `Return the digest text + confirm both file paths written.`,
  { label: 'learn', phase: 'Learn' }
)

return {
  task: TASK,
  mode: MODE,
  convened: roster.length,
  inner_council: inner.map((i) => i.name),
  wildcards: plan.wildcards || [],
  net_new_principle: converge.net_new_principle,
  forks: converge.forks || [],
  synthesis,
  learning_digest: learn,
}
