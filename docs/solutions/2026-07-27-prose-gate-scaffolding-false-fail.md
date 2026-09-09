---
date: 2026-07-27
session: teardowns x3 + LinkedIn profile
name: prose-gate-scaffolding-false-fail
problem_class: content / QA gate / scaffolding false fail
domain: content
status: proven
problem_signature: "prose_classifier flags a finished document as 10/10 AI on em dashes, headers, arrows, and parallel blocks that all come from markdown scaffolding rather than from the copy that actually ships inside the fenced blocks"
tags: [prose-classifier, gates, ai-slop, delivery, false-positive]
---
# Solution Card — prose_classifier fails whole documents when only the fenced blocks ship

**Date:** 2026-07-27 · **Domain:** content QA / delivery gates · **Session:** teardowns x3 + LinkedIn profile

## The problem

Ran `prose_classifier.py check` on three finished teardown documents. All three came back **FLAGGED, AI Score 10/10**, with `Expert Standard capped at 6`.

The flagged signals were:
- `em_dash_overuse` — 14 to 18 em dashes per file
- `town_crier_register` — "CREDIT WHERE IT", "WHAT THE CUSTOMERS ACTUALLY SAY"
- `structural_emoji` — "Wide → Deep", "CLAIM → PROOF → GAP"
- `parallel_structure_overuse` — 9 to 10 blocks

Every single one of those came from **document scaffolding**: markdown section headers, metadata rows, and `— Reviewer Name` quote attributions. None of it ships. The actual shipped copy is inside fenced code blocks.

Taking the verdict at face value would have triggered a rewrite of clean prose to satisfy a gate that was reading table-of-contents furniture.

## The fix

Gate the shipped blocks, not the document. Extract every fenced block, write each to its own file, run the classifier on those.

```python
import re, pathlib
for f in sorted(pathlib.Path(SRC_DIR).glob("*.md")):
    for i, b in enumerate(re.findall(r"```\n(.*?)\n```", f.read_text(), re.S)):
        (OUT / f"{f.stem}-b{i+1}.txt").write_text(b)
```

Then run `prose_classifier.py check` per block, plus a mechanical scan for the Farrice-specific bans the classifier doesn't cover: em dash present at all, `here's what/why/how`, `it's not X. it's Y.`, and a trailing `?` (question close).

## The result

Same three files, gated correctly:
- Teardown 1 post: **CLEAN 0/10**
- Teardown 2 post: **WARNING 2.0** → one real `contrast_reveal_antithesis` ("That's not a scandal. It's a mirror.") → rewritten → **CLEAN 0/10**
- Teardown 3 post: **CLEAN 0/10**
- About section regression: **CLEAN 0/10**

The block gate also caught three real violations the document-level run had buried in the noise: em dashes in all three DM greetings (`Hey [name] — `) and signatures (`— Farrice`), an em dash in a LinkedIn job title, and a `here's why` inside an Experience description.

## The rule

**Gate what ships, not what you wrote it in.** A document-level prose score on a file that is 60% scaffolding measures the scaffolding. The block-level run is both stricter on real copy and quieter on furniture, which is the only combination that keeps a gate trustworthy.

Corollary: a gate that cries wolf gets ignored, and an ignored gate is worse than no gate. The 10/10 FLAGGED verdict on genuinely clean prose is exactly how a binding check becomes advisory.

Related: [[feedback_ai-slop-ban-bank]] · [[feedback_ai-memory-dependent-observability]]
