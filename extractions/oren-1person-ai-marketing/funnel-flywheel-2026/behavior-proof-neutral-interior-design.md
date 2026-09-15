# Behavior Proof — Local Interior-Design Service

## Input Tested

- **Buyer:** Orange County homeowner preparing a bathroom renovation.
- **Purchased job:** reduce uncertainty before committing to a renovation and determine whether the designer is a fit.
- **Primary offer:** paid interior-design engagement; price and exact scope were not supplied.
- **Attention source:** local search, social content, referral, or direct visit.
- **Follow-up capacity:** one consultation owner plus basic email and lead tracking.
- **Economics:** unknown.
- **Permission:** draft/build specification only.

## Weakness Diagnosed

A page that says “call for design services” asks for a high-consideration commitment before the homeowner has planning clarity or evidence of fit. The route needs to provide useful preparation, capture permission, qualify the project, improve consultation attendance, and preserve follow-up.

## Source Mechanics Used

- Twelve-step renovation checklist as an entry asset.
- Capture page → thank-you/consultation transition → call preparation.
- Immediate confirmation and next-day education.
- Qualification before consultation.
- Completion-moment referral after delivery.

## Route Card

**Primary route:** renovation-planning guide → project-fit consultation → paid design engagement.

**Supporting route:** relevant one-to-one conversation for local referrals or engaged prospects, leading to the same qualification step.

| Alternative | Verdict | Reason |
|---|---|---|
| Lead-magnet route | SELECT | Planning education creates immediate value and matches the long consideration cycle. |
| Direct “call now” | REJECT | Too much commitment before fit, timing, and project readiness are known. |
| Tripwire | REJECT | No justified low-price service or fulfillment economics were provided. |
| Webinar | REJECT | One-to-many presentation is unnecessary for the first local test. |
| VSL | REJECT | The guide and consultation can explain the decision without a long video. |

## Customer-Journey Map

| State | Trigger | Asset/conversation | One next action | Owner | Measurement | Failure state |
|---|---|---|---|---|---|---|
| UNSEEN | Homeowner begins planning | Local search, referral, or useful post | Open the renovation guide page | Designer | Relevant visits | Traffic outside service area |
| ATTENTION | Page promise matches project | Twelve-step preparation guide | Request the guide | Homeowner | Guide requests | Promise too generic or form too demanding |
| KNOWN LEAD | Permissioned request completed | Thank-you page and delivered guide | Request project-fit consultation | Homeowner | Guide delivery and consult requests | No bridge to the design job |
| QUALIFIED | Fit form completed | Location, project type, budget range, timing, ownership | Book a consultation | Designer | Qualified bookings | Outside area, timing, scope, or fit |
| BOOKED | Calendar confirmation | Preparation page, agenda, reminders | Attend with project information | Designer + homeowner | Held consultations | Missing reminders or unclear expectations |
| HELD | Consultation occurs | Needs/fit discussion | Accept proposal or next scoped step | Designer | Held/qualified/proposal states | Advice given without a decision path |
| PAID | Payment event occurs | Design agreement and kickoff | Begin engagement | Designer | Collected payment | Payment and agreement not complete |
| FULFILLED | Engagement completes | Completion review | Give feedback and consider referral | Designer + homeowner | Completion and satisfaction signal | Referral asked before value is delivered |
| REFERRED/RETURNING | Relevant next project or introduction | Human referral follow-up | Start a new fit check | Designer | Qualified referrals | Automated or poorly timed ask |

## Capture/Conversation Sequence

1. **Guide page job:** explain what the homeowner will be able to prepare or decide; one CTA to receive the guide.
2. **Minimum fields:** first name, email, service-area confirmation, and consent. Project details wait until the fit step.
3. **Thank-you job:** deliver the guide, introduce the designer, and offer a project-fit consultation.
4. **Qualification:** location, bathroom/room type, approximate project budget, desired timing, property ownership, and decision participants.
5. **Preparation page:** who will attend, consultation agenda, photos/measurements/inspiration to bring, and rescheduling path.
6. **Immediate message — DRAFT:** confirm the guide request, link to the guide, introduce the designer, and explain the optional consultation.
7. **Next-day message — DRAFT:** send the strongest relevant planning lesson and one invitation to request a fit consultation.

## Automation Handoff

This is a tool-neutral build specification only. A future implementation may create permissioned guide delivery, qualification, booking confirmation, reminder, rescheduling, and next-day nurture states in the designer's existing stack. It must stop when the homeowner is outside the service area, declines consent, cancels, or fails qualification; no message is sent and no record is created by this artifact.

## Offer Ladder

| Rung | Job | Price state | Proof state |
|---|---|---|---|
| Renovation-planning guide | Help the homeowner prepare and self-identify fit | Free | Source-derived entry concept |
| Project-fit consultation | Determine fit, scope, readiness, and next step | Not supplied | UNTESTED |
| Paid design engagement | Plan and guide the renovation | Not supplied | UNTESTED in this case |
| Completion referral | Introduce another relevant homeowner after value is delivered | No assumed incentive | UNTESTED |

**ECONOMICS: UNPROVEN.** Required inputs: guide production/maintenance cost, traffic source cost, guide-to-qualified-consult rate, held-consult rate, proposal-to-payment rate, average engagement value, fulfillment margin, and referral rate.

## Measurement Plan

- Guide-page visit → permissioned request.
- Request → qualified consultation request.
- Qualified booking → held consultation.
- Held consultation → proposal and collected payment.
- Paid engagement → completed engagement.
- Completed engagement → qualified referral.

## Next-Test Queue

1. Test three guide promises: homeowner story, evidence/checklist rigor, and direct problem/cost prevention.
2. Keep the form, qualification, and consultation process constant.
3. Measure guide requests and qualified consultation requests separately.
4. With low traffic, treat results as directional and supplement them with homeowner questions; do not claim statistical confidence.
5. Retain which promise attracted projects that actually fit, not merely the most downloads.

## Behavior Delta

The system converted a generic local-service page into a complete, measurable journey with qualification, consultation attendance, payment, delivery, and referral states. It required no hidden category-specific context and refused unsupported economics.

## Remaining Risk

Offer price, service scope, local demand, traffic volume, delivery capacity, and conversion performance are unknown. This is an applied architecture proof, not market proof.
