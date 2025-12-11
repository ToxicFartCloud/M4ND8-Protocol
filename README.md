```text
$$\      $$\ $$\   $$\ $$\   $$\ $$$$$$$\   $$$$$$\        $$$$$$$\
$$$\    $$$ |$$ |  $$ |$$$\  $$ |$$  __$$\ $$  __$$\       $$  __$$\
$$$$\  $$$$ |$$ |  $$ |$$$$\ $$ |$$ |  $$ |$$ /  $$ |      $$ |  $$ | $$$$$$\   $$$$$$\ 
$$\$$\$$ $$ |$$$$$$$$ |$$ $$\$$ |$$ |  $$ | $$$$$$  |      $$$$$$$  |$$  __$$\ $$  __$$\ 
$$ \$$$  $$ |\_____$$ |$$ \$$$$ |$$ |  $$ |$$  __$$<       $$  ____/ $$ |  \__|$$ /  $$ |
$$ |\$  /$$ |      $$ |$$ |\$$$ |$$ |  $$ |$$ /  $$ |      $$ |      $$ |      $$ |  $$ |
$$ | \_/ $$ |      $$ |$$ | \$$ |$$$$$$$  |\$$$$$$  |      $$ |      $$ |      \$$$$$$  |
\__|     \__|      \__|\__|  \__|\_______/  \______/       \__|      \__|       \______/
```

# **M4ND8 – The Autonomous Agent Control Plane (AACP)**

Hard Governance for the Agentic Era.  
From "Soft Policies" to "Control Systems Engineering."

## **⚡ QUICK START (READ THIS FIRST)**

**⚠️ Do not clone this entire repository into your project.**

This repository contains both the *Source* (Factory) and the *Distribution* (Product). To use the M4ND8 Protocol in your project, follow these steps:

1. **Download the Capsule:** Copy the [**.m4nd8**](https://www.google.com/search?q=./.m4nd8) folder from this repo into your project's root.  
2. **Install the Spec:** Copy [**spec\_template.md**](https://www.google.com/search?q=./spec_template.md) to your project's root, fill it out and rename it to spec.md.  
3. **Run:** Execute the sentinel.py script located inside .m4nd8/bin/ to begin the governance loop.

*(See [CONTRIBUTING.md](https://www.google.com/search?q=%23development--contributing) if you want to modify the protocol itself.)*

## **✅ WHAT IS M4ND8?**

**M4ND8** (formerly the Mandate Protocol) is a **Policy-Based Orchestration Framework** designed to enforce **deterministic outputs** from non-deterministic Large Language Models (LLMs). It shifts AI safety from "Soft Governance" (prompt engineering and guidelines) to **Hard Governance**—a discipline rooted in Control Systems Engineering.

Unlike chat-based Copilots, autonomous agents introduce "Task-Induced Hallucinations" (sycophancy, data fabrication, and silence on errors). M4ND8 v2.0 mitigates these risks using a **Defense-in-Depth architecture** that includes:

* **Logit-Level Observability:** Detecting uncertainty before text is generated.  
* **Intent-Based Gating:** Semantic firewalls preventing unauthorized actions.  
* **Cryptographic Provenance:** Guaranteeing the chain of custody for every token.

See the Video here: https://youtu.be/Y3GX7xLFnYU?si=oyyt_Rm0QNu0BM5K

## **🏛️ THE CORE ARCHITECTURE (Tripartite Control)**

The protocol replaces the previous "Branches of Government" metaphor with industry-standard systems engineering terminology to minimize cognitive load and maximize adoption in enterprise CI/CD pipelines.

| Artifact | Previous Name | New Industry-Standard Name | Function |
| :---- | :---- | :---- | :---- |
| spec.md (root) | Legislative | **Architectural Specification Contract** | Defines the explicit **Definition of Done**, functional requirements, and acceptance criteria; agents cannot invent features outside this contract. |
| ledger.md (root) | Executive | **Shared Context Ledger** | A persistent **Sovereign Blackboard** that records every decision and state change to prevent context drift and ensure Multi-Agent coordination. |
| .m4nd8/policy/compliance.yaml | Judicial | **Compliance Verification Engine** | Automated, **blocking quality assurance** that enforces a **Fail-Closed** policy. The supreme checklist for ship/no-ship. |

## **⚙️ THE 5 PILLARS (M.A.N.D.8)**

The underlying technological components have been professionalized to reflect specific security and performance functions.

### **M: Cognitive State Observability**

* **The Challenge:** Traditional logs capture *what* happened; AI monitoring must capture *uncertainty*.  
* **The Solution:** We do not rely on text output. We monitor raw probabilities using **Min-P Sampling** and **Semantic Entropy**.  
* **Mechanism:** If the model generates a financial figure with low probability (high uncertainty), the system triggers an immediate **Semantic Circuit Breaker**.

### **A: Intent-Based Access Control**

* **The Challenge:** "Data Leakage" via RAG, where an agent summarizes private data it technically has permission to read.  
* **The Solution:** A **Semantic Firewall** using **NeMo Guardrails**.  
* **Mechanism:** Even if the user has clearance, if the *intent* of the prompt is sycophantic or malicious, the **Input Rail** blocks the interaction.

### **N: Cryptographic Provenance Chain**

* **The Challenge:** Proving that an AI output is based on real data and not "Imputation Hallucination" (fabricating data to fill a schema).  
* **The Solution:** **C2PA Provenance** \+ **Statistical Watermarking**.  
* **Mechanism:** Every asset contains a cryptographically signed Manifest Store binding the output to the specific hash of the source document.

### **D: Confidential Compute Layer**

* **The Challenge:** Utilizing cloud-scale intelligence without exposing sensitive IP or PII.  
* **The Solution:** **Trusted Execution Environments (TEEs)** (e.g., NVIDIA H100 Confidential Compute).  
* **Mechanism:** Data is encrypted in RAM and during computation. **Influence Functions** (EK-FAC) audit weights to ensure private data isn't retained.

### **8: Self-Correcting Verification Loop**

* **The Challenge:** Preventing "Sycophancy" (agreement \> truth).  
* **The Solution:** **Chain of Verification (CoVe)** \+ **Reinforcement Learning from Knowledge Feedback (RLKF)**.  
* **Mechanism:** The agent separates "Drafting" from "Verifying." It generates checking questions (e.g., "Verify $5M revenue") and executes them against the **Shared Context Ledger** before finalizing output.

## **🔄 STANDARD OPERATING PROCEDURE (SOP)**

### **1\. Context & Authorization**

* **Load:** director.yaml (Policies) → manifest.yaml (Capabilities) → ledger.md (State).  
* **Gate:** NeMo Guardrails scan input for malicious intent.

### **2\. Planning: Tree of Thoughts (ToT)**

* **Role:** **Architect Agent**.  
* **Action:** Instead of linear planning, the agent utilizes **Tree of Thoughts** reasoning to explore multiple architectural paths before committing.  
* **Output:** A finalized plan written to the **Shared Context Ledger**.

### **3\. Implementation: Test-First Discipline**

* **Role:** **Builder Agent**.  
* **Mandate:** **Test-First Implementation Discipline**.  
  1. **RED:** Write a failing test first to provide ground truth.  
  2. **GREEN:** Write minimal code to pass.  
  3. **REFACTOR:** Clean technical debt.  
* **Security:** All code execution must occur in an **ephemeral, network-isolated Sandbox** (e.g., E2B or Daytona).

### **4\. Verification: Property-Based Testing (PBT)**

* **Role:** **Tester Agent**.  
* **Upgrade:** The agent must generate **Property-Based Tests** (e.g., Hypothesis) to validate general correctness against edge cases.  
* **Reflexion:** If verification fails \> 2 times, the **Error Metacognition Loop** triggers a mandatory STOP and re-plan.

## **🛡️ THREAT MODEL & MITIGATIONS**

| Threat | Description | M4ND8 v2.0 Mitigation |
| :---- | :---- | :---- |
| **Social Sycophancy** | User pressures Agent to validate illicit strategies. | **Input Rails** detect coercive patterns. |
| **Imputation Hallucination** | Agent fabricates financial line items to satisfy a JSON schema. | **Min-P Sampling** detects low probability of fabricated numbers. |
| **Liability Evasion** | Operator claims an AI error was human-generated. | **Statistical Watermarking** embeds invisible signals. |
| **Context Drift** | Agents lose track of project state across long sessions. | **Shared Context Ledger** (ledger.md) acts as the single source of truth. |

## **🏗️ DEVELOPMENT & CONTRIBUTING**

**For Protocol Developers Only:**

The root directory of this repository represents the "Factory" environment where the protocol is built and tested.

* liveness\_checker.py, sentinel.py: The source code for the harness.  
* .m4nd8/: The distribution capsule (The Product).

If you make changes to the root files, run bash pack\_protocol.sh to update the .m4nd8 distribution folder before committing.

*Built with the M4ND8 Protocol.*
