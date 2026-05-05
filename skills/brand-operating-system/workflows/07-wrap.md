# Phase G — Wrap

**Duration**: ~half-day. Sequential.

## Required inputs

All 43 docs from Phases B-F. Plus the canonical inputs in `_source/`.

## Steps

### G1 — Adversarial Review

Invoke `agents/adversarial-reviewer/` (⚠️ NO Write tool — main thread saves output):

> Stress-test the entire BOS on 5 axes:
> 1. **Premise integrity** — Does the spine hold across all 43 docs?
> 2. **Evidence quality** — Are claims grounded? Reddit/external research gaps flagged?
> 3. **Voice alignment** — Do the docs teach voice or just describe it?
> 4. **Structural soundness** — File numbering consistent? Cross-references accurate?
> 5. **Market resilience** — Survives skeptical journalist? High-status partner? ICP profile?
>
> Score each axis 1-10. Identify top 5 fixes ranked CRITICAL / HIGH / MEDIUM with effort estimates.
>
> Run survival tests:
> - Skeptical journalist + press one-sheeter
> - High-status partner + DJ booking pack (or equivalent partner brief)
> - B2B venue manager + venue pitch
> - Hunter applying via why-gate
> - Real sponsor offer + non-negotiables
> - Founder on tough day + drift signals readback

Output: `_working/G1-adversarial-review.md`.

**Save pattern**: Subagent returns content inline → main thread writes:
```python
content = subagent_response
Path(output / "_working" / "G1-adversarial-review.md").write_text(content)
```

**Halt rule**: If any axis scores <6, fix CRITICAL items inline before proceeding. HIGH/MEDIUM can ship as v1.1 backlog.

### G2 — Prose Doctor

Invoke `agents/prose-doctor/`:

> Voice consistency scan across all 43 docs. Catch:
> - Em-dash count per file (rule: ≤2 per major section, ≤4 per long doc)
> - Banned phrases from voice document
> - Banned structural moves: "It's not X. It's Y." reveals, twin-aphorism endings, triple-beat anaphora outside the named pattern, italicized mid-paragraph aphorisms, "Here is the part nobody..." framing, mic-drop endings, cross-piece rhythm repetition
> - Cross-piece variance audit: no two docs should share a closing move or transition gesture

Output: `_working/G2-prose-scan.md` — file-by-file violation report.

**Halt rule**: 0 banned-move violations required. ≤2 em-dash violations across the entire BOS acceptable for v1; HIGH-priority backlog otherwise.

### G3 — Drive upload (only if `--drive-parent <folder_id>` supplied)

```bash
python3 execution/md_to_gdoc.py \
    <output>/ \
    --drive-parent <folder_id> \
    --mirror-folders \
    --create-folder "$(date +%Y-%m-%d) — Brand Operating System v1"
```

This:
1. Creates a dated subfolder under the supplied Drive parent
2. Mirrors the local 6-layer folder structure (00-foundation, 01-visual, ..., 05-ops, _source)
3. Excludes `_working/` (intermediate artifacts, not for delivery)
4. Uploads each .md as native Google Doc with auto-pageless via `set_pageless()`

**Verification**:
```bash
# Confirm 43 native Google Docs in Drive (not raw .docx)
# Manual: open Drive folder, count native docs vs other mimetypes
```

If `--drive-parent` not supplied: skip G3, print local-only instructions for manual upload later.

### G4 — Chain finalize

```bash
python3 execution/chain_runner.py finalize "<Brand> Brand Operating System v1" \
    --expert "brand-system-builder" \
    --skill "brand-operating-system" \
    --workflow "build-bos" \
    --type "Client Work" \
    --intent 9 \
    --expert-score 9 \
    --adversarial 8 \
    --notes "<Brand> BOS v1 — 6 layers, 43 docs, AI-pasteable | Factual Grounding: 9 | Verification: PASS"
```

This:
1. Runs the 4-dimension quality gate
2. Logs to Notion Performance Log
3. Registers in revenue tracker (if Client Work)
4. Captures in protocol activation tracking

**Halt rule**: Composite must be ≥7. If <7, retry the weakest dimension's section once, then re-finalize. Do not ship at <7.

## Quality gate (Phase G → done)

Before declaring v1 shipped:
- [ ] G1 adversarial review composite ≥7/10
- [ ] G2 prose scan: 0 banned-move violations, ≤2 em-dash violations
- [ ] If `--drive-parent` supplied: 43/43 native Google Docs in Drive, 0 raw .docx
- [ ] Chain finalize composite ≥7
- [ ] All 4 quality dimensions ≥6 (Intent / Expert Standard / Adversarial / Factual Grounding)
- [ ] No CRITICAL fixes from G1 unaddressed
- [ ] Founder has been informed of any PROPOSED items requiring adjudication (ICP profiles, voice memo, etc.)

## Post-ship

The BOS is now live. Three things happen next:
1. **Founder operates from it** — paste the AI Brain Master into Claude/ChatGPT to start producing content
2. **Amendments cascade** — when the founder names a change, the update protocol governs how it ripples through the 43 docs
3. **v1.1 schedules** — backlog from G1 (HIGH/MEDIUM fixes) + any new gaps surfaced during first cycle of operation merge into v1.1
