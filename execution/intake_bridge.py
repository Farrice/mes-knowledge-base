#!/usr/bin/env python3
"""
intake_bridge.py — deterministic bridge from Google Form submissions to
Growth Blueprint OS engagements ($0, read-only against the source).

Spec: growth-lab/intake/INTAKE-ENGINE.md · form kit: growth-lab/intake/google-form-kit.md
Column contract: Timestamp, Email Address, then the nine question titles EXACTLY
as the kit states them (Google Forms uses question titles as Sheet headers).
Optional extra column `Status` (added by hand in the Sheet, never in the form):
non-empty = handled, excluded from the pending count.

Commands:
  status [--sheet <id> | --csv <path>]
      List submissions with age vs the 48h promise clock. Writes
      .agent/intake/pending.json on every run (Homebase reads the count).
      Sheet mode attempts the gws CLI; on failure it prints the exact
      re-auth command and the CSV fallback — degrade loud, never silent.

  pull --row N (--csv <path> | --sheet <id>) --slug <client-slug> [--out-root growth-lab]
      Write growth-lab/<slug>/intake-pack.md in the FROZEN 9-section
      input-pack shape (provenance header, [V] verbatim labels, honest
      "NOT PROVIDED — interview fallback" for blanks), create/update the
      manifest.json engagement block, and print the fire commands.
      Row numbers are submission numbers as shown by `status` (header row
      excluded; submission #1 = first data row).

Both source modes parse the same header contract; the fixture CSV in
.scratch/kallaway-sandcastles-forge/fixture-intake.csv proves the parse.
"""
import argparse
import csv
import io
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PENDING_PATH = ROOT / ".agent" / "intake" / "pending.json"
CONFIG_PATH = ROOT / "growth-lab" / "intake" / "faces-config.json"
PROMISE_HOURS = 48

# ---- column contract (mirrors growth-lab/intake/google-form-kit.md) ----------
QUESTION_TITLES = (
    "What do you sell, and at what price?",                                   # Q1
    "Describe your ideal buyer: the one person you most want more of",        # Q2
    "If your content worked perfectly, what changes for you? (one sentence)", # Q3
    "Top 3 problems your buyers bring you, in their words",                   # Q4
    "What can you honestly claim that almost nobody else in your space can?", # Q5
    "Where does your content live today, and what gets in the way?",          # Q6
    "Which creators or competitors do you watch? (names or links, up to 5)",  # Q7
    "What matters most right now?",                                           # Q8
    "Which report should we build first?",                                    # Q9
)
EMAIL_HEADERS = ("email address", "email", "username")
STATUS_HEADER = "status"

# ---- FROZEN input-pack shape (baseline: extractions/kallaway/baseline-input-pack.md)
# Section order and stems are the contract; parentheticals adapt he->they /
# source-notes only. verify scripts diff stems against the baseline file.
FROZEN_SECTIONS = (
    "The business behind the content",
    "Ideal viewer/buyer avatar",
    "Dream outcome (one sentence)",
    "Pain points bank (ranked, in their words)",
    "Unfair advantage / unique expertise inventory",
    "Target Authority Statement candidates",
    "Platform reality",
    "Known competitors/creators they watch",
    "Delivery style",
)
# question index (0-based) feeding each section; None = interview fallback
SECTION_SOURCE = (0, 1, 2, 3, 4, None, 5, 6, None)

# ---- routing (Q9 label prefix -> gb-* chain; labels per google-form-kit.md) --
ROUTES = {
    "Positioning Dossier": ("positioning-dossier", ["/gb-interview"]),
    "Whitespace Map": ("whitespace-map", ["/gb-interview", "/gb-whitespace"]),
    "Audience Bullseye": ("bullseye", ["/gb-interview", "/gb-whitespace", "/gb-bullseye"]),
    "Topic Scan": ("topic-scan", ["/gb-topic-scan"]),
    "Format Playbook": ("format-playbook", ["/gb-topic-scan", "/gb-format-find"]),
    "Growth Blueprint": ("growth-blueprint",
                         ["/gb-interview", "/gb-whitespace", "/gb-bullseye",
                          "/gb-topic-scan", "/gb-format-find", "/growth-blueprint"]),
}
# "Not sure" recommendation by Q8 primary goal (documented in INTAKE-ENGINE.md)
RECOMMEND_BY_GOAL = {"reach": "Topic Scan", "trust": "Positioning Dossier",
                     "conversion": "Whitespace Map"}


def norm(s):
    """Header-matching normalizer: casefold, strip punctuation, collapse spaces."""
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", str(s or ""))).strip().casefold()


def parse_ts(raw):
    """Google Sheets timestamps arrive as '8/25/2026 14:03:22' (US locale) or ISO.
    Returns aware-UTC datetime or None (naive values are treated as local-naive UTC
    for age math — a labeled approximation, not a claim)."""
    raw = str(raw or "").strip()
    if not raw:
        return None
    for parse in (
        lambda s: datetime.fromisoformat(s.replace("Z", "+00:00")),
        lambda s: datetime.strptime(s, "%m/%d/%Y %H:%M:%S"),
        lambda s: datetime.strptime(s, "%m/%d/%Y %H:%M"),
        lambda s: datetime.strptime(s, "%Y-%m-%d %H:%M:%S"),
    ):
        try:
            dt = parse(raw)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def age_hours(ts):
    if ts is None:
        return None
    return (datetime.now(timezone.utc) - ts).total_seconds() / 3600


# ------------------------------------------------------------------ sources ---

def read_csv_rows(path):
    p = Path(path)
    if not p.exists():
        raise SystemExit(f"[intake_bridge] FAIL — CSV not found: {p}")
    with open(p, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        raise SystemExit(f"[intake_bridge] FAIL — CSV is empty: {p}")
    return rows, f"csv:{p}"


def read_sheet_rows(sheet_id, tab="Form Responses 1"):
    """Read the linked Sheet via the gws CLI. Degrade LOUD on any failure:
    name the exact re-auth command and the always-works CSV fallback."""
    params = json.dumps({"spreadsheetId": sheet_id, "range": f"{tab}!A1:T500"})
    cmd = ["gws", "sheets", "spreadsheets", "values", "get", "--params", params]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except FileNotFoundError:
        raise SystemExit("[intake_bridge] FAIL — `gws` CLI not on PATH.\n"
                         "  Fallback (always works): File > Download > CSV from the Sheet, then --csv <path>")
    except subprocess.TimeoutExpired:
        raise SystemExit("[intake_bridge] FAIL — gws timed out after 60s.\n"
                         "  Retry, or fall back to --csv <exported file>")
    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "").strip()[:400]
        hint = ("  Auth expired (7-day OAuth window). Re-auth with exactly:\n"
                "      gws auth login\n" if proc.returncode == 2 else "")
        raise SystemExit(f"[intake_bridge] FAIL — gws exit {proc.returncode}: {err}\n{hint}"
                         "  Fallback (always works): File > Download > CSV from the Sheet, then --csv <path>")
    try:
        values = json.loads(proc.stdout).get("values") or []
    except json.JSONDecodeError:
        raise SystemExit("[intake_bridge] FAIL — gws returned non-JSON output; run with --csv fallback")
    if not values:
        raise SystemExit(f"[intake_bridge] FAIL — sheet {sheet_id} range '{tab}' returned no rows")
    return values, f"sheet:{sheet_id}"


def resolve_source(args, need=True):
    if args.csv:
        return read_csv_rows(args.csv)
    sheet_id = args.sheet or ""
    if not sheet_id:
        try:
            cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            sheet_id = (cfg.get("sheet_id") or "").strip()
        except (OSError, ValueError):
            sheet_id = ""
    if sheet_id:
        return read_sheet_rows(sheet_id)
    if need:
        raise SystemExit("[intake_bridge] FAIL — no source: pass --csv <path> or --sheet <id> "
                         "(or set sheet_id in growth-lab/intake/faces-config.json)")
    return None, None


# ---------------------------------------------------------------- contract ----

def map_columns(header):
    """Return dict: {'ts': i, 'email': i|None, 'status': i|None, 'q': [i x9]}.
    Exact match first, normalized match second, loud failure third."""
    normed = [norm(h) for h in header]

    def find(title):
        if title in header:
            return header.index(title)
        n = norm(title)
        return normed.index(n) if n in normed else None

    ts_i = find("Timestamp")
    if ts_i is None:
        ts_i = 0  # Google Forms always emits Timestamp first; declare the assumption
    email_i = next((i for i, h in enumerate(normed) if h in EMAIL_HEADERS), None)
    status_i = next((i for i, h in enumerate(normed) if h == STATUS_HEADER), None)

    q_idx, missing = [], []
    for title in QUESTION_TITLES:
        i = find(title)
        if i is None:
            missing.append(title)
        q_idx.append(i)
    if missing:
        raise SystemExit("[intake_bridge] FAIL — header contract mismatch. Missing column(s):\n"
                         + "".join(f"    · {m}\n" for m in missing)
                         + f"  Found headers: {header}\n"
                         "  The form question titles must match growth-lab/intake/google-form-kit.md exactly.")
    return {"ts": ts_i, "email": email_i, "status": status_i, "q": q_idx}


def cell(row, i):
    if i is None or i >= len(row):
        return ""
    return str(row[i]).strip()


def submissions(rows):
    """Yield dicts for each data row (submission #1 = first row after header)."""
    header = [str(h).strip() for h in rows[0]]
    cols = map_columns(header)
    out = []
    for n, row in enumerate(rows[1:], 1):
        if not any(str(c).strip() for c in row):
            continue
        ts = parse_ts(cell(row, cols["ts"]))
        out.append({
            "n": n,
            "timestamp_raw": cell(row, cols["ts"]),
            "timestamp": ts.isoformat() if ts else None,
            "age_h": age_hours(ts),
            "email": cell(row, cols["email"]) or "(no email column)",
            "status": cell(row, cols["status"]),
            "answers": [cell(row, i) for i in cols["q"]],
        })
    return out


def route_for(sub):
    """(artifact_key, chain, note) from the Q9 label; 'Not sure' resolves via Q8."""
    q9 = sub["answers"][8]
    goal = sub["answers"][7].split("-")[0].strip().casefold()
    for prefix, (key, chain) in ROUTES.items():
        if q9.startswith(prefix):
            return key, chain, f"selector: {prefix}"
    if q9.casefold().startswith("not sure"):
        rec = RECOMMEND_BY_GOAL.get(goal, "Positioning Dossier")
        key, chain = ROUTES[rec]
        return key, chain, f"selector: not sure -> recommended {rec} (goal: {goal or 'unstated'})"
    return None, ["/gb-interview"], f"selector unrecognized ({q9[:60]!r}) -> default interview start"


def parse_seeds(q7_answer):
    """Radar niche seeds from the creators-watched answer: @handles + channel URLs."""
    seeds = []
    for m in re.findall(r"(?:youtube\.com/|youtu\.be/)(@[\w.\-]+)", q7_answer):
        seeds.append(m)
    for m in re.findall(r"(?<![\w/.])@[\w.\-]{2,}", q7_answer):
        seeds.append(m)
    seen, out = set(), []
    for s in seeds:
        if s.casefold() not in seen:
            seen.add(s.casefold())
            out.append(s)
    return out


# ------------------------------------------------------------------ status ----

def cmd_status(args):
    rows, source = resolve_source(args)
    subs = submissions(rows)
    pending = [s for s in subs if not s["status"]]
    overdue = [s for s in pending if s["age_h"] is not None and s["age_h"] > PROMISE_HOURS]

    print(f"[intake_bridge] source={source} — {len(subs)} submission(s), "
          f"{len(pending)} pending, {len(overdue)} past the {PROMISE_HOURS}h promise")
    for s in subs:
        if s["age_h"] is None:
            age = f"age unknown (timestamp {s['timestamp_raw']!r} unparseable)"
        else:
            age = f"age {s['age_h']:.1f}h of {PROMISE_HOURS}h"
            if s["age_h"] > PROMISE_HOURS and not s["status"]:
                age += "  << PAST PROMISE"
        handled = f"  [handled: {s['status']}]" if s["status"] else ""
        print(f"  #{s['n']}  {s['email']}  ·  {s['answers'][8][:52] or '(no artifact answer)'}  ·  {age}{handled}")

    PENDING_PATH.parent.mkdir(parents=True, exist_ok=True)
    receipt = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "submission_count": len(subs),
        "pending_count": len(pending),
        "overdue_count": len(overdue),
        "promise_hours": PROMISE_HOURS,
        "rows": [{"n": s["n"], "email": s["email"], "age_h": round(s["age_h"], 1) if s["age_h"] is not None else None,
                  "artifact": s["answers"][8][:80]} for s in pending],
    }
    PENDING_PATH.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"[intake_bridge] wrote {PENDING_PATH.relative_to(ROOT)} "
          f"(pending={len(pending)}, overdue={len(overdue)})")
    return 0


# -------------------------------------------------------------------- pull ----

def verbatim_block(answer, note=None):
    if not answer:
        return "- NOT PROVIDED — interview fallback\n"
    lines = [ln.strip() for ln in str(answer).splitlines() if ln.strip()]
    out = "".join(f'- [V] "{ln}"\n' for ln in lines)
    if note:
        out += f"- {note}\n"
    return out


def build_intake_pack(sub, source, slug):
    now = datetime.now(timezone.utc)
    ts = sub["timestamp"] or f"UNPARSEABLE ({sub['timestamp_raw']!r})"
    if sub["age_h"] is None:
        clock = "48h clock: UNKNOWN — submission timestamp unparseable; treat as due now"
    else:
        left = PROMISE_HOURS - sub["age_h"]
        clock = (f"48h clock: {sub['age_h']:.1f}h elapsed — "
                 + (f"{left:.1f}h remaining" if left > 0 else f"PAST PROMISE by {-left:.1f}h"))
    key, chain, route_note = route_for(sub)
    seeds = parse_seeds(sub["answers"][6])

    a = sub["answers"]
    head = (
        f"# INTAKE PACK — {sub['email']} ({slug})\n\n"
        f"> **Provenance:** Google Form submission #{sub['n']} · submitted {ts} · "
        f"pulled {now.isoformat()} · source {source}\n"
        f"> {clock}\n"
        f"> Labels: [V] = the client's verbatim answer, exactly as typed. Absent answers are declared,\n"
        f"> never invented. Shape: FROZEN 9-section input-pack "
        f"(baseline: extractions/kallaway/baseline-input-pack.md).\n\n---\n\n"
    )

    sections = []
    bodies = {
        0: verbatim_block(a[0]),
        1: verbatim_block(a[1]),
        2: verbatim_block(a[2]),
        3: verbatim_block(a[3], "Ranked as given; the verbatim pain-mining step (gb-interview Step 3) replaces memory with evidence."),
        4: verbatim_block(a[4]),
        5: verbatim_block(a[5]) + f"- Primary goal (form Q8): " + (f'[V] "{a[7]}"\n' if a[7] else "NOT PROVIDED\n"),
        6: verbatim_block(a[6], (f"Radar seeds parsed from the answer: {', '.join(seeds)} — verify before add-channels."
                                 if seeds else "No @handles or channel URLs parseable — ask for links in the kickoff reply.")),
    }
    for i, (stem, src_q) in enumerate(zip(FROZEN_SECTIONS, SECTION_SOURCE)):
        if src_q is None:
            body = ("- NOT PROVIDED — interview fallback (drafted live in /gb-interview Block 5; never invented from form text)\n"
                    if "Authority" in stem else
                    "- NOT PROVIDED — interview fallback (voice and register are captured live in /gb-interview; never inferred from form text)\n")
        else:
            body = bodies[src_q]
        sections.append(f"## {stem}\n\n{body}\n")

    tail = (
        "---\n\n"
        "## Engagement routing (intake metadata — not part of the frozen shape)\n\n"
        f"- Artifact interest (form Q9): " + (f'[V] "{a[8]}"\n' if a[8] else "NOT PROVIDED\n") +
        f"- Primary goal (form Q8): " + (f'[V] "{a[7]}"\n' if a[7] else "NOT PROVIDED\n") +
        f"- Route: {route_note}\n"
        f"- Paid chain when Farrice fires it: {' -> '.join(chain)}\n"
        f"- Free mini first (default): see growth-lab/intake/INTAKE-ENGINE.md §Free-mini recipe\n"
    )
    return head + "\n".join(sections) + tail, key, chain, seeds


def update_manifest(dirpath, slug, sub, artifact_key, source):
    manifest_path = dirpath / "manifest.json"
    manifest = {}
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            backup = manifest_path.with_suffix(".json.unreadable")
            manifest_path.rename(backup)
            print(f"[intake_bridge] WARN — existing manifest unreadable; moved to {backup.name}")
            manifest = {}
    manifest.setdefault("niche_slug", slug)
    manifest["engagement"] = {
        "client": sub["email"],
        "mode": "client",
        "offer_map": ("free mini-report -> paid full "
                      f"{artifact_key or 'artifact (to be recommended)'} "
                      "(payment link: payment_url in growth-lab/intake/faces-config.json — unset = pending Stripe task)"),
        "intake": {
            "source": source,
            "submission_n": sub["n"],
            "submitted_at": sub["timestamp"],
            "artifact_interest": sub["answers"][8],
            "primary_goal": sub["answers"][7],
            "pulled_at": datetime.now(timezone.utc).isoformat(),
            "promise_hours": PROMISE_HOURS,
        },
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest_path


def cmd_pull(args):
    rows, source = resolve_source(args)
    subs = submissions(rows)
    match = next((s for s in subs if s["n"] == args.row), None)
    if match is None:
        raise SystemExit(f"[intake_bridge] FAIL — no submission #{args.row} "
                         f"(source has {len(subs)}; numbers are as shown by `status`)")
    slug = args.slug
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
        raise SystemExit(f"[intake_bridge] FAIL — slug must be kebab-case: {slug!r}")

    pack, artifact_key, chain, seeds = build_intake_pack(match, source, slug)
    dirpath = Path(args.out_root) if Path(args.out_root).is_absolute() else ROOT / args.out_root
    dirpath = dirpath / slug
    dirpath.mkdir(parents=True, exist_ok=True)
    pack_path = dirpath / "intake-pack.md"
    pack_path.write_text(pack, encoding="utf-8")
    manifest_path = update_manifest(dirpath, slug, match, artifact_key, source)

    print(f"[intake_bridge] wrote {pack_path}")
    print(f"[intake_bridge] engagement block -> {manifest_path}")
    print("\nFire when ready (manual, never automatic):")
    print(f"  /gb-intake   — reads {pack_path.relative_to(ROOT) if pack_path.is_relative_to(ROOT) else pack_path}")
    if seeds:
        print(f"  free mini:   .venv/bin/python3 execution/outlier_radar.py add-channels --niche {slug} " + " ".join(seeds))
    else:
        print(f"  free mini:   .venv/bin/python3 execution/outlier_radar.py add-channels --niche {slug} <@handles — none parseable from Q7; ask>")
    print(f"               .venv/bin/python3 execution/outlier_radar.py refresh --niche {slug}")
    print(f"  paid chain ({artifact_key or 'recommend'}): {' -> '.join(chain)}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Bridge Google Form intake submissions to Growth Blueprint OS engagements.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_status = sub.add_parser("status", help="List submissions + 48h clock; writes .agent/intake/pending.json")
    p_status.add_argument("--csv", help="Exported-Sheet CSV path (always-works fallback)")
    p_status.add_argument("--sheet", help="Google Sheet id (gws CLI; falls back loud)")
    p_status.set_defaults(func=cmd_status)

    p_pull = sub.add_parser("pull", help="Write growth-lab/<slug>/intake-pack.md in the frozen shape")
    p_pull.add_argument("--row", type=int, required=True, help="Submission number as shown by status")
    p_pull.add_argument("--csv", help="Exported-Sheet CSV path")
    p_pull.add_argument("--sheet", help="Google Sheet id")
    p_pull.add_argument("--slug", required=True, help="Client slug (kebab-case) — names growth-lab/<slug>/")
    p_pull.add_argument("--out-root", default="growth-lab", help="Root dir for the engagement folder (default growth-lab)")
    p_pull.set_defaults(func=cmd_pull)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
