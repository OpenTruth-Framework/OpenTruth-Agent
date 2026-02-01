# Gastown Agent Integration Guide

This document defines how Gastown agents (Polecats, Witnesses, and Refineries) should utilize the OpenTruth Framework.

## 1. Additional Agent Roles

- **The Spotter (OpenTruth Specialist):** Responsible for executing `opentruth` CLI commands and converting outputs into Gastown Beads.
- **The Witness (Auditor):** Compares Agent outputs against OpenTruth provenance scores. If a score falls below 0.7, the Witness must trigger a `gt sling` to a Refinery.

## 2. Bead Formatting

Agents MUST encapsulate OpenTruth findings in a JSONL bead format:
{
  "timestamp": "ISO-8601",
  "agent_id": "polecat-01",
  "action": "verify_claim",
  "ot_score": 0.92,
  "ot_provenance_chain": ["link1", "link2"],
  "status": "verified"
}

## 3. Tool Hooks

Integration should be handled via Gastown Hooks. Before any `git commit` in the data plane:

1. Trigger `scripts/ot_verify.py` on the staged content.
2. If OpenTruth returns a high "Adversarial Risk," the commit is aborted.

### Command Line Usage for Agents

Agents should use the following syntax to communicate with the OpenTruth engine:

| Action | Command |
| :--- | :--- |
| **Verify Claim** | `python opentruth_cli.py verify "claim string" --bead` |
| **Audit File** | `python opentruth_cli.py scan path/to/file.png --bead` |
| **Compare Sources** | `python opentruth_cli.py cross-ref url1 url2 --bead` |

**Note:** Always use the `--bead` flag when running within a Gastown Convoy to ensure the output is properly piped into the data plane.