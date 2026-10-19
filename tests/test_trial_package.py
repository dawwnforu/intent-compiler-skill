"""One bounded encoding regression; no host or model compatibility claim."""
import io
from pathlib import Path
import sys
import zipfile

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pilot'))
from build_trial import recipient_archive

def check():
    raw=io.BytesIO();text='客户回复：确认时间，其他事项待定。\n'
    page='<meta charset="utf-8"><a href="回复单.txt">reply</a>'.encode('utf-8')
    with zipfile.ZipFile(raw,'w') as z:
        z.writestr('回复单.txt',text.encode('utf-8'))
        z.writestr('index.html',page)
        z.writestr('asset.bin',b'\x00\xff\x80')
        z.comment=b'fixture comment'
    original=raw.getvalue()
    fixed=recipient_archive(original)
    with zipfile.ZipFile(io.BytesIO(fixed)) as z:
        assert z.namelist()==['回复单.txt','index.html','asset.bin'] and z.comment==b'fixture comment'
        assert z.read('回复单.txt')==b'\xef\xbb\xbf'+text.encode('utf-8')
        assert z.read('asset.bin')==b'\x00\xff\x80'
        assert z.read('index.html')==page
    with zipfile.ZipFile(io.BytesIO(recipient_archive(fixed))) as z:
        assert z.read('回复单.txt')==b'\xef\xbb\xbf'+text.encode('utf-8')
    with zipfile.ZipFile(io.BytesIO(original)) as z:assert z.read('回复单.txt')==text.encode('utf-8')
    invalid=io.BytesIO()
    with zipfile.ZipFile(invalid,'w') as z:z.writestr('bad.txt',b'\xff')
    try:recipient_archive(invalid.getvalue())
    except UnicodeDecodeError:pass
    else:raise AssertionError('Unknown text encoding must fail, never guess or replace source text')
    print('PASS: explicit UTF-8 identity, original/other bytes preserved, repeat stable, unsupported encoding rejected')

if __name__=='__main__':check()
