# Source Ledger — skills/omar-eddaoudi

Claim-by-claim provenance for `genius.md`. Ground truth = files under
`extractions/omar-eddaoudi/` (four files verified by direct read + grep,
sizes recorded below — none absent, none 0-byte).

## Source files checked (per name-fragment search + full read)

| File | Size | Content |
|---|---|---|
| `extractions/omar-eddaoudi/transcript.txt` | 12,702 bytes, 1 line (no newlines) | "Psychology of Premium Branding" video — luxury value inversion, Rolex/Gleitze, Hermès distance |
| `extractions/omar-eddaoudi/extraction-report.md` | 6,491 bytes | Module 1 extraction summary (mirrors genius.md's luxury patterns verbatim) |
| `extractions/omar-eddaoudi/module_2/module_2_transcript.txt` | 64,251 bytes, 32 lines | Multi-video transcript: Nike ad-history, AI/LLM commerce future (LEO), 5-step premium-ads framework (Removal Game, Patek Philippe quote) |
| `extractions/omar-eddaoudi/module_2/extraction-report.md` | 7,620 bytes | Module 2 extraction summary (Narrative Hegemony, LEO, Objection-First, Removal Game) |
| `extractions/omar-eddaoudi/module_3/*.txt` (3 files) | 30,840 / 11,561 / 16,472 bytes | Zero-to-7-figures, wellness ad teardown, static ad design — NOT used by base `omar-eddaoudi` genius.md (belongs to sibling skills `omar-eddaoudi-premium-ads` / `omar-eddaoudi-scaling-ops`, out of scope for this repair) |

Search method: `grep -in` for name fragments (rolex, gleitze, birkin, hermes,
louis vuitton, gorbachev, deneuve, sean connery, patek, wilsdorf, eisenhower,
hillary) across every file above, plus a full read of `transcript.txt` and
the first ~2,000 chars of each `module_3` file to confirm topic scope. No
tarballs/archives exist for this skill (`find . -iname "*eddaoudi*.tar*"` /
`.zip` = no results) — flat `.txt`/`.md` files only, so no `tarfile` scan was
needed.

## Claims in genius.md

| # | Claim (genius.md section) | Label | Basis |
|---|---|---|---|
| 1 | The Value Inversion / Veblen Pivot pattern | VERIFIED | `transcript.txt`: "luxury is the only category here that fundamentally breaks the relationship between value and price... the value of a luxury product lies primarily in one thing, and that's price itself" |
| 2 | Controlled Distance / Cold Aesthetics pattern | VERIFIED | `transcript.txt`: "models look super serious... What if instead you as the consumer needed to prove yourself to the brand... This principle is called distance" |
| 3 | Archetypal Mirroring pattern | VERIFIED | `transcript.txt`: "That's why you see a lot of brands position their products as a mirror. Owning it says something about you" |
| 4 | Gravedigger's Detail / "Sweaty Neck" — Rolex hung a watch on a Channel swimmer's neck | VERIFIED (event) / synthesized (phrase) | `transcript.txt`: "He found Mercedes Gllights [sic, =Gleitze], a woman swimming the English Channel... hung a Rolex Oyster around her neck and after 10 hours in the freezing water, the watch was still ticking." "Sweaty Neck"/"salt-crusted" wording is the extraction's own vivid framing of the real event, not a verbatim Omar phrase. |
| 5 | "Art vs. Ad" Distinction | VERIFIED | `transcript.txt`: "They feel closer to art than advertising. But that's because art creates emotion." |
| 6 | Hierarchy of Needs Inversion — the problem is "Anonymity" | LIKELY | `transcript.txt` discusses Maslow's hierarchy and buying "to feel," but never uses the word "Anonymity" — this is the extraction's interpretive label on a real but looser source passage, not a direct quote. |
| 7 | Social Signal Precedence — "speaks before the owner does" | VERIFIED | `transcript.txt`: "A luxury product speaks before you do." (near-verbatim) |
| 8 | Hall of Fame Exemplar 1 — Rolex/Gleitze, "1927," exact ad copy quote | VERIFIED (core event) / LIKELY (exact date + ad copy text) | Core event confirmed in `transcript.txt` (see row 4). The specific year "1927" and the verbatim ad line "The Rolex Oyster, the world's first waterproof watch, worn by Mercedes Gleitze during her cross-Channel swim" do NOT appear in the transcript — this is real, well-documented advertising history but not sourced from the provided extraction. Labeled LIKELY for the added specifics, not UNCONFIRMED, because it is independently verifiable public record, not an invention. |
| 9 | Hall of Fame Exemplar 2 — Hermès Birkin waitlist | LIKELY | Absent from all four extraction files (confirmed by grep across `transcript.txt`, both `extraction-report.md` files, `module_2_transcript.txt`, and all three `module_3` files — zero matches for "birkin"). Real, publicly documented luxury-retail fact; not an Omar Eddaoudi statement. |
| 10 | Hall of Fame Exemplar 3 — LV "Core Values" campaign (Gorbachev, Deneuve, Connery) | LIKELY | Absent from all extraction files (zero grep matches for "louis vuitton," "gorbachev," "deneuve," "sean connery" anywhere in `extractions/omar-eddaoudi/`). Real, publicly documented 2007-08 LV ad campaign; not an Omar Eddaoudi statement. |
| 11 | Anti-Exemplar — hypothetical Patek/A. Lange financing ad | N/A (illustrative) | Explicitly hedged with "e.g." in the source genius.md text — a teaching device, not a claim of a real ad. Not present in any extraction file (no real ad by this description was located or claimed to exist). |
| 12 | Signature Moves (Provenance Narrative Weave, Aspirational Friction Gate, Heroic Archetype Anchor, Silence Premium Edit, Anonymity Cure Statement) | VERIFIED | Faithful restatements/renamings of patterns #1-3 and #6-7 above, which are themselves source-grounded. No new factual claims introduced. |
| 13 | Competence Rarity Architecture (Earned Exclusivity Layer) | UNCONFIRMED as an Omar Eddaoudi statement | Not present in any extraction file — the transcript never discusses service/expertise businesses in this framing. This is a skill-authored extension layer built to cover a gap in the source (physical-artifact focus only). Disclosed honestly in genius.md as a "Provenance note," not attributed to Omar as a direct teaching. |
| 14 | Expert-Specific Quality Rubric | VERIFIED (derivative) | Scoring criteria derived from patterns #1-3, #6-7 above; not an independent factual claim. |
| 15 | Perception Hegemony / LEO / Objection-First / Removal Game (used in `narrative-hegemony-positioning-strategy.md` and `leo-sentiment-signal-optimization.md`, referencing genius.md) | VERIFIED | `module_2/module_2_transcript.txt`: "Premium brands are in the removal game," "instead of competing on features, they want to redefine the perception," AI/LLM retrieval passage ("classify that data... retrieval, the classification and then the distribution"). |
| 16 | Patek Philippe "you never own it, you merely look after it" quote (used in `module_2/extraction-report.md`, informs Mirror-Bridge pattern referenced by workflows) | VERIFIED | `module_2/module_2_transcript.txt`: "you don't own a PEX. You merely look after it for the next generation." (Omar's own paraphrase of the real, independently famous Patek Philippe slogan.) |

## Labeling rule applied

VERIFIED = the specific wording or its clear paraphrase is present in a
named extraction file, quoted above. LIKELY = the underlying claim is real
and independently verifiable public-record fact, but not present in Omar's
own extraction transcripts — used instead of UNCONFIRMED because the claim
was actively checked against outside knowledge, not left unread. UNCONFIRMED
= reserved for claims that are neither source-anchored nor independently
verifiable as fact (none found in this skill's genius.md; the closest case,
row 13, is disclosed as a skill-authored extension rather than presented as
an Omar Eddaoudi claim, so it is not left silently unlabeled).
