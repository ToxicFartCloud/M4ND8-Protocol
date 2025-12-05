# Project Specification — Template  
## M4ND8 – An Autonomous Agent Control Plane (AACP)  
### v5.1 (Ghost Protocol Edition) — this spec inherits binding doctrine from:  
`.m4nd8/director.yaml`  
`.m4nd8/manifesto.md`

### Master templates live in `m4nd8_pro/`:  
`.m4nd8/templates/ledger.md` — ledger template block (formerly cofo.md)  
`.m4nd8/templates/hub.md` — hub template block (wiring)

🔒 Delete all TEMPLATE-ONLY boxes when copying into project folders. Do not omit unused sections—leave them in and explain why they are left unfilled.

## 0. Definition of Done (applies to every change)

- Code + tests + docs updated together.  
- Contract changes (API/Schema) versioned and migration written.  
- Feature behind a reversible flag with a rollback note.  
- Telemetry for success criteria added and visible in staging.  
- Security notes addressed or a risk waiver is attached to §13.  
- UI Changes: Must pass Visual Regression Tests (VRT) against Figma baselines.

### 0.1 Agentic TDD Mandate (Grounding)

✦ **Critical Anti-Hallucination Rule:**  
1. **RED**: Write the test case FIRST. Run it. It MUST fail (confirming the feature is missing).  
2. **GREEN**: Write the minimal code to pass the test.  
3. **REFACTOR**: Optimize code/tests.  
→ Any code written without a preceding failing test is a violation.

✦ **Structured Data Integrity Rule (CoVe):**  
When generating structured outputs (e.g., JSON, config), if the agent is uncertain about any field:  
- It MUST NOT invent a value to satisfy schema.  
- It MUST generate and answer verification questions via RAG.  
- It MUST omit unverifiable fields or set them to `null`.

### 0.2 The Ghost Protocol (Subtractive Build Mandate)

✦ **Critical Architecture Rule:**  
This project utilizes a **Subtractive Architecture** to enable "Scale-to-Infinity" without refactoring.

1. **Build the Chassis**: All `tier: core` components must be fully functional.  
2. **Gated Features**: If a requirement is marked `tier: enterprise` but the current `target_build_tier` is `micro_mvp`:  
   - **DO NOT** delete the logic.  
   - **DO** implement behind a **Feature Flag** (e.g., `if config.ENABLE_AUDIT_LOGS:`).  
   - **DO** ensure the code compiles/passes static analysis even if the flag is off.  
3. **Upgrade Path**: Enabling a higher tier requires **zero code changes**—only a config toggle (e.g., env var).  
4. **Janitor Immunity**: Code marked `dormant` or `tier: enterprise` is protected from "Unused Code" deletion policies.

---

## 1. Overview

- **Product name:** `<product-name>`  
- **One-sentence purpose:** `<what value is delivered and to whom>`  
- **Primary users / operators:** `<roles>`

**✦ Target Build Tier (Current Invoice):**  
`[ ] MicroMVP` | `[ ] Professional` | `[ ] Enterprise`  
*(Director Note: Only enable features matching this tier or lower.)*

**Success criteria (top 3):**  
- **Core:** `<criterion>`  
- **Pro:** `<criterion>`  
- **Enterprise:** `<criterion>`

---

## 2. Goals & Non-Goals

**Goals**  
- `<goal 1>`  
- `<goal 2>`

**Non-Goals**  
- `<non-goal 1>`  
- `<non-goal 2>`

---

## 3. Architecture & Runtime

### 3.1 Project Map (Directory Structure)

✦ **Directive**: Define the exact directory tree below. This is the source of truth for the Scaffolder agent.The tree shown is just an example do not use it as an exact copy for your tree.  
- Every directory listed here MUST be created.  
- **Dormant Directories**: If a directory belongs to a higher tier, mark it `(Dormant)` in `hub.md` but create it physically.

```text
.
├── src/
│   ├── core/          # Domain logic (Stable, Pure)
│   ├── adapters/      # Interface adapters (Volatile, Impure)
│   └── infrastructure/
├── tests/
├── docs/
├── data/
│   └── (runtime files only)
└── m4nd8_pro/
    └── (control plane)
```

### 3.2 Polyglot Architecture Blueprint

**Directives:**  
- **Greenfield**: Architect MUST declare all components here before Builder begins.  
- **Brownfield**: Coding Agent MUST populate this via static analysis before writing `file_change_plan.md`.

**A. Project Type Declaration (Select one)**  
`[ ] project_type: greenfield` — New project. Components below are authoritative declarations.  
`[ ] project_type: brownfield` — Existing codebase. Components below are to be populated by Coding Agent.

**B. Component Specification (Tiered)**  
Define the system components. Components marked `enterprise` are scaffolded but disabled in lower tiers.

| name | component_type | role | inputs | outputs | min_tier | critical_path | unique_ip | state | core? |
|------|----------------|------|--------|---------|----------|---------------|-----------|-------|-------|
| **auth_engine** | core/stateless | identity | creds | jwt | core | y | n | y | yes |
| **audit_logger** | sidecar | compliance | logs | db_row | enterprise | n | y | y | no |
| **example_ui** | core/stateless | render | user | html | core | y | n | n | yes |

**C. Decision Matrix (Scoring)**  
Use PDS weights: `performance:3`, `safety:2`, `ecosystem:2`, `deploy:2`, `team:1`, `hardware:2`.

| component | option | perf | safety | ecosystem | deploy | team | license_ok | hw_ok | total | status |
|-----------|--------|------|--------|-----------|--------|------|------------|-------|-------|--------|
| **example_ui** | react | 3 | 2 | 3 | 2 | 1 | 1 | 1 | 12 | accepted |

**D. State & Interop Model**  
Choose one per component:  
`core_owned` (stateless engines)  
`engine_snapshot` (engine exposes snapshot/restore)  
`external_store` (SQLite/Redis)

| name | engine_state | state_sync | cache_policy | interop_pattern |
|------|--------------|------------|--------------|------------------|
| **example_ui** | ephemeral | none | none | inproc |

Interop Patterns:  
`inproc` (<10µs)  
`subprocess_jsonrpc` (strong isolation, default)  
`service_grpc` (multi-consumer)

**E. Hardware Constraints**  
```yaml
hardware_targets: [x86_64]
gpu_support:
  allow: false
```

### 3.3 External Memory Strategy (`hub.md` & `cofo.md`)

To prevent context pollution, Agents must treat this file structure as Hierarchical Memory:  
- `hub.md` (Wiring): Read this FIRST to understand relationships without reading source code ("Paging In").  
- `cofo.md` (Ledger): Read this to understand history and status.  
- Source Code: Only read files explicitly referenced in `hub.md` for the current task.

📌 **Trace Reference Requirement**  
Every Change Note must include a `Trace Ref` pointing to `_logs/trace/{actor}/{timestamp}.json`.  
This enables the Manager Agent to perform dynamic replanning using low-level execution data.

✦ **Operational rule:**  
- Before any change → update `hub.md` if wiring changes.  
- After any change → append a Change Note in `cofo.md` (Timestamp / Actor / Path / Change / Why/Evidence / Trace Ref).

### 3.4 Environment & Provisioning

- **Target platforms:** `<linux/macos/windows variants>`  
- **Runtimes:** `<python 3.11 | node 20 | rust 1.79 | …>`

**Containerization (Optional)** → ❌ If unused, delete this entire section before finalizing `spec.md`.  
- **Image baseline:** `<base image>`  
- **Entrypoint:** `<command>`  
- **Volumes:** `<paths>`

#### 3.4.1 Dependency Manifest (choose one)  
Keep only your stack’s format. Delete others.  
- **Python:** `requirements.txt` + lockfile  
- **Node:** `package.json` + `package-lock.json` / `pnpm-lock.yaml`  
- **Rust:** `Cargo.toml` + `Cargo.lock`

#### 3.4.2 Provisioning Command (canonical)  
The entire project MUST provision with a single command on a clean machine:  
```makefile
make setup   # idempotent; installs toolchain, deps, git hooks
```
CI uses the same command. If platform variance is unavoidable, document subtargets: `make setup-linux`, `make setup-macos`.

---

## 4. Interface & Communication Design

✦ **Strict Topology**: Traffic direction dictates protocol. No accidental REST for internal services.

### 4.1 North-South Traffic (External Clients)  
- **Paradigm:** `<REST | GraphQL>` (Choose one)  
- **Contract:** `openapi.yaml` or `schema.graphql`  
- **Caching Strategy:** `<CDN | HTTP Caching>`

### 4.2 East-West Traffic (Internal Services)  
- **Paradigm:** `<gRPC | JSON-RPC | In-Process>` (Default: JSON-RPC for local agents)  
- **Contract:** `.proto` files or `json_schemas/`  
- **Transport:** `<HTTP/2 | Stdin/Stdout | Shared Mem>`

### 4.3 Golden Request/Response  
✦ **Mandatory**: Provide one full request/response pair for the primary entrypoint.  
- **Input:** `examples/primary_request.json`  
- **Output:** `examples/primary_response.json`

---

## 5. Functional Requirements (The Menu)

✦ **Directive**: Phoenix must fill ALL tiers. The Director filters active tasks based on §1.

**Tier 1: Core / MicroMVP (The Chassis)**  
Must be functional for the system to boot.  
FR-C01 — `<requirement>`  
- Acceptance (machine): Response MUST validate against `tests/schemas/fr_c01.response.schema.json`  
- Acceptance (behavior): Gherkin in `tests/e2e/fr_c01.feature` passes in CI  

**Tier 2: Professional (Growth Features)**  
Value-add features for paid users.  
FR-P01 — `<requirement>`  
- Flag: `ENABLE_<FEATURE_NAME>`  
- Acceptance (machine): …  

**Tier 3: Enterprise (Sovereignty & Scale)**  
Compliance, Security, and High-Availability.  
FR-E01 — `<requirement>`  
- Flag: `ENABLE_<FEATURE_NAME>`  
- Acceptance (machine): …  

(Repeat pattern for additional FRs.)

---

## 6. UI Governance & Anti-Slop (If `features.ui: true`)

✦ **Directive**: To prevent "AI Slop" (inconsistent, invented designs), the Builder MUST bind to these sources of truth.

### 6.1 Design System Authority  
- **Tokens Source:** `src/theme/tokens.json` (Colors, Spacing, Typography).  
- **Component Library:** `<Link to Component Docs or Path>`  
- **Icon Set:** `<Name/Source>` (No ad-hoc SVGs).  
- All color tokens in `src/theme/tokens.json` must pass automated PBT for WCAG 2.2 AA contrast (4.5:1).

### 6.2 Visual Regression Testing (VRT)  
- **Tool:** `<Percy | Chromatic | Playwright Snapshots>`  
- **Mandate:** CI MUST fail if pixel drift > 0% without manual approval.

---

## 7. Data Architecture & Polyglot Persistence

✦ **Directive**: Align database choice with data shape. No "one size fits all".

### 7.1 Database Selection Matrix

| Service/Context | Data Shape | Consistency | DB Choice | Rationale |
|-----------------|------------|-------------|-----------|-----------|
| e.g., Payments  | Relational | ACID (Strong) | Postgres | Financial integrity |
| e.g., Search    | Vector     | Eventual    | Qdrant   | RAG support |

### 7.2 Migrations & Retention  
- **Tool:** `<Alembic | Prisma | Flyway>`  
- **Policy:** `<Retention rules>`

---

## 8. Non-Functional Requirements

- **Performance**: P95 ≤ 300 ms for `POST /v1/foo` at 100 RPS (CI load test `make perf`).  
- **Reliability**: SLO 99.9% monthly; error budget 43m 12s. Link to dashboard: `<staging-url>`.  
- **Security**: Threat model in §10; authz matrix defined.  
- **Privacy/PII**: `<data handling — e.g., “no PII stored”>`  
- **Cost ceiling**: ≤ $450/month in staging; alert at $350. Enforced by `tools/cost_guard.yaml`.

---

## 9. Default Specifications & Bundled Artifacts

Purpose: eliminate underspec halts by shipping deterministic defaults.

- **9.1 Specification Fallback Registry (SFR)** → `defaults/spec_fallback_registry.yaml`  
- **9.2 RL Reward Contract** → `defaults/rl_reward.schema.json`  
- **9.3 GA Genome Spec** → `defaults/ga_genome.yaml`  
- **9.4 DTSE I/O Schemas** → `defaults/dtse/*.schema.json`  
- **9.5 Failure-Mode Catalog v1 (≥14)** → `defaults/failure_modes.yaml`  
- **9.6 MCP-DSL v0** →  
  - `defaults/mcp_dsl_v0.ebnf`  
  - `defaults/mcp_ast.schema.yaml`  
  - `examples/hello.spec-dsl`  
- **9.7 Policy Pack** →  
  - `.m4nd8/director.yaml`  
  - `.m4nd8/templates/manifest.template.yaml`  
  - `.m4nd8/policy/compliance.yaml`  
- **9.8 UI Baseline (if `features.ui: true`)** →  
  - `.m4nd8/policy/ui_gate.yaml`  
  - `.m4nd8/templates/ui_checklist_uni.md`

---

## 10. Security Model (Tiered)

- **AuthN/AuthZ:** `<design>`  
- **Secrets:** `<where stored/how injected>`  
- **Egress policy:** `<offline by default or allowlist>`

**Tiered Security Controls:**  
- **MicroMVP**: Basic Session Mgmt  
- **Enterprise**: mTLS, Audit Logs, RBAC *(inactive in lower tiers)*

**Top 5 Risks (STRIDE)**  
- **Spoofing**: token theft via misconfigured proxy  
  → Mitigation: mTLS + short-lived tokens (5m)  
- **Tampering**: schema-less inserts  
  → Mitigation: DB RLS + JSON Schema validate on ingress  
- **Repudiation**: missing admin audit  
  → Mitigation: append-only audit log with hash chain  
- **Information disclosure**: verbose errors  
  → Mitigation: error classes with redaction policy  
- **DoS**: unbounded requests  
  → Mitigation: per-IP + per-token rate limits; circuit breakers

---

## 11. Telemetry & Observability

- **Logging:** `<structure, redaction rules>`  
- **Metrics:** `<key KPIs>`  
- **Tracing:** `<sampling>`

**Dashboards (Optional)** → ❌ If unused, delete this entire section before finalizing.  
Links to: latency, error rate, saturation, cost; all must exist before Go.

---

## 12. Acceptance & Verification

- **Verification target**: defined in `manifest.yaml` → `verification_target`  
- **Tests directory**: `tests/`  
- **Green criteria**: verification target passes on clean checkout.

**Test plan**  
- **Unit**: `<scope/coverage targets>`  
- **Integration**: `<scope>`  
- **e2e (Optional)**: ❌ Delete if unused.

### 12.1 Go/No-Go Checklist (automated)  
`make verify` MUST pass on a clean checkout:  
- [ ] Unit + integration + e2e tests: GREEN  
- [ ] Contract drift check: GREEN (`make contract-check`)  
- [ ] Security scans (SAST/DAST/deps/secrets): GREEN or waiver in §14  
- [ ] Spec lint (optional sections removed; overrides tested): GREEN  
- [ ] VRT (Visual Regression Tests): GREEN (if UI exists)

### 12.2 Tiered Testing Strategy

The Test Suite **MUST** respect the **Target Build Tier** declared in §1.

- **Active Tiers** (`≤ current tier`): All corresponding tests **MUST PASS** (exit code `0`).  
- **Dormant Tiers** (`> current tier`): All corresponding tests **MUST BE SKIPPED**, not executed.  
  - Implementation: Use runtime-configurable skip conditions (e.g., `@pytest.mark.skipif(config.TIER < 'enterprise', reason='dormant tier')`).  
  - Language-agnostic analogues required for non-Python stacks.

✦ **Constraint**:  
Tests for dormant tiers **MUST NOT** be deleted, commented out, or excluded from version control. They are **scaffolded assets**, not dead code, and must remain executable upon tier activation.

✦ **Verification**:  
The `make verify` command **MUST** complete without error **even in MicroMVP mode**, with dormant tests cleanly skipped (not failed or ignored).

---

## 13. Worker Constraints (This Project)

✦ **Critical**: These constraints are hard-stops. Violation = HALT.

- **Filesystem boundary**: Writes allowed ONLY under:  
  `./src/`  
  `./tests/`  
  `./docs/`  
  `./data/`  
- **Constraint**: No writes to root config files (e.g., `package.json`, `Cargo.toml`) without explicit prompt authorization.  
- **Network egress**: DENY by default.  
  **Allowlist**: `<List specific domains: e.g., api.stripe.com, pypi.org>`  
- **Shell execution**: Only via `tools/run.sh` wrapper (records argv + exit code).  
- **Ambiguity handling**: On unclear instruction → `HALT_WITH_CITATION` (link to § and line).

### 13.1 Reflexion Protocol (Anti-Looping)

If a task fails verification > 3 times:  
- STOP execution.  
- GENERATE `_logs/reflection.md` explaining why the previous attempts failed (e.g., "Incorrect assumption about API response format").  
- RE-PLAN using the insight from the reflection.  
→ Blind retries without reflection are forbidden.

---

## 14. Meta-Rules & Anti-Patterns

✦ Enforced by `.m4nd8/director.yaml` and Code Reviews

- **MR-01: No God Objects**  
  Classes/Files must have a single responsibility. `Manager` or `Util` suffixes are forbidden.  
- **MR-02: No Shotgun Surgery**  
  If a change requires editing >5 files, pause and refactor.  
- **MR-03: Anti-Slop**  
  UI components must map to tokens/design system. No raw hex codes.  
- **MR-04: Traceability**  
  Every code change → `cofo.md` Change Note.  
- **MR-05: Optional Hygiene**  
  Optional sections must be deleted if unused.  
- **MR-06: Ghost Protocol Compliance**  
  Code marked as `dormant` or `tier: enterprise` MUST NOT be deleted by Janitor if current tier is `micro_mvp`. It is dormant, not dead.

---

## 15. Sign-off

- **Author(s):** `<name(s)>`  
- **Date:** `<YYYY-MM-DD>`  
- **Reviewers:** `<name(s)>`  
- **Decision:** `<approved/changes required>`  
- **Links:** `<PRs, tickets, docs>`

---

**Appendix A — Fill-and-Ship Cards (delete in final)**  
✦ For spec authors learning the format. Must be deleted before final audit.  
- Story card w/ Gherkin stub  
- API card w/ JSON Schema skeleton  
- Runbook card template

**Automation Hooks (Reference — not part of spec body)**  
```makefile
setup:         ## Install toolchain, deps, hooks
verify: test contract-check spec-lint sec-scan
spec-lint:
	python3 tools/spec_lint.py spec.md
contract-check:
	tools/openapi_check.sh openapi.yaml tests/schemas/**
sec-scan:
	tools/scan.sh
```

`tools/spec_lint.py` (enforcer logic)
```python
import sys, re, pathlib
text = pathlib.Path("spec.md").read_text(encoding="utf-8")
fail = 0
if "(Optional)" in text:
    fail += 1
if re.search(r"^## .+\s*$", text, re.M):
    fail += 1  # empty heading
print("FAIL" if fail else "OK")
sys.exit(1 if fail else 0)
```
