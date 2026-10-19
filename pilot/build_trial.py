"""Build a LOCAL synthetic trial archive from explicit files; never an Agensi upload."""
import json
import io
from pathlib import Path
import sys
import subprocess
import zipfile

def recipient_archive(data):
    """Identify UTF-8 TXT explicitly for browsers that otherwise guess its encoding."""
    output=io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(data)) as source, zipfile.ZipFile(output,'w') as target:
        target.comment=source.comment
        for item in source.infolist():
            body=source.read(item)
            if not item.is_dir() and item.filename.lower().endswith('.txt'):
                body=body.decode('utf-8-sig').encode('utf-8-sig')
            target.writestr(item,body)
    return output.getvalue()

def main():
    repo=Path(__file__).resolve().parent.parent
    target=Path(sys.argv[1]).resolve();example=Path(sys.argv[2]).resolve()
    target.parent.mkdir(parents=True,exist_ok=True)
    assert not subprocess.check_output(['git','diff','--name-only','HEAD','--','skills/intent-compiler'],cwd=repo).strip(),'Commit core changes before attributing a trial snapshot'
    core_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
    source={'project':'Intent Compiler','repository':'https://github.com/dawwnforu/intent-compiler-skill',
        'attribution':'Intent Compiler contributors','manifestVersion':json.loads((repo/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))['version'],
        'candidate':'2.0 unreleased','coreBaseCommit':core_commit,'purpose':'Free local synthetic pilot, not marketplace submission; MIT unchanged',
        'samplePresentation':'Recipient TXT files carry a UTF-8 BOM; decoded text, names and non-TXT member bytes are unchanged. Original R70 archive is preserved separately.'}
    entries={name:repo/'pilot'/name for name in ['README.md','feedback.md','pilot-log.csv']}
    entries.update({'COMPATIBILITY.md':repo/'pilot/compatibility.md','LICENSE':repo/'LICENSE'})
    core=repo/'skills/intent-compiler'
    for p in core.rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':entries['skill/intent-compiler/'+p.relative_to(core).as_posix()]=p
    for p in (repo/'pilot/sample-inputs').iterdir():entries['sample/inputs/'+p.name]=p
    for name in ['client.zip','internal.md']:entries['sample/outputs/'+name]=example/'outputs'/name
    assert (repo/'pilot/pilot-log.csv').read_text().count('\n')==1,'Never package participant records'
    payload={name:p.read_bytes() for name,p in entries.items()}
    original=payload['sample/outputs/client.zip']
    payload['sample/outputs/client.zip']=recipient_archive(original)
    with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr('SOURCE.json',json.dumps(source,ensure_ascii=False,indent=2)+'\n')
        for name,body in payload.items():z.writestr(name,body)
    with zipfile.ZipFile(target) as z:
        assert z.read('LICENSE')==(repo/'LICENSE').read_bytes()
        assert z.read('skill/intent-compiler/LICENSE')==(repo/'LICENSE').read_bytes()
        with zipfile.ZipFile(io.BytesIO(original)) as before, zipfile.ZipFile(io.BytesIO(z.read('sample/outputs/client.zip'))) as after:
            assert before.namelist()==after.namelist()
            for name in before.namelist():
                if name.lower().endswith('.txt'):
                    assert before.read(name).decode('utf-8-sig')==after.read(name).decode('utf-8-sig')
                    assert after.read(name).startswith(b'\xef\xbb\xbf')
                else:assert before.read(name)==after.read(name)
        assert not any(n.endswith(('.env','.pyc')) or '/.git/' in n for n in z.namelist())
    print(str(target),target.stat().st_size,'bytes; explicit-file package checks passed')

if __name__=='__main__':main()
