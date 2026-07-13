---
name: "Joscha Bach — Postmodernist Trap Audit"
source_prompt: born-v2
skill: joscha-bach-consciousness
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Joscha Bach's diagnostic on narrative-capability drift: "The story that we tell ourselves about what the system is doing becomes far less important than how well the system is able to deal with the ground truths." Systems calcify — become postmodernized — when what they claim to do disconnects from what they actually do.

Bach's canonical example: NASA "didn't really achieve its mission for a very long time... it became more of an employment program," and "SpaceX disrupted them precisely because NASA had become a story." The delta between narrative and capability is the diagnostic. This audit measures that delta, refuses to accept narrative evidence (testimonials about how great a system is) in place of ground-truth evidence (actual output, actual results), and prescribes concrete forcing functions to close the gap.

## Input Required

- `[SYSTEM]` — what's being audited: a competitor, institution, niche, industry leader, or your own system/product/team
- `[CLAIMS]` — what the system says about itself, or the claims to investigate (marketing copy, mission statements, public statements, internal narrative)
- `[EVIDENCE ACCESS]` — what evidence is available: public output, case studies, customer accounts, internal data, direct observation
- `[AUDIT PURPOSE]` (optional) — competitive analysis, self-audit, disruption-opportunity scan, or coaching diagnostic on someone who "talks about doing" more than "does"

## Execution Protocol

Run all five steps. Steps 1-2 must be evidence-grounded before Step 3's scoring — do not assign gap scores from impression alone.

**Step 1 — Narrative Capture.**
Document what the system claims, sourced:

| Claim | Source | How Prominent? |
|-------|--------|------------------|
| "We do [X]" | [where they say it] | Core/Secondary/Background |

Pull 3-5 claims. Prioritize claims that are central to the system's self-identity (Core), not incidental marketing lines.

**Step 2 — Capability Measurement.**
For each claim, measure actual capability using only ground-truth evidence:

| Claim | Evidence of Capability | Last Verified | Confidence |
|-------|--------------------------|-----------------|--------------|
| "We do [X]" | [actual output/evidence] | [when] | High/Medium/Low/None |

The key move: reject narrative evidence (testimonials, self-reported success stories, claims about claims) in favor of ground-truth evidence (actual output, actual results, actual capability demonstrations someone outside the system could verify). If no ground-truth evidence exists for a claim, confidence is "None" — do not round up.

**Step 3 — Gap Score.**
For each claim, score:
```
Narrative Intensity (1-10): How loudly/frequently do they claim this?
Capability Evidence (1-10): How strong is the ground-truth evidence?
Gap = Narrative Intensity - Capability Evidence
```
| Claim | Narrative (1-10) | Capability (1-10) | Gap |

Average the gaps and interpret:
- Average Gap < 2: Healthy system — narrative tracks capability
- Average Gap 2-4: Early postmodernization — narrative starting to drift
- Average Gap 5-7: Advanced postmodernization — narrative has largely replaced capability
- Average Gap 8+: Terminal postmodernization — the system is a story about itself, ripe for disruption

**Step 4 — Forcing Function Design.**
For each high-gap claim (Gap ≥ 5, or lower if the audit purpose calls for tighter scrutiny), design a ground-truth forcing function — a concrete test that would prove or disprove the claim, drawn from these types:
1. Public demonstration — make the system perform, not describe
2. Outcome tracking — measure results, not intentions
3. Competitive benchmark — compare against someone who actually does it
4. Constraint test — remove resources and see what still works
5. User/Customer audit — ask the actual recipients, not the providers

**Step 5 — Disruption Opportunity Map (Optional, only if auditing a competitor/market).**
For each high-gap claim, map what taking that gap would require:

| High-Gap Claim | Disruption Opportunity | What Would It Take? |

## Output Contract

Deliver exactly:
1. **SYSTEM** — what's being audited
2. **NARRATIVE MAP** — the top 3-5 claims table (Step 1)
3. **CAPABILITY MAP** — the evidence table (Step 2)
4. **GAP SCORES** — the scored table + average (Step 3)
5. **OVERALL HEALTH** — Healthy / Early Drift / Advanced / Terminal, with the average gap stated
6. **FORCING FUNCTIONS** — concrete tests for each high-gap claim (Step 4)
7. **DISRUPTION OPPORTUNITIES** — only if `[AUDIT PURPOSE]` is competitive; otherwise omit this section entirely rather than force it
8. **VERDICT** — one paragraph, direct, naming the specific narrative-capability delta and what it means for the system's trajectory

## Output Skeleton

```
SYSTEM: [audited]

NARRATIVE MAP:
| Claim | Source | Prominence |

CAPABILITY MAP:
| Claim | Evidence | Last Verified | Confidence |

GAP SCORES:
| Claim | Narrative (1-10) | Capability (1-10) | Gap |
Average Gap: [score]

OVERALL HEALTH: [Healthy / Early Drift / Advanced / Terminal]

FORCING FUNCTIONS:
| Claim | Gap | Forcing Function |

DISRUPTION OPPORTUNITIES: [table, or omit section if not applicable]

VERDICT: [one direct paragraph]
```

## Quality Gate

- Was every capability score backed by named, ground-truth evidence — not narrative evidence dressed up as capability evidence?
- Did any claim receive "Confidence: None" when no real evidence was found, rather than being rounded up out of charity or assumption?
- Are the forcing functions concrete and testable — could someone actually run them next week — not vague ("improve transparency")?
- Would this audit survive if the system's leadership read it? If it leans on insider access or unverifiable claims rather than observable reality, it's weak and should be revised.
- Is the Verdict specific to this system's actual delta, not a generic "there's always a gap between story and reality" hedge?

## Creative Latitude

This deliverable is a diagnostic, not a creative one — but the Verdict paragraph is where judgment matters most: name the delta plainly, in Bach's register (analytical, unflinching, willing to say a system is "a story about itself" if the evidence says so), rather than softening a Terminal-tier finding into diplomatic language. The Forcing Function design is the other high-leverage spot — a generic forcing function ("do a customer survey") is weak; the sharpest ones expose the gap in a single unambiguous test, the way SpaceX's reusable rockets exposed NASA's cost-narrative gap without anyone needing to argue about it.

## Deploy When

- Evaluating a competitor, institution, or niche for real vs. claimed capability
- Auditing your own systems for narrative inflation
- Coaching someone who talks about doing more than they do
- Analyzing why an industry leader may be vulnerable to disruption
- Running a periodic self-application check on whether this system's own skills/workflows are producing what their SKILL.md files claim
