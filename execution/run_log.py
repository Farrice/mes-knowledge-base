#!/usr/bin/env python3
"""run_log.py: the run folder is the state (IMPORT-LIST.md #1, 2026-09-09).

Every front door that produces a deliverable writes two files INTO THE RUN FOLDER:

  run.yaml          one machine-readable manifest per run (what was made, for whom,
                    at what cost, with what status); the page generators read it
  pipeline-log.md   one receipt line per step, in order, with an optional
                    Reasoning: line; a skipped step says so instead of vanishing

Both harnesses run the same three shell commands (no Claude-only tools, no hooks):

  python3 execution/run_log.py receipt  <run_dir> <STEP> "<receipt text>" [--reason "..."] [--skip]
  python3 execution/run_log.py manifest <run_dir> [--set k=v ...] [--from-json file] [--steps A,B,C]
  python3 execution/run_log.py check    <run_dir> [--steps A,B,C]      # exit 1 = incomplete
  python3 execution/run_log.py status   <run_dir>                       # one line

Scar: Jen's Valley OS page was regenerated from four hand-edited Python tables
(`jen_os_page.py` POSTS / MEMOS / HERS / OTHER) while the nine /jen receipts were
printed to chat and lost. The Scrapes pipelines keep post.yaml + pipeline-log.md
inside `{date}/{slug}/` and every reader (Studio, publisher, resume) reads the
folder; this file is that convention for our doors.

Consumer: `execution/jen_os_page.py` (the page Farrice judges), `/resume`,
`worktree_lane` merges (a run folder carries its own story across harnesses).

Stdlib only. Reads YAML through PyYAML when present, otherwise through the
subset parser below (the writer only ever emits that subset).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from pathlib import Path

SCHEMA = "antigravity-run/1"
REQUIRED_KEYS = ("schema", "brand", "door", "run", "kind", "status", "built")
DEFAULT_STEPS = {
    "jen": ["LOAD", "READ", "RESEARCH", "WRITE", "AMPLIFY", "CHECK", "RENDER", "DELIVER", "LEARN"],
}
LOG_NAME = "pipeline-log.md"
MANIFEST_NAME = "run.yaml"
_LINE = re.compile(r"^- (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) · ([A-Z][A-Z0-9_-]*): (.*)$")


# ── YAML subset: writer ──────────────────────────────────────────────────
_BARE = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9 _./+@()·,'’%$&-]*$")
_DATEISH = re.compile(r"^\d{4}-\d{2}-\d{2}")
_RESERVED = {"true", "false", "null", "yes", "no", "on", "off", "~", ""}


def _scalar(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v)
    if "\n" in s:
        return None  # block scalar, handled by caller
    if (_BARE.match(s) and s.strip() == s and s.lower() not in _RESERVED
            and not re.match(r"^[-+]?(\d[\d_]*\.?\d*|\.\d+)$", s) and not _DATEISH.match(s)
            and ":" not in s and " #" not in s):
        return s
    return json.dumps(s, ensure_ascii=False)


def _emit(obj, indent: int = 0) -> list[str]:
    pad = " " * indent
    out: list[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            key = str(k)
            if isinstance(v, dict):
                if not v:
                    out.append(f"{pad}{key}: {{}}")
                else:
                    out.append(f"{pad}{key}:")
                    out.extend(_emit(v, indent + 2))
            elif isinstance(v, list):
                if not v:
                    out.append(f"{pad}{key}: []")
                else:
                    out.append(f"{pad}{key}:")
                    out.extend(_emit(v, indent + 2))
            else:
                s = _scalar(v)
                if s is None:
                    out.append(f"{pad}{key}: |-")
                    out.extend(f"{pad}  {line}" if line else "" for line in str(v).split("\n"))
                else:
                    out.append(f"{pad}{key}: {s}")
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict):
                lines = _emit(item, indent + 2)
                if lines:
                    out.append(f"{pad}- {lines[0][indent + 2:]}")
                    out.extend(lines[1:])
                else:
                    out.append(f"{pad}- {{}}")
            elif isinstance(item, list):
                raise ValueError("nested lists are outside the run.yaml subset")
            else:
                s = _scalar(item)
                if s is None:
                    raise ValueError("multi-line strings inside lists are outside the run.yaml subset")
                out.append(f"{pad}- {s}")
    return out


def dump(obj: dict) -> str:
    return "\n".join(_emit(obj)) + "\n"


# ── YAML subset: reader (used when PyYAML is absent) ─────────────────────
def _parse_scalar(tok: str):
    t = tok.strip()
    if t == "" or t in ("null", "~"):
        return None
    if t == "true":
        return True
    if t == "false":
        return False
    if t == "[]":
        return []
    if t == "{}":
        return {}
    if t.startswith('"'):
        return json.loads(t)
    if re.match(r"^[-+]?\d+$", t):
        return int(t)
    if re.match(r"^[-+]?(\d+\.\d*|\.\d+)([eE][-+]?\d+)?$", t):
        return float(t)
    return t


def _load_subset(text: str):
    lines = [ln.rstrip("\n") for ln in text.split("\n")]
    pos = 0

    def indent_of(s: str) -> int:
        return len(s) - len(s.lstrip(" "))

    def skip_blank():
        nonlocal pos
        while pos < len(lines) and (not lines[pos].strip() or lines[pos].lstrip().startswith("#")):
            pos += 1

    def block_scalar(ind: int) -> str:
        nonlocal pos
        buf = []
        while pos < len(lines):
            ln = lines[pos]
            if ln.strip() == "":
                buf.append("")
                pos += 1
                continue
            if indent_of(ln) < ind:
                break
            buf.append(ln[ind:])
            pos += 1
        while buf and buf[-1] == "":
            buf.pop()
        return "\n".join(buf)

    def parse_mapping(ind: int) -> dict:
        nonlocal pos
        d: dict = {}
        while True:
            skip_blank()
            if pos >= len(lines) or indent_of(lines[pos]) < ind:
                return d
            ln = lines[pos]
            if indent_of(ln) != ind or ln.lstrip().startswith("- "):
                return d
            key, _, rest = ln.strip().partition(":")
            rest = rest.strip()
            pos += 1
            if rest in ("|", "|-"):
                d[key] = block_scalar(ind + 2)
            elif rest == "":
                skip_blank()
                if pos < len(lines) and lines[pos].lstrip().startswith("- "):
                    d[key] = parse_sequence(indent_of(lines[pos]))
                elif pos < len(lines) and indent_of(lines[pos]) > ind:
                    d[key] = parse_mapping(indent_of(lines[pos]))
                else:
                    d[key] = None
            else:
                d[key] = _parse_scalar(rest)

    def parse_sequence(ind: int) -> list:
        nonlocal pos
        out: list = []
        while True:
            skip_blank()
            if pos >= len(lines) or indent_of(lines[pos]) != ind or not lines[pos].lstrip().startswith("- "):
                return out
            ln = lines[pos]
            body = ln.strip()[2:]
            if ":" in body and not body.startswith('"'):
                # first key of an inline mapping item
                lines[pos] = " " * (ind + 2) + body
                out.append(parse_mapping(ind + 2))
            else:
                pos += 1
                out.append(_parse_scalar(body))

    skip_blank()
    if pos >= len(lines):
        return {}
    return parse_mapping(indent_of(lines[pos]))


def load(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(text)
        return data or {}
    except ImportError:
        return _load_subset(text)


# ── the manifest ─────────────────────────────────────────────────────────
def _coerce(v: str):
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    if v.lower() in ("null", "none", "~"):
        return None
    if re.match(r"^[-+]?\d+$", v):
        return int(v)
    if re.match(r"^[-+]?\d+\.\d+$", v):
        return float(v)
    if v.startswith("[") or v.startswith("{"):
        try:
            return json.loads(v)
        except json.JSONDecodeError:
            pass
    return v


def write_manifest(run_dir: Path, updates: dict, steps: list[str] | None = None) -> dict:
    run_dir = Path(run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    p = run_dir / MANIFEST_NAME
    data = load(p) if p.exists() else {}
    today = _dt.date.today().isoformat()
    data.setdefault("schema", SCHEMA)
    data.setdefault("run", run_dir.name)
    data.setdefault("status", "draft")
    data.setdefault("built", today)
    if steps:
        data["steps"] = list(steps)
    data.update(updates)
    data["updated"] = today
    # stable key order: required first, then the rest in insertion order
    ordered = {k: data[k] for k in REQUIRED_KEYS if k in data}
    ordered.update({k: v for k, v in data.items() if k not in ordered})
    tmp = p.with_suffix(".yaml.tmp")
    tmp.write_text(dump(ordered), encoding="utf-8")
    tmp.replace(p)
    return ordered


# ── the log ──────────────────────────────────────────────────────────────
def _ensure_log(run_dir: Path, door: str | None = None, brand_lock: str | None = None) -> Path:
    run_dir.mkdir(parents=True, exist_ok=True)
    p = run_dir / LOG_NAME
    if not p.exists():
        head = [f"# pipeline-log · {run_dir.name}" + (f" · {door}" if door else ""), ""]
        if brand_lock:
            head += [brand_lock, ""]
        head += ["One line per step, in order; `Reasoning:` under a line says why. A skipped step says so.", ""]
        p.write_text("\n".join(head), encoding="utf-8")
    return p


def receipt(run_dir: Path, step: str, text: str, reason: str | None = None, skip: bool = False,
            door: str | None = None, brand_lock: str | None = None) -> str:
    step = step.upper()
    stamp = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = f"skipped ({text})" if skip else text
    line = f"- {stamp} · {step}: {body}"
    p = _ensure_log(Path(run_dir), door, brand_lock)
    with p.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
        if reason:
            f.write(f"  Reasoning: {reason}\n")
    return line


def read_receipts(run_dir: Path) -> list[dict]:
    p = Path(run_dir) / LOG_NAME
    if not p.exists():
        return []
    out: list[dict] = []
    for ln in p.read_text(encoding="utf-8").split("\n"):
        m = _LINE.match(ln)
        if m:
            out.append({"at": m.group(1), "step": m.group(2), "text": m.group(3),
                        "skipped": m.group(3).startswith("skipped (")})
        elif ln.startswith("  Reasoning: ") and out:
            out[-1]["reason"] = ln[len("  Reasoning: "):]
    return out


# ── the gate ─────────────────────────────────────────────────────────────
def check(run_dir: Path, steps: list[str] | None = None) -> tuple[bool, list[str]]:
    run_dir = Path(run_dir)
    problems: list[str] = []
    mp = run_dir / MANIFEST_NAME
    data = load(mp) if mp.exists() else None
    if data is None:
        problems.append(f"{MANIFEST_NAME} missing")
        data = {}
    for k in REQUIRED_KEYS:
        if k not in data or data[k] in (None, ""):
            problems.append(f"{MANIFEST_NAME}: missing key `{k}`")
    if data.get("schema") not in (None, SCHEMA):
        problems.append(f"{MANIFEST_NAME}: schema {data.get('schema')!r} is not {SCHEMA}")
    want = steps or data.get("steps") or DEFAULT_STEPS.get(str(data.get("door", "")), None)
    if not want:
        problems.append("no step list: pass --steps or set `steps:` in run.yaml")
        return (not problems, problems)
    got = []
    for r in read_receipts(run_dir):
        if r["step"] not in got:
            got.append(r["step"])
    missing = [s for s in want if s not in got]
    if missing:
        problems.append(f"{LOG_NAME}: missing receipt(s) {', '.join(missing)}")
    order = [s for s in got if s in want]
    expected = [s for s in want if s in got]
    if order != expected:
        problems.append(f"{LOG_NAME}: receipts out of order: {' → '.join(order)} (expected {' → '.join(expected)})")
    return (not problems, problems)


def status_line(run_dir: Path) -> str:
    run_dir = Path(run_dir)
    mp = run_dir / MANIFEST_NAME
    data = load(mp) if mp.exists() else {}
    rec = read_receipts(run_dir)
    steps = [r["step"] + ("~" if r["skipped"] else "") for r in rec]
    ok, problems = check(run_dir) if mp.exists() else (False, ["no run.yaml"])
    return (f"{run_dir.name} · {data.get('door', '?')} · {data.get('brand', '?')} · status={data.get('status', '?')} · "
            f"receipts={' → '.join(steps) or 'none'} · gate={'PASS' if ok else 'FAIL: ' + '; '.join(problems)}")


# ── CLI ──────────────────────────────────────────────────────────────────
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="run_log.py", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("receipt", help="append one step receipt to <run>/pipeline-log.md")
    r.add_argument("run_dir")
    r.add_argument("step")
    r.add_argument("text")
    r.add_argument("--reason", default=None)
    r.add_argument("--skip", action="store_true", help="record the step as skipped (text = why)")
    r.add_argument("--door", default=None, help="door name for the log header (first write only)")
    r.add_argument("--brand-lock", default=None, help="BRAND LOCK line for the log header (first write only)")

    m = sub.add_parser("manifest", help="create or merge <run>/run.yaml")
    m.add_argument("run_dir")
    m.add_argument("--set", action="append", default=[], metavar="KEY=VALUE")
    m.add_argument("--from-json", default=None, help="merge this JSON object into the manifest")
    m.add_argument("--steps", default=None, help="comma-separated step order the gate will require")

    c = sub.add_parser("check", help="verify receipts (in order) + manifest keys; exit 1 when incomplete")
    c.add_argument("run_dir")
    c.add_argument("--steps", default=None)

    s = sub.add_parser("status", help="one line: door, brand, status, receipts, gate")
    s.add_argument("run_dir")

    a = ap.parse_args(argv)
    if a.cmd == "receipt":
        print(receipt(a.run_dir, a.step, a.text, a.reason, a.skip, a.door, a.brand_lock))
        return 0
    if a.cmd == "manifest":
        updates: dict = {}
        if a.from_json:
            updates.update(json.loads(Path(a.from_json).read_text(encoding="utf-8")))
        for kv in a.set:
            k, _, v = kv.partition("=")
            if not k:
                ap.error(f"bad --set {kv!r}")
            updates[k.strip()] = _coerce(v)
        steps = [x.strip() for x in a.steps.split(",") if x.strip()] if a.steps else None
        data = write_manifest(Path(a.run_dir), updates, steps)
        print(f"{Path(a.run_dir) / MANIFEST_NAME}: {len(data)} keys · status={data.get('status')}")
        return 0
    if a.cmd == "check":
        steps = [x.strip() for x in a.steps.split(",") if x.strip()] if a.steps else None
        ok, problems = check(Path(a.run_dir), steps)
        if ok:
            print(f"{Path(a.run_dir).name}: PASS · all receipts present and in order · manifest complete")
            return 0
        print(f"{Path(a.run_dir).name}: FAIL")
        for p in problems:
            print(f"  - {p}")
        return 1
    if a.cmd == "status":
        print(status_line(Path(a.run_dir)))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
