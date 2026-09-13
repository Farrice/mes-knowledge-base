import json
from pathlib import Path
import tempfile
import asset_filing as f
import document_history as h
checks=[]
def ok(name,value):
    assert value,name
    checks.append(name)
def refuses(name,fn):
    try:
        fn()
    except ValueError:
        checks.append(name)
        return
    raise AssertionError(name)
with tempfile.TemporaryDirectory() as d:
    f.WORK=Path(d).resolve()/'Work'
    home=f.init('business','Offer Example')
    original=Path(d)/'offer.md'
    original.write_text('# Retired pilot\nThe old offer costs 300.\n')
    first=f.file_asset(original,home,'offer',status='review')
    one=str(Path(first['path']).relative_to(home))
    h.transition(home,'offer','Synthetic approved baseline',0,path=one)
    old_bytes=Path(first['path']).read_bytes()
    original.write_text('# Current offer\nThe approved offer costs 750.\n')
    second=f.file_asset(original,home,'offer',status='review')
    two=str(Path(second['path']).relative_to(home))
    state=h.transition(home,'offer','Synthetic explicit replacement',1,path=two)
    ok('single current anchor',state['documents']['offer']['current']['path']==two)
    ok('stable entry follows promoted version',(home/'00-start-here'/'offer.md').resolve()==(home/two).resolve())
    archive=home/state['documents']['offer']['history'][0]['path']
    ok('old version archived byte-for-byte',archive.read_bytes()==old_bytes)
    ok('old link contains redirect not obsolete terms','300' not in (home/one).read_text() and 'SUPERSEDED' in (home/one).read_text())
    ok('sidecar names successor',json.loads(Path(str(home/one)+'.metadata.json').read_text())['superseded_by']==two)
    ok('normal search excludes superseded version',len(f.find_assets('offer',verify=True))==1)
    ok('explicit historical search finds both',len(f.find_assets('offer',verify=True,include_history=True))==2)
    refuses('parallel stale revision cannot overwrite current',lambda:h.transition(home,'offer','Old task',1,path=one))
    ok('current lookup verifies bytes',h.current(home)['documents']['offer']['verification']=='verified')
    h.transition(home,'offer','Synthetic user parks this direction',2,retire='parked')
    ok('parked stable entry cannot resurrect old copy','No current document' in (home/'00-start-here'/'offer.md').read_text())
    ok('parked offer has no fallback anchor',h.current(home)['documents']['offer']['current'] is None and not f.find_assets('offer'))
    ok('history remains recoverable',len(h.current(home,True)['documents']['offer']['history'])==2)
    refuses('historical redirect cannot be promoted',lambda:h.transition(home,'offer','Accidental restart',3,path=two))
    other=f.init('business','Existing Canon')
    (other/'CANON.md').write_text('# Human-owned authority\n')
    refuses('existing human canon is preserved',lambda:h.current(other))
    # Interrupted transitions must not return a plausible current anchor.
    h.pending_path(home).write_text('{}')
    refuses('interrupted transition blocks anchor use',lambda:h.current(home))
print(json.dumps({'passed':len(checks),'checks':checks},indent=2))
