#!/usr/bin/env python3
"""generate_media.py — recipe-driven media generation engine (/generate skill).

The thin fourth caller of fal_budget_guard.py — NOT a replacement for the
proven wrappers. Division of labor:
  - Models with a `wrapper` field in their recipe (gpt-image-2, kling-v3,
    seedance-*, nano-banana-2) are ALWAYS generated through their existing
    script; `run` refuses them and prints the wrapper command instead, so
    there is never a second code path to the same model.
  - Wrapper-less recipes (audio, recraft, future Fal models) run here through
    FalAdapter (queue REST). Provider pluggability = PROVIDERS dispatch keyed
    off the recipe's `provider` field.

Money path for `run`: recipe pricing → est cost → per-run budget check →
`fal_budget_guard.py check --mode=generic --est-cost=…` → call → download →
asset + sidecar + manifest line → `fal_budget_guard.py log`. The PreToolUse
cost-gate hook fires independently on the invoking Bash command.

Recipes: skills/generate/models/<id>.json — see models/README.md for schema.

CLI:
  python3 execution/generate_media.py models [--json]
  python3 execution/generate_media.py quote --model <id> [--param k=v ...] [--n N] [--text "..."]
  python3 execution/generate_media.py run   --model <id> --prompt "..." [--ref <path> ...]
        [--project <slug>] [--slug <name>] [--variant <name>]
        [--run-id <id>] [--run-budget 3.00] [--param k=v ...] [--n N]
  python3 execution/generate_media.py index --file <path> --model <id> [--prompt "..."]
        [--cost N] [--project <slug>] [--style <s>] [--ref <path> ...]

Output: deliverables/generations/{slug}_{variant}_{model}_{ts}.{ext}
        (or _active/<project>/05-assets/generated/ when --project is given)
        + sidecar <asset>.json + manifest line (.agent/assets/manifest.jsonl)
        + asset_gallery.py --quick so the board stays current.
"""
from __future__ import annotations

import argparse
import base64
import glob
import json
import math
import mimetypes
import os
import re
import subprocess
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECIPES_DIR = os.path.join(ROOT, "skills", "generate", "models")
MANIFEST = os.path.join(ROOT, ".agent", "assets", "manifest.jsonl")
RUN_STATE = os.path.join(ROOT, ".agent", "generate-run-state.json")
FAL_QUEUE = "https://queue.fal.run"

MEDIA_EXTS = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".mov", ".webm",
              ".mp3", ".wav", ".m4a", ".svg", ".glb")


# ---------------------------------------------------------------- helpers

def fail(msg: str, code: int = 1):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def load_env_key(name: str) -> str | None:
    if os.environ.get(name):
        return os.environ[name]
    try:
        for line in open(os.path.join(ROOT, ".env"), encoding="utf-8"):
            line = line.strip()
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    except OSError:
        pass
    return None


def load_recipes() -> dict:
    recipes = {}
    for path in sorted(glob.glob(os.path.join(RECIPES_DIR, "*.json"))):
        try:
            r = json.load(open(path, encoding="utf-8"))
            if r.get("id"):
                recipes[r["id"]] = r
        except (OSError, ValueError) as e:
            print(f"WARN: bad recipe {os.path.basename(path)}: {e}", file=sys.stderr)
    return recipes


def get_recipe(model_id: str) -> dict:
    recipes = load_recipes()
    if model_id not in recipes:
        fail(f"unknown model '{model_id}'. Known: {', '.join(sorted(recipes)) or '(none — add recipes to skills/generate/models/)'}")
    return recipes[model_id]


def parse_params(pairs: list[str]) -> dict:
    out = {}
    for p in pairs or []:
        if "=" not in p:
            fail(f"--param needs k=v, got '{p}'")
        k, v = p.split("=", 1)
        if v.lower() in ("true", "false"):
            out[k] = v.lower() == "true"
        else:
            try:
                out[k] = int(v) if re.fullmatch(r"-?\d+", v) else float(v)
            except ValueError:
                out[k] = v
    return out


def estimate(recipe: dict, *, n: int = 1, params: dict | None = None,
             text: str | None = None) -> float:
    pr = recipe.get("pricing") or {}
    unit = pr.get("unit", "per_generation")
    table = pr.get("table") or {}
    price = table.get("default")
    # param-keyed price override (e.g. table keyed by resolution value)
    for v in (params or {}).values():
        if isinstance(v, str) and v in table:
            price = table[v]
    if price is None:
        fail(f"recipe {recipe['id']} has no pricing.table.default — refusing to guess")
    if unit == "per_image" or unit == "per_generation":
        return round(price * max(1, n), 4)
    if unit == "per_second":
        dur = (params or {}).get("duration") or (params or {}).get("duration_seconds")
        if not dur:
            fail(f"{recipe['id']} prices per_second — pass --param duration=N")
        return round(price * float(dur), 4)
    if unit == "per_1k_chars":
        if not text:
            fail(f"{recipe['id']} prices per_1k_chars — the prompt/text drives cost")
        return round(price * math.ceil(len(text) / 1000), 4)
    fail(f"unknown pricing unit '{unit}' in recipe {recipe['id']}")


def slugify(s: str, words: int = 5) -> str:
    toks = re.findall(r"[a-z0-9]+", (s or "asset").lower())[:words]
    return "-".join(toks) or "asset"


# ---------------------------------------------------------------- providers

class FalAdapter:
    """Minimal Fal queue client: submit → poll → download. Sync, stdlib-only."""

    def __init__(self):
        self.key = load_env_key("FAL_KEY")
        if not self.key:
            fail("FAL_KEY not found in environment or .env")

    def _req(self, url: str, payload: dict | None = None) -> dict:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode() if payload is not None else None,
            headers={"Authorization": f"Key {self.key}",
                     "Content-Type": "application/json"},
            method="POST" if payload is not None else "GET")
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())

    def generate(self, endpoint: str, payload: dict, timeout_s: int = 300) -> dict:
        sub = self._req(f"{FAL_QUEUE}/{endpoint}", payload)
        status_url = sub.get("status_url")
        response_url = sub.get("response_url")
        if not status_url or not response_url:
            fail(f"unexpected Fal submit response: {json.dumps(sub)[:300]}")
        deadline = time.time() + timeout_s
        while time.time() < deadline:
            st = self._req(status_url)
            s = st.get("status")
            if s == "COMPLETED":
                return self._req(response_url)
            if s in ("FAILED", "CANCELLED", "ERROR"):
                fail(f"Fal job {s}: {json.dumps(st)[:400]}")
            time.sleep(3)
        fail(f"Fal job timed out after {timeout_s}s (status_url: {status_url})")


PROVIDERS = {"fal": FalAdapter}


def find_media_urls(obj) -> list[str]:
    """Recursively collect media file URLs from a Fal response."""
    urls = []

    def walk(x):
        if isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
        elif isinstance(x, str) and x.startswith("http"):
            path = x.split("?")[0].lower()
            if path.endswith(MEDIA_EXTS):
                urls.append(x)
    walk(obj)
    # de-dupe preserving order
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def file_to_data_uri(path: str) -> str:
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    data = base64.b64encode(open(path, "rb").read()).decode("ascii")
    return f"data:{mime};base64,{data}"


# ---------------------------------------------------------------- run budget

def run_budget_check(run_id: str | None, budget: float | None, est: float) -> None:
    if not run_id:
        return
    state = {}
    try:
        state = json.load(open(RUN_STATE))
    except (OSError, ValueError):
        pass
    rec = state.get(run_id)
    if rec is None:
        if budget is None:
            fail(f"run '{run_id}' unknown — pass --run-budget on its first call")
        rec = {"budget_usd": budget, "spent_usd": 0.0, "started": now_iso()}
        state[run_id] = rec
        os.makedirs(os.path.dirname(RUN_STATE), exist_ok=True)
        json.dump(state, open(RUN_STATE, "w"), indent=2)
    remaining = rec["budget_usd"] - rec["spent_usd"]
    if est > remaining:
        fail(f"run budget exceeded: est ${est:.4f} > remaining ${remaining:.4f} "
             f"(budget ${rec['budget_usd']:.2f}, spent ${rec['spent_usd']:.4f}). "
             f"This ceiling came from the prompt — ask Farrice before raising it.")


def run_budget_add(run_id: str | None, actual: float) -> float | None:
    if not run_id:
        return None
    try:
        state = json.load(open(RUN_STATE))
    except (OSError, ValueError):
        return None
    rec = state.get(run_id)
    if not rec:
        return None
    rec["spent_usd"] = round(rec["spent_usd"] + actual, 4)
    json.dump(state, open(RUN_STATE, "w"), indent=2)
    return rec["budget_usd"] - rec["spent_usd"]


# ---------------------------------------------------------------- manifest

def zone_for(rel_path: str) -> tuple[str, str | None]:
    if rel_path.startswith("deliverables/generations"):
        parts = rel_path.split("/")
        proj = parts[2] if len(parts) > 3 else None
        return "deliverables-generations", proj
    if rel_path.startswith("_active/"):
        parts = rel_path.split("/")
        idxs = [i for i, p in enumerate(parts) if p == "_active"]
        proj = parts[idxs[-1] + 1] if idxs and idxs[-1] + 1 < len(parts) else None
        return "active-projects", proj
    for zone, prefix in (("fantastic-posters", "skills/fantastic-posters/out"),
                         ("deliverables-images", "deliverables/images"),
                         ("deliverables-designs", "deliverables/designs"),
                         ("deliverables-carousel", "deliverables/carousel-images"),
                         ("deliverables-video", "deliverables/video-enhancement")):
        if rel_path.startswith(prefix):
            return zone, None
    return "deliverables-generations", None


TYPE_BY_EXT = {"png": "image", "jpg": "image", "jpeg": "image", "webp": "image",
               "gif": "image", "svg": "image", "mp4": "video", "mov": "video",
               "webm": "video", "mp3": "audio", "wav": "audio", "m4a": "audio",
               "glb": "doc", "pdf": "doc"}


def manifest_append(abs_path: str, *, model: str, provider: str | None,
                    prompt: str | None, refs: list[str], cost: float | None,
                    style: str | None, run_id: str | None, variant: str | None,
                    project_flag: str | None) -> None:
    rel = os.path.relpath(abs_path, ROOT)
    zone, proj = zone_for(rel)
    ext = rel.rsplit(".", 1)[-1].lower()
    try:
        st = os.stat(abs_path)
        mtime, size = int(st.st_mtime), st.st_size
    except OSError:
        mtime = size = None
    rec = {"v": 1, "path": rel, "type": TYPE_BY_EXT.get(ext, "doc"), "ext": ext,
           "zone": zone, "project": project_flag or proj, "src": provider,
           "model": model, "style": style, "prompt": prompt, "refs": refs,
           "cost_usd": cost, "ts": now_iso(), "mtime": mtime, "size": size,
           "w": None, "h": None, "dur_s": None, "tags": [], "keep": None,
           "status": "active"}
    if run_id:
        rec["run_id"] = run_id
    if variant:
        rec["variant"] = variant
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    with open(MANIFEST, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def gallery_quick() -> None:
    try:
        subprocess.run(["python3", os.path.join(ROOT, "execution", "asset_gallery.py"),
                        "--quick"], capture_output=True, timeout=120)
    except Exception:
        pass  # board refresh is a nudge, never a failure


# ---------------------------------------------------------------- commands

def cmd_models(args) -> int:
    recipes = load_recipes()
    if args.json:
        print(json.dumps(list(recipes.values()), indent=2))
        return 0
    if not recipes:
        print(f"no recipes found in {os.path.relpath(RECIPES_DIR, ROOT)}")
        return 0
    print(f"{'id':<18} {'type':<7} {'provider':<9} {'pricing':<26} {'route'}")
    for r in recipes.values():
        pr = r.get("pricing") or {}
        price = (pr.get("table") or {}).get("default")
        punit = f"${price} {pr.get('unit', '?')}" if price is not None else "?"
        if r.get("guard", {}).get("hard_blocked"):
            route = "HARD-BLOCKED"
        elif r.get("status") == "deferred":
            route = "deferred (no pricing verified)"
        elif r.get("wrapper"):
            route = f"wrapper: {r['wrapper']}"
        else:
            route = "generate_media.py run"
        print(f"{r['id']:<18} {r.get('media_type','?'):<7} {r.get('provider','?'):<9} {punit:<26} {route}")
    return 0


def cmd_quote(args) -> int:
    recipe = get_recipe(args.model)
    if recipe.get("guard", {}).get("hard_blocked"):
        print(f"{args.model}: HARD-BLOCKED — no quote, no run. {recipe.get('notes', '')}")
        return 1
    params = parse_params(args.param)
    est = estimate(recipe, n=args.n, params=params, text=args.text or args.prompt)
    print(f"QUOTE {args.model}: est ${est:.4f} "
          f"(n={args.n}, unit={recipe.get('pricing', {}).get('unit')})")
    if recipe.get("quote_required"):
        print("This model requires an explicit go from Farrice before running (paid video rule).")
    if recipe.get("wrapper"):
        print(f"Route: existing wrapper → {recipe['wrapper']}")
    return 0


def cmd_run(args) -> int:
    recipe = get_recipe(args.model)
    if recipe.get("guard", {}).get("hard_blocked"):
        fail(f"{args.model} is hard-blocked ({recipe.get('notes', 'no override path')})")
    if recipe.get("status") == "deferred":
        fail(f"{args.model} is a deferred stub — verify endpoint+pricing on fal.ai/models, "
             f"fill the recipe, and remove \"status\": \"deferred\" first")
    if recipe.get("wrapper"):
        print(f"{args.model} is wrapper-backed. One code path per model — run it via:")
        print(f"  {recipe['wrapper']}")
        print("Then index the result:")
        print(f"  python3 execution/generate_media.py index --file <output> --model {args.model} "
              f"--prompt \"...\" [--cost N]")
        return 2
    provider_name = recipe.get("provider", "fal")
    if provider_name not in PROVIDERS:
        fail(f"no adapter for provider '{provider_name}'")
    if not args.prompt:
        fail("run requires --prompt")

    params = dict(recipe.get("defaults") or {})
    params.update(parse_params(args.param))
    prompt_key = recipe.get("prompt_param", "prompt")
    params[prompt_key] = args.prompt
    refs = args.ref or []
    if refs:
        ref_param = recipe.get("ref_param")
        if not ref_param:
            fail(f"{args.model} recipe has no ref_param — it does not accept reference files")
        uris = [file_to_data_uri(p) if os.path.isfile(p) else p for p in refs]
        params[ref_param] = uris if recipe.get("ref_list", True) else uris[0]

    est = estimate(recipe, n=args.n, params=params, text=args.prompt)
    if args.n > 1 and "num_images" in (recipe.get("defaults") or {}):
        params["num_images"] = args.n

    # 1. per-run budget (prompt-level ceiling)
    run_budget_check(args.run_id, args.run_budget, est)
    # 2. fal budget guard (wallet-level ceilings; PreToolUse hook fired already)
    guard = subprocess.run(
        ["python3", os.path.join(ROOT, "execution", "fal_budget_guard.py"), "check",
         "--mode=generic", f"--est-cost={est}", f"--model={args.model}",
         f"--brief={(args.prompt or '')[:120]}"])
    if guard.returncode != 0:
        return guard.returncode

    print(f"→ {recipe['endpoint']} (est ${est:.4f})")
    adapter = PROVIDERS[provider_name]()
    t0 = time.time()
    result = adapter.generate(recipe["endpoint"], params,
                              timeout_s=int(recipe.get("timeout_s", 300)))
    urls = find_media_urls(result)
    if not urls:
        print(json.dumps(result, indent=2)[:1500], file=sys.stderr)
        fail("Fal job completed but no media URLs found in response (see above)")

    # destination
    if args.project:
        out_dir = os.path.join(ROOT, "_active", args.project, "05-assets", "generated")
    else:
        out_dir = os.path.join(ROOT, "deliverables", "generations")
    os.makedirs(out_dir, exist_ok=True)
    slug = args.slug or slugify(args.prompt)
    ts = time.strftime("%Y%m%d-%H%M%S")
    saved = []
    for i, u in enumerate(urls):
        ext = u.split("?")[0].rsplit(".", 1)[-1].lower()
        vpart = f"_{args.variant}" if args.variant else (f"_v{i+1}" if len(urls) > 1 else "")
        name = f"{slug}{vpart}_{args.model}_{ts}.{ext}"
        dest = os.path.join(out_dir, name)
        urllib.request.urlretrieve(u, dest)
        saved.append(dest)

    per_asset_cost = round(est / len(saved), 4)
    for dest in saved:
        sidecar = {"model": args.model, "provider": provider_name,
                   "endpoint": recipe["endpoint"], "prompt": args.prompt,
                   "params": {k: v for k, v in params.items()
                              if not (isinstance(v, str) and v.startswith("data:"))},
                   "refs": refs, "est_cost_usd": per_asset_cost, "ts": now_iso(),
                   "run_id": args.run_id, "elapsed_s": round(time.time() - t0, 1)}
        open(dest + ".json", "w", encoding="utf-8").write(
            json.dumps(sidecar, ensure_ascii=False, indent=2))
        manifest_append(dest, model=args.model, provider=provider_name,
                        prompt=args.prompt, refs=refs, cost=per_asset_cost,
                        style=args.style, run_id=args.run_id, variant=args.variant,
                        project_flag=args.project)

    subprocess.run(
        ["python3", os.path.join(ROOT, "execution", "fal_budget_guard.py"), "log",
         "--mode=generic", f"--est-cost={est}", f"--model={args.model}",
         "--status=success", f"--actual-cost={est}",
         f"--output-path={os.path.relpath(saved[0], ROOT)}",
         f"--brief={(args.prompt or '')[:120]}"],
        capture_output=True)
    remaining = run_budget_add(args.run_id, est)
    gallery_quick()

    for dest in saved:
        print(f"✓ {os.path.relpath(dest, ROOT)}")
    print(f"cost ${est:.4f}" + (f" · run '{args.run_id}' remaining ${remaining:.4f}"
                                if remaining is not None else ""))
    return 0


def cmd_index(args) -> int:
    abs_path = args.file if os.path.isabs(args.file) else os.path.join(ROOT, args.file)
    if not os.path.isfile(abs_path):
        fail(f"file not found: {args.file}")
    recipes = load_recipes()
    provider = (recipes.get(args.model) or {}).get("provider")
    manifest_append(abs_path, model=args.model, provider=provider,
                    prompt=args.prompt, refs=args.ref or [], cost=args.cost,
                    style=args.style, run_id=args.run_id, variant=args.variant,
                    project_flag=args.project)
    gallery_quick()
    print(f"indexed: {os.path.relpath(abs_path, ROOT)} (model={args.model})")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Recipe-driven media generation engine (/generate)")
    sub = p.add_subparsers(dest="cmd", required=True)

    pm = sub.add_parser("models", help="List model recipes")
    pm.add_argument("--json", action="store_true")

    def common(px, need_model=True):
        if need_model:
            px.add_argument("--model", required=True)
        px.add_argument("--prompt", default=None)
        px.add_argument("--param", action="append", default=[], help="k=v recipe param override")
        px.add_argument("--n", type=int, default=1)
        px.add_argument("--ref", action="append", default=[], help="reference file path (repeatable)")
        px.add_argument("--project", default=None, help="route output to _active/<slug>/05-assets/generated/")
        px.add_argument("--slug", default=None)
        px.add_argument("--variant", default=None)
        px.add_argument("--style", default=None)
        px.add_argument("--run-id", default=None, dest="run_id")
        px.add_argument("--run-budget", type=float, default=None, dest="run_budget")

    pq = sub.add_parser("quote", help="Estimate cost — never spends")
    common(pq)
    pq.add_argument("--text", default=None, help="for per_1k_chars pricing")

    pr = sub.add_parser("run", help="Generate via a wrapper-less recipe")
    common(pr)

    pi = sub.add_parser("index", help="Manifest line for an asset made by an existing wrapper")
    common(pi)
    pi.add_argument("--file", required=True)
    pi.add_argument("--cost", type=float, default=None)

    args = p.parse_args()
    return {"models": cmd_models, "quote": cmd_quote,
            "run": cmd_run, "index": cmd_index}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
