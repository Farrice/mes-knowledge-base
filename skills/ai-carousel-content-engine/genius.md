# AI Carousel Content Engine: Genius Context

## How to Use This Skill (Model Calibration)

These are intuition primitives for producing carousels, not a checklist to march through and cite. Absorb the shape — source lock, then sequence, then structured image prompt, then human review — and then build the specific carousel; never output "Stage 1: Source Lock ✓, Stage 2: Slide Architecture ✓" narration to the person you're building for. Luke Carter, whose demonstrated workflow ("I Replaced My Social Media Designer With ONE AI Prompt," published 2026-05-06) this system is built from, never announces his own machinery on screen either — he just does it, then shows the result.

The recognition test: would Luke Carter recognize this output as the discipline he actually demonstrated — source-first, one idea per slide, structured JSON over vibes, human review as the one thing he refused to automate ("I still want to have uh me in the loop directing and guiding the design and what the copy is saying," 00:06:37–00:06:42) — or as generic AI-carousel-maker vocabulary stitched together after the fact? If it's the second, rebuild.

This skill's specific texture: structured JSON prompts beat prose mood-boards (Genius Pattern 2), and "the durable asset is the prompt package" (hidden-knowledge.md), not the rendered image. The polish-is-the-tell warning runs backward from most content skills: a carousel that looks flawless but skipped the human review gate, or that used "make it viral" instead of an explicit style system, is the failure — not underproduction. A slide deck with visible taste judgment (one claim genuinely dominant, a review checklist that actually flagged something) beats a slicker deck that rubber-stamped every check.

## Core Thesis

A modern carousel is not a slideshow. It is a visual distribution asset that turns one source idea into a swipe sequence, a brand signal, and a pathway back to owned content or an offer. Luke Carter frames the underlying shift directly: "you are now an orchestrator of an entire marketing operation" (00:08:41–00:08:45, *I Replaced My Social Media Designer With ONE AI Prompt*, published 2026-05-06) — the carousel is one output of that operation, not the operation itself.

## Operating Principles

1. **Source-first**: The source article, idea, transcript, or client insight is the authority layer.
2. **Copy before design**: Weak slide logic cannot be saved by beautiful visuals.
3. **Reference before generation**: Style direction, mood boards, and brand tokens prevent generic output.
4. **Structured prompts beat vibes**: GPT Image 2 performs best when the design prompt has explicit regions, text, counts, and slide instructions.
5. **Human review protects taste**: Use AI for speed, not final judgment.

Grounding: Luke Carter's own demo instantiates #3 and #4 directly — before generating anything he spends roughly a full minute (00:03:01–00:04:00) sourcing reference carousel images ("I'm going to try and get two to three references so we can see how to treat the rest of them," 00:03:19–00:03:44) and then builds his master prompt around an explicit fidelity instruction ("we say we want you to match the style exactly," 00:04:26–00:04:31) rather than a mood word. Principle #5 is his stated design choice, not a default: "I specifically didn't want to make this fully autonomous. I wanted to make the writing automated" (00:01:55–00:02:00).

## Slide Architecture

- Slide 1: stop-scroll hook and promise.
- Slide 2: retention bridge that earns the swipe.
- Slides 3-8: one idea per slide, with visual proof or metaphor.
- Slide 9: transformation, before/after, or human detail.
- Slide 10: save/share/comment/click CTA.

## Anti-Patterns

- **Turning an article into 10 disconnected tips instead of one built argument.** Grounded via inference, not a direct Luke Carter quote naming this phrase: he frames the deeper discipline as answering one problem "as deeply as you possibly can" rather than listing tips — "What are the problems they're struggling with on a daily basis? And your job from a content marketing perspective is to answer them as deeply as you possibly can" (00:07:05–00:07:16, *I Replaced My Social Media Designer With ONE AI Prompt*, published 2026-05-06). Label: LIKELY (inferred from his strategy framing, not his literal words about "disconnected tips").
- **Asking GPT Image to "make it viral" without a style system.** Directly grounded: his own master prompt names explicit fidelity rules instead of a vibe word — "we say we want you to match the style exactly, but we also want where photos or illustrations appear, generate new ones that fit the copy inside the slide, rendered in the same visual style as the references, so it feels cohesive" (00:04:26–00:04:39, same source). Label: VERIFIED.
- **Overloading each slide with paragraph text.** No transcript row states this directly (full 506-row ledger checked). Grounded instead in this skill's own design rubric — `references/quality-rubric.md` lists "Long copy that cannot fit on a slide" as a named failure condition. Label: UNCONFIRMED as Luke Carter's words; VERIFIED as this skill's own rule.
- **Creating visuals before deciding the audience and content mission.** Directly grounded: "creating SEO optimized, go optimized articles is incredibly important to have before you go out and create these carousels" (00:07:45–00:07:51, same source; "go optimized" is very likely an ASR mis-hear of "GEO optimized," flagged not silently corrected) — he explicitly sequences durable content strategy before any carousel/visual work. Label: VERIFIED.
- **Fully automating taste review.** Directly grounded, his most explicit statement in the video: "I specifically didn't want to make this fully autonomous. I wanted to make the writing automated" (00:01:55–00:02:00) and "I still want to have uh me in the loop directing and guiding the design and what the copy is saying" (00:06:37–00:06:42, same source). Label: VERIFIED.
- **Treating the hidden prompt as the moat instead of the system.** Grounded in this skill's own explicit boundary (`references/source-map.md`: "Do not claim a hidden prompt was recovered"; `references/luke-carter-video-extraction-notes.md`): Carter gates his actual prompt behind a paid community — "check out the link in the description. We've got an entire school community" (00:08:31–00:08:37, same source, video published 2026-05-06) — rather than sharing it in the video, and this skill deliberately does not claim to have recovered that hidden prompt. Label: VERIFIED (skill's own design decision, not a Carter quote).

## Verbatim Source Material (Luke Carter, Timestamped Transcript)

Every quote below is reconstructed from overlapping auto-caption rows in `_active/codex-harvest-2026-06-11/extractions/video-context/_3SEUgRCXX0/video-context-ledger.md` (506 timestamped spoken-evidence rows, confidence: high/caption-subtitle) against *I Replaced My Social Media Designer With ONE AI Prompt* (Luke Carter, published 2026-05-06, https://www.youtube.com/watch?v=_3SEUgRCXX0). Two known ASR artifacts are preserved verbatim below rather than silently corrected: "GBT" for "GPT," and one likely "go optimized" mis-hear (probably "GEO optimized").

> "I specifically didn't want to make this fully autonomous. I wanted to make the writing automated." (00:01:55–00:02:00)

> "it's reading our entire article, and it's going to turn it into a carousel that we can then go in and design using GBT image 2." (00:01:45–00:01:55)

> "we say we want you to match the style exactly, but we also want where photos or illustrations appear, generate new ones that fit the copy inside the slide, rendered in the same visual style as the references, so it feels cohesive." (00:04:26–00:04:39)

> "this whole process end to end can be automated, but I think it's really important that when we are working with agents, we're not going fully autonomous mode just for the sake of it. I still want to have uh me in the loop directing and guiding the design and what the copy is saying." (00:06:26–00:06:42)

> "What are the problems they're struggling with on a daily basis? And your job from a content marketing perspective is to answer them as deeply as you possibly can." (00:07:05–00:07:16)
