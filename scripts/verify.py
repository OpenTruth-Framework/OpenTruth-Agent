#!/usr/bin/env python3
"""
OpenTruth Self-Verification Script
----------------------------------
This script is the "Mirror" for an autonomous agent. It allows the agent to 
look at its own file system and verify that its essential components (Soul, Truth, Memory)
are intact and operational.

Usage:
    ./scripts/verify.py

Exit Codes:
    0: Verification Successful (The agent is healthy)
    1: Verification Failed (Critical components are missing)
"""

import json      # Standard library for handling JSON data (used for logging proofs)
import datetime  # Standard library for generating timestamps
import os        # Standard library for file system operations (checking paths, making directories)
import sys       # Standard library for system-specific parameters and functions (exit codes)

# --- Configuration Constants ---
# PROOFS_DIR: The directory where verification logs (The Ledger) are stored.
# We use absolute paths to ensure we verify the correct location regardless of where the script is run from.
PROOFS_DIR = os.path.abspath("history/proofs")

# SOUL_PATH: The relative path to the Soul file, which contains the agent's core instructions.
SOUL_PATH = "SOUL.md"

def log_proof(action, status, details):
    """
    Writes a 'Proof' (a structured log entry) to the agent's history.
    
    This function ensures that every verification attempt is recorded in the 
    'history/proofs/' ledger. This traceability is a core tenet of the OpenTruth Framework.

    Args:
        action (str): The name of the action being verified (e.g., "verify_self").
        status (str): The outcome of the verification ("success" or "failure").
        details (dict): A dictionary of specific findings (e.g., {"has_soul": True}).
    """
    # Create the timestamp in UTC ISO 8601 format (e.g., "2023-10-27T10:00:00+00:00")
    # This ensures a standardized time format for all logs.
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()

    # Construct the Proof object
    proof = {
        "timestamp": timestamp,
        "agent": "OpenTruth-Agent", # Hardcoded identity since this is the single-player agent
        "action": action,
        "status": status,
        "details": details
    }
    
    # Ensure the directory exists before trying to write to it.
    # exist_ok=True prevents an error if the directory already exists.
    os.makedirs(PROOFS_DIR, exist_ok=True)
    
    # Define the log file path. We use a specific file for self-verification logs.
    proof_file = os.path.join(PROOFS_DIR, "self_verification.jsonl")
    
    # Append the proof to the JSONL file.
    # 'a' mode opens the file for appending.
    with open(proof_file, "a") as f:
        f.write(json.dumps(proof) + "\n")
    
    # Print a user-friendly message to the console
    print(f"📝 Proof logged: {action} -> {status}")

def verify_self():
    """
    The Core Self-Verification Routine.
    
    This function performs a series of checks to ensure the agent's environment is healthy.
    Current Checks:
    1. Soul Existence: Is 'SOUL.md' present? (The Agent's Conscience)
    2. Truth Directory: Is '.truth/' present? (The Agent's Goals)
    3. Proofs Directory: Is 'history/proofs/' present? (The Agent's Memory)

    Returns:
        bool: True if all critical checks pass, False otherwise.
    """
    print("🧘 Verifying Self...")
    
    # Dictionary to store the results of individual checks
    findings = {
        "has_soul": os.path.exists(SOUL_PATH),          # Check 1: Does the Soul exist?
        "has_truth_dir": os.path.isdir(".truth"),       # Check 2: Does the Truth directory exist?
        "has_proofs_dir": os.path.isdir(PROOFS_DIR)     # Check 3: Does the Proofs directory exist?
    }
    
    # Determine overall validity.
    # For now, the ONLY critical failure condition is missing the Soul.
    # Missing Truth or Proofs directories might just mean a fresh install, which is recoverable.
    is_valid = findings["has_soul"]
    
    if not is_valid:
        print("❌ Soul Missing! I am lost. (SOUL.md not found in root)")
    else:
        print("✅ Soul Found. I know who I am.")
        
    # Map boolean result to string status for logging
    status = "success" if is_valid else "failure"
    
    # Log the result of this introspection
    log_proof("verify_self", status, findings)
    
    return is_valid

# --- Entry Point ---
# This block runs only when the script is executed directly (not imported as a module).
if __name__ == "__main__":
    success = verify_self()
    
    # Exit with code 0 for success, 1 for failure.
    # This allows external tools (CI/CD, Gastown) to know if the check passed.
    if not success:
        sys.exit(1)
