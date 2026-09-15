#!/usr/bin/env python3
"""Decision-led historical-read advisory. Never infer authority from a filename.

The 2026-09-15 reconciliation replaces the old date/mtime shortcut. Exact
status, sidecar metadata, and archive placement establish historical use;
ordinary unknown files remain unknown. Does not block or mutate documents.
"""
import json
from pathlib import Path
import re
import sys

HISTORY = {"superseded", "archived", "retired", "parked", "rejected"}


def inspect(path):
    p = Path(path)
    if not p.is_file():
        return None
    try:
        head = p.read_text(errors="replace")[:4000]
        meta = {}
        sidecar = Path(str(p) + ".metadata.json")
        if sidecar.is_file():
            value = json.loads(sidecar.read_text())
            if isinstance(value, dict):
                meta.update(value)
        fm = re.match(r"\A---\s*\n(.*?)\n---\s*\n", head, re.S)
        if fm:
            for line in fm.group(1).splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta.setdefault(k.strip(), v.strip().strip("\"'"))
        status = str(meta.get("status", meta.get("lifecycle", ""))).lower()
        if status not in HISTORY and any(part in {"99-archive", "archive", "_archive"} for part in p.parts):
            status = "archived"
        if status not in HISTORY and head.startswith("# Historical document"):
            status = "superseded"
        if status not in HISTORY:
            return None
        successor = meta.get("superseded_by")
        return f"HISTORICAL INPUT: {p} is {status.upper()}. " + (f"Resolve successor {successor} against the current user decisions." if successor else "Resolve the decision-backed project index before building on it.") + " Historical comparison remains allowed when requested."
    except (OSError, ValueError):
        return None


def main():
    try:
        payload = json.load(sys.stdin)
        if payload.get("tool_name") != "Read":
            return 0
        fp = (payload.get("tool_input") or {}).get("file_path")
        if fp:
            path = Path(fp)
            if not path.is_absolute():
                path = Path(payload.get("cwd") or Path.cwd()) / path
            note = inspect(path)
            if note:
                print(note)
    except (ValueError, TypeError):
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
