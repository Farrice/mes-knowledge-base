"""Represent the user-approved four roots in the current Codex permission schema."""
from pathlib import Path
from datetime import datetime, timezone
import json
import re
import shutil
import tomllib
config=Path('/Users/farricecain/.codex/config.toml')
roots=[str(Path('/Users/farricecain/Work')/p) for p in ('20 Clients','30 Business','40 Creative','50 Reference/Asset Filing')]
old=config.read_text()
before=tomllib.loads(old)
assert before.get('sandbox_mode')=='workspace-write'
assert before.get('sandbox_workspace_write')=={'writable_roots':roots}
assert 'default_permissions' not in before and 'permissions' not in before
new,count=re.subn(r'^sandbox_mode\s*=\s*"workspace-write"\s*$', 'default_permissions = "asset-filing"',old,count=1,flags=re.M)
assert count==1
new,count=re.subn(r'(?ms)^# Approved asset-filing project/support folders; Downloads is unchanged\.\n\[sandbox_workspace_write\]\nwritable_roots = .*?$(?=\n\[|\Z)', '',new,count=1)
assert count==1
new=new.rstrip()+'\n\n# User-approved task filing scope; inherited workspace protection remains.\n[permissions.asset-filing]\ndescription = "Workspace plus approved task filing folders"\nextends = ":workspace"\n\n[permissions.asset-filing.filesystem]\n'
new+=''.join(json.dumps(root)+' = "write"\n' for root in roots)
new+='\n[permissions.asset-filing.network]\nenabled = false\n'
after=tomllib.loads(new)
unchanged_before={k:v for k,v in before.items() if k not in ('sandbox_mode','sandbox_workspace_write')}
unchanged_after={k:v for k,v in after.items() if k not in ('default_permissions','permissions')}
assert unchanged_before==unchanged_after
assert after['permissions']['asset-filing']['filesystem']==dict.fromkeys(roots,'write')
assert after['permissions']['asset-filing']['network']=={'enabled':False}
backup=config.parent/'backups'/('asset-filing-profile-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
backup.mkdir(mode=0o700)
shutil.copy2(config,backup/config.name)
(backup/config.name).chmod(0o600)
assert config.read_text()==old
pending=config.with_name('config.toml.asset-filing-profile-pending')
with pending.open('x') as f:f.write(new)
pending.chmod(config.stat().st_mode & 0o777)
pending.replace(config)
assert tomllib.loads(config.read_text())==after
print(json.dumps({'saved':True,'default_permissions':'asset-filing','writable_filing_folders':roots,'network_enabled':False,'other_config_unchanged':True,'backup':str(backup)},indent=2))
