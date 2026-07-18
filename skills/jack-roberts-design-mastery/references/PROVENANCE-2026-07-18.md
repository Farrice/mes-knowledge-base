# PROVENANCE — jack-roberts-design-mastery repair (2026-07-18, Wave 3 Lane 4 Batch 6 REDO)

Anchor → source file+location table. Full claim reasoning lives in
`references/source-ledger.md`; this file maps each new quote-anchor in
`genius.md` to its exact source location.

| Anchor (as it appears in repaired genius.md) | Source | Location |
|---|---|---|
| "AI is incredible at code. Design can actually be codified." | `extractions/jack-roberts/transcript.txt` | Central-premise passage, ~line 1 (single continuous transcript block) |
| "We're going to codify something once and once we do that, we can replicate it infinitely." | `extractions/jack-roberts/transcript.txt` | Opening framing of the design system, early in transcript |
| "it's a markdown file, no Figma export, no JSON schema, no special tooling." | `extractions/jack-roberts/transcript.txt` | DESIGN.md-format explanation passage |
| "You can see it a mile away." | `extractions/jack-roberts/transcript.txt` | Closing line of the AI-slop-apocalypse description |
| "you're going to see purple gradients. You're going to see interfont. You're going to see the classic three rounded boxes." | `extractions/jack-roberts/transcript.txt` | AI-slop-apocalypse passage |
| "the biggest criticism about AI generated content is mainly the fact that it all looks exactly the same." | `extractions/jack-roberts/transcript.txt` | Opens the AI-slop-apocalypse passage |
| "I mean, I don't like the now live and beta. Let's never have that." | `extractions/jack-roberts/transcript.txt` | Refinement-feedback example, mid-transcript |
| "I would just add I would like these to be more presentation. So, not loads and loads of text." | `extractions/jack-roberts/transcript.txt` | Presentation-brief example |
| "It has amnesia and a memory problem." | `extractions/jack-roberts/transcript.txt` | Final passage of the transcript |
| "I give all of my agents access to firecrol because it is just so powerful." | `extractions/jack-roberts/transcript.txt` | Firecrawl-integration demo passage |
| "Getting their logos, getting their accent colors, getting the typography that we can now pull in." | `extractions/jack-roberts/transcript.txt` | Firecrawl/Glido.com extraction demo |
| "what is the thing that you spend most of your own personal time creating and what would have the highest impact if you were to automate it." | `extractions/jack-roberts/transcript.txt` | Highest-leverage-selection passage |
| "Hey there, my last meeting, could you tell me one action that I had to do off the back of that, please?" | `extractions/jack-roberts/transcript.txt` | Granola-integration example |
| "bear in mind this is completely one shot." | `extractions/jack-roberts/transcript.txt` | Lovable/Ollama/SpaceX one-shot demo |
| Kia API "six cents um per image" → "~$0.06/image" | `extractions/jack-roberts/transcript.txt` | Image-generation pricing passage |
| 60,000+ customers / sold last startup / runs an AI startup | `extractions/jack-roberts/transcript.txt` | Opening self-introduction |
| 91% conversion stat, "Inblad Science" attribution | `extractions/jack-roberts/transcript.txt` | AI-slop-apocalypse data passage — attribution name itself flagged LIKELY (see source-ledger, not independently re-verified) |
| "53% of people are already starting to get this... hire designers less and less." | `extractions/jack-roberts/transcript.txt` | Closing market-adoption passage |
| 14 workflow "## Output Schema" / "## Quality Gate" sections | Pre-existing content within each workflow file itself (this repair) | Each schema/gate line cites the same file's own pre-existing "## Output" bullets or named numeric thresholds (e.g., anti-slop-audit.md's 15-point scale, brand-in-a-box.md's "13+/15" thresholds, design-iteration-loop.md's "When to stop iterating" rules) — no external source, self-referential to the file being repaired |
| `## Anti-Patterns (Sourced)` section (6 items) | `extractions/jack-roberts/transcript.txt` | Each item anchors to one of the six quotes above |
| `## How to Use This Skill (Model Calibration)` section | Original prose, this repair | Structurally modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per the repair envelope's instruction; content (dollars-per-image, stars-per-week, rejection-first iteration) drawn from facts already verified elsewhere in this table, not copied from Ben Watkins' file |
| Second Jack Roberts source discovered but unused | `_active/claude-export/index.json`, `harvest/census-full.json` | Conversation "11-8-25 Jack Roberts: How to go from $0 to $10,000/mo with AI Audits" (id `6e49b972-e4b3-4332-b9f7-eaf62c4440ae`) — topically distinct (business/monetization, not design), content file no longer on disk. See source-ledger Absence Verification for full detail. |

Sizes recorded per envelope instruction: `extractions/jack-roberts/transcript.txt` =
**29,046 bytes** (`wc -c`), confirmed non-trivial before any UNCONFIRMED claim was made.
