# Standing Councils

> Persistent expert councils with fixed membership, accumulated decision memory, and calibrated trust.

Standing councils differ from ad-hoc councils in three ways:

1. **Fixed membership** — The same agents sit on each council every time
2. **Decision memory** — Past decisions and outcomes are logged in `decisions.md`
3. **Calibrated trust** — Over time, agents whose predictions prove accurate gain higher weight

## Active Standing Councils

| Council | Members | Domain | Invoke |
|---------|---------|--------|--------|
| Revenue Council | Jeremy Miner, Michael Bernoff, Cardinal Mason, Samuel Thompson | Sales, monetization, client acquisition | `@revenue-council` |
| Content Council | Shaan Puri, Harry Dry, Mitch Albom, Dan Wang | Content strategy, storytelling, writing | `@content-council` |
| Brand Council | Dai Media, Caleb Ralston, Lulu Cheng Meservey, Erica Mallet | Positioning, personal brand, consumer psych | `@brand-council` |
| AI Council | Futurepedia, Nate B Jones, Darrel Wilson, Mark Kashef, Andrew Wilkinson | AI implementation, automation, agents | `@ai-council` |
| Creative Council | Kittl, Oscar Hoglund, Seena Rez | Design, sound, creative direction | `@creative-council` |

## How Standing Councils Work

### Invocation
When a standing council is invoked (via `@council-name` or domain match):

1. **Load membership** from the council's directory (e.g., `councils/revenue/`)
2. **Load decision log** from `councils/[name]/decisions.md`
3. **Load each member's** `AGENT.md` and `memory/context.md`
4. **Present the question** to each member in their persona
5. **Record the decision** in the decision log after resolution

### Decision Log Format
Each entry in `decisions.md` follows this structure:

```markdown
## [Date] — [Decision Topic]
**Question**: [What was asked]
**Members Present**: [Who participated]
**Positions**:
- [Agent]: [Their position + reasoning]
**Consensus**: [Final recommendation]
**Dissent**: [Any dissenting views]
**Outcome**: [TBD — updated when results are known]
**Trust Update**: [Which agents were right/wrong, if applicable]
```

### Trust Calibration
- Mark outcomes as they become known
- Agents whose predictions prove accurate build trust weight
- Trust weights inform how much weight to give each agent's position in future decisions
- This is qualitative, not algorithmic — use judgment

## Adding a New Standing Council

1. Create a directory: `councils/[council-name]/`
2. Create `councils/[council-name]/decisions.md` (empty decision log)
3. Add the council to this README and to `COUNCIL.md`
4. Define fixed membership (3-5 agents recommended)

---

*Created: 2026-02-17 | Roundtable Recommendation #7*
