import unittest
from types import SimpleNamespace
from unittest.mock import patch

from ai_pr_mentor import llm_client


class FakeModels:
    def __init__(self) -> None:
        self.calls: list[dict[str, str]] = []

    def generate_content(self, *, model: str, contents: str) -> object:
        self.calls.append({"model": model, "contents": contents})
        return SimpleNamespace(text="  # AI PR Review\nLooks good.  ")


class LLMClientTests(unittest.TestCase):
    def test_generate_review_uses_default_flash_lite_model(self) -> None:
        fake_models = FakeModels()
        fake_client = SimpleNamespace(models=fake_models)
        fake_google_module = SimpleNamespace(
            genai=SimpleNamespace(Client=lambda api_key=None: fake_client)
        )
        fake_dotenv_module = SimpleNamespace(load_dotenv=lambda: None)

        with patch.dict(
            "sys.modules",
            {"dotenv": fake_dotenv_module, "google": fake_google_module},
        ):
            review = llm_client.generate_review("Review this diff")

        self.assertEqual(review, "# AI PR Review\nLooks good.")
        self.assertEqual(
            fake_models.calls,
            [
                {
                    "model": "gemini-2.5-flash-lite",
                    "contents": "Review this diff",
                }
            ],
        )

    def test_generate_review_rejects_empty_prompt(self) -> None:
        with self.assertRaisesRegex(ValueError, "Prompt"):
            llm_client.generate_review("   ")


if __name__ == "__main__":
    unittest.main()
