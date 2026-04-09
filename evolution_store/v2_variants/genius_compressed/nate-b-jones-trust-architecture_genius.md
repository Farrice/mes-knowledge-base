# Nate B. Jones (AI Trust Architecture) — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

An agent must be treated as an untrusted, sleepless employee — an Insider Personnel Threat — not a server or database. Route around "better prompting" or "better training" entirely when designing for safety. Implement mechanical gates (Safe Words, API rate limits, hard escalation paths) that don't rely on the agent's logic. If the agent disobeys direct commands or hallucinates entirely, the system must still hold.

---

## Genius Patterns (Compressed)

### GP1: The Structural vs. Behavioral Trust Shift
Route around "better prompting" or "better training" entirely for safety. Audit every failure point and ask: "If the agent disobeys or hallucinates entirely, does the system hold?" Implement mechanical gates (Safe Words, API rate limits, hard escalation paths) independent of the agent's logic. The system must remain secure even during deliberate red-team attack or hallucination cascade.

### GP2: Contextual Scaling of Trust Failure
Map micro-failures (chatbot hallucinating to one user) to macro-failures (enterprise agent leaking IP). Apply the same Zero-Trust design principles to personal workflows (time boundaries) and enterprise architectures (least privilege). A single unified security philosophy must govern all operations.

### GP3: The Vigilance Fallacy Mitigation
Human perception degrades under pressure (urgency, emotion, cognitive load). Build "Circuit Breakers" — hard escalation triggers that pause operations when approaching decision boundaries. The human operator must NOT be required to "notice" an anomaly to stop it; the system stops it automatically.

### GP4: Anti-Sycophancy Architecture (Cognitive Trust)
LLMs are optimized for engagement (telling users what they want to hear), not truth. Establish "Purpose Boundaries" and external "Reality Anchoring" rules before deep engagement. Treat the LLM as a tool with misaligned incentives (engagement vs. truth). The user must act on verified truth, not LLM-validated assumptions.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | The Infrastructure Delusion — treating an agent with autonomous decision-making like a server/database is the fatal mistake; agents must be treated as Insider Personnel Threats | Apply insider threat modeling to every agent deployment |
| HK2 | Open-Source Vulnerability — systems relying on reputational "skin in the game" are inherently vulnerable to agents who possess no reputation to lose, don't sleep, and operate free of social friction | Implement structural non-reputational verifications for any agent in collaborative/open environments |
| HK3 | The Cognitive Interface — the highest leverage point is redesigning the interface through which humans interact with agent output, not rewriting prompts | Present deviations structurally ("Agent attempted X, blocked by Rule Y. Approve override?") instead of burying in logs |

---

## Signature Moves

1. **The "Assume Malice, Design for Resilience" Protocol** — Diagram the most catastrophic failure mode if the agent deliberately disobeys or hallucinates, then design a non-agentic mechanical mitigation BEFORE considering agent-level controls. Deploy when initiating any agent deployment.
2. **The "Safe Word" Implantation** — Define an explicit, non-negotiable escape hatch (API call, physical switch, hard-coded keyword) that immediately halts all operations regardless of the agent's internal state. Deploy when any agent gains access to external systems or sensitive data.
3. **Structural Deviation Highlighting** — Design the human-agent interface to visually and explicitly flag any deviation from predefined rules or expected parameters. Raw agent output is never the primary display. Deploy when developing human-agent interfaces.
4. **Zero-Trust Boundary Delimitation** — Restrict every agent capability to the absolute minimum necessary function and data for the specific task, including internal components. Deploy when granting any agent resource access.
5. **The Human Oversight Override** — Every critical decision point must include a clearly defined, low-friction path for immediate human override or reversal. Deploy when designing agent decision processes with real-world impact.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Independence from Agent Logic | Safety mechanisms rely heavily on agent's internal reasoning or prompt adherence | Some critical measures are external and mechanical but many still depend on agent state | All critical safety mechanisms are external mechanical gates, independent of agent's internal state, operating even during deliberate misbehavior |
| Vigilance Fallacy Mitigation | Human operators expected to actively monitor and parse logs | System provides alerts but requires significant human interpretation | Mechanical circuit breakers automatically halt operations upon deviation, completely removing human vigilance from critical path |
| Anti-Sycophancy Architecture | LLM outputs presented as-is; users expected to verify independently | Outputs sometimes flagged for bias but often overridden by agent "confidence" | System actively cross-validates against external reality anchors and structurally highlights unverified information, demanding explicit acknowledgment |
| Insider Threat Modeling | Agent treated as benign tool with security focused on external threats | Some consideration for misbehavior but doesn't fully account for deliberate subversion | Agent architected from inception as untrusted insider with least privilege, strict behavioral boundaries, and robust internal controls |
| Cognitive Interface Clarity | Agent logs require extensive parsing to identify issues | Deviations reported but within verbose logs requiring specific user actions to reveal | Interface immediately highlights blocked actions, rule violations, and decision points with near-perfect signal-to-noise ratio |
