# prompt_builder.py


def build_review_prompt(diff_text: str) -> str:
    diff_text = diff_text.rstrip()

    return f"""
You are an expert software engineer reviewing a Git pull request.

Review the following git diff.

Focus on:
1. Bugs
2. Logic issues
3. Security problems
4. Performance problems
5. Code readability
6. Missing tests
7. Unnecessary changes

Return the review in this markdown format:

# AI PR Review

## Summary
Briefly explain what changed.

## Issues Found
List real issues only. If no issues, say "No major issues found."

## Suggestions
Give practical improvement suggestions.

## Tests to Add
Suggest useful tests.

## Risk Level
Choose one: Low, Medium, High.

Here is the diff:

```diff
{diff_text}
```
""".strip()
