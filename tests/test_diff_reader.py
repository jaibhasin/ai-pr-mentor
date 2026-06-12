from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from ai_pr_mentor.diff_reader import get_diff_stats, read_diff_file


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

    def test_get_diff_stats_returns_per_file_line_counts(self) -> None:
        diff_text = """\
diff --git a/app.py b/app.py
index 1111111..2222222 100644
--- a/app.py
+++ b/app.py
@@ -1,3 +1,3 @@
-old line
+new line
 context line
diff --git a/readme.md b/readme.md
index 3333333..4444444 100644
--- a/readme.md
+++ b/readme.md
@@ -1 +1,2 @@
+added line
 unchanged line
"""

        summary = get_diff_stats(diff_text)

        self.assertEqual(
            summary,
            {
                "file_names": ["app.py", "readme.md"],
                "added_lines": [1, 1],
                "removed_lines": [1, 0],
            },
        )


if __name__ == "__main__":
    unittest.main()
