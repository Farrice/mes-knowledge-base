# The Arsenal Loop — build → fireable → findable

**Shipped 2026-07-25.** Closes the gap between building an asset and being able to use it.

## The problem it solves

Farrice builds fast — extractions, skills, agents, prompts, workflows, constantly. Two things
broke under that velocity, and they shared one root cause.

| Symptom | Measured 2026-07-25 |
|---|---|
| **Built but not fireable** | 728 skill workflows with no wrapper and no shim · 225 `.agent/workflows` with no `/` shim · 74 skills with no front door |
| **Built but not remembered** | No surface could answer "what do I already have for this?" at workflow granularity → assets rebuilt |

**Root cause:** nothing indexed `skills/*/workflows/*.md`. `find_skill.py` indexed only
`SKILL.md`; `sync_registries.py` mints one shim per *skill*, never per *workflow*. Per-workflow
wrapper minting was a manual instruction in workflow prose — and manual steps lose to velocity.

## The four parity surfaces (auto-fix, never block)

| Surface | Fires | Behavior |
|---|---|---|
| `execution/hooks/menu_parity_hook.py` (PostToolUse `Write\|Edit`) | writing a skill workflow | Advisory at write time. **Debounced: one notice per skill per session.** No index import — one stat call, <100ms |
| `end_session_closeout.py` → `menu-parity` step | every `/end-session` | **Mints**, refreshes indexes, logs to `.agent/sessions/menu-parity.jsonl` |
| launchd `com.antigravity.menu-parity` | daily 06:40 | `mint_menu_wrappers.py sweep` — the only surface not needing a Claude session, so it catches Codex-side builds |
| `menu_parity_hook.py sessionstart` | session start | One line: what was minted overnight, what still drifts. Silent when clean |

**They mint, they never block.** A gate that fails a closeout over housekeeping is a gate that
gets skipped. Detection alone was never enough — heartbeat check 7 has existed since 2026-07-25
and the drift still accumulated, because the missing piece was *minting*, not *noticing*.

## Components

| File | Owns |
|---|---|
| `execution/arsenal_index.py` | `.agent/arsenal-index.json` — ~5,600 entries: skill-workflow, command-workflow, skill, agent. mtime-fingerprinted cache |
| `execution/mint_menu_wrappers.py` | Minting wrappers + shims. `--scope all\|skill <name>` · `--dry-run` (default) · `--apply` · `--report` · `sweep` |
| `execution/arsenal.py` | `/arsenal` — the recall surface. `<task>` · `--family` · `--unused` · `--new N` · `--stats` · `--board` |
| `execution/skill_auditor.py` check 7 | **The single definition of "menu-reachable."** Imported, never re-implemented |

## Invariants — break these and the loop breaks

1. **One definition of reachable.** `arsenal_index` imports `_menu_surfaces`, `_MENU_EXEMPT_RE`,
   `_MENU_VARIANT_RE` from `skill_auditor`. If they ever diverged, the minter would mint what the
   auditor still counts as missing — an infinite housekeeping loop.
2. **Never clobber.** Every minted file carries `GEN_MARKER`. A target without it is hand-written
   and is reported, never modified. This protects the ~598 hand-written shims.
3. **A file stem is not a command name.** Numbered stems get prefixed (`04-viral-idea-ladder` →
   `/jenny-idea-ladder`). Always read `entry["command"]`; deriving from the stem hands back
   invocations that do not exist.
4. **`SLASH_COMMANDS.md` is a document, not the menu.** The `/` typeahead reads
   `.claude/commands/*.md`. The markdown index rolls skill families into one row each so it stays
   cheap to read on demand — it was 592KB before the rollup, past the 350KB bloat threshold
   `health_metrics.py:477` flags.
5. **`--unused` is a memory jog, not an indictment.** The router log records *routed* calls only;
   anything typed directly leaves no trace. Never present it as "you never used this."

## Named exemptions

A workflow opts out of parity with `menu_exempt:`, `status: superseded`, or `superseded_by:` in
frontmatter. Variant/backup filenames are auto-excluded. **An exemption is a decision, and a
decision has a name** — silence is what let 728 workflows hide.

## Operating it

```bash
python3 execution/arsenal.py "<task>"                    # what do I have for this?
python3 execution/arsenal.py --unused                    # built, forge-grade, no routing evidence
python3 execution/arsenal.py --board                     # regenerate the HTML console
python3 execution/arsenal_index.py drift                 # what's unreachable right now
python3 execution/mint_menu_wrappers.py --scope all --apply   # force parity now
python3 execution/skill_auditor.py check --skill <name>  # authoritative per-skill verdict
```

**Extend, never rebuild.** New asset types get a `kind` in `arsenal_index`; new surfaces read the
index. Do not build a second index, a second ranker, or a second minter.
