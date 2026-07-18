---
description: "/forge skill <concept> — Skill Forge lane, Stage 1: bare concept with no source material → receipts-backed grounding corpus → existing /extract-forge pipeline builds the full skill."
---

# Skill Forge — Bare Concept → Grounding Corpus → Full Skill

Dispatches `skills/forge-os/references/prompts-v2/grounding-sprint.md` (the engine — Stage 1 of
this lane; Stage 2 is the existing, unmodified `/extract-forge` pipeline). Status per `SKILL.md`:
**Stage 1 LIVE (Wave 2)**.

## Invocation

`/forge skill <raw intent>` when the operator wants a skill in a domain the system has never
extracted, or a THIN prior corpus needs a re-run after new source material appears.

## Stages

1. **Negative check** — `python3 execution/prompt_library.py search "<concept keywords>"` +
   `ls skills/ | grep -iE "<domain terms>"` + `DOMAIN_REGISTRY.md`; an owning skill already exists
   → STOP at verdict **ROUTE-EXISTING**, name it, write no corpus file.
2. **Multi-modal source hunt** — in-repo (`_active/`, `projects/`, `extractions/`,
   `research_outputs/`), Recall (`mcp__recall__search`), episodic memory (loose single-string
   queries, ≥2 phrasings before marking a modality empty), live web via `execution/research.py`
   at the approved tier only — **`--depth quick` is mandatory at the $0 tier**; running the
   default (Gemini-first, cost-gated) depth without it is a tier violation.
3. **Practitioner filter + assembly** — named practitioners' verbatim words and worked examples
   over generic listicle content; corpus lands at `extractions/grounding/<slug>-corpus.md`, 8-15
   load-bearing entries, each labeled VERIFIED / LIKELY / UNCONFIRMED.
4. **Readiness verdict** — exactly one of FORGE-READY / THIN / NO-BUILD / ROUTE-EXISTING, with a
   one-line reason.
5. **Handoff** — FORGE-READY corpus becomes the source for the existing `/extract-forge` pipeline;
   this lane never re-implements extraction.

## Output Schema

Exactly the three deliverables `grounding-sprint.md`'s own Output Contract names: (1) the corpus
file at `extractions/grounding/<slug>-corpus.md` with every entry carrying claim/method, verbatim
excerpt, receipt (URL / file path / `recall:<id>` / `episodic:<ref>`), and a VERIFIED/LIKELY/
UNCONFIRMED label; (2) the readiness verdict, stated once, with its one-line reason; (3) a 5-8
line Sprint Receipt (modalities swept with hit counts, practitioners found, confidence
distribution, research tier actually used, handoff command) written inside the corpus file AND
repeated in the final message. A ROUTE-EXISTING verdict writes NO corpus file — that is correct
behavior, not an incomplete run.

## Quality Gate

- Negative check ran BEFORE any hunting, result stated (this lane never duplicates an owning
  skill's corpus).
- Every entry carries a real receipt — zero training-memory entries; a synthesized-research file
  path caps its entry at LIKELY unless the underlying source was actually chased.
- Entries are practitioner-specific (names, mechanisms, verbatim words), not generic best-practice
  filler — filler gets dropped, not padded in to hit the ceiling.
- The verdict is honest to the density gate: <8 load-bearing entries declares THIN or NO-BUILD,
  never a padded FORGE-READY.
- The stated research tier matches what actually ran (`--depth quick` at $0, no silent escalation).
