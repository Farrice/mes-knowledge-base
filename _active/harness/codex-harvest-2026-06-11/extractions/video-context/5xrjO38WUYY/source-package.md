# Mark Kashef /goal Evidence Package

## Scope

This package preserves evidence for Mark Kashef's video and companion package:

| Source | Status | Local evidence |
|---|---:|---|
| YouTube video | Metadata and subtitles fetched | `metadata.json`, `transcript.vtt`, `transcript.txt`, `video-context-ledger.md` |
| Companion PDF | Local file available; text extractable | `/Users/farricecain/Downloads/Mark Kashef-goal_cookbook.pdf` |
| Raw prompt zip | Local file available; five prompt files inventoried | `/Users/farricecain/Downloads/Mark Kashef-Raw Text Prompts.zip` |

The package does not claim visual evidence. The run used transcript mode, so frames and OCR were intentionally unavailable.

## Acquisition Notes

- The first sandboxed YouTube fetch failed DNS resolution.
- The network retry succeeded with `python3 execution/video_context_ledger.py 'https://www.youtube.com/watch?v=5xrjO38WUYY' --mode transcript`.
- The fetched video metadata identifies the title as `How to Use /goal to Build a Self-Improving OS`, channel/uploader `Mark Kashef`, duration `10:53`, publish date `2026-05-17`.
- Subtitles were saved as `transcript.vtt` plus source VTT copies. The cleaned transcript has 626 rows, but the auto-caption output includes duplicated rolling fragments and recognition noise.
- The PDF was inspected with PyMuPDF because `pdftotext`, `pdfplumber`, and `pypdf` were unavailable.
- The prompt zip was inspected with `unzip`/`zipfile`; macOS resource-fork entries under `__MACOSX/` were ignored.

## Evidence Limits

- Observed spoken evidence: available from subtitles.
- Observed visual evidence: unavailable.
- Observed on-screen text: unavailable.
- Local package evidence: available as file inventory, hashes, page map, and paraphrased prompt roles.
- Full prompt bodies are not reproduced here. Use the source zip when exact prompt text is needed.

## Source Map

| Evidence lane | Evidence artifact | Count / coverage | Notes |
|---|---:|---:|---|
| YouTube metadata | `metadata.json` | 1 video | Includes title, channel, duration, description, publish date, thumbnail |
| Spoken transcript | `transcript.txt` | 626 rows | Timestamped subtitle rows; duplicated fragments remain visible |
| Ledger | `video-context-ledger.md` / `.json` | 628 rows | 626 spoken rows plus 2 uncertainty rows |
| PDF cookbook | local PDF | 11 pages | Cover, usage model, warmup, five steps, template, community CTA |
| Raw prompts | local zip | 5 prompt files | Clean, sharpen, revive, forge, maintain |

## Cross-Source Findings

| Theme | Video evidence | PDF evidence | Prompt zip evidence |
|---|---|---|---|
| Main thesis | Around 00:00-00:01, the video frames `/goal` as useful beyond technical code chores for improving an agentic OS. | Page 1 presents the cookbook as companion material for a self-improving agentic OS. | Each text file is a paste-ready operational prompt rather than a theory note. |
| Evaluation loop | Around 00:01:21-00:01:46, the video describes a loop with a separate judge/evaluator checking terminal conditions. | Page 2 explains that clear stop conditions are what keep a `/goal` from drifting. | Every prompt includes stop criteria and a turn cap. |
| Clean | Around 00:02:19-00:03:01, the demo audits skills/rules and archives rather than deletes. | Pages 4-5 cover `CLEAN` for auditing `~/.claude`. | `01_clean_audit.txt` targets stale skills, rule dedupe, contradictions, and `AUDIT_REPORT.md`. |
| Sharpen | Around 00:03:24-00:05:04, the demo uses rubric-driven iteration. | Page 6 covers skill iteration against a rubric. | `02_sharpen_skill.txt` uses `rubric.md`, `test_inputs.md`, and `ITERATION_LOG.md`. |
| Revive | Around 00:05:04-00:05:59, the demo scans dormant projects and logs whether they deserve resurrection. | Page 7 covers backlog resurrection. | `03_revive_backlog.txt` writes verdicts to `ALIVE.md` and avoids commits. |
| Forge | Around 00:05:59-00:07:51, the demo mines session transcripts for repeated patterns that should become skills. | Page 8 covers skill generation from session history. | `04_forge_skills.txt` creates three skill folders plus `FORGE.md`. |
| Maintain | Around 00:07:51-00:10:17, the demo combines `/loop` and `/goal` for recurring upkeep. | Page 9 covers a recurring heartbeat. | `05_maintain_heartbeat.txt` appends to `MAINTENANCE_LOG.md` and keeps rules/current skills aligned. |
| Prompt grammar | The video implies reusable patterns through the five demos. | Page 10 gives a fill-in template for building custom `/goal` prompts. | The five raw files instantiate the same pattern with targets, decisions, side effects, proof artifacts, stop criteria, and caps. |

## Implementation-Relevant Takeaways

The package is strongest as a source kit for an OS-maintenance workflow family: audit, improve, recover, generate, and maintain. The durable mechanism is not just "run autonomously"; it is "define a target, per-item criteria, state-changing action, proof artifact, measurable stop state, and turn cap."

For downstream implementation, treat the five raw prompt files as operational examples, not final Codex instructions. Translate destructive or risky actions into approval-gated local workflows before applying them to this workspace.

