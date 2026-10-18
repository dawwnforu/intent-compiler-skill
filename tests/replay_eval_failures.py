"""Reconstruct frozen local driver checks in a NEW directory; no model calls."""
import json
from pathlib import Path
import subprocess
import sys

def main():
    record=json.loads((Path(__file__).parent/'results/v2-eval-failures.json').read_text(encoding='utf-8'))
    target=Path(sys.argv[1]).resolve()
    target.mkdir(parents=True,exist_ok=False)
    work=target/'work';work.mkdir()
    for name,source in record['sources'].items():
        assert Path(name).name==name and name.endswith(('.py','.json')),name
        (work/name).write_text(source,encoding='utf-8')
    (target/'outputs/intent-compiler-v2').mkdir(parents=True)
    result=subprocess.run([sys.executable,str(work/'check_eval_failures.py')],cwd=target)
    raise SystemExit(result.returncode)

if __name__=='__main__':main()
