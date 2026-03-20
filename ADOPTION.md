# Adoption Guide

1. Copy this repository's scaffold contents into a new repository root.
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

## Repo content guidance

Keep a clear line between durable repo artifacts and temporary working material.

- Good long-term repo candidates:
  - architecture and product docs that describe the current system
  - durable decisions
  - stable operating notes another engineer would need later
- Usually local or temporary:
  - session-by-session scratch planning
  - agent-only working notes
  - generated artifacts, runtime state, and one-off investigation files

Teams can start broad, but should prune the committed docs set down to the pieces that remain useful after the current workstream is over.


## Paired adoption (recommended)

1. Clone `engineering-scaffold-template` into your project for execution scaffolding.
2. Clone `agent-overseer-framework` into `.overseer/` (or governance location) for oversight gates.
3. Require that all release decisions include both:
- engineering evidence artifacts
- overseer gate outcomes


## Pull Both Framework Repos

```bash
mkdir -p <new-project> && cd <new-project>
git init
git clone https://github.com/Solfood/engineering-scaffold-template.git .tmp-engineering
rsync -a .tmp-engineering/ ./
rm -rf .tmp-engineering
git clone https://github.com/Solfood/agent-overseer-framework.git .overseer
```

## New Chat Continuity

Use `docs/new-chat-continuation-prompt.md` whenever you start a new chat/session so the next agent loads the same sources, applies the same controls, and continues with evidence-backed slices.
