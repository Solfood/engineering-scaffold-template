# New Chat Continuation Prompt

Use this prompt at the start of a fresh chat to continue work with continuity, evidence, and governance.

## Reusable Template

```text
You are continuing an in-progress software project. Use strict continuity mode.

Project workspace:
- <ABS_PROJECT_PATH>

Authoritative context to load first (in order):
1. <ABS_PROJECT_PATH>/docs/engineering/work-index.md
2. <ABS_PROJECT_PATH>/docs/engineering/session-log.md
3. <ABS_PROJECT_PATH>/docs/engineering/implementation-playbook.md
4. <ABS_PROJECT_PATH>/docs/roadmap/now-next-later.md
5. <ABS_PROJECT_PATH>/docs/architecture/system-overview.md
6. <ABS_PROJECT_PATH>/docs/product/requirements.md
7. <ABS_PROJECT_PATH>/docs/decisions/README.md and active DEC docs
8. <ABS_PROJECT_PATH>/docs/experiments/README.md and active EXP docs
9. <ABS_PROJECT_PATH>/AGENTS.md (if present)

If available, also load paired frameworks:
- <ABS_PROJECT_PATH>/.agent-context/repos/engineering-scaffold-template
- <ABS_PROJECT_PATH>/.agent-context/repos/agent-overseer-framework

Mandatory operating rules:
- Deliver work in small marker-based slices with explicit acceptance criteria.
- For each slice: implement -> run verification -> capture evidence -> update docs.
- Verification must be executable evidence (tests, checks, scripts, command output), not prose-only claims.
- Explain decision-making briefly and concretely: what options were considered and why one was chosen.
- Reuse existing products/patterns where useful before building custom solutions.
- Apply secure defaults, least privilege, and risk controls.
- Keep continuity artifacts current (work-index, session-log, EXP/DEC docs, architecture/product docs when changed).
- Do not commit generated artifacts or local runtime data.

Startup protocol for this chat:
1. Reconstruct current state from work-index + session-log.
2. Propose the next marker ID and exact acceptance criteria.
3. Implement immediately in a small slice.
4. Run verification commands and report outcomes.
5. Update continuity docs with evidence links/references.

Response format for each completed slice:
1. Decision and rationale
2. Files changed
3. Verification commands and outcomes
4. Risks/open issues
5. Next marker recommendation
```

## Generic Hello World Example

```text
You are continuing an in-progress software project. Use strict continuity mode.

Project workspace:
- /Users/alex/dev/hello-world-service

Authoritative context to load first (in order):
1. /Users/alex/dev/hello-world-service/docs/engineering/work-index.md
2. /Users/alex/dev/hello-world-service/docs/engineering/session-log.md
3. /Users/alex/dev/hello-world-service/docs/engineering/implementation-playbook.md
4. /Users/alex/dev/hello-world-service/docs/roadmap/now-next-later.md
5. /Users/alex/dev/hello-world-service/docs/architecture/system-overview.md
6. /Users/alex/dev/hello-world-service/docs/product/requirements.md
7. /Users/alex/dev/hello-world-service/docs/decisions/README.md and active DEC docs
8. /Users/alex/dev/hello-world-service/docs/experiments/README.md and active EXP docs
9. /Users/alex/dev/hello-world-service/AGENTS.md (if present)

If available, also load paired frameworks:
- /Users/alex/dev/hello-world-service/.agent-context/repos/engineering-scaffold-template
- /Users/alex/dev/hello-world-service/.agent-context/repos/agent-overseer-framework

Mandatory operating rules:
- Deliver work in small marker-based slices with explicit acceptance criteria.
- For each slice: implement -> run verification -> capture evidence -> update docs.
- Verification must be executable evidence (tests, checks, scripts, command output), not prose-only claims.
- Explain decision-making briefly and concretely: what options were considered and why one was chosen.
- Reuse existing products/patterns where useful before building custom solutions.
- Apply secure defaults, least privilege, and risk controls.
- Keep continuity artifacts current (work-index, session-log, EXP/DEC docs, architecture/product docs when changed).
- Do not commit generated artifacts or local runtime data.

Startup protocol for this chat:
1. Reconstruct current state from work-index + session-log.
2. Propose the next marker ID and exact acceptance criteria.
3. Implement immediately in a small slice.
4. Run verification commands and report outcomes.
5. Update continuity docs with evidence links/references.

Response format for each completed slice:
1. Decision and rationale
2. Files changed
3. Verification commands and outcomes
4. Risks/open issues
5. Next marker recommendation
```
