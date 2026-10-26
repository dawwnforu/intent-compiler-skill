"""Input transport checks, not model or visual-quality tests."""
from pathlib import Path
import tempfile
import unittest
from eval_reference_inputs import image_arguments


class ReferenceInputs(unittest.TestCase):
    def test_declared_order_is_forwarded(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ("second.png", "first.png"):
                (root / name).write_bytes(b"fixture; decoding belongs to the host")
            self.assertEqual(image_arguments(root, ["second.png", "first.png"], required=True),
                             ["--image", str(root / "second.png"), "--image", str(root / "first.png")])

    def test_required_empty_list_blocks(self):
        with self.assertRaises(ValueError):
            image_arguments(".", [], required=True)

    def test_missing_blocks_instead_of_dropping(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError):
                image_arguments(folder, ["missing.png"], required=True)

    def test_empty_file_blocks(self):
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / "empty.png").touch()
            with self.assertRaises(ValueError):
                image_arguments(folder, ["empty.png"], required=True)

    def test_workspace_escape_blocks(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError):
                image_arguments(folder, ["../private.png"], required=True)

    def test_nonvisual_task_needs_no_image(self):
        self.assertEqual(image_arguments(".", []), [])


if __name__ == "__main__":
    unittest.main()
