---
name: storytelling-input-sufficiency
problem_signature: "A cross-domain storytelling router treated missing presentation context as a hard failure even when story evidence was sufficient."
domain: system
tags: [storytelling, routing, input-sufficiency, factual-integrity]
date: 2026-08-02
status: active
session: "Shaan Puri storytelling system"
---

## Problem

A fresh-context full-story replay selected the correct narrative dosage and preserved every supplied fact, yet failed the end-to-end contract because the fixture did not provide a platform, audience, destination, voice, tone, or desired action. The system could not distinguish missing story evidence from missing presentation context.

## Root Cause

The router and downstream narrative workflow listed all inputs as equally required and promised a deployment-ready asset unconditionally. That conflated truth-critical inputs—which determine whether a story exists—with reversible presentation choices that determine channel readiness.

## Approach That Worked

1. Separate decision-critical inputs (`objective`, `raw material`, and `truth risk`) from presentation context (`audience`, `medium`, `destination`, `attention`, and `voice`). Missing truth-critical inputs can block or downgrade; missing presentation context remains explicitly unknown.
2. When truth and scope remain clear, allow neutral platform-agnostic defaults only as labeled working assumptions. Return a truth-safe provisional asset, name the missing deployment fields, and prohibit a channel-ready claim.
3. Replay the same detached fact packet in a fresh context. Pass only if the model selects the same dosage, adds no facts, labels provisional status, and retains one production owner.
4. Make cold-context policy executable in retrieval. A frontmatter flag keeps `genius.md` out of preselection search so a future cache rebuild cannot silently reintroduce story mechanics before dosage is chosen.

## Dead Ends

Treating every missing field as a hard stop makes a cross-domain router brittle. Inventing an audience or platform to avoid the stop is worse because it hides uncertainty. Downgrading from full story solely because presentation fields are absent confuses narrative evidence with formatting context.

## Verification

The first full-story replay passed factual integrity but failed the command contract. After the bounded input-sufficiency repair, a second cold replay returned `FULL STORY`, one owner, zero added facts, labeled neutral defaults, and no named-channel readiness claim. Separate cold replays also passed `STORY FRAGMENT` and `NO STORY`. The source-package, prompt, skill, command-surface, and strict live-surface validators remained green.

## Weaker-Model Trap

A weaker model may fill an absent audience with a plausible persona, add emotional texture to make the draft feel complete, or treat a provisional local draft as published-channel copy. Force unknown presentation fields into the receipt and require an explicit provisional label.

## Pointers

- `skills/shaan-puri-storytelling/workflows/shaan-story-deploy.md`
- `skills/shaan-puri-storytelling/workflows/narrative-script-optimization-audit.md`
- `skills/shaan-puri-storytelling/references/story-deployment-map.md`
- `execution/context_retriever.py`
- `extractions/video-context/GlTA4wXSACE/fixtures/replays/full-story-replay.md`
- `extractions/video-context/GlTA4wXSACE/behavior-proof.md`
