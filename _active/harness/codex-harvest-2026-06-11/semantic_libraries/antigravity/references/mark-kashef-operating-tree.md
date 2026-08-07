# Mark Kashef Operating Tree

## Purpose

Use this selector when a Mark Kashef query could activate several adjacent
Mark skills, workflows, or operating-system routes. It is a routing reference,
not a new command.

The default rule is simple: when Mark Kashef is being used to improve workflows,
skill orchestration, self-improving systems, source-to-system conversion, or
agent-operating design, route through `/source-to-skill-system` first. Attach
`/self-evolve` and `/skill-anneal` as support routes when the request includes
failure history, performance logs, regression checks, or one weak skill.

## Selector

| Intent | Primary route | Support |
|---|---|---|
| Turn a Mark source, prompt, or method into a durable Codex system | `/source-to-skill-system` | `/extraction-governor-agent`, `/mission` |
| Build or repair self-improving Mark workflow composition | `/source-to-skill-system` | `/self-evolve`, `/skill-anneal` |
| Improve an existing workflow from failure history or performance logs | `/self-evolve` | `/routing-intelligence`, `/skill-anneal` |
| Tighten one Mark skill, prompt, or workflow that is underperforming | `/skill-anneal` | `/self-evolve` if failures repeat across runs |
| Map messy business data into an agentic OS build order | `/silver-platter` | `/system-audit` for internal control-plane proof |
| Design agent teams, councils, handoffs, or debate structure | Mark Agent Orchestration or Mark AI Councils skill | `/expert-composition-governor` if more than three experts compete |
| Plan visual assets before build or generation | Mark Visual Blueprint skill | `/generate-image`, `/sketch-to-build`, or design workflows |
| Build image-generation agent teams or visual DNA pipelines | Mark Banana Squad skill | Mark Visual Blueprint for layout-first planning |
| Bridge messaging, memory, or Claude Code access into an assistant | Mark Claude Claw skill | `/context-audit` for context-yield checks |

## No New Broad Command Rule

Do not add a catch-all Mark Kashef command for this tree. The useful surface is
a selector that routes into the existing front doors:

- `/source-to-skill-system` for source-to-operating-system conversion.
- `/self-evolve` for measured improvement loops.
- `/skill-anneal` for a single weak skill.
- `/silver-platter` for Pantry -> Prep -> Plate data-map work.
- Existing Mark skills for specialist execution.

## Natural Query Routing

| Query shape | Expected route |
|---|---|
| "Mark Kashef self-improving workflows" | `/source-to-skill-system` with `/self-evolve` and `/skill-anneal` support |
| "Use Mark Kashef to build a self-improving workflow system from this source" | `/source-to-skill-system` |
| "This Mark workflow keeps regressing after feedback" | `/self-evolve` |
| "Anneal the Mark visual blueprint skill prompts" | `/skill-anneal` |
| "Map my business tools into Mark's agentic OS" | `/silver-platter` |
| "Create a Mark-style AI council" | Mark AI Councils skill |
| "Make a Mark wireframe before generation" | Mark Visual Blueprint skill |

## Verification Query

```bash
python3 execution/routing_governor.py evaluate "Mark Kashef self-improving workflows"
```

The expected governor lane is `mark-operating-tree`, and the chosen route is
`/source-to-skill-system`.
