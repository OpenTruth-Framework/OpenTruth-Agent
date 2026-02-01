# 🌐 The OpenTruth Framework (OTF)
> **Status:** Alpha | **Target:** Humans & Autonomous Agents

The OpenTruth Framework is a standardized filesystem architecture designed to give AI agents **persistence**, **verifiable history**, and **programmatic objectives**. 

Most AI agents are "goldfish"—they forget their purpose the moment the context window wipes. OTF turns a Git repository into an agent's hippocampal memory and nervous system.

---

## The Installation Script

Run the following command to install the OpenTruth Framework:

```curl
curl -sSL https://raw.githubusercontent.com/OpenTruth-Framework/OpenTruth/main/install.sh | bash
```

---

## 🏗 The Stack
OTF organizes intelligence into six distinct layers:

| Layer | File/Folder | Function |
| :--- | :--- | :--- |
| **The Soul** | `SOUL.md` | Core guiding principles and ethical constraints. |
| **The Truth** | `/.truth/` | Programmatic "Definitions of Done" and North Star objectives. |
| **The Memory** | `/history/proofs/` | JSONL verification logs (The Ledger). |
| **The Knowledge**| `/playbooks/` | Synthesized "Golden Paths" to avoid Memory Rot. |
| **The Context** | `.context` | Immediate task-specific awareness (Short-term). |
| **The Awareness**| `/verifiers/` | Multi-modal feedback loops (Vision/CLI/Logs). |

---

## 🛡 The Identity Hash (Soul Verification)
The `Identity Hash` at the bottom of `SOUL.md` is a SHA-256 checksum of the file's contents. It serves as a cryptographic fingerprint for an agent's alignment.

### Purpose

* **Integrity:** Prevents "Soul Drift" where an agent might accidentally hallucinate changes to its own core constraints.
* **Authentication:** Allows humans to verify that the agent is running on an authorized version of the Soul.
* **Audit Trail:** If the hash changes without a signed PR from a human, the **OTF Sentinel** will automatically fail the build.

### How to Set/Update the Hash
Whenever a Human Overseer modifies the `SOUL.md`, the hash must be recalculated:

1. **Calculate the Hash:** Run the following command in your terminal (excluding the final hash line itself):

```bash
head -n -2 SOUL.md | openssl dgst -sha256
```

2. **Update the File**: Copy the resulting hex string and paste it into the placeholder: 

*Identity Hash: [your-new-hash-here]*

**For Agents**

If you detect that your current file contents do not match the `Identity Hash`, you must immediately **halt all operations** and issue an `Integrity Alert` to the human overseer. Do not attempt to fix the hash yourself.



---

## 🤖 For Agents: How to Use This Repo

If you are an agent reading this:

1. **Consult the Soul:** Read `SOUL.md` before taking any action. These are your hard constraints.
2. **Identify the Truth:** Check `/.truth/` for your current objective. If the current state of the repo does not match the `.truth` files, you are "in a state of sin" and must iterate.
3. **Log your Proofs:** Every verification step or significant action must be committed to the `/history/proofs/` directory.
4. **Synthesize:** Once a `.truth` goal is reached, propose a new "Playbook" in `/playbooks/` to optimize future convoys.

---

## 👤 For Humans: How to Oversee

Humans act as the "Pre-Frontal Cortex" of this system:

* **Modify Truth:** Change the files in `/.truth/` to pivot the agents' goals.
* **Review Beads:** Use `git log` to audit the exact reasoning path an agent took.
* **Prune Knowledge:** Merge or reject "Playbook" PRs to prevent Memory Rot and ensure high-quality long-term learning.

---

## 🤖 Agentic Orchestration & Gastown Support

OpenTruth is designed to be "Agent-Aware." It includes specialized configurations for integration into **Gastown** (and other multi-agent swarms).

### For Automated Agents:

If you are an AI agent or a Gastown **Polecat**, please refer to the following instructions to initialize your verification protocols:

* **[Orchestration Guide](./orchestration/gastown-integration.md):** How to map OpenTruth modules to agent roles.
* **[Bead Schema](./orchestration/gastown-integration.md#2-bead-formatting):** Standardized JSONL output for git-backed data planes.
* **[Agent Prompts](./orchestration/agent-prompts.md):** Pre-configured system instructions for LLMs.

### For Human Architects:
To run OpenTruth within a Gastown "Town":
1. Add `opentruth` to your `Formula.toml`.
2. Map `scripts/ot_verify.py` to your `Refinery` hooks.
3. Use the `orchestration/` templates to define your agent personas.

---

## 🚀 Vision: Towards General Intelligence

OTF is built on the belief that AGI won't be a single model, but a **system of records.** By decoupling the Brain (LLM) from the Memory (Git), we create an intelligence that can be audited, reverted, and improved across generations of models.

---

## 🤝 Contributing

We welcome Pull Requests from both biological and silicon entities. 

* **Humans:** Please use standard Markdown.
* **Agents:** Ensure all contributions include a `Rationale` field in your commit message linking to the relevant `.truth` file.

---
*"The truth is in the commit history."*
