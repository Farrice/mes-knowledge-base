# Workflow 01: Diagnostic Discovery Sprint

> Complete process audit with bottleneck identification — the foundation of every consulting engagement.

## Prerequisites
- **Load**: [genius.md](../genius.md) (required — contains the 6-step framework and interview techniques)
- **Input Required**: Client company name, industry, approximate revenue, number of employees, and the stated reason they're seeking AI consulting
- **Time Investment**: 2-4 hours of interviews + 2-3 hours of analysis

## Produces
A complete diagnostic discovery document containing:
1. Executive interview synthesis (strategic goals + destination)
2. Operator interview synthesis (actual daily workflows)
3. Executive-Operator Gap Analysis (the most expensive insight)
4. Initial bottleneck identification with preliminary waste estimates
5. Engagement recommendation (proceed to full audit / not a fit)

---

## Step 1: Pre-Interview Intelligence Gathering

Before any interview, build a company intelligence brief:

```
COMPANY DIAGNOSTIC BRIEF

Company: [Name]
Industry: [Sector]
Revenue: [Approximate annual revenue]
Employees: [Total headcount]
Stated Problem: [What they told you they need]

Pre-Interview Research:
- What does this company actually DO (product/service)?
- What are the primary revenue-generating processes?
- What departments are most likely to have process waste?
  (Sales, Operations, Customer Service, Finance, Marketing)
- What tools/platforms are they likely using?
- What is their competitive landscape?

Key Hypotheses to Test:
1. [Where you SUSPECT the biggest waste is]
2. [What the CEO probably THINKS the problem is]
3. [What the ACTUAL problem likely is based on industry patterns]
```

---

## Step 2: Executive Interview (The Destination Track)

Run this interview with the CEO/founder/senior leadership. Duration: 45-60 minutes.

**Opening Frame**: "I'm going to ask you some questions about your business. There are no wrong answers — I'm trying to understand where you want to go and what's standing in the way."

**Executive Interview Script**:

```
SECTION A: STRATEGIC VISION
1. What does your business look like in 12 months if everything goes perfectly?
2. What's the ONE thing that, if solved, would have the biggest impact on your bottom line?
3. Where are you spending the most money relative to the value you're getting?

SECTION B: PROCESS AWARENESS TEST
4. Walk me through how a new customer goes from first contact to paying you money.
5. Walk me through how your team handles [their core service/product delivery].
6. How long do each of these processes take? (Note: executives ALWAYS underestimate)

SECTION C: PAIN POINT MAPPING
7. What are you doing manually that you KNOW should be automated?
8. Where does your team spend the most TIME that doesn't directly generate revenue?
9. What tools are you currently paying for? How many? (Look for tool sprawl)

SECTION D: CHANGE READINESS
10. Who on your team would be the person to champion new systems? (AI Champion check)
11. Have you tried implementing any AI tools before? What happened?
12. What's your timeline for seeing results?
```

**Capture Format**:
```
EXECUTIVE INTERVIEW NOTES

Interviewee: [Name, Title]
Date: [Date]

Strategic Goals:
- Goal 1: [verbatim]
- Goal 2: [verbatim]

Perceived Bottlenecks:
- [What they THINK the problems are]

Estimated Process Times:
- [Process A]: [Their estimate] ← (will compare against operator reality)
- [Process B]: [Their estimate]

Change Readiness Score: [1-5]
- AI Champion identified: [Yes/No - Name]
- Previous AI attempts: [Details]
- Timeline expectation: [Realistic/Unrealistic]
```

---

## Step 3: Operator Interview (The Road Track)

Run this interview with 2-3 frontline employees who DO the daily work. Duration: 30-45 minutes each.

**Opening Frame**: "I'm not here to evaluate your performance. I'm here to understand exactly what you do every day so we can find ways to make your life easier. Walk me through your entire morning."

**The "Then What?" Cascade**:

```
OPERATOR INTERVIEW — THE 9-TO-5 NARRATION

"Let's start from the moment you sit down at your desk in the morning.
What's the very first thing you do?"

[Response]
"And then what?"
[Response]
"Show me exactly — which tab do you open? What do you click?"
[Response]
"And then what happens?"
[Continue until you've mapped their ENTIRE morning]

DECOMPOSITION PROBES (for every "simple" task):
- "When you say 'I follow up with leads' — walk me through every single click."
- "When you say 'I update the system' — which system? How many fields? How long?"
- "When you say 'I check email' — how many emails? What do you do with each one?"

WASTE DETECTION QUESTIONS:
- "What part of your day feels like the biggest waste of your time?"
- "If you could eliminate one task entirely, what would it be?"
- "How often do you copy information from one system to another?"
- "How much time do you spend looking for information?"
```

**Capture Format**:
```
OPERATOR INTERVIEW NOTES

Interviewee: [Name, Role]
Department: [Department]
Date: [Date]

Morning Routine (Chronological — EVERY step):
- [Time] [Task] [Duration] [Tools Used]
- [Time] [Task] [Duration] [Tools Used]
...

Afternoon Routine:
- [Same format]

Waste Self-Report:
- Biggest time waste: [verbatim]
- Task they'd eliminate: [verbatim]
- System-to-system copying frequency: [X times/day]

Process Decomposition Results:
- "[Simple task name]" actually = [X sub-steps]:
  1. [Sub-step] — [time]
  2. [Sub-step] — [time]
  ...
```

---

## Step 4: Gap Analysis

This is the most valuable output. Compare executive beliefs against operator reality.

```
EXECUTIVE-OPERATOR GAP ANALYSIS

| Process | Executive Belief | Operator Reality | Gap | Estimated Annual Cost |
|---------|-----------------|------------------|-----|----------------------|
| [Process A] | "[How CEO described it]" | "[What actually happens]" | [Description of gap] | $[Preliminary estimate] |
| [Process B] | "[CEO estimate: X min]" | "[Actual: Y min per person × Z people]" | [X times longer than expected] | $[Preliminary estimate] |

TOP 3 GAPS BY ESTIMATED COST:
1. [Biggest gap] — Preliminary waste estimate: $[X]/year
2. [Second gap] — Preliminary waste estimate: $[X]/year
3. [Third gap] — Preliminary waste estimate: $[X]/year

EXECUTIVE BLIND SPOTS DISCOVERED:
- [Thing the CEO had no idea was happening]
- [Process that takes 5x longer than leadership assumed]
```

---

## Step 5: Engagement Recommendation

```
DIAGNOSTIC DISCOVERY — ENGAGEMENT RECOMMENDATION

Client: [Company Name]
Discovery Date: [Date]
Conducted By: [Your Name]

RECOMMENDATION: [PROCEED TO FULL AUDIT / PARTIAL AUDIT / NOT A FIT]

Rationale:
- Total preliminary waste identified: $[X]/year
- Number of high-impact bottlenecks: [X]
- Change readiness score: [X/5]
- AI Champion: [Identified / Not Identified]
- AI Suitability (4-question filter pass rate): [X/Y processes]

Proposed Audit Scope:
- Departments to map: [List]
- Estimated processes to decompose: [Number]
- Proposed audit fee: $[X] (justified by [X]x potential ROI)
- Timeline: [X days/weeks]

NEXT STEP: Schedule full process mapping sessions (Workflow 02)
```

---

## Quality Gate

Before delivering, verify:
- [ ] Executive AND operator interviews completed (never one without the other)
- [ ] Every "simple task" decomposed into sub-steps with time estimates
- [ ] Gap analysis shows at least 2 areas where executive belief ≠ operator reality
- [ ] Preliminary waste estimates use the ROI formula (Time × People × Days × Cost)
- [ ] Change readiness assessed (AI Champion identified or flagged as missing)
- [ ] Engagement recommendation is clear and justified with dollar figures
