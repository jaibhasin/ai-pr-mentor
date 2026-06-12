import unittest

from ai_pr_mentor.prompt_builder import build_review_prompt


class BuildReviewPromptTests(unittest.TestCase):
    def test_includes_diff_in_closed_diff_code_fence(self) -> None:
        diff_text = """\
diff --git a/app.py b/app.py
--- a/app.py
+++ b/app.py
@@ -1 +1 @@
-old
+new
"""

        prompt = build_review_prompt(diff_text)

        self.assertIn("```diff\n" + diff_text + "```", prompt)
        self.assertTrue(prompt.startswith("You are an expert software engineer"))
        self.assertTrue(prompt.endswith("```"))


if __name__ == "__main__":
    unittest.main()
