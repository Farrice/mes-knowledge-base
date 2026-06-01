export const meta = {
  name: 'teardown-engine-live',
  description: 'Live teardown proof: for each big-name brand, recon their live copy + read the grounded avatar → avatar insight + beating copy + before/after + constructive LinkedIn post',
  phases: [
    { title: 'Teardown', detail: 'per-brand: recon + grounded avatar → beating copy + LinkedIn post' },
  ],
}

// Grounding dossiers are produced live by avatar_manifold_runner.py (real Gemini
// avatar research) at .tmp/copy-engine/teardown-<brand>/ground-dossier.md.
// Each agent grounds its rewrite in that real research + a live recon of the
// brand's actual copy. Ethics: tear down the COPY not the PEOPLE; excerpt +
// transform their copy, never reproduce; constructive triad.
const SKILL = 'skills/luke-iha-avatar-machine'

const brands = args && args.length ? args : [
  { slug: 'teardown-kajabi', brand: 'Kajabi', url: 'https://kajabi.com',
    customer: 'coaches/course-creators/experts monetizing their knowledge online',
    asset: 'cold Facebook/Meta ad' },
  { slug: 'teardown-skool', brand: 'Skool', url: 'https://www.skool.com',
    customer: 'community builders/coaches building a paid community + courses',
    asset: 'landing-page hero (headline + subhead + CTA)' },
  { slug: 'teardown-masterclass', brand: 'MasterClass', url: 'https://www.masterclass.com',
    customer: 'ambitious lifelong learners who want to learn craft from the best but rarely finish',
    asset: 'cold Facebook/Meta ad' },
]

const SCHEMA = {
  type: 'object',
  required: ['brand', 'their_copy_excerpt', 'avatar_insight', 'beating_copy', 'linkedin_post',
             'constructive', 'real_voc_used', 'self_score'],
  properties: {
    brand: { type: 'string' },
    their_copy_excerpt: { type: 'string', description: 'their LIVE headline/value-prop, short excerpt only (≤25 words) — the BEFORE' },
    avatar_insight: { type: 'string', description: 'the core wound / identity-safe angle / Pain-Matrix leverage dimension their copy MISSES — the differentiator, grounded in the dossier' },
    beating_copy: { type: 'string', description: 'the grounded rewrite of the asset — the AFTER (expert DR copy, real VOC, claim-safe)' },
    linkedin_post: { type: 'string', description: 'constructive brandjack post. MUST OPEN WITH A BRIEF SETUP FRAME (1-3 short lines) that tells the reader this is a teardown, by the author, of a brand they know — e.g. "Teardown of the week: <brand>." / "Every week I tear down a brand you know. This week, <brand>." — so the insight lands with context and lends authority (without it, the post reads mid-sentence). Vary the frame construction across brands. Then: What They Got Right → What They Missed (the avatar insight) → the before/after → What This Means For You. No contempt; close on a declaration or reader-stake, never a cheap question.' },
    constructive: { type: 'boolean', description: 'true if it tears down the copy not the people, leads with what they got right' },
    real_voc_used: { type: 'boolean' },
    self_score: { type: 'number', description: '1-10 vs the genius.md rubric + heartbeat' },
  },
}

const results = await pipeline(
  brands,
  (b) => agent(
    `TEARDOWN of ${b.brand} (${b.url}) — for their customer: ${b.customer}.\n\n` +
    `STEP 1 — RECON (capture their LIVE copy): WebFetch ${b.url} (and its pricing/product page) to read ${b.brand}'s ACTUAL current headline, value proposition, and primary CTA. Capture a SHORT verbatim excerpt (≤25 words) for the before. Note the asset type: ${b.asset}.\n\n` +
    `STEP 2 — GROUND THE AVATAR (resilient to the current Gemini outage): Read ${SKILL}/genius.md + ${SKILL}/references/framework-library.md (the frameworks). Then read .tmp/copy-engine/${b.slug}/ground-dossier.md IF it exists — but it may be DEGRADED/[MODELED] (Gemini Deep Research is erroring right now). If it's degraded or thin, DO NOT use modeled language — instead do your OWN live VOC research: WebFetch real customer language from G2 / Trustpilot / Reddit / forum threads / review pages for ${b.brand} (or its category), and use perplexity_ask if available. ${b.brand} is a well-known brand — combine real pulled VOC + your knowledge of it + the manifold frameworks. The differentiator: find the core wound, the identity-safe angle, and the ONE Pain-Matrix leverage dimension ${b.brand}'s live copy fails to touch. Cite real soundbites/URLs where you pulled them.\n\n` +
    `STEP 3 — PRODUCE:\n` +
    `• avatar_insight: the deep customer truth their copy misses (grounded in the dossier — quote real VOC where possible).\n` +
    `• beating_copy: a finished ${b.asset} that out-converts theirs — expert DR voice, grounded in real VOC, every claim safe (no unverifiable stats about ${b.brand} or fake numbers), no AI-tells.\n` +
    `• linkedin_post: a CONSTRUCTIVE teardown post. Lead with "What ${b.brand} got right." Then "What they're missing about their own customer" (the avatar insight). Then the before/after (their excerpt vs your rewrite). End on "What this means for you" + a soft CTA ("want this run on your competitor?"). NEVER mock or call them incompetent — tear down the COPY with respect. Excerpt + transform their copy; never reproduce it at length.\n\n` +
    `STANDARD (this is the bar — a teardown that reads like Luke Iha, not a summary):\n` +
    `• INSIGHT MUST BE A VECTOR, NOT A CLAIM. "They sell X, the customer wants Y" is a claim and it's banned. Instead: NAME the mechanism/trap (2-3 words, visual, emotional — e.g. "the Build Trap," "the Spectator's Surplus") and use reverse causation or a vicious cycle ("the arrow runs backwards"), confirming a suspicion the market already half-holds.\n` +
    `• PROOF BRAIDED, NOT DROPPED. Weave the real VOC quote INTO the claim as its evidence within the same beat, not as a bolted-on citation.\n` +
    `• BANNED STRUCTURAL MOVES (hard fail): max 2 em-dashes total (prefer 0); ZERO "It's not X. It's Y." / "isn't A, it's B" reveal patterns; no twin-sentence aphoristic paragraph endings; no triple-beat anaphora; no "here's the part nobody..." framing; NO cheap-question close ("drop their name below?" is banned) — close on a declaration, a reader-stake, or naming what they feel.\n` +
    `• CROSS-PIECE VARIANCE: vary your open, your mechanic, and your close so this post does NOT share a skeleton with the other two brands' posts.\n` +
    `• CONSTRUCTIVE: lead with genuine credit ("credit where it's due," "to be fair"); tear down the COPY, never the people; no unsourced factual claims about ${b.brand}'s business (revenue/metrics) — speak only about their public copy.\n` +
    `Make it sing: tension, recognition, a heartbeat. It must pass prose_classifier CLEAN and teardown_ethics_gate public PASS.`,
    { label: `teardown:${b.brand}`, phase: 'Teardown', schema: SCHEMA }
  ).then(r => ({ slug: b.slug, ...r })),
)

return results.map(r => ({
  brand: r.brand, slug: r.slug, constructive: r.constructive,
  real_voc_used: r.real_voc_used, self_score: r.self_score,
  avatar_insight: r.avatar_insight,
  their_copy_excerpt: r.their_copy_excerpt,
  beating_copy: r.beating_copy,
  linkedin_post: r.linkedin_post,
}))
