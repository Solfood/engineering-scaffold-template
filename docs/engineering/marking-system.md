# Marking System

Marker format:

`<MARKER_PREFIX>-<TRACK>-<NNNN>`

Example:

- `<MARKER_PREFIX>-ARCH-0001`

Track suggestions:

- `ARCH`, `API`, `CLIENT`, `ADMIN`, `DATA`, `OBS`, `DX`

Status values:

`PLANNED | IN_PROGRESS | BLOCKED | DONE | DROPPED`

Rules:

- Every commit should include one marker ID.
- Every active work item must appear in `work-index.md`.
- `session-log.md` entries must include marker IDs.
