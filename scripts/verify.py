#!/usr/bin/env python3
import json
import datetime
import os
import sys

# Configuration
PROOFS_DIR = os.path.abspath("history/proofs")
SOUL_PATH = "SOUL.md"

def log_proof(action, status, details):
    """Writes a proof bead to history."""
    proof = {
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
        "agent": "OpenTruth-Agent",
        "action": action,
        "status": status,
        "details": details
    }
    
    os.makedirs(PROOFS_DIR, exist_ok=True)
    proof_file = os.path.join(PROOFS_DIR, "self_verification.jsonl")
    
    with open(proof_file, "a") as f:
        f.write(json.dumps(proof) + "\n")
    
    print(f"📝 Proof logged: {action} -> {status}")

def verify_self():
    """
    Self-Verification Routine.
    Checks for the existence of the Soul and Truth.
    """
    print("🧘 Verifying Self...")
    
    findings = {
        "has_soul": os.path.exists(SOUL_PATH),
        "has_truth_dir": os.path.isdir(".truth"),
        "has_proofs_dir": os.path.isdir(PROOFS_DIR)
    }
    
    is_valid = findings["has_soul"]
    
    if not is_valid:
        print("❌ Soul Missing! I am lost.")
    else:
        print("✅ Soul Found.")
        
    status = "success" if is_valid else "failure"
    log_proof("verify_self", status, findings)
    return is_valid

if __name__ == "__main__":
    success = verify_self()
    if not success:
        sys.exit(1)
