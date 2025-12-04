# hub — Wiring Diagram (Control Plane)
_M4ND8 Protocol v4.2_

---

<!-- ------------------------------------------------------------------
  TEMPLATE-ONLY SECTION (kept here as the master template)
  Copy from “Template Start” to “Template End” into any other folder
  and then DELETE this template box there before shipping.
------------------------------------------------------------------- -->

<!-- TEMPLATE-ONLY: hub-template-start -->

## hub — Wiring Diagram (Template)

- **Directory:** `<path/to/dir>`  
- **Scope:** Declare how files in this folder connect to each other and to outside paths.  
- **Why Markdown:** In a catastrophic failure, humans can read this and reconstruct intent.

### Non-Obvious Placements (Why does this file live here?)

| Path               | Rationale                                       |
|--------------------|-------------------------------------------------|
| `./example_helper.py` | Lives alongside config to avoid circular import in `./src/core/`. |

### Wiring Table

| From           | Relation | To                    | Why              |
|----------------|----------|-----------------------|------------------|
| `./file_a.py`  | imports  | `./file_b.py`         | Validation helpers |
| `./file_b.py`  | reads    | `../assets/schema.json` | Runtime schema   |

Use verbs like `imports`, `reads`, `writes`, `invokes`, `generates`, `enforces`, `declares`, `copies_to`, `consumes_from`.

### External Dependencies (explicit, versioned)

| Name     | Version/Pin | Used by    | Why               |
|----------|-------------|-----------|-------------------|
| `pydantic` | `^2.7`      | `./api.py` | Request validation |

### Contracts / Invariants

- `./file_a.py` must not import network clients (keeps core pure).
- `./config/` writes only to `./state/` (no cross-folder writes).

### Machine-Readable Wiring (for checks)

```yaml
hub_wiring:
  nodes:
    - ./file_a.py
    - ./file_b.py
    - ../assets/schema.json
  edges:
    - { from: ./file_a.py, relation: imports, to: ./file_b.py, why: "Validation helpers" }
    - { from: ./file_b.py, relation: reads, to: ../assets/schema.json, why: "Runtime schema" }
  local_only:
    - ./README.md  # files intentionally not in the graph
    - ./cofo.md
    - ./hub.md
```

<!-- TEMPLATE-ONLY: hub-template-end -->

---

<!-- --------------------- END TEMPLATE-ONLY SECTION ------------------- -->

## Operating Hub — `./m4nd8_pro`

- **Directory:** `./m4nd8_pro`  
- **Scope:** Control plane wiring for policy, doctrine, UI rules, and verification.

### Non-Obvious Placements

| Path                      | Rationale                                                                 |
|---------------------------|---------------------------------------------------------------------------|
| `./manifest.template.yaml` | Lives in control plane so new projects inherit policy pins.              |
| `./cofo.md`               | Acts as the "Sovereign Blackboard" (Shared State Ledger).                |

### Wiring Table

| From                 | Relation   | To                       | Why                                       |
|----------------------|-----------|--------------------------|-------------------------------------------|
| `./director.yaml`    | enforces  | `./fnl_chk.yaml`         | Director maps violations → checks (teeth) |
| `./director.yaml`    | references | `./blueprint.md`        | Human procedure & SOP (how to obey)       |
| `./spec(template).md` | references | `./manifest.template.yaml` | Seeds the runtime manifest             |
| `./ui.yaml`          | is_a      | `./ui_checklist_uni.md`  | Checklist verifies the rules in `ui.yaml` |

### External Dependencies

| Name | Version/Pin | Used by | Why |
|------|-------------|---------|-----|
| (none) | — | — | — |

### Contracts / Invariants

- No product code lives in `./m4nd8_pro`.
- Any change to `./director.yaml` must be reflected in `./fnl_chk.yaml` if it alters enforcement.
- Any change to `./ui.yaml` must be auditable by `./ui_checklist_uni.md`.

### Machine-Readable Wiring (for checks)

```yaml
hub_wiring:
  nodes:
    - ./director.yaml
    - ./fnl_chk.yaml
    - ./blueprint.md
    - ./spec_template.md
    - ./manifest.template.yaml
    - ./ui.yaml
    - ./ui_checklist_uni.md
    - ./cofo.md
    - ./hub.md
  edges:
    - { from: ./director.yaml, relation: enforces, to: ./fnl_chk.yaml, why: "Violations → HARD_STOP checks" }
    - { from: ./director.yaml, relation: references, to: ./blueprint.md, why: "Read-order & SOP guidance" }
    - { from: ./spec_template.md, relation: references, to: ./manifest.template.yaml, why: "Seed manifest fields" }
    - { from: ./ui.yaml, relation: is_a, to: ./ui_checklist_uni.md, why: "Checklist verifies UI rules" }
  local_only:
    - ./README.md
```
