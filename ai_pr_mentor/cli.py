# cli.py
import typer
from rich.console import Console
from ai_pr_mentor.diff_reader import get_diff_stats, read_diff_file

app = typer.Typer()
console = Console()


@app.callback()
def main() -> None:
    """AI PR Mentor CLI."""


@app.command()
def review(diff_path: str):
    """
    Review a .diff file using AI.
    """
    diff_content = read_diff_file(diff_path)
    diff_stats = get_diff_stats(diff_content)

    console.print("Diff Summary")
    for file_name, added_lines, removed_lines in zip(
        diff_stats["file_names"],
        diff_stats["added_lines"],
        diff_stats["removed_lines"],
    ):
        console.print(
            f"{file_name}: Added lines: {added_lines}, Removed lines: {removed_lines}"
        )


if __name__ == "__main__":
    app()
