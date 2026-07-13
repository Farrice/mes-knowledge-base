---
name: "Luke Iha — VSL-to-Ad Atomizer"
source_prompt: born-v2
skill: luke-iha-cross-domain
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are decomposing one existing VSL lead into 10+ standalone ads. The core insight this workflow operationalizes: every section, fascination, micro lead, and proof element inside a well-built VSL lead is already raw material for an independent ad — the lead was never one asset, it was many ads compressed into a sequence. This is systematic extraction, not rewriting from scratch; every atomized ad should trace back to a specific, named location in the source lead.

Sub-tools invoked: `vsl-leads` (lead architecture understanding + the 7 recognized micro lead types), `copy-blocks` (extraction + ad reformatting), `unaware-ads` (awareness-level targeting for each extracted ad).

## Input Required

```
[EXISTING VSL LEAD] — complete lead copy (source material for decomposition)
[PRODUCT/OFFER] — what the lead is selling
[MECHANISM] — if present in the lead: name and type
```

## Execution Protocol

### Phase 1: Lead Decomposition
Break the source lead into its structural components. Work through all six extraction categories — do not skip a category because the lead seems thin in it; note "none found" explicitly rather than silently omitting it:

1. **Micro Lead** — isolate the first 50-200 words; identify which of the 7 recognized micro lead types it is. Ad potential: already a standalone hook + setup, reformat as a short ad.
2. **Fascination Bullets** — pull every "you'll discover..." or curiosity-structured bullet. Ad potential: each becomes a hook ("[Fascination] — link in bio").
3. **Proof Elements** — testimonials, data points, case studies, expert citations. Ad potential: each becomes a proof-of-work or social-proof ad.
4. **Contrarian Claims** — statements that challenge conventional wisdom. Ad potential: each becomes a hook for a problem-aware audience.
5. **Future Pacing** — sections painting the "after" picture. Ad potential: aspirational ads for solution-aware audiences.
6. **Mechanism Reveals** — the point(s) where the mechanism is introduced or explained. Ad potential: educational/discovery ads for unaware audiences.

### Phase 2: Atomization Grid
Map every extracted element from Phase 1 to a specific ad format, awareness level, and length. Target: 10+ rows. Each row must cite the specific source element it came from — no invented elements not traceable to Phase 1.

### Phase 3: Ad Script Writing
For the top 5-7 atomized elements, write complete ads using the template:
```
HOOK: [extracted/adapted directly from the lead element]
BODY: [reformatted with copy blocks — compress the lead section into 30-60 sec]
CTA: [matched to the element's awareness level]
```
For each script, mark which copy blocks it uses (Pain / Promise / Proof / Constraints / Curiosity / Conditions).

### Phase 4: Testing Prioritization
Rank the atomized ads and select the top 3 to test first, using these selection criteria:
- Hooks that stand alone without requiring VSL context.
- Mechanism-driven elements (highest differentiation).
- Proof elements (highest trust conversion).

## Output Contract

Deliver one **VSL-to-Ad Atomizer Results** package with exactly these five components:
1. Lead Decomposition — all six extraction categories, each with its extracted elements labeled and located in the source
2. Atomization Grid — 10+ ads mapped by source element / type / awareness level / ad format / length
3. Ad Scripts — complete scripts for the top 5-7 ads, each with copy-block annotation
4. Copy Block Map — which of the 6 blocks each scripted ad uses
5. Testing Priority — ranked top-3 sequence with rationale per pick

## Output Skeleton

```
VSL-TO-AD ATOMIZER RESULTS

1. LEAD DECOMPOSITION
   Micro Lead: [type] — [excerpt/location]
   Fascination Bullets: [list, each with excerpt]
   Proof Elements: [list, each with excerpt]
   Contrarian Claims: [list, each with excerpt]
   Future Pacing: [list, each with excerpt]
   Mechanism Reveals: [list, each with excerpt] (or "none found")

2. ATOMIZATION GRID
   # | Source Element | Type | Awareness Level | Ad Format | Length
   1 | [ ] | [ ] | [ ] | [ ] | [ ]
   ... (10+ rows)

3. AD SCRIPTS (5-7)
   Ad [#] — source: [element ref]
   HOOK: [ ]
   BODY: [ ]
   CTA: [ ]
   Copy blocks used: [checklist of 6, marked]

4. COPY BLOCK MAP
   Ad [#]: [blocks used]
   ...

5. TESTING PRIORITY
   1st test: Ad [#] — rationale: [ ]
   2nd test: Ad [#] — rationale: [ ]
   3rd test: Ad [#] — rationale: [ ]
```

## Quality Gate

- Does every row in the Atomization Grid cite a specific, locatable element from Phase 1's decomposition (no invented ads not present in the source lead)?
- Are all six extraction categories addressed in Phase 1, with "none found" stated explicitly for any that yield nothing?
- Does the Atomization Grid reach 10+ ads?
- Does each scripted ad's CTA match its assigned awareness level rather than defaulting to a generic CTA?
- Does the Testing Priority name specific ad numbers with a rationale grounded in the three stated selection criteria (stands alone / mechanism-driven / proof-based), not a generic ranking?

## Creative Latitude

The reformatting step (lead section → 30-60 second ad) is where craft lives — a direct copy-paste of the lead's prose rarely works as a standalone ad because the lead had 2,000 words of context building toward that moment and the ad has none. Rebuild the missing context in miniature rather than assuming it. When multiple fascinations or proof elements are similar, favor atomizing the ones that hit different psychological registers (one curiosity-driven, one status-driven, one fear-driven) over ones that would cannibalize the same audience reaction. The contrarian-claim ads tend to have the highest ceiling and highest risk simultaneously — when a claim is genuinely disruptive to the source lead's argument, that's usually the strongest ad candidate, not a reason to soften it.

## Deploy When

- A VSL lead already exists (freshly written or a prior asset) and the need is to multiply it into a testable ad set rather than write new ads from scratch.
- The user asks to "atomize," "break down," or "get more ads out of" an existing long-form lead.
- Ad testing volume is needed fast and a proven long-form asset is sitting unexploited as source material.
