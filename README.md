# Engineering Scaffold Template

Reusable project scaffold for iterative delivery across multiple sessions.

## Includes

- Decision/experiment-driven docs workflow
- Marker-based work tracking (`<PREFIX>-<TRACK>-<NNNN>`)
- Session handoff log for continuity
- Evidence-first validation policy
- Container-first local/CI workflow

## Quick Start

1. Copy this template into a new repo.
2. Set your marker prefix in `docs/engineering/marking-system.md`.
3. Create your first experiment from `docs/experiments/EXP-0001-template.md`.
4. Update CI workflow commands in `.github/workflows/compose-tests.yml`.

## Placeholder Convention

Search and replace these tokens:

- `<PROJECT_NAME>`
- `<MARKER_PREFIX>`
- `<SERVICE_NAME>`
- `<DEFAULT_PORT>`
- `<TEST_CMD_1>`, `<TEST_CMD_2>`, `<TEST_CMD_3>`

## Companion Framework

Use this together with `agent-overseer-framework` to add governance and security gatekeeping to execution workflows.

- Companion repo: https://github.com/Solfood/agent-overseer-framework
- Integration guide: `docs/paired-with-overseer.md`


## Start New Project (Human Bootstrap)

```bash
mkdir -p <new-project> && cd <new-project>
git init

# Pull execution scaffold
git clone https://github.com/Solfood/engineering-scaffold-template.git .tmp-engineering
rsync -a .tmp-engineering/ ./
rm -rf .tmp-engineering

# Pull overseer framework as governance layer
git clone https://github.com/Solfood/agent-overseer-framework.git .overseer
```

Then run:

```bash
python3 tools/validate_template_scaffold.py
python3 .overseer/tools/validate_overseer_framework.py
```
