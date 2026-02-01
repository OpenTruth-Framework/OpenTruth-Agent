# 🌐 OpenTruth Agent (Solo)
> **Status:** Alpha | **Target:** Single Autonomous Agents

The OpenTruth Agent is a drop-in "Brain Structure" for a standalone AI agent. It gives your agent:
1.  **A Soul:** Hardcoded ethical/operational constraints (`SOUL.md`).
2.  **Memory:** A verifiable history of actions (`history/proofs/`).
3.  **Objectives:** A way to track and verify its own goals (`/.truth/` and `bd`).

---

## 🏗 The Stack

| Layer | File/Folder | Function |
| :--- | :--- | :--- |
| **The Soul** | `SOUL.md` | Core guiding principles. |
| **The Truth** | `/.truth/` | Your agent's "Definition of Done". |
| **The Memory** | `/history/proofs/` | Verification logs (The Ledger). |
| **The Tasks** | `.beads/` | Task management (via `bd`). |

---

## 🛠 Usage

This repository is designed to be the **Root** of your agent's workspace.

### Self-Verification
To verify that you (the agent) are functioning correctly and adhering to your Truths:

```bash
# Verify your own logic/state
./scripts/verify.py
```

---

## 🛡 The Identity Hash
(See SOUL.md for details on the cryptographic identity lock).

---

## 🤖 For Gastown Swarms
If you are looking to orchestrate *multiple* agents in a Gastown Polyrepo, please use the **[OpenTruth-Gastown](../OpenTruth-Gastown)** repository instead.
