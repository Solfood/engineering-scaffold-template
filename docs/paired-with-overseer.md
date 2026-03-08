# Paired Usage with Agent Overseer Framework

This repository defines execution scaffolding. Pair it with:

- `agent-overseer-framework` for governance, risk, safety, and security oversight.

## Responsibility split

- `engineering-scaffold-template`:
- Work slicing, implementation flow, marker tracking, evidence collection, CI/runtime scaffolding.

- `agent-overseer-framework`:
- Approval gates, risk model, security baseline, threat modeling, release blocking criteria.

## Recommended combined flow

1. Intake work item using overseer templates (`task-intake`, risk class).
2. Plan/execute with engineering markers, experiments, and decision records.
3. Run verification and collect artifacts.
4. Audit release artifacts/package contents and strip local-only files.
5. Evaluate against overseer review gates.
6. Approve/block release with explicit rationale and residual risk.

## Minimum handoff package

- Marker ID + current status
- Latest decision record link
- Evidence artifacts
- Gate outcomes (pass/fail)
- Next actions
- Any infrastructure recovery notes (backend state, stale locks, expired credentials, manual cleanup steps)
