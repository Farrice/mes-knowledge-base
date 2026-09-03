"""Scrapes Skill Systems routing + BRAND LOCK — sabotage tests both directions.

Pins (2026-09-02):
  - a carousel/ebook/shorts ask surfaces the Scrapes front door; a Parallax
    edition, a plain LinkedIn text post, and a README typo do NOT
  - the router index carries the vendored skills (find_skill)
  - BRAND LOCK: one named brand resolves; nobody or two brands → ambiguous;
    a client alias is never overridden by the owner default; cwd under a
    client root resolves that client; readiness fails without tokens/pool and
    passes with them; a client path declared under another brand's root is a
    cross-brand leak
"""
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import find_skill  # noqa: E402
import routing_enforcer as renf  # noqa: E402
import scrapes_brand as sb  # noqa: E402

SCRAPES_DOORS = {"social-carousel", "social-post", "social-repurpose",
                 "deck-build", "video-to-shorts", "video-to-ebook", "scrapes"}


def test_umbrella_door_routes_and_ignores_web_scraping():
    assert "scrapes" in doors("set up my templates for my brand")
    assert "scrapes" in doors("run this through scrapes: a supplement teardown")
    assert "scrapes" not in doors("scrape linkedin posts from this profile")
    assert (ROOT / ".agent" / "workflows" / "scrapes.md").exists()
    assert (ROOT / "_active" / "harness" / "scrapes-skill-systems" / "USER-GUIDE.md").exists()


def doors(prompt):
    return {h["workflow"] for h in renf.match_bindings(prompt)}


@pytest.mark.parametrize("prompt,want", [
    ("make Jen a carousel about still renting in the valley", "social-carousel"),
    ("linkedin carousel on creatine timing for my brand", "social-carousel"),
    ("turn this youtube video into an ebook", "video-to-ebook"),
    ("cut this into clips, youtube to shorts", "video-to-shorts"),
    ("repurpose this edition for threads and instagram", "social-repurpose"),
    ("create a presentation about the sprint offer", "deck-build"),
])
def test_scrapes_asks_route_to_front_doors(prompt, want):
    assert want in doors(prompt)


@pytest.mark.parametrize("prompt", [
    "write my Parallax edition on identity and suppression",
    "write a linkedin post from scratch about pricing",
    "fix the typo in README",
    "what's the status of the gigi engine run",
])
def test_non_scrapes_asks_do_not_route_to_scrapes(prompt):
    assert not (doors(prompt) & SCRAPES_DOORS), doors(prompt)


def test_parallax_carousel_mention_is_not_a_scrapes_carousel():
    # negative signal: the Parallax edition owns its own visuals
    assert "social-carousel" not in doors("carousel of quotes for the parallax substack edition")


def test_bindings_and_directive_table_updated_together():
    md = (ROOT / "directives" / "routing-bindings.md").read_text()
    ids = {b["id"] for b in renf.BINDINGS}
    for door in SCRAPES_DOORS:
        assert any(b.get("mandatory_workflow") == door for b in renf.BINDINGS), door
        assert f"`/{door}`" in md, f"{door} missing from routing-bindings.md"
    assert "scrapes_social_carousel" in ids


def test_router_index_carries_vendor_skills():
    idx = find_skill.build_index()
    vendor = {s["directory"]: s for s in idx if s.get("vendor") == "scrapes"}
    assert "00-social-content" in vendor
    assert vendor["00-social-content"]["slash"] == "/00-social-content"
    top = [s["directory"] for s, _ in find_skill.rank(idx, "run social content generate post carousel images", top=3)]
    assert top[0] == "00-social-content"


def test_front_door_workflows_exist_and_are_thin_wrappers():
    for door in SCRAPES_DOORS:
        wf = ROOT / ".agent" / "workflows" / f"{door}.md"
        text = wf.read_text()
        assert text.startswith("---\ndescription:"), door
        assert "BRAND LOCK" in text, door
        assert ".claude/skills/" in text, f"{door} does not name its Scrapes machinery"
        assert "Never" in text


# ── BRAND LOCK ─────────────────────────────────────────────────────────

OWNER = """
brand: owner
display: Owner Brand
kind: owner
aliases: [owner, my brand, for me]
brand_context: {root}/owner-root/brand_context
output_base: {root}/owner-root/out
template_pools:
  linkedin-carousel: {root}/owner-root/brand_context/templates/linkedin-carousel
voice: {{dial: BLEND}}
pens: {{hook: luke, integrator: owner-pen, veto: owner}}
"""

CLIENT = """
brand: cli
display: Client One
kind: client
aliases: [cli, client one]
client_root: {root}/clients/cli
brand_context: {root}/clients/cli/brand_context
output_base: {out}
template_pools:
  linkedin-carousel: {root}/clients/cli/brand_context/templates/linkedin-carousel
renderer_fallback: {fallback}
voice: {{dial: "OFF"}}
pens: {{hook: alyssa+luke, integrator: cli-pen, veto: cli}}
"""


@pytest.fixture
def brands(tmp_path, monkeypatch):
    def make(client_out=None, fallback="null"):
        root = tmp_path
        for rel, text in (
            ("owner-root/brand_context/BRAND.yaml", OWNER.format(root=root)),
            ("clients/cli/brand_context/BRAND.yaml",
             CLIENT.format(root=root, out=client_out or f"{root}/clients/cli/out", fallback=fallback)),
        ):
            p = root / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text)
        monkeypatch.setattr(sb, "SEARCH_ROOTS", (root,))
        monkeypatch.setattr(sb, "ROOT", root)
        return sb.load_brands()
    return make


def test_lock_resolves_exactly_one_named_brand(brands):
    b = brands()
    got, status = sb.resolve(b, prompt="make cli a carousel about renting")
    assert status == "ok" and got["brand"] == "cli"
    got, status = sb.resolve(b, prompt="carousel for my brand about creatine")
    assert status == "ok" and got["brand"] == "owner"


def test_lock_refuses_to_guess(brands):
    b = brands()
    assert sb.resolve(b, prompt="make a carousel about creatine")[1] == "ambiguous"
    assert sb.resolve(b, prompt="carousel for cli and for me")[1] == "ambiguous"
    assert sb.resolve(b, brand="nobody")[1] == "unknown"


def test_client_alias_beats_owner_cwd(brands, tmp_path):
    b = brands()
    got, status = sb.resolve(b, prompt="client one carousel", cwd=str(tmp_path / "owner-root"))
    assert status == "ok" and got["brand"] == "cli"


def test_cwd_under_client_root_resolves_client_when_nobody_named(brands, tmp_path):
    b = brands()
    got, status = sb.resolve(b, prompt="carousel about creatine", cwd=str(tmp_path / "clients" / "cli" / "x"))
    assert status == "ok" and got["brand"] == "cli"


def test_check_not_ready_without_tokens_or_pool(brands):
    b = brands()
    rep = sb.check(b, b["cli"], "linkedin-carousel")
    assert rep["ready"] is False
    failed = {c["check"] for c in rep["checks"] if not c["ok"]}
    assert "tokens.json" in failed and "template pool linkedin-carousel" in failed
    assert rep["render_path"] == "blocked"


def test_check_ready_with_tokens_pool_and_voice(brands, tmp_path):
    b = brands()
    bc = tmp_path / "clients" / "cli" / "brand_context"
    (bc / "visual-identity").mkdir(parents=True)
    (bc / "visual-identity" / "tokens.json").write_text("{}")
    (bc / "voice-profile.md").write_text("# voice\n")
    pool = bc / "templates" / "linkedin-carousel"
    pool.mkdir(parents=True)
    (pool / "manifest.json").write_text(json.dumps({"templates": [{"id": "cover", "status": "ready"}]}))
    rep = sb.check(b, b["cli"], "linkedin-carousel")
    assert rep["ready"] is True and rep["render_path"] == "scrapes-template-pool"
    # Farrice's Approve flips ready -> approved; the pool must still count as usable
    (pool / "manifest.json").write_text(json.dumps({"templates": [{"id": "cover", "status": "approved"}]}))
    rep = sb.check(b, b["cli"], "linkedin-carousel")
    assert rep["ready"] is True and rep["render_path"] == "scrapes-template-pool"


def test_check_uses_brand_renderer_when_pool_missing(brands, tmp_path):
    b = brands(fallback=f"{tmp_path}/clients/cli/render.py")
    bc = tmp_path / "clients" / "cli" / "brand_context"
    (bc / "visual-identity").mkdir(parents=True)
    (bc / "visual-identity" / "tokens.json").write_text("{}")
    (bc / "voice-profile.md").write_text("# voice\n")
    rep = sb.check(b, b["cli"], "linkedin-carousel")
    assert rep["render_path"] == "brand-renderer"


def test_cross_brand_leak_is_caught(brands, tmp_path):
    # client output declared under the OWNER's root → isolation check fails
    b = brands(client_out=f"{tmp_path}/owner-root/out/cli")
    rep = sb.check(b, b["cli"], None)
    leak = next(c for c in rep["checks"] if c["check"] == "cross-brand isolation")
    assert leak["ok"] is False and "output_base" in leak["detail"]


def test_real_registry_has_farrice_and_jen_isolated():
    b = sb.load_brands()
    assert {"farrice", "jen"} <= set(b)
    for name in ("farrice", "jen"):
        rep = sb.check(b, b[name], None)
        iso = next(c for c in rep["checks"] if c["check"] == "cross-brand isolation")
        assert iso["ok"], iso["detail"]
    assert sb.resolve(b, prompt="make Jen a carousel about still renting")[0]["brand"] == "jen"
    assert sb.resolve(b, prompt="make a carousel about creatine")[1] == "ambiguous"
