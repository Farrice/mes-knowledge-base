# Source Ledger — Ghostwriting Voice Engine

**Purpose**: Document the sourcing confidence level (VERIFIED/LIKELY/UNCONFIRMED) for every claim, pattern, and exemplar in genius.md. Sourced from extraction transcripts, published works, and documented practices.

**Legend**:
- **VERIFIED** — Direct quote from extraction transcript, confirmed by direct file read (file path given below). Reflects the expert's actual language.
- **LIKELY** — Pattern documented across 2+ expert sources or stated practice described in extractions, but no single verbatim quote. High confidence based on corroboration.
- **UNCONFIRMED** — Pattern synthesized from known practices, or a specific figure/stat that could not be located verbatim in an available source file. Remains useful but requires expert validation if challenged.

**2026-07-17 (Wave 3 Batch 4) — correction note**: A prior repair pass (Batch 3) wrote extensive REPAIR-NOTES.md and PROVENANCE.md claiming this ledger's Anti-Patterns 8–9 and a "Model Calibration" section had been added to `genius.md`. Direct read of the live `skills/ghostwriting-voice-engine/genius.md` on this pass found neither — only the meta-files (this ledger, PROVENANCE.md, REPAIR-NOTES.md) had actually landed in the tree; the underlying content edits never did, which is why `anti_patterns_sourced` and `recognition_test` were still failing. This pass adds the missing content for real (see `## Anti-Patterns (Sourced Failure Modes)` and `## How to Use This Skill (Model Calibration)` in the delivered `genius.md`), re-verifies every anti-pattern quote against the actual extraction files, and corrects one over-claimed citation (Anti-Pattern 7, below).

---

## Anti-Patterns (genius.md — new "## Anti-Patterns (Sourced Failure Modes)" section)

All 7 verified by direct read of the cited file on 2026-07-17 — exact substring search, not paraphrase-matching.

### 1. The Portfolio Paradox
- **Source**: Nicolas Cole
- **Confidence**: VERIFIED
- **Quote**: "The client does not care how much quote unquote industry credibility you have... The only thing the client cares about is you educating them on a problem they know they have in their business but haven't gotten around to solving or a problem they don't even know they have in the first place."
- **File**: `extractions/nicolas-cole-ghostwriting-v2/transcript.txt`

### 2. The Pricing Floor
- **Source**: Nicolas Cole
- **Confidence**: VERIFIED
- **Quote**: "You should never be charging less than $3,000 for a project or per month."
- **File**: `extractions/nicolas-cole-ghostwriting-v1/transcript.txt`

### 3. Free Work Without a Boundary
- **Source**: Nicolas Cole
- **Confidence**: VERIFIED
- **Quote**: "Don't look at it as free work. Look at it as a marketing cost."
- **File**: `extractions/nicolas-cole-ghostwriting-v2/transcript.txt`

### 4. Case-Study-Only Content
- **Source**: Lara Acosta
- **Confidence**: VERIFIED
- **Quote**: "that's one of the biggest mistakes I see with people whether it's LinkedIn content or even YouTube content is they... got a bunch of videos of like case studies and things I've done with my clients and like that's great but it's probably not... going to get a few hundred views realistically."
- **File**: `extractions/lara-acosta/transcript.txt`

### 5. Voice Fidelity Without a Distribution Strategy
- **Source**: Lara Acosta
- **Confidence**: VERIFIED
- **Quote**: "taking what works and using your story or skill to grow."
- **File**: `extractions/lara-acosta/transcript.txt`
- **Note**: The prior (Batch 3) ledger paired this quote with a second fragment about "AI slop" / "cringe" as if part of the same continuous statement. Re-checked directly: both phrases exist in the transcript but in different, unrelated passages (the "AI slop" line is a show-intro description of Acosta's topic, not her own coined term; "cringe" describes an unrelated anecdote about a job-seeking platform). Dropped from this anti-pattern to avoid misattributing a composite quote as verbatim.

### 6. Losing the Reader
- **Source**: Mitch Albom
- **Confidence**: VERIFIED
- **Quote**: "the worst thing you want to hear as a writer is I tried to read it but I got lost."
- **File**: `extractions/mitch-albom/transcript.txt`

### 7. Anaphora Run the Whole Length
- **Source**: Ward Farnsworth
- **Confidence**: VERIFIED
- **Quote**: "you don't want the entire speech to be this kind of repetition."
- **File**: `extractions/ward-farnsworth/transcript.txt`
- **Context**: Part of Farnsworth's soccer-commentator analogy (announcers stay level, get loud only approaching the goal) — corroborates the existing Hidden Knowledge row "The ear detects difference, not absolute level."

---

## Legacy Anti-Pattern Sourcing (Hidden Knowledge table, unchanged rows)

Carried forward from the prior ledger version; re-checked, labels adjusted where the prior VERIFIED claim could not be confirmed.

- **Voice lives in the "imperfections"** (Cole + Acosta) — LIKELY. No single verbatim quote combining both experts on this exact framing; corroborated by Cole's rule-breaking/compression emphasis and Acosta's authenticity-signal commentary across their transcripts.
- **BECOME, don't imitate** (Albom) — LIKELY. Consistent with Albom's embodiment-over-imitation framing across `extractions/mitch-albom/transcript.txt`; no single verbatim sentence matches this exact phrasing.
- **Voice extraction fails when you flatten emotional range** (Acosta + Mallet) — LIKELY (Acosta) / UNCONFIRMED (Mallet — no extraction file exists for Erica Mallet; see Expert Stack Attribution below).
- **The ear detects difference, not absolute level** (Farnsworth) — LIKELY, now reinforced by the VERIFIED Anti-Pattern 7 quote above (soccer-commentator analogy).
- **Limitations you accept become signatures readers love** (Albom + Cole) — LIKELY. Directionally consistent with both transcripts' emphasis on constraint-as-signature; no single verbatim quote states this framing directly.
- **Repetition is the ghostwriter's hidden enemy** (Cole) — LIKELY. Consistent with Cole's compression doctrine (`extractions/nicolas-cole-ghostwriting-v2/transcript.txt`); "one clear statement > two fuzzy restatements" is a paraphrase of that doctrine, not a verbatim line.
- **The quality of a ghostwritten piece is determined in the first hour after publishing — "80% of LinkedIn reach is set in the first 60 minutes"** (Acosta) — **UNCONFIRMED** (downgraded from the prior ledger's VERIFIED label). Direct search of `extractions/lara-acosta/transcript.txt` and `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt` for "first hour," "60 minutes," and "80%" found no matching passage. The broader point — that early engagement drives distribution — IS corroborated (e.g., "the hard part is what happens after you hit publish," "wasting a perfectly written post... without a strategy for it to be seen," references to LinkedIn algorithm shifts), but the specific 80%/60-minute figure is not traceable to a source file in this repo. Treat the number as illustrative, not attributed.

---

## Genius Patterns (Expert-Sourced Tables)

### Voice Extraction Patterns
- **Source**: Lara Acosta — **Confidence**: VERIFIED — `extractions/lara-acosta/transcript.txt`, `extractions/lara-acosta/extraction-report.md`, `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt`
- **Key patterns**: 5-Dimension Voice Scan, Signature Phrase Extraction, Rhythm Fingerprinting, Emotional Range Mapping, Voice Discovery Interview, Dual-Persona Lens.

### Voice Embodiment Patterns
- **Source**: Mitch Albom — **Confidence**: LIKELY — `extractions/mitch-albom/transcript.txt` (92KB, confirmed present and readable). Consistent with "internalize worldview, not surface patterns" framing throughout; individual pattern names in genius.md are synthesis, not verbatim.

### Voice Crystallization Patterns
- **Source**: Erica Mallet — **Confidence**: UNCONFIRMED. No `extractions/erica-mallet*` directory exists in this repo (verified via `ls extractions/` search, 2026-07-17). These patterns (6-Component Voice DNA, 4-Axis Voice Spectrum, etc.) are system-design synthesis, not sourced to a transcript. Treat as house framework, not a direct Mallet quote/claim.

### Voice Refinement Patterns
- **Source**: Nicolas Cole — **Confidence**: VERIFIED — `extractions/nicolas-cole-ghostwriting-v1/transcript.txt`, `extractions/nicolas-cole-ghostwriting-v2/transcript.txt`. Compression, portfolio-paradox, and pricing-floor claims directly verified (see Anti-Patterns 1–3 above).

### Voice Elevation Patterns
- **Source**: Ward Farnsworth — **Confidence**: LIKELY — `extractions/ward-farnsworth/transcript.txt` (72KB, confirmed present). Rhetorical device names (Saxon Punch, Chiasmus, Epistrophe, Anaphora) are house terminology applied to Farnsworth's underlying rhetorical principles; the register-contrast principle itself is VERIFIED (Anti-Pattern 7 above).

---

## Hall of Fame Exemplars

- **Exemplar 1 ("Alex Chen")** — UNCONFIRMED (illustrative composite, not actual client work).
- **Exemplar 2 ("Sarah Miller")** — UNCONFIRMED (illustrative composite, not actual client work).
- **Anti-Exemplar (Generic Corporate Statement)** — LIKELY (recognizable archetype of AI-slop/corporate copy, not a single sourced case).

---

## Client-Acquisition Layer (Lines ~193–207 in genius.md, "Farrice / Nicolas Cole Ghostwriting OS")

- **Farrice ICP Triad**: LIKELY — Farrice synthesis built on Cole's client-targeting logic; not a verbatim Cole framework.
- **Information Advantage Audit**: LIKELY — consistent with Cole's "you are your own case study" / asymmetric-knowledge framing in `extractions/nicolas-cole-ghostwriting-v1/transcript.txt`.
- **Leaks & Faucets Warm Network**: LIKELY — general practice, not a verbatim Cole quote in the available transcripts.
- **Personalized Loom Outreach**: UNCONFIRMED — no direct transcript match found for "Loom" specifically.
- **Education-as-Sales Problem Script**: VERIFIED (directionally) — matches Cole's extended "educating the client on a problem" argument in `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` (see Anti-Pattern 1 quote and surrounding context).
- **Problem-First Discovery Call**: LIKELY — consistent with Cole's problem-education philosophy; call-structure specifics are Farrice synthesis.
- **Outcome-Based 3-Tier Pricing**: LIKELY — pricing-floor principle (Anti-Pattern 2) is VERIFIED; the 3-tier structure itself is Farrice synthesis.
- **Free Work Accelerator (guard-railed)**: VERIFIED (directionally) — Cole's "confidence / testimonial / referral" trade framework is present in `extractions/nicolas-cole-ghostwriting-v1/transcript.txt`; the "marketing cost, not free work" framing is VERIFIED verbatim (Anti-Pattern 3).
- **Land-First-$10K Sequence**: LIKELY — composite workflow built from the above, Farrice orchestration.

---

## Quality Gate: Voice Authenticity Standard (10-Point Checklist)

Each point is a house-synthesized checklist item attributed to the expert whose pattern set it draws from (Albom, Acosta, Cole, Mallet, Farnsworth) — LIKELY across the board; these are system design applying each expert's documented emphasis, not verbatim checklist quotes from any single source.

---

## Expert Stack Attribution

| Expert | Role | Primary Extraction | Confidence |
|--------|------|-------------------|------------|
| Lara Acosta | Voice extraction + platform strategy | `extractions/lara-acosta/transcript.txt` + `2026-linkedin-playbook-transcript.txt` | VERIFIED |
| Mitch Albom | Voice embodiment + character internalization | `extractions/mitch-albom/transcript.txt` | LIKELY (VERIFIED for Anti-Pattern 6) |
| Erica Mallet | Voice crystallization + drift warnings | No extraction file exists in this repo | UNCONFIRMED |
| Nicolas Cole | Voice refinement + sentence optimization + client acquisition | `extractions/nicolas-cole-ghostwriting-v1/transcript.txt` + `-v2/transcript.txt` | VERIFIED |
| Ward Farnsworth | Rhetorical elevation + register contrast | `extractions/ward-farnsworth/transcript.txt` | LIKELY (VERIFIED for Anti-Pattern 7) |
| Farrice Cain | System orchestration + ICP/offer synthesis | Implicit in genius.md structure (claude.ai export) | N/A (system designer, not extracted expert) |

---

## Extraction Files Referenced (confirmed present + readable, 2026-07-17)

| File | Size | Expert(s) | Status |
|------|------|-----------|--------|
| `extractions/lara-acosta/transcript.txt` | 64,332 bytes | Lara Acosta | VERIFIED, read |
| `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt` | 31,860 bytes | Lara Acosta | VERIFIED, read |
| `extractions/lara-acosta/extraction-report.md` | 8,192 bytes | Lara Acosta | present |
| `extractions/nicolas-cole-ghostwriting-v1/transcript.txt` | 30,638 bytes | Nicolas Cole | VERIFIED, read |
| `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` | 21,487 bytes | Nicolas Cole | VERIFIED, read |
| `extractions/mitch-albom/transcript.txt` | 92,280 bytes | Mitch Albom | VERIFIED, read |
| `extractions/ward-farnsworth/transcript.txt` | 72,156 bytes | Ward Farnsworth | VERIFIED, read |
| `extractions/Ward Farnsworth/transcript.txt` + `extraction-report.md` | 72,156 + 6,802 bytes | Ward Farnsworth | duplicate/legacy path, present |
| `extractions/erica-mallet*` | — | Erica Mallet | **does not exist** — confirmed via `ls extractions/` search |

---

## Notes for Maintenance

1. **When adding new anti-patterns**: extract the verbatim quote yourself via direct file read (grep/search the transcript), don't trust a prior ledger's claim without re-checking — this pass caught one over-claimed citation (the "80%/60-minute" stat) and one composite-quote misattribution ("AI slop"/"cringe") from the Batch 3 version of this file.
2. **Erica Mallet has no extraction source** in this repo as of 2026-07-17. All "Mallet" patterns in genius.md are house-synthesized voice-crystallization framework, not sourced quotes. Label any new Mallet claim UNCONFIRMED unless a real extraction file is added.
3. **Wave 3 Batch 4 (2026-07-17)**: closed the gap where Batch 3's REPAIR-NOTES.md/PROVENANCE.md described genius.md edits that were never actually applied to the live file. This ledger now matches the genius.md actually delivered in this batch's output directory.
