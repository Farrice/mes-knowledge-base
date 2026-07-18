# PROVENANCE — alex-myatt-creative-engine repair

Anchor → source file + location, for every quote/claim added or re-anchored in this
repair. All quotes verified by direct read of the source file during this session
(2026-07-17). File sizes confirmed with `wc -c` (not `wc -l` — `transcript.txt` is a
single unbroken line, `wc -l` would falsely read as empty/0-byte-equivalent).

| Anchor text (as used in genius.md) | Source file | Verification |
|---|---|---|
| "So, they would put out one with a yellow background..." | `extractions/alex-myatt/transcript.txt` (121,038 bytes) | Direct substring match, offset ~96700 |
| "Meta would classify all of those kinds of ads... under the same entity ID" | same | Direct substring match, offset ~96761 |
| "That's not your research. That's Claude's research" | same | Direct substring match, offset ~115980 |
| "offload the stuff that they're thinking about onto your plate so that they can get back to their next point of leverage" | same | Direct substring match, offset ~65829 |
| "I've created a ton of SOPs like super boring stuff but stuff that matters" | same | Direct substring match, offset ~113626 |
| "I've always hated the advice about, oh, you have to specialize. You have to niche down... I'm like a proud generalist" | same | Direct substring match, offset ~31481 |
| "saying yes first and then working out later is the best way to grow" | same | Direct substring match, offset ~58966 |
| "clients, they perceive the homepage to be super valuable" | same | Direct substring match, offset ~67123 |
| "the idea is essentially what are you actually saying? What is the point you're making?" | same | Direct substring match, offset ~104376 |
| "Problem, solution, systemize, delegate, and then sell it." | same | Direct substring match, offset ~85864 |
| "some clients ... love to show off their homepage. They show it to friends at dinners." | same | Direct substring match, offset ~66774 (note: source reads "some clients um love to..."; the ledger and anchor both flag the filler-word elision) |
| "There's um system, selling, and strategy" | same | Direct substring match, offset ~84666 |
| "Just relate to the audiences of the brands you're working with in a way that makes them buy things. That's basically it." | same (pre-existing in genius.md, not modified) | Not re-verified this session — pre-existing content, additive-first boundary respected |

## Claims explicitly flagged UNCONFIRMED/LIKELY this repair (see references/source-ledger.md for full table)

- "Doesn't have a driving license. Loves dogs." (Who Alex Is bio line, pre-existing, not
  located in transcript.txt on this pass) — UNCONFIRMED, disclosed in ledger, left
  in place per additive-first (not disprovable either — absence-from-search ≠
  absence-from-source, and the line predates this repair).
- "5 hook types" taxonomy across `references/prompts-v2/*.md` and workflows —
  UNCONFIRMED as an Alex-stated list. Pre-existing and already disclosed honestly in
  SKILL.md's "Notes on Source" section; this repair adds a formal ledger entry, makes
  no content change to the workflows (workflow_contracts check already passed and
  boundaries prohibit rewriting passing content).
- IVOC "50+ quotes / 3+ venues" and Content Grid "50-300 concepts" — LIKELY/UNCONFIRMED
  as extraction-team estimates, not verbatim Alex numbers. Ledger entry added; no
  existing text changed (not part of the failing checks).

## Files consulted, with recorded sizes (verifying non-absence per envelope rule 2)

- `extractions/alex-myatt/transcript.txt` — 121,038 bytes (`wc -c`)
- `extractions/alex-myatt/extraction-report.md` — 34,259 bytes (`wc -c`)
- `extractions/Alex Myatt/transcript.txt` — 121,038 bytes (`wc -c`; identical duplicate,
  not a distinct second source)
- `skills/alex-myatt-creative-engine/` — full directory read (SKILL.md, genius.md, 3
  references/*.md, 11 references/prompts-v2/*.md, 12 workflows/*.md) before any edit
