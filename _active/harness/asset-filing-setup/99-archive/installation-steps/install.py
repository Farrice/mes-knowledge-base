"""Install the reviewed asset-filing package with narrow permissions and backups."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import tomllib
from datetime import datetime, timezone

PACKAGE=Path(__file__).resolve().parent.parent
WORK=Path('/Users/farricecain/Work')
SUPPORT=WORK/'50 Reference'/'Asset Filing'
CONFIG=Path('/Users/farricecain/.codex/config.toml')
GLOBAL=Path('/Users/farricecain/.codex/AGENTS.md')
STAMP=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
BACKUP=Path('/Users/farricecain/.codex/backups')/('asset-filing-'+STAMP)
roots=[str(WORK/name) for name in ('20 Clients','30 Business','40 Creative')]+[str(SUPPORT)]
old_config=CONFIG.read_text()
parsed=tomllib.loads(old_config)
assert parsed.get('sandbox_mode')=='workspace-write', 'Review changed sandbox config before installation.'
assert 'default_permissions' not in parsed, 'Permission profiles need a separate reviewed patch.'
assert 'sandbox_workspace_write' not in parsed, 'Merge existing writable-root table explicitly rather than replacing it.'
config_new=old_config.rstrip()+'\n\n# Asset filing: keep personal Downloads unchanged; allow only project/support folders.\n[sandbox_workspace_write]\nwritable_roots = '+json.dumps(roots)+'\n'
new_parsed=tomllib.loads(config_new)
new_without=dict(new_parsed)
new_without.pop('sandbox_workspace_write')
assert new_without==parsed
old_global=GLOBAL.read_text()
marker='<!-- BEGIN:asset-filing-default -->'
assert marker not in old_global, 'Already installed; inspect existing block before updating.'
block='''
<!-- BEGIN:asset-filing-default -->
## Task Asset Filing

When an authorized task downloads, creates, uploads, files, or reuses project assets, read `/Users/farricecain/Work/ASSET-FILING.md` and apply its task-time filing and retrieval steps. Keep Chrome's default destination as Downloads. File only assets whose ownership is established for the current task; preserve unrelated and original downloads. Reuse established project homes and artifact-router/worktree rules. Use descriptive versioned names, provenance, and a readable asset index. Verify the intended asset before reuse and the receiving tool after upload. This authorizes no background sweep, broader upload destination, publication, spending, deletion, or security bypass. The guide and helper add no new approval policy.
<!-- END:asset-filing-default -->
'''
global_new=old_global.rstrip()+'\n'+block
start=WORK/'START-HERE.md'
old_start=start.read_text()
start_marker='## Asset Filing During Tasks'
assert start_marker not in old_start
start_new=old_start.rstrip()+'''\n\n## Asset Filing During Tasks

Read [Find and File Assets](ASSET-FILING.md) for automatic task-time filing, version names, and retrieval. Personal downloads continue going to Downloads. Codex files only the current task's identified assets and preserves existing project homes. Setup proof and examples live in `50 Reference/Asset Filing`.
'''
# Check destination files before any mutation.
assert not (WORK/'ASSET-FILING.md').exists()
assert not SUPPORT.exists()
for p in (WORK,CONFIG,GLOBAL,start):
    assert not p.is_symlink(), f'Review linked installation target: {p}'
BACKUP.mkdir(parents=True, mode=0o700)
for src,name in ((CONFIG,'config.toml'),(GLOBAL,'AGENTS.md'),(start,'START-HERE.md')):
    dest=BACKUP/name
    shutil.copy2(src,dest)
    dest.chmod(0o600)
SUPPORT.mkdir(parents=True)
for folder in roots[:3]:
    Path(folder).mkdir(exist_ok=True)
shutil.copy2(PACKAGE/'06-system'/'asset_filing.py',SUPPORT/'asset_filing.py')
shutil.copy2(PACKAGE/'ASSET-FILING.md',WORK/'ASSET-FILING.md')
# Reject concurrent changes rather than overwriting them.
assert CONFIG.read_text()==old_config and GLOBAL.read_text()==old_global and start.read_text()==old_start
for path,content in ((CONFIG,config_new),(GLOBAL,global_new),(start,start_new)):
    temp=path.with_name(path.name+'.asset-filing-pending')
    with temp.open('x') as out:
        out.write(content)
    temp.chmod(path.stat().st_mode & 0o777)
    temp.replace(path)
assert tomllib.loads(CONFIG.read_text())==new_parsed
assert GLOBAL.read_text()==global_new
assert hashlib.sha256((SUPPORT/'asset_filing.py').read_bytes()).hexdigest()==hashlib.sha256((PACKAGE/'06-system'/'asset_filing.py').read_bytes()).hexdigest()
receipt={'installed_at':STAMP,'guide':str(WORK/'ASSET-FILING.md'),'helper':str(SUPPORT/'asset_filing.py'),'writable_roots':roots,'backups':str(BACKUP),'config_parsed':True,'other_config_unchanged':True,'global_instruction_installed':True,'current_task_permissions_reloaded':False,'browser_setting':'User reports ask-before-saving off; Downloads destination unchanged','browser_transfer_test':'NOT_RUN','background_watcher':False}
(SUPPORT/'installation.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
