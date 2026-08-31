---
date: 2026-08-06
session: sam-vander-wielen extract-forge
name: auto-caption-proper-nouns-poison-extraction-slug
problem_class: extraction / identity / mangled proper noun
domain: research
status: proven
problem_signature: "YouTube auto-captions consistently mangle an expert's name or domain and the extraction inherits the misspelling into the skill slug, so every wrapper, index, memory reference and future extension match keys off a name that is not the real person's"
tags: [extraction, captions, slug, identity, verification, youtube]
---
# Auto-caption proper nouns poison the extraction slug

**Date**: 2026-08-06
**Context**: `/watch` + `/extract-forge` on a 61-minute YouTube interview
**Cost of the miss**: a complete forge (12 workflows, 12 prompts, agent, registries, wrappers) built under a wrong expert slug, then fully renamed

## The problem

YouTube auto-captions **silently mangle proper nouns**, and an extraction that trusts them inherits the error into the *slug* — which is the one thing every downstream system keys on.

Concrete: the expert's surname is **Vander Wielen**. The captions rendered it:
- "Vanderland" (throughout)
- "San Vander" (at 33:10)
- "samvanderland.com" (her domain)

Nothing in the transcript flags this. The name is internally consistent across 2,093 caption segments, so no self-consistency check catches it. The whole skill got built as `sam-vanderland`.

## Why it matters more than a typo

A wrong slug is not cosmetic — it is **routing poison with a long tail**:
- `SKILL_INDEX.md` / `AGENT_INDEX.md` index the wrong name
- Minted wrappers, shims, and the expert front door all derive from it
- `/extract` **Extension Mode matches on the slug** — so the next source from the same expert creates a *duplicate expert* instead of extending
- Memory, `memory_facade.py`, and solution cards all reference the wrong name forever
- Any client-facing artifact misattributes a real person's name

## The fix

**Verify the expert's identity off-source BEFORE building anything.** One web search, thirty seconds, at Phase 1 — not at the verification gate.

Corroborate on **multiple independent identifiers**, not just the name. Here, five lined up and made the correction certain:

| Identifier | Caption | Verified |
|---|---|---|
| Name | "Sam Vanderland" | **Sam Vander Wielen** |
| Domain | samvanderland.com | samvanderwielen.com |
| Podcast | "On Your Terms" | On Your Terms® |
| Product | Ultimate Bundle | ✅ matched |
| Newsletter | Sam's Sidebar | ✅ matched — Tuesday cadence corroborated a transcript line |

Matching product/newsletter names are what confirm it is the *same person*, not a different one — that's why you check several, not just re-spell the surname.

## Rule

> **Never take a proper noun from auto-captions.** Any name, brand, domain, product, or book title that will become a slug, a file path, or a client-facing string gets verified off-source before the build starts.

Applies to: expert names, company names, product names, book titles, URLs, and cited third parties. Extraction workflows already require expert identification at Phase 1 — this is *why*.

## Also: leave the transcript unedited

`transcript.md` stays as the raw caption record, mangled names and all. It is the evidence. The correction belongs in the source ledger with the verification table, so a future reader can see both what the source said and what is true.

## Detection heuristic

Suspect caption mangling whenever a name is:
- an unusual or multi-word surname (space-separated surnames get fused)
- non-Anglophone
- rendered inconsistently anywhere in the transcript (here: "San Vander" at one point) — **one inconsistent rendering is the tell**
- attached to a domain that doesn't resolve

## Related

- `docs/solutions/2026-07-07-transcript-only-extraction-generic-output.md` — the other transcript-source scar (thin extractions). Different failure: that one is about *depth*, this one is about *identity*.
- `skills/sam-vander-wielen/references/source-ledger.md` — the correction table as shipped
