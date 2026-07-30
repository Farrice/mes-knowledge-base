#!/usr/bin/env python3
"""verify_dialect_injector.py — Bound injector (Model-Dialect Adaptation Layer).

Verifies steering_loop_hook.py's bound injector THROUGH THE FIRE PATH: every
behavioral check runs the hook as a subprocess with a real payload, exactly the
way Claude Code invokes it (docs/solutions/2026-07-21-wired-but-never-loaded-
prompts.md: test the fire path, not the link path).

Discipline (docs/solutions/2026-07-27-*):
- Pinned expectations: the marker string, the negative brief, and the default
  model are HARDCODED here, never read from the module or card under test.
- Structural assertions parse the AST, never string-match source.
- The suite snapshots and restores every telemetry file the hook writes, so a
  run leaves `git status` byte-identical.

Exit: 0 all pass, 1 any fail (Sunday fleet counts nonzero exits).
"""

import ast
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
HOOK = REPO_ROOT / "execution" / "hooks" / "steering_loop_hook.py"
CARD = REPO_ROOT / "directives" / "model-dialects" / "claude-opus-5.md"
STATE = REPO_ROOT / ".agent" / "steering-loop-state.json"
MODEL_CACHE = REPO_ROOT / ".agent" / "active-model.json"

# ── PINNED expectations (never read from the artifact under test) ────────
# Amnesty 2026-07-29: header compressed to "MODEL DIALECT (card: X, class: Y —
# nudge, not cage; Farrice's explicit bounds always win):" — pin follows.
PIN_MARKER = "MODEL DIALECT (card:"
PIN_NEGATIVE_BRIEF = ("no Chain, no finalize, no Notion, no Next Moves, "
                      "return only the artifact")
PIN_DEFAULT_MODEL = "claude-opus-5"
PIN_BOUNDS_WIN = "explicit bounds always win"
PIN_BEGIN = "<!-- BEGIN:machine-dialect -->"
PIN_END = "<!-- END:machine-dialect -->"

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = ""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  ok  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name}" + (f" — {detail}" if detail else ""))


def run_hook(payload: dict, env_extra: dict = None) -> str:
    env = dict(os.environ)
    env["CLAUDE_PROJECT_DIR"] = str(REPO_ROOT)
    env.pop("CLAUDE_MODEL", None)
    env.pop("ANTHROPIC_MODEL", None)
    env.pop("DIALECT_INJECTOR_OFF", None)
    env.pop("DIALECT_CARDS_DIR", None)
    if env_extra:
        env.update(env_extra)
    r = subprocess.run(
        [sys.executable, str(HOOK), "prompt"],
        input=json.dumps(payload), capture_output=True, text=True,
        env=env, timeout=30)
    return r.stdout, r.returncode


def snapshot(path: Path):
    return path.read_bytes() if path.exists() else None


def restore(path: Path, data):
    if data is None:
        path.unlink(missing_ok=True)
    else:
        path.write_bytes(data)


def main():
    state_bak = snapshot(STATE)
    cache_bak = snapshot(MODEL_CACHE)
    try:
        run_checks()
    finally:
        restore(STATE, state_bak)
        restore(MODEL_CACHE, cache_bak)

    print(f"\n{PASS} pass / {FAIL} fail")
    sys.exit(1 if FAIL else 0)


def run_checks():
    sid = {"session_id": "verify-dialect-injector"}

    # ── Card structure ───────────────────────────────────────────────────
    text = CARD.read_text(errors="replace")
    check("card_has_markers", PIN_BEGIN in text and PIN_END in text)
    block = ""
    data = {}
    try:
        block = text.split(PIN_BEGIN, 1)[1].split(PIN_END, 1)[0]
        import re as _re
        block = _re.sub(r"^\s*```(json)?\s*$", "", block, flags=_re.M)
        data = json.loads(block)
    except Exception as e:
        data = {}
    check("card_block_parses_json", isinstance(data, dict) and bool(data))
    check("card_model_match", PIN_DEFAULT_MODEL in (data.get("model_match") or []))
    inj = data.get("inject") or {}
    check("card_has_classes",
          bool(inj.get("deliverable")) and bool(inj.get("conversational"))
          and bool(inj.get("delegation")))
    check("card_negative_brief_pinned",
          data.get("negative_brief") == PIN_NEGATIVE_BRIEF,
          f"card says: {data.get('negative_brief')!r}")
    check("card_single_machine_section", text.count(PIN_BEGIN) == 1)

    # ── Fire-path behavior ───────────────────────────────────────────────
    out, rc = run_hook({**sid, "prompt": "write a linkedin post about the launch",
                        "model": PIN_DEFAULT_MODEL})
    check("deliverable_injects", PIN_MARKER in out and "class: deliverable" in out)
    check("deliverable_carries_negative_brief", PIN_NEGATIVE_BRIEF in out)
    check("deliverable_bounds_win_framing", PIN_BOUNDS_WIN in out)
    check("steering_block_still_present", "STEERING LOOP" in out)

    out, _ = run_hook({**sid, "prompt": "what do you think about the roadmap timing?",
                       "model": PIN_DEFAULT_MODEL})
    check("conversational_injects_light",
          PIN_MARKER in out and "class: conversational" in out)
    check("conversational_no_negative_brief", PIN_NEGATIVE_BRIEF not in out)

    out, _ = run_hook({**sid, "prompt": "/parallax new edition on suppression",
                       "model": PIN_DEFAULT_MODEL})
    check("slash_workflow_is_deliverable", "class: deliverable" in out)

    # Compass retune 2026-07-28 + amnesty 2026-07-29: short prompts get NO
    # dialect and NO steering block (steering is deliverable-class only) —
    # the old expectation of "STEERING LOOP" here predated the retune.
    out, _ = run_hook({**sid, "prompt": "go", "model": PIN_DEFAULT_MODEL})
    check("short_prompt_skipped",
          PIN_MARKER not in out and "STEERING LOOP" not in out)

    out, rc = run_hook({**sid, "prompt": ""})
    check("empty_prompt_silent", out.strip() == "" and rc == 0)

    out, _ = run_hook({**sid, "prompt": "write a post", "model": "claude-nonexistent-9"})
    check("unknown_model_honest_silence", PIN_MARKER not in out)

    out, _ = run_hook({**sid, "prompt": "write a post", "model": PIN_DEFAULT_MODEL},
                      {"DIALECT_INJECTOR_OFF": "1"})
    check("kill_switch_env", PIN_MARKER not in out and "STEERING LOOP" in out)

    # default resolution: no model anywhere → default seat card
    MODEL_CACHE.unlink(missing_ok=True)
    out, _ = run_hook({**sid, "prompt": "draft the offer page copy"})
    check("default_model_resolves", f"card: {PIN_DEFAULT_MODEL}" in out)

    # cache resolution: a cached model with no card wins over the default
    MODEL_CACHE.write_text(json.dumps({"model": "claude-nonexistent-9", "ts": "t"}))
    out, _ = run_hook({**sid, "prompt": "draft the offer page copy"})
    check("cache_beats_blind_default", PIN_MARKER not in out)
    MODEL_CACHE.unlink(missing_ok=True)

    # ── Fail-safe: malformed card must mean silence, never a crash ───────
    with tempfile.TemporaryDirectory() as td:
        bad = Path(td) / "claude-opus-5.md"
        bad.write_text(f"{PIN_BEGIN}\n```json\n{{not json,,,\n```\n{PIN_END}\n")
        out, rc = run_hook({**sid, "prompt": "write a post",
                            "model": PIN_DEFAULT_MODEL},
                           {"DIALECT_CARDS_DIR": td})
        check("malformed_card_silent_not_crashed",
              rc == 0 and PIN_MARKER not in out and "STEERING LOOP" in out)

        empty = Path(td)
        bad.unlink()
        out, rc = run_hook({**sid, "prompt": "write a post",
                            "model": PIN_DEFAULT_MODEL},
                           {"DIALECT_CARDS_DIR": td})
        check("no_cards_dir_silent", rc == 0 and PIN_MARKER not in out)

    r = subprocess.run([sys.executable, str(HOOK), "prompt"],
                       input="{{{garbage", capture_output=True, text=True,
                       env={**os.environ, "CLAUDE_PROJECT_DIR": str(REPO_ROOT)},
                       timeout=30)
    check("garbage_stdin_exit_zero", r.returncode == 0)

    # ── Structural (AST, never string-match) ─────────────────────────────
    tree = ast.parse(HOOK.read_text())
    fns = {n.name: n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    check("ast_injector_functions_exist",
          all(f in fns for f in ("_dialect_block", "_active_model",
                                 "_load_dialect", "_dialect_class")))

    hp = fns.get("handle_prompt")
    called_in_try = False
    if hp:
        for node in ast.walk(hp):
            if isinstance(node, ast.Try):
                for inner in ast.walk(node):
                    if (isinstance(inner, ast.Call)
                            and isinstance(inner.func, ast.Name)
                            and inner.func.id == "_dialect_block"):
                        called_in_try = True
    check("ast_dialect_call_is_failsafe", called_in_try,
          "_dialect_block must be called inside try/except in handle_prompt")

    stop_fn = fns.get("handle_stop")
    stop_calls_dialect = False
    if stop_fn:
        for node in ast.walk(stop_fn):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                    and node.func.id == "_dialect_block"):
                stop_calls_dialect = True
    check("ast_stop_path_never_injects", not stop_calls_dialect)

    yaml_imported = any(
        (isinstance(n, ast.Import) and any(a.name == "yaml" for a in n.names))
        or (isinstance(n, ast.ImportFrom) and n.module == "yaml")
        for n in ast.walk(tree))
    check("ast_no_yaml_dependency", not yaml_imported,
          "hook must stay stdlib-only (JSON card block)")


if __name__ == "__main__":
    main()
