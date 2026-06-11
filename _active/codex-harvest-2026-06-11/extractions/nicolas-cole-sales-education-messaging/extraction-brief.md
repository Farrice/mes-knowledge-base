# Nicolas Cole Sales Education Messaging - Extraction Brief

## Source Package

- Source: `https://www.youtube.com/watch?v=jWL3Am1v9t8&t=870s`
- Title: "Sales Is Education: Say these words & people buy."
- Expert/channel: Nicolas Cole
- Published: 2026-05-08
- Duration: 25:24
- Grounded package: `extractions/video-context/jWL3Am1v9t8/`
- Highlighted timestamp: 14:30, used as the specific-knowledge and objection-confidence section.

## Build Decision

Build shape: new companion skill.

Reason: the source is broader than `nicolas-cole-client-acquisition`. It applies to service sales, product launches, sales pages, emails, DMs, positioning translation, objection handling, and category education. It should stack with existing Cole systems instead of being buried inside one.

## Extracted Operating Model

The central model is an eight-part education arc:

1. Problem awareness.
2. Reasons the problem exists.
3. Consequences and opportunity cost.
4. Emotional or second-order impact.
5. Category of solution.
6. Power of that category.
7. Benefits of implementing that category.
8. Ultimate positive outcome.

## Evidence Boundary

The extraction uses spoken evidence from the transcript and ledger. The video-context package also contains frame samples, but no OCR rows. Visual claims are not used as proof unless a future pass reviews the frames directly.

## Deployed Skill

- Skill root: `skills/nicolas-cole-sales-education-messaging/`
- Commands:
  - `/sales-education-map`
  - `/buyer-belief-ladder`
  - `/problem-articulation-script`
  - `/positioning-message-bridge`
  - `/objection-education-loop`
  - `/say-these-words-script`
  - `/sales-page-education-audit`
  - `/offer-education-sequence`

## Cold-Start Usage

Given an offer, buyer, and current sales asset, future agents should:

1. Use `/sales-education-map` to build the education arc.
2. Use `/buyer-belief-ladder` to identify missing beliefs and objections.
3. Use `/problem-articulation-script` or `/positioning-message-bridge` to produce language.
4. Use `/sales-page-education-audit` or `/offer-education-sequence` to deploy across a page, call, or email sequence.
