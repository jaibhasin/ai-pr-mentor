from os import PathLike
from pathlib import Path
from typing import Union

ReviewPath = Union[str, PathLike[str]]


def write_review_file(review_text: str, path: ReviewPath = "review.md") -> Path:
    """Write the generated review to a markdown file and return its path."""
    review_path = Path(path)
    review_path.write_text(review_text, encoding="utf-8")
    return review_path
