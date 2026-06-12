from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from ai_pr_mentor.diff_reader import read_diff_file


class ReadDiffFileTests(unittest.TestCase):
    def test_reads_diff_file_contents(self) -> None:
        with TemporaryDirectory() as temp_dir:
            diff_path = Path(temp_dir) / "changes.diff"
            diff_path.write_text("diff --git a/file.py b/file.py\n", encoding="utf-8")

            self.assertEqual(
                read_diff_file(diff_path),
                "diff --git a/file.py b/file.py\n",
            )

    def test_rejects_missing_file(self) -> None:
        with self.assertRaises(FileNotFoundError):
            read_diff_file("missing.diff")

    def test_rejects_non_diff_extension(self) -> None:
        with TemporaryDirectory() as temp_dir:
            patch_path = Path(temp_dir) / "changes.patch"
            patch_path.write_text("diff contents", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, r"\.diff"):
                read_diff_file(patch_path)

    def test_rejects_directory_with_diff_suffix(self) -> None:
        with TemporaryDirectory() as temp_dir:
            diff_dir = Path(temp_dir) / "changes.diff"
            diff_dir.mkdir()

            with self.assertRaisesRegex(ValueError, "file"):
                read_diff_file(diff_dir)


if __name__ == "__main__":
    unittest.main()
