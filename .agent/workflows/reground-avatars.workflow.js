export const meta = {
  name: 'reground-avatars',
  description: 'Re-ground the 26 zero-URL VOC/avatar dossiers flagged by the integrity audit. Each dossier: identify the expert + its unsourced attributed "pain quotes", run a real grounding pass (research.py / Tavily) for that audience\'s actual public VOC, and APPEND an honest Grounding Verification ledger — mark the original quotes [MODELED], add real source-linked VOC where found. Additive only; never rewrites the original.',
  phases: [{ title: 'Scout' }, { title: 'Re-ground' }],
}

const ROOT = '/Users/farricecain/Google Antigravity'
const DIR = 'research_outputs/ai_authority_architect_agents'

const LIST_SCHEMA = {
  type: 'object',
  required: ['dossiers'],
  properties: { dossiers: { type: 'array', items: { type: 'string' } } },
}

const REGROUND_SCHEMA = {
  type: 'object',
  required: ['file', 'appended'],
  properties: {
    file: { type: 'string' },
    expert: { type: 'string' },
    appended: { type: 'boolean' },
    real_sources_found: { type: 'number' },
    modeled_flagged: { type: 'number' },
    headline: { type: 'string' },
  },
}

// ── Scout: enumerate the expert dossiers (exclude the rollup + metadata) ──
phase('Scout')
const listing = await agent(
  `List the avatar dossiers to re-ground. Run exactly and return ONLY the JSON:\n` +
    `cd "${ROOT}" && python3 -c "import glob,os,json; ` +
    `fs=[os.path.basename(f) for f in glob.glob('${DIR}/*.md') if 'final_synthesis' not in f]; ` +
    `print(json.dumps({'dossiers': sorted(fs)}))"`,
  { label: 'scout', phase: 'Scout', schema: LIST_SCHEMA }
)
const dossiers = (listing && listing.dossiers) || []
log(`Scout: ${dossiers.length} expert dossiers to re-ground`)

// ── Re-ground each (parallel; ~16 concurrent, rest queue) ──
phase('Re-ground')
const results = await parallel(
  dossiers.map((fname) => () =>
    agent(
      `Re-ground a zero-URL VOC/avatar dossier. File: ${ROOT}/${DIR}/${fname}\n\n` +
        `## Mission\n` +
        `This dossier mines an audience's pain/voice for an expert persona, but its "quotes" and claims ` +
        `carry NO source URLs — they read as real VOC but are AI-inferred. Ground what you can, flag the rest, APPEND a ledger. ` +
        `Do NOT rewrite or delete the original body.\n\n` +
        `## Steps\n` +
        `1. READ the dossier. Identify (a) the expert/persona and the AUDIENCE it profiles, and (b) the attributed "pain quotes" / verbatim claims that have no source.\n` +
        `2. Run a REAL grounding pass on that audience's actual public voice: ` +
        `\`cd "${ROOT}" && python3 execution/research.py "<the audience> pain points frustrations reddit reviews forums" --depth standard\` ` +
        `(prints a Research Receipt), plus targeted \`tvly search\` / WebSearch on the specific pains. Collect real, source-linked VOC.\n` +
        `3. APPEND to the END of the file a section titled exactly:\n` +
        `   "## ⚠️ Grounding Verification (re-grounded 2026-06-02 via unified research engine)"\n` +
        `   containing: (a) a one-line verdict; (b) "**Original soundbites: [MODELED] — unsourced, AI-inferred. Do not quote as real VOC until matched to a source.**"; ` +
        `(c) a "Real source-linked VOC found" subsection — a markdown list of genuine quotes/pains WITH their URLs (only ones you actually found; never fabricate a URL); ` +
        `(d) a "Re-ground action" line (e.g., 'rebuild via /avatar-machine for full sourced VOC' if thin).\n` +
        `4. Use Edit/Write to APPEND only. Preserve everything above.\n\n` +
        `Return JSON {file, expert, appended, real_sources_found, modeled_flagged, headline}.`,
      { label: fname.replace('.md', ''), phase: 'Re-ground', schema: REGROUND_SCHEMA }
    )
  )
)

const out = results.filter(Boolean)
const totalReal = out.reduce((n, r) => n + (r.real_sources_found || 0), 0)
log(`Re-grounded ${out.filter((r) => r.appended).length}/${out.length} dossiers; ${totalReal} real source-linked VOC found`)

return {
  dossiers: out.length,
  appended: out.filter((r) => r.appended).length,
  total_real_sources: totalReal,
  per_dossier: out.map((r) => ({ file: r.file, expert: r.expert, real: r.real_sources_found, headline: r.headline })),
}
