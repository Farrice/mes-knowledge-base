# Source-To-Skill Brief: Attention Hijack Hooks

## Source

- URL: `https://www.youtube.com/watch?v=Zc4E_K48v48&t=43s`
- Video ID: `Zc4E_K48v48`
- Title: `I Studied 131 Viral LinkedIn Hooks, These 5 Will Make You Go Viral`
- Uploader: `Diandra Escobar`
- Local package: `extractions/video-context/Zc4E_K48v48/`
- Evidence limit: transcript-backed spoken evidence; frame and OCR evidence unavailable in the current package

## Extraction Verdict

Build shape: companion skill system plus cold command workflow.

Reason: the source is useful beyond LinkedIn because it teaches a portable attention operation:

1. identify a hookable signal or body insight,
2. create an expectation-versus-claim gap,
3. choose above-fold packaging,
4. validate first-window fit,
5. hand off into full content generation.

This should enrich `/farrice-content-os` and `/diandra-linkedin-system`, not become a competing content OS.

## Deployed Components

| Component | Path | Role |
|---|---|---|
| Semantic primitive | `semantic_libraries/antigravity/primitives/attention-hijack-hook-system.md` | Source-grounded behavior contract |
| Companion skill | `skills/attention-hijack-hooks/` | Reusable hook system with five workflows |
| Command workflow | `.agent/workflows/attention-hijack-hooks.md` | Slash-command execution surface |
| Claude command bridge | `.claude/commands/attention-hijack-hooks.md` | Legacy/source compatibility |
| Cold Codex wrapper | `.agents/cold-skills/source-command-wrappers/source-command-attention-hijack-hooks/SKILL.md` | Recoverable command wrapper without hot-surface expansion |
| Agent spec | `agents/attention-hijack-hooks/AGENT.md` | Main-thread role/process owner |
| Optional subagent spec | `.claude/agents/attention-hijack-hook-auditor.md` | Delegation-ready audit worker, not spawned by default |
| Deterministic helper | `execution/attention_hijack_hooks.py` | Mechanical hook audit |
| Verifier | `execution/verify_attention_hijack_hooks.py` | File, routing, and helper proof |

## Evidence-To-System Map

| Source Mechanic | System Behavior |
|---|---|
| First 40 to 50 words matter | Platform Fit Gate checks first-window signal |
| Human and algorithm both judge the opening | Audits score topical signal and curiosity gap |
| Five formats from outlier hooks | Generator produces Dense, Punchy plus Context, Single-Line Bomb, Stacked, and guarded Hybrid |
| Pixel width beats character count | Local helper estimates first-window width and mobile line count |
| Gap is the engine, format is packaging | Workflows lock payload and gap before format selection |
| Full draft context improves hooks | Hookable Elements Extractor requires source/draft/payload context |
| AI gives starting points, judgment chooses | Output requires one winner, rejected-hook reasons, and downstream route |

## Cold-Start Prompt

```text
/attention-hijack-hooks rehook "[paste draft]" --platform linkedin --reader "[ICP]" --terms "[topic terms]"
```

Expected output: Signal/Payload lock, hook table, selected hook, platform fit audit, and Content Bridge handoff.
