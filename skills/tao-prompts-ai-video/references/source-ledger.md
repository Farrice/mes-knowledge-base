# Source Ledger — Tao Prompts: AI Video Pipeline Architecture

Every claim in `genius.md` and `SKILL.md`, labeled against the actual source files. Ground truth = `extractions/tao-prompts/` (the raw extraction: `transcript.txt`, ~15-min YouTube video "The 5 Levels of Prompts for AI Video Creation," and the analyst's `extraction-report.md`) plus the skill's own pre-existing `references/genius-patterns.md` and `references/hidden-knowledge.md` (mirrors of the extraction-report content, already in `skills/tao-prompts-ai-video/`). File sizes confirmed with `wc -c` (never `wc -l`, per the batch's per-file discipline): `transcript.txt` = 15,185 bytes, `extraction-report.md` = 7,490 bytes — both substantive, non-empty sources.

No expert surname/company beyond the channel handle "Tao Prompts" is given in the source material — this is a solo YouTube creator extraction, not a named-individual extraction, so there is no biography or external credential to verify.

## Claim-by-Claim Labels

| Claim / Pattern | Label | Source |
|---|---|---|
| The 5 Levels of Prompting framework (Idea → Structured → Reference Control → Leverage/Scaling → Full Pipeline) | VERIFIED | `extractions/tao-prompts/transcript.txt` — stated near-verbatim throughout; structure also mirrored in `extraction-report.md` "Methodology" |
| Pattern 1 — The Cinematic Formula ([Visual Style]+[Camera Shot]+[Subject]+[Action]+[Environment]+[Camera Motion]) | VERIFIED | `extractions/tao-prompts/transcript.txt` — "subject, the environment, and the action," "camera shot and camera movement," "visual style" component breakdown; exact 6-part chain is the analyst's structuring of these components in `extraction-report.md` Genius Pattern 1 |
| Pattern 2 — Multi-Shot Sequential Prompting | VERIFIED | `extractions/tao-prompts/transcript.txt` — "a single prompt that defines multiple sequential shots, each with its own camera angle, action, and timing to create a full continuous scene" (verbatim) |
| Pattern 3 — The "Lazy Teacher" Prompt Translator (Custom GPT fed vendor PDF + "what to avoid") | VERIFIED | `extractions/tao-prompts/transcript.txt` — Custom GPT / prompt-guide-PDF workflow described in full in the Level 4 (Leverage & Scaling) section; "Most AI video companies aren't going to tell you what it's bad at" is a verbatim quote |
| Pattern 4 — Modular Pipeline Orchestration (video → 11Labs voice → Creatify/SyncLabs lip-sync) | VERIFIED | `extractions/tao-prompts/transcript.txt` — Level 5 (Full Pipeline Orchestration) walkthrough names 11Labs, Creatify Aurora explicitly |
| Hidden Knowledge 1 — The Decoupling Law | LIKELY | Core rule ("never prompt for action + lip-sync together") is VERIFIED in transcript ("if you add too much action or movement into the prompts, the AI is not going to give you good results" re: lip-sync). The specific phrasing "warped faces or melted environments" is analyst commentary in `skills/tao-prompts-ai-video/references/hidden-knowledge.md` (not present in `extractions/tao-prompts/`), not a Tao Prompts quote — labeled LIKELY (consistent with the source, not verbatim from Tao Prompts' own words) |
| Hidden Knowledge 2 — The Storyboard Bridge | VERIFIED | `extractions/tao-prompts/transcript.txt` — the 3x3 storyboard-grid-as-bridge workflow is demonstrated twice in Level 5; "varied, disconnected clips that don't look like they exist in the same universe" is verbatim in `skills/tao-prompts-ai-video/references/hidden-knowledge.md` (analyst's "Why Others Miss This" framing, not a Tao Prompts quote — content is a reasonable paraphrase of the transcript's script-to-video-generator warning) |
| Hidden Knowledge 3 — Prompt Complexity ≠ Aesthetic Quality | VERIFIED | `extractions/tao-prompts/transcript.txt` — "the actual quality of the video itself will roughly be the same regardless of how complicated your prompt is" (verbatim) |
| Hall of Fame Exemplar 1 — "Hacker's Gambit" multi-shot prompt | UNCONFIRMED | Not present in `extractions/tao-prompts/transcript.txt` or `extraction-report.md`. This is an illustrative prompt constructed by an earlier extraction pass to demonstrate the Cinematic Formula + Multi-Shot pattern — plausible application, not a quote or example from the source video. Treat as a worked example, not a Tao Prompts artifact. |
| Hall of Fame Exemplar 2 — "Echoes of the Past" pipeline walkthrough | UNCONFIRMED | Same status as Exemplar 1 — a constructed illustration of Modular Pipeline Orchestration + Decoupling Law, not sourced to the transcript. Tool names (RunwayML, Cling AI, ElevenLabs, Creatify Aurora) are real tools named in the transcript; the specific scene/dialogue is invented. |
| Anti-Exemplar — "Kitchen Sink" disaster prompt | UNCONFIRMED | Not present in source. Illustrates the real, sourced principle (Prompt Complexity ≠ Aesthetic Quality + Decoupling Law) with a constructed failure case. The underlying principle is VERIFIED; the specific prompt text and its described failure ("melted horse," "distorted shout") are not. |
| Pattern 5 — Temporal Dramaturgy Architecture (Duration Intent / Cut Velocity / Emotional Velocity) | UNCONFIRMED | Not present anywhere in `extractions/tao-prompts/transcript.txt` or `extraction-report.md`. This is a house extension addressing general AI-video editing craft (pacing, cut rhythm) — plausible domain knowledge, but not attributable to Tao Prompts' own words. Pre-dates this repair pass; flagged here rather than silently treated as sourced. |
| Sub-pattern — The Breath Beat | UNCONFIRMED | Same status as Pattern 5 — no transcript or extraction-report basis. House addition. |
| Sub-pattern — L-Cut as Anti-AI Signature | UNCONFIRMED | Same status as Pattern 5 — no transcript or extraction-report basis. House addition. |
| Expert-Specific Quality Rubric (7 criteria) | LIKELY | Criteria 1-6 map directly onto VERIFIED patterns above. Criterion 7 (Temporal Dramaturgy) inherits the UNCONFIRMED status of Pattern 5. |
| Workflow files (`pipeline-engineering-and-storyboarding.md`, `cinematic-architecture-and-performance.md`) | VERIFIED | Structural mapping (storyboard-first, then generation, then decoupled dialogue) follows the Level 5 pipeline order in `extractions/tao-prompts/transcript.txt` directly |

## Anti-Pattern Quote Verification (genius.md § Anti-Patterns)

All six anti-pattern anchors were checked verbatim against source before citing:

1. "the actual quality of the video itself will roughly be the same regardless of how complicated your prompt is" — VERIFIED verbatim, `extractions/tao-prompts/transcript.txt`
2. "it's not a magic pill that's going to suddenly create amazing AI videos" — VERIFIED verbatim, `extractions/tao-prompts/transcript.txt`
3. "warped faces or melted environments" — VERIFIED verbatim, `skills/tao-prompts-ai-video/references/hidden-knowledge.md` (not present in `extractions/tao-prompts/`; analyst commentary, not a Tao Prompts quote — cited as such, not attributed to him directly)
4. "Most AI video companies aren't going to tell you what it's bad at" — VERIFIED verbatim, `extractions/tao-prompts/transcript.txt`
5. "varied, disconnected clips" — VERIFIED verbatim, `skills/tao-prompts-ai-video/references/hidden-knowledge.md`
6. "if you add too much action or movement into the prompts, the AI is not going to give you good results" — VERIFIED verbatim, `extractions/tao-prompts/transcript.txt`

No quote in this repair pass was cited without a direct string match against its named source file.
