# Adoption Guide

1. Copy `template/` contents into a new repository root.
2. Replace placeholders:
- `<PROJECT_NAME>`
- `<MARKER_PREFIX>`
- `<SERVICE_NAME>`
- `<DEFAULT_PORT>`
- `<TEST_CMD_1>`, `<TEST_CMD_2>`, `<TEST_CMD_3>`
3. Run scaffold validation:
```bash
python3 tools/validate_template_scaffold.py
```
4. Create first marker and experiment:
- `docs/engineering/work-index.md`
- `docs/experiments/EXP-0001-<slug>.md`
5. Enable CI by pushing `.github/workflows/compose-tests.yml`.


## Paired adoption (recommended)

1. Clone `engineering-scaffold-template` into your project for execution scaffolding.
2. Clone `agent-overseer-framework` into `.overseer/` (or governance location) for oversight gates.
3. Require that all release decisions include both:
- engineering evidence artifacts
- overseer gate outcomes
