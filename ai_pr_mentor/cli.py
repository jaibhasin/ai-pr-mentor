# cli.py
import typer
from rich.console import Console
from ai_pr_mentor.diff_reader import read_diff_file

app = typer.Typer()
console = Console()


@app.command()
def review(diff_path: str):
    """
    Review a .diff file using AI.
    """
    diff_content = read_diff_file(diff_path)
    console.print(diff_content)


if __name__ == "__main__":
    app()