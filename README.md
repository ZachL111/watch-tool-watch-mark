# watch-tool-watch-mark

`watch-tool-watch-mark` is a Python project for CLI tools. It turns package a Python local lab for watch analysis with fixture event logs, golden state snapshots, and documented operating limits into a small local model with readable fixtures and a direct verification command.

## Reading Watch Tool Watch Mark

Start with the README, then open `metadata/project.json` to check the constants behind the examples. After that, `fixtures/cases.csv` shows the compact path and `examples/extended_cases.csv` gives a wider look at the same rule.

## Purpose

The repository exists to keep a technical idea small enough to reason about. The implementation avoids external dependencies where possible, then uses fixtures to make changes easy to review.

## Design Sketch

The core is a scoring model over demand, capacity, latency, risk, and weight. That keeps terminal output, argument shape, and file input in one explicit decision path. The threshold is 183, with risk penalty 7, latency penalty 3, and weight bonus 2. The Python code favors standard library tools and direct tests over framework weight.

## Fixture Notes

The extended cases are not random smoke tests. `degraded` keeps pressure on the review path, while `recovery` shows the model when capacity and weight are strong enough to clear the threshold.

## What It Does

- Uses fixture data to keep argument shape changes visible in code review.
- Includes extended examples for file input, including `recovery` and `degraded`.
- Documents repeatable reports tradeoffs in `docs/operations.md`.
- Runs locally with a single verification command and no external credentials.
- Stores project constants and verification metadata in `metadata/project.json`.

## Setup

Install Python and run the commands from the repository root. The project does not need credentials or a hosted service.

## Verification

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/audit.ps1
```

The audit command checks repository structure and README constraints before it delegates to the verifier.

## Files Worth Reading

- `src`: primary implementation
- `tests`: verification harness
- `fixtures`: compact golden scenarios
- `examples`: expanded scenario set
- `metadata`: project constants and verification metadata
- `docs`: operations and extension notes
- `scripts`: local verification and audit commands
- `pyproject.toml`: Python project metadata

## Limits

This code is local-first. It makes no claim about deployed usage and avoids credentials, hosted state, and environment-specific setup.

## Next Directions

- Add a short report command that prints the score breakdown for a single scenario.
- Add malformed input fixtures so the failure path is as visible as the happy path.
- Split the scoring constants into a typed configuration object and validate it before use.
- Add one more cli tools fixture that focuses on a malformed or borderline input.

## Usage

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

This runs the language-level build or test path against the compact fixture set.
