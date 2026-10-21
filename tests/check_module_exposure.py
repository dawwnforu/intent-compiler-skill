"""Conservative tool-output evidence for a scoped Skill-method comparison.

This is not proof of attention or a security attestation. Missing/truncated or
unrecognized read evidence stays unverified; do not regenerate to force a pass.
"""
import argparse
import json
from pathlib import Path
import re


def module_exposure(events, module, marker):
    path = module.replace('\\', '/')
    matches = []
    for event in events:
        item = event.get('item', {})
        if event.get('type') != 'item.completed' or item.get('type') != 'command_execution':
            continue
        command = item.get('command', '').replace('\\', '/')
        output = item.get('aggregated_output', '')
        if (path in command and re.search(r'\bGet-Content\b|\bread_text\s*\(|\bReadAllText\s*\(', command)
                and isinstance(output, str) and marker in output):
            matches.append({'item': item.get('id'), 'exitCode': item.get('exit_code')})
    return {'status': 'observed' if matches else 'unverified', 'module': module, 'matches': matches,
            'scope': 'Matching file-read command plus distinctive method text in actual completed tool output; not model self-report or proof of attention.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('events', type=Path)
    parser.add_argument('--module', required=True)
    parser.add_argument('--marker', required=True)
    args = parser.parse_args()
    events = [json.loads(line) for line in args.events.read_text(encoding='utf-8').splitlines() if line.strip()]
    result = module_exposure(events, args.module, args.marker)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result['status'] == 'observed' else 2


if __name__ == '__main__':
    raise SystemExit(main())
