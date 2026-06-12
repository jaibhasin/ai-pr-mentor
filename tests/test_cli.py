from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from typer.testing import CliRunner

from ai_pr_mentor.cli import app


class CliTests(unittest.TestCase):
    def test_review_subcommand_prints_diff_contents(self) -> None:
        runner = CliRunner()

        with TemporaryDirectory() as temp_dir:
            diff_path = Path(temp_dir) / "changes.diff"
            diff_path.write_text("diff --git a/file.py b/file.py\n", encoding="utf-8")

            result = runner.invoke(app, ["review", str(diff_path)])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("diff --git a/file.py b/file.py\n", result.output)


if __name__ == "__main__":
    unittest.main()
