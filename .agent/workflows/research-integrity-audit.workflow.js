export const meta = {
  name: 'research-integrity-audit',
  description: 'System-wide research integrity sweep: inventory every research producer/consumer + triage already-produced deliverables for grounding risk (false-PASS era, [MODELED] VOC, unsourced findings). Produces one honest report — trustworthy vs suspect vs now-fixed. READ-ONLY: flags, never edits.',
  phases: [
    { title: 'Inventory' },
    { title: 'Triage' },
    { title: 'Report' },
  ],
}

const ROOT = '/Users/farricecain/Google Antigravity'

const CONSUMER_SCHEMA = {
  type: 'object',
  required: ['consumers'],
  properties: {
    consumers: {
      type: 'array',
      items: {
        type: 'object',
        required: ['file', 'risk'],
        properties: {
          file: { type: 'string' },
          research_path: { type: 'string' },
          bypasses_engine: { type: 'boolean' },
          risk: { type: 'string' }, // none | low | medium | high
          note: { type: 'string' },
        },
      },
    },
  },
}

const TRIAGE_SCHEMA = {
  type: 'object',
  required: ['suspect'],
  properties: {
    suspect: {
      type: 'array',
      items: {
        type: 'object',
        required: ['file', 'reason', 'severity'],
        properties: {
          file: { type: 'string' },
          reason: { type: 'string' },
          severity: { type: 'string' }, // low | medium | high
        },
      },
    },
    scanned: { type: 'number' },
  },
}

// ── Phase: Inventory — who does/uses research, and do they bypass the engine? ──
phase('Inventory')
const inventoryAreas = [
  {
    label: 'workflows',
    prompt:
      `Inventory RESEARCH producers/consumers in ${ROOT}/.agent/workflows/. Use grep/glob (read-only).\n` +
      `Find every workflow .md that does research or consumes research output. For each, identify which research path it uses:\n` +
      `  - "engine" = calls execution/research.py (the unified engine — GOOD)\n` +
      `  - "direct-client" = calls deep_research_client.py / perplexity_client.py / deep_research_engine.py directly\n` +
      `  - "raw-tools" = uses WebSearch/WebFetch/perplexity_ask/tvly ad hoc without the engine\n` +
      `  - "avatar-runner" = calls avatar_manifold_runner.py (GROUND path)\n` +
      `Set bypasses_engine=true if it does research but NOT via research.py. risk: high if it presents research as grounded but bypasses the engine + has no source gate; medium if direct-client; low if engine or trivial; none if not really research.\n` +
      `Search markers: "research.py", "deep_research_client", "perplexity_client", "deep_research_engine", "avatar_manifold_runner", "perplexity_ask", "WebSearch", "tvly", "deep research", "GROUND".\n` +
      `Return JSON {consumers:[{file, research_path, bypasses_engine, risk, note}]}. Cap at the 40 most relevant.`,
  },
  {
    label: 'skills',
    prompt:
      `Inventory RESEARCH-dependent SKILLS in ${ROOT}/skills/. Use grep/glob (read-only).\n` +
      `Find skills whose SKILL.md/workflows reference research or grounding. Classify research_path (engine | direct-client | raw-tools | avatar-runner | none) and bypasses_engine. ` +
      `risk high if the skill's output is presented as grounded fact but it has no real source gate.\n` +
      `Markers: "research", "deep research", "perplexity", "gemini deep", "VOC", "ground", "WebSearch", "tvly", "sources", "citation".\n` +
      `Return JSON {consumers:[{file, research_path, bypasses_engine, risk, note}]}. Cap at 40 most relevant.`,
  },
  {
    label: 'execution',
    prompt:
      `Inventory RESEARCH scripts in ${ROOT}/execution/. Use grep/glob + read key files (read-only).\n` +
      `Find every .py that produces, logs, or gates research. For each note research_path and whether it bypasses the unified engine (research.py). ` +
      `Flag risk high for any that log usage/cost or write findings WITHOUT validating content first (the false-log / unsourced bug class) — but note these were the ones FIXED this session: deep_research_client.py, perplexity_client.py, deep_research_engine.py, research_quality_gate.py, avatar_manifold_runner.py. Confirm whether each still has the risk or is fixed.\n` +
      `Markers: "_log_usage", "estimated_cost", "source_url", "findings.append", "validate_engine_text", "MODELED", "raise_for_status".\n` +
      `Return JSON {consumers:[{file, research_path, bypasses_engine, risk, note}]}.`,
  },
]
const inv = await parallel(
  inventoryAreas.map((a) => () =>
    agent(a.prompt, { label: `inv:${a.label}`, phase: 'Inventory', schema: CONSUMER_SCHEMA })
  )
)
const consumers = []
inv.forEach((r) => { if (r && r.consumers) consumers.push(...r.consumers) })
const bypassers = consumers.filter((c) => c.bypasses_engine && (c.risk === 'high' || c.risk === 'medium'))
log(`Inventory: ${consumers.length} research consumers; ${bypassers.length} bypass the engine at medium/high risk`)

// ── Phase: Triage — which ALREADY-PRODUCED outputs were built on shaky ground? ──
phase('Triage')
const triageAreas = ['deliverables', 'products', 'projects', 'research_outputs', '_active']
const tri = await parallel(
  triageAreas.map((dir) => () =>
    agent(
      `Triage already-produced outputs in ${ROOT}/${dir}/ for GROUNDING RISK. Read-only (grep/glob/read).\n` +
        `Flag a file as grounding-suspect if it shows signs its research foundation was unsound:\n` +
        `  - contains "[MODELED]" placeholder data presented as if real,\n` +
        `  - a ground-status.json with has_modeled=true or rqg_strict_pass=false,\n` +
        `  - market/stat/quote claims with NO source URLs (unsourced findings),\n` +
        `  - provenance tied to "Gemini Deep Research" before 2026-06-01 (the false-PASS / empty-but-logged era),\n` +
        `  - VOC/avatar dossiers with few or zero source-linked soundbites.\n` +
        `Use grep for: "\\[MODELED", "has_modeled", "rqg_strict", "no source", "Gemini Deep Research", "MODELED — replace".\n` +
        `Return JSON {suspect:[{file, reason, severity}], scanned}. severity high = decisions likely built on it. Cap at 30 most important.`,
      { label: `triage:${dir}`, phase: 'Triage', schema: TRIAGE_SCHEMA }
    )
  )
)
const suspect = []
let scanned = 0
tri.forEach((r) => { if (r) { if (r.suspect) suspect.push(...r.suspect); scanned += r.scanned || 0 } })
const highSuspect = suspect.filter((s) => s.severity === 'high')
log(`Triage: scanned ~${scanned} outputs; ${suspect.length} grounding-suspect (${highSuspect.length} high-severity)`)

// ── Phase: Report — one honest map, written to disk ──────────────────────
phase('Report')
const reportData = JSON.stringify({ consumers, bypassers, suspect, highSuspect }, null, 2)
const summary = await agent(
  `Write an honest Research Integrity Audit report to ${ROOT}/research_outputs/research-integrity-audit.md.\n\n` +
    `Use this data (consumers = research producers/consumers; bypassers = those bypassing the unified engine at risk; suspect = already-produced outputs with grounding risk):\n` +
    '```json\n' + reportData + '\n```\n\n' +
    `Structure the report:\n` +
    `# Research Integrity Audit (date it 2026-06-01)\n` +
    `## Verdict — one paragraph: what was broken (false logging, unsourced findings, unenforced [MODELED]), what is now FIXED (the unified engine + honest receipt), and what residual risk remains.\n` +
    `## Now-Fixed (trustworthy going forward) — the engine, the 3 trust-fixes, the routing lock.\n` +
    `## Consumers Still Bypassing the Engine — table of bypassers with risk + the one-line fix (route through research.py).\n` +
    `## Grounding-Suspect Past Work — table of suspect outputs sorted by severity, with WHY and the re-ground action. Be honest but not alarmist; most modeled data was LABELED as modeled.\n` +
    `## Re-Ground Worklist — concrete prioritized next actions.\n\n` +
    `Then output a 5-line executive summary of the verdict.`,
  { label: 'write-report', phase: 'Report' }
)

return {
  consumers_total: consumers.length,
  bypassers: bypassers.length,
  suspect_total: suspect.length,
  high_severity: highSuspect.length,
  report_path: 'research_outputs/research-integrity-audit.md',
  executive_summary: summary,
}
