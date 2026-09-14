from pathlib import Path
import sys
import tempfile
sys.path.insert(0,str(Path(__file__).resolve().parents[4]/'execution'))
import front_door as front
import artifact_router as router
checks=[]
with tempfile.TemporaryDirectory() as directory:
    root=Path(directory)
    base=root/'_active'/'example'
    base.mkdir(parents=True)
    front.ROOT=root
    front.git_dates=lambda p:{}
    (base/'current-guide.md').write_text('# Working candidate\n')
    (base/'parked-offer.md').write_text('---\nstatus: parked\n---\n# Old offer\n')
    (base/'old-guide.md').write_text('# Old guide\n')
    (base/'old-guide.md.metadata.json').write_text('{"status":"superseded"}')
    (base/'2026-09-12-retired-record.md').write_text('---\nstatus: retired\n---\n# Retired\n')
    (base/'99-archive').mkdir()
    archived=base/'99-archive'/'old.md'
    archived.write_text('# Old\n')
    (base/'bad-metadata.md').write_text('# Unresolved\n')
    (base/'bad-metadata.md.metadata.json').write_text('[]')
    scanned=front.scan(base)
    assert [p['name'] for p in scanned['living']]==['current-guide.md']
    checks.append('parked frontmatter and superseded sidecar excluded')
    assert not scanned['records']
    checks.append('retired dated records excluded')
    assert any('unreadable lifecycle metadata' in warning for warning in scanned['drift'])
    checks.append('invalid lifecycle metadata excluded pending review')
    rendered=front.render_md(scanned,None)
    assert '## Live now' not in rendered and 'do not establish authority' in rendered
    checks.append('index does not declare name/date authority')
    assert router.infer_lifecycle(archived)[0]=='archive'
    checks.append('native artifact router recognizes 99-archive')
    router.ROOT=root/'.tmp'/'codex-worktrees'/'sample'
    assert not router.should_skip(router.ROOT/'_active'/'example'/'current.md')
    assert router.should_skip(router.ROOT/'.tmp'/'scratch.md')
    checks.append('lane ancestor does not hide project inventory; local scratch still excluded')
print({'passed':len(checks),'checks':checks})
