# Contributing

Thanks for helping. The Lab is a set of small browser tools, each one file with no dependencies.

## Before you change anything

Open an issue first, so the idea is agreed before the work is done. A typo fix does not need one.

## How to change a tool

1. Edit the file in `src/` or `shared/`. Never edit a generated `<tool>/index.html` or `README.md`.
2. Run `python3 build.py`.
3. Commit the source and the regenerated pages together. CI fails if they are out of date.
4. Open a pull request that mentions the issue.

`meeting-receipt` is hand-written, so it is edited directly.

## Ground rules

- No network calls, no accounts, no tracking. Files are read in the browser and never uploaded.
- No dependencies. Each tool stays one standalone file.
- Test on your own sample file before opening a pull request, and never attach real personal data to an issue.
