"""Install local filing artifacts only. No Codex configuration or instruction edits."""
from pathlib import Path
import hashlib
import json
import shutil
PACKAGE=Path(__file__).resolve().parent.parent
WORK=Path('/Users/farricecain/Work')
SUPPORT=WORK/'50 Reference'/'Asset Filing'
assert not SUPPORT.exists() and not (WORK/'ASSET-FILING.md').exists()
assert not WORK.is_symlink() and not (WORK/'50 Reference').is_symlink()
start=WORK/'START-HERE.md'
old=start.read_text()
assert '## Asset Filing During Tasks' not in old
SUPPORT.mkdir(parents=True)
shutil.copy2(start,SUPPORT/'START-HERE.before-asset-filing.md')
shutil.copy2(PACKAGE/'ASSET-FILING.md',WORK/'ASSET-FILING.md')
shutil.copy2(PACKAGE/'06-system'/'asset_filing.py',SUPPORT/'asset_filing.py')
assert start.read_text()==old
start.write_text(old.rstrip()+'''\n\n## Asset Filing During Tasks

Read [Find and File Assets](ASSET-FILING.md) for naming, project filing, and retrieval. Personal downloads continue going to Downloads. The helper and synthetic proof are in `50 Reference/Asset Filing`. Global Codex activation and additional folder permissions are pending explicit approval; see SETUP-RECEIPT.md there.
''')
assert hashlib.sha256((SUPPORT/'asset_filing.py').read_bytes()).hexdigest()==hashlib.sha256((PACKAGE/'06-system'/'asset_filing.py').read_bytes()).hexdigest()
print(json.dumps({'guide':str(WORK/'ASSET-FILING.md'),'helper':str(SUPPORT/'asset_filing.py'),'start_here_link':'installed','global_config_changed':False,'global_instructions_changed':False}))
