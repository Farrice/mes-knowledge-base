# Source Ledger — Oscar Höglund / Sound Storytelling

Claim-by-claim provenance. Ground rule: no `extractions/` file exists for this expert —
confirmed via `ls extractions/ | grep -i hoglund|hoglund|epidemic` (zero hits) and a repo-wide
grep for "Höglund/Hoglund/Epidemic Sound" outside the skill tree. The real source material was
recovered from `_archive/claude-export-2026-07-01.tar.gz` via a full Python `tarfile` per-member
scan (7,720 members scanned, all `.md`/`.txt`/`.json`/`.jsonl` bodies checked for "hoglund" /
"epidemic sound") — 5 members matched by content; the primary one is the original MES 3.0
extraction conversation that produced this skill's patterns.

## Sources Consulted

| ID | Source | Location | Size | Status |
|----|--------|----------|------|--------|
| S1 | Podcast transcript, Oscar Höglund (CEO, Epidemic Sound) interviewed by Chris Do, "The Impact of Sound in Your Storytelling w/ CEO of Epedemic Sound," auto-transcribed by Merlin AI | `https://www.youtube.com/watch?v=ee-kOLCnuh0` (URL as pasted into the original extraction prompt; not independently re-fetched this session) | transcript block = one paragraph, ~7,500 words, embedded at line 30 of S2 | **LIKELY** — content reads as a genuine unedited ASR transcript (filler words, false starts, one name mis-transcription "Oscar Haglun"/"Amami" for "umami"); URL not re-verified live this session, so video existence/accuracy is LIKELY not VERIFIED |
| S2 | Claude.ai conversation export capturing the original MES 3.0 extraction session that generated this skill's 14 patterns / 6 hidden-knowledge items | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/9781b202-5d3f-4aae-8a90-e6797a35abc0.md` | member: 86,143 bytes; archive: 332,779,255 bytes | **VERIFIED** — file opened and read directly this session; local mirror at `references/source-transcript-excerpt.md` |
| S3 | `skills/oscar-hoglund-sound-storytelling/genius.md` (pre-repair) — Hall of Fame Exemplars ("Echoes of Home," "Weight of Silence," "Generic Corporate Explainer") and Signature Moves | in-repo | n/a | **UNCONFIRMED as Höglund case studies** — these terms/scenarios do not appear anywhere in S2's transcript (checked via full-text search). They are illustrative constructs authored by the original extraction pass to demonstrate the patterns, not real Epidemic Sound projects or Höglund quotes. Preserved as-is (they were never presented as direct quotes, and `verbatim_exemplars` already passes), but must not be cited as sourced. |

## Per-Pattern Grounding

| Item | Status | Anchor |
|---|---|---|
| Pattern 1 — Emotional Umami Creation | VERIFIED | S2 L30: "if you add taste, if you add um[ami], it not only becomes memorable, but if you do it right, it becomes unforgettable" |
| Pattern 2 — Body-Based Truth Connection | VERIFIED | S2 L30: heartbeat-in-horror-films passage ("it signals your heart to beat faster... a little perspiration and you're short of breath") |
| Pattern 3 — Self-Proving Arguments | VERIFIED | S2 L30: "you don't have to take Oscar's word for [it]... Pick a movie... Watch it without sound... You can come to your own conclusion" |
| Pattern 4 — Continuum Mapping | VERIFIED | S2 L30: music/visual-content spectrum discussion; Game of Thrones budget "$10 million. 10 to $20 million" |
| Pattern 5 — Empty Calorie to Michelin Transformation | **PARTIAL** — "empty calories" half VERIFIED (S2 L30 food metaphor); "Michelin" half UNCONFIRMED — the word "Michelin" does not occur anywhere in S2 (checked, 0 hits across 804 lines). It is an extraction-authored elaboration on Höglund's actual metaphor, not his word. |
| Pattern 6 — Adversity as Innovation Fuel | VERIFIED | S2 L30: "all great things come from adversary and from friction"; Jeff Bezos "failure and innovation... inseparable twins" (attributed by Höglund, not independently verified as an actual Bezos quote — LIKELY) |
| Pattern 7 — Economic Translation | VERIFIED | S2 L30: GoT cost figures + IKEA/H&M "decent furniture/clothing for all" democratization analogy |
| Pattern 8 — Infinite Consumption Design | VERIFIED | S2 L30: "some songs have been played hundreds of times. But I can't say any movie I've ever watched 100 times" |
| Pattern 9 — Multi-Sensory Layering | VERIFIED | S2 L30: five-senses passage ("The one sense that you cannot turn off is your ears") |
| Pattern 10 — Classroom Story Architecture | VERIFIED | S2 L30: "bring a parent to school day," "25 7 year olds," son "Seth," Frozen/Elsa track |
| Pattern 11 — Oscillation Design | VERIFIED | S2 L30: "you need to oscillate between that... that's not... the recipe to have like exceptional outcomes" |
| Pattern 12 — Narrative Without Selling | LIKELY | Inferred from the same self-proving passage (Pattern 3) reframed as non-assertive persuasion; no separate direct quote names this as distinct from Pattern 3 |
| Pattern 13 — Intent Decoding | VERIFIED | S2 L30: Marrakech bazaar passage ("my entire body jolted... a completely different vibe") + "I like to read people, rooms, contexts" |
| Pattern 14 — Versatile Asset Creation | VERIFIED | S2 L30: "It's not the painting, it's the pigment... in the hands of each artist, we get to tell our own stories" |
| Hidden Knowledge 1-6 | VERIFIED (all 6 trace to the same passages as their matching Pattern above) | S2 L30 |
| Signature Moves (Sonic Archetype Mapping, Sub-Audible Layering, Resonance Check, Oscillation Blueprinting, Infinite Return Pathfinding) | LIKELY | Reasonable synthesis of Höglund's stated principles; the specific example phrases in quotes ("aching hope," "brittle joy," infrasound/high-frequency shimmer specifics) do NOT appear in S2 — those illustrative micro-quotes are UNCONFIRMED as his words |
| Hall of Fame Exemplars 1-2 ("Echoes of Home," "Weight of Silence") | UNCONFIRMED as real Höglund/Epidemic projects | Not found in S2 or elsewhere; illustrative fiction, not misattributed as direct quotes in-file |
| Anti-Exemplar ("Generic Corporate Explainer Video") | UNCONFIRMED as a real case | Illustrative negative example, not sourced to a real project |

## Rule Compliance Notes

1. No quote in this repair is presented as verbatim Höglund language unless it is found in S2 —
   checked via direct file read, not assumed.
2. The prior absence of any `extractions/` file for this expert was verified by directory listing
   and repo-wide grep before writing "no extractions exist," not asserted from memory.
3. All anchors above point to a specific member path + line in the actual archive, plus a local
   mirrored excerpt (`references/source-transcript-excerpt.md`) for fast verification without
   re-opening the 332MB tarball.
