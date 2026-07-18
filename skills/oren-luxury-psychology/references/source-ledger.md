# Source Ledger — oren-luxury-psychology

Every source consulted for this repair, labeled VERIFIED / LIKELY / UNCONFIRMED, claim-by-claim. Sizes recorded via `wc -c` on 2026-07-18 (repair session) so future auditors can confirm nothing was invented or silently dropped.

## Sources Consulted

| File | Size (wc -c) | Role |
|---|---|---|
| `extractions/oren/extraction-report.md` | 23,343 bytes | **Primary source** for this skill. Header states: "Source: YouTube video — 'Psychology of Luxury Branding' (~25 min, ~4,674 words)." Contains the Genius Patterns (1-9), Hidden Knowledge (1-8), and Methodology sections that the skill's genius.md is built from. |
| `extractions/oren/transcript.txt` | 29,376 bytes | **Read and checked — NOT the luxury-psychology source.** Content is a different Oren video ("brand social media archetypes / Oracle, Performer, World Builder..."). This transcript backs a sibling skill (oren-archetypes lineage), not oren-luxury-psychology. Flagged explicitly so no one assumes it's the raw transcript behind extraction-report.md. |
| `extractions/oren/oren-systems-extraction-report.md` | 14,668 bytes | Read — different Oren extraction ("11 Ways to Get Your Life Together," operational systems). Not used for luxury-psychology content; confirms the "Existing Overlap" note in extraction-report.md about the 3-skill Oren stack. |
| `extractions/oren/extraction-report-repositioning.md` | 21,509 bytes | Read — different Oren extraction (repositioning/creative direction of personalities). Not used for luxury-psychology content; same stacking note as above. |
| `skills/oren-luxury-psychology/genius.md` (pre-repair) | 19,771 bytes | Existing skill file — all Pattern/Hidden Knowledge prose already present here traces to extraction-report.md; verified by side-by-side comparison during this repair. |
| `skills/oren-luxury-psychology/references/genius-patterns.md` | 4,790 bytes | Existing reference mirror of Patterns 1-9 — consistent with extraction-report.md, no new claims. |
| `skills/oren-luxury-psychology/references/hidden-knowledge.md` | 4,796 bytes | Existing reference mirror of Hidden Knowledge 1-8 — consistent with extraction-report.md, no new claims. |

## Claim-by-Claim Labels

| Claim / quote | Label | Basis |
|---|---|---|
| "Never EXPLAIN codes (outsider signal). DEPLOY them (insider signal)." | VERIFIED | Verbatim in `extractions/oren/extraction-report.md`, Pattern 2 ("The Insider Codes Mechanic," Executable Behavior line). |
| "Superiority signaling is the riskiest — it attracts superficial buyers." | VERIFIED | Verbatim in `extractions/oren/extraction-report.md`, Pattern 1 ("The Four-Factor Purchase Psychology," Executable Behavior line). |
| Moncler sells 12 units of a $2,000 collaboration jacket vs. thousands of core down jackets | VERIFIED | Verbatim numbers in `extractions/oren/extraction-report.md`, Hidden Knowledge 4 ("Marketing IS the Core Product"). Note: the extraction's own Pattern 6 names the collaborator as "ASAP Rocky" while Hidden Knowledge 4 names "Donald Glover" for the same $2,000 jacket claim — an internal inconsistency in the source document itself, not introduced by this repair. Both instances are flagged LIKELY on the collaborator name specifically (the dollar figure and unit count are consistent across both and VERIFIED). |
| Manhattan Saddlery / Japanese gardening store in London / 500-1,000 vs. 50,000 buyers | VERIFIED | Verbatim in `extractions/oren/extraction-report.md`, Hidden Knowledge 8 ("Niche Luxury Is Under-penetrated"). |
| "to premium buyers, busyness is the OPPOSITE of luxury" (paraphrase of "busyness is the OPPOSITE of luxury") | VERIFIED | Verbatim phrase "busyness is the OPPOSITE of luxury" appears in `extractions/oren/extraction-report.md`, Hidden Knowledge 5. The "to premium buyers" framing is repair-worker paraphrase wrapping a verbatim core clause — labeled VERIFIED for the quoted clause itself. |
| Indonesian horse troughs sold as "French provincial planters" for $2,000-4,000 | VERIFIED | Verbatim in `extractions/oren/extraction-report.md`, Hidden Knowledge 3 ("Providence Arbitrage"). |
| "Democratize access, but create tiers of connoisseurship. Let everyone in the door; sell depth to those who want it." | VERIFIED | Verbatim in `extractions/oren/extraction-report.md`, Pattern 3. |
| "For most people, building a product brand is the wrong move; curating someone else's products with taste is the right move." | VERIFIED | Verbatim in `extractions/oren/extraction-report.md`, Pattern 9. |
| "The REAL product being sold is the PROGRESSION itself. Every 'tier' is a new purchase opportunity." | VERIFIED | Verbatim in `extractions/oren/extraction-report.md`, Hidden Knowledge 1 ("Why It's Missed" line). |
| "identify the 5-10 insider codes that separate people who belong from people pretending" | VERIFIED | Verbatim in `extractions/oren/extraction-report.md`, Pattern 2 (Executable Behavior line). |
| "Choose which of the 4 purchase triggers your offer activates (belonging, individualism, enjoyment, superiority). Write ALL communications to that trigger." | VERIFIED | Verbatim in `extractions/oren/extraction-report.md`, Methodology "Layer 3 — Trigger Activation." |
| Store names "Good Hood, March, MurthA" (Pattern 9, pre-existing genius.md content, untouched by this repair) | UNCONFIRMED | Not found verbatim in extraction-report.md or any file under `extractions/oren/`. Pre-existing content this repair did not author or verify further — flagged here for the next auditor rather than silently carried forward as fact. |
| Raw primary transcript of "Psychology of Luxury Branding" (the actual video source behind extraction-report.md) | UNCONFIRMED — file not present | No transcript file matching this video exists anywhere under `extractions/oren/` as of this repair (only `transcript.txt`, confirmed above to be a *different* video). extraction-report.md is a synthesis document, not the primary source; its internal quotes are VERIFIED as text-in-file but not independently checkable against the original spoken source. |

## Honest Gap

The single biggest gap: this skill's ground truth is a distilled extraction report, not a raw transcript. Every VERIFIED label above means "this exact string is present in extraction-report.md," not "this exact string was independently confirmed against Oren's spoken words." That distinction matters for an adversarial verifier — treat VERIFIED here as "verbatim-in-cited-file," the standard this repair batch's envelope asks for.
