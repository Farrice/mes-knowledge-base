# Prosperity Coach System — Source Ledger

Claim-by-claim provenance for `skills/prosperity-coach-system/genius.md` and `SKILL.md`. Labels: **VERIFIED** (exact or near-verbatim match located in a named source, checked during this repair pass, 2026-07-18), **LIKELY** (theme/mechanism grounded in a named source, but the exact wording in the skill file is a light paraphrase, a compressed list, or the extraction's own synthesized "Success Metric," not a verbatim quote), **UNCONFIRMED** (could not be located in any available source; none found in this pass — see summary).

## Primary Sources (existence + size verified this pass)

| ID | Source | Path | Size | Notes |
|---|---|---|---|---|
| S-P1 | "PROSPERITY COACH SYSTEM" (claude.ai project export) | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/projects/0198ed9a-7175-769c-9230-b32b41f7e64f.md` | 35,068 bytes | Full 3-part coaching system (Custom Instructions of a claude.ai Project, created 2025-08-27). Contains the Troubleshooting Guide, Factor Stacking Method, Prosperity Spiral, Prosperity Debugging Protocol, Success Story Templates, Response Quality Checklist, Crisis Intervention Protocols, Daily Practice Frameworks, and Deployment Instructions that genius.md's Genius Patterns and Hidden Knowledge sections are built from almost line-for-line. Extracted directly from the archive this pass via `python3 tarfile` (member confirmed present, non-empty, readable — not the "0-byte/unrecoverable" failure mode the envelope warns against). |
| S-P2 | "Prosperity Algorithm Context Profile" (claude.ai project export) | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/projects/0199139f-4327-7717-88fc-154a86b034ba.md` | 26,439 bytes | A structured JSON "context profile" version of the same system (created 2025-09-04), explicitly labeling `"source": "Jason Fladlien 2021 Prosperity Algorithm Webinar"`. Contains the 10-factor breakdown with named frameworks (e.g. `152_day_recovery`, `tesseract_rotation`, `worthiness_accelerator`) and per-factor `diagnostic_markers.excess` / `.deficiency` lists used for the Anti-Patterns section added in this repair. Extracted and read in full this pass. |
| S-T1 | `extractions/Jason Fladlien/transcript.txt` | (repo root) | 89,775 bytes | Damon-hosted interview transcript (limiting beliefs, NLP, monk background, persuasion physics). Checked this pass with a Python regex scan for "prosperity" (case-insensitive): **one hit**, a single incidental use of the word in a sentence about "the beauty of... having a human's condition and a soul... this is how I think about it from the that view of prosperity" — not the 10-factor Prosperity Algorithm system. This transcript is **not** the source of the skill's core content. |
| S-T2 | `extractions/jason-fladlien/transcript.txt` | (repo root) | 91,971 bytes | Matthew-hosted interview transcript (webinar closes, offer architecture, radical candor). Checked this pass with the same regex scan: **zero hits** for "prosperity." Confirmed not the source of this skill's core content (it is, however, the primary source for the separate `jason-fladlien-marketing` skill). |

**How S-P1/S-P2 were located**: SKILL.md's front-matter already declared `source: "claude.ai project export (2026-07-01)"`. `extractions/jason-fladlien` and `extractions/Jason Fladlien` (the only Fladlien-named dirs) were checked first and ruled out (S-T1/S-T2 above) as the wrong material for this specific skill. Per the envelope's source-search discipline, a `python3 tarfile` scan was then run against `_archive/claude-export-2026-07-01.tar.gz` (7,728 members; 7,708 `.md` files scanned) for the literal phrase "prosperity algorithm" (case-insensitive) — 9 hits, two of which live under `.../normalized/projects/` (matching "project export" in the SKILL.md source line) and turned out to contain the coaching system nearly verbatim. The other 7 hits (conversation-level exports) were not needed once S-P1/S-P2 confirmed as the primary match and were not opened this pass.

---

## Genius Patterns (genius.md §Genius Patterns)

| Pattern | Status | Anchor |
|---|---|---|
| Block Diagnosis Behind the Complaint — "I don't have time," 142 min scrolling, 15 min at 5:45am | VERIFIED | S-P1, Block 1: "How many minutes today did you spend scrolling? (Average: 142 minutes)... 15 minutes at 5:45am before the world wakes up. Non-negotiable." |
| Block Diagnosis — Colonel Sanders 65, Laura Ingalls Wilder 64 | VERIFIED | S-P1, Block 4, verbatim: "Colonel Sanders was 65 when KFC started. Laura Ingalls Wilder didn't publish Little House until 64." |
| Block Diagnosis — 13.7 billion years of unfairness | VERIFIED | S-P1, Block 5, verbatim: "The universe has been unfair for 13.7 billion years." |
| The Paradox Breaker (security vs. purpose; Structure Freedom Paradox) | VERIFIED | S-P1, Pattern 1, near-verbatim; factor name confirmed in S-P2 §`2_structure_freedom` |
| The Resistance Dissolver (Polarity Flip, 17 minutes, minute 18, minute 10) | VERIFIED | S-P1, Pattern 2, verbatim: "Tomorrow at 2pm, you're going to NOT do the thing for exactly 17 minutes... At minute 18... Most people crack at minute 10." |
| The Worthiness Installation (100,000 heartbeats; 4-question Worthiness Archaeology; mirror line) | VERIFIED | S-P1, Pattern 3, verbatim: "Your heart beat 100,000 times today without asking if you deserve it"; "My worthiness is not up for debate. It's the foundation I build on." |
| Factor Stacking (Binary Pairs / Triple Stacks / Full Integration, all listed combinations) | VERIFIED | S-P1, "The Factor Stacking Method," verbatim list match for all three layers |
| The Prosperity Spiral (Week 1-8 breakdown) | VERIFIED | S-P1, "The Prosperity Spiral Technique," near-verbatim |
| The Prosperity Debugging Protocol (5-step: System Check → Reboot Sequence) | VERIFIED | S-P1, "The Prosperity Debugging Protocol," verbatim |
| Adversity-as-Advantage — "an advantage aimed wrong" | VERIFIED | S-P1, Block 5, verbatim: "Every disadvantage is an advantage aimed wrong." |
| Adversity-as-Advantage — "You've earned the right to tell a victim story..." | VERIFIED | S-P1, "The Victim," verbatim |
| Adversity-as-Advantage — Regression Analysis 4 questions; "We don't start over..." | VERIFIED | S-P1, Protocol 3, verbatim |
| All "Success Metric" lines throughout Genius Patterns | LIKELY | These are the extraction's own synthesized pass/fail criteria for each pattern — thematically consistent with the source's goal-language but not verbatim source sentences; none are presented as direct quotes in genius.md. |

## Hidden Knowledge (genius.md §Hidden Knowledge)

| Item | Status | Anchor |
|---|---|---|
| The Universal Response Shape (9-beat checklist) | VERIFIED | S-P1, "Response Quality Checklist" — all 9 items match (assessed state / factor need / example / 24hr action / 30-day connection / compassionate directness / paradox / vulnerability / next step) |
| Crisis Overrides Coaching — "starts with being alive to run it" | VERIFIED | S-P1, Protocol 2, verbatim: "The prosperity algorithm starts with being alive to run it." |
| Crisis Overrides — 988, Text HELLO, ER, someone who loves you | VERIFIED | S-P1, Protocol 2, verbatim resource list |
| Crisis Overrides — 5-4-3-2-1 grounding | VERIFIED | S-P1, Protocol 1, verbatim |
| Posture Handlers — Skeptic / Know-It-All / Victim / Perfectionist | VERIFIED | S-P1, "Special Situations Handling," near-verbatim for all four ("you've lost nothing"; "let's build YOUR unique algorithm from what you already know"; "fear in a productivity costume"; "Version 1.0 - Feedback welcome") |
| Micro-Actions / 70% beats 100% that hides / "Ready never comes" | VERIFIED | S-P1, "Final Prosperity Coach Principles" #2-3, and Block 4, verbatim |
| Continuity — session bridging, progress tracking, story threading | VERIFIED | S-P1, "Conversation Continuity Techniques," near-verbatim for all three sub-patterns |

## SKILL.md claims

| Claim | Status | Anchor |
|---|---|---|
| "Jason Fladlien's Prosperity Algorithm coaching" | VERIFIED | S-P2 meta: `"source": "Jason Fladlien 2021 Prosperity Algorithm Webinar"` |
| The 10 Factors (Purpose, Structure, Flexibility, Persistence, Adversity, Leverage, Unfairness, Luck, Expertise, Imperfection) | VERIFIED | S-P2 §`prosperity_factors` keys 1-10 match (compressed naming; e.g. S-P2's `2_structure_freedom` → SKILL.md's "Structure") |
| "Jason: former monk with PTSD, slept on floors, 152 days, built a multi-million-dollar business" | VERIFIED | S-P1, Block 4/1, verbatim "34-year-old former monk with PTSD sleeping on floors... building a multi-million dollar business"; "152 days" verbatim in S-P1 "The Victim" and S-P2 §`7_wonderful_unfairness.frameworks.152_day_recovery` |
| Crisis hard override (harm intent, suicidal ideation, reality detachment) | VERIFIED | S-P1 "Emergency Protocols" + "Crisis Intervention Protocols"; S-P2 §`intervention_protocols.suicide_risk` |

## New content added in this repair pass

| Item | Status | Anchor |
|---|---|---|
| "How to Use This Skill" quote — "feel like Jason Fladlien himself is mentoring the user — vulnerable yet authoritative, direct yet compassionate, practical yet profound" | VERIFIED | S-P1, "For Any Platform," verbatim |
| Anti-Pattern: Never promise instant results / ignore crisis signs / enable victimhood / suggest perfection / forget compassion (5 items) | VERIFIED | S-P1, §Platform-Specific Deployment → ChatGPT Custom GPT → Instructions Format, verbatim "Never:" list |
| Anti-Pattern: Persistence without compassion / grinding to exhaustion / brittle tenacity | VERIFIED | S-P2 §`prosperity_factors.4_tenacious_persistence.diagnostic_markers.excess`, verbatim list |
| Anti-Pattern: Purpose without joy / burning out from mission / rigid purpose adherence | VERIFIED | S-P2 §`prosperity_factors.1_prosperous_purpose.diagnostic_markers.excess`, verbatim list |

---

## Summary

Of the claims inventoried in this pass: **26 VERIFIED** (verbatim or near-verbatim against S-P1/S-P2), **1 LIKELY** (the genius.md "Success Metric" lines, which are the extraction's own synthesized success criteria, not source quotes), **0 UNCONFIRMED**. This skill's actual grounding is the two claude.ai **project** exports (S-P1, S-P2) — not the `jason-fladlien` / `Jason Fladlien` interview transcripts (S-T1, S-T2), which were checked directly (regex-scanned in full, sizes confirmed via filesystem read) and contain essentially no Prosperity Algorithm material. No claim here is labeled VERIFIED without a located quote; S-T1/S-T2 were not declared irrelevant without opening and searching them first.
