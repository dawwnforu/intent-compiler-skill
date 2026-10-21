"""Local packaging boundaries, not marketplace scan or model-behavior tests."""
import io
from pathlib import Path
import sys
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'commercial'))
from build_submission import committed_source, encode_archive, verify_archive


class SubmissionPackage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries, cls.source, cls.timestamp = committed_source('HEAD')

    def test_exact_source_and_deterministic_bytes(self):
        first = encode_archive(self.entries, self.source, self.timestamp)
        self.assertEqual(first, encode_archive(self.entries, self.source, self.timestamp))
        source, entries = verify_archive(first)
        self.assertEqual(entries, self.entries)
        self.assertEqual(source['sourceCommit'], self.source['sourceCommit'])
        self.assertIn('SKILL.md', zipfile.ZipFile(io.BytesIO(first)).namelist())

    def test_unsafe_or_unexpected_members_rejected(self):
        for path in ['../outside.md', '/outside.md', '.env', 'scripts/cache.pyc']:
            with self.subTest(path=path), self.assertRaises(ValueError):
                encode_archive({**self.entries, path: b'disposable fixture'}, self.source, self.timestamp)

    def test_missing_runtime_reference_stops_build(self):
        entries = dict(self.entries)
        del entries['references/quality-check.md']
        with self.assertRaises(ValueError):
            encode_archive(entries, self.source, self.timestamp)

    def test_known_secret_pattern_stops_build(self):
        entries = {**self.entries, 'README.md': b'Synthetic scanner fixture: ghp_' + b'A' * 36}
        with self.assertRaises(ValueError):
            encode_archive(entries, self.source, self.timestamp)

    def test_tampered_member_rejected(self):
        original = encode_archive(self.entries, self.source, self.timestamp)
        output = io.BytesIO()
        with zipfile.ZipFile(io.BytesIO(original)) as source, zipfile.ZipFile(output, 'w') as target:
            for name in source.namelist():
                target.writestr(name, source.read(name) + (b'\nchanged' if name == 'SKILL.md' else b''))
        with self.assertRaises(ValueError):
            verify_archive(output.getvalue())


if __name__ == '__main__':
    unittest.main()
