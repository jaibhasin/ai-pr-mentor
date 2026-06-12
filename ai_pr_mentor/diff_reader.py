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


def get_diff_stats(diff_text: str) -> dict[str, list[str] | list[int]]:
    """Return per-file added and removed line counts from a unified diff."""
    file_names: list[str] = []
    added_lines: list[int] = []
    removed_lines: list[int] = []
    current_file: str | None = None
    current_added = 0
    current_removed = 0

    def flush_current_file() -> None:
        nonlocal current_file, current_added, current_removed
        if current_file is None:
            return

        file_names.append(current_file)
        added_lines.append(current_added)
        removed_lines.append(current_removed)

        current_file = None
        current_added = 0
        current_removed = 0

    for line in diff_text.splitlines():
        if line.startswith("diff --git "):
            flush_current_file()
            parts = line.split()
            if len(parts) >= 4:
                current_file = parts[3].removeprefix("b/")
            continue

        if line.startswith("+++") or line.startswith("---"):
            continue

        if current_file is None:
            continue

        if line.startswith("+"):
            current_added += 1
        elif line.startswith("-"):
            current_removed += 1

    flush_current_file()

    return {
        "file_names": file_names,
        "added_lines": added_lines,
        "removed_lines": removed_lines,
    }
