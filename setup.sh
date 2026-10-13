#!/usr/bin/env bash
# .pi/setup.sh - Setup learning environment in the current workspace
set -euo pipefail

TARGET_DIR="$(pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 Setting up AI Learning Environment in: $TARGET_DIR"

# 1. Symlink root instruction files
if [ -f "$SCRIPT_DIR/AGENTS.md" ]; then
  ln -sf .pi/AGENTS.md "$TARGET_DIR/AGENTS.md"
  echo "✔ Symlinked AGENTS.md -> .pi/AGENTS.md"
fi

if [ -f "$SCRIPT_DIR/GEMINI.md" ]; then
  ln -sf .pi/GEMINI.md "$TARGET_DIR/GEMINI.md"
  echo "✔ Symlinked GEMINI.md -> .pi/GEMINI.md"
fi

# 2. Setup .agents directory for Antigravity & Gemini CLI
mkdir -p "$TARGET_DIR/.agents/rules"

# Symlink skills directory
ln -sfn ../.pi/skills "$TARGET_DIR/.agents/skills"
echo "✔ Symlinked .agents/skills -> ../.pi/skills"

# Symlink agent rules
if [ -f "$SCRIPT_DIR/.agents/rules/agents.md" ]; then
  ln -sf ../../.pi/.agents/rules/agents.md "$TARGET_DIR/.agents/rules/agents.md"
  echo "✔ Symlinked .agents/rules/agents.md"
fi

# Write .agents/skills.json
cat << 'EOF' > "$TARGET_DIR/.agents/skills.json"
{
  "entries": [
    {
      "path": ".pi/skills"
    }
  ]
}
EOF
echo "✔ Configured .agents/skills.json"

# 3. Initialize learn_log.md if not present
if [ ! -f "$TARGET_DIR/learn_log.md" ]; then
  cat << 'EOF' > "$TARGET_DIR/learn_log.md"
# Study Log

Running session log for learning nodes, dependency maps, and quiz checks.
EOF
  echo "✔ Initialized learn_log.md"
fi

# 4. Exclude personal learning files from project git status
if [ -d "$TARGET_DIR/.git" ]; then
  EXCLUDE_FILE="$TARGET_DIR/.git/info/exclude"
  mkdir -p "$(dirname "$EXCLUDE_FILE")"
  touch "$EXCLUDE_FILE"

  ITEMS=(".pi" ".agents" "AGENTS.md" "GEMINI.md" "learn_log.md" "viz/")
  for item in "${ITEMS[@]}"; do
    if ! grep -Fxq "$item" "$EXCLUDE_FILE" 2>/dev/null; then
      echo "$item" >> "$EXCLUDE_FILE"
    fi
  done
  echo "✔ Added learning files to local .git/info/exclude (git status is clean)"
fi

echo "✨ All set! Antigravity & Gemini are ready with your learning skills and agents."
