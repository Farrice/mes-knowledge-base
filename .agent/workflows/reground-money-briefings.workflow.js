export const meta = {
  name: 'reground-money-briefings',
  description: 'Re-ground the HIGH-severity money/decision briefings flagged by the integrity audit. Per briefing: extract the highest-stakes numeric/market claims, verify each via the unified engine + targeted web search, and APPEND an honest Grounding Verification ledger (VERIFIED-with-URL / LIKELY / UNCONFIRMED). Does NOT rewrite the original body — additive honesty only.',
  phases: [{ title: 'Re-ground' }],
}

const ROOT = '/Users/farricecain/Google Antigravity'

const BRIEFINGS = [
  'deliverables/prediction-market-business-briefing.md',
  'deliverables/prediction-market-partner-briefing.md',
  'deliverables/prediction-market-proposal-package.md',
  'research_outputs/prediction-market-arb/00-research-dossier.md',
  'research_outputs/dj-event-matchmaking-research.md',
  'research_outputs/ghostwriting_niche_selection.md',
]

const SCHEMA = {
  type: 'object',
  required: ['file', 'appended', 'claims_checked'],
  properties: {
    file: { type: 'string' },
    appended: { type: 'boolean' },
    claims_checked: { type: 'number' },
    verified: { type: 'number' },
    likely: { type: 'number' },
    unconfirmed: { type: 'number' },
    headline: { type: 'string' }, // one-line verdict on the briefing's trustworthiness
  },
}

phase('Re-ground')
const results = await parallel(
  BRIEFINGS.map((f) => () =>
    agent(
      `Re-ground a HIGH-severity money/decision briefing. File: ${ROOT}/${f}\n\n` +
        `## Mission\n` +
        `This briefing drives a real money/positioning decision but was flagged as grounding-suspect ` +
        `(claims stated as fact with few/zero source URLs). Verify its key claims and APPEND an honest ledger. ` +
        `Do NOT rewrite or delete the original body — additive only.\n\n` +
        `## Steps\n` +
        `1. READ the briefing. Extract the 6-10 HIGHEST-STAKES claims — the specific numbers a decision rests on ` +
        `(market size, growth %, profit figures, named-trader stats, pricing bands, membership counts, etc.).\n` +
        `2. Ground them: run \`cd "${ROOT}" && python3 execution/research.py "<the briefing's core topic + the key metrics>" --depth standard\` ` +
        `for a cited foundation (it prints a Research Receipt). Then targeted \`WebSearch\`/\`WebFetch\` (or \`tvly search\`) ` +
        `on each specific number to find a primary source.\n` +
        `3. Label each claim: **VERIFIED** (real source URL found — include it), **LIKELY** (directionally supported but no exact-figure source), ` +
        `or **UNCONFIRMED** (no source — flag as not-decision-grade). Never fabricate a URL.\n` +
        `4. APPEND to the END of the file a section exactly titled:\n` +
        `   "## ⚠️ Grounding Verification (re-grounded 2026-06-02 via unified research engine)"\n` +
        `   with: a one-line trust verdict, then a markdown table | Claim | Status | Source / Note |, ` +
        `then a short "Decision guidance" line (which claims are safe to act on, which need more work before capital/commitment).\n` +
        `5. Use the Edit/Write tool to append (read the file, add the section at the end). Preserve everything above it.\n\n` +
        `Return JSON {file, appended, claims_checked, verified, likely, unconfirmed, headline}.`,
      { label: f.split('/').pop(), phase: 'Re-ground', schema: SCHEMA }
    )
  )
)

const out = results.filter(Boolean)
const totalChecked = out.reduce((n, r) => n + (r.claims_checked || 0), 0)
const totalUnconfirmed = out.reduce((n, r) => n + (r.unconfirmed || 0), 0)
log(`Re-grounded ${out.filter((r) => r.appended).length}/${out.length} briefings; ${totalChecked} claims checked, ${totalUnconfirmed} UNCONFIRMED`)

return {
  briefings: out.length,
  appended: out.filter((r) => r.appended).length,
  claims_checked: totalChecked,
  unconfirmed: totalUnconfirmed,
  per_briefing: out.map((r) => ({ file: r.file, headline: r.headline, verified: r.verified, unconfirmed: r.unconfirmed })),
}
