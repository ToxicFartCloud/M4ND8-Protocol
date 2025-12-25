# M4ND8 Protocol — Doctrine (v4.4)

_A visual + procedural guide for humans and autonomous workers. Static doctrine, not a template._

---

## 0) Why this exists

This blueprint teaches workers how to use the Mandate Protocol so builds are predictable, auditable, and ship-ready—no matter the prompt.

- The law lives in `director.yaml`.
- The contract lives in `spec.md`.
- The teeth live in `fnl_chk.yaml`.

This doctrine file is static. It never changes per project.

---

## 1) The Three Unbreakable Mandates

- **Absolute Census (`hub.md` as wiring)**  
  Each directory maintains a `hub.md` wiring diagram describing connections (nodes/edges), non-obvious placements, and explicit external dependencies. It includes a small `hub_wiring:` YAML block for machine checks.

- **Sovereign Blackboard (`cofo.md` as ledger)**  
  Each directory maintains a `cofo.md`. This is the Shared State Ledger. It is the **only** valid mechanism for agent‑to‑agent context transfer. Passing context via chat history alone is forbidden.

- **Intentional Emptiness**  
  Empty or deferred areas must be declared in `cofo.md` and reflected in `hub.md`.

> Violate a mandate → **HARD_STOP → ESCALATE** (per `director.yaml`).

---

## 2) Visual Map — How the control plane fits together

```text
┌─────────────────────────────┐
│ m4nd8_pro/director.yaml     │ ← Law: read-order, roles, budgets, hard-stops, escalation
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ m4nd8_pro/manifest.yaml    │ ← Runtime truth: verification_target, features, boundaries
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ ./hub.md (wiring)           │ ← Directory wiring diagram (nodes/edges + rationale + YAML)
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ {target_dir}/cofo.md        │ ← Sovereign Blackboard (Items + Change Notes + State)
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ m4nd8_pro/spec.md           │ ← Sovereign project contract (no placeholders)
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ m4nd8_pro/doctrine.md       │ ← This file: how to use the protocol (doctrine + SOP)
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ m4nd8_pro/ui.yaml (+chk)    │ ← UI rules (tokens/modes) + ui_checklist_uni.md audit
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ m4nd8_pro/fnl_chk.yaml      │ ← Supreme Law: final certification checks (teeth)
└─────────────────────────────┘
```

---

## 3) File Roles (non-overlapping)

- **`director.yaml`**  
  First read, last authority. Defines read-order, roles, budgets, hard-stops, escalation, and the log contract.

- **`manifest.yaml`**  
  Declares `verification_target`, enabled features, and boundaries. May override defaults.

- **`hub.md`**  
  Wiring diagram, not a tree. Shows non-obvious placements, relations (verbs like `imports`, `reads`, `writes`, `invokes`, `generates`, `enforces`, `consumes_from`, etc.), and a `hub_wiring:` YAML block so automation can verify nodes/edges.

- **`cofo.md`**  
  Sovereign Blackboard: the shared brain for all agents. Records **Items** (Path / Role / Description) and **Change Notes** (Timestamp / Actor / Path / Change / Evidence).

- **`spec.md`**  
  Sovereign specification; exhaustive and explicit. Template-only authoring guidance lives in `spec(template).md`, not here.

- **`ui.yaml` / `ui_checklist_uni.md`**  
  UI rules and the corresponding audit steps (WCAG 2.2 AA). If UI exists, run the audit before final certification.

- **`fnl_chk.yaml`**  
  Supreme checks. All applicable must pass; no ship otherwise.

### 3.1) Using `cofo.md` (Context Form) and `hub.md` (Wiring)

**`cofo.md` — Sovereign Blackboard (ledger)**

- Items table lists every file/subdir with a one-line purpose.
- Change Notes table gets a new row for every edit:  
  `Timestamp (UTC), Actor, Path, Change, Why/Evidence (PR/commit/HALT)`.
- Function: agents must read this to understand **where we are** before acting. Agents must write to this to signal **what I did** to the next agent.

**`hub.md` — Wiring Diagram**

- *Non-Obvious Placements* explains why files live where they live.
- *Wiring Table* lists relations (From, Relation, To, Why) using verbs like `imports`, `reads`, `writes`, `invokes`, `generates`, `enforces`, `consumes_from`.
- *Machine-Readable Wiring*: a `hub_wiring:` YAML block with `nodes`, `edges`, and `local_only` for checks.

**Catastrophic-readability guarantee:**  
Both are Markdown so a human can reconstruct what happened with nothing but a text viewer.

---

## 4) Standard Operating Procedure (SOP)

Run this sequence at the start of every task/session.

### 4.1 Conformance Audit

1. Confirm `manifest.yaml` exists and declares a runnable `verification_target`.
2. Confirm target directories have `hub.md` (wiring) and `cofo.md` (ledger).
3. If anything is missing or ambiguous → `HALT_WITH_CITATION` .

### 4.2 Load Context (Strict Order)

Load in this exact order:

1. `director.yaml`  
2. `manifest.yaml`  
3. `hub.md`  
4. target `cofo.md`  
5. `spec.md`  
6. `doctrine.md`  
7. (`ui.yaml` + `ui_checklist_uni.md`, if UI exists)  
8. `fnl_chk.yaml`

### 4.3 Plan → Implement (Agentic TDD) → Verify

Emit `_logs/action_plan.md` with steps mapped to files.

**Agentic TDD Loop (Anti-Hallucination):**

1. **RED:** Write the failing test case first. Run it to confirm failure.
2. **GREEN:** Write the minimal code to pass the test.
3. **REFACTOR:** Optimize and clean up.

If UI is enabled, the Builder **must** write a PBT spec for theme contrast before implementing any visual component.

**Reflexion Protocol:**

- If verification fails more than 2 times:  
  1. **STOP** execution.  
  2. **GENERATE** `_logs/reflection.md` explaining why the approach failed (for example: “Incorrect assumption about API response format”).  
  3. **RE-PLAN** using the insight from the reflection.  
- Blind retries without reflection are forbidden.

Logging during work:

- Update `hub.md` if wiring changes.
- Update `cofo.md` Change Notes; log `COFO_NOTE_OK: <path>`.
- Log full execution trace to `_logs/trace/{actor_id}/{timestamp}.json`.
- Always log `WRITE_OK: <path>` for each write.

### 4.3.1 Reflexion Protocol (Enhanced)

If verification fails > 2 times:

1. **STOP** execution.
2. **GENERATE** `_logs/reflection.md` using **structured trace data** from `_logs/trace/`.
3. **RE-PLAN** using low-level error codes, dependency hashes, and file snippets—not just `cofo.md` summaries.

### 4.4 Audit & Complete — Janitor Sweep

- Run janitor agent to remove unused variables, commented-out code, and temp files.
- If UI features are enabled, run the UI audit from `ui_checklist_uni.md`.
- Run `fnl_chk.yaml`. **100% or no ship.**
- Any HALT triggers the escalation protocol and produces `_logs/HALT_ALERT.md`.

---

## 5) Logging Contract (what workers must write to logs)

Workers must emit these canonical lines (exactly) so automation and humans can follow the story:

```text
READ_OK: director.yaml → manifest.yaml → hub.md → cofo.md → spec.md → doctrine.md → fnl_chk.yaml
PLAN_OK
WRITE_OK: <path>           # one per changed path
COFO_NOTE_OK: <path>       # one per changed path after Change Note added
HUB_WIRING_OK: <dir>       # optional; when wiring gets updated/validated
VERIFY_OK
HALT:<reason>
```

These lines make certification checks greppable and post-mortems human-readable.

---

## 6) Optional Features & Templates

- Optional directories (for example, `plugins/`, `adapters/`) are created only when feature flags are `true` in `manifest.yaml`. Otherwise, they do not exist.
- Master templates for `cofo.md` and `hub.md` live inside `./m4nd8_pro` and are marked **TEMPLATE-ONLY**.  
  When copied into other folders, delete the template boxes before shipping.

---

## 7) Minimal Conformance Checklist (eyes-only quick pass)

- [ ] `manifest.yaml` exists with a runnable `verification_target`.
- [ ] Target folders contain `hub.md` (wiring) and `cofo.md` (ledger).
- [ ] For each changed file: `WRITE_OK` + a Change Note row + `COFO_NOTE_OK`.
- [ ] TDD verified: tests were written before the implementation code.
- [ ] If wiring changed: `hub.md` updated and (optionally) `HUB_WIRING_OK` logged.
- [ ] No optional scaffolds exist without feature flags.
- [ ] `verification_target` is green; `fnl_chk.yaml` is 100% green.
- [ ] Any HALT produced `_logs/HALT_ALERT.md` and a clear citation.

---

## 8) Glossary (fast onboarding)

- **Wiring Diagram (`hub.md`)** — Human + machine description of connections (nodes/edges), rationale, and external dependencies.
- **Sovereign Blackboard (`cofo.md`)** — The shared brain. Records state, history, and intent. Critical for multi-agent coordination.
- **Verification Target** — Single command proving the project works.
- **Agentic TDD** — The mandate to write failing tests before writing code to prevent hallucination.
- **HARD_STOP / ESCALATE** — Policy violation triggers structured alert; work pauses until reviewed.

> Prompts are fickle; structure is reliable. Follow the map, log the steps, and leave breadcrumbs in Markdown.

---

## Chain of Verification (CoVe) Policy

When generating structured outputs (e.g., JSON, config files, reports), agents **must not fabricate fields** to satisfy schema requirements.

If an agent is uncertain about the existence of a data point:
1. It **must generate verification questions** (e.g., "Verify revenue amount from Q3 report").
2. It **must execute retrieval** (RAG) to answer them.
3. It **must rewrite the output** using only verified facts.