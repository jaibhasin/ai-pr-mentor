# AI PR Mentor

A CLI tool for reviewing `.diff` files with Gemini.

## Features

- Reads local `.diff` files.
- Shows per-file added and removed line counts.
- Generates AI-powered PR reviews.
- Saves generated reviews to `review.md`.

## Commands

```bash
ai-pr-mentor stats path/to/changes.diff
```

Shows a diff summary with files changed, added lines, and removed lines.

```bash
ai-pr-mentor review path/to/changes.diff
```

Sends the diff to Gemini, prints the AI review, and writes it to `review.md`.
