# Engineering Scaffold Template

Reusable scaffold for AI-assisted iterative delivery. Combines execution structure with governance gates in a single repo.

## Setup

1. Copy this repo into your project.
2. Set your project name and marker prefix in `policies/project-policy.yaml`.
3. Read `CLAUDE.md` — that's the full operating guide for any AI agent working in this repo.

## Placeholders to replace

- `<PROJECT_NAME>`
- `<MARKER_PREFIX>`

## How it works

- `CLAUDE.md` — AI operating instructions: lifecycle, gates, markers, security defaults
- `docs/work-index.md` — track active work items
- `docs/session-log.md` — continuity across sessions
- `docs/decisions/` — decision records (DEC-NNNN.md)
- `docs/experiments/` — experiment records (EXP-NNNN.md)
- `templates/` — intake, decisions, threat models, release readiness

## Commit hygiene

Keep durable artifacts (decisions, experiments with evidence, architecture notes). Prune session scratchpads and agent-only working notes before pushing.
