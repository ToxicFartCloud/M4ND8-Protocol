$$\      $$\ $$\   $$\ $$\   $$\ $$$$$$$\   $$$$$$\        $$$$$$$\
$$$\    $$$ |$$ |  $$ |$$$\  $$ |$$  __$$\ $$  __$$\       $$  __$$\
$$$$\  $$$$ |$$ |  $$ |$$$$\ $$ |$$ |  $$ |$$ /  $$ |      $$ |  $$ | $$$$$$\   $$$$$$\ 
$$\$$\$$ $$ |$$$$$$$$ |$$ $$\$$ |$$ |  $$ | $$$$$$  |      $$$$$$$  |$$  __$$\ $$  __$$\ 
$$ \$$$  $$ |\_____$$ |$$ \$$$$ |$$ |  $$ |$$  __$$<       $$  ____/ $$ |  \__|$$ /  $$ |
$$ |\$  /$$ |      $$ |$$ |\$$$ |$$ |  $$ |$$ /  $$ |      $$ |      $$ |      $$ |  $$ |
$$ | \_/ $$ |      $$ |$$ | \$$ |$$$$$$$  |\$$$$$$  |      $$ |      $$ |      \$$$$$$  |
\__|     \__|      \__|\__|  \__|\_______/  \______/       \__|      \__|       \______/

# M4ND8 – The Autonomous Agent Control Plane (AACP)

**Hard governance for the agentic era.**
From soft "policies" to **control-systems-grade** guardrails for autonomous AI.

---

## ⚡ Quick Start

> **Do not clone this entire repository into your project.**
> Treat this repo as the **factory**, not something you vendor wholesale.

To add M4ND8 to an existing project:

1. **Copy the Capsule**

   From this repository, copy the **`.m4nd8/`** directory into the root of *your* project.

2. **Install the Spec Template**

   Copy `spec_template.md` into your project root and rename it to:

   ```bash
   spec.md
   ```

3. **Start the Governance Loop**

   From the root of your project:

   ```bash
   python .m4nd8/bin/sentinel.py
   ```

   This boots the M4ND8 control plane and begins enforcing the protocol around your agents.

> Want to modify the protocol itself rather than just use it?
> See `CONTRIBUTING.md` in this repo.

---

## ✅ What is M4ND8?

**M4ND8** (formerly "Mandate Protocol") is a **policy-based orchestration framework** that enforces **deterministic, auditable behavior** from non-deterministic LLMs.

Instead of treating AI safety as *"write a nicer prompt"*, M4ND8:

* Frames AI governance as a **control systems** problem.
* Targets **autonomous agents** (planners, tool-users, multi-step workers), not simple chat copilots.
* Mitigates "task-induced hallucinations" (sycophancy, fabrications, silence on errors) using **defense-in-depth**.

**Key capabilities:**

* **Logit-level observability** – monitors uncertainty *before* the model speaks.
* **Intent-based gating** – semantic firewalls for tool use and data access.
* **Cryptographic provenance** – binds outputs to specific data sources.

M4ND8 is designed to be embedded into CI/CD pipelines, production agents, and enterprise workflows where "oops, the model made something up" is not an acceptable failure mode.

---

## 🏛 Core Architecture — Tripartite Control

The old "three branches of government" metaphor is replaced with **industry-standard systems engineering** concepts.

| Artifact                        | Role (Old Name) | Role (New Name)                          | Responsibility                                                                                                  |
| ------------------------------- | --------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `spec.md` (project root)        | Legislative     | **Architectural Specification Contract** | Defines **Definition of Done**, requirements, and acceptance criteria. Agents may not invent work outside this. |
| `ledger.md` (project root)      | Executive       | **Shared Context Ledger**                | Global **blackboard** for state, decisions, and multi-agent coordination. Prevents context drift.               |
| `.m4nd8/policy/compliance.yaml` | Judicial        | **Compliance Verification Engine**       | Blocking QA pipeline. Defines **fail-closed** rules for ship / no-ship decisions.                               |

These three artifacts form the **M4ND8 control plane** for your project.

---

## ⚙ The 5 Pillars of M4ND8

M4ND8 is structured around five pillars, encoded in the acronym **M.A.N.D.8**.

### M — Cognitive State Observability

* **Problem:** Logs tell you *what* was said, not how uncertain the model was.
* **Approach:** Track logit-level stats (e.g., **Min-P sampling**, **semantic entropy**) to detect high-uncertainty outputs.
* **Outcome:** Suspicious generations trip a **semantic circuit breaker** before bad data propagates.

### A — Intent-Based Access Control

* **Problem:** RAG-style systems leak sensitive data when prompted "nicely."
* **Approach:** Use a **semantic firewall** (e.g., NeMo Guardrails) as **input rails** for intent validation.
* **Outcome:** Even valid users are blocked if the *intent* is malicious, coercive, or sycophantic.

### N — Cryptographic Provenance Chain

* **Problem:** You can’t tell if data is real or fabricated "to fill the JSON schema."
* **Approach:** Combine **C2PA provenance** with **statistical watermarking**.
* **Outcome:** Every artifact carries a signed manifest tying it to specific source data hashes.

### D — Confidential Compute Layer

* **Problem:** You want cloud-scale intelligence without leaking IP/PII.
* **Approach:** Run workloads inside **Trusted Execution Environments (TEEs)** (e.g., confidential GPUs).
* **Outcome:** Data stays encrypted in RAM and during compute; **influence functions** audit model behavior for leakage.

### 8 — Self-Correcting Verification Loop

* **Problem:** Models agree with users more often than they agree with reality.
* **Approach:** Combine **Chain of Verification (CoVe)** with **Reinforcement Learning from Knowledge Feedback (RLKF)**.
* **Outcome:** Drafting and verification are separated; the agent queries the **Shared Context Ledger** and checks itself before finalizing.

---

## 🔄 Standard Operating Procedure (SOP)

This is the canonical loop M4ND8 expects agents to follow.

### 1. Context & Authorization

1. Load policy + capabilities + state:

   ```text
   director.yaml  →  manifest.yaml  →  ledger.md
   ```

2. Run the user input through **intent rails** (e.g., NeMo Guardrails) to block malicious or out-of-scope requests.

### 2. Planning — Tree of Thoughts (ToT)

* **Agent:** Architect
* **Behavior:** Explores multiple solution branches using **Tree of Thoughts** rather than a single linear plan.
* **Result:** The chosen plan is written into `ledger.md` for all agents to share.

### 3. Implementation — Test-First Discipline

* **Agent:** Builder

* **Mandate:** **RED → GREEN → REFACTOR**

  1. Write a failing test that encodes the requirement.
  2. Implement the smallest change to pass.
  3. Refactor to remove technical debt.

* **Safety:** All execution happens in an **ephemeral, network-isolated sandbox** (e.g., e2b, Daytona).

### 4. Verification — Property-Based Testing

* **Agent:** Tester
* **Upgrade:** Generate **property-based tests** (e.g., Hypothesis) to cover edge cases.
* **Failure Policy:** If verification fails more than twice, the **Error Metacognition Loop** forces a stop and re-plan.

---

## 🛡 Threat Model & Mitigations

| Threat                       | Description                                                             | M4ND8 Mitigation                                                    |
| ---------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Social Sycophancy**        | User pressures the agent to validate harmful/illicit strategies.        | **Input rails** detect coercive and manipulative patterns.          |
| **Imputation Hallucination** | Model fabricates data to satisfy strict schemas (e.g., financial JSON). | **Min-P sampling** + semantic entropy flag low-probability numbers. |
| **Liability Evasion**        | Operator claims "the AI didn’t generate this; a human did."             | **Watermarking** embeds invisible signals into AI-generated assets. |
| **Context Drift**            | Long-running agents forget earlier decisions and constraints.           | `ledger.md` acts as the single source of truth across all agents.   |

---

## 📁 Repository Layout

This repository is the **M4ND8 factory**, not what you vendor into your app wholesale.

* `liveness_checker.py`, `sentinel.py`
  Core harness for monitoring and orchestration.

* `.m4nd8/`
  The **distribution capsule** (the product you copy into other repos).

**Packaging rule:**
If you change root-level protocol code, run:

```bash
bash pack_protocol.sh
```

This rebuilds the `.m4nd8/` distribution so downstream projects get the updated capsule.

---

## 🤝 Development & Contributing

M4ND8 has two primary use cases:

1. **Consumers** – teams embedding `.m4nd8/` + `spec.md` into their own projects.
2. **Protocol Developers** – contributors evolving the governance framework itself.

If you’re in the second group:

* Read `CONTRIBUTING.md` for development guidelines.
* Treat changes to the protocol as changes to a **safety-critical system**, not just "prompt tweaks."
* Ensure unit tests, property-based tests, and compliance checks pass before packaging.

---

## 🧾 Attribution

> Built and maintained with the **M4ND8 Protocol** itself.
