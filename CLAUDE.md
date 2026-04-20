# CLAUDE.md — Project Operating Instructions

This scaffold gives AI agents a consistent execution and governance framework across sessions. Read this file at the start of every chat.

---

## Startup Protocol

Every new session:
1. Read `docs/work-index.md` — what's active and its status
2. Read `docs/session-log.md` — what happened last session and what's next
3. Propose the next marker ID and exact acceptance criteria
4. Implement in the smallest useful slice, verify, update docs

---

## Markers

Format: `<PREFIX>-<TRACK>-<NNNN>`

Example: `MYAPP-ARCH-0001`

Common tracks: `ARCH` `API` `DATA` `SEC` `OBS` `DX` `FIX`

Rules:
- Every active work item has a marker in `docs/work-index.md`
- Every commit references a marker ID
- `docs/session-log.md` entries include marker IDs

Status values: `PLANNED | IN_PROGRESS | BLOCKED | DONE | DROPPED`

Set your prefix in `policies/project-policy.yaml`.

---

## Lifecycle

Work moves through six stages. Gates are checkpoints embedded within them — don't skip.

### 1. DISCOVER
- Confirm the baseline behavior and constraints
- Scan for prior art and reusable patterns before building anything new

### 2. DECIDE
- Compare options; write `DEC-NNNN.md` in `docs/decisions/`
- Classify risk: **low / medium / high** (see Risk section)
- Fill `templates/task-intake.md`
- **Gate 1 — Coherence:** task-intake complete, scope bounded, decision record written
- **Gate 3 — Security** *(medium/high risk only)*: complete `templates/threat-model.md` before any implementation

### 3. BUILD
- Implement the smallest vertical slice first
- Flag any deviations from the approved design in `docs/session-log.md`
- **Gate 4 — Engineering Fundamentals:** see checklist below

### 4. VERIFY
- Run tests and checks; attach output as evidence artifacts
- No prose-only claims — if you can't attach evidence, the verification didn't happen
- **Gate 5 — Verification:** tests pass, evidence attached, security checks pass

### 5. CONSOLIDATE
- Promote stable outcomes into `docs/decisions/` or architecture docs
- Prune temporary working notes from the repo

### 6. HANDOFF
- Write a session log entry with exact next actions
- **Gate 2 — Safety:** rollback plan documented
- **Gate 6 — Release Readiness:** complete `templates/release-readiness.md` before any release

---

## Gates Quick Reference

| Gate | Name | Stage | Requires |
|------|------|-------|----------|
| 1 | Coherence | DECIDE | task-intake.md + DEC-NNNN.md |
| 2 | Safety | HANDOFF | rollback plan in session-log or release-readiness |
| 3 | Security | DECIDE (medium/high) | threat-model.md complete |
| 4 | Engineering Fundamentals | BUILD | checklist below satisfied |
| 5 | Verification | VERIFY | test/check artifacts attached |
| 6 | Release Readiness | HANDOFF | release-readiness.md all gates pass |

**Block conditions:** any failed gate blocks release until resolved or explicitly risk-accepted with rationale documented.

---

## Risk Classification

**Low** — reversible, no critical asset impact → fast-path, no threat model required

**Medium** — cross-service impact, user data touched, or non-trivial blast radius → threat model required before BUILD

**High** — auth/crypto/infra boundaries, regulated data, irreversible migrations → explicit approval required, escalated review

Escalation triggers (always stop and document):
- Unresolved critical or high vulnerability
- Data loss risk without tested rollback
- Irreversible migration without staged validation

---

## Engineering Fundamentals Checklist

Before marking any work DONE, verify:

- [ ] Objective and success criteria were defined before building
- [ ] Inputs validated at all trust boundaries
- [ ] Error paths implemented and tested, not just happy path
- [ ] Names convey intent; control flow is easy to follow
- [ ] Tests appropriate for the risk level; evidence attached
- [ ] Rollback or containment path exists for risky changes
- [ ] Logs/metrics sufficient for diagnosis in production

---

## Security Defaults

Always apply, no exceptions:
- No plaintext secrets in the repo (use env vars or secret managers)
- Input validation at every trust boundary
- Least privilege for service accounts, API tokens, credentials
- Explicit authz checks on sensitive operations
- Dependency vulnerability scanning enabled

Sensitive change categories requiring extra scrutiny:
- Authentication / authorization logic
- Cryptography, key handling, token handling
- Data export/import, backups, migrations
- Network perimeter or firewall changes

---

## Decision Standard

Every `DEC-NNNN.md` must include:
- What was decided and why
- Alternatives rejected and the reason each was rejected
- Risks and mitigations
- Evidence supporting the decision
- What remains unverified

---

## Artifact Hygiene

**Commit:** decision records, experiment results with evidence, architecture docs, session log, work index

**Do not commit:** agent scratch notes, generated files, local state, secret overrides, temporary planning artifacts

---

## File Map

| File | Purpose |
|------|---------|
| `docs/work-index.md` | Active work items with marker IDs and status |
| `docs/session-log.md` | Append-only continuity log across sessions |
| `docs/decisions/` | DEC-NNNN.md decision records |
| `docs/experiments/` | EXP-NNNN.md experiment records |
| `policies/project-policy.yaml` | Project config: name, prefix, risk tolerance, critical assets |
| `templates/task-intake.md` | Start every work item here |
| `templates/decision-record.md` | Significant design decisions |
| `templates/experiment.md` | Hypothesis-driven investigation |
| `templates/threat-model.md` | Required for medium/high risk work |
| `templates/release-readiness.md` | Required before every release |
