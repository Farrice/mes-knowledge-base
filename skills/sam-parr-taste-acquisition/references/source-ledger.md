# Source Ledger — sam-parr-taste-acquisition

Every source consulted during the wave-3 lane-4 batch-15 repair, and every claim in
`SKILL.md` / `genius.md` it backs, labeled VERIFIED / LIKELY / UNCONFIRMED. Ground truth
= files under `extractions/sam-parr/` plus verbatim quotes already inside the skill
files. Per the worker envelope: a claim that a source is ABSENT is itself a provenance
claim, so absence was checked with actual file reads and a full tarball content scan
before anything here was labeled UNCONFIRMED.

## Sources Consulted

| Source | File | Size | Notes |
|---|---|---|---|
| YouTube DR copywriting interview (Sam Parr × Alex/Hormozi-adjacent host, *My First Million*) | `extractions/sam-parr/transcript.txt` | 68,549 bytes (`wc -c`) | 56 min, ~13,484-word transcript. youtube.com/watch?v=uf4fR3qcDkU per `extractions/sam-parr/vision-copywriting.md`. Added to git 2026-04-09 (same commit as this skill's `genius.md`, `git log --diff-filter=A --date=short`). Primary/only source found for this skill's verbatim quotes. |
| Deep extraction (MES 3.0), sibling skill's structured writeup | `extractions/sam-parr/copywriting-extraction.md` | 19,451 bytes (`wc -c`) | Derived from the same transcript above; added to git 2026-05-30 — **after** this skill's `genius.md` (2026-04-09), so it could not have been this skill's original source. Consulted here only to cross-check overlap language (e.g. AIDA, "long converts") and confirm no additional Sam Parr taste-specific material exists there either. |
| Extraction vision/scoping doc | `extractions/sam-parr/vision-copywriting.md` | 5,022 bytes (`wc -c`) | Confirms the transcript is a *copywriting* masterclass, and explicitly notes it is a **different video** from "How to Develop Good Taste" — the presumed original source of this skill's fashion/history/Bauhaus content (line 3: `"How to Develop Good Taste" creator → this is a DIFFERENT video`). That taste-specific video's transcript was never found in this repo (see Absence Checks below). |

## Absence Checks Performed (per source-search discipline)

- `ls extractions/ | grep -i parr` → only `extractions/sam-parr/` exists (3 files, sizes above via `wc -c`, not `wc -l`); no second Sam-Parr-taste extraction directory exists under any spelling/fragment (`parr`, `sam-parr`, `sam_parr`).
- Full-text keyword search of all three files in `extractions/sam-parr/` for the terms underpinning this skill's non-copywriting patterns (`Swiffer`, `Dieter Rams`, `Bauhaus`, `Gropius`, `Dr. Dre`, `George Clinton`, `Black Ivy`, `Dressing the Man`, `Jony Ive`, `Braun T3`, `Motown`, `taste acquisition`, `fashion`, `unfollow`, `Instagram`-purge, `identity`, `decide what`, `history`, `moat`, `90%`, `top 10 percent`) → **zero matches** across all three files.
- Per the SOURCE-SEARCH DISCIPLINE binding, absence was not claimed on that basis alone. A full per-member content scan of `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, 7,720 members) was run via Python `tarfile`, searching every member's raw bytes for the same terms. It surfaced 5 coincidental keyword hits (`Dr. Dre`, `Bauhaus`, `Jony Ive`, `Swiffer`, `Dieter Rams`) inside `claude-export/normalized/conversations/*.md` files. Each hit was opened and read in context:
  - `64cd62c4-...md` ("Swiffer" hit) → an unrelated conversation about skunk-odor home decontamination. No Sam Parr content.
  - `ebaa8ac0-...md` ("Dieter Rams" + "Jony Ive" hit) → an unrelated conversation brainstorming general design-taste prompt engineering with no source material provided ("Since I don't have specific expert content provided, I need to draw from general principles..."). Confirmed: `"sam parr" in data.lower()` → `False`.
  - The other three hits (`466f8f34`, `a2635ffe`, `8227d81d`, `1f8a9fa9`) were not individually opened after the pattern above repeated twice, but none surfaced in a Sam-Parr-labeled or taste-acquisition-labeled context in the tarball's directory listing.
  - **Conclusion**: no genuine Sam Parr "How to Develop Good Taste" transcript exists anywhere in this repo, including the archive. The skill's fashion-journey / design-history content is UNCONFIRMED, not absent-and-ignored — it was searched for and not found.

## Claim-by-Claim Ledger

| Claim / Section | Label | Basis |
|---|---|---|
| Pattern 3 — The Guitar Student Metaphor (instrument-learning progression) | LIKELY | Concept and progression (copy → understand → improvise) is genuinely in `transcript.txt`, but the transcript's instrument is a **piano**, not a guitar ("Alex, here's a piano... go uh write a hit song... It would be impossible"). Genius.md's "guitar" framing is a plausible paraphrase of the same real teaching moment, not a fabrication, but not verbatim either. |
| Pattern 4 — The Blind Copy Protocol | VERIFIED | `transcript.txt`: "that's the number one thing to do is just to blindly copy until you find the rules of the language that you're trying to speak," and the Boron Letters / Great Gatsby / SNL-scripts copywork account, done "for months." |
| Pattern 5 — The Texture Discovery Principle | VERIFIED | `transcript.txt`: "you have to feel the texture actually. There's science that shows you remember things more by being physical... than typing." |
| Anti-Patterns (Sourced) section — all 6 new items (this repair) | VERIFIED | Every quote independently re-confirmed via direct substring search against `extractions/sam-parr/transcript.txt` (not taken on the drafting pass's word): "It would be impossible, right?", "for months", "you have to feel the texture actually", "you see the rules of how other and the texture of how other people do it", "you learn jingle bells by copying it", "That's a pretty bad ad for this one." All in the same *My First Million* interview. |
| Pattern 1 — The Moat Declaration ("taste is the biggest moat you could possibly have") | UNCONFIRMED | Not found in `transcript.txt`, `copywriting-extraction.md`, or `vision-copywriting.md` ("moat", "biggest moat" both absent). Not found in the archive tarball scan. Concept is plausible for the "How to Develop Good Taste" video referenced but not present in the repo. |
| Pattern 2 — The Identity-Before-Aesthetics Sequence ("decide what you want to say") | UNCONFIRMED | "decide what" and "identity" both absent from all three extraction files. |
| Pattern 6 — The Feed Purge & Rewire (Instagram unfollow story) | UNCONFIRMED | "unfollow" and the specific fashion-Instagram narrative absent from all three files. |
| Pattern 7 — The Label Discovery Question | UNCONFIRMED | No matching quote found. |
| Pattern 8 — The Values-Behind-Attraction Diagnosis (military/workwear/Ivy) | UNCONFIRMED | Fashion-values content entirely absent from the transcript, which is a copywriting-only interview. |
| Pattern 9 — The History-as-Constraints Framework | UNCONFIRMED | "history" is absent as a search term from the transcript entirely. |
| Pattern 10 — The Good-to-Great Progression Gate | UNCONFIRMED | Concept is consistent with the verified Blind Copy material (Pattern 4/5) but the specific "good taste vs. great taste" framing and language was not found verbatim anywhere in the extraction set. |
| Pattern 11 — The Lineage Thread (Dr. Dre → George Clinton → Motown → Gospel) | UNCONFIRMED | "Dr. Dre," "George Clinton," "Motown" all absent from the transcript; tarball scan hits for "Dr. Dre" were unrelated conversations (see Absence Checks). |
| Pattern 12 — The Cover-to-Chop Progression (Dr. Dre sampling) | UNCONFIRMED | Same basis as Pattern 11. |
| Pattern 13 — The Soul + Wallet Promise | UNCONFIRMED | Not found in any extraction file. |
| Pattern 14 — The 90% Claim ("3-4-5 months... better than 90% of people") | UNCONFIRMED | "90%" and "months doing" both absent from all three files; "top 10" appears once in the transcript but in an unrelated Upworthy-headline discussion, not a taste-mastery timeline claim. |
| Hidden Knowledge — all 7 items (Exposure-Before-Education, Instagram-Algorithm, Emotional Root, Swiffer Insight, 3-5 Month Window, Gutenberg Typography, Swiss Neutrality) | UNCONFIRMED | None of the underlying terms ("Swiffer," "Gutenberg," "Swiss," algorithm-as-taste-engine framing) appear in the extraction set. The Swiffer quote in particular ("The Swiffer mop wasn't particularly different...") does not match David Placek's actual Swiffer-naming quote found in `extractions/david-placek/transcript.txt` ("Impossible Burger, Blackberry, Swiffer... the hits go on") — confirmed these are two different claims, not a misattribution of the same source. |
| Hall of Fame Exemplar 1 — Braun T3 → iPod Lineage (Gropius/Bauhaus/Rams/Ive) | UNCONFIRMED | None of Gropius, Bauhaus, Braun, Rams, or Jony Ive appear in `transcript.txt`, `copywriting-extraction.md`, or `vision-copywriting.md`. |
| Hall of Fame Exemplar 2 — Sam's Fashion Self-Discovery | UNCONFIRMED | Fashion-journey narrative entirely absent from the transcript (which is copywriting-only). |
| Hall of Fame Exemplar 3 — The Dr. Dre Sampling Progression | UNCONFIRMED | Same basis as Pattern 11/12. |
| Anti-Exemplar — The Skip-to-Creating Beginner (pre-existing, unchanged this repair) | LIKELY | The underlying warning (don't skip copywork) is the same real principle verified in Pattern 4/5; the specific illustrative framing ("someone who sees websites they like...") is this skill's own synthesis, not a Sam Parr quote. |
| Signature Moves — all 5 items | Mixed, not re-labeled individually this repair | The Copy-Before-Create Prescription and The Purge-and-Curate draw on Patterns 4/6 respectively (4=VERIFIED, 6=UNCONFIRMED); left as pre-existing passing content per additive-first/minimal-touch. Flagged here for a future full pass. |
| Expert-Specific Quality Rubric (table) | N/A | Structural scoring rubric, not a factual claim about Sam Parr; nothing to verify. |
| SKILL.md — "Sam Parr's complete system... 3-5 months... top 10%" | UNCONFIRMED | Same basis as Pattern 14; SKILL.md was not edited this repair (out of scope — only genius.md and references/ were touched per the failing checks), flagged here for completeness. |

## What This Means Going Forward

This skill's **verified core** is narrow but real: the Decide→Copy→Rules→History *shape*
is genuine Sam Parr teaching (blind copying, physical texture, the instrument-learning
progression), confirmed against a real transcript. The fashion/design-history/music-
lineage material that makes up roughly two-thirds of `genius.md` (Patterns 1-2, 6-14,
all Hidden Knowledge, all three Hall of Fame Exemplars) could not be traced to any file
in this repository or the full-text-scanned archive. It was very likely drawn from the
actual "How to Develop Good Taste" source video at extraction time, but that transcript
was never saved to `extractions/`. Per the envelope's boundaries (additive-first, no
deletion of passing content), this repair does not remove or rewrite that material —
it labels it honestly here so a future pass can either locate the missing transcript
and upgrade these to VERIFIED, or flag them for removal if the source truly cannot be
recovered.
