# M4ND8 Protocol Refactor Plan: Factory/Distribution Architecture
**Version:** 1.0.0
**Date:** 2025-12-24
**Status:** DRAFT - PENDING AUTHORIZATION
**Analyst:** M4ND8 Systems Analyst (Compiler Persona)

---

## ⚠️ EXECUTION WARNING
**DO NOT EXECUTE THIS PLAN WITHOUT EXPLICIT AUTHORIZATION.**
This plan involves significant structural changes to the M4ND8 Protocol repository. All operations must be verified against the backup artifacts before commitment.

---

## 1. Executive Summary

This Refactor Plan aligns the M4ND8 Protocol repository with a strict **Factory/Distribution** architectural model.

*   **The Factory (`/factory`)**: The volatile, active development environment where the protocol is engineered. All "Source" files (policies, tools, templates) reside here.
*   **The Distribution (`/.m4nd8`)**: The stable, certified product artifact intended for deployment into consumer repositories. This directory is treated as a "Build Artifact" of the Factory.
*   **The Root (`/`)**: A clean entry point containing only high-level documentation, the Factory, the Distribution, and the Orchestration scripts (`pack_protocol.sh`).

This separation enforces the **Three Unbreakable Mandates** by ensuring that only "Certified" (built and verified) components enter the `.m4nd8` distribution, eliminating "Instruction Bleed" and "Ghost Connections" caused by root-level clutter.

## 2. Pre-Execution Safety Checklist

Before initiating any phase, the following safety checks must be performed:

- [ ] **Snapshot**: Create a full tarball backup of the current directory.
  ```bash
  tar -czf .backup_pre_refactor_$(date +%s).tar.gz . --exclude=.git
  ```
- [ ] **Git Status**: Ensure the working directory is clean.
- [ ] **Checksum Baseline**: Generate SHA256 checksums for all existing `.m4nd8/` files to ensure zero unintentional mutation during the move.
- [ ] **Tree Validation**: Verify current structure matches `tree.txt`.

## 3. Phase 1: Dependency Checker Integration

**Objective**: Establish the `.m4nd8/data/approved_dependencies.db` as the Sovereign Source of Truth for dependency governance and ensure tools are correctly distributed.

### 3.1 Operations
1.  **Centralize Data**:
    *   Ensure `data/approved_dependencies.db` is canonical.
    *   Plan move: `data/` -> `factory/data/`.
    *   Plan sync: `factory/data/approved_dependencies.db` -> `.m4nd8/data/approved_dependencies.db`.

2.  **Tool Standardization**:
    *   Target: `update_adb.py` (Root) and `tools/update_dependency_index.py`.
    *   Action: Consolidate dependency management scripts into `factory/tools/dependency_manager/`.
    *   Distribution: Copy runtime-required tools (e.g., `check_dependencies.py` wrapper) to `.m4nd8/tools/`.

3.  **Compliance Integration**:
    *   Update `policy/compliance.yaml` (to be moved to `factory/kernel/guardrails/`) to explicitly verify the hash of `.m4nd8/data/approved_dependencies.db`.

### 3.2 Rollback Procedure
*   Restore `data/` and `tools/` from the pre-execution backup.
*   Revert `compliance.yaml` changes.

## 4. Phase 2: Structural Optimization (The Factory Migration)

**Objective**: Clear the root directory of "Monolithic Rigidity" by moving development assets into `factory/` and defining the Distribution Manifest.

### 4.1 Target Directory Structure

```text
/
├── factory/                 # DEVELOPMENT SOURCE (The "Factory")
│   ├── kernel/              # Identity & Law (director.yaml, manifesto.md)
│   ├── runtime/             # Execution logic (bin/, tools/)
│   ├── interface/           # Templates & Docs (templates/, docs/)
│   └── source_policies/     # Raw Policy definitions (policies/, policy/)
│
├── .m4nd8/                  # CERTIFIED PRODUCT (The "Distribution")
│   ├── MANIFEST             # New file: Checksum list of all distro files
│   ├── director.yaml
│   ├── policy/              # Compiled/Copied policies
│   ├── tools/               # Runtime tools
│   └── data/                # Reference Data
│
├── pack_protocol.sh         # Script to Sync Factory -> .m4nd8
├── refactor_plan.md         # This Document
├── README.md
└── LICENSE
```

### 4.2 Migration Steps
1.  **Create Factory Scaffold**:
    ```bash
    mkdir -p factory/{kernel,runtime,interface,source_policies}
    ```
2.  **Relocate Root Assets**:
    *   `director.yaml`, `manifesto.md`, `M4ND8_handbook.md` -> `factory/kernel/`
    *   `bin/`, `tools/` -> `factory/runtime/`
    *   `templates/`, `onboarding*`, `spec_template.md` -> `factory/interface/`
    *   `policy/`, `policies/` -> `factory/source_policies/`
3.  **Eliminate Root Redundancy**:
    *   Remove root-level copies of folders *after* verifying they exist in `factory/` and have a build path to `.m4nd8/`.
4.  **Create Manifest**:
    *   Generate `.m4nd8/MANIFEST` listing every file in the distribution folder with its SHA256 hash.

### 4.3 `pack_protocol.sh` Specification
A new script `pack_protocol.sh` will be created to:
1.  Read `factory/`.
2.  Run tests/verification.
3.  Copy certified artifacts to `.m4nd8/`.
4.  Update `.m4nd8/MANIFEST`.

### 4.4 Rollback Procedure
*   Expand the pre-execution tarball to restore the original root structure.

## 5. Phase 3: Safety & Documentation

**Objective**: Ensure the new structure is documented and protected against regression.

### 5.1 Documentation
*   Update `README.md` to explain the Factory/Distribution model.
*   Update `factory/kernel/M4ND8_handbook.md` to reflect the new paths.

### 5.2 Automation
*   **Backup Script**: Create `factory/runtime/bin/backup_protocol.sh`.
*   **Pre-commit Hook**: Create a git hook that prevents committing changes to `.m4nd8/` directly (forcing changes to go through `factory/` + `pack_protocol.sh`).

## 6. Authorization Request

**Current Status**: Plan Generated.
**Next Action**: Waiting for user approval to begin **Phase 1: Dependency Checker Integration**.

> "Prompts are fickle; Structure is reliable."

---
*End of Refactor Plan*
