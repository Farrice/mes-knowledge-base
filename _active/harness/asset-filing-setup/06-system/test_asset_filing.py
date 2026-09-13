import importlib.util
import json
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location('filing', Path(__file__).with_name('asset_filing.py'))
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
checks = []
def ok(name, condition):
    assert condition, name
    checks.append(name)
with tempfile.TemporaryDirectory() as d:
    f.WORK = Path(d) / 'Work'
    home = f.init('client', 'Example Client - Property Video')
    source = Path(d) / 'download.txt'
    source.write_text('Synthetic asset, version one.\n')
    one = f.file_asset(source, home, 'exterior-camera-rise')
    ok('copy preserves original and bytes', source.exists() and f.digest(Path(one['path'])) == f.digest(source))
    again = f.file_asset(source, home, 'exterior-camera-rise')
    ok('repeat import is idempotent', again['result'] == 'already-filed' and len(f.records(home)) == 1)
    source.write_text('Synthetic asset, version two.\n')
    two = f.file_asset(source, home, 'exterior-camera-rise')
    ok('revision retains v01 and writes v02', '-v02-review.txt' in two['path'] and Path(one['path']).read_text().endswith('one.\n'))
    try:
        f.file_asset(source, home, 'exterior-camera-rise', 'approved')
        raise AssertionError('approval note required')
    except ValueError:
        checks.append('approval note required')
    approved = f.file_asset(source, home, 'exterior-camera-rise', 'approved', approval_note='Synthetic test approval only')
    found = f.find_assets('exterior-camera-rise', 'approved', True)
    ok('retrieval finds and verifies approved version', len(found) == 1 and found[0]['file_state'] == 'verified')
    Path(approved['path']).write_text('Changed outside filing helper')
    ok('retrieval flags changed bytes', f.find_assets('exterior-camera-rise', 'approved', True)[0]['file_state'] == 'changed')
    partial = Path(d) / 'video.crdownload'
    partial.write_text('unfinished')
    try:
        f.file_asset(partial, home, 'partial')
        raise AssertionError('partial download refused')
    except ValueError:
        checks.append('partial download refused')
    other = Path(d) / 'outside'
    other.mkdir()
    (home / '90-exports').symlink_to(other, target_is_directory=True)
    try:
        f.file_asset(source, home, 'linked', 'export')
        raise AssertionError('linked destination refused')
    except ValueError:
        checks.append('linked destination refused')
    ok('readable index and provenance exist', (home / 'ASSET-INDEX.md').is_file() and f.records(home)[0]['original_name'] == 'download.txt')
print(json.dumps({'passed': len(checks), 'checks': checks}, indent=2))
