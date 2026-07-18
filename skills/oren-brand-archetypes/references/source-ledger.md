# Source Ledger — oren-brand-archetypes

Every source consulted during this repair, and the confidence label attached to each claim group carried in `genius.md`. Labels: **VERIFIED** (verbatim or near-verbatim match found in a source file, quote confirmed by direct read), **LIKELY** (concept/mechanism confirmed in source but the specific wording is a paraphrase or the extraction itself flags uncertainty), **UNCONFIRMED** (no matching source file found; claim ships as-is because it was pre-existing content out of this repair's scope, not because it's been verified).

## Sources Consulted (file + size, `wc -c`)

| File | Size | Role |
|---|---|---|
| `extractions/oren/transcript.txt` | 29,376 bytes | PRIMARY raw transcript of the source video ("Choose One of these Archetypes to Beat 99% of Brands on Social Media," orenmeetsworld). Undated harvest, no timestamps, but the fullest/cleanest pass — most brand-name spellings in `genius.md` trace to this file exactly. |
| `extractions/oren-john-identity-marketing/companion-brand-archetypes-transcript.md` | 31,331 bytes | SECONDARY transcript of the same video, timestamped (`[MM:SS]`), harvested 2026-07-15 from YouTube ID `tcqf6sgw_Ho`. Used for all timestamp anchors in this repair's new Anti-Patterns section. |
| `extractions/oren-john-identity-marketing/companion-brand-archetypes.md` | 12,104 bytes | Companion digest (structure map, case-study table, explicit warning not to merge this archetype framework with Oren's separate identity-association five archetypes). Own "Honest assessment" section flags one uncertain reference ("Artifact C") — see below. |
| `extractions/oren/extraction-report.md`, `extractions/oren/oren-systems-extraction-report.md`, `extractions/oren/extraction-report-repositioning.md` | 23,343 / 14,668 / 21,509 bytes | Checked, confirmed OUT OF SCOPE — these cover Oren's luxury-branding, operational-systems, and repositioning extractions (feed sibling skills oren-luxury-psychology / oren-operational-systems / oren-repositioning), not the archetypes framework. Not cited. |
| `extractions/oren-1person-ai-marketing/*`, `extractions/oren-identity-brand-os/*` | — | Checked, confirmed OUT OF SCOPE (different Oren John source families — AI marketing and identity/brand-OS extractions, not the archetypes video). Not cited. |

## Claim-by-Claim

### New content added this repair (Anti-Patterns section, Model Calibration section)

| Claim | Label | Anchor |
|---|---|---|
| "a lot of brands have an idea... rarely does anyone actually ever do the big idea... they're constrained" | VERIFIED | Verbatim in both `companion-brand-archetypes-transcript.md` [02:24] and `extractions/oren/transcript.txt` (near-identical second pass: "Why not? Is because they're constrained.") |
| "No shared terminology; do not merge the two five-part lists..." | VERIFIED | Verbatim, `companion-brand-archetypes.md` line 5 |
| "I don't think anything is too boring... a story behind every screw, every bolt, every welding piece" | VERIFIED | Verbatim in both transcript files (companion [05:24]; primary transcript, "industrial parts manufacturing" section) |
| "the catalyst is like is aspiring... Whereas the helper is more practical" | VERIFIED | Verbatim, `companion-brand-archetypes-transcript.md` [17:55], corroborated in `extractions/oren/transcript.txt` |
| "this is best for teams and founders that are willing to take a risk. It's not for everyone" | VERIFIED | Verbatim, `companion-brand-archetypes-transcript.md` [13:08], corroborated in primary transcript |
| "The product barely needs to be mentioned, it's often omnipresent throughout the entire content" | VERIFIED | Verbatim, `companion-brand-archetypes-transcript.md` [10:10], corroborated in primary transcript |
| "You don't have an expert who can be on camera, so Oracle is off the table" (Model Calibration section, register example) | LIKELY | This exact sentence is authored to demonstrate the register `archetype-diagnostic.md` Phase 2 already prescribes ("be direct about eliminations out loud") — the MECHANISM is verbatim-sourced (Phase 1 elimination logic, resource audit), the specific sentence is a constructed example, not a lifted quote. Labeled LIKELY, not VERIFIED, for honesty. |

### Pre-existing content spot-checked (not modified this repair — named_entity_floor already PASSED; documented here for adversarial-verification honesty per envelope rule #2)

| Entity in `genius.md` Pattern 3 (unchanged) | Label | Anchor |
|---|---|---|
| Ken Sakata / Front Office | VERIFIED | `extractions/oren/transcript.txt`: "one of my absolute favorites... is Ken Sakata... releasing his own version under his brand front office." (Note: the companion transcript spells this "Ken Sekiguchi" — a cross-harvest transcription variance on the same proper noun; the primary transcript's spelling matches `genius.md` exactly.) |
| Blam Motorworks | VERIFIED | `extractions/oren/transcript.txt`, verbatim |
| Kreiss (two-account method) | VERIFIED | `extractions/oren/transcript.txt`: "Crease Furniture... K R E I S S and an actual C R E A S E" — spelled out letter-by-letter in source |
| Rarify | VERIFIED | `extractions/oren/transcript.txt`, verbatim |
| Duer Shoots | LIKELY | Both transcripts capture the spoken brand name imperfectly ("there's shoots" / "Dur Shoots") — `genius.md`'s "Duer Shoots" is the plausible real-world normalization (DUER is a known menswear brand) but is not itself a verbatim transcript string. Flagged LIKELY, not VERIFIED. |
| Mohawk Chevrolet, LC Sign | VERIFIED | `extractions/oren/transcript.txt`, verbatim |
| Death to Stock, Cluey, Fern | VERIFIED | `extractions/oren/transcript.txt`, verbatim |
| Crease Group (Catalyst example, manufacturing) | VERIFIED | `extractions/oren/transcript.txt`: "my favorite example of this is someone who I worked with closely on their social strategy which is crease group. So a manufacturing group." (Not present in the companion digest, which uses a different Catalyst example, "Chris Cruise" — the two harvests sampled different portions of the same section; both are legitimate, non-contradictory.) |
| Artifaxing | VERIFIED | `extractions/oren/transcript.txt`: "accounts like big accounts like Artifaxing." (The companion digest's own honest-assessment section flags this same reference as uncertain — "Artifact C" — because its harvest pass mis-transcribed the name; the primary transcript resolves it cleanly.) |
| Base Living | VERIFIED | `extractions/oren/transcript.txt`, verbatim |
| Kiyoko Beauty | VERIFIED | `extractions/oren/transcript.txt`, verbatim exact spelling match |
| HashiHome / Certigrad | VERIFIED | `extractions/oren/transcript.txt`: "Another example, Certigrad, Hashihome, where they're doing relatable stuff about being a host" (order reversed vs. `genius.md`, same two names) |
| Marpipe | VERIFIED | `extractions/oren/transcript.txt`, verbatim |

**Net finding**: every existing brand exemplar in `genius.md` Pattern 3 traces to `extractions/oren/transcript.txt` (the primary, untimestamped harvest) even though `genius.md` currently carries no inline citations for that pattern. This ledger is the first place that provenance is made explicit. No fabricated entities were found — the one open question (Duer Shoots) is a transcription-fidelity gap, not an invented brand.
