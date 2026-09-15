#!/usr/bin/env python3
"""Offline content-analysis pilot. No network transport, key loading or live switch.

All money is simulated. Preview -> approve-simulation -> simulate -> status.
A successful simulation is NOT evidence of video quality, API entitlement or cost.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing as mp
import re
import sqlite3
import subprocess
import sys
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path
from urllib.parse import parse_qs, urlparse

SCHEMA = 1
PROMPT_VERSION = "content-analyst-pilot-v1"
RATES = {  # USD per million tokens, published 2026-09-14; estimates only.
    "gemini-3.7-flash": ("0.75", "3.75"),
    "gemini-3.8-flash": ("0.75", "3.75"),
    "gemini-3.5-flash-lite": ("0.30", "2.50"),
}
PRICE_EXPIRY = datetime(2027, 1, 1, tzinfo=timezone.utc).timestamp()
VIDEO_SUFFIXES = {".mp4", ".mov", ".webm", ".avi", ".mpeg", ".mpg", ".wmv", ".3gp"}


class Denied(ValueError):
    """Fail closed; caller must not retry or route around this failure."""


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def integer(value, label, low, high):
    if type(value) is not int or not low <= value <= high:
        raise Denied(f"{label} must be an integer in {low}..{high}")
    return value


def money(value):
    try:
        d = Decimal(str(value))
        if not d.is_finite() or d < 0 or d > 100:
            raise Denied("simulated budget must be finite and between $0 and $100")
        return int((d * 1_000_000).to_integral_value(rounding=ROUND_FLOOR))
    except (InvalidOperation, ValueError) as exc:
        raise Denied("invalid simulated budget") from exc


def usd(micro):
    return f"{Decimal(micro) / 1_000_000:.6f}"


def file_hash(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def classify_source(source):
    """Inspect only. Never resolve a remote link or upload a local file."""
    if not isinstance(source, str) or not source.strip():
        raise Denied("source must be a nonempty URL or file path")
    parsed = urlparse(source)
    if parsed.scheme in ("https", "http"):
        if parsed.username or parsed.password or parsed.port:
            raise Denied("URL credentials and custom ports are not supported")
        host = (parsed.hostname or "").lower()
        video_id = None
        if host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
            if parsed.path == "/watch":
                video_id = parse_qs(parsed.query).get("v", [None])[0]
            elif parsed.path.startswith(("/shorts/", "/embed/")):
                video_id = parsed.path.split("/")[2]
        elif host in {"youtu.be", "www.youtu.be"}:
            video_id = parsed.path.strip("/")
        if video_id and re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            return {"uri": f"https://www.youtube.com/watch?v={video_id}",
                    "route": "public-youtube-candidate", "access": "NOT_CHECKED"}
        return {"uri": source, "route": "retrieve-or-native-read-first",
                "access": "UNVERIFIED", "ready": False}
    if parsed.scheme:
        raise Denied("only http(s) or existing local video paths are accepted")
    path = Path(source).expanduser().resolve(strict=True)
    if not path.is_file() or path.suffix.lower() not in VIDEO_SUFFIXES:
        raise Denied("needs a supported local video; articles/carousels use their native reader")
    return {"uri": str(path), "route": "local-video", "access": "LOCAL_FILE_ONLY",
            "sha256": file_hash(path), "bytes": path.stat().st_size}


def quote_tokens(model, input_tokens, output_tokens):
    inp, out = RATES[model]
    # USD/M tokens multiplied by tokens yields micro-USD.
    return int((Decimal(inp) * input_tokens + Decimal(out) * output_tokens)
               .to_integral_value(rounding=ROUND_CEILING))


def compile_plan(request, now=None):
    now = time.time() if now is None else now
    if now >= PRICE_EXPIRY:
        raise Denied("pricing snapshot expired; refresh and review before previewing")
    if not isinstance(request, dict):
        raise Denied("request must be an object")
    question = request.get("question", "")
    if not isinstance(question, str) or not 1 <= len(question.strip()) <= 12000:
        raise Denied("provide a specific analysis question (1..12000 characters)")
    mode = request.get("mode", "extract")
    if mode not in {"discover", "taste", "extract", "adapt"}:
        raise Denied("mode must be discover, taste, extract or adapt")
    model = request.get("model", "gemini-3.7-flash")
    if model not in RATES:
        raise Denied("model is not in the reviewed pricing snapshot")
    resolution = request.get("resolution", "low")
    if resolution not in {"low", "high"}:
        raise Denied("resolution must be low or high")
    processing = request.get("processing", "static")
    if processing not in {"static", "agentic"}:
        raise Denied("processing must be static or agentic")
    output = integer(request.get("max_output_tokens", 8192), "output tokens", 1, 32768)
    timeout = integer(request.get("timeout_seconds", 30), "timeout seconds", 1, 60)
    items = request.get("items")
    if not isinstance(items, list) or not 1 <= len(items) <= 20:
        raise Denied("batch must contain 1..20 videos")
    plan = {"schema": SCHEMA, "environment": "simulation", "paid_execution": "DISABLED",
            "mode": mode, "question": question.strip(), "model": model,
            "processing": processing, "resolution": resolution,
            "max_output_tokens": output, "timeout_seconds": timeout,
            "max_calls": len(items), "retries": 0, "prompt_version": PROMPT_VERSION,
            "rates": list(RATES[model]), "pricing_expires_at": PRICE_EXPIRY,
            "cost_status": "STATIC_ESTIMATE_NOT_PROVIDER_CAP",
            "items": []}
    seen = set()
    for item in items:
        if not isinstance(item, dict):
            raise Denied("each video must be an object")
        source = classify_source(item.get("source"))
        if source.get("ready") is False:
            raise Denied(f"source needs retrieval or native reading first: {source['uri']}")
        seconds = integer(item.get("duration_seconds"), "declared duration", 1, 10800)
        # Duration is operator-supplied, not probed. This is a preview, not a cost guarantee.
        tokens = seconds * (100 if resolution == "low" else 300) + len(question) + 2048
        if tokens + output > 1_000_000:
            raise Denied("video exceeds conservative context allowance; preview bounded segments")
        fp = digest({"source": source, "seconds": seconds, "mode": mode,
                     "question": question.strip(), "model": model, "processing": processing,
                     "resolution": resolution, "output": output, "prompt": PROMPT_VERSION,
                     "environment": "simulation"})
        if fp in seen:
            raise Denied("duplicate video/request in batch; keep one copy")
        seen.add(fp)
        plan["items"].append({"source": source, "duration_seconds": seconds,
                              "duration_status": "DECLARED_NOT_PROBED", "key": fp,
                              "estimated_input_tokens": tokens,
                              "reserve_micro_usd": quote_tokens(model, tokens, output)})
    plan["estimated_total_usd"] = usd(sum(i["reserve_micro_usd"] for i in plan["items"]))
    plan["agentic_cost_bound"] = "UNVERIFIED" if processing == "agentic" else "NOT_APPLICABLE"
    return plan


def shared_state_dir():
    root = Path(__file__).resolve().parent.parent
    p = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
                       cwd=root, text=True, capture_output=True, timeout=5)
    if p.returncode == 0:
        root = Path(p.stdout.strip()).parent
    return root / ".agent" / "content-analysis-pilot"


def fake_provider(conn, item, plan, fault):
    """Child process with no network imports, credentials or real observations."""
    if fault == "timeout":
        time.sleep(plan["timeout_seconds"] + 10)
    if fault == "crash":
        conn.close()
        return
    result = {"environment": "simulation", "evidence_status": "SYNTHETIC_NOT_OBSERVED",
              "text": "Synthetic control test only. No video was watched.",
              "input_tokens": item["estimated_input_tokens"] // 2,
              "output_tokens": min(256, plan["max_output_tokens"])}
    if fault == "missing-usage":
        result.pop("input_tokens")
    elif fault == "overrun":
        result["input_tokens"] = item["estimated_input_tokens"] * 3
        result["output_tokens"] = plan["max_output_tokens"] * 3
    conn.send(result)
    conn.close()


class Pilot:
    def __init__(self, state_dir=None, clock=time.time):
        self.path = Path(state_dir) if state_dir is not None else shared_state_dir()
        self.path.mkdir(parents=True, exist_ok=True)
        self.clock = clock
        self.db = self.path / "simulation.sqlite3"
        with self.connect() as conn:
            conn.executescript("""
              CREATE TABLE IF NOT EXISTS batches (
                id TEXT PRIMARY KEY, plan TEXT NOT NULL, status TEXT NOT NULL,
                approval_budget INTEGER, approval_expires REAL, approval_note TEXT);
              CREATE TABLE IF NOT EXISTS calls (
                key TEXT PRIMARY KEY, batch_id TEXT NOT NULL, status TEXT NOT NULL,
                reserved INTEGER NOT NULL, actual INTEGER, result TEXT, error TEXT);
            """)

    def connect(self):
        conn = sqlite3.connect(self.db, timeout=5)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=FULL")
        return conn

    @contextmanager
    def transaction(self):
        conn = self.connect()
        try:
            conn.execute("BEGIN IMMEDIATE")
            yield conn
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()

    def _load(self, conn, batch):
        row = conn.execute("SELECT * FROM batches WHERE id=?", (batch,)).fetchone()
        if not row:
            raise Denied("unknown batch")
        try:
            plan = json.loads(row["plan"])
            valid = digest(plan) == batch and plan["environment"] == "simulation"
        except (ValueError, TypeError, KeyError):
            valid = False
        if not valid:
            raise Denied("stored preview failed integrity check; no execution")
        return row, plan

    def preview(self, request):
        plan = compile_plan(request, self.clock())
        batch = digest(plan)
        with self.transaction() as conn:
            conn.execute("INSERT OR IGNORE INTO batches(id,plan,status) VALUES(?,?,?)",
                         (batch, canonical(plan), "preview"))
        return {"batch": batch, "preview": plan}

    def approve(self, batch, expected_hash, budget_usd, note, ttl_seconds=900):
        budget = money(budget_usd)
        integer(ttl_seconds, "approval TTL", 1, 3600)
        if batch != expected_hash:
            raise Denied("approval hash does not match the preview")
        if not isinstance(note, str) or not note.strip():
            raise Denied("record the explicit simulation approval decision")
        with self.transaction() as conn:
            row, plan = self._load(conn, batch)
            if row["status"] not in {"preview", "approved"}:
                raise Denied("started, stopped or completed batches cannot be reapproved")
            if self.clock() >= plan["pricing_expires_at"]:
                raise Denied("pricing expired")
            required = sum(i["reserve_micro_usd"] for i in plan["items"])
            if budget < required:
                raise Denied(f"budget below preview reservation ${usd(required)}")
            expires = min(self.clock() + ttl_seconds, plan["pricing_expires_at"])
            conn.execute("UPDATE batches SET status='approved',approval_budget=?,"
                         "approval_expires=?,approval_note=? WHERE id=?",
                         (budget, expires, note.strip(), batch))
        return {"batch": batch, "status": "approved-for-simulation-only",
                "simulated_budget_usd": usd(budget), "paid_allowance_usd": "0"}

    def _check_approval(self, row, plan):
        if row["approval_budget"] is None:
            raise Denied("exact-batch simulation approval required")
        if self.clock() >= row["approval_expires"] or self.clock() >= plan["pricing_expires_at"]:
            raise Denied("approval or pricing expired; no further calls")

    def _reserve(self, batch, item):
        with self.transaction() as conn:
            row, plan = self._load(conn, batch)
            self._check_approval(row, plan)
            if row["status"] != "running":
                raise Denied("batch is not running")
            if conn.execute("SELECT 1 FROM calls WHERE status!='complete' LIMIT 1").fetchone():
                raise Denied("unresolved reservation: inspect receipt; no retry or new dispatch")
            source = item["source"]
            if source["route"] == "local-video" and file_hash(Path(source["uri"])) != source["sha256"]:
                raise Denied("source changed after preview; no dispatch")
            cached = conn.execute("SELECT * FROM calls WHERE key=?", (item["key"],)).fetchone()
            if cached:
                return json.loads(cached["result"])
            used = conn.execute("SELECT COALESCE(SUM(COALESCE(actual,reserved)),0) "
                                "FROM calls WHERE batch_id=?", (batch,)).fetchone()[0]
            if used + item["reserve_micro_usd"] > row["approval_budget"]:
                raise Denied("remaining approved budget insufficient")
            count = conn.execute("SELECT COUNT(*) FROM calls WHERE batch_id=?", (batch,)).fetchone()[0]
            if count >= plan["max_calls"]:
                raise Denied("request count exceeded")
            conn.execute("INSERT INTO calls(key,batch_id,status,reserved) VALUES(?,?,'reserved',?)",
                         (item["key"], batch, item["reserve_micro_usd"]))
            return None

    def _finish(self, batch, item, result=None, error=None):
        with self.transaction() as conn:
            _, plan = self._load(conn, batch)
            actual = None
            if error is None:
                try:
                    inp = integer(result["input_tokens"], "usage input", 0, 20_000_000)
                    out = integer(result["output_tokens"], "usage output", 0, 1_000_000)
                    if result["environment"] != "simulation":
                        raise Denied("wrong evidence environment")
                    actual = quote_tokens(plan["model"], inp, out)
                    if (inp > item["estimated_input_tokens"] or out > plan["max_output_tokens"]
                            or actual > item["reserve_micro_usd"]):
                        error = "usage exceeded the simulated envelope; stop and review"
                except (KeyError, TypeError, Denied):
                    error = "missing or invalid usage; liability stays reserved"
            status = "unknown" if error else "complete"
            # A reported overrun is retained at its larger actual value; never cap it in accounting.
            conn.execute("UPDATE calls SET status=?,actual=?,result=?,error=? WHERE key=?",
                         (status, actual, canonical(result) if result else None, error, item["key"]))
            if error:
                conn.execute("UPDATE batches SET status='stopped' WHERE id=?", (batch,))
        if error:
            raise Denied(error)

    def run(self, batch, *, live=False, fault="ok"):
        if live:
            raise Denied("LIVE EXECUTION DISABLED: no Gemini transport is installed; no paid approval exists")
        if fault not in {"ok", "timeout", "crash", "missing-usage", "overrun"}:
            raise Denied("unsupported simulation fault")
        with self.transaction() as conn:
            row, plan = self._load(conn, batch)
            if row["status"] == "complete":
                return self.status(batch)
            if row["status"] != "approved":
                raise Denied("batch needs approval, is already running, or has stopped")
            self._check_approval(row, plan)
            # Hash local bytes again BEFORE changing state or reserving any call.
            for item in plan["items"]:
                s = item["source"]
                if s["route"] == "local-video" and file_hash(Path(s["uri"])) != s["sha256"]:
                    raise Denied("source changed after preview; create a new batch")
            conn.execute("UPDATE batches SET status='running' WHERE id=?", (batch,))
        deadline = time.monotonic() + plan["timeout_seconds"]
        try:
            for item in plan["items"]:
                if time.monotonic() >= deadline:
                    raise Denied("batch deadline reached before dispatch")
                cached = self._reserve(batch, item)
                if cached is not None:
                    continue
                parent, child = mp.get_context("spawn").Pipe(duplex=False)
                process = mp.get_context("spawn").Process(target=fake_provider,
                                                          args=(child, item, plan, fault))
                result, error = None, None
                try:
                    process.start()
                    child.close()
                    if parent.poll(max(0, deadline - time.monotonic())):
                        try:
                            result = parent.recv()
                        except EOFError:
                            error = "provider exited without a receipt; liability stays reserved"
                    else:
                        error = "deadline exceeded; liability stays reserved"
                finally:
                    if process.pid is not None:
                        if process.is_alive():
                            process.terminate()
                        process.join(timeout=1)
                        if process.is_alive():
                            process.kill()
                            process.join(timeout=1)
                    parent.close()
                    child.close()
                self._finish(batch, item, result, error)
            with self.transaction() as conn:
                conn.execute("UPDATE batches SET status='complete' WHERE id=?", (batch,))
        except BaseException:
            # SIGKILL may skip this, but the committed reservation survives either way.
            with self.transaction() as conn:
                conn.execute("UPDATE batches SET status='stopped' WHERE id=?", (batch,))
            raise
        return self.status(batch)

    def status(self, batch):
        with self.connect() as conn:
            row, plan = self._load(conn, batch)
            calls = [dict(r) for r in conn.execute("SELECT * FROM calls WHERE batch_id=?", (batch,))]
            total = conn.execute("SELECT COALESCE(SUM(COALESCE(actual,reserved)),0) FROM calls").fetchone()[0]
            items = []
            for item in plan["items"]:
                cached = conn.execute("SELECT batch_id,status,result FROM calls WHERE key=?",
                                      (item["key"],)).fetchone()
                items.append({"source": item["source"]["uri"], "key": item["key"],
                              "status": cached["status"] if cached else "not-dispatched",
                              "reused": bool(cached and cached["batch_id"] != batch),
                              "result": json.loads(cached["result"]) if cached and cached["result"] else None})
        for call in calls:
            call["result"] = json.loads(call["result"]) if call["result"] else None
        return {"batch": batch, "status": row["status"], "environment": "simulation",
                "paid_execution": "DISABLED", "real_api_calls": 0, "real_spend_usd": "0",
                "simulated_liability_usd": usd(sum(c["actual"] if c["actual"] is not None
                                                  else c["reserved"] for c in calls)),
                "all_batches_simulated_liability_usd": usd(total), "calls": calls,
                "planned_items": len(plan["items"]), "items": items,
                "approval_note": row["approval_note"], "quality_proof": "NOT_RUN"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, help="isolated simulation store; default shared workspace store")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("preview")
    p.add_argument("request", type=Path)
    p = sub.add_parser("approve-simulation")
    p.add_argument("batch")
    p.add_argument("--hash", required=True)
    p.add_argument("--budget-usd", required=True)
    p.add_argument("--note", required=True)
    p.add_argument("--ttl-seconds", type=int, default=900)
    for name in ("simulate", "run", "status"):
        p = sub.add_parser(name)
        p.add_argument("batch")
        if name == "simulate":
            p.add_argument("--fault", default="ok", choices=["ok", "timeout", "crash", "missing-usage", "overrun"])
    args = parser.parse_args(argv)
    try:
        if args.command == "run":
            raise Denied("LIVE EXECUTION DISABLED: use simulate for offline controls; a live trial needs separate approval")
        pilot = Pilot(args.state_dir)
        if args.command == "preview":
            result = pilot.preview(json.loads(args.request.read_text()))
        elif args.command == "approve-simulation":
            result = pilot.approve(args.batch, args.hash, args.budget_usd, args.note, args.ttl_seconds)
        elif args.command == "simulate":
            result = pilot.run(args.batch, fault=args.fault)
        else:
            result = pilot.status(args.batch)
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0
    except (Denied, OSError, sqlite3.Error, ValueError) as exc:
        print(json.dumps({"status": "DENIED", "reason": str(exc), "real_api_calls": 0}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
