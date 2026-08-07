# Nicolas Cole — Ghostwriting Client Acquisition Extraction

Two YouTube videos covering **how to land ghostwriting clients from zero** — a domain not currently covered by any existing Nicolas Cole skill.

## Content Assessment

| Field | Value |
|-------|-------|
| **Source** | 2 YouTube videos (~10K words combined) |
| **Expert** | Nicolas Cole — founder of Digital Press, Premium Ghostwriting Academy; scaled ghostwriting agency to $M+ revenue, 300+ clients, 23+ employees |
| **Domain** | Ghostwriting client acquisition, service positioning, outreach psychology |
| **Depth Tier** | **Standard** — two focused single-topic deep dives |
| **Genius Patterns** | 8 identified |
| **Hidden Knowledge** | 6 tacit insights detected |
| **Existing Overlap** | `nicolas-cole-niche-positioning` has minor overlap on service selection; client acquisition methodology is **net-new** |

## Key Concepts Identified

### Video 1 — "30-Day Client Acquisition Plan"
1. **Removal List** — create capacity by eliminating before adding
2. **Service-First Niching** — specialize in service before industry
3. **Power-Leveling Credibility** — self-as-guinea-pig in 1 week
4. **Leaks & Faucets Network Mapping** — categorize contacts by direct help vs. referral access
5. **Free Consulting Outreach** — quality over spray-and-pray, 15 min homework per prospect
6. **5x Follow-Up Discipline** — all money in the follow-up
7. **Idiot-Genius Roller Coaster** — psychology management as core skill

### Video 2 — "5 Ways Without Portfolio"
1. **Free Custom Sample** — AI-accelerated sample creation as marketing cost
2. **Free Project → Pay in Confidence/Testimonials/Referrals** — three non-cash currencies
3. **Self as Case Study** — guinea pig positioning that de-risks the client
4. **Pitch in Public** — content-as-outreach, demonstrating expertise publicly
5. **Educate the Client** — articulate their problem better than they can

## Proposed Changes

### New Skill: `nicolas-cole-client-acquisition`

#### [NEW] [SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/nicolas-cole-client-acquisition/SKILL.md)
Skill overview with 3-4 workflows covering the full client acquisition pipeline.

#### [NEW] [genius.md](file:///Users/farricecain/Google%20Antigravity/skills/nicolas-cole-client-acquisition/genius.md)
Full genius file: genius patterns, hidden knowledge, Hall of Fame exemplars, signature moves, quality rubric, and Voice DNA calibrated from both transcripts.

#### [NEW] Workflows (in `workflows/`)
1. **zero-to-client-sprint.md** — Full 30-day blueprint from removal list through first 3 clients
2. **no-portfolio-client-landing.md** — The 5 strategies for landing clients without testimonials/portfolio/case studies
3. **outreach-and-follow-up-engine.md** — Cold outreach + Leaks/Faucets mapping + 5x follow-up system

---

### Crown Jewel Prompts (in `references/prompts/`)

6-8 practitioner-mode prompts:
1. **removal-list-capacity-audit.md** — Audit current time allocation and produce a removal list
2. **service-niche-selector.md** — Select ghostwriting service specialization based on enjoyment + existing practice
3. **power-level-credibility-plan.md** — 7-day credibility power-leveling sprint plan
4. **leaks-faucets-network-mapper.md** — Map personal network into leaks (direct clients) and faucets (referral sources)
5. **free-consulting-pitch-generator.md** — Research a prospect and produce personalized outreach with problem diagnosis
6. **pitch-in-public-content-engine.md** — Transform prospect research into public content that demonstrates expertise
7. **client-education-script.md** — Produce a call script that articulates the prospect's problem so well they assume you're the expert
8. **psychology-management-toolkit.md** — Idiot-Genius roller coaster + faulty belief uprooting framework

---

### Agent Update

#### [MODIFY] [AGENT.md](file:///Users/farricecain/Google%20Antigravity/agents/nicolas-cole/AGENT.md)
- Add `nicolas-cole-client-acquisition` to skills list
- Add Client Acquisition competency section
- Add activation triggers for client acquisition scenarios
- Update handoff protocol

---

### Slash Commands (10 new in `.agent/workflows/`)

| Command | Description |
|---------|-------------|
| `/cole-zero-to-client` | Full 30-day sprint from zero to paying clients |
| `/cole-no-portfolio` | 5 strategies for landing clients without portfolio |
| `/cole-leaks-faucets` | Map your network into direct clients and referral sources |
| `/cole-cold-outreach` | Generate personalized, high-quality cold outreach messages |
| `/cole-pitch-public` | Create public content that doubles as prospect pitch |
| `/cole-power-level` | 7-day credibility sprint plan |
| `/cole-removal-list` | Capacity audit — what to cut to create time |
| `/cole-free-sample` | Create AI-accelerated free custom sample for prospect |
| `/cole-educate-client` | Build client education script for sales calls |
| `/cole-follow-up` | Generate 5x follow-up sequence for any prospect |

---

### KI Update

#### [MODIFY] Nicolas Cole KI
Add client acquisition domain coverage to the existing KI artifact.

---

### Parallel Research Enrichment

Deploy a grounded Perplexity swarm to enrich:
- Latest ghostwriting market data (2025-2026 pricing, demand, AI impact)
- Cole's Premium Ghostwriting Academy curriculum details
- Competitive landscape of ghostwriting acquisition strategies

## Verification Plan

### Automated
- Run `python3 execution/sync_registries.py` to verify all new slash commands register correctly
- Validate all new skill files follow MES 3.0 format structure

### Manual
- Deploy one prompt (e.g., `free-consulting-pitch-generator`) against a real prospect scenario to confirm practitioner-mode output
- Verify agent loads correctly with new skill by running a test activation
