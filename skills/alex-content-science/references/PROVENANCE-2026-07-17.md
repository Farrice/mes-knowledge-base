# PROVENANCE — alex-content-science repair

Anchor → source file + location. Full claim-by-claim ledger with
VERIFIED/LIKELY/UNCONFIRMED labels lives in `references/source-ledger.md`;
this table is the quick-reference index for every quote/number added during
this repair pass.

| Added to | Anchor text (excerpt) | Source file | Location |
|---|---|---|---|
| genius.md, "How to Use This Skill" | "20 invisible decisions underneath the surface..." / "2.7 million views...90,000-follower...30x" / "318 likes...800,000 views" | extractions/alex-content-science/transcript.txt | offsets ~0–100, ~4808, ~12480–12679 |
| genius.md, § 2 The Sheep Cycle | "So you copy a competitor's video..." / "So what do you do? You panic..." | transcript.txt | ~3021–3232 |
| genius.md, § 7 Pattern Interrupt Engineering | "calm reads as authority. Calm reads as expensive." | transcript.txt | ~6832 |
| genius.md, § 10 Cross-Niche Format Hacking | "Lead with a visual result. Show the tool easy..." / Wimbledon vs. smartphone | transcript.txt | ~11236 |
| genius.md, § 11 Competitor Database Method | filters/Notion/1,000,000+ views detail | extractions/alex-content-science/extraction-report.md | Genius Pattern #11 (labeled LIKELY — Perplexity-enrichment layer, not verbatim transcript) |
| genius.md, "What Did They Refuse to Do?" Lens | "Ask yourself, why did they choose the angle?..." | transcript.txt | ~14798 |
| genius.md, The Subconscious Trust Stack | "You stop scrolling because something feels different, even if you can't explain [music] why." | transcript.txt | ~6857 |
| genius.md, § Quality Rubric | "that's not stealing like an artist. That's just stealing." | transcript.txt | ~317 |
| genius.md, § Hall of Fame Exemplars (confidence note) | none — flagged as illustrative/UNCONFIRMED, not sourced | n/a | added label only, no new claim |
| genius.md, § Anti-Patterns (all 7 bullets) | see references/source-ledger.md VERIFIED table | transcript.txt | offsets 317 / 2102 / 2815 / 3021 / 3232 / 3350 / 14524 / 13105 |

All offsets are approximate character positions confirmed via `python3`
`str.find()` against the actual file content read on 2026-07-17, not
estimated from memory. `transcript.txt` = 21,666 bytes (`wc -c`);
`extraction-report.md` = 17,524 bytes (`wc -c`) — both confirmed non-empty,
non-truncated.
