export const meta = {
  name: 'bypasser-migration',
  description: 'Surgically migrate the priority research bypassers (HIGH-risk skills + hardcoded-GROUNDED labels + direct-client workflows) onto the unified research engine. One agent per file, MINIMAL edits, preserve structure. READ the file, make the smallest change that closes the gap, report what changed.',
  phases: [{ title: 'Migrate' }],
}

const ROOT = '/Users/farricecain/Google Antigravity'

// Priority bypassers + the surgical fix for each (from research-integrity-audit.md).
const TARGETS = [
  { file: 'skills/market_intelligence/SKILL.md',
    fix: 'This skill markets "live SERP validation / real data" but keyword_auditor.py SERP is MOCKED and there is no source gate. EDIT: add a prominent note near the research/validation step that market/SERP claims MUST be grounded via `python3 execution/research.py "<query>" --depth standard` (which returns a Research Receipt) and that any number not backed by a source URL must be labeled an ESTIMATE. Do NOT claim "real data" unless the engine sourced it. Minimal edit; do not rewrite the skill.' },
  { file: 'skills/consumer-posture-research/SKILL.md',
    fix: 'Says "validate with real-time web search" with no tool binding or source floor. EDIT: bind that validation to `python3 execution/research.py` and require a source floor before any claim is called "research-grounded." Add the one note; preserve the rest.' },
  { file: 'skills/business-intelligence-audit/references/extraction-protocol.md',
    fix: 'Only gate is a manual checkbox ("3 external sources checked"). EDIT: replace/augment that checkbox with an instruction to run the foundation through `python3 execution/research.py` and validate output via `python3 execution/research_quality_gate.py validate <file> --strict`. Minimal edit.' },
  { file: 'skills/bond-halbert-copywriting/SKILL.md',
    fix: 'Description sells "deep market research" but the mechanism is philosophy ("live in the market") with no web tool. EDIT: add a clarifying note that this skill does NOT itself fetch market data — if grounded market claims are needed, run `/copy-engine` ground (or `research.py`) first; do not present its output as "market-researched." Minimal note.' },
  { file: '.agent/workflows/mini-brief.md',
    fix: 'Has HARDCODED "GROUNDED" labels in the template regardless of whether research ran. EDIT: make the GROUNDED/provenance label CONDITIONAL — it may only say GROUNDED if a real `research.py` call + `research_quality_gate.py` pass occurred; otherwise label PROJECTED/UNVERIFIED. Change the template so the label is not a constant.' },
  { file: '.agent/workflows/diandra-growth-sprint.md',
    fix: 'Hardcoded "GROUNDED" even when Perplexity is skipped. EDIT: make GROUNDED conditional on a real research_quality_gate pass; route the research step through `research.py`. Minimal edit to the label logic.' },
  { file: '.agent/workflows/diandra-content-engine.md',
    fix: 'Hardcoded "Research: GROUNDED" label leaning on Recall + ad-hoc Perplexity. EDIT: make the label conditional on a real gate; note research should route through `research.py`. Minimal edit.' },
  { file: '.agent/workflows/generate-brief.md',
    fix: 'Phase 3 calls deep_research_engine.py directly. EDIT: swap the direct `deep_research_engine.py` invocation for `python3 execution/research.py "<query>" --depth deep` (same receipt, honest logging). Keep everything else.' },
  { file: '.agent/workflows/research-landscape.md',
    fix: 'Phase 1 Demand Scan calls deep_research_engine.py directly. EDIT: route the Demand Scan foundation through `python3 execution/research.py --depth standard`. Minimal swap.' },
  { file: '.agent/workflows/research-topic.md',
    fix: 'Foundation Research uses deep_research_client/engine directly. EDIT: replace with `python3 execution/research.py "<query>" --depth deep` (or --max). Keep the rest of the workflow.' },
  { file: '.agent/workflows/grounding-pass.md',
    fix: 'The --research-first path calls deep_research_engine.py directly. EDIT: point --research-first at `python3 execution/research.py`. Minimal swap (purpose is to ADD grounding, so low misrep — just route it through the engine).' },
]

const SCHEMA = {
  type: 'object',
  required: ['file', 'changed', 'summary'],
  properties: {
    file: { type: 'string' },
    changed: { type: 'boolean' },
    summary: { type: 'string' },
    risk_note: { type: 'string' },
  },
}

phase('Migrate')
const results = await parallel(
  TARGETS.map((t) => () =>
    agent(
      `Migrate ONE research bypasser onto the unified engine. File: ${ROOT}/${t.file}\n\n` +
        `## The gap + the surgical fix\n${t.fix}\n\n` +
        `## Rules\n` +
        `- READ the file first. Make the SMALLEST edit that closes the gap. Do NOT rewrite or restructure.\n` +
        `- Preserve the file's voice, frontmatter, and existing content. Add/adjust only what the fix requires.\n` +
        `- The unified engine entrypoint is \`python3 execution/research.py "<query>" --depth quick|standard|deep|max\` (Gemini-first → Perplexity → Tavily bedrock floor, honest Research Receipt, $0 on failure). For deep/max the swarm is \`.agent/workflows/deep-research-swarm.workflow.js\`.\n` +
        `- If after reading you judge the file is already adequately gated or the fix doesn't apply, make NO edit and say so.\n\n` +
        `Return JSON {file, changed (true/false), summary (what you changed or why not), risk_note (anything the user should double-check)}.`,
      { label: t.file.split('/').pop(), phase: 'Migrate', schema: SCHEMA }
    )
  )
)

const out = results.filter(Boolean)
const changed = out.filter((r) => r.changed)
log(`Migration: ${changed.length}/${out.length} files edited`)

return {
  migrated: changed.length,
  total: out.length,
  files: out.map((r) => ({ file: r.file, changed: r.changed, summary: r.summary, risk_note: r.risk_note || '' })),
}
