# Engineering Scaffold Template

Reusable scaffold for AI-assisted iterative delivery. Combines execution structure with governance gates in a single repo.

## Bootstrap a new project

```bash
mkdir -p <new-project> && cd <new-project>
git init
git clone https://github.com/Solfood/engineering-scaffold-template.git .tmp
rsync -a .tmp/ ./
rm -rf .tmp
```

Then open `policies/project-policy.yaml` and set `project_name` and `marker_prefix`.

## Placeholders to replace

- `<PROJECT_NAME>`
- `<MARKER_PREFIX>`

## How it works

- `CLAUDE.md` — full operating guide for any AI agent in this repo
- `docs/work-index.md` — active work items with markers
- `docs/session-log.md` — continuity across sessions
- `docs/decisions/` — DEC-NNNN.md decision records
- `docs/experiments/` — EXP-NNNN.md experiment records
- `templates/` — decision-record (includes intake), experiment, threat-model, release-readiness

## Commit hygiene

Keep: decisions, experiments with evidence, architecture notes, session log. Prune: agent scratch notes, generated files, local state.
