"""Candidate helper tests; not evidence that a Skill improves model behavior."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).parent / "fixtures/html-entry-helper/check_html_scripts.py"
spec = importlib.util.spec_from_file_location("html_scripts", SCRIPT)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


class CheckScripts(unittest.TestCase):
    def test_markup_and_files(self):
        with tempfile.TemporaryDirectory(dir=SCRIPT.parent) as directory:
            page = Path(directory) / "index.html"
            (page.parent / "应用.js").write_text("const example = 1;", encoding="utf-8")
            cases = [
                ('<script src="应用.js"></script><body>OK</body>', True),
                ('<script src="应用.js"></head><body>Lost</body>', False),
                ('<SCRIPT SRC="应用.js"/>', False),
                ('<!-- <script src="missing.js"> --><p>OK</p>', True),
                ('<script>const a="<script>";</script>', True),
                ('<script src="%E5%BA%94%E7%94%A8.js?v=2#x"></script>', True),
                ('<script src="missing.js"></script>', False),
                ('<script src=""></script>', False),
            ]
            for markup, passed in cases:
                with self.subTest(markup=markup):
                    page.write_text(markup, encoding="utf-8")
                    self.assertEqual(helper.check(page)["passed"], passed)

    def test_environment_resources_are_explicitly_unchecked(self):
        with tempfile.TemporaryDirectory(dir=SCRIPT.parent) as directory:
            page = Path(directory) / "index.html"
            page.write_text('<script src="https://example.invalid/a.js"></script><script src="/app.js"></script>', encoding="utf-8")
            result = helper.check(page)
            self.assertTrue(result["passed"])
            self.assertEqual(len(result["skipped"]), 2)

    def test_command_fails_for_unreadable_input(self):
        with tempfile.TemporaryDirectory(dir=SCRIPT.parent) as directory:
            result = subprocess.run([sys.executable, str(SCRIPT), str(Path(directory) / "absent.html")], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('"passed": false', result.stdout)


if __name__ == "__main__":
    unittest.main()
