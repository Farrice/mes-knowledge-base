# Rory Sutherland v5.0 Practitioner Smoke Tests

These are simulated deployment cases, not market-result claims. Each case tests whether the new Rory architecture can select one behavioral obstruction, produce a usable artifact, expose its assumptions, and design a falsifiable test.

## Test 1: AI Product Marketing / Adoption Unit

### Scenario

A fictional AI research assistant, ResearchPilot, is sold to boutique agencies. Buyers do not know how model benchmarks affect a client brief. For this test, the only admissible pilot evidence is:

- ten historical brief logs with a median of 6.0 analyst-hours;
- ten paired assisted trials with a median of 2.5 analyst-hours after human source checking;
- paired time differences of 3.0, 3.5, 4.0, 2.5, 3.5, 3.5, 4.5, 3.0, 4.0, and 3.5 hours, giving a median paired difference of 3.5 hours and a total of 35 hours;
- the assisted trials used the same brief type and verification standard;
- no retention, revenue, or across-category evidence exists.

All names and figures in this case are simulated fixture inputs. They are not ResearchPilot market claims.

### Routing Receipt

- **Primary obstruction:** specifications do not translate into a buyer decision.
- **Selected route:** `/adoption-unit`.
- **Rejected route:** Psychological Bottleneck Finder; the evidence already identifies comprehension, not rejection or response friction, as the first bottleneck.
- **Confidence:** high for the pilot context; low outside the tested brief type.

### Deployment Artifact

**Buyer-native unit:** Verified Brief Hours Returned.

**Calculation:** median of the ten paired time differences = **3.5 verified analyst-hours returned per tested brief**.

### Canonical Re-Expression Table

The `/adoption-unit` alias invokes Price Frame Architect and Perception Metric Reframe; this table satisfies their canonical calculation and truth-preservation requirements.

| Lens | Original expression | Re-expression | Calculation | Evidence status | Intended behavior |
|---|---|---|---|---|---|
| Direct time | 6.0-hour baseline median versus 2.5-hour assisted median | “2.5 median hours after human checking” | Observed medians | Simulated pilot input | Understand assisted workflow duration |
| Paired per-brief | Ten paired trials | “3.5 median verified hours returned per tested brief” | Median of paired differences | Simulated paired data | Start a paired trial |
| Portfolio total | Ten paired trials | “35 verified analyst-hours returned across ten tested briefs” | Sum of paired differences | Simulated paired data | Estimate pilot capacity effect |
| Inverse | Baseline and assisted medians | “Assisted median time was 41.7% of the baseline median” | 2.5 ÷ 6.0 | Descriptive, not a paired effect | Compare workload scale |
| Planning scenario | Twenty comparable briefs | “About 70 hours returned if the observed paired median held” | 20 × 3.5 | Extrapolation, unverified | Decide whether to run a larger pilot |

**Landing-page hero**

> **Fixture copy. Publish only when the underlying pilot receipt matches.**
>
> Give each tested client brief 3.5 verified analyst-hours back.
>
> In ten paired pilot briefs, the median paired time difference was 3.5 hours after human source checking. Baseline and assisted medians were 6.0 and 2.5 hours. Your results may differ by brief type and review standard.

**Primary CTA:** “Run one paired brief.”

### Buyer-Native Unit and Truth-Preservation Receipt

| Field | Receipt |
|---|---|
| Original values | Baseline median 6.0 hours; assisted median 2.5 hours |
| Unit formula | Median of paired baseline-minus-assisted differences |
| Pairing method | Same brief type and verification standard; one baseline and one assisted observation per pair |
| Inputs | Ten paired differences listed in the scenario |
| Exclusions | Quality uplift, revenue, retention, other brief types, onboarding time, and unmeasured review work |
| Confidence | Pilot-only; sample too small for a broad product guarantee |
| Original total preserved | Yes; baseline and assisted medians remain beside the new unit |
| Concealment risk | Medium. A time unit could hide output-quality loss, so source accuracy and reviewer acceptance stay as guardrails. |
| Adoption behavior | Qualified paired-brief start |

### Smallest Test Card

| Field | Specification |
|---|---|
| Hypothesis | A buyer-native time unit improves qualified trial starts more than an abstract model-benchmark claim. |
| Control | Existing hero using the model benchmark. |
| Variant | The Verified Brief Hours Returned hero above. |
| Changed variable | Value expression only. |
| Primary metric | Qualified paired-brief starts per eligible visit. |
| Guardrails | Source accuracy, reviewer acceptance, proof-detail opens, evidence objections, and cancellation rate. |
| Decision rule | Before launch, power the test and pre-register “material” as a 2-point rise in evidence objections/cancellation or a 5-point fall in reviewer acceptance; keep the unit only if qualified starts rise without crossing a guardrail. |

### Fixture Conformance Verdict: Market Test Not Run

**PASS after red-team repair.** The alias executes its two canonical engines, the unit uses paired differences rather than a difference of medians, and the original totals, formula, exclusions, and concealment risk remain visible.

## Test 2: Entrepreneurial Strategy / Chosen Trade-Off

### Scenario

A conference operator wants a premium coffee service that keeps breaks moving. The proposed concept has four drinks, no bespoke recipes, scheduled service waves, excellent beans, decaf, and clearly handled allergy information.

### Routing Receipt

- **Primary obstruction:** the offer needs focus without making the restriction feel like a concealed cut.
- **Selected route:** `/chosen-tradeoff-architect`.
- **Rejected route:** Price Frame Architect; price is not yet the load-bearing question.
- **Confidence:** medium until attendee preference and throughput are observed.

### Deployment Artifact

### Category Expectation Ledger

| Convention | Customer job | Hidden job | Cost or complexity | Harm if removed | Verdict |
|---|---|---|---|---|---|
| Large customizable menu | Personal preference | Feeling individually served | Slower ordering and more production variance | Wrong-fit guests lose choice | TRADE with fallback |
| Decaf option | Caffeine control | Inclusion | Low | Excludes caffeine-sensitive guests | KEEP |
| Allergy information | Safety | Trust | Low | Safety and trust failure | KEEP |
| Full-service alternative | Complex needs | Recovery from mismatch | Venue coordination | No safe route for unsupported needs | KEEP as fallback |
| Scheduled service waves | Queue distribution | Confidence during a short break | Organizer coordination | Poor timing can move rather than solve the queue | TEST |

**Chosen bargain**

> **Fixture copy. This bargain and its performance have not been market-tested.**
>
> We deliberately serve four drinks and no custom menu so conference guests can get a carefully made coffee without spending the break in a queue.

**Compensating-strength hypothesis:** a smaller menu can create more dependable break-time flow and more repeatable drink execution. “Under 45 seconds” is a pilot target, not a pre-launch promise.

**Five-part expectation contract**

1. **Name:** Four-Cup Conference Bar.
2. **Before purchase:** “Four drinks. No custom recipes.”
3. **Exchange:** “A smaller menu, designed to keep the keynote moving.”
4. **Wrong-customer warning:** “If you want syrups, size changes, or a bespoke recipe, use the venue café listed beside this menu.”
5. **Arrival reminder:** “Choose espresso, long black, flat white, or oat flat white. Decaf available. Ask us about allergens.”

**Mismatch safeguards**

- preserve decaf and allergy handling;
- allow water without purchase;
- tell organizers the exact menu before contracting;
- route guests who require unsupported customizations to the venue’s full-service option;
- never describe the restriction as “faster” until the pilot supports it;
- give staff this script: “We keep this bar to four drinks so the whole break can move. The venue café can make a custom order for you.”;
- review the contract if more than 5% of served guests report surprise about the menu;
- let the event-service lead restore the broad menu at the next break if accessibility, safety, or core drink quality fails.

### Smallest Test Card

Run two comparable conference breaks using the same staffing and machine capacity: current broad menu versus the four-drink concept with its expectation contract. This is a **radical concept test**; it can judge the whole bargain but cannot identify which component caused the result.

**Hypothesis:** making the restriction explicit and limiting production choices will lower wait and abandonment without a material satisfaction loss or expectation mismatch.

| Measure | Success criterion | Kill criterion |
|---|---|---|
| Median wait | At least 30% below the current-menu baseline | Less than 10% below baseline |
| Satisfaction | No worse than 0.3 points on a 5-point scale | Drop greater than 0.3 |
| Abandonment | Lower than baseline | Higher than baseline |
| Restriction complaints | Fewer than 5% of served guests | Repeated accessibility or expectation failures |
| Bargain comprehension | At least 85% can name the restriction and compensating aim before ordering | Below 70% |
| Voluntary preference | Selection reaches the pre-registered viable service-wave count | Below that count |
| Repeat selection | At least half of prior choosers select it again at a comparable follow-up event | Below one-third |

Before the test, calculate the viable service-wave count as fixed event setup cost divided by contribution margin per drink, rounded up, and confirm it fits physical capacity.

**Scale rule:** repeat at two more comparable events only if every named success criterion is met and no kill criterion fires across all seven measures. Move into the standard event package only after the repeat events also pass.

**Rollback owner:** event-service lead.

### Fixture Conformance Verdict: Market Test Not Run

**PASS after red-team repair.** The missing options purchase a testable strength, all five expectation messages are present, the wrong customer has a safe alternative, and the test now has hypothesis, kill, scale, staff, and rollback rules.

## Test 3: B2B Creator Content / Advertising Archaeology

### Scenario

A B2B operations creator publishes competent educational list posts that look interchangeable with every other account in the category.

### Routing Receipt

- **Primary obstruction:** format sameness, not lack of expertise.
- **Selected route:** `/advertising-archaeology-lab`.
- **Rejected route:** Irritation Reversal Lab; the opportunity begins with an abandoned response mechanism rather than a customer ritual to invert.
- **Confidence:** medium; performance must be tested on the creator’s audience.

### Archaeology Shortlist

No historical artifact was supplied for this fixture. The shortlist therefore treats Rory's 72:33 source statement as a search lead, not proof of current efficacy.

| Candidate | Source era | Provenance status | Why it disappeared | Current-use verdict |
|---|---|---|---|---|
| Comic-strip advertisement | Twentieth-century print advertising | SOURCE-STATEMENT ONLY; exact piece not supplied | Format fashion and print decline may be factors | Test hypothesis |
| Reply coupon | Direct-response print era | CORPUS-GROUNDED mechanism; exact comparator not supplied | Postal response moved online | Test the response device atomically |
| Recurring character | Serialized advertising and publishing | HYPOTHESIS; source artifact required before historical claim | Brand systems moved toward isolated campaign assets | Test as a memory cue |

### Source-Era Mechanism Map

| Historical element | Enduring mechanism | Dated skin to discard | Modern expression |
|---|---|---|---|
| Comic-strip advertisement | Sequential curiosity and narrative completion | Retro typography, caricature, period pacing | Six-panel LinkedIn document with one operational scene |
| Reply coupon | Explicit low-friction response | Printed form and postal return | One named comment or DM route |
| Recurring character | Memory through continuity | Mascot-for-mascot’s-sake | A recognizable operator facing one constraint per edition |

### Moving-Parade Test

1. The target audience sees carousels and documents, but the input provides no evidence they have experienced a sequential comic-strip sales argument.
2. Sequential panels may feel unfamiliar enough to earn attention; retro styling would feel old and is excluded.
3. LinkedIn's swipe document performs the old page-sequence function.
4. A clear business scene and a complete lesson remain necessary for comprehension.
5. Typography, pacing, character treatment, and response route must belong to the current platform.

### Modern Content Artifact

**Series:** “The 4:47 Operator”

**Edition 1, six-panel document**

**Fixture notice:** The scene below is a fictionalized illustration built from a corpus-grounded closing-signal mechanism. It is not a reported client case.

1. **4:47 PM. The dashboard said demand had vanished.**
2. The team prepared to shorten service hours.
3. One site visit showed the chairs stacked, the mop out, and the coffee machine cooling.
4. Customers had not stopped wanting coffee. The room had started saying “closed.”
5. The fix was not a demand campaign. It was removing the closing signals and measuring orders for one more hour.
6. **Before you optimize the metric, visit the moment it describes.**

**Response device:** “Comment `LOOK` and I’ll send the five-line observation sheet used for the test.” This is used only if the sheet exists and can actually be delivered.

**Adaptation specification**

- **Format:** six-panel LinkedIn document.
- **Sequence:** apparent demand problem, field observation, reversed conclusion, cheap test, decision rule.
- **Opening:** a specific moment that creates an unanswered causal question.
- **Response device:** one deliverable comment keyword, used only when fulfillment exists.
- **Proof:** none claimed; the scene is labeled fictionalized and the mechanism is a test hypothesis.
- **Offer:** a five-line observation sheet.
- **Platform behavior:** swiping supplies narrative completion; the final panel carries the response route.
- **Measurement:** qualified dwell, completion, saves, profile visits, and fulfilled responses.

### Atomic and Radical Test Cells

1. **Sequence test [ATOMIC]:** keep the same six panels, words, visuals, and CTA; reveal the reversed conclusion on panel 4 in A and panel 1 in B. Information sequence is the only variable.
2. **Response test [ATOMIC]:** keep the winning document unchanged; use the `LOOK` comment keyword in A and a direct-message link in B. Response route is the only variable.
3. **Continuity test [ATOMIC]:** keep the same plot, panels, and CTA; carry “The 4:47 Operator” series label in A and no recurring label in B. The continuity cue is the only variable.
4. **Radical test:** compare the complete sequential document with the creator's current list-post format. Treat the result as a concept comparison; do not infer which redesigned element caused the difference.

### Novelty-Without-Amnesia Brief

Older direct-response practitioners understood sequence, explicit response, and memory devices. Those mechanisms may still matter because the audience still has to notice, follow, remember, and act. Distribution and interface have changed: a swipe document replaces the printed sequence, and a comment or direct message replaces the coupon. Current efficacy is unknown. The atomic tests can identify sequence, response-route, and continuity effects; the radical test can only tell us whether the whole adaptation deserves further study.

### Fixture Conformance Verdict: Market Test Not Run

**PASS after red-team repair.** The shortlist exposes weak provenance, the story is labeled fictional, the adaptation is deployable, three atomic tests each change one variable, and the radical comparison makes no causal claim.

## Test 4: Non-Marketing Service Design / Uncertainty & Progress

### Scenario

A client-service firm completes onboarding in five business days. Clients describe it as slow, and the team proposes an expensive platform rebuild. Current operations already record receipt, access verification, strategist assignment, and kickoff readiness, but clients see only an initial confirmation and a final booking email.

### Routing Receipt

- **Primary obstruction:** a four-day information void creates uncertainty.
- **Selected route:** `/uncertainty-progress-designer`.
- **Rejected route:** engineering rebuild; no evidence yet shows objective duration is the primary harm.
- **Confidence:** high for the communication gap; completion-time performance still requires monitoring.

### Ranked Uncertainty Map

| Stage | Actual state | What the client sees | Feared unknown | Consequence | Rank |
|---|---|---|---|---|---:|
| Access check | Accounts and files reviewed | Silence | “Am I holding this up?” | Missing access ages unnoticed | 1 |
| Assignment | Strategist assigned | Silence | “Has anyone started?” | Status-chasing and trust loss | 2 |
| Submission | Materials received | Generic receipt | “Did everything arrive?” | Duplicate sends and support contact | 3 |
| Readiness | Kickoff packet prepared | Final booking email | “Why did this take five days?” | Duration feels unexplained | 4 |

**Primary uncertainty:** the client cannot tell whether work is moving or blocked by something they must fix.

### Estimate Architecture

- **Current evidence:** event timestamps exist, but no verified historical distribution was supplied for this fixture.
- **Completion estimate:** do not publish a 4–6-day range yet.
- **First commitment:** acknowledge receipt immediately and promise an access-status update by the next business day.
- **Refresh rule:** publish a new status when the source event changes or at the promised next-update time, whichever comes first.
- **Unknown state:** say “We cannot estimate kickoff readiness until access is complete; next check by [time]” rather than inventing precision.
- **Escalation:** if a promised update is missed, route the case to the onboarding lead and tell the client who owns the recovery.

### Truthful Progress Sequence

1. **Received:** “We received [file count] files and access to [account count] accounts. We’ll flag anything missing by [time].”
2. **Checked:** “Access check complete. [Missing permission] is still needed.” Include a direct repair link.
3. **Assigned:** “[Strategist name] is your strategist. Your kickoff packet is being prepared; next update by [time].”
4. **Ready:** “Your kickoff packet is ready. Choose one of these three call times.”

### Agency Design

| Client action | Real effect | Limit made explicit |
|---|---|---|
| Repair missing access | Removes a known blocker | Does not guarantee immediate kickoff |
| Choose one of three call times | Sets the kickoff slot | Does not change packet-preparation time |
| Ask for human escalation | Gets an owner and review | Does not bypass safety, scope, or quality checks |
| Pause onboarding | Stops avoidable work | May move the eventual kickoff date |

Preserve the human strategist welcome call because it carries judgment, trust, and exception handling that a status page does not replace.

### Transition Communication Set

| Transition | Status message | Next event and commitment | Available action | Exception message |
|---|---|---|---|---|
| Submitted → received | “Your materials are in.” | Access check by [time] | View received-item list | “One upload could not be opened; replace it here.” |
| Received → checked | “Access check complete.” | Assignment update by [time] | Repair listed permissions | “We cannot continue until [permission] is restored.” |
| Checked → assigned | “[Strategist] now owns onboarding.” | Readiness update by [time] | Contact the named owner | “Assignment changed; [new owner] has the full case history.” |
| Assigned → ready | “Your kickoff packet is ready.” | Choose a call time | Book, reschedule, or escalate | “The packet missed its update time; [lead] is reviewing it and will update you by [time].” |

### Smallest Test Card

Use matched-random assignment across the next 20 eligible onboardings, pairing cases by submission completeness and account complexity before randomizing current versus four-stage communication. Leave the underlying operation unchanged.

| Measure | Purpose |
|---|---|
| Actual days to kickoff readiness | Confirm the operation did not slow |
| “I knew what was happening” score | Measure perceived certainty |
| Status-chasing messages per client | Measure information friction |
| Missing-access repair time | Measure useful agency |
| Estimate accuracy | Prevent reassurance through false precision |

Stop or revise if messages create more support work, clients misunderstand a milestone as completion, or promised update times are met in fewer than 80% of cases.

**Keep rule:** retain the sequence if perceived certainty improves and status-chasing falls without worse actual duration, support load, estimate reliability, or recovery satisfaction.

**Scale rule:** automate only the transition messages whose source events and exception paths remain accurate through the 20-case test.

### Fixture Conformance Verdict: Market Test Not Run

**PASS after red-team repair.** The route ranks the information void, withholds an unsupported completion range, connects every status to a real event, names the effect and limit of each control, preserves human judgment, and adds exception, keep, scale, and rollback logic.

## Design-Conformance Matrix: No Market Tests Run

| Requirement | T1 | T2 | T3 | T4 |
|---|---:|---:|---:|---:|
| One dominant behavioral lens | PASS | PASS | PASS | PASS |
| Exact behavior or obstruction named | PASS | PASS | PASS | PASS |
| Technical reality preserved | PASS | PASS | PASS | PASS |
| Deployment artifact produced | PASS | PASS | PASS | PASS |
| One-variable or radical-alternative test | PASS | PASS | PASS | PASS |
| Claims and assumptions bounded | PASS | PASS | PASS | PASS |
| More than marketing applicability | Not applicable | PASS | PASS | PASS |

## Source Receipt

The routing mechanics are grounded in the 2026 MFM transcript/captions and the existing Rory corpus. Workflow names, output contracts, thresholds used for these simulated tests, and composition rules are Antigravity operational synthesis. The thresholds are test policies, not Rory claims. The official Penguin *Alchemy* sample informed orientation only; the full book was not reviewed.
