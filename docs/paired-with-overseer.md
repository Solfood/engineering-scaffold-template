# Paired Usage with Agent Overseer Framework

This repository defines execution scaffolding. Pair it with:

- `agent-overseer-framework` for governance, risk, safety, and security oversight.

## Responsibility split

| This repo (`engineering-scaffold-template`) | `agent-overseer-framework` |
|---|---|
| Work slicing, marker tracking, implementation flow | Approval gates, risk classification, blocking criteria |
| Evidence collection and artifact capture | Security baseline, threat model policy |
| CI/runtime scaffolding and experiment tracking | Gate evaluation and release sign-off |
| Session continuity and handoff notes | Operating model and escalation triggers |

---

## When to trigger a gate review

Gate reviews happen at specific scaffold lifecycle stages — not continuously.

| Playbook stage | What you do | Gate(s) triggered |
|---|---|---|
| `DISCOVER` | Fill `task-intake.md` with objective, scope, risk class, critical assets | Gate 1 — Coherence |
| `DECIDE` | Complete `DEC-NNNN.md` with chosen option, alternatives rejected, rationale | Gate 1 — Coherence (finalize) |
| `DECIDE` (medium/high risk) | Complete `threat-model.md` before any implementation begins | Gate 3 — Security |
| `BUILD` | Implement against approved design; flag deviations in session log | Gate 4 — Engineering Fundamentals (ongoing) |
| `VERIFY` | Run tests, attach output as evidence artifact; do not use prose-only claims | Gate 5 — Verification |
| `CONSOLIDATE` | Promote stable outcomes into architecture/product docs | Gate 1 — Coherence (close) |
| `HANDOFF` | Fill `release-readiness.md`; include rollback plan and operational notes | Gates 2, 6 — Safety + Readiness |

---

## Scaffold artifact → gate mapping

Use this table when filling out `release-readiness.md` to know which artifacts satisfy each gate.

| Gate | Gate name | Satisfied by (scaffold artifact) |
|---|---|---|
| Gate 1 | Coherence | `task-intake.md` (objective + scope) + `DEC-NNNN.md` (decision record) |
| Gate 2 | Safety | `task-intake.md` (risk class) + rollback notes in `session-log.md` or `release-readiness.md` |
| Gate 3 | Security | `threat-model.md` (medium/high risk tasks) + secrets handling notes in decision record |
| Gate 4 | Engineering Fundamentals | Session log entries referencing marker IDs + code review evidence |
| Gate 5 | Verification | `EXP-NNNN.md` experiment outcomes + CI run artifacts from `compose-tests.yml` |
| Gate 6 | Release Readiness | Completed `release-readiness.md` + deployment/rollback plan documented |

---

## Minimum handoff package

Every release handoff must include:

- Marker ID and current status (from `work-index.md`)
- Decision record link (`docs/decisions/DEC-NNNN.md`)
- Evidence artifacts (test output, CI logs, experiment results)
- Completed `release-readiness.md` with all six gate outcomes
- Any infrastructure recovery notes (backend state, stale locks, expired credentials, manual cleanup steps)
- Next actions for the receiving engineer or agent
