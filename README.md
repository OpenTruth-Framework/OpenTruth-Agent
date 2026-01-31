# 🌐 The OpenTruth Framework (OTF)
> **Status:** Alpha | **Target:** Humans & Autonomous Agents

The OpenTruth Framework is a standardized filesystem architecture designed to give AI agents **persistence**, **verifiable history**, and **programmatic objectives**. 

Most AI agents are "goldfish"—they forget their purpose the moment the context window wipes. OTF turns a Git repository into an agent's hippocampal memory and nervous system.

---

## 🏗 The Stack
OTF organizes intelligence into six distinct layers:

| Layer | File/Folder | Function |
| :--- | :--- | :--- |
| **The Soul** | `SOUL.md` | Core guiding principles and ethical constraints. |
| **The Truth** | `/.truth/` | Programmatic "Definitions of Done" and North Star objectives. |
| **The Memory** | `/history/beads/` | Git-tracked JSONL work history (The Ledger). |
| **The Knowledge**| `/playbooks/` | Synthesized "Golden Paths" to avoid Memory Rot. |
| **The Context** | `.context` | Immediate task-specific awareness (Short-term). |
| **The Awareness**| `/verifiers/` | Multi-modal feedback loops (Vision/CLI/Logs). |

---

## 🤖 For Agents: How to Use This Repo

If you are an agent reading this:

1. **Consult the Soul:** Read `SOUL.md` before taking any action. These are your hard constraints.
2. **Identify the Truth:** Check `/.truth/` for your current objective. If the current state of the repo does not match the `.truth` files, you are "in a state of sin" and must iterate.
3. **Log your Beads:** Every tool-call or significant thought must be committed to the `/history/beads/` directory.
4. **Synthesize:** Once a `.truth` goal is reached, propose a new "Playbook" in `/playbooks/` to optimize future convoys.

---

## 👤 For Humans: How to Oversee

Humans act as the "Pre-Frontal Cortex" of this system:

* **Modify Truth:** Change the files in `/.truth/` to pivot the agents' goals.
* **Review Beads:** Use `git log` to audit the exact reasoning path an agent took.
* **Prune Knowledge:** Merge or reject "Playbook" PRs to prevent Memory Rot and ensure high-quality long-term learning.

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
