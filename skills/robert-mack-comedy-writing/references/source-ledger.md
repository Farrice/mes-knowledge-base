# Source Ledger — Robert Mack: Comedy Writing Mastery

Ground truth for this repair pass is the extraction pair at `extractions/comedy-writing/`
(the only path under `extractions/` matching this expert — confirmed via
`grep -rli "robert mack" extractions/`). No `extractions/robert-mack*` directory exists;
this skill's source material lives under the topical name `comedy-writing`.

## Primary Sources

| Source | Path | Size | Status |
|---|---|---|---|
| Podcast transcript | `extractions/comedy-writing/transcript.txt` | 60,090 bytes / 60,090 chars, single unbroken line (no `\n`) | VERIFIED — read in full via direct file read + string search, not assumed empty from `wc -l` (which reports 0 lines because the file has no newline characters) |
| Extraction report | `extractions/comedy-writing/extraction-report.md` | 18,814 bytes / 218 lines | VERIFIED — human-authored synthesis of the transcript, read in full |

**Provenance note (transcript identity)**: the transcript's own text names the show as
*How I Write* and the guest as Robert Mack, discussing craft from Jerry Seinfeld and Mitch
Hedberg (transcribed "Mitch Hedber" — clear ASR truncation, same person). This matches
`extraction-report.md`'s stated source: "YouTube Interview — How I Write Podcast with David
Perell (~33 min)." David Perell's name does not appear inside `transcript.txt` itself (he is
the unnamed interviewer, denoted `>>`) — LIKELY, not VERIFIED, as a literal transcript string.

## Claim-by-Claim Ledger (genius.md)

### Genius Patterns 1–12

| # | Claim / Attribution | Status | Note |
|---|---|---|---|
| 1 | Skewed Perspective Engine — "I used to do drugs. I still do, but I used to, too." (Mitch Hedberg) | VERIFIED | Verbatim at transcript char ~2404, immediately preceded by "it's Mitch Hedber." |
| 2 | Pattern Recognition Exploitation — "If I say Romeo, you think Juliet. If I say peanut butter, jelly." | VERIFIED | Verbatim at transcript char ~11184 (added as anchor this pass) |
| 3 | Tension-Relief Architecture — nurse-outfit setup/release | VERIFIED | Verbatim at transcript char ~22090 |
| 4 | Bait-and-Switch — Bible/Harry Potter bit | VERIFIED | Verbatim at transcript char ~17314. Genius.md attributes it "(Attributed to various comedians)" — appropriately hedged; the transcript itself gives no personal attribution beyond "I read an article that said..." |
| 5 | Vivid Specificity — "my mother-in-law looks like the Michelin man" | VERIFIED | Verbatim at transcript char ~8912 (transcript reads "Michelin man" exactly) |
| 6 | Universal-to-Specific — "close talker" | VERIFIED | Verbatim at transcript char ~31103, explicitly sourced there to Seinfeld: "this is from Seinfeld which he obviously worked on" — also names Larry David doing this move "150 times" |
| 7 | Concision Under Pressure — "a story isn't everything that happened" / Bob Dylan example | LIKELY | The concision principle is VERIFIED (transcript char ~47804, "just don't need all this setup... could have 10%"); the specific "driving Bob Dylan" illustration in genius.md is a plausible paraphrase-style example, not a verbatim transcript quote — no "Dylan" string in transcript.txt |
| 8 | The Unspoken Setup — "seven feet tall" comedian | VERIFIED | Verbatim at transcript char ~16400 (added as anchor this pass) |
| 9 | Word Selection — outfit/costume/uniform test | VERIFIED | Verbatim at transcript char ~16850–23850 |
| 10 | Meta-Humor Breakout — "Don't even go to that bar" | VERIFIED | Verbatim at transcript char ~41949 |
| 11 | Audience Calibration — Ella Fitzgerald / Beyoncé | VERIFIED | Verbatim at transcript char ~38385 (added as anchor this pass) |
| 12 | Observation-to-Bit Pipeline — dog-sweater / internet-for-dogs riff | VERIFIED | Verbatim at transcript char ~55842–56668 |

### Hidden Knowledge 1–8

| # | Claim | Status | Note |
|---|---|---|---|
| 1 | Comedy as Evolutionary Safety Signal | LIKELY | The play-fighting/safety-signal framing is a faithful synthesis of the "benign violation" material Mack discusses (transcript char ~39554–39900, referencing the academic "benign violation" formula); not a single verbatim transcript sentence |
| 2 | Benign Violation Threshold — Polish jokes | VERIFIED | Verbatim at transcript char ~39267, "I can make Polish jokes because I'm Polish" (added as anchor this pass) |
| 3 | Investment Principle — animal-crackers "seal" joke | VERIFIED | Verbatim at transcript char ~28091 |
| 4 | Naming Creates Reality — "close talker" owned by Seinfeld | VERIFIED | Same anchor as Pattern 6 above |
| 5 | Character Distance Shield — Louis CK's taxi-driver story | VERIFIED | Transcript explicitly frames it: "this little story from Louis CK" (char ~45750), followed by the full bit (char ~46014) |
| 6 | The Single-Word Pivot — outfit/costume/uniform | VERIFIED | Same anchor as Pattern 9 |
| 7 | Loss > Victory — "Winning isn't funny" (Charles Schultz) / Chris Rock private-school bit | VERIFIED | Both verbatim: "winning isn't funny... Charles Schultz" at char ~14520; Chris Rock private-school/gated-community material at char ~14912–15154. Note: the transcript's own spelling is "Schultz" — the cartoonist's actual name is usually rendered "Charles M. Schulz"; kept as transcribed since that is the verbatim source string |
| 8 | Stench Replacement Effect | VERIFIED | Verbatim at transcript char ~53644 (added as anchor this pass) |

### Hall of Fame Exemplars (pre-existing section, not modified this pass)

| Exemplar | Status | Note |
|---|---|---|
| Exemplar 1 — Hedberg "I used to do drugs" | VERIFIED | Same anchor as Pattern 1 |
| Exemplar 2 — Bible/Harry Potter bait-and-switch | VERIFIED | Same anchor as Pattern 4 |
| Exemplar 3 — nurse-outfit bit, attributed "(Rodney Dangerfield)" | **UNCONFIRMED** | The joke text itself is VERIFIED verbatim (char ~22090), delivered by Robert Mack in his own voice with no attribution given in the transcript. "Rodney Dangerfield" does not appear anywhere in `transcript.txt` (confirmed via direct string search). Flagging honestly per this batch's provenance rule rather than silently carrying the attribution forward — this line predates this repair pass and was left in place (additive-only, minimal-touch boundary), but should not be treated as a confirmed attribution downstream |
| Anti-Exemplar (grocery-store apple bit) | LIKELY | Illustrative negative example authored for the skill, not a transcript quote — correctly unattributed in genius.md, no source claim to verify |

### New Anti-Patterns Section (added this pass)

All six items are VERIFIED verbatim against `transcript.txt` — see anchors inline in
`genius.md` § Anti-Patterns (each bullet carries its own quote and location).

### Domain Applications, Prompts, Workflows

The 10 Domain Application files and 30 prompt files under `references/` were NOT re-verified
line-by-line this pass (out of scope — the failing checks target genius.md, SKILL.md, and
three workflow files only). Their content is LIKELY-tier: internally consistent with the
verified Genius Patterns above but not individually checked against the transcript in this
repair.

## Absence Claims (per this batch's provenance rule — verified, not assumed)

- No `extractions/robert-mack*` or `extractions/*mack*` directory exists — confirmed via
  `ls extractions/ | grep -i mack` (empty result) and `find` search of the full repo.
- `transcript.txt` reporting "0 lines" via `wc -l` is a formatting artifact (no `\n` bytes in
  the file), NOT an empty or corrupted file — confirmed by reading its 60,090 characters
  directly and finding dozens of distinct verbatim quotes throughout.
