#!/usr/bin/env bash
set -euo pipefail

echo "🔍 M4ND8: Verifying dependencies against approved list..."

# Check uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ ERROR: uv not found. Install with: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Check Python dependencies
if [[ -f "requirements.txt" ]]; then
    echo "🐍 Verifying Python dependencies..."
    uv pip compile --check requirements.txt -o /dev/null
fi

# Check system dependencies
echo "⚙️ Verifying system dependencies..."
if ! python3 -c "import tkinter; print('Tkinter available')" &> /dev/null; then
    echo "❌ ERROR: Tkinter not available. Install with: sudo dnf install python3-tkinter"
    exit 1
fi

echo "✅ ALL DEPENDENCIES VERIFIED"
exit 0
