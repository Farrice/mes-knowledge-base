---
date: 2026-07-23
session: lakajev-conversation-layer
tier: operator-guide
status: enriched
---

# Matthew Lakajev A-Tier Blind Pass — What We Proved 2026-07-23 and How to Rerun It

> This session promoted `skills/matthew-lakajev-linkedin` v3.0 to **A-tier** via a Farrice-judged blind pass (EVAL-054) run the honest way: an artifact-only specimen a fresh agent generated from the shipped skill files alone, judged blind against two verbatim real Lakajev posts — and Farrice **preferred the generated one**. The capability manual for the skill itself is [2026-07-21-matthew-lakajev-forge.md](2026-07-21-matthew-lakajev-forge.md) — this guide covers the verification protocol, the reusable corpus trick, and what the verdict changed. Ledger: `extractions/matthew-lakajev-linkedin/blind-pass-log.md`.

## ⚡ If you only read 10 lines

- **Verdict**: Farrice ranked the generated post strongest of three ("felt the best from his perspective"), correctly dated both real posts as 2023-era. Recognition test: indistinguishable AND preferred → A-tier.
- The honest protocol (per `docs/solutions/2026-07-16-rubber-stamp-blind-pass-artifact-only-retest.md`): a **fresh agent loads ONLY SKILL.md + genius.md + one Tier-1 workflow + its v2 prompt** — no transcript, no corpus, no session context — and executes a real brief.
- Conductor-written specimens are soft rubber stamps: the 07-21 EVAL-053 (written with full transcript in context) was superseded, not trusted.
- Corpus collection for LinkedIn experts: `WebSearch site:linkedin.com/posts/<handle>` → `WebFetch` each permalink with an "if authwall, say AUTHWALL" prompt — ~half render logged-out. Card: `docs/solutions/2026-07-21-linkedin-authwall-corpus-via-public-post-permalinks.md`.
- Corpus gate: `python3 execution/blind_pass.py prepare --expert <skill-dir>` (needs ≥2 provenance-lined pieces NOT quoted in the skill files).
- Record: `python3 execution/blind_pass.py record --expert <skill-dir> --verdict PASS|FAIL --notes "..." --generated <path> --reference <path>`.
- Present the lineup **unlabeled in plain chat text** — AskUserQuestion preview panes did not render for Farrice; posts must be visible in the message body.
- A FAIL on a *real* piece is information, not noise: Farrice failing the real 2023 GPT-4 post located **corpus staleness**, not skill weakness.
- Known caveat: both corpus posts are Sept/Oct 2023 — refresh with 2026-era public posts when fetchable.
- Taste signal banked: heavy unicode-formatted process posts are authentic-Matt but not-Farrice — when `/ml-*` output ships under Farrice's name, voice-os BLEND governs the surface.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `python3 execution/blind_pass.py prepare --expert <skill-dir>` | Corpus-gate verdict + exact collection instructions | Before any blind pass; any skill stuck at "A-tier pending" |
| `python3 execution/blind_pass.py record --expert <skill-dir> --verdict ... --generated ... --reference ...` | EVAL entry + ledger line | After the human/model side-by-side judgment |
| `python3 execution/skill_auditor.py check --skill <skill-dir>` | 6-check heartbeat gate (tier-capping) | Cheap deterministic re-verify; can't be flattered |
| `/ml-closed-lost` · `/ml-six-gates` · 11 more `/ml-*` | See the [07-21 manual](2026-07-21-matthew-lakajev-forge.md) | Deploying the now-A-tier skill |

## The mental model

1. **The blind pass tests artifacts, not the conductor.** Whoever read the source transcript can imitate the expert from memory; only a context-free agent proves the *files* carry the voice. If the specimen was written in the build session, the pass is decorative.
2. **"Blind" means the judge can be wrong in both directions** — and both directions are data. Farrice failing a real post didn't break the test; it dated the corpus. Preferred-over-real is the ceiling verdict, and it's only meaningful because the real posts could lose.
3. **Trust the ledger, not the claim.** A verdict without `--generated`/`--reference` paths behind it is a rubber stamp regardless of notes (the 07-16 Jenny Hoyos lesson, applied successfully here).

## What the verdict changed

- **A-tier confirmed** for `matthew-lakajev-linkedin` — recorded in blind-pass-log.md (EVAL-054), project memory, and the 07-21 guide's payload block. The "extend never rebuild" rule now protects an A-tier asset.
- **Signal Pilot deployment unblocked** with a voice rule attached: Lakajev supplies conversation *mechanics*; Farrice's BLEND voice supplies the *surface*. Handoff ready: `.agent/handoffs/2026-07-23-lakajev-conversation-layer.md` (thread `lakajev-conversation-layer`).
- **Protocol precedent**: this is the first A-tier promotion earned through artifact-only regeneration + operator blind judgment end-to-end. The same sequence (prepare → fetch corpus → fresh-agent specimen → unlabeled lineup → record) is the template for the other skills waiting on "A-tier awaits Farrice blind pass" (Jenny Hoyos, Ben Watkins, Matthew Lakajev conversation predecessors, Paolo Trivellato, Ray Amjad, Baldacci, Satori v3).

## Honest edges

- **One judge, one specimen, one deliverable type.** The pass covers post-voice; DM scripts and audit outputs were never blind-tested. If `/ml-opinion-ladder` output feels off in deployment, that's untested surface, not contradiction.
- **Corpus is thin and old**: two pieces, both 2023. The gate minimum was met, not exceeded. Refresh before the next re-verify.
- **Farrice knew a test was coming** and which topics the corpus covered (from the prior closeout summary) — mitigated by the fresh specimen using a different topic, but a fully naive judge this was not.
- The AskUserQuestion preview surface failed once for exactly this use case (side-by-side long texts); until that changes, lineups go in message body text.

## Composition (options, not pipeline)

| Stack | When it earns its cost |
|---|---|
| This protocol × any "A-tier awaits blind pass" skill | The skill's expert publishes anywhere publicly fetchable (LinkedIn permalinks, Substack, YouTube transcripts) |
| Blind-pass FAIL × diction ratchet (07-16 card step 3) | The judge names a tell — write it into genius.md + prompt Quality Gates before the single retry |
| A-tier Lakajev × Signal Pilot | Every send-lane deliverable; campaign scarcity must match real pilot capacity |
