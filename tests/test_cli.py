from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

try:
    from typer.testing import CliRunner
except ModuleNotFoundError:  # pragma: no cover - depends on local env
    CliRunner = None

try:
    from ai_pr_mentor.cli import app
except ModuleNotFoundError:  # pragma: no cover - depends on local env
    app = None



@unittest.skipUnless(CliRunner is not None and app is not None, "typer is not installed")
class CliTests(unittest.TestCase):
    def test_review_subcommand_prints_diff_summary(self) -> None:
        runner = CliRunner()

        with TemporaryDirectory() as temp_dir:
            diff_path = Path(temp_dir) / "changes.diff"
            diff_path.write_text(
                """\
diff --git a/file.py b/file.py
--- a/file.py
+++ b/file.py
@@ -1 +1,2 @@
-old line
+new line
+another line
""",
                encoding="utf-8",
            )

            result = runner.invoke(app, ["review", str(diff_path)])

        self.assertEqual(result.exit_code, 0)
        self.assertIn("Diff Summary", result.output)
        self.assertIn("file.py: Added lines: 2, Removed lines: 1", result.output)


if __name__ == "__main__":
    unittest.main()
