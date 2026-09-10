#!/usr/bin/env python3
"""verify_harness_behavior_report.py — sabotage test for harness_behavior_report.py.

Builds a synthetic sqlite index + two fake transcripts (one Codex-shaped, one
Claude-shaped, 2 exchanges each with known tool-call/write/prose/artifact-path
counts), runs summary() against them, and asserts the exact numbers. Also
constructs a deliberate calls-per-turn regression (25 -> 12) to confirm the
>30%-below-14-day-baseline flag fires, and confirms a missing db degrades to
UNKNOWN rather than inventing zeros. Deterministic, stdlib only.

Usage: python3 execution/verify_harness_behavior_report.py
"""

import json
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "execution"))
from harness_behavior_report import summary  # noqa: E402

PASS: list = []
FAIL: list = []


def check(name: str, cond: bool, detail: str = ""):
    if cond:
        PASS.append(name)
    else:
        FAIL.append(f"{name} -- {detail}")


def fc(name, args):
    return json.dumps({"type": "response_item", "payload": {
        "type": "function_call", "name": name, "arguments": json.dumps(args)}})


def ctc(name, inp):
    return json.dumps({"type": "response_item", "payload": {
        "type": "custom_tool_call", "name": name, "input": inp}})


def amsg(text):
    return json.dumps({"type": "response_item", "payload": {
        "type": "message", "role": "assistant",
        "content": [{"type": "output_text", "text": text}]}})


def a_msg(content):
    return json.dumps({"type": "assistant", "message": {"role": "assistant", "content": content}})


def tu(name):
    return {"type": "tool_use", "id": f"toolu_{name}", "name": name, "input": {}}


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="harness-behavior-verify-"))
    try:
        db_path = tmp / "db.sqlite"
        archive_root = tmp / "archives"
        archive_root.mkdir(parents=True, exist_ok=True)

        now = datetime.now(timezone.utc)
        recent_ts = (now - timedelta(days=1)).isoformat()
        old_ts = (now - timedelta(days=10)).isoformat()

        # ---- Codex-shaped archive: 2 exchanges, known counts ----
        codex_text1 = "Done, wrote execution/foo.py and execution/bar.py."
        codex_text2 = "All good, no changes needed."
        codex_lines = [
            fc("shell", {"cmd": "ls"}),                               # 1
            fc("shell", {"cmd": "pwd"}),                               # 2
            ctc("exec", "text(await tools.apply_patch({...}))"),       # 3 write
            ctc("exec", "text(await tools.apply_patch({...}))"),       # 4 write
            fc("read_file", {"path": "x"}),                            # 5
            amsg(codex_text1),                                         # 6  (exchange1 = lines 1-6, tc=5, writes=2)
            fc("shell", {"cmd": "ls"}),                                # 7
            fc("shell", {"cmd": "pwd"}),                               # 8
            amsg(codex_text2),                                         # 9  (exchange2 = lines 7-9, tc=2, writes=0)
        ]
        (archive_root / "codex_exact.jsonl").write_text("\n".join(codex_lines) + "\n")

        # ---- Claude-shaped archive: 2 exchanges, known counts ----
        claude_text1 = "Wrote to _active/test/plan.md and execution/thing.py."
        claude_text2 = "All good, no changes needed."
        claude_lines = [
            a_msg([tu("Bash"), tu("Write")]),                                          # 1
            a_msg([tu("Edit"), tu("Read"), {"type": "text", "text": claude_text1}]),    # 2 (exchange1 = lines 1-2, tc=4, writes=2)
            a_msg([tu("Bash"), tu("Read"), {"type": "text", "text": claude_text2}]),    # 3 (exchange2 = line 3, tc=2, writes=0)
        ]
        (archive_root / "claude_exact.jsonl").write_text("\n".join(claude_lines) + "\n")

        # ---- Codex drop-test archive: old turns @25 calls, recent turns @12 calls ----
        def build_block(n_calls, text):
            block = [fc("shell", {"cmd": "x"}) for _ in range(n_calls)]
            block.append(amsg(text))
            return block

        drop_lines = []
        drop_lines += build_block(25, "old turn one")     # lines 1-26
        drop_lines += build_block(25, "old turn two")      # lines 27-52
        drop_lines += build_block(12, "recent turn one")   # lines 53-65
        drop_lines += build_block(12, "recent turn two")   # lines 66-78
        (archive_root / "drop_test.jsonl").write_text("\n".join(drop_lines) + "\n")

        # ---- Build the sqlite index ----
        conn = sqlite3.connect(str(db_path))
        conn.execute(
            "CREATE TABLE exchanges ("
            "id TEXT PRIMARY KEY, harness TEXT, model TEXT, session_id TEXT, "
            "archive_path TEXT, line_start INTEGER, line_end INTEGER, timestamp TEXT)"
        )

        def insert(id_, harness, model, session_id, archive_path, line_start, line_end, ts):
            conn.execute(
                "INSERT INTO exchanges (id, harness, model, session_id, archive_path, "
                "line_start, line_end, timestamp) VALUES (?,?,?,?,?,?,?,?)",
                (id_, harness, model, session_id, archive_path, line_start, line_end, ts),
            )

        insert("c1", "codex", "codex-exact-model", "sess-c", "codex_exact.jsonl", 1, 6, recent_ts)
        insert("c2", "codex", "codex-exact-model", "sess-c", "codex_exact.jsonl", 7, 9, recent_ts)

        insert("l1", "claude", "claude-exact-model", "sess-l", "claude_exact.jsonl", 1, 2, recent_ts)
        insert("l2", "claude", "claude-exact-model", "sess-l", "claude_exact.jsonl", 3, 3, recent_ts)

        insert("d1", "codex", "drop-test-model", "sess-d", "drop_test.jsonl", 1, 26, old_ts)
        insert("d2", "codex", "drop-test-model", "sess-d", "drop_test.jsonl", 27, 52, old_ts)
        insert("d3", "codex", "drop-test-model", "sess-d", "drop_test.jsonl", 53, 65, recent_ts)
        insert("d4", "codex", "drop-test-model", "sess-d", "drop_test.jsonl", 66, 78, recent_ts)

        conn.commit()
        conn.close()

        # ---- Run summary() over the synthetic index ----
        s = summary(days=7, db_path=str(db_path), archive_root=str(archive_root))
        check("status is not UNKNOWN for a valid db", s.get("status") != "UNKNOWN", str(s.get("reason")))

        by_model = s.get("by_model", {})

        cm = by_model.get("codex-exact-model", {})
        check("codex turns == 2", cm.get("turns") == 2, str(cm))
        check("codex calls_per_turn == 3.5", cm.get("calls_per_turn") == 3.5, str(cm))
        check("codex writes_per_turn == 1.0", cm.get("writes_per_turn") == 1.0, str(cm))
        expected_prose_codex = round((len(codex_text1) + len(codex_text2)) / 7, 1)
        check("codex prose_chars_per_call", cm.get("prose_chars_per_call") == expected_prose_codex,
              f"got {cm.get('prose_chars_per_call')} want {expected_prose_codex}")
        check("codex pct_turns_le3_calls == 50.0", cm.get("pct_turns_le3_calls") == 50.0, str(cm))
        check("codex pct_final_with_artifact_path == 50.0", cm.get("pct_final_with_artifact_path") == 50.0, str(cm))

        lm = by_model.get("claude-exact-model", {})
        check("claude turns == 2", lm.get("turns") == 2, str(lm))
        check("claude calls_per_turn == 3.0", lm.get("calls_per_turn") == 3.0, str(lm))
        check("claude writes_per_turn == 1.0", lm.get("writes_per_turn") == 1.0, str(lm))
        expected_prose_claude = round((len(claude_text1) + len(claude_text2)) / 6, 1)
        check("claude prose_chars_per_call", lm.get("prose_chars_per_call") == expected_prose_claude,
              f"got {lm.get('prose_chars_per_call')} want {expected_prose_claude}")
        check("claude pct_turns_le3_calls == 50.0", lm.get("pct_turns_le3_calls") == 50.0, str(lm))
        check("claude pct_final_with_artifact_path == 50.0", lm.get("pct_final_with_artifact_path") == 50.0, str(lm))

        dm = by_model.get("drop-test-model", {})
        check("drop-test window turns == 2", dm.get("turns") == 2, str(dm))
        check("drop-test window calls_per_turn == 12.0", dm.get("calls_per_turn") == 12.0, str(dm))
        baseline = s.get("baseline_14d", {})
        check("drop-test baseline_14d == 18.5", baseline.get("drop-test-model") == 18.5, str(baseline))
        flags = s.get("flags", [])
        flagged = any("drop-test-model" in f and "below 14-day median" in f for f in flags)
        check("30% drop flag fires", flagged, str(flags))

        # ---- Missing db degrades to UNKNOWN, never invented zeros ----
        missing = summary(days=7, db_path=str(tmp / "does-not-exist.sqlite"), archive_root=str(archive_root))
        check("missing db -> UNKNOWN", missing.get("status") == "UNKNOWN", str(missing))

    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"{len(PASS)} pass / {len(FAIL)} fail")
    if FAIL:
        for f in FAIL:
            print(f"  FAIL: {f}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
