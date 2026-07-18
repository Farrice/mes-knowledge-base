# Source Ledger — Sharran Srivatsaa Scaling

> Claim-by-claim provenance. Repair pass 2026-07-18. Ground-truth search performed
> before any UNCONFIRMED label was assigned per the "absence is itself a claim" rule.

## Provenance search performed

- `extractions/` — searched for `sharran` and `srivatsaa` (fragments, no punctuation). Zero matches. `ls extractions/` (200+ dirs/files) confirmed no Sharran/Srivatsaa extraction exists in this repo.
- `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed via `wc -c` not `wc -l`) — scanned all 7,728 members with a Python `tarfile` per-member content read (case-insensitive regex `sharran|srivatsaa`, files ≤5MB, UTF-8 decode with error tolerance). Zero matches.
- **Conclusion: no primary transcript/interview source file exists anywhere in this repo for this expert.** All quotes in SKILL.md/genius.md predate this repair pass and cannot be verified against a local transcript — they trace to the original 2026-04-24 extraction's stated `source_material` ("Decision Mapping Method" Ep. 299, "4-Step Process for Investing" Ep. 67, "37 Lessons Growing Teles 10x to $3.4B") plus Perplexity enrichment, per SKILL.md frontmatter.
- Live web search (2026-07-18) run to verify the biographical/framework claims that anchor the skill's credibility, since no local file could confirm or deny them.

## Claims

| Claim | Label | Basis |
|---|---|---|
| Sharran Srivatsaa scaled Teles Properties from $300M to $3.4B in ~5 years, sold to Douglas Elliman | **VERIFIED** | Cross-confirmed 2026-07-18 via acquisition.com/bio-sharran, sharran.com/press-2-2/, Forbes ("The New CEO Of Acquisition.com," Mar 2026), Travis Chappell podcast episode title "$300 million to $3.4 billion??", Krista Mashore site. Multiple independent sources agree on the figures. |
| Sharran Srivatsaa is President & Managing Partner of Acquisition.com | **VERIFIED** | acquisition.com/bio-sharran; Forbes profile naming him incoming CEO of Acquisition.com (Mar 2026), consistent with "President and Managing Partner" framing across sources. |
| Sharran Srivatsaa was President of Real Brokerage (NASDAQ: REAX) | **VERIFIED** | Confirmed via web search 2026-07-18 (RocketReach, LinkedIn bio, sharran.com); matches SKILL.md frontmatter's "Real Brokerage" attribution. |
| Sharran Srivatsaa is Chairman of ARC Multifamily Group | **VERIFIED** | arcmf.com/about/ and PRWeb release "Sharran Srivatsaa joins ARC Multifamily Group as Partner" — confirmed Chairman/Partner role; matches SKILL.md frontmatter's "ARC Multifamily" attribution. |
| "Decision Mapping Method" is a real, named Sharran Srivatsaa framework (4 steps: Context → Isolate → Accept → Map), taught as Episode 299 of his podcast | **VERIFIED** | sharran.com/episode299/ titled exactly "Episode 299: Decision Mapping Method"; web search 2026-07-18 confirms 4-step structure (context/isolate/accept-risk/map) matches genius.md Pattern 3 almost verbatim. This directly confirms the SKILL.md frontmatter citation "(Ep. 299)". |
| "Four Goods" is a real, named Sharran Srivatsaa investment framework | **VERIFIED** (framework existence); **LIKELY** (all 4 sub-names exact) | Web search 2026-07-18 confirms "four goods" language and "Good People" / "Good Intentions" definitions match genius.md Pattern 4 closely. "Good Rationale" and "Good Contract" sub-names were not independently located in search snippets — plausible but not independently confirmed, hence LIKELY not VERIFIED for the full 4-part naming. |
| Verbatim quotes attributed to Sharran inside genius.md/SKILL.md (e.g., "You start operating from a powerful place where facts meet inspiration," "A decision without action is just a thought," all Hidden Knowledge item quotes) | **UNCONFIRMED** | No transcript file exists locally to check word-for-word. Not disproven — the surrounding frameworks they illustrate ARE verified real — but exact phrasing cannot be confirmed without the source episode audio/transcript. Treat as paraphrase-risk, not fabrication-risk. |
| Genius Patterns 1, 5-13 and all 9 Hidden Knowledge items (Compounding Machine, Triple-S, Artifacts of Success, Process-Driven Results, Greatness in Granularity, Results Economy, Inversion Test, 10X Requires Every Domain, Expensive Middle Person, Einstein's 55-Minute Rule, Coach Memo Technique, Imaginary Board, Decision Etymology, Turning Points, Triple Responsibility, Work Smart ≠ Skip Hard, No Process = Flawed Judgment) | **UNCONFIRMED** | Consistent in voice and content with Sharran's verified public teaching style (constraint-based, process-driven, Acquisition.com-adjacent) but not independently located in a specific dated episode this pass. Carried over from the original 2026-04-24 extraction; no local transcript to check against. |
| Hall of Fame Exemplars 1-2 and the Anti-Exemplar ("$800K service business," "$50K ad spend," "30% equity offer," "80-hour weeks / 4 revenue streams") | **ILLUSTRATIVE — not a provenance claim** | These are explicitly constructed teaching scenarios built to demonstrate the frameworks above, not claimed as real Sharran case studies. No verification needed or attempted; flagged here so they are never mistaken for verified anecdotes. |
| "37 Lessons Growing Teles 10x to $3.4B" as a named source | **LIKELY** | Matches the growth figures independently VERIFIED above; the exact title as a discrete piece of content was not independently re-located in this pass's web search, but the underlying facts it describes are confirmed. |

## Labeling rule applied

VERIFIED = confirmed against ≥2 independent live sources 2026-07-18. LIKELY = consistent with verified facts/voice but not independently re-confirmed this pass. UNCONFIRMED = no local transcript and not independently checked externally — explicitly not "false," just unauditable at the quote level. No claim in this skill was found to be contradicted by external sources.
