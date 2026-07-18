# Provenance — Ocean Vuong Perceptual Writing Repair

Anchor → source file+location. All anchors point to files under `extractions/ocean-vuong/` (sizes confirmed via `wc -c`: `extraction-report.md` = 31,645 bytes, `transcript.txt` = 75,514 bytes — transcript is a single unbroken line, so offsets not line numbers) or to external web sources checked 2026-07-18.

| Anchor (as used in genius.md / source-ledger.md) | Source file | Location / method |
|---|---|---|
| "80% of writing is looking and thinking. The last part is syntax." | extractions/ocean-vuong/transcript.txt | `python3 -c "re.finditer('80% of writing', text)"` — match at offset found via script in this session |
| "the spike protein... the downloading mechanism" | extractions/ocean-vuong/transcript.txt | same substring-search method, 1 hit |
| "300,000 people beat you to it" / Ben Lerner | extractions/ocean-vuong/transcript.txt | substring search, "Ben Lerner" 1 hit, "300,000" 1 hit, same anecdote block |
| Mike Tyson's ear / rose cliché rescue | extractions/ocean-vuong/transcript.txt | substring search "Mike Tyson", 1 hit |
| "idiosyncrasy and strangeness" / Hemingway | extractions/ocean-vuong/transcript.txt | substring search "maximalist", 1 hit |
| "too felt" newspaper-sentence critique | extractions/ocean-vuong/transcript.txt | substring search "too felt", 1 hit |
| "There's no such thing as cliché" | extractions/ocean-vuong/transcript.txt | substring search "no such thing as cliché", 1 hit |
| Robert Browning "Meeting at Night," 20 years | extractions/ocean-vuong/transcript.txt | substring search "Meeting at Night" / "Robert Browning", verified together |
| Eduardo Corral moss/applause, nine years | extractions/ocean-vuong/transcript.txt + extraction-report.md lines 62, 226 | transcript: substring "nine years" + "looked at moss for a long time"; extraction-report.md for the full simile text (transcript excerpt truncates mid-word in this session's search window) |
| Isaac Babel beheaded sunset | extractions/ocean-vuong/transcript.txt | substring search "beheaded", 4 hits, quote confirmed at first hit |
| Japanese botanist / medicinal plant method | extractions/ocean-vuong/transcript.txt | substring search "Japanese botanist", 1 hit |
| Skateboarding / eight-stair | extractions/ocean-vuong/transcript.txt | substring search "eight-stair", 1 hit |
| Shklovsky ostranenie, Aristotle mimesis/poiesis, Lotman synchronic/diachronic | extractions/ocean-vuong/extraction-report.md | lines 24, 30, 53, 211 (theory framing as extracted by the original extraction pass) |
| MacArthur Fellow, T.S. Eliot Prize, NYU professor | WebSearch 2026-07-18 | umass.edu/news "Ocean Vuong Named 2019 MacArthur Fellow"; tseliot.com prize page; oceanvuong.com/about |
| Age 2 emigration from Vietnam, family illiteracy | WebSearch 2026-07-18 | Wikipedia "Ocean Vuong," Britannica "Ocean Vuong" |
| New Yorker slush pile | extractions/ocean-vuong/transcript.txt | substring search "slush", 3 hits, verbatim quote at first two |
| "11 out of 12 editors" (SKILL.md line 3 / genius.md line 9) | **No corroborating source found** | Checked transcript.txt ("Midwest" editor anecdote, 1 hit, does not state a ratio) and WebSearch (no external corroboration) — labeled UNCONFIRMED in source-ledger.md, flagged for conductor, left unedited (outside the two failing checks this worker was scoped to repair) |

Method note: `transcript.txt` has 0 newline characters (`wc -l` = 0), so all substring searches were run via a Python script using `re.finditer` on the full file text rather than `grep`/`sed` line addressing.
