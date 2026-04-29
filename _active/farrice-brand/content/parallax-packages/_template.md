---
edition_number: 0N
title: "[Edition Title]"
slug: 0N-[slug]
status: draft   # draft | review | scheduled | published | archived
publish_date: YYYY-MM-DD
publish_day: [Monday]
notes_published: 0/5
source_edition: ../substack-v2-drafts/0N-[slug].md
source_prompt_pack: ../prompt-packs/0N-[slug].md
---

# Edition 0N — [Title]

> **Status**: draft → review → scheduled → published
> **Last reviewed**: [date]
> **Notes posted**: 0/5

---

## 🎯 Ship Checklist

Walk these before publishing. Top-down. No shortcuts.

- [ ] Edition body voice-checked (no "Here's what/why/how" openers, ≤2 em dashes per piece)
- [ ] Edition body structural-tells audited (no banned moves — see bottom of file)
- [ ] Prompt pack tested in Claude or ChatGPT (you ran it yourself, output landed)
- [ ] Subject line tested for inbox preview truncation (~50 chars before cut)
- [ ] Preview text reads as a complete teaser (not a continuation of subject)
- [ ] All 5 Notes drafted and structurally varied (no repeated formats back-to-back)
- [ ] First Note scheduled (T-2 days minimum)
- [ ] Section assignment correct (`Editions`)
- [ ] Internal links work (manifesto reference, prior editions, prompt pack)
- [ ] One quotable line identified for restack-bait Note (Note 3 slot)
- [ ] Mobile preview checked (Substack iOS app)

---

## 📧 Substack Post — Copy-Paste Block

### Subject Line
```
[paste subject line — keep ~40-50 chars to avoid truncation]
```

### Preview Text
```
[paste preview text — completes the hook from subject, NOT a continuation]
```

### Section
`Editions`

### Tags
[3-5 tags for SEO/discoverability — e.g., `psychology, identity, AI, creativity`]

### Body

> Paste everything below this line as the post body, including the prompt pack section.

---

[FULL EDITION BODY GOES HERE]

---

### Paired Prompt Pack

[FULL PROMPT PACK BODY GOES HERE — embedded at bottom of edition]

---

## 📱 Notes Batch — Launch Week (5 Notes)

> All 5 Notes follow the **Notes Trailer Playbook** at [NOTES_TRAILER_PLAYBOOK.md](NOTES_TRAILER_PLAYBOOK.md). Each is one of 5 archetypes deployed across launch week. Schedule via Substack "Schedule for later." Notes are **trailers, not clips** — original compositions in manifesto voice that prime readers, not extractions of edition lines.

### Note 1 — Origin Wound (T-2 days)
**Archetype**: Story Note + Statement hook
**Schedule**: 2 days before publish, mid-day
**Status**: [ ] drafted [ ] scheduled [ ] posted

```
[paste Note 1 body — concrete opening (dollar amount/named thing/dated moment, 7-10 words), 2-3 sentences personal narrative, line that hints at thesis without spoiling, edition tease. 32-63 words. Statement hook, NOT question.]
```

**Voice Test (5/5 required)**: ☐ concrete opening ☐ authorship test ☐ rhythm varies ☐ slot-machine close ☐ standalone-readable

---

### Note 2 — Asset Drop (T+0 morning)
**Archetype**: Copy-Paste Asset (3.4x conversion lift) + Statement hook
**Schedule**: Publish day, within 1 hour of edition going live
**Status**: [ ] drafted [ ] scheduled [ ] posted

```
[paste Note 2 body — statement hook framing a question/framework, 3-5 lines of usable asset (a question to ask, prompt to run, checklist, framework), 1 line context tying to edition + link. The asset must be useful WITHOUT the edition.]
```

**Voice Test**: ☐ concrete opening ☐ authorship test ☐ rhythm varies ☐ slot-machine close ☐ standalone-readable

---

### Note 3 — Counterintuitive Truth (T+0 evening, restack-bait)
**Archetype**: Single resonant line + minimal context
**Schedule**: 8-12 hours after Note 2
**Status**: [ ] drafted [ ] scheduled [ ] posted

```
[paste Note 3 body — one contrarian wisdom statement (the edition's most quotable line, possibly verbatim), one expansion line, one context line + link. The quoted line must stand on its own when restacked.]
```

**Voice Test**: ☐ concrete opening ☐ authorship test ☐ rhythm varies ☐ slot-machine close ☐ standalone-readable

---

### Note 4 — Public Reckoning (T+2 to T+3)
**Archetype**: Vulnerable admission + Statement hook
**Schedule**: 2-3 days after publish
**Status**: [ ] drafted [ ] scheduled [ ] posted

```
[paste Note 4 body — statement hook with a personal stance/admission (NOT a question hook — 52% conversion penalty), 2-3 sentences expanding with specificity, connection to edition's territory from a different angle than Note 1, soft conditional invitation + link.]
```

**Voice Test**: ☐ concrete opening ☐ authorship test ☐ rhythm varies ☐ slot-machine close ☐ standalone-readable

---

### Note 5 — Bridge to Edition 0(N+1) (T+5 to T+6)
**Archetype**: Forward tease / anticipation Note
**Schedule**: Day before next edition drops
**Status**: [ ] drafted [ ] scheduled [ ] posted

```
[paste Note 5 body — statement hook naming next edition's thesis without delivering it (7-10 words), 1-2 sentences signaling territory, drop date for next edition. Avoid "It's not X. It's Y." reveal patterns. Single declarative thesis sentence.]
```

**Voice Test**: ☐ concrete opening ☐ authorship test ☐ rhythm varies ☐ slot-machine close ☐ standalone-readable

---

### Cross-batch audit (run before scheduling Note 1)

- [ ] **Em dash count across all 5 Notes**: target 0, max 1 (manifesto rule ≤2; Notes target tighter)
- [ ] **Italicized words**: 0 or 1 per Note, never phrases (manifesto convention: single resonant words like `*noise*`, `*alive*`)
- [ ] **Structural variance**: All 5 Notes use distinct opening patterns and closing gestures
- [ ] **Hook discipline**: All 5 are statement hooks (no questions). Statement hooks drive 52% more subscriber conversions per 19,471-Note research.
- [ ] **Length sweet spot**: 32-63 words per Note (Bridge can be tighter)
- [ ] **Banned moves clear**: No "It's not X. It's Y." reveals, no twin-sentence aphoristic endings, no triple-beat anaphora unless quoted from manifesto
- [ ] **Voice DNA**: Each Note hits ≥3 of 5 voice fingerprints (concrete opening / disparate-domain parallel / italicized single word / question-into-answer cadence / contrarian wisdom frame)

---

## 🗂️ Notion Sync Checklist

Log this Edition to Notion in the right order. Each step has a different timing.

### Pre-publish (during draft + review)
- [ ] **Content Pipeline DB**: Create row with Edition #, Title, Status=Draft, Target publish date
- [ ] Update row to `Status: Scheduled` once first Note is scheduled

### At publish
- [ ] **Content Pipeline DB**: Update row to `Status: Published`, paste live URL
- [ ] **Knowledge Vault DB**: Auto-triggered if `chain_runner.py finalize` was run with quality ≥7. Otherwise manual: `python3 execution/notion_api.py vault-create "[Title]" --expert farrice-brand --domain [domain]`

### Post-publish (48-72h after)
- [ ] **Performance Log DB**: Add row with Open rate, Click rate, Subscribes from this edition, Notes engagement totals
- [ ] **Knowledge Vault**: Add post-publish notes (what worked, what didn't, structural lessons) to the existing row

---

## 🔗 Source Files

- **Edition working draft**: [substack-v2-drafts/0N-[slug].md](../substack-v2-drafts/0N-[slug].md)
- **Prompt pack working draft**: [prompt-packs/0N-[slug].md](../prompt-packs/0N-[slug].md)
- **Strategy brief / research**: [link if applicable]

> **Source-of-truth rule**: Once this package is created and you start the ship checklist, THIS package becomes the canonical version. The `substack-v2-drafts/` and `prompt-packs/` files are working drafts only — edits made there after this package is sealed will not flow through automatically.

---

## 🚨 Voice + Structural-Tells Audit (Pre-Publish)

Quick gut-check before you ship. If any of these fire, fix and re-audit.

### Banned MOVES (not just phrases — see [feedback_ai-structural-tells.md](../../../../../.claude/projects/-Users-farricecain-Google-Antigravity/memory/feedback_ai-structural-tells.md))

- [ ] No "It's not X. It's Y." reveal patterns
- [ ] No twin-sentence aphoristic endings
- [ ] No triple-beat anaphora (unless quoted from your own prior writing)
- [ ] No italicized mid-paragraph aphorisms
- [ ] No "Here is the part nobody talks about..." framing
- [ ] No mic-drop + deflation closing structure
- [ ] Cross-piece rhythm check: does this edition repeat the structural shape of the previous edition? If yes — vary.

### Banned PHRASES (from [feedback_ai-writing-tells.md](../../../../../.claude/projects/-Users-farricecain-Google-Antigravity/memory/feedback_ai-writing-tells.md))

- [ ] No "Here's what/why/how..." openers
- [ ] Em dashes ≤ 2 per piece
- [ ] No structural tropes lifted from prior editions

### Voice gut-check

- [ ] Reader-as-protagonist where applicable (especially profile/About-style sections)
- [ ] Show-don't-tell at sentence level (specific moments, not abstract benefits)
- [ ] "Would Farrice say this to a friend?" — if no, rewrite
- [ ] No forced jargon ("dangerous in a room" — banned)
- [ ] Pull-through: the edition has a real open loop, not "more on this soon"
