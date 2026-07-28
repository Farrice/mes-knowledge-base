#!/usr/bin/env python3
"""verify_self_heal.py — prove the self-healer heals nothing it shouldn't.

A self-healing layer is the most dangerous thing in a harness: it edits state
without asking. The value is entirely in what it REFUSES to touch. So the
safety properties get tested first and hardest:

  1. `report` mutates nothing.
  2. Drift with NO commit trail is JUDGMENT — never blessed. That silence is
     the loss signal the drift check exists to catch, and auto-blessing it
     would delete the only warning that work went missing.
  3. Unknown failures default to JUDGMENT. Allowlist only.
  4. A heal that doesn't verify green reports heal_failed, never success.
  5. No healer "fixes" anything by loosening a threshold.

Joins the Sunday fleet via the execution/verify_*.py glob.

Usage: python3 execution/verify_self_heal.py
Exit:  0 all pass · 1 any failure
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOD = ROOT / "execution" / "self_heal.py"
BASELINE = ROOT / ".agent" / "health" / "born-intent-baseline.json"
PY = sys.executable

FAILURES: list[str] = []
PASSES = 0
PORCELAIN_AT_START = ""


def git_arg_lists(path: Path) -> list[list[str]]:
    """Every literal argv list in the source whose first element is "git".

    FOURTH ATTEMPT, and the lesson (2026-07-27): three prior versions of this
    assertion string-matched the source and produced FALSE REDS — first on the
    docstring documenting `--since=`, then on the comment documenting `git add
    -A`, then on a local variable named `add` followed by `.returncode`. Textual
    matching cannot tell code from prose from coincidence. Parse the AST and
    inspect the actual argv lists instead; nothing else is trustworthy.
    """
    import ast
    out: list[list[str]] = []
    try:
        tree = ast.parse(path.read_text())
    except SyntaxError:
        return out
    for node in ast.walk(tree):
        if not isinstance(node, ast.List):
            continue
        parts = [e.value for e in node.elts
                 if isinstance(e, ast.Constant) and isinstance(e.value, str)]
        if parts and parts[0] == "git":
            out.append(parts)
    return out


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASSES
    if ok:
        PASSES += 1
        print(f"  PASS  {label}")
    else:
        FAILURES.append(f"{label}{(' — ' + detail) if detail else ''}")
        print(f"  FAIL  {label}{(' — ' + detail) if detail else ''}")


def main() -> int:
    print("verify_self_heal.py — self-healing safety contract\n")

    check("module exists", MOD.exists(), str(MOD))
    if FAILURES:
        return 1
    r = subprocess.run([PY, "-m", "py_compile", str(MOD)], capture_output=True, text=True)
    check("self_heal.py compiles", r.returncode == 0, (r.stderr or "")[:160])
    if FAILURES:
        return 1

    global PORCELAIN_AT_START
    PORCELAIN_AT_START = subprocess.run(
        ["git", "status", "--porcelain"], cwd=str(ROOT),
        capture_output=True, text=True, timeout=30).stdout

    sys.path.insert(0, str(ROOT / "execution"))
    import self_heal  # noqa: E402

    # ── 1. report mode is READ-ONLY ────────────────────────────────────────
    before = BASELINE.stat().st_mtime if BASELINE.exists() else None
    p = subprocess.run([PY, str(MOD), "report"], capture_output=True, text=True,
                       timeout=300, cwd=str(ROOT))
    after = BASELINE.stat().st_mtime if BASELINE.exists() else None
    check("report exits 0", p.returncode == 0, (p.stderr or "")[:160])
    check("report does NOT touch the born-intent baseline", before == after,
          f"{before} -> {after}")
    check("report renders a SELF-HEAL block", "SELF-HEAL" in (p.stdout or ""))

    # ── 2. THE SAFETY PROPERTY: no commit trail => JUDGMENT, never blessed ─
    #    A fabricated anchor pointing at a path git has never seen. If this
    #    ever classifies EVIDENCE, the healer would silently bless away the
    #    exact signal that says work disappeared.
    ghost = self_heal.classify_drift(["skill:__nonexistent_ghost_skill__"])
    check("drift with NO commit trail classifies JUDGMENT",
          ghost["cls"] == self_heal.JUDGMENT, json.dumps(ghost)[:220])
    check("no-trail drift is described as a loss signal",
          "loss signal" in ghost.get("what", ""), ghost.get("what", "")[:160])

    # A MIXED set (one explained, one not) must escalate the whole batch —
    # blessing the batch would bless the unexplained one along with it.
    real = "skill:dara-denney-meta-ads"
    mixed = self_heal.classify_drift([real, "skill:__nonexistent_ghost_skill__"])
    check("mixed explained/unexplained drift escalates the WHOLE batch",
          mixed["cls"] == self_heal.JUDGMENT, json.dumps(mixed)[:220])

    # ── 2b. REGRESSION: the verdict must not depend on the baseline's mtime ─
    #    The first version keyed deliberateness to `git log --since=<baseline
    #    mtime>`. verify_born_intent_drift rewrites that file on every run to
    #    adopt newborn anchors, so the window collapsed and a correct EVIDENCE
    #    verdict flipped to JUDGMENT mid-heal. The verdict must now be stable
    #    across a baseline touch.
    # D2 (2026-07-27): this probe used to call BASELINE.touch() on a GIT-TRACKED
    # file. A verifier must not mutate repo state to test a property. The verdict
    # is now timestamp-free by construction, so stability is proven from source
    # plus repeated evaluation — no file is touched at all.
    before_v = self_heal.classify_drift([real])["cls"]
    after_v = self_heal.classify_drift([real])["cls"]
    check("drift verdict is stable across repeated evaluation (regression)",
          before_v == after_v, f"{before_v} -> {after_v}")
    check("a committed, clean anchor classifies EVIDENCE",
          before_v == self_heal.EVIDENCE, f"got {before_v}")
    # Match LIVE CODE, not prose. The first version of this check searched the
    # raw source for "--since=" and tripped on the docstring that documents the
    # very bug it guards against — a false RED produced by a test reading its
    # own documentation. The live form was f"--since={since_iso}", so anchor on
    # the interpolation brace, and confirm no git call passes the flag at all.
    src_ts = MOD.read_text()
    live_window = ("--since={" in src_ts) or ('"--since="' in src_ts)
    check("no baseline-mtime time window remains in live code",
          not live_window, "a git --since= window is still being built")
    check("_commit_evidence no longer reads the baseline's mtime",
          "BASELINE.stat()" not in src_ts, "baseline mtime still consulted")

    # ── 2c. D1: a `report` run must NOT touch the heal-mode cache ──────────
    #    self_heal writes LATEST for heal and REPORT_CACHE for report. The first
    #    version wrote LATEST in both modes, so every fleet run (which shells out
    #    to `report`) replaced the record of what was actually repaired.
    latest = ROOT / ".agent" / "health" / "self-heal-latest.json"
    lm_before = latest.stat().st_mtime if latest.exists() else None
    subprocess.run([PY, str(MOD), "report"], capture_output=True, text=True,
                   timeout=300, cwd=str(ROOT))
    lm_after = latest.stat().st_mtime if latest.exists() else None
    check("a `report` run does NOT touch the heal-mode cache (D1)",
          lm_before == lm_after, f"{lm_before} -> {lm_after}")
    check("heal and report caches are distinct paths",
          self_heal.LATEST != self_heal.REPORT_CACHE)

    # ── 2d. THE COMMIT SAFETY PROPERTY: scoped add, never `git add -A` ─────
    #    A cron-invoked committer that stages everything would sweep up whatever
    #    else happened to be in the tree. Every healer declares its write-set and
    #    the staged result is verified against it before committing.
    csrc = MOD.read_text()
    gitcalls = git_arg_lists(MOD)
    adds = [g for g in gitcalls if len(g) > 1 and g[1] == "add"]
    unscoped = [g for g in adds if any(a in ("-A", "--all", ".", "-u") for a in g)]
    check("no unscoped `git add` in any real git call (AST-checked)",
          not unscoped, f"unscoped: {unscoped}")
    check("a `git add` call site exists and passes an explicit separator",
          any("--" in g for g in adds), f"add calls: {adds}")
    check("every AUTO/EVIDENCE healer declares a write-set",
          set(self_heal.HEALERS) <= set(self_heal.HEALER_WRITES),
          f"undeclared: {set(self_heal.HEALERS) - set(self_heal.HEALER_WRITES)}")
    check("commit honours SELF_HEAL_NO_AUTOCOMMIT",
          "SELF_HEAL_NO_AUTOCOMMIT" in csrc)
    check("--no-commit short-circuits before any git call",
          "if no_commit:" in csrc and csrc.index("if no_commit:") < csrc.index('"git", "add"'))
    check("staged set is verified against the declaration before commit",
          "stray" in csrc and '"reset", "HEAD"' in csrc)

    # ── 2d-bis. THE POSITIVE COMMIT PATH, proven in a sandbox repo ────────
    #    Source assertions prove no `git add -A` exists. They cannot prove the
    #    commit actually EXCLUDES an undeclared dirty file. This builds a throw-
    #    away repo, dirties one file inside the healer's write-set and one
    #    outside it, commits, and asserts only the declared file moved. The real
    #    repo is never touched.
    import tempfile, shutil
    sandbox = Path(tempfile.mkdtemp(prefix="verify-sh-commit-"))
    def _sh(*a):
        return subprocess.run(a, cwd=sandbox, capture_output=True, text=True, timeout=30)
    try:
        _sh("git", "init", "-q")
        _sh("git", "config", "user.email", "t@t"); _sh("git", "config", "user.name", "t")
        (sandbox / ".agent" / "health").mkdir(parents=True)
        (sandbox / ".agent" / "health" / "born-intent-baseline.json").write_text('{"a":1}\n')
        (sandbox / "UNRELATED.md").write_text("do not commit me\n")
        _sh("git", "add", "-A"); _sh("git", "commit", "-qm", "base")
        (sandbox / ".agent" / "health" / "born-intent-baseline.json").write_text('{"a":2}\n')
        (sandbox / "UNRELATED.md").write_text("still must not be committed\n")
        real_root = self_heal.ROOT
        self_heal.ROOT = sandbox
        try:
            note = self_heal._commit_healed("born_intent_drift", "sandbox probe")
            committed = _sh("git", "show", "--stat", "--format=", "HEAD").stdout
            dirty_after = _sh("git", "status", "--porcelain").stdout
        finally:
            self_heal.ROOT = real_root
        check("scoped commit includes the healer's declared file",
              "born-intent-baseline.json" in committed, f"note={note}")
        check("scoped commit EXCLUDES an undeclared dirty file",
              "UNRELATED" not in committed and "UNRELATED.md" in dirty_after,
              f"committed={committed.strip()[:120]}")
    except Exception as e:  # noqa: BLE001
        check("scoped commit sandbox probe runs", False, f"{type(e).__name__}: {e}")
    finally:
        shutil.rmtree(sandbox, ignore_errors=True)

    # A pre-staged index must abort rather than fold someone else's work in.
    check("commit refuses to run when the index already has staged changes",
          "index already has staged changes" in csrc)

    # ── 2e. GIT CLEANLINESS: the suite itself must not dirty the tree ──────
    porcelain_now = subprocess.run(["git", "status", "--porcelain"], cwd=str(ROOT),
                                   capture_output=True, text=True, timeout=30).stdout
    check("verifier has not dirtied the working tree so far",
          porcelain_now == PORCELAIN_AT_START,
          "the suite mutated tracked state")

    # ── 3. heal refuses to act on a JUDGMENT classification ────────────────
    #    Verified structurally: heal() only dispatches to HEALERS for non-
    #    JUDGMENT rows, and heal_born_intent_drift re-detects before blessing.
    out = self_heal.heal([{"id": "born_intent_drift", "cls": self_heal.JUDGMENT,
                           "what": "x", "fix": "y"}])
    check("heal() escalates a JUDGMENT row instead of fixing it",
          out and out[0].get("action") == "escalated", json.dumps(out)[:200])
    out2 = self_heal.heal([{"id": "totally_unknown_failure", "cls": self_heal.AUTO,
                            "what": "x", "fix": "y"}])
    check("heal() escalates an id that is not on the allowlist",
          out2 and out2[0].get("action") == "escalated", json.dumps(out2)[:200])

    # ── 4. anchor-key resolution matches collect_anchors() ─────────────────
    cases = {
        "skill:foo": ROOT / "skills" / "foo" / "SKILL.md",
        "workflow:bar": ROOT / ".agent" / "workflows" / "bar.md",
        "agent:baz": ROOT / "agents" / "baz" / "AGENT.md",
        "prompt:foo/qux": ROOT / "skills" / "foo" / "references" / "prompts-v2" / "qux.md",
    }
    bad = [k for k, want in cases.items() if self_heal._anchor_path(k) != want]
    check("every anchor kind resolves to the right path", not bad, f"wrong: {bad}")
    check("a malformed anchor key resolves to None",
          self_heal._anchor_path("garbage-no-colon") is None)

    # ── 5. no healer launders a failure by weakening an assertion ──────────
    src = MOD.read_text()
    launder = [w for w in ("--bless-all", "top_k=10", "assert True", "pytest.skip")
               if w in src]
    check("no assertion-weakening shortcuts in the healer", not launder, f"found: {launder}")
    check("allowlist is small and explicit", len(self_heal.HEALERS) <= 8,
          f"{len(self_heal.HEALERS)} healers")

    # ── 6. every healer verifies its own work ──────────────────────────────
    #    A heal that returns True without re-running its check is a heal that
    #    can report success on a still-broken system.
    import inspect
    for hid, (_, healer) in self_heal.HEALERS.items():
        body = inspect.getsource(healer)
        check(f"healer '{hid}' re-runs a verifier before claiming success",
              "verify_" in body, "no verify_* call in the healer body")

    # ── 6b. HOLE REGRESSION: an owned-but-undetected red verifier must still
    #    appear. verify_system.py was skipped unconditionally, so when it began
    #    failing for a reason no healer knew about (SLASH_COMMANDS.md drift),
    #    the failure disappeared from the report entirely.
    import json as _j
    fleet = ROOT / ".agent" / "health" / "verify-fleet.json"
    if fleet.exists():
        try:
            _d = _j.loads(fleet.read_text())
            _red = {str(r.get("name") or r.get("script")) for r in _d.get("results", [])
                    if str(r.get("status", "")).upper() in ("FAIL", "TIMEOUT")}
        except (OSError, ValueError):
            _red = set()
        for owned in set(self_heal.HEALER_OWNS.values()):
            if owned not in _red:
                continue
            rows_none = self_heal.fleet_unhealed(set())   # no healer found anything
            check(f"red-but-unrepresented '{owned}' is surfaced, not skipped",
                  any(r["id"] == owned for r in rows_none),
                  f"missing from {[r['id'] for r in rows_none]}")
    check("every detector declares which verifier it owns",
          set(self_heal.HEALERS) | set(self_heal.CLASSIFIERS) == set(self_heal.HEALER_OWNS),
          f"mismatch: {(set(self_heal.HEALERS)|set(self_heal.CLASSIFIERS)) ^ set(self_heal.HEALER_OWNS)}")
    check("classify-only detectors are NOT dispatchable by heal()",
          not (set(self_heal.CLASSIFIERS) & set(self_heal.HEALERS)),
          f"overlap: {set(self_heal.CLASSIFIERS) & set(self_heal.HEALERS)}")
    _cls_rows = self_heal.heal([{"id": k, "cls": self_heal.AUTO, "what": "x", "fix": "y"}
                                for k in self_heal.CLASSIFIERS])
    check("a classify-only id is escalated even if mislabelled AUTO",
          all(r.get("action") == "escalated" for r in _cls_rows), json.dumps(_cls_rows)[:200])

    # ── 7. detectors are exception-safe (a broken detector must not stop the scan)
    orig = self_heal.HEALERS.get("stale_registries")

    def boom():
        raise RuntimeError("simulated detector explosion")

    self_heal.HEALERS["stale_registries"] = (boom, orig[1])
    try:
        rows = self_heal.scan()
        check("a raising detector degrades to JUDGMENT instead of crashing scan()",
              any(r["id"] == "stale_registries" and r["cls"] == self_heal.JUDGMENT
                  for r in rows), json.dumps(rows)[:200])
    except Exception as e:  # noqa: BLE001
        check("a raising detector degrades to JUDGMENT instead of crashing scan()",
              False, f"{type(e).__name__}: {e}")
    finally:
        self_heal.HEALERS["stale_registries"] = orig

    print(f"\n{PASSES} passed, {len(FAILURES)} failed")
    if FAILURES:
        print("\nFAILURES:")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
