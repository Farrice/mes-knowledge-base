---
name: dump
description: "/dump — throw any raw, tangled thought at the Chief of Staff at any hour: it captures verbatim, visibly detangles the separate things inside it, routes each to its home (thought-bank, memory, open loops, parked, goals), and offers — never performs — the next step. The pressure valve between /cos briefings."
expert: Chief of Staff OS
domains: system, personal, capture, content
---

# /dump

> **Skill**: `chief-of-staff-os`
> **Workflow**: `workflows/cos-dump.md`

Read and execute `skills/chief-of-staff-os/workflows/cos-dump.md`. Load
`skills/chief-of-staff-os/genius.md` first (Detangle Rule + Capture Discipline).

## Deterministic capture spine (2026-07-06)

Capture Discipline's `python3 execution/cos_prep.py capture --route inbox --text "..."`
call (content sparks → thought-bank) now delegates to
`execution/thought_bank.py capture` under the hood — one writer, one entry
format (`## HH:MM — <first 8 words>`), and a mirror into the sovereign episodic
tier (`tier=episodic, category=milestone, source=thought_bank`) so the fragment
flows into the existing weekly distill → `flagged_review` → `memory_review.py`
pipeline like every other episodic record. Nothing about the cos-dump.md
routing steps changes — this just guarantees the write actually lands instead
of depending on the conversation remembering to make it.

For a content spark that should skip the journal mirror entirely, invoke the
sink directly: `python3 execution/thought_bank.py capture "<text>" --theme <t> --source dump`.

**Nightly backstop**: `execution/harvest_memory_daily.py` (launchd, daily) scans
the last 24h of episodic exchanges for user turns opening with `/dump`,
`thought:`, `note to self`, or `capture this`, and appends any not already in
today's inbox file (deduped by normalized first-60-chars) — the physical
guarantee for the case where a dump session happens but the capture call gets
skipped mid-conversation.
