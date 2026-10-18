"""Build a LOCAL synthetic trial archive from explicit files; never an Agensi upload."""
import json
from pathlib import Path
import sys
import subprocess
import zipfile

def main():
    repo=Path(__file__).resolve().parent.parent
    target=Path(sys.argv[1]).resolve();example=Path(sys.argv[2]).resolve()
    target.parent.mkdir(parents=True,exist_ok=True)
    assert not subprocess.check_output(['git','diff','--name-only','HEAD','--','skills/intent-compiler'],cwd=repo).strip(),'Commit core changes before attributing a trial snapshot'
    core_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
    source={'project':'Intent Compiler','repository':'https://github.com/dawwnforu/intent-compiler-skill',
        'attribution':'Intent Compiler contributors','manifestVersion':json.loads((repo/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))['version'],
        'candidate':'2.0 unreleased','coreBaseCommit':core_commit,'purpose':'Free local synthetic pilot, not marketplace submission; MIT unchanged'}
    entries={name:repo/'pilot'/name for name in ['README.md','feedback.md','pilot-log.csv']}
    entries.update({'COMPATIBILITY.md':repo/'pilot/compatibility.md','LICENSE':repo/'LICENSE'})
    core=repo/'skills/intent-compiler'
    for p in core.rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':entries['skill/intent-compiler/'+p.relative_to(core).as_posix()]=p
    for p in (repo/'pilot/sample-inputs').iterdir():entries['sample/inputs/'+p.name]=p
    for name in ['client.zip','internal.md']:entries['sample/outputs/'+name]=example/'outputs'/name
    assert (repo/'pilot/pilot-log.csv').read_text().count('\n')==1,'Never package participant records'
    with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr('SOURCE.json',json.dumps(source,ensure_ascii=False,indent=2)+'\n')
        for name,p in entries.items():z.write(p,name)
    with zipfile.ZipFile(target) as z:
        assert z.read('LICENSE')==(repo/'LICENSE').read_bytes()
        assert z.read('skill/intent-compiler/LICENSE')==(repo/'LICENSE').read_bytes()
        assert z.read('sample/outputs/client.zip')==(example/'outputs/client.zip').read_bytes()
        assert not any(n.endswith(('.env','.pyc')) or '/.git/' in n for n in z.namelist())
    print(str(target),target.stat().st_size,'bytes; explicit-file package checks passed')

if __name__=='__main__':main()
