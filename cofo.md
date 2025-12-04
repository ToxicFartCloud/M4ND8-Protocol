# cofo — Context Form (Control Plane)
_M4ND8 Protocol v4.2_

---

<!-- ------------------------------------------------------------------
  TEMPLATE-ONLY SECTION (kept here as the master template)
  Copy from “Template Start” to “Template End” into any other folder
  and then DELETE the whole template box there before shipping.
------------------------------------------------------------------- -->

<!-- TEMPLATE-ONLY: cofo-template-start -->

## cofo — Context Form (Template)

- **Directory:** `<path/to/dir>`  
- **Purpose:** One sentence on what this directory is for.

### Items (Role & Description)

| Path                | Role    | Description                     |
|---------------------|---------|---------------------------------|
| `./example_file.ext` | Module | What this file is for.          |
| `./subdir/`         | Subdir  | What lives here.                |

_List every file/subdir in this folder. If something is deferred or temporary, say so here._

### Change Notes

_Add an entry whenever an item changes. Keep it short; link to evidence._

| Timestamp (UTC)        | Actor     | Path                | Change            | Why / Evidence              |
|------------------------|-----------|---------------------|-------------------|-----------------------------|
| 2025-01-01T00:00:00Z   | worker-id | `./example_file.ext` | Short verb phrase | PR #123 / commit `abc123`   |

### Rules (Local)

- `cofo` must list **all** items in this folder.
- Every edit to an item must add a **Change Note** row.
- Keep prose minimal; this is a ledger, not an essay.

<!-- TEMPLATE-ONLY: cofo-template-end -->

---

<!-- --------------------- END TEMPLATE-ONLY SECTION ------------------- -->

## Operating Ledger — `./m4nd8_pro`

- **Directory:** `./m4nd8_pro`  
- **Purpose:** Project control plane (policy, doctrine, verification). Sovereign Blackboard for agent context.

### Items (Role & Description)

| Path                       | Role   | Description                                                     |
|----------------------------|--------|-----------------------------------------------------------------|
| `./director.yaml`          | Policy | Read order, roles, budgets, hard stops, escalation.            |
| `./fnl_chk.yaml`           | Checks | Final certification (teeth).                                   |
| `./blueprint.md`           | Guide  | How to use `m4nd8_pro` (visual map + SOP).                   |
| `./spec_template.md`       | Template | Authoring contract + Template-Only usage rules.              |
| `./manifest.template.yaml` | Template | Seed for `manifest.yaml` (features, `verification_target`).  |
| `./ui.yaml`                | UI Rules | Tokens, modes, baseline constraints (if UI exists).         |
| `./ui_checklist_uni.md`    | UI Audit | WCAG 2.2 AA checklist & verification steps.                 |
| `./cofo.md`                | Ledger | This file—doubles as template and local `cofo`.               |
| `./hub.md`                 | Census | Absolute file list for this folder.                           |

_If you add/remove a file here, update `hub.md` first, then this **Items** table._

### Change Notes

_Record why each change happened, with evidence._

| Timestamp (UTC) | Actor | Path | Change | Why / Evidence |
|-----------------|-------|------|--------|----------------|
|                 |       |      |        |                |

### Rules (Local)

- **Control plane purity:** Only control artifacts live here; no product code or third-party assets.
- **Template hygiene:** “TEMPLATE-ONLY” markers are allowed here (master template) but must not appear in any other folder’s `cofo.md`.
- **Audit trail:** Any edit to an item in this folder requires a **Change Note** entry.

