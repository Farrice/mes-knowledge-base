# Provenance — sabrina-ramonov-ai-monetization repair

Anchor → source file + location. Ground truth = `extractions/sabrina-ramonov/`
(only extraction directory found for this expert; confirmed via
`ls extractions/ | grep -i ramonov` and `grep -i sabrina`).

| Anchor (used in genius.md) | Source file | Location |
|---|---|---|
| "It is so tempting to switch... chasing the next shiny object..." | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | mid-transcript, "Step number one" / lock-in section |
| "they spend months building courses or products that nobody buys..." | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | opening paragraph |
| "if you wait until you're ready, honestly, you're giving it yourself an excuse to never get started" | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | learn-in-public section |
| "AI startups in particular flush with cash..." | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | sponsorship / monetization section, near end |
| "the vast majority of courses are not recurring revenue... you pay once... it's like goodbye" | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | offer-design section |
| "people have the tendency to listen to a podcast or see something on Instagram and then like completely change their strategy" | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | closing "bonus step four" section |
| "A lot of people are concerned if I post too much then I'm going to like overwhelm my audience" | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | learn-in-public / volume section |
| "the reason why I'm 100% confident in this path when you invest first in building a brand..." | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | recap section, after learn-in-public |
| "anybody can come into your community and honestly just clone all of your courses. But it's very difficult to clone the people..." | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | community-offer section |
| "there's a lot of excitements in the market and there's a lot of money flowing into something already..." | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | lock-in / market-timing section |
| "in 99% of the failed stories I hear about, truthfully, the entrepreneur would have been successful if they just did things in the right order..." | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | opening paragraph |
| "Competitors can copy your curriculum; they can't copy your members' wins" | `extractions/sabrina-ramonov/extraction-report.md` | Hidden Knowledge #3 ("The Wins-as-Moat Principle") |
| "over 20 million users" (Skool) | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | community-offer section |
| "$50,000 per month in 6 months" (entrepreneur example) | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | opening paragraph |
| "50 bucks per month" (starting community price) | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | pricing section |
| "By the way, I am not a guru" / "built and sold an AI company for millions of dollars" | `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | opening paragraph |

All quotes above verified verbatim via `grep -o "<exact string>" extractions/sabrina-ramonov/transcript-zero-to-1m.txt` (and the one extraction-report.md quote via the same grep against that file) before being written into genius.md — none were written from memory or inference.

File sizes recorded with `wc -c` (not `wc -l`, per the single-line-file gotcha):
- `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` — 18,394 bytes
- `extractions/sabrina-ramonov/extraction-report.md` — 14,149 bytes

No archive scan of `_archive/claude-export-2026-07-01.tar.gz` was needed — both source files were
found directly and immediately under `extractions/sabrina-ramonov/`.
