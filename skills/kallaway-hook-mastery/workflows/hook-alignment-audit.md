---
name: "Hook Alignment Audit"
slug: "hook-alignment-audit"
produces: "Scored audit of an existing hook (all channels) + prioritized fixes"
expert: "Kallaway Hook Mastery"
tier: 2
description: "Diagnostic for an existing video/script/post: scores the two-question test, the 4 S's, triple-hook alignment, and the lock-in zone. Finds the exact reason a hook isn't hooking — the #1 culprit is misalignment."
---

# Hook Alignment Audit

> **🔒 Pre-Flight Gate**: genius.md Decision Framework. Audit mode — diagnose before prescribing. Get the actual artifact (video, script, or post), not a description of it.

## Skill Acquisition
`genius.md` (rubric + anti-patterns) + `references/text-hook-rules-card.md`.

## Input Required
- **[ARTIFACT]**: the video/script/post (or its hook set: spoken, text, visual description, caption line)
- **[PERFORMANCE DATA]** (optional): views/retention vs. account baseline
- **[INTENT]**: what outcome the piece was supposed to drive

## Execution

1. **Channel inventory.** Extract what actually exists: spoken hook (word-for-word), text hook (design + words), visual hook (first 3s description), caption hook (first line). Missing channel = finding #1.
2. **Two-question test (cold read).** From each channel ALONE: can a cold viewer state subject and payoff? Record per channel.
3. **4 S's scorecard** on the spoken hook: Subject / Stakes / Speed (word count vs. 8–12) / Super Clear (one interpretation?). Any miss = automatic fail flag.
4. **Alignment matrix.** Each channel → predict the other two. Mark every misprediction (the business-owner failure mode: polished spoken hook, orphaned text/visual).
5. **Micro-rules pass** on the text hook: six rules + placement + 3-second hold (check the actual timing if video).
6. **Lock-in zone check**: claim confirmed? trust anchor present and concrete? four levers scan.
7. **Verdict + fix stack.** Score the 10-dimension rubric; rank fixes by leverage (text-hook copywriting fixes usually first — highest-leverage lever).

## Content Type Adaptations
| Artifact | Adaptation |
|---|---|
| Short-form video | Full audit incl. timing + eye-path |
| Script (pre-production) | Audit spoken+text; flag visual as unplanned if absent |
| LinkedIn post | Channels = line 1 (spoken analog), formatting (text analog), image (visual analog) |
| Ad | Add trust-anchor severity: missing proof = critical, not minor |
| YouTube long-form | Title/thumbnail = text hook; intro = lock-in zone |

## Output Requirements
Deliver: (1) channel inventory, (2) rubric scorecard with per-dimension one-liners, (3) alignment matrix with mispredictions named, (4) top-3 fixes ranked by leverage with rewritten examples for each. State length held. Feedback Triad.

Execution prompt: references/prompts-v2/khm_hook_alignment_audit.md

## Quality Gate
Every finding cites the specific rule/pattern violated (no vibes verdicts). Fixes are rewrites, not advice ("change X to Y", shown). If performance data provided, findings must be consistent with it or the tension named.
