from os import PathLike
from pathlib import Path
from typing import Union

DiffPath = Union[str, PathLike[str]]


def read_diff_file(path: DiffPath) -> str:
    """Return the contents of a UTF-8 encoded .diff file."""
    diff_path = Path(path)

    if not diff_path.exists():
        raise FileNotFoundError(f"Diff file not found: {path}")

    if diff_path.suffix != ".diff":
        raise ValueError("Input file must be a .diff file")

    if not diff_path.is_file():
        raise ValueError("Input path must be a file")

    return diff_path.read_text(encoding="utf-8")
