"""Build a reviewable Skill-only ZIP from committed Git blobs, never upload it."""
import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'skills/intent-compiler/'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def validate_entries(entries):
    required = {'SKILL.md', 'LICENSE', 'README.md', 'agents/openai.yaml',
                'references/knowledge-index.md', 'scripts/check_html_scripts.py'}
    if not required <= entries.keys():
        raise ValueError('Required Skill resources are missing')
    for name, body in entries.items():
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or '\\' in name:
            raise ValueError('Unsafe archive path: ' + name)
        allowed = (name in {'SKILL.md', 'README.md', 'LICENSE', 'agents/openai.yaml'}
                   or path.parent == PurePosixPath('references') and path.suffix == '.md'
                   or name == 'scripts/check_html_scripts.py'
                   or path.parent == PurePosixPath('assets') and path.suffix == '.svg')
        if not allowed:
            raise ValueError('Unexpected file: ' + name)
        text = body.decode('utf-8')
        if '\ufffd' in text or re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|ghp_[A-Za-z0-9]{36,}|AKIA[0-9A-Z]{16}', text):
            raise ValueError('Damaged text or a known credential pattern: ' + name)
        if path.suffix == '.md':
            for link in re.findall(r'!?\[[^\]]*\]\(([^)\s]+)\)', text):
                parsed = urlsplit(link)
                if parsed.scheme or not parsed.path:
                    continue
                parts = list(path.parent.parts)
                raw = unquote(parsed.path)
                if raw.startswith(('/', '\\')):
                    raise ValueError('Absolute resource link: ' + link)
                for part in PurePosixPath(raw).parts:
                    if part == '..':
                        if not parts:
                            raise ValueError('Resource leaves archive: ' + link)
                        parts.pop()
                    elif part != '.':
                        parts.append(part)
                if '/'.join(parts) not in entries:
                    raise ValueError('Missing relative resource: ' + name + ' -> ' + link)
    skill = entries['SKILL.md'].decode('utf-8')
    if not skill.startswith('---\n') or '\n---\n' not in skill:
        raise ValueError('Missing frontmatter')
    header = skill.split('\n---\n', 1)[0]
    if not re.search(r'^name: intent-compiler$', header, re.M) or not re.search(r'^description: .+', header, re.M):
        raise ValueError('Missing required name/description')
    # This is a check of this controlled header, not a general YAML/platform validator.


def encode_archive(entries, source, timestamp):
    validate_entries(entries)
    source = {**source, 'files': {name: {'sha256': digest(body), 'bytes': len(body)}
                                 for name, body in sorted(entries.items())}}
    payload = {**entries, 'SOURCE.json': (json.dumps(source, ensure_ascii=False, indent=2) + '\n').encode('utf-8')}
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, body in sorted(payload.items()):
            info = zipfile.ZipInfo(name, timestamp)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, body, compresslevel=9)
    return output.getvalue()


def verify_archive(data):
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or archive.testzip() is not None:
            raise ValueError('Duplicate member or failed CRC')
        source = json.loads(archive.read('SOURCE.json'))
        entries = {name: archive.read(name) for name in names if name != 'SOURCE.json'}
    validate_entries(entries)
    expected = {name: {'sha256': digest(body), 'bytes': len(body)} for name, body in sorted(entries.items())}
    if source.get('files') != expected:
        raise ValueError('SOURCE member hashes do not match')
    return source, entries


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def committed_source(ref):
    commit = git('rev-parse', '--verify', ref + '^{commit}').decode().strip()
    entries = {}
    for row in git('ls-tree', '-rz', commit, '--', PREFIX).split(b'\0'):
        if not row:
            continue
        descriptor, path = row.split(b'\t', 1)
        mode, kind, sha = descriptor.split()
        if kind != b'blob' or mode not in (b'100644', b'100755'):
            raise ValueError('Only ordinary committed files are allowed')
        name = path.decode('utf-8').removeprefix(PREFIX)
        entries[name] = git('cat-file', 'blob', sha.decode())
    manifest = json.loads(git('show', commit + ':.codex-plugin/plugin.json'))
    if entries.get('LICENSE') != git('show', commit + ':LICENSE'):
        raise ValueError('Root and standalone MIT notices differ')
    shallow = git('rev-parse', '--is-shallow-repository').strip() == b'true'
    runtime = None if shallow else git('log', '-1', '--format=%H', commit, '--', PREFIX + 'SKILL.md', PREFIX + 'references', PREFIX + 'scripts').decode().strip()
    source = {'project': 'Intent Compiler', 'repository': manifest['repository'],
              'attribution': manifest['author']['name'], 'manifestVersion': manifest['version'],
              'candidate': '2.0 unreleased candidate', 'sourceCommit': commit,
              'runtimeCommit': runtime, 'sourceBytes': 'Committed Git blobs; no worktree caches or local data',
              'marketplaceStatus': 'Submission candidate only; platform scan, agent delivery and licence relationship unverified',
              'license': 'MIT; the bundled standard notice is unchanged'}
    epoch = int(git('show', '-s', '--format=%ct', commit))
    timestamp = datetime.fromtimestamp(epoch, timezone.utc).timetuple()[:6]
    return entries, source, timestamp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output_directory', type=Path)
    parser.add_argument('--ref', default='HEAD')
    args = parser.parse_args()
    entries, source, timestamp = committed_source(args.ref)
    data = encode_archive(entries, source, timestamp)
    verify_archive(data)
    args.output_directory.mkdir(parents=True, exist_ok=True)
    target = args.output_directory / ('intent-compiler-2.0-candidate-' + source['sourceCommit'][:7] + '.zip')
    with target.open('xb') as file:
        file.write(data)
    with target.with_suffix('.zip.sha256').open('x', encoding='ascii') as file:
        file.write(digest(data) + '  ' + target.name + '\n')
    print(json.dumps({'file': str(target), 'bytes': len(data), 'sha256': digest(data), 'members': len(entries) + 1,
                      'sourceCommit': source['sourceCommit'], 'runtimeCommit': source['runtimeCommit']}, indent=2))


if __name__ == '__main__':
    main()
