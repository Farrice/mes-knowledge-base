# PROVENANCE — chris-cimorelli-copywriting repair

Anchor → source file + location, for every quote/date/fact used in the repaired `genius.md` Anti-Patterns section and Model Calibration section. Full claim ledger with VERIFIED/LIKELY/UNCONFIRMED labels: `references/source-ledger.md`.

| Anchor used in repair | Exact source | Verified how |
|---|---|---|
| "Discover our cutting-edge AI platform designed to help you make smarter investment decisions" | `skills/chris-cimorelli-copywriting/genius.md`, § Hall of Fame Exemplars, Exemplar 3 (Anti-Exemplar) — pre-existing text, unchanged | Read full file before editing; quote copy-pasted verbatim |
| "Cimorelli never describes how the product works in front-end copy. He sells the outcome — the lifestyle, the feeling, the result." | Same file, § Hidden Knowledge, "Sell the Vacation, Not the Flight" — pre-existing | Same |
| "our proprietary system delivered a verifiable average of 20.7% annually" | Same file, § Hall of Fame Exemplars, Exemplar 2, Proof Layer 1 — pre-existing | Same |
| "Copy that names what the reader feels but can't articulate ('The Unnamed Feeling') creates trust at a level that proof alone can't reach" | Same file, § Evolution Log, entry dated 2026-04-09 — pre-existing | Same |
| "The first 10 hooks you write are your assumptions about what works. Hooks 11-50 are where you discover what ACTUALLY works." | Same file, § Hidden Knowledge, "50+ Variations Is Not Obsessive" — pre-existing | Same |
| "No 'guaranteed' language? No claims without substantiation? Legally clean?" | `skills/chris-cimorelli-copywriting/workflows/03-copy-diagnostic.md`, line 39, Metric 9 row | Read full file during this repair; quote confirmed at that exact line |
| `source: "Perplexity research — FMS FinPub Pro Podcast, Agora case studies, industry analysis"`, `last_updated: 2026-03-19` | `_active/codex-harvest-2026-06-11/agents/chris-cimorelli/AGENT.md`, frontmatter lines 7 and 9 | Read full file during this repair |
| No `extractions/` file for Cimorelli exists | Ran `ls extractions/ \| grep -i cimorelli` (0 results) and `grep -ril cimorelli extractions/` (1 hit: `extractions/sam-parr/vision-copywriting.md`, name-only mention, checked with `grep -n -i cimorelli` on that file) | Actual shell commands, output captured in this session |
| File sizes (not 0-byte/corrupted) | `wc -c` on `SKILL.md`, `genius.md`, all `workflows/*.md`, all `references/prompts-v2/*.md` | Actual shell command, output captured in this session (see `references/source-ledger.md` for the byte counts) |

No new facts about Chris Cimorelli himself were invented. Every anti-pattern item either quotes this skill's own pre-existing files verbatim or is explicitly labeled UNCONFIRMED/LIKELY where authorship against a primary Cimorelli source could not be established.
