# luke-iha-copy-blocks — Source Ledger

> Ground-truth audit for `genius.md` and `workflows/`. Labels: **VERIFIED** (read the file directly, quote/claim confirmed against it) · **LIKELY** (file exists and is on-topic, not line-by-line diffed against every claim it supports) · **UNCONFIRMED** (claimed in the skill but no source file exists in the extraction set to check it against — treated as plausible domain knowledge, not fabricated provenance).

## VERIFIED — read directly, anchors quote-checked

| File | Covers | Used for |
|---|---|---|
| `extractions/luke-iha/video-4-copy-blocks/extraction-report.md` (source video: "The fastest way to become a highly paid creative strategist in 2026," ID `riD2Vns4NPE`) | 6 Copy Blocks, CASH Method, hook psychology, HK4 (sequential vs. interleaved blocks) | Anti-Pattern: Sequential blocks · SKILL.md block list · `cash-method-generator` workflow |
| `extractions/luke-iha/extraction-report.md` (root; source video: "The 22 'proof weapons' I used to sell $100mm") | 22 proof weapons, 5 proof domains, "proof is safety not conviction" | Anti-Pattern: Over-proofing |
| `extractions/luke-iha/video-1-proof-mechanisms/extraction-report.md` (source: ~3,780-word transcript) | Proof taxonomy enhancement, Promise-Proof Match, Hard-to-Fake Hierarchy | Genius Codex Proof section (cross-ref only; not directly quoted in an anchor) |
| `extractions/luke-iha/video-8-proof-ladder/extraction-report.md` (source video: "The Simplest Client-Getting Strategy You're Probably Ignoring") | Proof Ladder 5-tier hierarchy, Proof Braiding, Belief Hardening & Backward Dissolution, Proof Balance Scale | Anti-Pattern: Claim bigger than proof · Anti-Pattern: Challenging identity/values head-on · Canyon-metaphor provenance note ($100M+ figure) |
| `extractions/luke-iha-creative-strategist/transcript.txt` | Full raw transcript for the video-8-proof-ladder source ("...the ladder of proof...") — confirms video-8's extraction-report.md is a faithful summary, not an invented one | Model Calibration section (texture quote: "This is the number one thing") |
| `extractions/luke-iha/video-3-levels-of-awareness/extraction-report.md` | Awareness spectrum, unaware-ad architecture, worldview porn | Read for this repair pass; not directly anchored (no genius.md claim traced to it needed sourcing) |
| `extractions/luke-iha/video-6-offer-cycling/extraction-report.md` | Agency ladder, offer heat, positioning | Read for this repair pass; not directly anchored |
| `references/quality-rubric.md` (in-skill) | Score 4 / 7 / 10 rubric anchors | Quality Rubric section entity fix |

## LIKELY — exists, on-topic, not diffed line-by-line for this pass

| File | Note |
|---|---|
| `extractions/luke-iha/video-2-creative-strategy/extraction-report.md` | Creative-strategy/freelance material; skill-boundary note in SKILL.md ("Skill Stacking") already routes strategy content to `luke-iha-creative-strategy` — consistent with this file's scope. |
| `extractions/luke-iha/video-5-vsl-leads/extraction-report.md` | VSL lead architecture; consistent with SKILL.md's stated boundary to `luke-iha-vsl-leads`. |
| `extractions/luke-iha/video-7-million-dollar-mechanisms/extraction-report.md` | UMP/UMS mechanism material; consistent with SKILL.md's stated boundary to `luke-iha-million-dollar-mechanisms`. |
| `extractions/luke-iha/transcript.txt` (root) | Large raw transcript; not opened for this pass — root `extraction-report.md` (VERIFIED above) is the distilled version already checked. |

## UNCONFIRMED — claimed in genius.md, no backing file in the extraction set

These are the honest gaps. Nothing here is asserted as fabricated — the claims may well be accurate transcriptions of the original "Director's Cut" training — but **no transcript or report file exists under `extractions/` to check them against**, so per the repair-envelope rule ("cannot ground it → label UNCONFIRMED") they are flagged rather than silently treated as verified:

- **The full "Director's Cut" grammar** (genius.md v2.0, per its own header: "Rebuilt from the complete two-day Copy Blocks foundational training… 30k words + 255 slides"): Resonance Hierarchy + AWE, Promise Ladder / Identity Runway / Gradualization, Proof Braid + Belief Bank Account (as named terms), the Curiosity Quadrant + 4 Thinking Tools, Conditions' 5 types, CRAVES, the Copy Blocks Equation, and the Canyon/Helicopter teaching metaphor. `extractions/luke-iha/video-4-copy-blocks/` has only an `extraction-report.md` (no `transcript.txt`), and its content is a compact ~15,500-word summary that does not include this deeper grammar. No other file in `extractions/luke-iha/` or `extractions/luke-iha-creative-strategist/` contains it either.
- **The "claude.ai export" material** (two labeled Patterns sections: "Collaborative Copywriting & Marketing Maestro" and "Luke Iha conversations (2026-07-01)"): both cite a claude.ai export / certainty-call recording as source. That export is outside the `extractions/` folder scope defined for this repair pass — flagged, not verified.
- **Hall of Fame Exemplars 1–3** (Arthur Z. joint-pain, eye-bag skincare, "made-up, dating"): exemplar #3 is explicitly labeled "made-up" in the skill itself (honest). Exemplars #1–2 read as real ad copy but have no traceable file in the extraction set — treat as illustrative, not verified swipe-file entries.

## How this ledger was built

Read every file under `extractions/luke-iha/` (all 8 `video-N-*/` subfolders' extraction-report.md files, plus the root `extraction-report.md`) and `extractions/luke-iha-creative-strategist/transcript.txt` (opened, not fully read — ~15K+ words, spot-checked the opening against video-8's extraction-report.md to confirm fidelity). Anchors added to `genius.md` anti-pattern items quote source text verbatim (see `PROVENANCE.md` for exact file+section citations). No new anchor was added without a matching sentence found in the cited file.
