# PROVENANCE — meg-heckman-buyer-trigger-os repair (Wave 3 Lane 3, batch4)

All anchors verified by direct `grep`/read against `extractions/meg-heckman/` before use. No quote in this repair was invented; every one below was located verbatim in a source file.

## genius.md — "How to Use This Skill (Model Calibration)" (new section)

| Claim/quote | Source file | Verified |
|---|---|---|
| "The question is not, 'Does my design look good?' The question is, 'Can my design stop a person who is not trying to buy anything and make them feel something strong enough to take action?'" | `extractions/meg-heckman/transcript-designs-changed-whats-selling.txt` (Video 3, iFvHwZBIwoA) | Already verbatim in skill's own `references/source-quotes.md` line 30; cross-checked against transcript file |
| Design A/Design B polish-vs-conversion contrast (woodblock/eagle/van/waterfall vs. "Out of Breath," 3,714 sales claim) | `references/source-quotes.md` (Video 2, mV-DQElnWGk) — pre-existing skill content, reused | Pre-existing in skill, not newly sourced |

## genius.md — Anti-Patterns section (9 items newly sourced; 3 already passed pre-repair — see AUDIT NOTE)

| Anti-pattern item | Quote added | Source file (grep-verified) | Video |
|---|---|---|---|
| Make the buyer decode | "People scroll fast. They do not decode designs, especially in ads on Facebook. They simply react to them." | `extractions/meg-heckman/video-context-7MNa2YTPGs4/transcript.txt` (1 occurrence, confirmed via `grep -c`) | Video 1, 7MNa2YTPGs4 |
| Target a demographic | "We went after somebody completely different, the casual hiker. The person who goes for a 30-minute stroll on a mountain and calls it a hike, and they're genuinely proud of that." | `extractions/meg-heckman/transcript-designs-changed-whats-selling.txt` | Video 3, iFvHwZBIwoA |
| Scale by taste | "You will fall in love with a design that does not perform well in ads and you will have to be willing to cut it... The market does not care what you love. The market cares about what it loves." | `extractions/meg-heckman/transcript-861k-method.txt` | Video 5, 19ur85v6OPA |
| Touch ad account before mockup swap | "We ended up swapping the mockup and reran our tests. And it showed the exact same design on a different mock-up and the CPCs immediately started to come down." | `extractions/meg-heckman/transcript-30k-profit-metrics.txt` | Video 6, MfP-56ayttE |
| Optimize checkout before cart-page trust | "does this store feel trustworthy enough for me to even buy from?" + "a very clear return policy" | `extractions/meg-heckman/transcript-30k-profit-metrics.txt` (grep-confirmed both substrings) | Video 6, MfP-56ayttE |
| Install upsell apps before catalog cohesion | "I would focus first on creating more products or designs that people genuinely want to buy and pair together." | `extractions/meg-heckman/transcript-30k-profit-metrics.txt` (grep-confirmed) | Video 6, MfP-56ayttE |
| Expand to mugs/hoodies before loop repeats | "Focus on one product in the beginning... Depth before breadth every time." | `extractions/meg-heckman/transcript-861k-method.txt` (grep-confirmed both fragments) | Video 5, 19ur85v6OPA |
| Stop generating at design #30 | "Your one breakout design might be design 91 or 312 or 800. If you stop early, the design that would have changed everything just stays unfound." | `extractions/meg-heckman/transcript-861k-method.txt` (grep-confirmed) | Video 5, 19ur85v6OPA |
| Interrupt without delivery | "The interrupt has to lead somewhere... it's the door. It's not the room." (full sentence: "...because that's the door. It's not the room.") | `extractions/meg-heckman/transcript-designs-changed-whats-selling.txt` (grep-confirmed) | Video 3, iFvHwZBIwoA |
| Quote thresholds as universal laws | Cited to `references/source-quotes.md` § Claims Ledger, LIKELY band (shipping tiers, 48h ad window) | `skills/meg-heckman-buyer-trigger-os/references/source-quotes.md` (pre-existing, internal citation) | n/a — internal ledger cite |
| Assert revenue claims as verified | Cited to `references/source-quotes.md` § Claims Ledger, UNCONFIRMED band | `skills/meg-heckman-buyer-trigger-os/references/source-quotes.md` (pre-existing, internal citation) | n/a — internal ledger cite |

**Items already passing pre-repair (untouched wording, no new anchor needed):** "Judge by prettiness" (quote already inline), "Copy a bestseller" (quote already inline) — both already carried a 6+ char quoted string, which is what the auditor's `_HB_SOURCE_ATTR_RE` counts as sourced. I added a video citation to these two as well for consistency/robustness, not because they were failing.

## workflows/meg-factory-loop.md

No new claims introduced. The `## Output: The Written Operating Cadence` heading was retitled to `## Output Format` (house-style match with the other 11 workflow files in this skill) and its existing four elements (Weekly rhythm, Decision thresholds, Weekly review, No-redesign clause) were reformatted into a fenced-code-block template — same house style as `meg-aov-architect.md`'s Output Format section. No prose content was deleted; the 90-day volume target section was added as a fifth template block to make the schema self-contained (values sourced from the pre-existing "Step 1: GENERATE" prose in the same file, not new claims).

## AUDIT NOTE (correction to my own initial read)

The audit file states 3/13 anti-pattern items were already source-attributed pre-repair. I confirmed this via the auditor's own regex (`_HB_SOURCE_ATTR_RE`) against the original file: items "Judge by prettiness" (inline quote), "Copy a bestseller" (inline quote), and "Quote her thresholds as universal laws...2026..." (year token `2026`) already matched. My repair added qualifying anchors to the remaining 10 items, bringing sourced count to 13/13, confirmed by re-running `skill_auditor.heartbeat_checks()` against a scratch merge of the repaired files (see REPAIR-NOTES.md for the verification command and output).
