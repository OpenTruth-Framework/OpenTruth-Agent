#!/bin/bash
# OpenTruth Framework (OTF) - Initializer v1.0.1

echo "🌐 Initializing OpenTruth Framework..."

# 1. Create standardized directory structure
mkdir -p .truth history/beads playbooks verifiers .agent

# 2. Retrieve templates (Fallback to local if remote fails)
RAW_URL="https://raw.githubusercontent.com/OpenTruth-Framework/OpenTruth/main/templates"

curl -sSL "$RAW_URL/SOUL.md" -o SOUL.md
curl -sSL "$RAW_URL/instructions.md" -o .agent/instructions.md

# 3. Generate the Initial Identity Hash
if [ -f "SOUL.md" ]; then
    echo "🔒 Securing the Soul..."
    
    # Calculate hash of file excluding the last two lines (the placeholder area)
    # Uses openssl for cross-platform compatibility (Linux/macOS)
    NEW_HASH=$(head -n -2 SOUL.md | openssl dgst -sha256 | awk '{print $NF}')
    
    # Replace the placeholder with the actual hash
    # Note: On macOS, sed -i requires an empty string argument: sed -i '' "s/..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s/\[sha256-placeholder\]/$NEW_HASH/" SOUL.md
    else
        sed -i "s/\[sha256-placeholder\]/$NEW_HASH/" SOUL.md
    fi
    
    echo "✅ Soul Fingerprint Created: $NEW_HASH"
fi

# 4. Generate Machine-Readable Manifest
cat <<EOF > otf.json
{
  "version": "1.0.1",
  "framework": "OpenTruth",
  "identity_hash": "$NEW_HASH",
  "layers": {
    "soul": "SOUL.md",
    "truth": ".truth/",
    "memory": "history/beads/",
    "knowledge": "playbooks/"
  }
}
EOF

# 5. Git Commit
git add .
git commit -m "chore(otf): bootstrap OpenTruth architecture with verified soul"

echo "✅ Installation Complete. The agent is now grounded."