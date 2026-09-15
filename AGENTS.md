# Project instructions

## Purpose

This repository is for teaching FastAPI to beginners. Build the material incrementally as the user shares each lesson's content.

## Teaching materials

- Maintain Markdown lecture notes and runnable `.py` examples together.
- Store numbered notes in `notes/lecture_XX.md`.
- Write clear, general teaching notes without YouTube, video, or screenshot references.
- Explain concepts, commands, and code in simple language. Include learning objectives, expected output, common problems, and practice exercises where useful.
- Keep examples focused on the current lesson. Preserve completed examples when later lessons extend them.
- Keep the lecture index and setup instructions in `README.md` accurate.

## Python environment and validation

- Use the existing `.venv` environment for installations and execution.
- Use Windows PowerShell commands in setup instructions.
- Maintain `requirements.txt` when project dependencies change.
- Keep `.venv`, Python caches, credentials, and secrets out of Git.
- Run changed Python examples and appropriate checks before publishing. For documentation-only changes, check accuracy, links, and consistency with the code.

## GitHub workflow

- Destination repository: https://github.com/haqnawaz99/fast-api.
- Use origin for this remote and main as the default branch.

- Publish each update through a feature branch and pull request. Do not push changes directly to the default branch.
- Push the feature branch, create a PR, review its complete diff, address findings, and then merge it after relevant checks pass.
- Review notes and code for correctness, beginner readability, consistency, and accidental inclusion of generated files or secrets.
- Report review findings honestly. Do not claim independent approval when performing a self-review.
- Respect branch protection and required external approvals; do not bypass them.
- The user has authorized pushing project updates, creating PRs, reviewing them, and merging them through this workflow. Do not request repeated permission for these routine steps.
- Confirm the merged state and provide the PR link and validation summary after publishing.
- If the destination repository is unknown, obtain its URL before publishing. Do not guess the destination or create a new GitHub repository without instruction.
