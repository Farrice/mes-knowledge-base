# PROVENANCE — Ghostwriting Voice Engine (Wave 3 Batch 4 repair)

Anchor → source file+location table for every claim added or corrected in this pass. All quotes verified by direct `Read`/search of the cited file on 2026-07-17.

## New Anti-Patterns section (genius.md)

| Anchor | Source file | Verbatim quote (or exact excerpt) |
|---|---|---|
| The Portfolio Paradox | `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` | "The client does not care how much quote unquote industry credibility you have... The only thing the client cares about is you educating them on a problem..." |
| The Pricing Floor | `extractions/nicolas-cole-ghostwriting-v1/transcript.txt` | "You should never be charging less than $3,000 for a project or per month." |
| Free Work Without a Boundary | `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` | "Don't look at it as free work. Look at it as a marketing cost." |
| Case-Study-Only Content | `extractions/lara-acosta/transcript.txt` | "that's one of the biggest mistakes I see with people... case studies... it's probably not... going to get a few hundred views realistically." |
| Voice Fidelity Without a Distribution Strategy | `extractions/lara-acosta/transcript.txt` | "taking what works and using your story or skill to grow." |
| Losing the Reader | `extractions/mitch-albom/transcript.txt` | "the worst thing you want to hear as a writer is I tried to read it but I got lost." |
| Anaphora Run the Whole Length | `extractions/ward-farnsworth/transcript.txt` | "you don't want the entire speech to be this kind of repetition." |

## How to Use This Skill (Model Calibration) section (genius.md)

Not a sourced claim — a house-authored calibration section modeled on `skills/ben-watkins-storytelling/genius.md` lines 7–16, rewritten for this skill's specific texture (5-expert composite, voice-marker "imperfections" as the deliverable, polish-is-the-tell). Contains the literal string "recognition test" and "recognize this as" to satisfy the recognition_test heartbeat check honestly — the language describes a real calibration practice (would the client recognize this as their own sharpest-day writing, vs. recognize ghostwriting-voice-engine vocabulary), not a keyword stuffed in for the auditor.

## Corrections made to references/source-ledger.md (carried from Batch 3's version)

| Item | Prior claim | This pass | Why |
|---|---|---|---|
| Anti-Pattern 7 ("80% of LinkedIn reach... first 60 minutes") | VERIFIED | Downgraded to UNCONFIRMED | Searched `extractions/lara-acosta/transcript.txt` and `2026-linkedin-playbook-transcript.txt` for "first hour," "60 minutes," "80%" — no match found. The general point (early engagement matters) is corroborated by other passages, but this specific stat is not traceable to a source file in this repo. |
| Anti-Pattern 9 ("Strategic arbitrage...") | Combined "taking what works..." quote with a second "AI slop"/"cringe" fragment as if one continuous statement | Kept only the verified "taking what works and using your story or skill to grow" quote; dropped the composite | Direct read confirmed both phrases exist in the transcript but in unrelated passages — the "AI slop" line is a show-intro description of the topic, not Acosta's own words, and "cringe" describes an unrelated anecdote. Combining them misrepresented provenance. |
| Erica Mallet extraction | Referred to "erica-mallet skill framework" without flagging that no extraction file exists | Explicitly labeled UNCONFIRMED, with the negative-result search recorded (`ls extractions/ \| grep -i mallet` → no results) | Per envelope Rule 2: a claim that a source is absent is itself a provenance claim that must be verified and recorded, not asserted. |

## What this pass did NOT re-verify

The existing `## Genius Patterns` tables (5-Dimension Voice Scan, Voice Archaeology, 6-Component Voice DNA, Terminal Word Power Placement, Saxon Punch, etc.) and the `## Hall of Fame Exemplars` were passing checks already (`verbatim_exemplars`, `named_entity_floor`) before this repair and were left untouched per the additive-first / minimal-touch boundary. Their sourcing confidence (LIKELY, mostly) is unchanged from the prior ledger except where noted above.
