#!/usr/bin/env python3

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    'README.md',
    'Dockerfile',
    'docker-compose.yml',
    'Makefile',
    '.github/workflows/compose-tests.yml',
    'docs/README.md',
    'docs/engineering/implementation-playbook.md',
    'docs/engineering/marking-system.md',
    'docs/experiments/EXP-0001-template.md',
    'docs/decisions/DEC-0001-template.md',
    'docs/dev/container-first.md',
    'app/main.py',
]

for rel in REQUIRED:
    p = ROOT / rel
    if not p.exists():
        raise FileNotFoundError(f'missing required file: {rel}')

print('OK: template scaffold validation passed')
