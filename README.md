# Learn MCP Protocol with Python

A hands-on workspace for learning the Model Context Protocol (MCP) with Python,
following *Learn Model Context Protocol with Python*. Examples will be added as
you work through the book.

## Prerequisites

- Python 3.10 or newer (Python 3.11 is a good choice for matching book examples)
- `venv` and `pip` (included with standard Python installations)

This starter pins the MCP Python SDK to its v1 maintenance line because many
book examples use the `FastMCP` API. The newer v2 SDK has breaking API changes.
Follow the version used by the book when reproducing its examples.

## Create and activate a virtual environment

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS / Linux
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

To leave the environment, run `deactivate`. The `.venv/` directory is ignored by
Git and should never be committed.

## Run the starter MCP server

With the virtual environment active:

```bash
mcp dev src/server.py
```

This launches the MCP Inspector for interactive exploration. The sample server
exposes a greeting tool, a small resource, and a prompt. To run it directly over
stdio, use:

```bash
python src/server.py
```

## Suggested learning flow

1. Run the sample and inspect its tool, resource, and prompt.
2. Add one example at a time as you reach each book chapter.
3. Keep personal notes and credentials out of this public repository.

## Public repository and secrets

This repository is intended to be public. Do not add API keys, access tokens,
passwords, private notes, or personal data. Put local credentials in `.env`;
Git ignores it. `.env.example` is safe for documenting variable names and
non-secret placeholder values.

Before pushing, inspect the staged changes with `git diff --cached` and run:

```bash
git status --short
git diff --cached --check
```
