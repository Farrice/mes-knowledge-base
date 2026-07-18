# Source Ledger — Noah Hawley Storytelling Mastery

Every source consulted for this skill, and every non-trivial claim, labeled VERIFIED / LIKELY / UNCONFIRMED. Built during the Wave 3 Lane 4 repair pass (2026-07-18) to satisfy the `source_ledger` heartbeat check. Claims already in `genius.md`, `references/genius-patterns.md`, `references/hidden-knowledge.md`, and `references/cross-domain-patterns.md` are re-verified here against the transcript directly, not re-derived.

## Primary Sources

| Source | Size | Status | Notes |
|---|---|---|---|
| `extractions/noah-hawley/transcript.txt` | 82,156 chars (0 newlines — single block, no line-numbered structure) | **VERIFIED** | *How I Write* interview with Noah Hawley, 2026. Ground truth for all direct quotes in this skill. Re-checked with `grep -o` for every quote cited below; all matched verbatim. |
| `extractions/noah-hawley/mastery-extraction.md` | 4,777 chars | **VERIFIED** | The extraction author's structured summary (16 patterns, 12 hidden-knowledge items, 3 exemplars + 1 anti-exemplar, 7-dim rubric, 20 workflows). Cross-checked against the transcript; summary claims trace correctly. |

No video-vision pass exists for this source — the extraction notes explicitly SKIPPED it (84-min runtime exceeds the 10-min cap); the skill is transcript-grounded only, not audio/visual-grounded. This repair did not attempt to source a video-vision pass.

## Claim-by-Claim Verification (this repair pass)

| Claim / Quote | Location in `genius.md` | Status | Verification method |
|---|---|---|---|
| "This happens, then this happens, then this happens... the list-making part of your brain, the outline part of your brain" | Anti-Patterns, Operating Principle 1 | VERIFIED | `grep` matched verbatim in transcript's writers'-room opening passage |
| "Don't talk about what happens next. Let's talk about how assimilation is a theme that runs through this season" | Operating Principle 1 | VERIFIED | matched verbatim, same passage |
| "reality rarely ends with white hat versus black hat in the town square at noon" | Operating Principle 1, Anti-Patterns | VERIFIED | matched verbatim, *Fargo*-twists passage |
| "The ending of a story is what gives the story meaning..." | Operating Principle 3 | VERIFIED | matched verbatim |
| "Comedy and horror are the same. It's just tension, tension, tension, release." | Operating Principle 4 | VERIFIED | matched verbatim |
| Prince Valiant haircut / Chigurh gray-zone description | Operating Principle 4 | VERIFIED | matched verbatim |
| "My first question is always: what am I taking for granted..." | Operating Principle 6, Exemplar 3 | VERIFIED | matched verbatim ("what am I taking for granted in approaching the story") |
| Biscuit scene (*Fargo* S5) — "what if she refuses to play his scene?" | Exemplar 1 | VERIFIED | matched verbatim ("What if she doesn't play his scene? What if she refuses to play his scene?") |
| Soap/Gloria scene (*Fargo* S3) — "you are real," "totally legitimate," "impact of that was so high" | Exemplar 2 | VERIFIED | matched verbatim across 3 separate grep hits in the same passage; note the extraction's exemplar title "Soap Dispenser" is descriptive shorthand, not a literal transcript phrase — transcript says "the soap in the sink never works" / "the soap works," never "dispenser" |
| "emotionality" / "simulation of emotion" | Anti-Exemplar, Anti-Patterns, "How to Use" section | VERIFIED | matched verbatim in ABC-executives passage |
| "42-minute show with 38 minutes of music" | Anti-Patterns | VERIFIED | matched verbatim |
| "junkyard dogs and protect their work at all costs... a recipe for disaster" | Anti-Patterns | VERIFIED | matched verbatim |
| "how do I get what I want while making them think that I'm giving them what they want" | Anti-Patterns, Signature Moves | VERIFIED | matched verbatim |
| C-story service creep — "What is this C story with this romance thing that I don't care about... I don't know what to do with these two actors" | Operating Principle 8, Anti-Patterns | VERIFIED | matched verbatim |
| *Legion* "we don't know if he has these powers or if he's crazy... the audience isn't sure either" | Operating Principle 6, Anti-Patterns | VERIFIED | matched verbatim |
| "paint swatch of emotions" | Core Paradox section | VERIFIED | matched verbatim |
| Theme "invisibly to the audience, but for me they're always part of it" | Anti-Patterns ("Naming the machinery") | VERIFIED (as grounding) | matched verbatim; used as the grounding source for a principle the extraction states in its own words — see below |
| "Naming the machinery" as an exact Hawley phrase | Anti-Patterns | **UNCONFIRMED** | No matching string in transcript for "naming the machinery," "don't name it," or equivalent. This is the extraction author's synthesis label for the verified principle above, not a direct quote. Flagged honestly rather than anchored as if verbatim. |
| Credits: *Fargo*, *Legion*, *Alien: Earth*, novels *Before the Fall* and *Anthem* | SKILL.md frontmatter, genius.md intro | **LIKELY** | Public-record industry credits, consistent with the transcript's self-references to *Fargo* (S2/S3/S5), *Legion*, and *Lucy in the Sky*. Not independently re-verified against IMDb/WGA credits in this repair pass — no contradiction found, but no primary filmography source was pulled either. |
| "Before the Fall" / "Anthem" as Hawley's own novels | SKILL.md frontmatter | **LIKELY** | Not mentioned in the transcript itself (interview is TV/film-focused); carried over from the original 2026-06-09 extraction's general-knowledge grounding, per that extraction's own Factual Grounding note ("Non-transcript claims... confined to identity/credits... labeled as general grounding"). Not re-verified against a primary bibliography source this pass. |

## Scope of This Repair

This pass re-verified every quote cited in the reformatted Anti-Patterns section and the new "polish is the tell" calibration note, plus spot-checked the three Hall of Fame exemplars already present in the file. It did not re-audit the full 16 genius patterns, 20 workflow files, `references/genius-patterns.md`, `references/hidden-knowledge.md`, `references/cross-domain-patterns.md`, or `references/implementation.md` line-by-line — those files were not flagged as failing by the heartbeat audit (`named_entity_floor` and `workflow_contracts` both PASS) and were left untouched per the additive-first, minimal-touch boundary in the worker envelope.
