# Phase B — Foundation

**Duration**: ~1 day. Sequential within phase.

## Required inputs

From Phase A:
- `_source/*.md` — canonical inputs
- `_working/A1-reconciliation.md` — conflict resolution
- `00-foundation/02-icp-master.md` — early draft

## Steps

### B1 — Brand Bible

Invoke `agents/brand-system-builder/` (HAS Write tool — saves directly to disk):

> Produce the canonical brand bible. 9 sections:
> 1. Spine (the one-sentence promise + mechanism)
> 2. The Person (ICP umbrella prose)
> 3. Voice signature + named patterns (preview — full doc in B3)
> 4. Visual direction (preview — full DESIGN.md in C1)
> 5. The Founding Story (long version; if pending voice memo, use placeholder marked PENDING)
> 6. Non-Negotiables (preview — full doc in B2)
> 7. Crystallized phrases (verbatim-use signature language)
> 8. The Enemies (sharpened "we are not X" lines)
> 9. Stage Evolution (where the brand goes from launch through year 1, 2, 5)

Output: `00-foundation/01-brand-bible.md` (~3500-4500 words).

### B2 — Non-Negotiables

Direct port from canonical inputs (`_source/founder-anchor*.md`):

> Copy the non-negotiables verbatim from the founder's anchor doc. Add:
> - "How To Use This Document" section (when to paste, how to triage decisions)
> - Sponsor decision template (pre-built triage prompt)
> - "Variations are sub-brands, not exceptions" clause (variations require a different name)
> - "What this document is not" section
> - "What happens when a line bends" surface-and-reset protocol

Output: `00-foundation/05-non-negotiables.md`.

### B3 — Voice Document

Run `/voice-document` (skill: `skills/voice-document/`):

> Produce voice document with:
> - 4-8 named voice patterns (e.g., anaphora, frame-then-sharpen, hell-yes filter, mechanic-as-sentence)
> - Each pattern: definition + 2-4 paired GOOD/BAD examples
> - ≥30 paired examples total
> - Banned phrases list (wince-list with 1-line reasoning per phrase)
> - Compressed paragraph for AI paste-in (1 paragraph, ≤120 words)
> - Voice test: "Would [founder] say this to a friend over coffee?"

Output: `00-foundation/03-voice-document.md` (~3000-4000 words).

### B4 — ICP Master finalization

The early draft from A2 is upgraded with:
- Final adjudication of PROPOSED profiles (founder review)
- 60% TAM rule (audience state breakdown)
- Cross-reference into voice patterns and Bridge Messages

Output: `00-foundation/02-icp-master.md` (final).

### B5 — Positioning One-Pager

Invoke `agents/master-copywriter/` (⚠️ NO Write tool — main thread saves output):

> Distill the brand to a single page. 400-500 words.
> Built around the spine line. Includes: who we are (one paragraph), the enemy (one paragraph), the mechanic (one paragraph), the proof (one paragraph), the call (one paragraph).
> For: press, decks, partner intros, fast handoff.

Output: `00-foundation/04-positioning-one-pager.md`.

**Save pattern** (for master-copywriter outputs):
```python
# Subagent returns content inline; main thread writes to disk
content = subagent_response  # the draft text
Path(output_path / "00-foundation" / "04-positioning-one-pager.md").write_text(content)
```

### B6 — Master Index

Invoke `agents/master-copywriter/` (same save pattern):

> Build the front-door doc for the BOS. Includes:
> - Hot Path table — 12-row table mapping common use cases to which doc to paste
> - 6-layer architecture overview
> - Cross-references to every layer
> - "Read once" vs "paste-every-session" distinction

Output: `00-foundation/00-master-index.md`.

## Output Schema

**Inputs**: 
- `_source/*.md` — Canonical inputs from Phase A
- `_working/A1-reconciliation.md` — Conflict resolution table
- `00-foundation/02-icp-master.md` — Early draft ICP from Phase A

**Outputs**:
- `00-foundation/01-brand-bible.md` — 9 sections (Spine, The Person, Voice signature, Visual direction, Founding Story, Non-Negotiables, Crystallized phrases, Enemies, Stage Evolution). ~3,500-4,500 words.
- `00-foundation/02-icp-master.md` — Finalized ICP Master (umbrella + 3-5 psychographic profiles, each with want/need/obstacle/nemesis/Bridge Message/audience-state mapping)
- `00-foundation/03-voice-document.md` — 4-8 named voice patterns (e.g., anaphora, frame-then-sharpen, hell-yes filter), each with 2-4 paired GOOD/BAD examples. ≥30 paired examples total, banned phrases list, compressed paragraph for AI paste-in. ~3,000-4,000 words.
- `00-foundation/04-positioning-one-pager.md` — Single page (400-500 words): who we are, the enemy, the mechanic, the proof, the call.
- `00-foundation/05-non-negotiables.md` — Founder's non-negotiables (verbatim from canonical) + "How To Use This Document" section + decision triage template + "Variations are sub-brands, not exceptions" clause.
- `00-foundation/00-master-index.md` — Front-door doc with 12-row Hot Path table (common use cases → which doc to paste), 6-layer architecture overview, cross-references to every layer.

**Purpose**: Lock the brand's spine (positioning, voice, ICP, non-negotiables). These 6 docs form the source-of-truth for all downstream work (visual, briefs, marketing, AI handoff).

**Quality Gate Checkpoint**:
- [ ] All 6 foundation docs exist
- [ ] Brand Bible covers 9 sections (founding story may be PENDING — note explicitly)
- [ ] Voice Document has ≥30 paired examples + named patterns
- [ ] ICP Master has umbrella + 3 profiles (PROPOSED OK if founder approved)
- [ ] Non-Negotiables is verbatim from canonical (not paraphrased)
- [ ] Positioning One-Pager is ≤500 words
- [ ] Master Index Hot Path table has ≥10 rows

If any unchecked, halt and complete. Foundation drift in Phase B compounds across the rest of the build.

---

## Quality gate (Phase B → C)

Before advancing to Phase C:
- [ ] All 6 foundation docs exist
- [ ] Brand Bible covers 9 sections (founding story may be PENDING — note explicitly)
- [ ] Voice Document has ≥30 paired examples + named patterns
- [ ] ICP Master has umbrella + 3 profiles (PROPOSED OK if founder approved)
- [ ] Non-Negotiables is verbatim from canonical (not paraphrased)
- [ ] Positioning One-Pager is ≤500 words
- [ ] Master Index Hot Path table has ≥10 rows

If any unchecked, halt and complete. Foundation drift in Phase B compounds across the rest of the build.
