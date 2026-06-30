# Frontier Follow-up Patterns

## Purpose

This reference keeps `/steering-compass` modeled on strong current AI product
patterns without copying any single product's surface. The goal is not more
questions. The goal is better next moves.

## Researched Patterns

- **Perplexity pattern: contextual deepening.** Follow-ups stay attached to the
  existing thread, sources, and prior answer, so the user can go deeper without
  restating context. Translation: every suggestion should preserve the session
  object and name the route or evidence surface it will use.
  Source: https://www.lifewire.com/use-perplexity-ai-8729843
- **Manus pattern: hands-on transformation.** Its front door points users toward
  concrete outputs such as slides, websites, apps, design, and wide research.
  Translation: at least one suggestion should turn the current object into a
  real asset or working surface when safe.
  Source: https://manus.im/
- **Genspark pattern: output families.** Genspark exposes many adjacent output
  families: presentations, websites, spreadsheets, flowcharts, diagrams,
  portfolios, pitch decks, proposals, reports, white papers, case studies,
  ebooks, and content assets. Translation: suggestions should reveal output
  families Farrice may not know to ask for yet.
  Source: https://www.genspark.ai/
- **Genspark/Manus build pattern: preview, refine, ship.** Strong agentic tools
  do not stop at a topic suggestion; they move toward editable files, live
  previews, facts checks, exports, or shipped assets. Translation: every option
  needs an expected output and quality bar.
  Sources: https://www.genspark.ai/tools/ai-presentation-maker,
  https://www.genspark.ai/tools/ai-website-builder,
  https://manus.im/features/webapp
- **Research pattern: higher-order curiosity.** Better follow-ups use diverse
  strategies and higher-order moves like applying and relating, not only
  information gathering. Translation: Use Now should apply the work, Harden
  should test or relate it, and Expand should move it into a bigger system.
  Source: https://arxiv.org/abs/2309.05007
- **Research pattern: unique insight beats simple clarification.** Users value
  questions that are thought-provoking, open-ended, or reveal unique insight
  more than simple fact collection. Translation: each suggestion must include an
  Operator Insight and Hidden Gap/Opportunity.
  Source: https://arxiv.org/abs/2407.12017
- **Research pattern: information-gap bridging.** Strong follow-up generation
  can compare a partial answer against a fuller possible answer and ask toward
  the missing information. Translation: the renderer should name what the
  current output is missing and why the next action closes that gap.
  Source: https://arxiv.org/abs/2502.17715
- **Anti-pattern: engagement bait.** Follow-ups that are unrelated, clicky, or
  designed only to continue the conversation waste attention. Translation:
  skip conditions and quality bars are mandatory; disposable or distracting
  suggestions should not appear.
  Source: https://www.techradar.com/ai-platforms-assistants/chatgpt/i-got-tired-of-chatgpt-trying-to-bait-me-with-follow-up-questions-after-every-answer-so-i-made-this-one-easy-change

## Pinnacle Standard

Each suggested follow-up must satisfy at least three of these five tests:

1. Produces a concrete artifact, file, proof surface, or decision packet.
2. Reveals a Codex capability or workflow the user may not know is available.
3. Bridges a real information, proof, audience, taste, or execution gap.
4. Expands the work into a more valuable format, channel, system, or offer.
5. Preserves context so the next session can continue without re-explaining.

## Suggestion Family Map

- **Transform:** script, slides, webpage, app, dashboard, deck, report, proposal,
  content pack, launch sprint.
- **Deepen:** source-backed research, opportunity map, evidence audit, buyer
  trigger map, mechanism brief, comparison matrix.
- **Harden:** fact check, quality pass, proof gap audit, routing proof,
  regression guard, repeatability packet.
- **Compound:** reusable skill, workflow, primitive, template, campaign system,
  service ladder, library asset.
- **Ship:** prototype, live preview, export packet, public-ready page, client
  handoff, launch checklist.

## No-Lazy-Path Gate Extension

Reject a suggestion if it is only a topic, only a question, only a generic
"continue" instruction, or only a capability name. A strong suggestion names the
object, the output family, the capability path, the gap being closed, and the
quality bar.
